from collections import defaultdict
dd = defaultdict(list)
dd['key'].append(1)
dd

dd['key'].append(2)
dd

dd['key'].append(3)
dd

dep = [('Sales', 'John Doe')
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jon Doe')
       ('Marketing', 'Elizabet Smith')
       ('Marketing', 'Adam Doe')]
dep_dd = defaultdict(list)
for departament, employee in dep:
    dep_dd[departament].append(enplayee)