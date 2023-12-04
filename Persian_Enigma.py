import string
import random
import pickle
import sys

alphabet = "ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"

def rndm_r():
    r1 = "غصبلرشذثیکقجوهحاطزدپژگنخفسظضمتچع"
    r2 = "وخثزگحضلکظرعتجذنهغبیمطافقشچپصسدژ"
    r3 = "زهمبدکترغضلپنعجگاخظژسچطذفوصثیحقش"
    return r1, r2, r3

def create_rotor():
    rotor = list(alphabet)
    return rotor

def rndm_rotor():
    r1, r2, r3 = rndm_r()
    r1 = list(r1)
    r2 = list(r2)
    r3 = list(r3)
    return r1, r2, r3

def reflector(c):
    return alphabet[len(alphabet) - alphabet.find(c) - 1]

def enigma_one_char(c, r1, r2, r3):
    c1 = r1[alphabet.find(c)]
    c2 = r2[alphabet.find(c1)]
    c3 = r3[alphabet.find(c2)]
    reflected = reflector(c3)
    c3 = alphabet[r3.index(reflected)]
    c2 = alphabet[r2.index(c3)]
    c1 = alphabet[r1.index(c2)]
    return c1

def encode_message(message, r1, r2, r3):
    result = ""
    for char in message:
        result += enigma_one_char(char, r1, r2, r3)
    return result

def decode_message(encoded_message, r1, r2, r3):
    result = ""
    for char in encoded_message:
        result += enigma_one_char(char, r1, r2, r3)
    return result

message = input("پیغام خود را وارد کنید: ")
senchar = [char for char in message if char != ' ']

r1, r2, r3 = rndm_rotor()
encoded_message = encode_message(senchar, r1, r2, r3)
print("Encoded message:", encoded_message)

