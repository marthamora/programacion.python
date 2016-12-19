#MARTHA ELENA NIEVES MORA
#LABORATORIO 3B
#ejercicios 7

import sys,os,pkgutil


ddef load_all_modules_from_dir(dirname):
    for importer, package_name, _ in pkgutil.iter_modules([dirname]):
        full_package_name = '%s.%s' % (dirname, package_name)
        if full_package_name not in sys.modules:
            module = importer.find_module(package_name
                        ).load_module(full_package_name)
            print module

def main():
    load_all_modules_from_dir('ejercicio 1')
    load_all_modules_from_dir('ejercicio 2')
    load_all_modules_from_dir('ejercicio 3')
    load_all_modules_from_dir('ejercicio 4')
    load_all_modules_from_dir('ejercicio 5')
    load_all_modules_from_dir('ejercicio 6')
    load_all_modules_from_dir('ejercicio 7')
    print 'modules'


if __name__ == '__main__':
        main()
