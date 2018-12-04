'''
modul to test deliverly service
'''


import json
import re
import numpy as np

class Error(Exception):
    """Base class for exceptions in this module."""
pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

def __init__(self, expr):
        self.expr = expr

def get_address_if(fn):
    def wrapper(*args, **kwargs):
        for x in args:
            if x == 'test':
                break
        return fn(*args, **kwargs)
    return wrapper


def check_address(to_check: str):
    if type(to_check) !=str:
        raise InputError("Некорректный тип данных")
    if re.findall(r'[^\w\s.]', to_check):
        raise InputError("Ошибки в названиии " + to_check)

def to_data(address: str)-> str:
    if type(address) != str:
        raise InputError("Некорректный тип данных")
    term = address[-4:]
    if term == 'json':
        with open(address,'r',encoding="utf-8") as fp:
            my_json = json.loads(json.load(fp))
    else:
        my_json = json.loads(address)
    return my_json

@get_address_if
def get_address(address)-> str:
    '''
    Return random address
:param address: input address, it can be both file.json or string as json
:return: random address
    '''
    my_json = to_data(address)
    if not my_json:
        raise InputError("Некорректный тип данных")

    if not (my_json['Страны'] and my_json['Города'] and my_json['Улицы']):
        raise InputError("Ошибки в названиии ")
    countries = my_json['Страны']
    cities = my_json['Города']
    streets = my_json['Улицы']
    i = 0
    while i < 10:
        if type(countries) == str:
            country = countries
        else:
            country = countries[np.random.randint(0,len(countries))]
        if type(cities) == str:
            city = cities
        else:
            city = cities[np.random.randint(0,len(cities))]

        if type(streets) == str:
            street = streets
        else:
            street = streets[np.random.randint(0,len(streets))]
        check_address(city)
        check_address(country)
        check_address(street)
        house = str(np.random.randint(0,100))
        flat = str(np.random.randint(0,1000))
        has_corp = np.random.randint(0,2)
        if has_corp:
            corp = str(np.random.randint(0,20))

        yield " ".join([country, city, street,"д." + house,"корп." + corp if has_corp else '',"кв." + flat])


if __name__ == "__main__":
    with open('path\data.json', 'w', encoding="utf-8") as fp:
        my_json = json.dumps({'Страны':('Россия'),'Города': ('Спб'), 'Улицы':('Моховая ул.','Набережная реки Фонтанки','Невский пр.')},ensure_ascii=False)
        json.dump(my_json, fp)
        fp.close()

    with open('path\data.json','r',encoding="utf-8") as fp:
        dictionary = json.load(fp)
        #print(dictionary)
    fp.close()

    t=get_address(dictionary)
    print(next(t))
    print(next(t))
    get_address('path\data.json')
    print(next(t))
    print(next(t))