#!/usr/bin/env python3

from __future__ import print_function

from httpbar import HTTPPowerBar

from barconfig import *


class Button(object):
    def __init__(self, parent, cb=None):
        self.__state = False
        self.parent = parent
        self.cb = cb

    def __bool__(self):
        return self.state()

    def __nonzero__(self):
        return self.__bool__()

    def state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state
        if self.cb:
            self.cb(self)


normal_actions = {
    '0': lambda state: AUX_BAR[6].set_state(state),
}


def to_byte(b):
    return ''.join(map(lambda x: '1' if x else '0', b))[::-1]


def energise_cb(self):
    if self:
        byte = self.parent.byte + to_byte(self.parent.bitswitches)
        print('Bytes:', byte)
        if self.parent.usage:
            print('Expert mode: %d' % int(byte, 2))

            self.parent.byte = ""
        else:
            print('Normal mode; pass')

        self.set_state(False)


def status_cb(self):
    print('Status callback')


def usage_cb(self):
    print('Usage callback')


def next_byte_cb(self):
    if not self.parent.usage:
        return

    if self:
        self.parent.byte += to_byte(self.parent.bitswitches)
        self.set_state(False)


def bit_cb(self):
    for idx, x in enumerate(self.parent.bitswitches):
        if self == x:
            print('Found (%d): %s %s' % (idx, bool(x), x))

            if not self.parent.usage:
                print('Normal action:', idx)
                normal_func = normal_actions[str(idx)]
                print('normal_func:', normal_func)
                print('normal_func():', normal_func(bool(self)))

            break


class ButtonBoard(object):
    def __init__(self):
        self.bitswitches = [Button(self, bit_cb) for _ in range(8)]
        self.energise = Button(self, energise_cb)
        self.next_byte = Button(self, next_byte_cb)
        self.status = Button(self, status_cb)
        self.usage = Button(self, usage_cb)

        self.byte = ""


bb = ButtonBoard()

bb.usage.set_state(False)

#bb.bitswitches[0].set_state(False)
bb.bitswitches[0].set_state(True)

#bb.next_byte.set_state(True)
#bb.bitswitches[0].set_state(False)
#bb.bitswitches[7].set_state(True)
#bb.energise.set_state(True)
