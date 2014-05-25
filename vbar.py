class VirtualPowerBar(object):
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.sockets)

    def __getitem__(self, index):
        return self.sockets[index - 1]

    def __iter__(self):
        return iter(self.sockets)

class VirtualPowerSocket(object):
    def __init__(self, bar, num, name=None):
        """
        Name is purely for descriptive purposes
        """
        self.bar = bar
        self.num = num + 1
        self.name = 'Socket %d' % self.num if not name else name

        self.state = None

        self.refcount = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'PowerSocket (%s)' % self.name

    def set_state(self, state):
        raise NotImplementedException('set_state')
