import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
import pylab as pl
import logging
import datetime
import collections

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

class Client:
    def __init__(self):
        random = Crypto.Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()

    @property
    def identity(self):
            return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
    def identify(self):
         return binascii.hexlify(self._private_key.exportKey(format='DER')).decode('ascii')
class Transaction:
    def __init__(self, sender, receiver, value):
        self.sender = sender
        self.receiver = receiver
        self.value = value
        self.time = datetime.datetime.now()
    
    def to_dictionary(self): 
    
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity

        return collections.OrderedDict({'sender':identity,
                            'receiver': self.receiver,
                            'value': self.value,
                            'time': self.time}
                           )

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dictionary()).encode('utf8'))
        
        return binascii.hexlify(signer.sign(h)).decode('ascii')
    def displayy(transaction):
            dict = transaction.to_dictionary()
          
            print("Sender:" + dict['sender'])
            print("-------------------------------")
            print("Recepient:" + dict['receiver'])
            print("-------------------------------")
            print("Value:" + str(dict['value']))
            print("-------------------------------")
            print("Timestamp:" + str(dict['time']))
            print("-----------------------------------------------------------------")
transactionlist = []
samuel = Client()
james = Client()
david = Client()
print(james.identify())
t = Transaction(
    samuel,
    james.identity,
    4.0
    )
t.sign_transaction()

transactionlist.append(t)
t1 = Transaction(
    james,
    david.identity,
    14.0
    )
t1.sign_transaction()


transactionlist.append(t1)
for i in transactionlist:
    i.displayy()
print(t.sign_transaction())

