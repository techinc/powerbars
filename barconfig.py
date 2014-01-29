from bar import PowerBar, write_read

bars = []

bars.append(PowerBar('/dev/ttyUSB0', 2, 'My Little Powerbar (MLP)'))

FIRST_BAR = bars[0]

LIGHT_TABLE                     = FIRST_BAR[0]
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
