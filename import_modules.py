import sys
sys.path.append('D:\Rokid\pycharm\_PythonScripts')
import change_line_numbers
from TextProcessing.separate_lines import *
from TextProcessing.check_english import *
from music import *

from os.path import dirname, basename, isfile, join
import glob
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

'''

from package1 import module1
from package1.module2 import function1
from package2 import class1
from package2.subpackage1.module5 import function2

'''