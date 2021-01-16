import logging
import sys

a_logger = logging.getLogger()
a_logger.setLevel(logging.DEBUG)

output_file_handler = logging.FileHandler("output.log")
stdout_handler = logging.StreamHandler(sys.stdout)

a_logger.addHandler(output_file_handler)
a_logger.addHandler(stdout_handler)


def addition():

    while True:
        try:
            result = 0
            numbers_list = input("Podaj liczby ktore mam zsumować, w liście odzielone spacją: ")
            numbers_list = numbers_list.split(' ')
            for number in numbers_list:
                a_logger.debug(f"Dodaje {number} do {result}")
                result = result + int(number)
            print(result)
            break
        except ValueError:
            print("Oops!  Podaj liczbę: ")


def subtraction():

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
        addition()

    elif calculation_type == 2:
        subtraction()

    elif calculation_type == 3:
        multiplication()

    elif calculation_type == 4:
        division()
    elif calculation_type > 4:
        a_logger.debug(f"User provided {calculation_type} value. Selected value is out of available scope.")
        exit()
