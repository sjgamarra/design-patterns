'''
Created on Oct 21, 2017

@author: zethiel
'''


class AbstractDispatcher():

    def __init__(self, delivery_mode):
        self.delivery = delivery_mode
    
    def send(self):
        self.delivery.send_package()