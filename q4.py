N = float(input("enter a integer greater than zero:"))  #enter an integer greater than zero and convert it to the value of N
  
def f(N):  #define a function
     x=1  #the start value of x is 1
     while x<=N: #When x is greater than N, the loop stop
          print(x,"\t",x+1,"\t",x**(x+1))  #print the solution of x、x+1、x**(x+1)
          x=x+1  # x increase 1

while N<=0 or N%1!=0:  #start the while loop when N<=0 or N%1!=0 till the user input the correct value
     N= float(input('please enter an integer greater than 0:' ))  #assign a new value to N
print("m\tm+1\tm**(m+1)")  #print the header
f(N)  #run the function
