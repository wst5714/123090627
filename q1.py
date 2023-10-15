finalAccount= float(input("enter the final account value:")) #input the final account value and convert the value to finalAccount
rate = float(input("enter the annual interst rate:")) #input the rate and convert the value to rate
years = int(input("enter the number of years:")) #input the number of years and convert the value to years
  
def f(): #define the function
  	return finalAccount/(1+rate/100)**years  #return the value of the final account after computing
result = f() #use the function
print("the initial value is:",result) #print 'the initial value is：' and print the solution after computing