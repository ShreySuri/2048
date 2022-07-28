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
highest_num = 0

x = random.randint(0, 159)
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

game = True

while game == True:
	
	input_1 = "None"
	while input_1 != "w" and input_1 != "a" and input_1 != "s" and input_1 != "d":
		print("")
		input_1 = input(print("Use w, a, s, and, d, keys to play. "))
		input_1 = input_1.lower()

	if input_1 == "w":
		column_1 = forward(column_1)
		column_2 = forward(column_2)
		column_3 = forward(column_3)
		column_4 = forward(column_4)
		sync = "column"
	elif input_1 == "a":
		row_1 = forward(row_1)
		row_2 = forward(row_2)
		row_3 = forward(row_3)
		row_4 = forward(row_4)
		sync = "row"
	elif input_1 == "s":
		column_1 = backward(column_1)
		column_2 = backward(column_2)
		column_3 = backward(column_3)
		column_4 = backward(column_4)
		sync = "column"
	elif input_1 == "d":
		row_1 = backward(row_1)
		row_2 = backward(row_2)
		row_3 = backward(row_3)
		row_4 = backward(row_4)
		sync = "row"
	else:
		print("Something went wrong.")

	if sync == "column":
		master_list = []
		x = column_1[0]
		master_list.append(x)
		x = column_2[0]
		master_list.append(x)
		x = column_3[0]
		master_list.append(x)
		x = column_4[0]
		master_list.append(x)
		x = column_1[1]
		master_list.append(x)
		x = column_2[1]
		master_list.append(x)
		x = column_3[1]
		master_list.append(x)
		x = column_4[1]
		master_list.append(x)
		x = column_1[2]
		master_list.append(x)
		x = column_2[2]
		master_list.append(x)
		x = column_3[2]
		master_list.append(x)
		x = column_4[2]
		master_list.append(x)
		x = column_1[3]
		master_list.append(x)
		x = column_2[3]
		master_list.append(x)
		x = column_3[3]
		master_list.append(x)
		x = column_4[3]
		master_list.append(x)

	elif sync == "row":
		master_list = []
		x = row_1[0]
		master_list.append(x)
		x = row_1[1]
		master_list.append(x)
		x = row_1[2]
		master_list.append(x)
		x = row_1[3]
		master_list.append(x)
		x = row_2[0]
		master_list.append(x)
		x = row_2[1]
		master_list.append(x)
		x = row_2[2]
		master_list.append(x)
		x = row_2[3]
		master_list.append(x)
		x = row_3[0]
		master_list.append(x)
		x = row_3[1]
		master_list.append(x)
		x = row_3[2]
		master_list.append(x)
		x = row_3[3]
		master_list.append(x)
		x = row_4[0]
		master_list.append(x)
		x = row_4[1]
		master_list.append(x)
		x = row_4[2]
		master_list.append(x)
		x = row_4[3]
		master_list.append(x)

	else:
		print("Something went wrong.")


        y = 1
        while y != 0:
            x = random.randint(0, 15)
            y = master_list[x]

        master_list[x] = 2
        z = random.randint(0, 9)
        if z == 0:
            master_list[x] = 2 * master_list[x]
        else:
            toggle = False





	
if win == True:
	print("")
	print("You Won!")
else:
	print("")
	print("You Lost!")



	



