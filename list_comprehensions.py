numbers = range(1,11)
evens_squared = []
for number in numbers:
    if number % 2 == 0:
        evens_squared.append(number ** 2)

print(evens_squared)

# better solution thanks to list comprehensions
numbers = range(1,11)
evens_squared = [number ** 2 for number in numbers if number % 2 == 0]
print(evens_squared)
