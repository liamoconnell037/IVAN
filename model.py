import tensorflow_hub as hub
import tensorflow_text
from tensorflow import keras
import base64
import numpy as np
from bitarray import bitarray  # pip install bitarray

model = keras.models.load_model('./model.keras')
preprocessor = hub.KerasLayer('https://www.kaggle.com/api/v1/models/tensorflow/bert/tensorFlow2/en-cased-preprocess/3/download')
encoder = hub.KerasLayer(
    "https://www.kaggle.com/api/v1/models/tensorflow/bert/tensorFlow2/en-cased-l-12-h-768-a-12/4/download", trainable=True)


def decode(msg, num=0):
    if num >= 5:
        print("hit the limit for number of recursions")
        return msg
    prediction = model.predict(bertsentence([msg]))
    m = np.argmax(prediction[0])
    match m:
        case 0:
            print("base64!")
            return decode(base64.b64decode(msg).decode('ascii'), num+1)
        case 1:
            print("binary!")
            return decode(bitarray(msg).tobytes().decode('ascii'), num+1)
        case 2:
            print("english!")
            return msg


def bertsentence(sentences):
    return encoder(preprocessor(sentences))['pooled_output']

print("single encoded:")
print(decode('RHVyaW5nIHRoZSBzZXZlbnRlZW50aCBzZWFzb24gb2YgQW1lcmljYSdzIEdvdCBUYWxlbnQsIEpvSm8gYW5kIEplc3NhbHluIGZvcm1lZCB0aGUgZ3JvdXAgWE9NRyBQb3AgdGhhdCB3ZXJlIHByZXZpb3VzbHkgZGlzY292ZXJlZCBvbiBTaXdhJ3MgRGFuY2UgUG9wIFJldm9sdXRpb24gd2hvIGF1ZGl0aW9uZWQgYnkgc2luZ2luZyAiQ2FuZHkgSGVhcnRzIi4gVGhlIGp1ZGdlcyB3ZXJlIGltcHJlc3NlZCBhbmQgcHJvbW90ZWQgdGhlbSB0byB0aGUgbmV4dCByb3VuZC4gSm9KbyBhbmQgSmVzc2FseW4gY29uZ3JhdHVsYXRlZCB0aGUgZ3JvdXAgYXMgSm9KbyB0b2xkIHRoZSBqdWRnZXMgdGhhdCBzaGUgaXMgYSBiaWcgZmFuIG9mIEFHVC4='))
print('\n')
print(decode('01001001 01101110 00100000 01000001 01110101 01100111 01110101 01110011 01110100 00100000 00110010 00110000 00110010 00110001 00101100 00100000 01000001 01110010 01100111 01100101 01101110 01110100 01101001 01101110 01100101 00100000 01100001 01101110 01100100 00100000 01101001 01101110 01110100 01100101 01110010 01101110 01100001 01110100 01101001 01101111 01101110 01100001 01101100 00100000 01101101 01100101 01100100 01101001 01100001 00100000 01110010 01100101 01110000 01101111 01110010 01110100 01100101 01100100 00100000 01110100 01101000 01100001 01110100 00100000 01100011 01100001 01110000 01111001 01100010 01100001 01110010 01100001 01110011 00100000 01101000 01100001 01100100 00100000 01100010 01100101 01100101 01101110 00100000 01100011 01100001 01110101 01110011 01101001 01101110 01100111 00100000 01110011 01100101 01110010 01101001 01101111 01110101 01110011 00100000 01110000 01110010 01101111 01100010 01101100 01100101 01101101 01110011 00100000 01100110 01101111 01110010 00100000 01110010 01100101 01110011 01101001 01100100 01100101 01101110 01110100 01110011 00100000 01101111 01100110 00100000 01001110 01101111 01110010 01100100 01100101 01101100 01110100 01100001 00101100 00100000 01100001 01101110 00100000 01100001 01100110 01100110 01101100 01110101 01100101 01101110 01110100 00100000 01100111 01100001 01110100 01100101 01100100 00100000 01100011 01101111 01101101 01101101 01110101 01101110 01101001 01110100 01111001 00100000 01101110 01101111 01110010 01110100 01101000 00100000 01101111 01100110 00100000 01000010 01110101 01100101 01101110 01101111 01110011 00100000 01000001 01101001 01110010 01100101 01110011 00100000 01100010 01110101 01101001 01101100 01110100 00100000 01100001 01110100 01101111 01110000 00100000 01110111 01100101 01110100 01101100 01100001 01101110 01100100 00100000 01101000 01100001 01100010 01101001 01110100 01100001 01110100 00101110 00100000 01010100 01101000 01101001 01110011 00100000 01101001 01101110 01110011 01110000 01101001 01110010 01100101 01100100 00100000 01110011 01101111 01100011 01101001 01100001 01101100 00100000 01101101 01100101 01100100 01101001 01100001 00100000 01110101 01110011 01100101 01110010 01110011 00100000 01110100 01101111 00100000 01101010 01101111 01101011 01101001 01101110 01100111 01101100 01111001 00100000 01100001 01100100 01101111 01110000 01110100 00100000 01110100 01101000 01100101 00100000 01100011 01100001 01110000 01111001 01100010 01100001 01110010 01100001 00100000 01100001 01110011 00100000 01100001 00100000 01110011 01111001 01101101 01100010 01101111 01101100 00100000 01101111 01100110 00100000 01100011 01101100 01100001 01110011 01110011 00100000 01110011 01110100 01110010 01110101 01100111 01100111 01101100 01100101 00100000 01100001 01101110 01100100 00100000 01100011 01101111 01101101 01101101 01110101 01101110 01101001 01110011 01101101 00101110 00100000 01000010 01110010 01100001 01111010 01101001 01101100 01101001 01100001 01101110 00100000 01001100 01111001 01101101 01100101 00101101 01101100 01101001 01101011 01100101 00100000 01100010 01101111 01110010 01110010 01100101 01101100 01101001 01101111 01110011 01101001 01110011 00100000 01101100 01101001 01101011 01100101 01101100 01111001 00100000 01101001 01101110 01110110 01101111 01101100 01110110 01100101 01110011 00100000 01100011 01100001 01110000 01111001 01100010 01100001 01110010 01100001 01110011 00100000 01100001 01110011 00100000 01110010 01100101 01110011 01100101 01110010 01110110 01101111 01101001 01110010 01110011 00100000 01100001 01101110 01100100 00100000 01000001 01101101 01100010 01101100 01111001 01101111 01101101 01101101 01100001 00100000 01100001 01101110 01100100 00100000 01010010 01101000 01101001 01110000 01101001 01100011 01100101 01110000 01101000 01100001 01101100 01110101 01110011 00100000 01110100 01101001 01100011 01101011 01110011 00100000 01100001 01110011 00100000 01110110 01100101 01100011 01110100 01101111 01110010 01110011 00101110'))
print('\n')
print(decode('eWF5eXl5IEkgbG92ZSB3YXRjaGluZyBjaGFvcw=='))
print('\n')
print(decode("Hahaha! I love typing things into this string"))
print('\n')
print(decode('U29tZXRoaW5nIHNvbWV0aGluZyBBSEhISEhISEhISEhISEhIIG1vcmUgdGhpbmdzIHRvIHR5cGUgaW50byBib3ggd29vb29vb29vb29vb29vbyBJIGxvdmUgZW5jb2RpbmcgYW5kIGFsc28gZGVjb2RpbmcgdGhpbmdzIGl0cyByZWFsbHkgZWFzeSE='))

