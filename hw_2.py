# 1
str_1 = 'a'
str_2 = 'b'

int_1 = 1
int_2 = 2

float_1 = 1.5
float_2 = 2.5

bool_1 = True
bool_2 = False

list_1 = [1, 2, 3]
list_2 = [0, 1.5, 7]

dict_1 = {1: 'a', 2: 'b', 3: 'c'}
dict_2 = {1: 1, 2: True, 3: list_1}

tuple_1 = {1, 'a', True}
tuple_2 = {-3, 'X', False}

none_var = None

# 2
print(str_1 > str_2, str_1 == str_2, str_1 < str_2)
print(int_1 > int_2, int_1 == int_2, int_1 < int_2)
print(float_1 > float_2, float_1 == float_2, float_1 < float_2)
print(bool_1 > bool_2, bool_1 == bool_2, bool_1 < bool_2)
print(list_1 > list_2, list_1 == list_2, list_1 < list_2)
print(dict_1 == dict_2)
print(tuple_1 > tuple_2, tuple_1 == tuple_2, tuple_1 < tuple_2)
print(none_var == none_var, none_var == str_2, none_var == int_1)


# Робота з рядками:
# 1
num_str = 125
num_str = str(num_str)
print(type(num_str))

# 2
message = 'Hi, my name is Python!'
message.replace('y', '0')
message.replace('i', '1')

# 3
split_test = 'This is a split test'
split_list = split_test.split(' ')
print(split_list)
string_join = ' '.join(split_list)
print(string_join)

# 4
print(len(string_join))


# Робота зі списками
# 1
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)

# 2
list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])

# 3
print(list_extend.index(6))

# 4
print(len(list_append))

# Робота зі словниками
# 1
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'], dict_test['where'])

# 2
print(list(dict_test.keys()))
print(list(dict_test.values()))

# 3
print(list(dict_test.items()))
