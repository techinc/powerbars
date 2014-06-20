#!/usr/bin/env python3

from __future__ import print_function

import time

from vbar import VirtualPowerBar, VirtualPowerSocket

VIRTUAL = False

if not VIRTUAL:
    from serial import Serial
else:
    print('WARNING: Virtual mode activated')
    class Serial(object):
        def __init__(self, **kwargs):
            pass

        def __getattr__(self, attr):
            return lambda self, **kwargs: None

def write_read(s, m):
    s.write(m)
    s.timeout = 10
    l = len(m) + len('RPC-28A>\r')
    t1 = time.time()
    f = s.read(l)
    return f


class PowerBar(VirtualPowerBar):
    def __init__(self, path, sn=20, name='Default PowerBar name'):
        VirtualPowerBar.__init__(self, name)

        s = Serial(port=path, baudrate=9600)

        # Just in case
        s.setDsrDtr(False)
        s.setRtsCts(False)
        s.setXonXoff(False)

        self.s = s
        self.sockets = [PowerSocket(self, _) for _ in xrange(sn)]


class PowerSocket(VirtualPowerSocket):
    def __init__(self, bar, num, name=None):
        VirtualPowerSocket.__init__(self, bar, num, name)

    def set_state(self, state):
        s = 'On' if state else 'Off'
        self.state = state
        print('Setting', self.num, 'to', s)
        m = '%s %d\r\n' % (s, self.num)
        write_read(self.bar.s, m)

on = True
stat = 'On' if on else 'Off'

if __name__ == '__main__':
    b = PowerBar('/dev/ttyUSB0', 20, 'Texting')

    write_read(b.s, '\r\n')
    for s in b.sockets:
        s.set_state(on)
