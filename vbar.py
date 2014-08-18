#!/usr/bin/env python3

from __future__ import print_function


class VirtualPowerBar(object):

    def __init__(self, name):
        self.name = name

        self.sockets = {}

    def make_socket(self, name, ident):
        """
        This function is used to create PowerSocket instances in barconfig
        """
        raise NotImplementedException('make_socket')


class VirtualPowerSocket(object):

    def __init__(self, bar, name, ident):
        self.bar = bar
        self.name = name
        self.ident = ident
        self.state = None

        self.refcount = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'PowerSocket (%s)' % self.name

    def set_state(self, state):
        raise NotImplementedException('set_state')
