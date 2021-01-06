import logging
logging.basicConfig(level=logging.DEBUG)


def addition():
    a = int(input("Podaj skladnik 1: "))
    b = int(input("Podaj skladnik 2: "))
    logging.debug(f" Dodaje {a} i {b}")
    result = a + b
    print (result)

def subtraction():
    a = int(input("Podaj skladnik 1: "))
    b = int(input("Podaj skladnik 2: "))
    logging.debug(f" Odejmuje {a} i {b}")
    result = a - b
    print (result)

def multiplication():
    
    a = int(input("Podaj skladnik 1: "))
    b = int(input("Podaj skladnik 2: "))
    logging.debug(f" Mnoze {a} i {b}")
    result = a * b 
    print (result)

def division():
    a = int(input("Podaj skladnik 1: "))
    b = int(input("Podaj skladnik 2: "))
    logging.debug(f" Dziele {a} przez {b}")
    result = a / b 
    print (result)

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
        print("Nie umiem wykonać tej operacji")