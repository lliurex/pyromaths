# Création d'un paquet python (sources, wheel)

Lancer :

    # Création du fichier MANIFEST.in
    make MANIFEST.in
    # Paquet sources
    python setup.py sdist
    # Paquet wheel
    python setup.py bdist_wheel

Ceci est fait automatiquement avec :

    make src wheel

# Téléversement sur pypi

En utilisant twine :

    twine upload -s dist/PAQUET

# Création d'un paquet Debian

TODO
