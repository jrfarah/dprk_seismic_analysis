import subprocess
import os

print '==============Program Beginning=============='

master_dataset = "master_dataset.txt"
print 'Creating the master dataset file.'
subprocess.check_output("touch {0}".format(master_dataset), shell=True)

def add_to_master_dataset(filename):
	print 'Opening file: ', filename
	with open("data/{0}".format(filename),"r") as data_file:
		micro_set = data_file.readlines()
		micro_set.pop(0)
	print "First element of the current micro data file: ", micro_set[0]
	print 'Adding data to master dataset.'
	with open(master_dataset, "a") as master:
		for data_point in micro_set:
			print>>master, data_point.strip('\n')

for filename in os.listdir("data/"):
	add_to_master_dataset(filename)
	print 'Finished updating the master dataset.'

print '==============Done=============='