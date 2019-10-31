#Jack Amos
#CS2300-002
#11/4/2019
#Project 3
#Python 3.7


#operate on any nxn size matrix
#read file as: dimension, values
#sys matrix is nxn, prod matix is nx1
#divide above value by below value to get quotient then mult lower row by quotient and sub upper row from lower row
#make sure to perform operations on prod matrix as well
#if x < .0000001, x = 0



def printSys(sys, size):
	pass


def printProd(prod):
	pass


def sysCheck(sys, size):
	
	return False



def solveForX(sys,prod):

	#sys
	with open(sys,'r') as file:
		contents = file.read()

	#get each value in string an convert it to float
	sys_values = [float(x) for x in contents.split()]

	#prod
	with open(prod,'r') as file:
		contents = file.read()

	#get each value in string an convert it to float
	prod_values = [float(x) for x in contents.split()]


	#determine matrix size 
	size = int(sys_values[0])

	#remove size data from lists to make operations easier
	sys_values.remove(size)
	prod_values.remove(size)

	#making sys into 2d array so it can be processed easier
	count = size
	iterator = size
	start = 0
	end = size
	temp = []
	sysFinal = []

	while count != 0:

		temp = sys_values[start:end]
		sysFinal.append(temp)
		temp = []
		count-=1
		start+=iterator
		end+=iterator


	#check if all necessary 0's exist
	check = False

	while check == False:

		check = sysCheck(sysFinal,size)





solveForX("sysMat1","prodVec1")


