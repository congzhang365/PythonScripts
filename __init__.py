import sys
sys.path.append('D:\Rokid\pycharm\_PythonScripts')

import glob
from os.path import dirname, basename, isfile, join


modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
# print(__all__)
