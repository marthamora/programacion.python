import sys,os,pkgutil

def load_all_modules_from_dir(dirname):
    for importer, package_name, _ in pkgutil.iter_modules([dirname]):
        full_package_name = '%s.%s' % (dirname, package_name)
        if full_package_name not in sys.modules:
            module = importer.find_module(package_name).load_module(full_package_name)
            print module

def main():
    load_all_modules_from_dir('ejercicio1')
    load_all_modules_from_dir('ejercicio2')
    load_all_modules_from_dir('ejercicio3')
    print "Archivo Principal"

if_name_=='_main_':
    main()