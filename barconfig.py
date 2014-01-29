from bar import PowerBar, write_read

# TODO: Keep track of active profile, simple use-counter
# Disable low level access (per socket)
# Alles met use-counter=1 starten on start

bars = []

FIRST_BAR = PowerBar('/dev/ttyUSB0', 20, 'My Little Powerbar (MLP)')

bars.append([
    FIRST_BAR,
])

LIGHT_TABLE                     = FIRST_BAR[1]
LIGHT_SOLDERING                 = FIRST_BAR[2]

groups = {
    'lights' : [LIGHT_TABLE, LIGHT_SOLDERING],
}

GROUPS_LIGHT = groups['lights']

prefixes = {
    'spacestate' : [
        GROUPS_LIGHT,
    ]
}
