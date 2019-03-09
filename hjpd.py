import os
import math

#file_output = open("hjpd_dl.txt", "w+")
file_output = open("hjpd_dl.t.txt","w+")

# This is used to calculate the centroid of all the points
# This is the reference point used in the paper
def calculate_centroid(x_val, y_val, z_val):
	sum_x = 0
	sum_y = 0
	sum_z = 0

	for val_x in x_val:
		if val_x != "NaN":
			sum_x = sum_x + float(val_x)

	for val_y in y_val:
		if val_y != "NaN":
			sum_y = sum_y + float(val_y)
	
	for val_z in z_val:
		if val_z != "NaN":
			sum_z = sum_z + float(val_z)
	
	return [sum_x/len(x_val), sum_y/len(y_val), sum_z/len(z_val)]

# This is used to get the distribution of histogram. This is same as the rad method
def hist_block(distances, no_bins):
	
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

# This function is used to read file and do all prelimnary operations
def read_file(filename):
	file_input = open(filename,"r")
	
	values_x = []
	values_y = []
	values_z = []
	
	del_x = [[] for i in range(20)]
	del_y = [[] for i in range(20)]
	del_z = [[] for i in range(20)]

	for line in file_input:
		values = []
		values = line.split()
		
		values_x.append(values[2])
		values_y.append(values[3]) 
		values_z.append(values[4])
	
		if int(values[1]) == 20:
			centroid = calculate_centroid(values_x, values_y, values_z)
			
			for x in range(20):
				if values_x[x] != "NaN":
					del_x[x].append(float(values_x[x])-centroid[0])
	

			for y in range(20):
				if values_y[y] != "NaN":
					del_y[y].append(float(values_y[y])-centroid[1])

			for z in range(20):
				if values_z[z] != "NaN":
					del_z[z].append(float(values_z[z])-centroid[2])

			values_x.clear()
			values_y.clear()
			values_z.clear()
			
	
	for x in range(20):
		hist_block(del_x[x], 10)
		file_output.write(' ')		

	for y in range(20):
		hist_block(del_y[y], 10)
		file_output.write(' ')	
	
	for z in range(20):
		hist_block(del_z[z], 10)
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

#set_path_train()
set_path_test()
