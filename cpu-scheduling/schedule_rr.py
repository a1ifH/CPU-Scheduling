"""
Author: Zubair Asif

'I acknowledge the DCU Academic Integrity Policy'

"""
import sys
from functions import *
from statistics import mean

def main():
	
	all_contents_list = []
	
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
	
	for line in file:
		all_contents_list.append(line.strip().split(","))

	#Calling function to upon list to sort it
	sortedlist = list_sorter_fcfs(all_contents_list)

	#calling function to get burst times
	all_burst = get_burst_time(sortedlist)

	# ROUND ROBIN STARTS
	n = len(all_burst)

	waiting_time = []
	remaining_burst = []
	int_burst = []
	#looping through to make a copy of bursts
	for i in range(n):
		remaining_burst.append(int(all_burst[i]))
		int_burst.append(int(all_burst[i]))

	#flag
	time_counter = 0
	quantum = 10

	while True:
		#condition to keep loop running
		validation = 1
		for i in range(n):
			if remaining_burst[i] > 0:
				#this when 0 means that there is another process still due
				validation = 0

				if remaining_burst[i] > quantum:
					time_counter = time_counter + quantum
					remaining_burst[i] = remaining_burst[i] - quantum
				else:
					time_counter = time_counter + remaining_burst[i]
					waiting_time.append(time_counter - int_burst[i])
					remaining_burst[i] = 0
		if validation == 1:
			break
	#call function to get turnaround times
	tat_times = get_turnaround_rr(all_burst, waiting_time)
	
	#get averages
	average_wt = mean(waiting_time)
	average_tat = mean(tat_times)

	#Print formatting work
	print("{:^65}".format("Round Robin Scheduling"))
	print("{:^65}".format("============================="))
	print("{:^20} {:^20} {:^20}".format("Task", "Priority", "Burst Time"))
	print("{:^20} {:^20} {:^20}".format("----", "--------", "----------"))

	for name in sortedlist:#Print Task, Priority & Burst
		title_task = name[0]
		title_priority = name[1]
		title_burst = name[2]
		print("{:^20} {:^20} {:^20}".format(title_task, title_priority, title_burst))


	#Getting Waiting times
	string_wt = ", ".join(str(v) for v in waiting_time)
	print("\n{:^65}\n{:^65}".format("Waiting Times (ms):", string_wt))
	
	#Getting Turnaround Times
	#Turnaround = CPU Burst + Arrival Times
	string_tat = ", ".join(str(v) for v in tat_times)
	print("\n{:^65}\n{:^65}".format("Turnaround Times (ms):", string_tat))

	#Getting Average Waiting Time
	print("\n{:^65}\n{:^65.2f}".format("Average Waiting Time (ms):", average_wt))

	#Getting Average Turnaround Time
	print("\n{:^65}\n{:^65.2f}".format("Average Turnaround Time (ms):", average_tat))

if __name__ == '__main__':
	main()
