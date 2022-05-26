from collections import deque

numbers = deque( [1, 2, 3, 4] )
numbers.popleft()
numbers.popleft()
print(numbers)

numbers.appendleft(2)
numbers.appendleft(1)
print(numbers)
