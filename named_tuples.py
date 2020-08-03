from collections import namedtuple
# namedtuple needs to get imported

# person = ("Mark", 18, "Staff")
# print(person[0])

Person = namedtuple("Person","name age job")
me = Person("Mark",18,"Teacher")
# the dot notation part is what makes a named tuple cooler than a regular one since .name is easier than trying to figure out an index number
print(me.name)
print(me[0])

# named tuples are awesome if the data size doesn't chance, you must add all the required data to create them
# me = Person("Mark",18,"Teacher") works
# me = Person("Mark",18,None) works BUT is bad practice
# me = Person("Mark",18) doesn't
# me = Person("Mark",18,19,20,30) doesn't