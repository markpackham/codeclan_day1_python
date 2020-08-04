  
# Meet the Beatles:

beatles = [
    {"name": "John Lennon", "birth_year": 1940, "death_year": 1980, "instrument": "piano"},
    {"name": "Paul McCartney", "birth_year": 1942, "death_year": None, "instrument": "bass"},
    {"name": "George Harrison", "birth_year": 1943, "death_year": 2001, "instrument": "guitar"},
    {"name": "Ringo Starr", "birth_year": 1940, "death_year": None, "instrument": "drums"}
]

# Use the `beatles` list above to answer the following questions:

# 1. John Lennon also plays guitar. Access the `instrument` key in his dictionary and change its value:
beatles[0]["instrument"] = "piano & guitar"
print(beatles[0]["instrument"])

# Better solution using list for all of them rather than just 1 string
beatles[0]["instrument"] = ["piano, guitar"]
beatles[1]["instrument"] = ["bass"]
beatles[2]["instrument"] = ["guitar"]
beatles[3]["instrument"] = ["drums"]
print(beatles[0]["instrument"])


# 2. Write a function which takes in the list of band members as a parameter,
#    and returns a list of all the Beatles' names:
# Expected result: ['John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr']
# def get_names(members):
#     names = []
#     for member in members:
#         names.append(member["name"])
#     return names

# print(get_names(beatles))

def get_names_comprehension(members):
    return [member["name"] for member in members]
print(get_names_comprehension(beatles))

# 3. Write a function which takes in the list of band members as a parameter,
#    and returns a list of the members who are still alive
#    (i.e. they have no value for `death_year`)
#    Return the full dictionary for each member
# Expected result: [
#    {'name': 'Paul McCartney', 'birth_year': 1942, 'death_year': None, 'instrument': 'bass'},
#    {'name': 'Ringo Starr', 'birth_year': 1940, 'death_year': None, 'instrument': 'drums'}
# ]

# def get_alive(members):
#     alive = []
#     for member in members:
#         if member["death_year"] == None:
#             alive.append(member)
#     return alive

# print(get_alive(beatles))


def get_alive_comprehension(members):
    return [member for member in members if member["death_year"] == None]
print(get_names_comprehension(beatles))

# 4. Combine the above two functions to return the names of all the members who are alive:
# Expected result: ['Paul McCartney', 'Ringo Starr']

alive_beatles = get_alive_comprehension(beatles)
print(get_names_comprehension(alive_beatles))