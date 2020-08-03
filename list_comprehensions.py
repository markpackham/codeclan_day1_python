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

# one liner solution for evil people
print([number ** 2 for number in range(1,11) if number % 2 == 0])


words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
letters = [word[0].lower() for word in words]
# ['t', 'q', 'b', 'f', 'j', 'o', 't', 'l', 'd']
print(letters)