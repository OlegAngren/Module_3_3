def print_params(a=1, b='строка', c=True):
    print(a, b, c)
#Эта функция имеет три параметра с значениями по умолчанию:
#a по умолчанию равно 1,
#b по умолчанию равно 'строка',
#c по умолчанию True.

# Задание 1
print_params()
print_params(10)
print_params(10, 'новая строка')
print_params(10, 'новая строка', False)
print_params(b=25)
print_params(c=[1, 2, 3])
# rint_params() будет вызывать функцию с значениями по умолчанию:
# вывод будет 1 строка True.
# print_params(10) заменит значение a на 10, остальные значения останутся по умолчанию:
# вывод будет 10 строка True.
# print_params(10, 'новая строка') заменит значения a и b:
# вывод будет 10 новая строка True.
# print_params(10, 'новая строка', False) заменит все значения:
# вывод будет 10 новая строка False.
# print_params(b=25) изменит значение b, остальные значения будут по умолчанию:
# вывод будет 1 25 True.
# print_params(c=[1, 2, 3]) изменит значение c на список, остальные значения будут по умолчанию:
# вывод будет 1 строка [1, 2, 3].

# # Задание 2
values_list = [5, "example", False]
values_dict = {"a": 10, "b": "text", "c": [4, 5, 6]}
# print_params(*values_list)
# print_params(**values_dict)
# print_params(*values_list): оператор * распаковывает элементы списка values_list и
# передает их как позиционные аргументы: вывод будет 5 example False.
# print_params(**values_dict): оператор ** распаковывает словарь values_dict и
# передает его как именованные аргументы: вывод будет 10 text [4, 5, 6].

# # Задание 3
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
# print_params(*values_list_2, 42): оператор * распаковывает элементы списка
# values_list_2 и передает их как первые два позиционные аргументы,
# затем передает 42 как третий аргумент: вывод будет 54.32 Строка 42.