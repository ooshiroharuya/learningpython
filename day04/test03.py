import os

print(list(range(1, 11)))

print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'abc' for n in 'xyz'])

print([d for d in os.listdir()])

L = ['Hello', "World", 18, 'Apple', None]

print([s.lower() for s in L if isinstance(s, str)])