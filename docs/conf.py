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

sys.path.insert(0, os.path.abspath("../src"))


# -- Project information -----------------------------------------------------

project = "weiyih"
copyright = "2022, Yap Wei Yih"
author = "Yap Wei Yih"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "nbsphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    # "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.doctest",
    # "myst_parser",
    # "sphinx_toggleprompt",
    # "sphinx_autodoc_typehints",
    # "sphinxemoji.sphinxemoji",
    # "sphinx_gallery.load_style",
]
autosectionlabel_prefix_document = True
autosummary_generate = True
autoclass_content = "both"
autodoc_default_options = {"show-inheritance": True}
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

nbsphinx_kernel_name = "python3"
# https://nbsphinx.readthedocs.io/en/0.8.8/usage.html#nbsphinx_execute_arguments
nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc=figure.dpi=96",
]

# Customize the html files generated from notebooks:
# - Add "download as .ipynb" link.
# - Make ANSI yellow more visible on white background. Typically needed by rich colored outputs.
nbsphinx_epilog = r"""
{% set docname = env.doc2path(env.docname, base=None).rsplit('/', 1)[1] %}

.. raw:: html

    <style>
        .ansi-yellow-fg { color: #b65908; }
        .ansi-yellow-bg { color: #b65908; }
    </style>

    <div class="admonition note">
    Download this page as <a href="{{ docname|e }}">{{ docname|e }}</a> (right-click, and save as).
    </div>
 """

# nbsphinx_epilog = nbsphinx_prolog

# URL-shortener for docstrings
extlinks = {
    "pdug": (
        "https://pandas.pydata.org/pandas-docs/stable/user_guide/%s",
        "Pandas User Guide %s",
    )
}


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]

# pydata-theme: add icon links to show up to the right of your main navigation bar.
html_theme_options = {
    "github_url": "https://github.com/yapweiyih/template-doc",
    "icon_links": [
        {
            "name": "Gmail",
            "url": "https://www.gmail.com",
            "icon": "_static/gmail.png",
            "type": "local",
        },
    ],
    "use_edit_page_button": True,
}


# pydata-theme: add an edit-this-page button
# https://github.com/yapweiyih/template-doc.git
html_context = {
    "github_url": "https://github.com",
    "github_user": "yapweiyih",
    "github_repo": "template-doc",
    "github_version": "main",
    "doc_path": "docs",
}


def autodoc_skip_member(app, what, name, obj, skip, options):
    """Show only members from whatif module.

    Typical use-case: make the autosummary table of whatif.DataFrame exclude methods and attributes
    inherited from pandas. This will drastically reduce the autosummary table, and also the
    lhs-navbar.
    """
    if obj is None:
        return True
    if isinstance(obj, property):
        obj = obj.fget
    if not hasattr(obj, "__module__"):
        return True
    if obj.__module__ and obj.__module__.startswith("weiyih."):
        return None
    return True


def setup(app):
    app.add_css_file("custom.css")
    app.connect("autodoc-skip-member", autodoc_skip_member)
