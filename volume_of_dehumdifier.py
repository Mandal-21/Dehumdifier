filename = 'Desiccant_based_dehumidifier.txt'


def vol_of_dehumidifier(length, width, height):
    # calculation of volume of tank
    volume = round(length * width * height * 2 * 0.001)
    with open(filename,'a') as project:
        project.write(f'\tVolume of Dehumidifier is : {volume} litre \n\n')
    return volume


def dimensions_dehumd():
    # input values of dimension
    with open(filename, 'a') as project:
        project.write('Dehumdifier Volume :\n')
    length = float(input('Enter length : '))
    width = float(input('Enter width : '))
    height = float(input('Enter height : '))
    with open(filename, 'a') as project:
        project.writelines(f'\tLength : {length}cm\n'
                           f'\tWidth : {width}cm \n'
                           f'\tHeight : {height}cm \n')
    return length, width, height


# l, w, h = dimensions_dehumd()
# vol_of_dehumidifier(l, w, h)
