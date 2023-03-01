"==================JSON==================="
# JavaScript Object Notation - еденый формат,в котором хранится только те типы данных
# которые есть во всех яп поддерживающие json

# числа int , float
# строки str
# словари dict
# булевые значение True, False
# списки list
# пустое значение None

import json

# сериализация - перевод из python в json 
# dump -  функция которая переводит python obj в json строку и записывает в файл
# dumps - функция которая переводит python obj в json строку

# десерализация - перевод из json в python
# load - функция , которая переводит json строку в python обьект и записывает в файл

# loads - функция , которая переводит json строку в python обьект

python_list = [1,2,3]
json_list = json.dumps(python_list)
print(type(python_list)) # list
print(type(json_list)) # str

print(type(python_list)) # [1,2,3]
print(type(json_list)) # "[1,2,3]"



json_dict = '{"a":1, "b":2}'
python_dict = json.loads(json_dict)

print(type(json_dict)) # str
print(type(python_dict)) # dict




list_ = [
    1,2,3,
    4.6,
    (1,2,3),
    {'A':1},
    'hello',
    True,False,None
]

with open("test.json", "w") as file:
    json.dump(list_, file)






with open("test.json", "r") as file:
    res = json.load(file)

print(res)
# [1, 2, 3, 4.6, [1, 2, 3], {'A': 1}, 'hello', True, False, None]