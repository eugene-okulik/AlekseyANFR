my_dict = {}
my_dict['tuple'] = (1, 3, 'text', False, 2.42)
print(my_dict['tuple'][-1])

my_dict = {}
my_dict['list'] = [1, 3, 'text', False, 2.42]
my_dict['list'].append('wow')
print(my_dict['list'])
my_dict['list'].pop(1)
print(my_dict['list'])

my_dict = {}
my_dict['dict'] = {'one': 'value', 'two': 'value2', 'three': 'value3', 'four': 'value4', 'five': 'value5'}
my_dict['dict'][('i am a tuple',)] = 10101
my_dict['dict'].pop('one')
print(my_dict)

my_dict = {}
my_dict['set'] = {1, 3, 6, 7, None}
my_dict['set'].add(5000)
poped = my_dict['set'].pop()
print(my_dict)
