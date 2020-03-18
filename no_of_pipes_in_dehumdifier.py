filename = 'Desiccant_based_dehumidifier.txt'


def no_of_pipes(dia, length, width, height):
    """perimeter available for piping / diameter of each pipe"""
    pipes = length + width + height / dia
    with open(filename, 'a') as project:
        project.writelines(f'\tNo of pipes available in one compartment : {float(pipes)} \n')


def pipe_considering_clearance(dia, length, width, height):
    """considering 3mm clearance"""
    pipe_in_wall = round(height - (0.3 * (height - 1)))
    pipe_in_base = round(width - (0.3 * (width - 1)))
    total_pipe = 4 * (pipe_in_base + 2 * pipe_in_wall)
    with open(filename, 'a') as project:
        project.writelines(f'\tNo of pipes in side wall are {pipe_in_wall}' + '\n'
                           f'\tNo of pipes in base are {pipe_in_base}' + '\n'
                           f'\tTotal four compartment(Dehumdifier*2 and Regenrator*2)\n'
                           f'\tTherefore total no of pipes {total_pipe}')


def perimeter():
    print('\nPerimeter dimensions of Dehumidifier Tank :')
    dia = float(input('\nEnter diameter of pipe : '))
    length = float(input('Enter length of dehumidifier for perimeter : '))
    width = float(input('Enter width of dehumidifier for perimeter : '))
    height = float(input('Enter height of dehumidifier for perimeter : '))
    with open(filename, 'a') as project:
        project.writelines(f'\tDiameter : {dia}cm \n'
                           f'\tLength : {length}cm\n'
                           f'\tWidth : {width}cm \n'
                           f'\tHeight : {height}cm \n')
    return dia, length, width, height


def dehumdifier_pipes():
    with open(filename, 'a') as project:
        project.write('Calculations of pipes in Dehumdifier are :\n\n')
    d, l, w, h = perimeter()
    no_of_pipes(d, l, w, h)
    pipe_considering_clearance(d, l, w, h)
