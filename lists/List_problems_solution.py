# problem  1. Write a Python program to sum all the items in a list
# problem  2. Write a Python program to multiply all the items in a list

my_list = [1, 4, 3, 2, 5]

sum = 0

for i in my_list:
  #print(i)
  sum =sum +i

multi=1
for j in my_list:
  multi = multi*j


print("Sum is : " ,sum)
print("Multiplication is =" , multi)


# Problem 3 : Finding largest number
# Using funciton
my_list = [1, 4, 3, 32, 5 ,10,23,]
print("Max number from the list using function " , max(my_list) ) 


# Problem 3 : Finding largest number
# Using data structure
my_list = [1, 4, 3, 32, 5 ,10,23,]
max = 0

for i in my_list:
  if i > max:
    max = i

print("Max number from the list using data structure: " , max ) 


## Problem 4. Write a Python program to get the smallest number from a list.

my_list = [4,3,32,5,1,10,23]
print("Min  number from the list using data structure: " , min(my_list) ) 


#  Problem 5
#  Write a Python program to count the number of strings where the string length is 2 or more 
#  and the first and last character are same from a given list of strings. 
#  Sample List : ['abc', 'xyz', 'aba', '1221']
#  Expected Result : 2

my_string_list= ['abc', 'xyz', 'aba', '1221','aa']
count = 0
for i in my_string_list:
  #print( i[0:1] )
  #print( i[-1] )
  string_len=len(i)
  if (string_len>2):
    if (i[0:1]==i[-1]):
      #print(i[0:1]==i[-1])
      #print("match found 1st letter and last letter same ")
      count+=1
      
print("Match found as per coniditon logic are : " , count)



