import os, sys
import math

PI = 3.14159

#file_output = open("hod_dl.txt", "w+")
file_output = open("hod_dl.t.txt", "w+")

def calc_angle(value_1, value_2):
	angle = 90
	
	if (value_2[0] - value_1[0] != 0):	
		angle = math.atan((value_2[1] - value_1[1])/(value_2[0] - value_1[0])) * 180/PI	
	return angle

def temporal_hist(x_y, no_bins):
	
	bin_size = (360-0)/no_bins;
	base_hist = [[0 for j in range(no_bins)] for i in range(4)]
	middle_hist = [[0 for j in range(no_bins)] for i in range(2)]
	top_hist = [0 for j in range(no_bins)]

	for i in range(len(x_y)):
		if x_y[i] == 360:
			x_y[i] = x_y[i] - 1
		bin_value = int(x_y[i] / bin_size)
		
		# For the top layer of the histogram
		top_hist[bin_value] += 1
		
		# To form the base of the temporal pyramid
		if i < len(x_y)/4:
			base_hist[0][bin_value] +=1
		elif i < (len(x_y)*2)/4:
			base_hist[1][bin_value] +=1
		elif i< (len(x_y)*3)/4:	
			base_hist[2][bin_value] +=1
		else:
			base_hist[3][bin_value] +=1

		#To form the middle of the temporal pyramid
		if i < len(x_y)/2:
			middle_hist[0][bin_value] += 1
		else:			
			middle_hist[1][bin_value] += 1

	#To write the base values to the file
	for ini in range(4):
		for fin in range(no_bins):
			value = base_hist[ini][fin]/(sum(base_hist[ini]))			
			file_output.write(str(value))
			file_output.write(' ')
	
	#To write the middle values to the file
	for j in range(2):
		for k in range(no_bins):	
			value = middle_hist[j][k]/(sum(middle_hist[j]))
			file_output.write(str(value))
			file_output.write(' ')
	
	#To write the values of top bin	
	for val in range(no_bins):
		value = top_hist[val]/sum(top_hist)
		file_output.write(str(value))
		file_output.write(' ')
			
		
def read_file(filename):
	file_input = open(filename, "r")
	full_data = []
	
	for line in file_input:
		full_data.append(line.strip("\n").split())

	x_y = []
	y_z = []
	x_z = []
	
	no_bins = 8
		
	for j in range(20):
		j = 0
		for i in range(1, int(len(full_data)/20)):
		
			if (full_data[j+20][2]!="NaN" and full_data[j+20][3]!="NaN" and full_data[j][2]!="NaN" and full_data[j][3]!="NaN"):			
				val_1 = [float(full_data[j+20][2]), float(full_data[j+20][3])]
				val_2 = [float(full_data[j][2]), float(full_data[j][3])]
				x_y.append (calc_angle(val_1, val_2))	

			if (full_data[j+20][3]!="NaN" and full_data[j+20][4]!="NaN" and full_data[j][3]!="NaN" and full_data[j][4]!="NaN"):			
				val_3 = [float(full_data[j+20][3]), float(full_data[j+20][4])]
				val_4 = [float(full_data[j][3]), float(full_data[j][4])]
				y_z.append (calc_angle(val_3, val_4))

			if (full_data[j+20][2]!="NaN" and full_data[j+20][4]!="NaN" and full_data[j][2]!="NaN" and full_data[j][4]!="NaN"):			
				val_5 = [float(full_data[j+20][2]), float(full_data[j+20][4])]
				val_6 = [float(full_data[j][2]), float(full_data[j][4])]
				x_z.append (calc_angle(val_5, val_6))
			j = j +20
	
		temporal_hist(x_y, no_bins)
		temporal_hist(y_z, no_bins)
		temporal_hist(x_z, no_bins)
		x_y.clear()
		y_z.clear()
		x_z.clear()
	
	file_output.write('\n')

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
