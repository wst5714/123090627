# project name

![img](img/1.jpg)





```python

while N<=0 or N%1!=0:  #start the while loop when N<=0 or N%1!=0 till the user input the correct value
     N= float(input('please enter an integer greater than 0:' ))  #assign a new value to N
print("m\tm+1\tm**(m+1)")  #print the header
f(N)  #run the function

```

## solution 1

### result = xxxx

```python
finalAccount= float(input("enter the final account value:")) #input the final account value and convert the value to finalAccount
rate = float(input("enter the annual interst rate:")) #input the rate and convert the value to rate
years = int(input("enter the number of years:")) #input the number of years and convert the value to years
  
def f(): #define the function
  	return finalAccount/(1+rate/100)**years  #return the value of the final account after computing
result = f() #use the function
print("the initial value is:",result) #print 'the initial value is：' and print the solution after computing
```

