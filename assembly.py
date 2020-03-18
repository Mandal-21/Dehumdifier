"""Output of dimensions of container"""
from sump_tank import vol_of_pipes
from no_of_pipes_in_dehumdifier import dehumdifier_pipes
from heater import heater

filename = 'Desiccant_based_dehumidifier.txt'


def vol_and_dimensions():
    with open(filename, 'w') as project:
        project.write('Calculations : \n\n')
    vol_of_pipes()
    dehumdifier_pipes()
    heater()


vol_and_dimensions()
