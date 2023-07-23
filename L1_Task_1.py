#This is the program to implement the string reversal function by taking a string as a input and returning a reversed string as a output 
#reverse a string using reversed()   
# Function to reverse a string   

x=input("Enter a string : ")  
def reverse(str):   
    string = "".join(reversed(str)) # reversed() function inside the join() function  
    return string   
  
print ("The original string is : ",x)   
print ("The reversed string using reversed() is : ",reverse(x) )  