import base64
from Crypto.Cipher import AES
import pandas as pd

class MyAes:
    def __init__(self,ciphertext:str,key:str):
        self.ciphertext = base64.b64decode(ciphertext)
        self.key = self.zeropadding(key,16)
        self.key = self.key.encode('ascii') #Encode key to byte

    def zeropadding(self,key:str,size):
        while(len(key) % size != 0):
            key += '\0'
        return key

    def decode(self):
        #AES decode
        cipher = AES.new(self.key, AES.MODE_ECB)
        decrypted = cipher.decrypt(self.ciphertext)
        #Transfer to base64
        try:
            message = decrypted.decode('UTF-8')
            print(f'Key:{self.key.decode()}')
            print(f'Message:{message}')
        except:
            pass

for i in range(32,127):
    for j in range(32,127):
        for k in range(32,127):
            for l in range(32,127):
                key =  chr(i) + '-?5Q' + chr(j) + 'E' + chr(k) + 'qeDe' + chr(l) + '%Bs'
                a = MyAes('IZ7J32pjWOR0zpJeQbj1Z+Mu0cRftohz6imCF3+2k1w=',key)
                a.decode()


