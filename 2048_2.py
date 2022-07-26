import random

def base_4(int_1):
	rem = int_1 % 4
	quotient = int((int_1 - rem)/4)
	final_int = 10 * quotient + rem
	return(final_int)



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
column_3 = []



