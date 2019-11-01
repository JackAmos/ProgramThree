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
#if x < .00001, x = 0



def printSysProd(sys,prod,col_round):

	count = len(sys)
	row_string = ""

	print("\nColumn %d"%(col_round))

	while count != 0:

		for n in sys:

			for m in n:
				index = sys.index(n)
				row_string+=str("{:.4f}".format(m))+"  "
			row_string+="x  "+str("{:.4f}".format(prod[index]))+"\n"
			print(row_string)
			row_string = ""
			count-=1
		
		

def sysCheck(sys):

	num_zeros = 0
	count = len(sys)

	while count != 0:
		num_zeros+=count
		count-=1


	#sets completed rows corresponding index to 0
	zero_count = 0
	

	for n in sys:
		for m in n:
			if m == 0.0:
				zero_count+=1

	if zero_count < num_zeros:

		return False

	return True
	


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
	i = 0
	col_top = 0
	num_zeros = 0
	zero_count = 0
	index = 0
	top = 0.0
	col_round = 1


	while check == False:

		print(sysFinal)
		#gaussian solving logic
		for n in sysFinal:

			num_zeros = size - 1

			if n[i] == 0.0:
				zero_count+=1
			elif n != sysFinal[col_top] and n != sysFinal[0]:

				top = -1 * (sysFinal[col_top][i])
				current = n[i]

				for m in n:
					n[n.index(m)] = (m * top) + (sysFinal[col_top][n.index(m)] * current)
					prod_values[sysFinal.index(n)] = (prod_values[sysFinal.index(n)] * top) + (prod_values[col_top] * current)

				zero_count+=1
		col_top+=1
		i+=1


		#set value to 0 if below or at minimum of .00001
		for n in sysFinal:
			for m in n:

				if m <= .00001 and m > 0.0:
					n[n.index(m)] = 0.0
				elif m >= -.00001 and m < 0.0:
					n[n.index(m)] = 0.0			


		printSysProd(sysFinal,prod_values,col_round)
		col_round+=1

		check = sysCheck(sysFinal)
	print(check)





solveForX("sysmat1.txt","prodvec1.txt")
solveForX("sysmat2.txt","prodvec2.txt")

