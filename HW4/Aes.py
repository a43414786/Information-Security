import base64

import json
import string
from Crypto.Cipher import AES

class MyAes:
    def __init__(self,ciphertext:str,key:str):
        self.ciphertext = self.zeropadding(ciphertext)
        self.ciphertext = self.ciphertext.encode('ascii') #Encode key to byte
        self.key = self.zeropadding(key)
        self.key = self.key.encode('ascii') #Encode key to byte

    def zeropadding(self,key:str):
        while(len(key) % 16 != 0):
            key += '0'
        return key

    def decode(self):
        #AES decode
        cipher = AES.new(self.key, AES.MODE_ECB)
        decrypted = cipher.decrypt(self.ciphertext)
        # print(decrypted)
        #Transfer to base64
        message_bytes = base64.b64decode(decrypted)
        
        # message = message_bytes.decode('UTF-8')
        print(message_bytes)



a = MyAes('pKjVPv28yVMn5cRXeUNYpg==','123456789')
# a.str2Base64()
a.decode()

s = 'security'

b = s.encode('utf-8')
ans = base64.b64encode(b)
print(ans)

b = base64.b64decode(ans)
s = b.decode('utf-8')
print(s)
