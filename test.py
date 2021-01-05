
def to_be_filled():
    return 'l1c0'

variable_dict = {'l0c0': 0, 'l0c1': 0, 'l1c0': 0, 'l1c1': 0}

for key, value in variable_dict():
    while(value < 6):





variable_dict = {'l0c0': 0, 'l0c1': 0, 'l1c0': 0, 'l1c1': 0}

for key, value in variable_dict.items():
    if value < 6:
        for key, value in variable_dict.items():
            fill_form(b, to_be_filled(), 'Fulano', 'senha1234')
            value += 1
            sleep(1)

    """
while 5 not in variable_dict.values():
    fill_form(b, to_be_filled(), 'Fulano', 'senha1234')
    sleep(1)
    if not to_be_filled() in variable_dict.keys():
        variable_dict[to_be_filled()] = 1
    else:
        variable_dict[to_be_filled()] += 1
    """

    """
    form = to_be_filled
    fill_form(b, to_be_filled(), 'Fulano', 'senha1234')
    variable_dict[form] += 1
    sleep(1)
    """