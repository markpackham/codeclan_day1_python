# List is an Array in any other language
my_list = ["spam","ham","eggs"]
my_number_list = [4,8,15,16,23,42]

print(my_list[1])
print(my_number_list[1:4])
print(my_number_list[-1])

print(len(my_number_list))
print(sum(my_number_list))

stops = ["Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket"]
stops.append("Edinburgh Waverley")
stops.insert(0,"Queen Street")
print(stops)
print(stops.index("Croy"))
stops.insert(stops.index("Linlithgow"),"Polmont")
print(stops)
stops.remove("Haymarket")
print(stops)
stops.clear()
print(stops)
# Another way to clear our list out
stops = []
print(stops)