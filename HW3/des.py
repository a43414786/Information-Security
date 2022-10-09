from hashlib import new
from Crypto.Cipher import DES
import binascii

class Des():
    def __init__(self,plainText:str,key:str):
        self.plainText = self.zeropadding(plainText,8)
        self.plainText = self.plainText.encode('utf-8')
        self.cipherText = ""
        # print(self.plainText)
        self.key = self.zeropadding(key,8,True)
        self.key = self.key.encode('utf-8')
        # print(self.key)
        
    def zeropadding(self,text:str,size:int,isKey = False):
        while len(text) % size != 0:
            text += '\0'
        if(isKey):
            return text[0:8]
        else:
            return text
        # text = text[0:8]
        
    def encode(self):
        des = DES.new(self.key, DES.MODE_ECB)
        self.cipherText = des.encrypt(self.plainText)
        print(self.cipherText.hex())

        return
    
des = Des('Hello','abcdefgh')
des.encode()
print(binascii.unhexlify(des.cipherText.hex()))
des = Des('Hello','ibcdefgh')
des.encode()
print(binascii.unhexlify(des.cipherText.hex()))
des = Des('Hello','abcdefgh')
des.encode()
print(binascii.unhexlify(des.cipherText.hex()))
des = Des('Helln','abcdefgh')
des.encode()
print(binascii.unhexlify(des.cipherText.hex()))

