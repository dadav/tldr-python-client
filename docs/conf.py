# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import re
from pathlib import Path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# -- Project information -----------------------------------------------------

project = 'tldr'
copyright = '2014, Felix Yan'
author = 'Felix Yan'

_setup_dir = Path(__file__).resolve().parent.parent
_version = re.search(
    r'__version__ = "(.*)"',
    Path(_setup_dir, 'tldr.py').open().read()
)
if _version is None:
    raise SystemExit("Could not determine version to use")

_version = _version.group(1)
release = _version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxarg.ext'
]
