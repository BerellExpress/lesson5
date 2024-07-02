immutable_var = 1, True, 'name'
print(immutable_var)
# immutable_var[0] = 25 не позволяет изменить значение '1' на '25',
# т.к. у нас неизменяемый список (кортеж) из целых, а не составных элементов (1, а не [1, 2, 3])

mutable_list = [1, True, 'name']
mutable_list[2] = 'Name2'
print(mutable_list)