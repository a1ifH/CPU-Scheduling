"""
Author: Zubair Asif

'I acknowledge the DCU Academic Integrity Policy'

"""
import sys
from functions import *
from statistics import mean

def main():

	all_contents_list = []#store the tasks

	# Common error handling 
	try:
		#opening the file through command line
		with open(sys.argv[1], 'r') as f:
			#reading in by line
			file = f.readlines()
	
	except IndexError:
		print("~ Failed to specifiy test file ~")
		sys.exit()

	except FileNotFoundError:
		print("~ The file you have entered is not recognised ~")
		sys.exit()

	#Appending line to all contents
	for line in file:
		all_contents_list.append(line.strip().split(","))
	
	sortedlist = list_sorter_fcfs(all_contents_list)#Calling function to upon list to sort it

	#Print formatting work
	print("{:^65}".format("First Come First Serve (FCFS)"))
	print("{:^65}".format("============================="))
	print("{:^20} {:^20} {:^20}".format("Task", "Priority", "Burst Time"))
	print("{:^20} {:^20} {:^20}".format("----", "--------", "----------"))

	for name in sortedlist:#Print Task, Priority & Burst
		title_task = name[0]
		title_priority = name[1]
		title_burst = name[2]
		print("{:^20} {:^20} {:^20}".format(title_task, title_priority, title_burst))
	
	#Getting Arrival Times
	all_arrival = ", ".join(str(v) for v in arrival_time(sortedlist))
	print("\n{:^65}\n{:^65}".format("Arrival Times (ms):", all_arrival))
	
	#Getting Turnaround Times
	#Turnaround = CPU Burst + Arrival Times
	bursttimes = get_burst_time(sortedlist)
	arrivaltimes = arrival_time(sortedlist)
	bt_x_at = ", ".join(str(v) for v in get_turnaround(bursttimes, arrivaltimes))
	print("\n{:^65}\n{:^65}".format("Turnaround Times (ms):", bt_x_at))

	#Getting Average Turnaround Time
	avg_turn = get_turnaround(bursttimes, arrivaltimes)
	print("\n{:^65}\n{:^65.2f}".format("Average Turnaround Time (ms):", mean(avg_turn)))

	#Getting Average Waiting Time
	average_wait = waiting_time(sortedlist)
	print("\n{:^65}\n{:^65.2f}".format("Average Waiting Time (ms):", average_wait))


if __name__ == '__main__':
	main()
