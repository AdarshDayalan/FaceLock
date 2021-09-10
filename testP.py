def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return (int(n * multiplier)) / multiplier

a = 4.1212

b = round(a, 1)

print(b)
