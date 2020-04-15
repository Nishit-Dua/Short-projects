import random

class TaskList_WithoutNum:

	def __init__(self):

		'''
		This differs from the prev version as in this you
		dont need to predefine number of tasks beforehand
		and just write done case-insensitively voila.
		Cannot take more than 10000 tasks, which i doubt 
		will anyone do. lol
		'''
		pass
		
	def order_tasks(self):
		random_list = []
		task_dict = {}
		temp_task_upper = ''

		while temp_task_upper != 'DONE':
			len_list = random_list.__len__()
			rand_num = random.randint(1, 10000)

			if rand_num not in random_list:

				temp_task = self.ask_inputs(len_list + 1)
				temp_task_upper = temp_task.upper()

				if temp_task_upper != 'DONE':
					random_list.append(rand_num)
					task_dict[rand_num] = temp_task

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
		num = sorted_random_list.__len__() - 1

		print('\n\nFirstly {}'.format(tasks[sorted_random_list[0]]) , end ='')
		for task_num in range(1 , num):
			print(", then {}".format(tasks[sorted_random_list[task_num]]) , end ='')
		print(', then Finally {}\n'.format(tasks[sorted_random_list[num]]))

if __name__ == '__main__':
	task = TaskList_WithoutNum()
	task.print_result()