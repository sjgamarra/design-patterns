'''
Created on Oct 21, 2017

@author: zethiel
'''
import abc

class AbstractService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def print_name(self):
        pass