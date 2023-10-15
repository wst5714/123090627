m = float(input("m="))  #input the value of m
n=0  #the start value of n is 0

while True:  
  if m<n**2 :  #if m＜n**2, start the loop
    print("n=",n)  #print the value of n if n satisfy the condition
    break  #end the loop
  n=n+1  #n increase 1 if n doesn't satisfy m＜n**2