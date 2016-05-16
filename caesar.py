import collections

START = ord('A')
END = ord('Z')
ALPHABET = map(chr, range(START, END+1))
LENGTH = len(ALPHABET)
DICTIONARY = ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL', 'ANY', 'HER', 'HIM']


def table(offset):
    """
    Given offset, rotate the alphabet by offset characters, circularly.
    """
    t = collections.deque(ALPHABET)
    t.rotate(offset)
    return list(t)


def encode(msg, offset):
    """
    Given cleartext msg, encode using caesar cipher of provided offset.
    """
    t = table(offset)
    r = []
    for c in msg.upper():
        if c in ALPHABET:
            i = ord(c) - START
            r.append(t[i])
    return "".join(r)
        
    
    
def decode(cipher, offset):
    """
    Given enciphered cipher, decode using caesar cipher of provided offset.
    """
    return encode(cipher, -offset)

def crack(cipher):
    """
    Attempt to crack the caesar ciphered text by looking for words in dictionary.
    """
    for i in range(0, LENGTH):
        for word in DICTIONARY:
            clear = decode(cipher, i)
            if word in clear:
                yield (i, clear)
                break
    
    

msg = "Hello World!"
offset = 17
cipher = encode(msg, offset)
clear = decode(cipher, offset)
print(cipher)
print(clear)

for guess in crack(cipher):
    print("%d: %s" % guess)
else:
    print("Didn't make any guesses....")
