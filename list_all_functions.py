import sys
sys.path.append('D:\Rokid\pycharm\_PythonScripts')
import types
from . import *
from os.path import dirname, basename, isfile, join
import glob
import os
import importlib


# def print_module_functions(module):
#
#     print('\n'.join([str(module.__dict__.get(a).__name__) \
#                      for a in dir(module) \
#                      if isinstance(module.__dict__.get(a), types.FunctionType)]))
#
# modules = glob.glob(join(dirname(__file__), "*.py"))
# __all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

for name in os.listdir("TextProcessing"):
    if name.endswith(".py"):
        #strip the extension
        module = name[:-3]
        # set the module name in the current global name space:
        importlib.import_module("TextProcessing" + "." + module)
        # print_module_functions(scale2Textgrid)