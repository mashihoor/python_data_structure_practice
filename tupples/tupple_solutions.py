# 1. Write a Python program to create a tuple. Go to the editor
#Blacnk tuple
a=()
print(a)

# 2. Write a Python program to create a tuple with different data types. Go to the editor

a=(1,2,3,'t' ,True ,"test")
print(a)


# 3. Write a Python program to create a tuple with numbers and print one item. Go to the editor

a=(1,2,3,'t' ,True ,"test")
print ( a[:1] )
print ( a[0] )


# 4. Write a Python program to unpack a tuple in several variables. Go to the editor

tuplex=(1 ,True ,"test")

var1 = var2 = var3 = tuplex
print(var1)

# 5. Write a Python program to add an item in a tuple. Go to the editor

 #create a tuple
tuplex = (4, 6, 2, 8, 3, 1) 
print(tuplex)

#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)
