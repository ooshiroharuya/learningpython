from day04.mytools import normalize, prod

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

i = prod([3, 5, 7, 9])

print(i)

i = 'name.great'
s = i.split(".")

print(s)