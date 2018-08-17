
###############################
# Exercise
###############################

color = {"col1" : "Red", "col2" : "Green", "col3" : "Orange" }
print("Dictionary : ", color)

print("First item of the dictionary" , color["col1"] ) 


en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
print (en_de)
print (en_de["red"])


for key in en_de:
  print(en_de[key])
  
  

squares = {x: x*x for x in range(6)}
print(squares)

# Table 3 generation
namta ={x: x*3 for x in range(11)}
print(namta, "x")


w={"house":"Haus","cat":"Katze","red":"rot"}
w1 = {"red":"rouge","blau":"bleu"}
w.update(w1)
print ("Updated dictionary" , w)



#########################################
# Problem 2
# add item

  
my_dict = {'name':'Jack', 'age': 26}
print("Old Dictionary: " , my_dict)
# update value
my_dict['age'] = 27
print("New Dictionary: " ,my_dict)

my_dict['address'] = 'Downtown'  

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print("New Dictionary with adding key and value: ", my_dict)






