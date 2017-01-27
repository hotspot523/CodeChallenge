
# argument count is number of rows which is entered from terminal.
def pascal_t(count,input_list=0):

	if not count: exit() # if count is 0 program will exit.

	if not input_list: # to print first element as 1 when there is no input list.
		created_array=[1]
		print (count*"   "),"    ".join(map(str,created_array))

		pascal_t((count-1),created_array) # recursive call; created array will be taken as input list.

	created_array=[] # initializing list

	# for loop to insert numbers in created_array
	for index in range(len(input_list)):
		# when index is 0 then first value will be inserted in created_ array
		if not index:

			# if there is only 1 element in the list, this condition will insert first element again in created_array
			if (index+1)==len(input_list):
				created_array.append(input_list[index])
			created_array.append(input_list[index])
		
		elif (index+1)==len(input_list):	# when index is second last, it will insert two elements in created_array		
			created_array.extend((input_list[index-1]+input_list[index],input_list[index]))

		else:
			created_array.append(input_list[index-1]+input_list[index])

	# list formatting for proper pattern printing.
	formatted_list = [str(num)+"   " if num>9 and num<=99 else str(num)+"  " if num>99 and num<=999 else str(num)+" "
	if num>999 and num<=9999 else str(num)+"" if num>9999 else str(num)+"    " for num in created_array]
	
	# Creating and printing string from created_array	
	string_to_print = " ".join(formatted_list)
	print count*"   ",string_to_print
	pascal_t((count-1),created_array) # recursive call; created array will be taken as input list.


'''
Program's sequential pattern printing will work only till 20th row.
After 20th row; on 21st row, it will give 6digit numbers; result can be printed
but will break the sequential pattern as condition is not specified for that.
'''

# function call with user input from terminal
pascal_t(int(raw_input("Enter Number of Rows(1-20) for Pascal's Triangle: ")))


