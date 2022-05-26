from collections import deque
import numbers

numbers = deque( [1, 2, 3, 4] )
numbers.pop()
numbers.pop()
print(numbers)

numbers.pop(0)
