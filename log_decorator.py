# Andrew Stade
# 1/29/2021
# afs18c
# The program in this file is the individual work of Andrew Stade.

import sys
import time

def log(*args):
    if(len(args)==1):
    
        def wrap(x):
            def wrapped_f(*args):
                orig_stdout = sys.stdout
                os = open("logger.txt", "a")
                sys.stdout = os
                os.write("********************************************\n")
                os.write("Calling function " + x.__name__ + "\n")
                os.write("Arguments:\n")
                for arg in args:
                    data = "\t- "+ str(arg)+" of type "+type(arg).__name__+"\n"
                    os.write(data+"\n")
                    
                os.write("Output: " + "\n")
                start_time = time.perf_counter()
                output = str(x(*args))
                end_time = time.perf_counter()
                timeOut = "Execution time " + "%.5f s" % (end_time-start_time)+"\n"
                os.write(timeOut)
                
                sys.stdout= orig_stdout
                if(output != None):
                    data = "Return value: " + str(output) + " of type " + type(output).__name__+"\n"
                    os.write(data)
                else:
                    os.write("No return value."+"\n")
                os.write("********************************************\n\n")
                
            return wrapped_f
        return wrap
    else:
        def wrap(x):
            def wrapped_f(*args):
                print("********************************************")
                print("Calling function " + x.__name__)
                print("Arguments:")
                for arg in args:
                    print("\t- ", arg, " of type ", type(arg).__name__)
                    
                print("Output: ")
                start_time = time.perf_counter()
                output = x(*args)
                end_time = time.perf_counter()
                print("Execution time ", "%.5f s" % (end_time-start_time))
                if(output != None):
                    print("Return value: ", output, " of type ", type(output).__name__)
                else:
                    print("No return value.")
                print("********************************************")
            return wrapped_f
        return wrap
        
from log_decorator import log
import time
@log("hello","world", 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)
@log()
def wasteTime(a,b,c):
    time.sleep(1)
    return(a,b,c)

sayHello("say", "hello", "argument", "list")
@log()
def factorial(*nums_list):
    results = []
    for number in nums_list:
        res = number
        for i in range(number-1,0,1):
            res = i*res
        results.append(res)
        return results
@log("logger.txt")
def waste_time(a,b,c):
    print("Wasting Time")
    time.sleep(5)
    return a,b,c
@log("logger.txt")
def gcd(a,b):
    print("THE GCD of ", a, " and", b, " is ", end="")
    while a!=b:
        if a>b:
            a -= b
        else:
            b -= a
        print(abs(a))
        return abs(a)
@log()
def print_hello():
    print("Hello!")
@log(10)
def print_goodbye():
    print("Goodbye!")
if __name__ == "__main__":
    factorial(4,5)
    waste_time("one", 2, "3")
    gcd(15,9)
    print_hello()
    print_goodbye()