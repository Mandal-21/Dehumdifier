from volume_of_dehumdifier import vol_of_dehumidifier, dimensions_dehumd
from pipe_diameter import pipe_dia

filename = 'Desiccant_based_dehumidifier.txt'


def volume():
    l, w, h = dimensions_dehumd()
    total_volume = vol_of_dehumidifier(l, w, h)
    return l, w, total_volume


def height_of_sump():
    l, width, vol = volume()
    v = vol * 2 + 20
    height = round(v * (10 ** -3) / (l * width * 2 * (10 ** -6)))
    with open(filename, 'a') as project:
        project.write(f'Sump tank pipe calculations : \n\n'
                      f'\tClearance of 3cm is required for pipe from top\n'
                      f'\tHeight of Sump tank must be {height} cm \n'
                      f'\tActual usable height is {height - 3} cm \n')
    return height - 3, l * 2, v, width


def number_of_pipes_in_sump():
    dia = pipe_dia()

    h, l, v, width = height_of_sump()
    side_wall_pipe = round(h/dia - (0.3 * (h/dia - 1)))
    base_pipe = round((l - 1) - (0.3 * (l - 2)))
    return side_wall_pipe, base_pipe, v, dia, width


def print_sump_pipes():
    side_pipe, base_pipe, v, dia, width = number_of_pipes_in_sump()
    total_pipes_in_sump = side_pipe * 2 + base_pipe
    with open(filename, 'a') as project:
        project.write(f'\tTotal number of pipes in Sump tank is {total_pipes_in_sump} \n')
    return total_pipes_in_sump, v, dia, width


def vol_of_pipes():
    total_pipes_in_sump, vol, dia, width = print_sump_pipes()
    volume = round(total_pipes_in_sump * (3.1412 * (dia / 2) ** 2 * width * 3) * 10 ** -3)
    with open(filename, 'a') as project:
        project.write(f'\tVolume of pipe is {volume} litre \n\n')

# vol_of_pipes()
