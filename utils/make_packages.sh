#!/bin/bash
DIR=$(cd `dirname $0` && pwd)
PYROPATH=$(cd `dirname $0` && cd .. && pwd)

# Install build dependencies (if needed)
if [ ! -f /usr/bin/debuild ];
then
    sudo apt-get install devscripts equivs python-setuptools dh-python
fi
if [ ! -f /usr/bin/rpm ];
then
    sudo apt-get install rpm
fi
if [ ! -f /usr/lib/python3/dist-packages/sphinxarg/ext.py ];
then
    sudo apt install python3-sphinx-argparse
fi

# Update pyromaths version
VERSION=`date +%y.%m`
echo "What is the current version number? (Default: ${VERSION})"
read touche
case "$touche" in
  "" )
  ;;
  * )
  VERSION="$touche"
  ;;
esac
echo "*** Update pyromaths version..."
sed -i "s/VERSION ?= .*/VERSION ?= ${VERSION}/" ${PYROPATH}/Makefile

# Clean-up and create Documentation
cd $PYROPATH/Doc
make clean
make doctest
make html

# Prepare Changelog
cd $PYROPATH
head -20 NEWS
dch -v ${VERSION}-1
dch -r

# Clean-up and create packages
make clean
make all
make repo

echo "*** Create Windows binary..."
echo "Hit 'enter' when Windows package is ready."
read touche

echo "*** Tag git develop ***"
echo "Do you want to commit and tag the git develop branch (o/N)?"
read touche
case "$touche" in
  [oO] )
  git commit -am 'Pyromaths Release'
  git tag -u B39EE5B6 version-${VERSION} -m "Pyromaths ${VERSION}"
  #git push --tags:
  ;;
esac

echo "*** Update pyromaths web-site links..."
cat > ${PYROPATH}/pyrosite.txt << EOF
:title: Version ${VERSION}
:slug: version-$(echo ${VERSION} | sed 's/\./-/g')
:date: $(date +"%Y-%m-%d %H:%M")
:category: telecharger
:description: Liens vers la version ${VERSION}

* |debian| `Pyromaths pour Linux - deb <https://enligne.pyromaths.org/downloads/pyromaths_${VERSION}-1_all.deb>`_
* |redhat| `Pyromaths pour Linux - rpm <https://enligne.pyromaths.org/downloads/pyromaths-${VERSION}-1.noarch.rpm>`_
* |macos| `Pyromaths pour Mac OS X <https://enligne.pyromaths.org/downloads/pyromaths-${VERSION}-macos.dmg>`_
* |windows| `Pyromaths pour Windows <https://enligne.pyromaths.org/downloads/pyromaths_${VERSION}.exe>`_
* |sources| `Sources de Pyromaths <https://pypi.org/project/pyromaths/>`_

.. |debian| image:: images/debian.png
    :alt: Debian Linux
.. |redhat| image:: images/redhat.png
    :alt: RedHat Linux
.. |macos| image:: images/macosx.png
    :alt: Mac OS X
.. |windows| image:: images/winvista.png
    :alt: Windows
.. |sources| image:: images/source.png
    :alt: Sources

Nouveautés de cette version :
=============================

EOF
