import os
import math

PI = 3.14159

#file_output = open("rad_dl.txt", "w+")
file_output = open("rad_dl.t.txt","w+")

# This funcion is used to calculate the angle between two lines
# The function returns the value of angle in degree
def calc_angle(args_1, args_2, args_3):
	
	# This sub is done to change the reference to origin
	args_1[0] = args_1[0] - args_3[0]
	args_1[1] = args_1[1] - args_3[1]
	args_1[2] = args_1[2] - args_3[2]
		
	args_2[0] = args_2[0] - args_3[0]
	args_2[1] = args_2[1] - args_3[1]
	args_2[2] = args_2[2] - args_3[2]

	#This is the formula to calculate angle between two vectors
	num = args_1[0] * args_2[0] + args_1[1] * args_2[1] + args_1[2] * args_2[2]
	den = math.sqrt(args_1[0]**2 + args_1[1]**2 + args_1[2]**2) * math.sqrt(args_2[0]**2+args_2[1]**2+args_2[2]**2)  
	
	angle = math.acos(num/den)

	return (angle*180 / PI)

#This function is used to calculate the distance between centre and point
def calc_distance(args_1, args_2):
	distance = math.sqrt( (args_1[0]-args_2[0])**2 + (args_1[1]-args_2[1])**2 + (args_1[2]-args_2[2])**2 )
	return distance

# This function is used to write the normalized histogram value into the file.
#This method is used for the distance function.
# Different functions are used to allow variation of the number of bins for the distance and angle fucntion.
def distance_block(distances, no_bins):
	
	hist_list = [0]*no_bins
	
	minimum = min(distances)
	maximum = max(distances)
	
	bin_size = (maximum - minimum)/ no_bins
	
	for i in range(len(distances)):
		slot = math.floor((distances[i] - minimum)/ bin_size)
		if slot == no_bins:
			slot = slot -1		
		hist_list[slot] = hist_list[slot] +1
			
	if sum(hist_list) == len(distances):
		for j in range(no_bins):
			hist_list[j] = hist_list[j]/(len(distances))
	
	file_output.write(' '.join(str(e) for e in hist_list))

# This function gives the normalized histogram values for the angle values.
def angle_block(distances, no_bins):
	
	hist_list = [0]*no_bins
	
	minimum = min(distances)
	maximum = max(distances)
	
	bin_size = (maximum - minimum)/ no_bins
	
	for i in range(len(distances)):
		slot = math.floor((distances[i] - minimum)/ bin_size)
		if slot == no_bins:
			slot = slot -1		
		hist_list[slot] = hist_list[slot] +1
			
	if sum(hist_list) == len(distances):
		for j in range(no_bins):
			hist_list[j] = hist_list[j]/(len(distances))
	
			
	file_output.write(' '.join(str(e) for e in hist_list))

def read_file(filename):
	
	file_input = open(filename,"r")

	# This is the final vectors that are required for the histogram
	# All the required distances and angles are described as list of list.
	
	d = [[] for i in range(5)]
	a = [[] for i in range(5)]

	# This is to make sure that there is no infinite value in the file.	
	flag = 1

	for line in file_input:
		values = []
		values = line.split()
		if int(values[1]) == 1:
			if (values[2] == "NaN" or values[3] == "NaN" or values[4] == "NaN"):
				flag = 0
			else:			
				dim_1 = [float(values[2]), float(values[3]), float(values[4])]
				flag = 1
			
		elif int(values[1]) == 4:
			if flag != 0 and (values[2] != "NaN" and values[3] != "NaN" and values[4] != "NaN"):
				dim_4 = [float(values[2]), float(values[3]), float(values[4])]
				d[0].append(calc_distance(dim_4,dim_1))

		elif int(values[1]) == 8:
			if flag != 0 and (values[2] != "NaN" and values[3] != "NaN" and values[4] != "NaN"):
				dim_8 = [float(values[2]), float(values[3]), float(values[4])]
				d[1].append(calc_distance(dim_8,dim_1))

		elif int(values[1]) == 12:
			if flag != 0 and (values[2] != "NaN" and values[3] != "NaN" and values[4] != "NaN"):
				dim_12 = [float(values[2]), float(values[3]), float(values[4])]
				d[2].append(calc_distance(dim_12,dim_1))

		elif int(values[1]) == 16:
			if flag != 0 and (values[2] != "NaN" and values[3] != "NaN" and values[4] != "NaN"):
				dim_16 = [float(values[2]), float(values[3]), float(values[4])]
				d[3].append(calc_distance(dim_16,dim_1))

		elif int(values[1]) == 20:
			if flag != 0 and (values[2] != "NaN" and values[3] != "NaN" and values[4] != "NaN"):
				dim_20 = [float(values[2]), float(values[3]), float(values[4])]	
				d[4].append(calc_distance(dim_20,dim_1))

				if len(dim_4)!=0 and len(dim_8)!=0:
					a[0].append(calc_angle(dim_4,dim_8,dim_1))
				if len(dim_4)!=0 and len(dim_12)!=0:
					a[1].append(calc_angle(dim_4,dim_12,dim_1))
				if len(dim_8)!=0 and len(dim_16)!=0:
					a[2].append(calc_angle(dim_8,dim_16,dim_1))
				if len(dim_12)!=0 and len(dim_20)!=0:				
					a[3].append(calc_angle(dim_12,dim_20,dim_1))
				if len(dim_16)!=0 and len(dim_20)!=0:
					a[4].append(calc_angle(dim_16,dim_20,dim_1))

	for j in range(5):
		distance_block(d[j], 10)
		file_output.write(' ')
	
	for k in range(5):
		distance_block(a[k], 10)
		file_output.write(' ')
	

# Call this function to run all the training files.
def set_path_train():
	fileDir = os.path.dirname(os.path.realpath('__file__'))
	
	# The pattern in the training pattern is used to create the file path name.
	a = [8,10,12,13,15,16];
	
	for i in a:
		for j in range(1,7):
			for k in range(1,3):
				if i == 8:
					path = "a08_s0"+str(j)+"_e0"+str(k)+"_skeleton_proj.txt";
				else:
					path = "a"+str(i)+"_s0"+str(j)+"_e0"+str(k)+"_skeleton_proj.txt";	
				filename = os.path.join(fileDir,'../HCR/dataset/train/'+path)
				filename = os.path.abspath(os.path.realpath(filename))				
				read_file(filename)
				file_output.write("\n")
				file_output.write("\n")

# Call this function to run all the test files.
# Please note the comments available in the beginning and end of the file for running different files.
def set_path_test():
	fileDir = os.path.dirname(os.path.realpath('__file__'))
	
	# The pattern in the training pattern is used to create the file path name.
	a = [8,10,12,13,15,16];
	
	for i in a:
		for j in range(7, 11):
			for k in range(1,3):
				if i == 8:
					if j<10:
						path = "a08_s0"+str(j)+"_e0"+str(k)+"_skeleton_proj.txt"
					else:
						path = "a08_s"+str(j)+"_e0"+str(k)+"_skeleton_proj.txt"
				else:
					if j<10:						
						path = "a"+str(i)+"_s0"+str(j)+"_e0"+str(k)+"_skeleton_proj.txt"
					else:
						path = "a"+str(i)+"_s"+str(j)+"_e0"+str(k)+"_skeleton_proj.txt"	
				filename = os.path.join(fileDir,'../HCR/dataset/test/'+path)
				filename = os.path.abspath(os.path.realpath(filename))				
				read_file(filename)
				file_output.write("\n")
				file_output.write("\n")
					

#set_path_train()
set_path_test()
