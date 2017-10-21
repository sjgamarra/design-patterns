'''
Created on Oct 21, 2017

@author: zethiel
'''
from concrete_dispatcher import ConcreteDispatcher
from delivery_air import DeliveryAir
from delivery_ground import DeliveryGround

def main():
    delivery_by_air = DeliveryAir()
    delivery_by_ground = DeliveryGround()
    
    dispatcher = ConcreteDispatcher(delivery_by_ground)
    dispatcher.send()
    
    dispatcher = ConcreteDispatcher(delivery_by_air)
    dispatcher.send()

if __name__ == "__main__":
    main()