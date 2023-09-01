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


# -- Project information -----------------------------------------------------

project = 'Tutorial/Linux'
copyright = '2016, Robin Long'
author = 'Robin Long'


# -- General configuration ---------------------------------------------------
# -- General configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.extlinks',
    'sphinx.ext.imgmath',
    'sphinx.ext.graphviz',
]



intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for EPUB output
epub_show_urls = "footnote"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
#html_css_files = ["_static/style.css"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_logo = 'logo-lancs.png'





pygments_style = 'sphinx'
htmlhelp_basename = 'SphinxRestMemodoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}
latex_documents = [
  ('index', 'SphinxRestMemo.tex', 'Sphinx/Rest Memo',
   'Marc Zonzon', 'manual'),
]
man_pages = [
    ('index', 'sphinxrestmemo', 'Sphinx ReST Memo',
     ['Marc Zonzon'], 1)
]
texinfo_documents = [
  ('index', 'SphinRestMemo', 'Sphinx/reST Memo',
   'Marc Zonzon', 'SphinRestMemo', 'Sphinx/reST Memo.',
   'Miscellaneous'),
]
epub_title = 'Introduction to Linux'
epub_author = 'Robin Long'
epub_publisher = 'Robin Long'
epub_copyright = '2016, Robin Long'



extlinks = {
    'sphinx': ('http://sphinx-doc.org/latest/%s', 'Sphinx: '),
    'restref': ('http://docutils.sourceforge.net/docs/ref/rst/%s', 'ReST Référence: ')
}
