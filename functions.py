def say_hello():
    return "Hello World"
print(say_hello())

# Formal Parameter
def set_alarm(day):
    if day == "Saturday" or day == "Sunday":
        return "Attemd Mass"
    else:
        return "Wake up"

# Actual Parameter
print(set_alarm("Sunday"))


def add(a,b):
    return a + b
result = add(6,8)
print(result)


name = "Mark"
def say_hello():
    name = "Not Mark"
    # the f when printing makes it a formatted string, think printf in C
    print(f"Hello {name}!")

# prints "Mark"
print(name)
# prints "Not Mark" since Mark gets overwritten
say_hello()


def say_hello(name = "Billy"):
    print(f"Hello {name}!")
# the default gets printed if nothing entered, handy to avoid None
say_hello()


# Keyword arguments (set the order things get done)
# VERY useful for divides where order matters
def add (a, b):
    return a + b

result = add(b = 5, a = 7)
print(result)



def divide (a, b):
    return a / b

result = divide(b = 5, a = 10)
print(result)

# Deconstruction (get the stuff out of the Dictionary)
numbers = {
    "a":100,
    "b":5
}
def divide (a, b):
    return a / b
# same as doing divide(a = 100, b = 5)
# double star targets keyword arguments **
# a single star would be for index arguments *
result = divide(**numbers)
print(result)



def add(a, b = 2):
    return a + b

# result = add(a = -2) # 0
# result = add(b = 3) # breaks
# result = add(2, b = 4) # 6
# result = add(b = 4, 2) # breaks ALWAYS start with positional argument over keyword argument, position first keyword second
# result = add(a = 2, 4) # breaks ALWAYS start with positional argument over keyword argument
print(result)