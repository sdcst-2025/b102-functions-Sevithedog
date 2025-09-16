# 100 review of functions

## Objectives
* to review and remember
  1. naming of functions
  2. use of (input) parameters
  3. use of return values
  4. local scope


Recall that functions are mini programs that you can *call* from your main block of code, or from other mini programs by using the function name.  A function may have input parameters (sometimes called parameters) that are variable names included in the brackets of the function definition.

```
def functionName(parameter1,parameter2):
  pass

functionName(3,4)
functionName(parameter2 = 4, parameter1 = 3)
```
In this sample function, parameter1 and parameter2 are 2 variable names that serve as place holders for data that you will send the function when you *call* it by using the function name.  You include the values you want to use in those variables, in order.  Note that you can also choose to specify the values directly by name, in which case they do not need to be in order.

The command "pass" is also a placeholder, it does nothing but helps preserve the fact that a function contains a block of code.

Note that other variables that are used in a function are local values.  They do not exist outside of a function. Take a look at the program in "scope.py".  Even though y is defined in the main block of code, the program has an error when we try to use y inside the function.  You will also notice that the program crashes when it gets to line 11, because x only exists within the function.  We say that the variable y has a "global scope" and that x has a "local scope".  x is local to the function and can only be used in the function.
You could force the use of y within the function by adding line 4:
```
line4: global y
```
This tells the function to make use of the global value of y, and change the value of y in the global scope if it is changed in the function. However, it is much better practice to instead send the value of y as an input parameter if you need to use it within the function.

A function is intended to return a specific value.

## Assignment
### Assignment 1
#### Random Recipe
Create a function that chooses a random ingredient from a list and returns a string that contains ingredient along with a random value

Your program should call the function several times and display the result.

Criteria:
* use a loop to repeat a block of commands 5 times
* each block should retrieve one value from the function and display it on a line
* you will need to make use of the "random" module (import random) to access the class methods/functions to help you generate random numbers and select random items from a list.


### Assignment 2
#### Check Divisibility
Create a function that receives 2 numbers, divisor and dividend. Return a boolean value (True or False) that indicates whether the first number is evenly divisible by another number

Criteria:
* best way to check divisibilty is using the modulus & operator


### Assignment 3
#### User Input
Create a function that asks the user to enter an integer number.  Return this value as your output.  This allows you to keep your error checking/try except statements out of your main block to keep your main block more concise.

Criteria
* the function does not need an input parameter
* the function returns an integer value

### Assignment 4
#### Prime factorization
Create a program that incorporates assignment 2 and 3 to do the prime factorizations for a number.  You will need to develop an algorithm to determine how you can do this.  If you can't figure it out by the beginning of next class, your teacher will provide you with some pseudocode/a method for determining how you can do this.