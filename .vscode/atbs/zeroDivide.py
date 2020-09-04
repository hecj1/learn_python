# practicing exception handling, will use the zero divide exception

def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide be zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))