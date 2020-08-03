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