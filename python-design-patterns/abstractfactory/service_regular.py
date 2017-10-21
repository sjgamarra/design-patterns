'''
Created on Oct 21, 2017

@author: zethiel
'''
from abstract_service import AbstractService

class ServiceRegular(AbstractService):

    def print_name(self):
        print('This is a regular service...')