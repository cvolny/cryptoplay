import collections
import operator

START = ord('A')
END = ord('Z')
ALPHABET = list(map(chr, range(START, END+1)))
LENGTH = len(ALPHABET)
DICTIONARY = ['HELLO', 'THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL', 'ANY', 'HER', 'HIM']
FREQUENCIES = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'


def table(offset):
    """
    Given offset, rotate the alphabet by offset characters, circularly.
    """
    t = collections.deque(ALPHABET)
    t.rotate(offset)
    return list(t)

def freq(text):
    """
    Count the number of occurences of each character in a given text and return an ordered dictionary.
    """
    f = collections.defaultdict(int)
    for c in text:
        f[c] += 1
    r = sorted(f.items(), key=operator.itemgetter(1))
    return r


def encipher(cleartext, offset):
    """
    Given cleartext msg, encode using caesar cipher of provided offset.
    """
    t = table(offset)
    r = []
    for c in cleartext.upper():
        if c in ALPHABET:
            i = ord(c) - START
            r.append(t[i])
    return "".join(r)
        

def decipher(ciphertext, offset):
    """
    Given enciphered cipher, decode using caesar cipher of provided offset.
    """
    return encipher(ciphertext, -offset)


def freqcrack(ciphertext):
    """
    Given a ciphertext, perform frequency analysis and guess the offset.
    """
    f = freq(ciphertext)
    cipherletter, cipherfreq = f.pop()
    for clearletter in FREQUENCIES:
        offset = (ord(cipherletter) - ord(clearletter)) % LENGTH
        cleartext = decipher(ciphertext, offset)
        yield (offset, cipherletter, cipherfreq, cleartext)
    

def dictcrack(ciphertext):
    """
    Attempt to crack the caesar ciphered text by looking for words in dictionary.
    """
    for i in range(0, LENGTH):
        for word in DICTIONARY:
            cleartext = decipher(ciphertext, i)
            if word in cleartext:
                yield (i, cleartext, word)
                break
                
def crack(ciphertext):
    """
    Composite crack function based on frequency analysis and dictionary words.
    """
    for offset, cipherletter, cipherfreq, cleartext in freqcrack(ciphertext):
        for word in DICTIONARY:
            if word in cleartext:
                yield (offset, cleartext, cipherletter, cipherfreq, word)
                break
