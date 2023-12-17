import string
import random
import pickle
import sys

alphabet = "ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"

def create_rotor():
    rotor = list(alphabet)
    return rotor

def rndm_rotor():
    r1 = list(alphabet)
    random.shuffle(r1)

    r2 = list(alphabet)
    random.shuffle(r2)

    r3 = list(alphabet)
    random.shuffle(r3)

    return r1, r2, r3

def conv_sen(r1, r2, r3, senchar):
    result = ""
    for char in senchar:
        c1 = r1[alphabet.find(char)]
        c2 = r2[alphabet.find(c1)]
        c3 = r3[alphabet.find(c2)]
        result += c3
    
    return result

message = input("پیغام خود را وارد کنید: ")
senchar = [char for char in message if char != ' ']

r1, r2, r3 = rndm_rotor()
result = conv_sen(r1, r2, r3, senchar)
print(result)
