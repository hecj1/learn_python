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

print('How many cookies do you have?')
numCookies = input()
try:
    if int(numCookies) >= 4:
        print('You must be a cookie monster')
    else:
        print('You\'re not eating enough cookies')
except ValueError:
    print('You did\'t enter a number for your cookies')