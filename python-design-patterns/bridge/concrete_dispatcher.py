'''
Created on Oct 21, 2017

@author: zethiel
'''
from abstract_dispatcher import AbstractDispatcher

class ConcreteDispatcher(AbstractDispatcher):

    def print_name(self):
        print('Im a dispatcher...')