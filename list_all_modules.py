import sys
sys.path.append('D:\Rokid\pycharm\_PythonScripts')
# from os.path import dirname, basename, isfile, join
import os
# import importlib
from inspect import getmembers, isfunction


def import_modules(parentdir, print_modules=True):
    parentdir_modules = []
    subdir_modules = []
    subdir_module_names = []

    for file in os.listdir(parentdir):
        if file.endswith(".py"):
            #strip the extension
            module = file[:-3]
            # set the module name in the current global name space:
            # importlib.import_module(module)
            if print_modules:
                print(module)
            parentdir_modules.append(module)
            # if print_modules:
                # print(module)


    for root, dirs, files in os.walk(parentdir):
        # print(dirs)
        for dir in dirs:
            if os.path.isdir(dir) and not dir.startswith('.') and not dir.startswith('_'):
                if print_modules:
                    print('-------------', dir, '-------------')

                for file in os.listdir(dir):
                    # print(os.listdir(dir))

                    if file.endswith(".py"):
                        #strip the extension
                        module = file[:-3]
                        # set the module name in the current global name space:
                        # importlib.import_module("%s."%dir + module)
                        subdir_modules.append(module)
                        if print_modules:
                            print(module)
                        subdir_module_names.append('%s.%s'%(dir, module))
    my_modules = parentdir_modules+subdir_module_names

    return my_modules


# import yourmodule




# def list_functions(one_module):
#     importlib.import_module(one_module)
#     my_functions = inspect.getmembers(music.get_wav_duration, inspect.isfunction)
#     print(my_functions)

if __name__ == '__main__':
    pkg = 'D:\Rokid\pycharm\_PythonScripts/'
    my_modules = import_modules(pkg, 1)

###### print all the import statements for further imports
    final_mo = []
    for m in my_modules:
        new_m = 'import '+ m
        final_mo.append(new_m)

    print('\n'.join(final_mo))
######

    with open('my_modules.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(my_modules))