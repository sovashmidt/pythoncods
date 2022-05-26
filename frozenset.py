# https://t.me/c/1676257985/179
vowels = ('a', 'e', 'i', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())
fSet.add('v')
person = {"name": "John", "age": 23, "sex": "male"}
fSet = frozenset(person)
print('The Frozen set is:', fSet)