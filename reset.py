#!/usr/bin/env python2

from __future__ import print_function

from serial import Serial

import time

def timeread(s):
    s.timeout = 6
    return s.read(10000)

def serialwrite(s, m):
    s.write(m + '\r\n')

s = Serial(port='/dev/ttyS1', baudrate=9600)

s.write('\r\n')
print(repr(timeread(s)))

s.write('Config\r\n')
print(repr(timeread(s)))

s.write('3\r\n')
m = timeread(s)

print(m)

if 'Disable Confirmation' in m:
    print('Found disable')
    s.write('Y\r\n')
else:
    s.write('N\r\n')

print(repr(timeread(s)))

s.write('4\r\n')
m = timeread(s)

print(m)

if 'Disable Status Menu' in m:
    print('Found disable')
    s.write('Y\r\n')
else:
    s.write('N\r\n')

print(repr(timeread(s)))

# Return to 'normal'
s.write('\r\n')
print(repr(timeread(s)))
