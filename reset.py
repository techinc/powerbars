#!/usr/bin/env python2

from __future__ import print_function

from serial import Serial

import time
import sys

def resetserial(name):

    def timeread(s):
        s.timeout = 6
        return s.read(10000)
    
    def serialwrite(s, m):
        s.write(m + '\r\n')
    
    s = Serial(port='/dev/ttyS1', baudrate=9600)
    
    s.write('\r\n')
    m = timeread(s)
    #print(repr(m))
    
    s.write('Config\r\n')
    m = timeread(s)
    #print(repr(m))
    
    s.write('3\r\n')
    m = timeread(s)
    
    #print(m)
    
    if 'Disable Confirmation' in m:
        #print('Found disable')
        s.write('Y\r\n')
    else:
        s.write('N\r\n')
    
    m = timeread(s)
    #print(repr(m))
    
    s.write('4\r\n')
    m = timeread(s)
    
    #print(m)
    
    if 'Disable Status Menu' in m:
        #print('Found disable')
        s.write('Y\r\n')
    else:
        s.write('N\r\n')
    
    m = timeread(s)
    #print(repr(m))
    
    # Return to 'normal'
    s.write('\r\n')
    m = timeread(s)
    #print(repr(m))

if __name__ == '__main__':
    resetserial(sys.argv[1])

