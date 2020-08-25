# This will make a list of numbers from 1 to 1million
million = [value for value in range(1, 1000001)]
def count_million():
    for number in million:
        print(number)

# Adding a million numbers
total = sum(million)
print(total)