print("\n\nmultiple encoded:")

print(decode('MDEwMDEwMDAgMDExMDAwMDEgMDExMDEwMDAgMDExMDAwMDEgMDExMDEwMDAgMDExMDAwMDEgMDAxMDAwMDEgMDAxMDAwMDAgMDEwMDEwMDEgMDAxMDAwMDAgMDExMDExMDAgMDExMDExMTEgMDExMTAxMTAgMDExMDAxMDEgMDAxMDAwMDAgMDExMTAxMDAgMDExMTEwMDEgMDExMTAwMDAgMDExMDEwMDEgMDExMDExMTAgMDExMDAxMTEgMDAxMDAwMDAgMDExMTAxMDAgMDExMDEwMDAgMDExMDEwMDEgMDExMDExMTAgMDExMDAxMTEgMDExMTAwMTEgMDAxMDAwMDAgMDExMDEwMDEgMDExMDExMTAgMDExMTAxMDAgMDExMDExMTEgMDAxMDAwMDAgMDExMTAxMDAgMDExMDEwMDAgMDExMDEwMDEgMDExMTAwMTEgMDAxMDAwMDAgMDExMTAwMTEgMDExMTAxMDAgMDExMTAwMTAgMDExMDEwMDEgMDExMDExMTAgMDExMDAxMTE='))

print(decode(input('\n\nEnter your own string: ')))