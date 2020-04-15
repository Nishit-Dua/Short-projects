import random

class TaskList:

	def __init__(self):
		self.EPOCHS = int(input('enter number of tasks : '))
		print('')
		
	def order_tasks(self):
		random_list = []
		task_dict = {}

		while True:
			rand_num = random.randint(1, self.EPOCHS)
			len_list = random_list.__len__()

			if rand_num not in random_list:

				random_list.append(rand_num)
				temp_task = self.ask_inputs(len_list + 1)
				task_dict[rand_num] = temp_task

			if len_list == self.EPOCHS:
				break

		return random_list , task_dict

	def ask_inputs(self, x):
		return input('enter task {} : '.format(x))

	def sort_dict(self):
		random_list , task_dict = self.order_tasks()

		sorted_task_dict = {}
		sorted_random_list = random_list
		sorted_random_list.sort()

		for task in sorted_random_list:
			sorted_task_dict[task] = task_dict[task]

		return sorted_random_list , sorted_task_dict

	def print_result(self):
		sorted_random_list , tasks = self.sort_dict()
		print('\n\nFirstly {}'.format(tasks[1]) , end ='')
		for task_num in range(2 , self.EPOCHS):
			print(", then {}".format(tasks[task_num]) , end ='')
		print(', then Finally {}\n'.format(tasks[self.EPOCHS]))

if __name__ == '__main__':
	task = TaskList()
	task.print_result()