#!/usr/bin/env python3

from __future__ import print_function

from bar import PowerBar
from httpbar import HTTPPowerBar

# TODO: Keep track of active profile, simple use-counter
# Disable low level access (per socket)
# Alles met use-counter=1 starten on start

bars = []

FIRST_BAR = PowerBar('/dev/ttyS0', 20, 'MLP')
AUX_BAR = HTTPPowerBar(host='http://10.0.20.41:5000', sn=20, name='AUX')

bars += [
    FIRST_BAR,
    AUX_BAR
]

def make_bar(name, bar, idx):
    globals()[name] = bar[idx]
    bar[idx].name = name

# Bar 1

make_bar('LIGHT_MAKERLANE', FIRST_BAR, 3)
make_bar('LIGHT_MAKERTABLE', FIRST_BAR, 4)
make_bar('LIGHT_TABLE', FIRST_BAR, 5)
make_bar('LIGHT_CRAFT', FIRST_BAR, 6)
make_bar('LIGHT_ENTRANCE', FIRST_BAR, 7)
make_bar('LIGHT_KITCHEN', FIRST_BAR, 8)
make_bar('LIGHT_SOFA', FIRST_BAR, 10)

make_bar('AUDIO_AMPLIFIER', FIRST_BAR, 13)
make_bar('AUDIO_MIXER', FIRST_BAR, 14)

make_bar('MONITOR_3D_1', FIRST_BAR, 16)
make_bar('MONITOR_3D_2', FIRST_BAR, 17)

make_bar('PRINTER', FIRST_BAR, 18)
make_bar('MONITOR_AV_1', FIRST_BAR, 19)
make_bar('MONITOR_AV_2', FIRST_BAR, 20)

make_bar('W_POWER_NW_TABLE', AUX_BAR, 2)
make_bar('W_POWER_SW_TABLE', AUX_BAR, 7)
make_bar('W_POWER_MAIN_TABLE', AUX_BAR, 3)
make_bar('W_POWER_PILLAR', AUX_BAR, 20)

make_bar('W_LIGHT_TABLE', AUX_BAR, 4)
make_bar('W_LIGHT_TL_DOOR', AUX_BAR, 14)
make_bar('W_LIGHT_SOLDER', AUX_BAR, 16)
make_bar('W_LIGHT_THEATER', AUX_BAR, 17)
make_bar('W_LIGHT_GLASS', AUX_BAR, 19)


groups = {
    'general' : [LIGHT_ENTRANCE, LIGHT_KITCHEN, LIGHT_SOFA, LIGHT_TABLE],
    'craft' : [LIGHT_CRAFT],
    'audio' : [AUDIO_AMPLIFIER, AUDIO_MIXER],
    'makerlane' : [LIGHT_MAKERLANE, LIGHT_MAKERTABLE, MONITOR_3D_1, MONITOR_3D_2],
    'displays' : [MONITOR_AV_1, MONITOR_AV_2, MONITOR_3D_1, MONITOR_3D_2],
    'av' : [MONITOR_AV_1, MONITOR_AV_2],
    'printer' : [PRINTER],

    'soldering' : [W_POWER_NW_TABLE, W_POWER_SW_TABLE, W_LIGHT_SOLDER],
    'powerwest' : [W_POWER_NW_TABLE, W_POWER_MAIN_TABLE, W_POWER_SW_TABLE, W_POWER_PILLAR],
    'lightwest' : [W_LIGHT_TABLE, W_LIGHT_THEATER, W_LIGHT_GLASS, W_LIGHT_SOLDER],
    'tlwest'    : [W_LIGHT_TL_DOOR],
}


groups_state = {}
for _ in groups.keys():
    groups_state[_] = None

GROUPS_LIGHT = ['general', 'craft', 'makerlane', 'lightwest', 'tlwest']

presets = {
    'lightsoff' : {
        'Off' : GROUPS_LIGHT,
        'On' : [],
    },
    'lightson' : {
        'Off' : [],
        'On' : GROUPS_LIGHT,
    },
    'alloff' :{
        'Off' : list(groups.keys()),
    },
    'allon' :{
        'On' : list(groups.keys()),
    },
}
