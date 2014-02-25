from bar import PowerBar, write_read

# TODO: Keep track of active profile, simple use-counter
# Disable low level access (per socket)
# Alles met use-counter=1 starten on start

bars = []

FIRST_BAR = PowerBar('/dev/ttyS0', 20, 'My Little Powerbar (MLP)')
SECOND_BAR = PowerBar('/dev/ttyUSB0', 20, 'My Large Powerbar (MLP)')

bars += [
    FIRST_BAR,
    SECOND_BAR
]

# Bar 1

LIGHT_SOLDER            = FIRST_BAR[3]
LIGHT_BAR               = FIRST_BAR[4]
LIGHT_TABLE             = FIRST_BAR[5]
LIGHT_3D                = FIRST_BAR[6]
LIGHT_ENTRANCE          = FIRST_BAR[7]
LIGHT_KITCHEN           = FIRST_BAR[8]
#LIGHT_Y                 = FIRST_BAR[9]
LIGHT_SOFA              = FIRST_BAR[10]

AUDIO_AMPLIFIER         = FIRST_BAR[13]
AUDIO_MIXER             = FIRST_BAR[14]

MONITOR_3D_1            = FIRST_BAR[16]
MONITOR_3D_2            = FIRST_BAR[17]

PRINTER                 = FIRST_BAR[18]
MONITOR_AV_1            = FIRST_BAR[19]
MONITOR_AV_2            = FIRST_BAR[20]

# Bar 2 (New space)

POWER_NW_TABLE          = SECOND_BAR[2]
POWER_NE_TABLE          = SECOND_BAR[3]
POWER_SW_TABLE          = SECOND_BAR[7]
POWER_PILLAR            = SECOND_BAR[20]

LIGHT_NE_TABLE          = SECOND_BAR[6]
LIGHT_THEATHER          = SECOND_BAR[17]
LIGHT_GLASS             = SECOND_BAR[19]

groups = {
    'entrance' : [LIGHT_ENTRANCE],
    'solder' : [LIGHT_SOLDER],
    'bar' : [LIGHT_BAR],
    'table' : [LIGHT_TABLE],
    'kitchen' : [LIGHT_KITCHEN],
    'sofa' : [LIGHT_SOFA],
    'audio' : [AUDIO_AMPLIFIER, AUDIO_MIXER],
    '3d' : [LIGHT_3D, MONITOR_3D_1, MONITOR_3D_2],
    'displays' : [MONITOR_AV_1, MONITOR_AV_2, MONITOR_3D_1, MONITOR_3D_2],
    'av' : [MONITOR_AV_1, MONITOR_AV_2],
    'printer' : [PRINTER],
    'powerwest' : [POWER_NW_TABLE, POWER_NE_TABLE, POWER_SW_TABLE,
        POWER_PILLAR],
    'lightwest' : [LIGHT_NE_TABLE, LIGHT_THEATHER, LIGHT_GLASS],
}


groups_state = {}
for _ in groups.iterkeys():
    groups_state[_] = None

GROUPS_LIGHT = ['entrance', 'solder', 'bar', 'table', '3d', 'sofa', 'kitchen',
        'lightwest']

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
        'Off' : list(groups.iterkeys()),
    },
    'allon' :{
        'On' : list(groups.iterkeys()),
    },
    'the lone solder' :{
        'Off' : 'entrance bar table 3d displays av printer'.split(),
        'On' : ['solder'],
    },
}
