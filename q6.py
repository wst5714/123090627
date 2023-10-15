import math  #invoke trigonometric functions from math package

def is_number(s):   #define a function to determine whether the input value is a number
    try:
        float(s)   #if the input value can't be converted into float then will throw the exception from the float function
        return True   #no exceptions,return true,prove that the input value is a number
    except Exception as e:   #catch exceptions and execute
        return False   #the solution after executing return false,prove the input value isn't a number
   

def f(a,b,N,operatorFunc):   #define a function to culculate
    sum = 0   #use 'sum' to represent the sum total value, the start value is 0
    for i in range(1,N+1):   #
        fres=0   #use fres to represent the value after every computing,the start value is 0
        fres =eval("math."+operatorFunc+"(a+((b-a)/N)*(i-1/2))")   #assign the value after computing to fres
         
        sum = sum+((b-a)/N)*fres   #sum up every sum with the vary of N

    return sum   #return the final value to sum after all execution
    

str_N = input("enter a Integer [N]:")   #assign the value of str_N by inputing an integer
while not str_N.isdigit():   #if str_N is not an integer greater than 0, ask the user to input another value till a correct value is inputted
    str_N=input("enter an integer greater than 0 to represent N:")   #ask the user to input a correct value and assign the new value to str_N
a = b = 0
while(not a<b):
    str_a = input("enter a number [a]:")   #assign the value of str_a by inputing an number
    while not is_number(str_a):   #if str_a is not a number, ask the user to input another value till a correct value is inputted
        str_a=input("please enter a number to represent a:")   #ask the user to input a correct value and assign the new value to str_a

    str_b = input("enter b number [b]:")   #assign the value of str_a by inputing an number
    while not is_number(str_b):   #if str_N is not a number, ask the user to input another value till a correct value is inputted
        str_b=input("please enter a number to represent b:")   #ask the user to input a correct value and assign the new value to str_b
    a = float(str_a)
    b = float(str_b)

func_str_name = "sin"   #assign the default value of func_str_name to sin
func_str_name = input("please enter an string [sin/cos/tan] default sin:")  #assign the value of func_str_name by inputing a trigonometric functions
funlist = ["sin","cos","tan"]   #the trigonometric functions should be selected from the funlist
while not (func_str_name in funlist):   #continue the loop till the user input the correct value
    func_str_name = input("please enter an string [sin/cos/tan] default sin:")   #the trigonometric function should from the funlist

print(f(float(str_a),float(str_b),int(str_N),func_str_name))   #run the function






