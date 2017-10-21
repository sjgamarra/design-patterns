'''
Created on Oct 21, 2017

@author: zethiel
'''
from abstract_factory import AbstractFactory
from delivery_national import DeliveryNational
from service_express import ServiceExpress

class FactoryAdvancePackage(AbstractFactory):

    def create_delivery(self):
        return DeliveryNational()

    def create_service(self):
        return ServiceExpress()