
names_string = input()
names = names_string.split(", ")
import random
n = len(names)
index = random.randint(0, n-1)
random_choice = names[index]
print(random_choice + " is going to buy the meal today!")
