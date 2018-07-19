"""Chemin de quelques répertoires propres à Pyromaths."""

import os
import sys

import pkg_resources

DATADIR = pkg_resources.resource_filename("pyromaths", "data")
EXODIR = os.path.join(DATADIR, "exercices")
LOCALEDIR = os.path.join(DATADIR, "locale")

if os.name == 'nt': # Windows
    HOME = os.environ['USERPROFILE']
    CONFIGDIR = os.path.join(os.environ['APPDATA'], "pyromaths")
elif sys.platform == "darwin":  # Mac OS X
    HOME = os.environ['HOME']
    CONFIGDIR = os.path.join(HOME, "Library", "Application Support", "Pyromaths")
else: # Linux (et autres ?)
    HOME = os.environ['HOME']
    CONFIGDIR = os.path.join(HOME, ".config", "pyromaths")

