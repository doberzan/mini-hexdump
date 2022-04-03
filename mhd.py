# AUTHOR: TNAR5
# TITLE.: minihexdump
# DATE..: 04/03/2022
# SYNTAX: ./mhd.py <file> <bytes_per_line>
import sys

BYTES_PER_LINE = 12

def conv_hex(n):
    h = ""
    while n != 0:
        r = (n%16)
        n = int(n/16)
        if r <10:
            h += chr(48+r)
        else:
            h += chr(55+r)
    while len(h) != 2:
        h += '0'
    return h[::-1]

def print_hex(data):
    counter = 0
    top = BYTES_PER_LINE
    while counter < len(data):
        if((len(data)-counter) < BYTES_PER_LINE):
            top = (len(data)-counter)%BYTES_PER_LINE
        for i in range(0, top):
            print(conv_hex(data[counter]),end=' ')
            counter += 1
        for i in range(0, BYTES_PER_LINE-top):
            print('  ', end=' ')
        print("\t\t|", end=' ')
        for i in range((counter-top), counter):
            if (data[i] > 126) or (data[i] < 33):
                print('.', end='')
            else:
                print(chr(data[i]), end='')
        print('')

if len(sys.argv) == 1:
    print("SYNTAX: ./mhd.py <file> <bytes_per_line>")
elif len(sys.argv) == 3:
    BYTES_PER_LINE = int(sys.argv[2])

f = open(sys.argv[1], 'rb')
data = f.read()
print_hex(data)