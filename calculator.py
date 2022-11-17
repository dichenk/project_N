import math

inp = input('Введите выражение:')

str = inp.split('+')

for i in range(len(str)):
    if '*' in str[i]:
        str[i] = str[i].split('*')
        str[i] = list(map(int, str[i]))
        str[i] = math.prod(str[i])
    else: str[i] = int(str[i])

str = list(map(int, str))
print(inp, " = ", sum(str))
