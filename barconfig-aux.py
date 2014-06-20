from bar import PowerBar

bars = []

AUX_BAR = PowerBar('/dev/ttyS1', 20, 'AUX')

bars += [
    AUX_BAR
]

def make_bar(name, bar, idx):
    globals()[name] = bar[idx]
    bar[idx].name = name

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
}


groups_state = {}
for _ in groups.keys():
    groups_state[_] = None

GROUPS_LIGHT = []

presets = {
}
