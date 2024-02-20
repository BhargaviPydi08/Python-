#This code finds where the tressure is hidden . An input(position) is taken from the user and is converted to an actual index to access that particular item in the list and replace its value with "X".

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

abc = ["a", "b", "c"]
number_index = int(position[1])-1
letter = position[0].lower()
letter_index = abc.index(letter)

map[number_index][letter_index] = "X"
print(f"{line1}\n{line2}\n{line3}")

