# -*- coding: utf-8 -*-
import sys
import os
import time
import bottle

bottle_dir = os.path.abspath(os.path.join(os.path.dirname("__file__"), '../'))
print bottle_dir
sys.path.insert(0, bottle_dir)

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx',
              'sphinx.ext.viewcode']
master_doc = 'index'
project = u'Bottle'
copyright = u'2009-%s, %s' % (time.strftime('%Y'), bottle.__author__)
version = ".".join(bottle.__version__.split(".")[:2])
release = bottle.__version__
add_function_parentheses = True
add_module_names = False
pygments_style = 'sphinx'
intersphinx_mapping = {'python': ('http://docs.python.org/', None),
                       'werkzeug': ('http://werkzeug.pocoo.org/docs/', None)}
locale_dirs = ['_locale/']
gettext_compact = False

autodoc_member_order = 'bysource'

