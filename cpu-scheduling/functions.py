"""
Author: Zubair Asif

'I acknowledge the DCU Academic Integrity Policy'

"""

from statistics import mean

def list_sorter_fcfs(all_contents_list):#sorts file contents
	all_contents_list.sort()
	return all_contents_list

def burst_element_sjf(elem):#used to sort the list based on burst
	return elem[2]

def list_sorter_sjf(all_contents_list):#sorts file contents
	all_contents_list.sort(key=burst_element_sjf)
	return all_contents_list
	#all_contents_list.sort(key= lambda x: x[2])
	#return all_contents_list

def string_converter(all_contents_list):
	newlist = []
	for group in all_contents_list:
		list_int = [int(s) if s.isdigit() else s for s in group]
		newlist.append(list_int)

	return newlist

def burst_element_p(elem):#used to sort the list based on burst
	return int(elem[1])

def list_sorter_p(all_contents_list):#sorts file contents
	all_contents_list.sort(key=burst_element_p, reverse=True)
	return all_contents_list


def waiting_time(sortedlist):#gets average waiting time

	burstlist = []#will only contain the burst times
	for burst in sortedlist:#seperating the sortedlist
		burstlist.append(burst[2])
	
	time = 0
	alltimes = []# will contain all waiting times
	i = 0
	while i < len(burstlist):
		alltimes.append(time)
		time = time + int(burstlist[int(i)])
		i += 1
	
	return mean(alltimes)

def get_burst_time(sortedlist):
	burstlist = []#will only contain the burst times
	for burst in sortedlist:#seperating the sortedlist
		burstlist.append(burst[2])
	return burstlist

def arrival_time(sortedlist):#get arrival time
	
	burstlist = []#will only contain the burst times
	for burst in sortedlist:#seperating the sortedlist
		burstlist.append(burst[2])
	
	time = 0
	alltimes = []	# will contain all waiting times
	i = 0
	while i < len(burstlist):
		alltimes.append(time)
		time = time + int(burstlist[int(i)])
		i += 1
	
	return alltimes

def get_turnaround(bursttimes, arrivaltimes):
	turnaround_list = []
	i = 0
	while i < len(bursttimes):
		turnaround_list.append(int(bursttimes[i]) + int(arrivaltimes[i]))
		i += 1
	return turnaround_list

def get_turnaround_rr(bt, wt):
	turnaround_list = []
	i = 0
	while i<len(bt):
		turnaround_list.append(int(bt[i]) + int(wt[i]))
		i+=1
	return turnaround_list
