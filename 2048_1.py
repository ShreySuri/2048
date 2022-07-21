import random

print("Hello, welcome to 2048")
print("Use w, a, s, and d keys to play")
print("")

full_char_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

x = random.randint(0, 160)
y = x % 16
z = int((x - y)/16)

if z == 0:
	full_char_list[y] = 4:
else:
	full_char_list[y] = 2:

for i in range (0, 4):
	


