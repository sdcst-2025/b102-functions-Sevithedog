"""
### Assignment 4
#### Prime factorization
Create a program that incorporates assignment 2 and 3 to do the prime factorizations for a number.  You will need to develop an algorithm to determine how you can do this.  If you can't figure it out by the beginning of next class, your teacher will provide you with some pseudocode/a method for determining how you can do this.
"""
import time
def get_integer_input():
    accval = False
    while accval == False:
        num = input("Enter an integer: ")
        try:
            intnum = int(num)
        except: 
            print("Please enter an integer")
            continue
        if intnum == float(num):
            accval = True
            return int(num)
def factorise(number):
    lfactor =[]
    #onumber = number
    number = int(number)
    prime = False
    while prime == False:
        for i in range(2, int(number**0.5)):
            if i == number:
                prime = True 
                lfactor.append(i)
                return lfactor 
            if number % i == 0:
                number = number//i
                lfactor.append(i)
                break
                
            
    
       
        

input = int(input("Enter integer: "))
start = time.time()
pass
print(f"The factors are: {factorise(input)}")
end = time.time()
elapsed = end-start
print(elapsed)