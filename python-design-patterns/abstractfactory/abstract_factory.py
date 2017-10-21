'''
Created on Oct 21, 2017

@author: zethiel
'''

import abc

class AbstractFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_delivery(self):
        pass

    @abc.abstractmethod
    def create_service(self):
        pass
        