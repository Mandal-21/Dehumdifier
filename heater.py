filename = 'Desiccant_based_dehumidifier.txt'


def heater():
    print('\nHeater tank dimensions\n')
    length = float(input('length of Heater tank : '))
    width = float(input('width of Heater tank : '))
    height = float(input('height of Heater tank : '))
    volume = round(float(length * width * height * 10 ** -3))
    with open(filename, 'a') as project:
        project.writelines(f'\n\nHeater Tank calculations :\n\n'
                           f'\tLength : {length}cm\n'
                           f'\tWidth : {width}cm\n'
                           f'\tHeight : {height}cm\n'
                           f'\tVolume of Heater Tank is {volume} litre')



