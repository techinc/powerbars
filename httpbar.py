#!/usr/bin/env python3

from __future__ import print_function

import requests
from vbar import VirtualPowerSocket, VirtualPowerBar

TIMEOUT = 5.  # Quite high; but this is a lot more stable.


class HTTPPowerBar(VirtualPowerBar):

    def __init__(self, host='http://powerbar.ti', name='HTTPPowerBar'):
        VirtualPowerBar.__init__(self, name)
        self.host = host

    def make_socket(self, name, ident):
        return HTTPPowerSocket(self, name, ident)


class HTTPPowerSocket(VirtualPowerSocket):

    def __init__(self, bar, name, ident):
        VirtualPowerSocket.__init__(self, bar, name, ident)

    def set_state(self, state):
        s = 'On' if state else 'Off'

        r = requests.post('%s/%s/%s' % (self.bar.host, self.bar.name,
                                        self.ident),
                          data={'state': s}, timeout=TIMEOUT)

        if r.status_code == 200:
            self.state = state
