import logging
import sys

a_logger = logging.getLogger()
a_logger.setLevel(logging.DEBUG)

output_file_handler = logging.FileHandler("output.log")
stdout_handler = logging.StreamHandler(sys.stdout)

a_logger.addHandler(output_file_handler)
a_logger.addHandler(stdout_handler)


def input_data(func):
     while True:
        try:
            numbers_list = input("Podaj liczby ktore mam zsumować, w liście odzielone spacją: ")
            numbers_list = numbers_list.split(' ')
            func(numbers_list)
            break
        except ValueError:
            print("Oops!  Podaj liczbę: ")

def addition(numbers_list):

    '''Adding number from list.
    User is asked to provide number separated only by whitespace.
    Example of correctly provided data: 12 2 3'''

    result = 0
    for number in numbers_list:
        a_logger.debug(f"Dodaje {number} do {result}")
        result = result + int(number)

    return (result)



def subtraction():

    '''Subtracting 2nd value from 1st value.'''

    while True:
        try:
            a = int(input("Podaj skladnik 1: "))
            b = int(input("Podaj skladnik 2: "))
            a_logger.debug(f"Odejmuje {a} i {b}")
            result = a - b
            print(result)
            break
        except ValueError:
            print("Oops!  Podaj liczbę: ")


def multiplication():

    '''Multiplying all values from a list.
    User is asked to provide all numbers for the calculation in a list.
    Numbers should be splitted by ' ' whitespace only.
    Example of correctly provided data: 12 3 1
    Function returns result of multiplication all number.'''

    while True:
        try:
            numbers_list = input("Podaj liczby ktore mam pomnozyc ze soba, w liście odzielone spacją: ")
            result = 1
            numbers_list = numbers_list.split(' ')
            for number in numbers_list:
                a_logger.debug(f"Mnoze {number} z {result}")
                result = int(number) * result
            print(result)
            break
        except ValueError:
            print("Oops!  Podaj liczbę: ")


def division():

    '''Dividing 2 provided by users number.
    Function return result of dividng 1st value by 2nd value.'''

    while True:
        try:
            a = int(input("Podaj skladnik 1: "))
            b = int(input("Podaj skladnik 2: "))
            a_logger.debug(f"Dziele {a} przez {b}")
            result = a / b
            print(result)
            break
        except ValueError:
            print("Oops!  Podaj liczbę: ")


if __name__ == "__main__":

    calculation_type = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))

    if calculation_type == 1:
        input_data(addition)

    elif calculation_type == 2:
        subtraction()

    elif calculation_type == 3:
        multiplication()

    elif calculation_type == 4:
        division()

    elif calculation_type > 4:
        a_logger.debug(f"User provided {calculation_type} value. Selected value is out of available scope.")
        exit()
