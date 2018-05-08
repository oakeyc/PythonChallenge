from Crypto.Cipher import DES
from Crypto import Random

from cryptography.fernet import Fernet
key = Fernet.generate_key()
userKey = "BZh91AY&SYA"
cipertext = b"\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084" 

cipher_suite = Fernet(userKey)
plain_text = cipher_suite.decrypt(cipertext)

'''
iv = Random.new().read(DES.block_size/2)
obj2 = DES.new(userKey, DES.MODE_CFB, iv)
print(obj2.decrypt(ciphertext))
'''
