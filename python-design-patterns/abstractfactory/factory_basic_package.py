'''
Created on Oct 21, 2017

@author: zethiel
'''
from abstract_factory import AbstractFactory
from delivery_zonal import DeliveryZonal
from service_regular import ServiceRegular

class FactoryBasicPackage(AbstractFactory):

    def create_delivery(self):
        return DeliveryZonal()

    def create_service(self):
        return ServiceRegular()