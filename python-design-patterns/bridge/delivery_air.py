'''
Created on Oct 21, 2017

@author: zethiel
'''
from abstract_delivery_mode import AbstractDeliveryMode

class DeliveryAir(AbstractDeliveryMode):

    def send_package(self):
        print('Sent by plane...')