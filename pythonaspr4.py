# initialize the amount variable
# amount = 10000
#
# # check that You are eligible to
# # purchase Dsa Self Paced or not
# if(amount > 2999):
#     print("You are eligible to purchase Dsa Self Paced")
# initialize the amount variable
# marks = 10000
#
# # perform division with 0
# a = marks / 0
# print(a)

# Python program to handle simple runtime error
#Python 3

a = [1, 2, 3]
try:
	print ("Second element = %d" %(a[1]))

	# Throws error since there are only 3 elements in array
	print ("Fourth element = %d" %(a[3]))

except:
	print ("An error occurred")


