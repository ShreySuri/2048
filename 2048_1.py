import random

print("Hello, welcome to 2048")
print("Use w, a, s, and d keys to play")
print("")
print("")

full_char_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

x = random.randint(0, 160)
y = x % 16
z = int((x - y)/16)

list_1 = []
list_1 = []
list_1 = []
list_1 = []


if z == 0:
	full_char_list[y] = 4:
else:
	full_char_list[y] = 2:

for i in range (0, 4):
	temp = full_char_list[i]
	list_1.append(temp)
for j in range (4, 8):
	temp = full_char_list[i]
	list_2.append(temp)
for k in range (8, 12):
	temp = full_char_list[i]
	list_3.append(temp)
for l in range (12, 16):
	temp = full_char_list[i]
	list_4.append(temp)

print(list_1)
print(list_2)
print(list_3)
print(list_4)
print("")

game = True

while game == True:
	input_1 = input(print(""))
	



