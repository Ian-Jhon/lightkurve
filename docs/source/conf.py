#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__name__), '..'))

import lightkurve


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'nbsphinx',
    'numpydoc',
    'sphinx_automodapi.automodapi',
    'sphinxcontrib.rawfiles']

# Disable RequireJS because it creates a conflict with bootstrap.js.
# This conflict breaks the navigation toggle button.
# The exact consequence of disabling RequireJS is not understood
# -- likely it means that notebook widgets may not work?
nbsphinx_requirejs_path = ""

numpydoc_show_class_members = False


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Exclude build directory and Jupyter backup files:
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Lightkurve'
copyright = 'Lightkurve developers'
author = 'Kepler/K2 Guest Observer Office'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ".".join(lightkurve.__version__.split('.')[:2])
# The full version, including alpha/beta/rc tags.
release = lightkurve.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["**/.ipynb_checkpoints"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Some notebook cells take longer than 60 seconds to execute
nbsphinx_timeout = 300

# PUT PROLOG HERE
nbsphinx_prolog = r"""
{% set docname = env.doc2path(env.docname, base=None) %}

.. only:: html

    .. raw:: html

        <div style="float:right; margin-top:1em; margin-bottom:-1em;">
            <a href="https://github.com/KeplerGO/lightkurve/tree/master/docs/source/{{ docname }}"><img src="https://img.shields.io/badge/Jupyter%20Notebook-Download-blue.svg"></a>
            <a href=" https://colab.research.google.com/github/KeplerGO/lightkurve/blob/master/docs/source/{{ docname }}"><img src="https://colab.research.google.com/assets/colab-badge.svg"></a>
            <a href="https://mybinder.org/v2/gh/KeplerGO/lightkurve/master?filepath=docs/source/{{ docname }}"><img alt="Binder badge" src="https://mybinder.org/badge_logo.svg"></a>
        </div>
        <br style="clear:both;">
"""

# -- Options for HTML output ----------------------------------------------
html_theme = 'amunra_sphinx_theme'

html_theme_options = {
    "navbar_title": "Lightkurve v" + version,
    "navbar_links": [
        ("Quickstart", "quickstart"),
        ("Tutorials", "tutorials/index"),
        ("API", "api/index"),
        ("About", "about/index"),
    ],
    "github_link": "https://github.com/KeplerGO/Lightkurve",
    "footer_text": """Created with ♥ by the Lightkurve collaboration.
                      Please <a href="/about/citing.html">cite us</a> or
                      <a href="https://github.com/KeplerGO/Lightkurve">join us on GitHub.</a>""",
    "analytics_id": "UA-69171-9"
}

html_title = "Lightkurve"

html_static_path = ['_static']

# Raw files we want to copy using the sphinxcontrib-rawfiles extension:
# - CNAME tells GitHub the domain name to use for hosting the docs
# - .nojekyll prevents GitHub from hiding the `_static` dir
rawfiles = ['CNAME', '.nojekyll']

# Make sure text marked up `like this` will be interpreted as Python objects
default_role = 'py:obj'

# intersphinx enables links to classes/functions in the packages defined here:
intersphinx_mapping = {'python': ('https://docs.python.org/3/', None),
                       'numpy': ('https://docs.scipy.org/doc/numpy/', None),
                       'scipy': ('https://docs.scipy.org/doc/scipy/reference', None),
                       'matplotlib': ('https://matplotlib.org', None),
                       'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
                       'oktopus': ('https://keplergo.github.io/oktopus', None),
                       'astropy': ('https://docs.astropy.org/en/latest/', None)}
