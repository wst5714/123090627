def f(x):  #define a function
  if x>0:  #stop the if when x＜=0
    f(x//10)   #assign x//10 to the value of x
    print(x%10)  #print the solution

integer = int(input("enter an integer:"))  #input the value of integer
f(integer)  #output the solution after computing
