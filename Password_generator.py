import random
import json
import hashlib
import sys
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import clipboard
import getpass as gp
class manager(object):
    iv = b'idhnclx1734bs8av'

    def __init__(self, file):
        self.salt = ''
        master_password = gp.getpass('Your Password\n')
        r =  random.Random(master_password)
        if len(master_password) < 10:
            print('Your Password is not secure')
            sys.exit()
        elif len(master_password)< 32:
            for i in range(32):
                self.salt += (chr((int(r.random()*(127-33))+33)))
        elif len(master_password)<64:
            for i in range(64):
                self.salt += (chr((int(r.random()*(127-33))+33)))
        else:
            print('password to long')
            sys.exit()
        self.master_password = master_password + self.salt[len(master_password):]
        self.file = file
        self.data = {}
        print(master_password)

    def initialisiere():
        try:
            with open(file,'r') as f:
                self.data = json.load(f)
                if (hashlib.sha512((self.master_password).encode('utf-8')).hexdigest() != self.data['master_password']):
                    print('password not correct')
                    sys.exit()
        except FileNotFoundError:
            pass

    def add_password(self, password_site:str, password:str) -> None:
        cipher = AES.new(key = self.master_password.encode(), mode = AES.MODE_CFB, iv = manager.iv)
        ct_bytes = cipher.encrypt(password.encode())
        self.data[password_site] = b64encode(ct_bytes).decode('utf-8')
        self.save()

    def save(self) -> None:
        with open(self.file, 'w') as f:
            json.dump(self.data,f, indent = 4)

    def read_password(self, password_site:str)-> None:
        cipher = AES.new(key = self.master_password.encode(), mode = AES.MODE_CFB, iv = manager.iv)
        clipboard.copy(cipher.decrypt(b64decode(self.data[password_site])).decode())

    def create_new_manager(self) -> None:
        self.cipher = AES.new(key = self.master_password.encode(), mode = AES.MODE_CFB, iv = manager.iv)
        self.data= {'master_password':hashlib.sha512((self.master_password).encode('ascii')).hexdigest()}
        with open(self.file, 'w') as f:
            json.dump(self.data,f, indent = 4)

    @staticmethod
    def generator(x: int = 64) -> str:
        if (type(x) is not int or x <1):
            raise ValueError('x has to be a positive integer')
        if(x<10):
            if input('x is verry small, your password is not secure Continue (y/n)?\n') == 'y':
                pass
            else:
                while(True):
                    try:
                        return manager.generator(int(input('How many digits?\n')))
                    except TypeError:
                        pass
        j = ""
        for i in range(x):
            j += (chr((int(random.random()*(127-33))+33)))
        return j

maneger = manager('this.json')
#maneger.create_new_manager()
#maneger.add_password('Disney', 'Wasgeht')
#print(maneger.read_password('Disney'))
#maneger.add_password('Netflix', 'Nope__ist_kein_sicheres_passwort=')
#x = manager.generator(64)
#maneger.add_password('Keine Ahnung was noch', x)
#maneger.add_password('Keine Ahnung was noch',x)
#maneger.read_password('Keine Ahnung was noch')
#print(x)

print(len('idhnclx1734bs8av'))
#Verhindern, dass Zeugs im log landet
