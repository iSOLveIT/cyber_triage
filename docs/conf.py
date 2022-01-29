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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
# import sphinx_rtd_theme
import sphinx_material
from datetime import datetime as dt


# -- Project information -----------------------------------------------------

project = 'Cyber Triage'
copyright = f"{dt.now().year}, Basis Technology"
author = 'Basis Technology'
version = '3.0'
release = '3.0.2'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx-prompt', 'sphinx_substitution_extensions']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Required theme setup
html_theme = 'sphinx_material'
# Set the logo and favicon
html_logo = './_static/img/logo_header.jpg'
html_favicon = './_static/img/favicon.ico'
# Set link name generated in the top bar.
# html_title = 'Cyber Triage'
# Material theme options (see theme.conf for more information)
html_theme_options = {
    # Set the name of the project to appear in the navigation.
   #  'nav_title': 'Cyber Triage',
    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://project.github.io/project',
    # Set the color and the accent color
    'color_primary': 'indigo',
    'color_accent': 'green',
    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/iSOLveIT/cyber_triage',
    'repo_name': 'Cyber Triage',
    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 1,
    # If False, expand all TOC entries
    'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': True,
    'html_minify': True,
    'css_minify': True,
    'theme_color': '#3f51b5'
}
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

html_style = 'css/material_custom.css'
file_insertion_enabled = True
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_show_sphinx = False  # shows sphinx footer link
html_show_sourcelink = False  # shows link to rst file that generates page

rst_epilog = """

.. |cyTriage| replace:: Cyber Triage\ :sup:`®`

.. |basisTech| replace:: Basis Technology\ :sup:`®`

.. |br| raw:: html 

   <br>

"""

html_last_updated_fmt = '%b %d, %Y'

# tablecaption = 'below'

pygments_style = 'sphinx'

# PDF output
latex_engine = 'pdflatex'
latex_logo = './_static/img/cyber_triage.jpg'