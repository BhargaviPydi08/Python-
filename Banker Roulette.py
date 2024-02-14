#This code helps to pick out a random person from a list of people, and that person has to pay the bill among the friends at restaurant.
names_string = input()
names = names_string.split(", ")
import random
n = len(names)
index = random.randint(0, n-1)
random_choice = names[index]
print(random_choice + " is going to buy the meal today!")
