# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Universe Map'
copyright = '2022, Sara Collins'
author = 'Sara Collins'
release = '0.0.1-rc-1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.githubpages',
              'sphinx.ext.duration',
              'sphinx.ext.doctest',
              'sphinx.ext.napoleon',
              'numpydoc',
              'autoapi.extension']

templates_path = ['_templates']
exclude_patterns = []
autosummary_generate = True
autosummary_imported_members = True
numpydoc_show_class_members = True
autoapi_dirs = ['../../universe_map']
autoapi_python_class_content = 'init'
autoapi_add_toctree_entry = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'nature'
html_static_path = ['_static']

def skip_properties(app, what, name, obj, skip, options):
    if what == "property":
        skip = True
    elif "logger" in name:
        skip = True
    return skip

def setup(sphinx):
   sphinx.connect("autoapi-skip-member", skip_properties)
