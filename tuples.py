person = ["Mark",20,"Typist",False]
print(person)
print(person[0])

# Use tuple when data must NEVER change
# The data is made immutable
person = ("Mark",20,"Typist",False)
print(person[0])
# Check how many times Mark is in the tuple
print(person.count("Mark"))

fruits = ("apple", "banana","banana","banana","orange")
print(fruits.count("banana"))

print(person.index("Typist"))

print(len(person))