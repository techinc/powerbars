from bar import BayTechPowerBar

# This is the 'aux' config for TechInc (http://techinc.nl)
# The config for the 'main' room can be found in configs/techinc-main.py

bars = []

AUX_BAR = BayTechPowerBar('/dev/ttyS1', name='AUX')

bars += [
    AUX_BAR
]

def make_bar(bar, name, ident=None):
    if ident is None:
        ident = name

    __s = bar.make_socket(name, ident)
    globals()[name] = __s
    bar.sockets[name] = __s

make_bar(AUX_BAR, 'W_POWER_NW_TABLE', 2)
make_bar(AUX_BAR, 'W_POWER_SW_TABLE', 7)
make_bar(AUX_BAR, 'W_POWER_MAIN_TABLE', 3)
make_bar(AUX_BAR, 'W_POWER_PILLAR', 20)

make_bar(AUX_BAR, 'W_AIR_FAN', 6)

make_bar(AUX_BAR, 'W_LIGHT_TABLE', 4)
make_bar(AUX_BAR, 'W_LIGHT_TL_DOOR', 14)
make_bar(AUX_BAR, 'W_LIGHT_SOLDER', 16)
make_bar(AUX_BAR, 'W_LIGHT_THEATER', 17)
make_bar(AUX_BAR, 'W_LIGHT_GLASS', 19)


groups = {
}

groups_state = {}
for _ in groups.keys():
    groups_state[_] = None

GROUPS_LIGHT = []

presets = {
}

