"""
#### User Input
Create a function that asks the user to enter an integer number.  Return this value as your output.  This allows you to keep your error checking/try except statements out of your main block to keep your main block more concise.

Criteria
* the function does not need an input parameter
* the function returns an integer value
"""

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
            return num
if __name__ == "__main__":
    user_input = get_integer_input()
    print(f"You entered the integer: {user_input}")
