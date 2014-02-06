from bar import PowerBar, write_read

# TODO: Keep track of active profile, simple use-counter
# Disable low level access (per socket)
# Alles met use-counter=1 starten on start

bars = []

FIRST_BAR = PowerBar('/dev/ttyS0', 20, 'My Little Powerbar (MLP)')

bars += [
    FIRST_BAR,
]

LIGHT_SOLDER            = FIRST_BAR[3]
LIGHT_BAR               = FIRST_BAR[4]
LIGHT_TABLE             = FIRST_BAR[5]
LIGHT_3D                = FIRST_BAR[6]
LIGHT_ENTRANCE          = FIRST_BAR[7]

MONITOR_3D_1            = FIRST_BAR[16]
MONITOR_3D_2            = FIRST_BAR[17]

PRINTER                 = FIRST_BAR[18]
MONITOR_AV_1            = FIRST_BAR[19]
MONITOR_AV_2            = FIRST_BAR[20]

groups = {
    'lights' : [LIGHT_SOLDER, LIGHT_BAR, LIGHT_TABLE, LIGHT_3D,
        LIGHT_ENTRANCE],
    'entrance' : [LIGHT_ENTRANCE],
    'solder' : [LIGHT_SOLDER],
    'bar' : [LIGHT_BAR],
    'table' : [LIGHT_TABLE],
    '3d' : [LIGHT_3D, MONITOR_3D_1, MONITOR_3D_2],
    'displays' : [MONITOR_AV_1, MONITOR_AV_2, MONITOR_3D_1, MONITOR_3D_2],
    'av' : [MONITOR_AV_1, MONITOR_AV_2],
    'printer' : [PRINTER],
}


groups_state = {}
for x in groups.iterkeys():
    groups_state[x] = None

GROUPS_LIGHT = groups['lights']

#prefixes = {
#    'spacestate' : [
#        GROUPS_LIGHT,
#    ]
#}
#
#prefixes_state = {}
#for x in prefixes.iterkeys():
#    prefixes_state[x] = False
#
