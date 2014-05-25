import requests
from vbar import VirtualPowerSocket, VirtualPowerBar

TIMEOUT = 0.5

class HTTPPowerBar(VirtualPowerBar):
    def __init__(self, host='http://powerbar.ti', sn=20, name='HTTPPowerBar'):
        VirtualPowerBar.__init__(self, name)
        self.host = host

        self.sockets = [HTTPPowerSocket(self, _) for _ in xrange(sn)]

    def __len__(self):
        return len(self.sockets)

    def __getitem__(self, index):
        return self.sockets[index - 1]

    def __iter__(self):
        return iter(self.sockets)

class HTTPPowerSocket(VirtualPowerSocket):

    def __init__(self, bar, num, name=None):
        VirtualPowerSocket.__init__(self, bar, num, name=None)

        self.bar = bar
        self.num = num + 1
        self.name = 'Socket %d' 

    def set_state(self, state):
        s = 'On' if state else 'Off'

        r = requests.post('%s/%s/%d' % (self.bar.host, self.bar.name, self.num - 1),
                data = {'state' : s}, timeout=TIMEOUT)

        if r.status_code == 200:
            self.state = state
