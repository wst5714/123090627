def is_prime(x): #to justify whether x is prime number
        if(x<2): #x couldn't be prime number if x is smaller than 2
         return False  #jump out the function 
        for index in range(2,int(x**(1/2)+1)):  #for loop: Find out if x is divisible by index between 2~sqrt(x)+1 and is certainly not a prime number        
            if(x%index==0): #judge whether x is divisible or not
                return False #x is not a prime number, returns false
        return True #if x is not divisible in the range 2~sqrt(x)+1,x is prime number

def solution_question5(input_value):#define the problem-solving function
    count=0 #use 'count' to record the total number of the prime number,the start value of it is 0
    for n in range(input_value): # for loop: use n to represent the value in the range of 0~input_value
        if is_prime(n): #if n is a prime number
            print(n,end="\t") #print n and be formatted
            count=count+1 #assign count+1 to count after find a prime number
            if(count%8==0): #if count is divisable by 8, print a line break 
                print()#print a line break
#  (^.⌒)γ
input_value=input('input an integer greater than 0:')  #input an integer greater than 0 and assign it to input_value
while (not input_value.isdigit()) or int(input_value)<=0:  #if input_value isn't an integer greater than 0, continue the while loop till input the correct value
    input_value=input('please enter an Integer greater than 0:')  #let the user to input another integer and assign it to input_value
solution_question5(int(input_value))  #run the problem-solving function
