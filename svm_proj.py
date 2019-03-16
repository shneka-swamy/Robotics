from svmutil import *
import os

# To print the confusionn matrix
def confusion_matrix_func(y_1, p_labels):
	mat_grid = list(set(y_1))	
	mat_size = len(mat_grid)
	confusion_matrix = [[0]*mat_size for i in range(mat_size)]

	for i in range(len(y_1)):
		confusion_matrix[mat_grid.index(y_1[i])][mat_grid.index(p_labels[i])] +=1
	
	# This part is just to make the matrix look good while printing
	# This part has nothing to do with the calculation.	
	print("\t", end = " ")
	print('\n'.join(['\t'.join([str(int(val)) for val in mat_grid])]))
	print('\n')
	
	for j in range(mat_size):
		print(str(int(mat_grid[j])), end ='\t'),
		for k in range(mat_size):
			print(confusion_matrix[j][k], end ='\t')
		print('\n')

def run_svm_rad():
	y, x = svm_read_problem("rad_dl.txt")
	y_1, x_1 = svm_read_problem("rad_dl.t.txt")
	prob = svm_problem(y, x)
	param = svm_parameter('-t 2 -s 0 -c 5 -g 0.5')
	m = svm_train(prob, param)
	p_labels, p_acc, p_vals = svm_predict(y_1, x_1, m)
	confusion_matrix_func(y_1, p_labels)
	
def run_svm_hjpd():
	y, x = svm_read_problem("hjpd_dl.txt")
	y_1, x_1 = svm_read_problem("hjpd_dl.t.txt")
	prob = svm_problem(y, x)
	param = svm_parameter('-t 2 -s 0 -c 5 -g 0.5')
	m = svm_train(prob, param)
	p_labels, p_acc, p_vals = svm_predict(y_1, x_1, m)
	confusion_matrix_func(y_1, p_labels)

def run_svm_hod():
	y, x = svm_read_problem("hod_dl.txt")
	y_1, x_1 = svm_read_problem("hod_dl.t.txt")
	prob = svm_problem(y, x)
	param = svm_parameter('-t 2 -s 0 -c 0.58 -g 0.007')
	m = svm_train(prob, param)
	p_labels, p_acc, p_vals = svm_predict(y_1, x_1, m)
	confusion_matrix_func(y_1, p_labels)
	
run_svm_rad()
run_svm_hjpd()
run_svm_hod()
