'''
Created on Oct 21, 2017

@author: zethiel
'''
from abstract_delivery import AbstractDelivery

class DeliveryNational(AbstractDelivery):

    def print_name(self):
        print('This is a national delivery...')