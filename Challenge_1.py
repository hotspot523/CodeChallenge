# function takes array of numbers and return array of odd numbers
def ret_odd(input_array, odd_array = []):

    if input_array:
        num = input_array.pop(0)

        #checking whether array element is int or not; and if int number is odd or not using '&' operator
        if isinstance(num,int) and num&1:
            odd_array.append(num)

        #recursive call; with updated odd_array
        ret_odd(input_array,odd_array)

    #returning final odd_array
    return odd_array

#calling method to get array as argument
print ret_odd([1,2,3,4,5,6,7,8,9,10,11,121,324,3423])
