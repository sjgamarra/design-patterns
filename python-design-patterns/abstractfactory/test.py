'''
Created on Oct 21, 2017

@author: zethiel
'''
from factory_basic_package import FactoryBasicPackage
from factory_advance_package import FactoryAdvancePackage

def main():
    for factory in (FactoryBasicPackage(), FactoryAdvancePackage()):
        print('----------------------------')
        delivery = factory.create_delivery()
        service = factory.create_service()
        delivery.print_name()
        service.print_name()

if __name__ == "__main__":
    main()