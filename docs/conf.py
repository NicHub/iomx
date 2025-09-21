import os
import sys

# Add project path
sys.path.insert(0, os.path.abspath('..'))

project = 'iomx'
copyright = '2025'
author = 'Nicolas Jeanmonod'

extensions = [
    'myst_parser',
]

myst_enable_extensions = [
    'colon_fence',
]

html_theme = 'sphinx_rtd_theme'
master_doc = 'index'
