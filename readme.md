# assignment 1
you are supposed to use vscode to compile it.

## question 1
 prompts the user to enter final account value, annual interest rate in percent, and the number of years, and displays the initial deposit amount.

```python
finalAccount= float(input("enter the final account value:")) #input the final account value and convert the value to finalAccount
rate = float(input("enter the annual interst rate:")) #input the rate and convert the value to rate
years = int(input("enter the number of years:")) #input the number of years and convert the value to years
  
def f(): #define the function
  	return finalAccount/(1+rate/100)**years  #return the value of the final account after computing
result = f() #use the function
print("the initial value is:",result) #print 'the initial value is：' and print the solution after computing
```
[!img./q1.png]
the example are above


## question 2
 Write a program that prompts the user to enter an integer and displays each of its numbers one by one.

 ```
 def f(x):  #define a function
  if x>0:  #stop the if when x＜=0
    f(x//10)   #assign x//10 to the value of x
    print(x%10)  #print the solution

integer = int(input("enter an integer:"))  #input the value of integer
f(integer)  #output the solution after computing
 ```
