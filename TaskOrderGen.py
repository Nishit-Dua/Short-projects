import random

random_list = []

def order_tasks():
	EPOCHS = input("enter number of tasks : ")
	EPOCHS = int(EPOCHS)

	while True:
		x = random.randint(1,EPOCHS)
		if x not in random_list:
			random_list.append(x)
		if random_list.__len__() == EPOCHS:
			break
	return random_list

print('\n\n',order_tasks(), '\n')