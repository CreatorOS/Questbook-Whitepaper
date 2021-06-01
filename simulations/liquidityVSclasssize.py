import math
data = {}
for classsize in range(1,100):
    a0 = 0.0
    for iteration in range(1,100): 
        a0 = ( -0.2 * math.log(classsize, 2.718) + 0.6 ) + a0
        liquidity = 10*a0*(1-1/classsize)
        if iteration not in data.keys():
            data[iteration] = []
        data[iteration].append(liquidity)

keys = list(data.keys())
keys.sort()
for iteration in keys:
    line = ""
    for liquidity in data[iteration]:
        line+=str(liquidity)+","
    print(line)


