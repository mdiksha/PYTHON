#NUMERIC
a = 5  
print("The type of a", type(a))  
  
b = 40.5  
print("The type of b", type(b))  
  
c = 1+3j  
print("The type of c", type(c))  
print(" c is a complex number", isinstance(1+3j,complex)

#STRING
s1 = 'string using double quotes'  
print(s1)  
s2 = '''''A multiline 
string'''  
print(s2)

str1 = 'hello javatpoint' #string str1    
str2 = ' how are you' #string str2    
print (str1[0:2]) #printing first two character using slice operator    
print (str1[4]) #printing 4th character of the string    
print (str1*2) #printing the string twice    
print (str1 + str2) #printing the concatenation of str1 and str2

#LIST     
list1  = [1, "hi", "Python", 2]    
#Checking type of given list  
print(type(list1))  
  
#Printing the list1  
print (list1)  
  
# List slicing  
print (list1[3:])  
  
# List slicing  
print (list1[0:2])   
  
# List Concatenation using + operator  
print (list1 + list1)  
  
# List repetation using * operator  
print (list1 * 3)

#TUPLE
tup  = ("hi", "Python", 2)    
# Checking type of tup  
print (type(tup))    
  
#Printing the tuple  
print (tup)  
  
# Tuple slicing  
print (tup[1:])    
print (tup[0:1])    
  
# Tuple concatenation using + operator  
print (tup + tup)    
  
# Tuple repatation using * operator  
print (tup * 3)     
  
# Adding value to tup. It will throw an error.  
t[2] = "hi"

#DICTIONARY
d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'}     
  
# Printing dictionary  
print (d)  
  
# Accesing value using keys  
print("1st name is "+d[1])   
print("2nd name is "+ d[4])    
  
print (d.keys())    
print (d.values())

#BOOLEAN
print(type(True))  
print(type(False))  
print(false)
      
#SET
# Creating Empty set  
set1 = set()  
  
set2 = {'James', 2, 3,'Python'}  
  
#Printing Set value  
print(set2)  
  
# Adding element to the set  
  
set2.add(10)  
print(set2)  
  
#Removing element from the set  
set2.remove(2)  
print(set2) 
