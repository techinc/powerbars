#!/usr/bin/env python3

from __future__ import print_function

# from barconfig import *
# from httpbar import HTTPPowerBar


class Button(object):

    def __init__(self, parent, cb=None):
        self.__state = False
        self.parent = parent
        self.cb = cb

    # Since Python 3.x
    def __bool__(self):
        return self.state()

    # Python 2.x support (equivalent of __bool__)
    def __nonzero__(self):
        return self.__bool__()

    def state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state
        if self.cb:
            self.cb(self)


normal_actions = [
    # lambda state: <bar>.<socket[number>].set_state(state)
    lambda state: 'This is 0',
    lambda state: 'This is 1',
    lambda state: 'This is 2',
    lambda state: 'This is 3',
    lambda state: 'This is 4',
    lambda state: 'This is 5',
    lambda state: 'This is 6',
    lambda state: 'This is 7',
]


def to_byte(b):
    return ''.join(map(lambda x: '1' if x else '0', b))[::-1]


def energise_cb(self):
    if self:
        byte = self.parent.byte + to_byte(self.parent.bitswitches)

        # Only in expert mode
        if self.parent.usage:
            print('Expert mode, action number: %d' % int(byte, 2))

            self.parent.byte = ""

        # Turn ourselves off again.
        self.set_state(False)


def status_cb(self):
    print('Status callback')


def usage_cb(self):
    print('Usage callback. Changed to:', bool(self))
    self.parent.byte = ''


def next_byte_cb(self):
    # Only in export mode
    if not self.parent.usage:
        return

    # Append to byte if state is 'On'
    if self:
        self.parent.byte += to_byte(self.parent.bitswitches)
        self.set_state(False)


def bit_cb(self):
    # Get our own index
    for idx, x in enumerate(self.parent.bitswitches):
        if self == x:
            # Only in normal mode
            if not self.parent.usage:
                normal_func = normal_actions[idx]
                if normal_func:
                    print('Normal mode, action number: %d -> %s' %
                          (idx, normal_func(bool(self))))
                else:
                    print('Normal mode, action number: %d -> No function'
                          % (idx))

            break


class ButtonBoard(object):

    def __init__(self):
        self.bitswitches = [Button(self, bit_cb) for _ in range(8)]
        self.energise = Button(self, energise_cb)
        self.next_byte = Button(self, next_byte_cb)
        self.status = Button(self, status_cb)
        self.usage = Button(self, usage_cb)

        self.byte = ''


if __name__ == '__main__':

    bb = ButtonBoard()

    # Normal mode.
    bb.usage.set_state(False)

    bb.bitswitches[4].set_state(True)

    # Expert mode.
    bb.usage.set_state(True)

    bb.bitswitches[0].set_state(False)

    # Get result
    bb.energise.set_state(True)

    # Store byte, start with next
    bb.next_byte.set_state(True)

    bb.bitswitches[0].set_state(True)
    bb.bitswitches[7].set_state(True)

    # Get result
    bb.energise.set_state(True)
