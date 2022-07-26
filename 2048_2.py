import random

def base_4(int_1):
	rem = int_1 % 4
	quotient = int((int_1 - rem)/4)
	final_int = 10 * quotient + rem
	return(final_int)

# [00, 01, 02, 03]
# [10, 11, 12, 13]
# [20, 21, 22, 23]
# [30, 31, 32, 33]


def forward(list_1):
	temp_list = []
	counter = 0
	for i in range (0, 4):
		if list_1[i] != 0:
			x = list_1[i]
			temp_list.append(x)
		else:
			counter = counter + 1
	for j in range (0, counter):
		temp_list.append(0)
	
	for i in range (0, 3):
		if temp_list[i] == temp_list[i + 1]:
			x = temp_list[i]
			x = 2 * x
			temp_list[i] = x
			temp_list[i + 1] = 0
		else:
			toggle = True

	list_2 = []
	counter = 0
	for i in range (0, 4):
		if temp_list[i] != 0:
			x = temp_list[i]
			list_2.append(x)
		else:
			counter = counter + 1
	for j in range (0, counter):
		list_2.append(0)

	return(list_2)

def backward(list_1):
	temp_list = forward(list_1)
	list_2 = []
	counter = 0
	for i in range (0, 4):
		if temp_list[i] == 0:
			counter = counter + 1
		else:
			toggle = False

	for i in range (0, counter):
		list_2.append(0)
	counter = 4 - counter

	for i in range (0, counter):
		x = temp_list[i]
		list_2.append(x)

	return(list_2)



master_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

x = random.randint(0, 159):
y = x % 16
z = int((x - y)/16)

if z == 0:
	master_list[y] = 4
else:
	master_list[y] = 2

row_1 = []
row_2 = []
row_3 = []
row_4 = []

column_1 = []
column_2 = []
column_3 = []
column_4 = []

for i in range (0, 16):
	base_int = base_4(i)
	value = master_list[i]
	
	if base_int >= 0 and base_int < 10:
		row_1.append(value)
	elif base_int >= 10 and base_int < 20:
		row_2.append(value)
	elif base_int >= 20 and base_int < 30:
		row_3.append(value)
	elif base_int >= 30 and base_int < 40:
		row_4.append(value)
	else:
		print("Something went wrong.")

	if base_int % 10 == 0:
		column_1.append(value)
	elif base_int % 10 == 1:
		column_2.append(value)
	elif base_int % 10 == 2:
		column_3.append(value)
	elif base_int % 10 == 3:
		column_4.append(value)
	else:
		print("Something went wrong.")

print(row_1)
print(row_2)
print(row_3)
print(row_4)


input_1 = "None"
while input_1 != "w" and input_1 != "a" and input_1 != "s" and_1 input_1 != "d":
	input_1 = input(print("Use w, a, s, and, d, keys to play. "))
	input_1 = input_1.lower()

if input_1 = "w":


