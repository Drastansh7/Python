me = ['Peter', 'Portsmouth']
my_family = [['Peter', 'portsmouth'], ['Penny','Columbus'],...]


my_students = {'Fajr':'Bayonne', 'Ananya':'Delhi','Tyler':'Brooklyn'}
print(my_students['Tyler'])
my_students['Tyler'] = 'Reykjavic'
my_students['Damien'] = 'Gotham'

print(my_students)

for key in my_students.keys():
    print("Key:", key)
print('------------------')
for value in my_students.values():
    print('Value:', value)
print('------------------')
for key, value in my_students.items():
    print(key,value)

for something in my_students.items():
    print(type(something))

my_friends = {'Alan':'Newport', 'Drastansh':'Jaipur'}
new_dictionary = my_students + my_friends
print(new_dictionary)

