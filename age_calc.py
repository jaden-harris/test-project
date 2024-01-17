age = int(input("How old are you?\n"))

decades = age//2
years = age % 10
output = "You are " + str(decades) + " decades" + " and " + str(years) + " years old"

print(output)
