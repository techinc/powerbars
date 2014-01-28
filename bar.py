import time
from serial import Serial

def write_read(s, m):
    s.write(m)
    s.timeout = 10
    l = len(m) + len('RPC-28A>\r')
    #print 'Reading:', l
    t1 = time.time()
    f = s.read(l)
    #print time.time() - t1
    #print f
    return f


class PowerBar(object):
    def __init__(self, path, sn):
        s = Serial(port=path, baudrate=9600)

        # Just in case
        s.setDsrDtr(False)
        s.setRtsCts(False)
        s.setXonXoff(False)

        self.s = s
        self.sockets = [PowerSocket(self, _) for _ in xrange(sn)]

class PowerSocket(object):
    def __init__(self, bar, num):
        self.bar = bar
        self.num = num + 1

    def set_state(self, state):
        s = 'On' if state else 'Off'
        m = '%s %d\r\n' % (s, self.num)
        write_read(self.bar.s, m)

on = True
stat = 'On' if on else 'Off'

if __name__ == '__main__':
    b = PowerBar('/dev/ttyUSB0', 20)

    write_read(b.s, '\r\n')
    for s in b.sockets:
        s.set_state(on)
