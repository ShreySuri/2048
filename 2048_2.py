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

