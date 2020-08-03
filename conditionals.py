today = "Saturday"

# We just use the keywords "or" "and" rather than || or &&
if(today == "Saturday" or today == "Sunday"):
    print("Let's have a long-lie")

if(today == "Saturday" and today == "Sunday"):
    print("This will not print")

print(5 != 10)
print(5 <= 5)

if today == "Sunday":
    print("Yey it is Sunday")
elif today == "Friday":
    print("TGIF")
else:
    print("On no work awaits")

