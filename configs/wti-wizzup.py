from wtibar import WTIPowerBar

# This is the WTI config for Wizzup's home (http://wizzup.org)

bars = []

WTI_BAR = WTIPowerBar('10.0.0.80', name='WTI')

bars += [
    WTI_BAR,
]

def make_bar(bar, name, ident=None):
    if ident is None:
        ident = name

    __s = bar.make_socket(name, ident)
    globals()[name] = __s
    bar.sockets[name] = __s

make_bar(WTI_BAR, 'LIGHT_DESK', 1)


groups = {
    'lights' : [LIGHT_DESK],
}

groups_state = {}
for _ in groups.keys():
    groups_state[_] = None

GROUPS_LIGHT = ['lights',]

presets = {
    'lightsoff' : {
        'Off' : GROUPS_LIGHT,
        'On' : [],
    },
    'lightson' : {
        'Off' : [],
        'On' : GROUPS_LIGHT,
    },
}

