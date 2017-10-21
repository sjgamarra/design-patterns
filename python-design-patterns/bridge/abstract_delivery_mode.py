'''
Created on Oct 21, 2017

@author: zethiel
'''
import abc

class AbstractDeliveryMode(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def send_package(self):
        pass