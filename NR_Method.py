# Newton Raphson method to solve non-linear equations. Please read the documentation in details
import sys

def nr(func, deriavtive, x, small_value):   #this is the function which is called by the user
    f_value = func(x)                       #this will jump to the function func and will put the value of x there
    print("Initial value of x before starting iteration is:",x)  #this is x0 provided by the user
    counter=0;                                #this indicated that iterations has not been started
    final_value=int(input("Enter the times you want to iterate the program:")) #this is the limit till iteration should continue
    while(abs(f_value)>small_value and counter<final_value):
        try:
            x=x-float(f_value)/deriavtive(x)
        except ZeroDivisionError:            #some times there is zero division occurs and hence we should consider this
            print("Zero division error occurs:")
            sys.exit()
        print("value of x after {} iteration is: ".format(counter+1),x)    #display the progress after each iteration
        f_value = func(x)
        counter += 1
        print("Value of function(x) after putting above x is",f_value)
        if (f_value<small_value):                                         #condition to stop the operation either through iterations
                                                                          # or through this condition
            break;
    return f_value,counter,x

#Please see the usage of this function in the function nr
def func(x):
    return x**2-16;
#Please see the usage of this function in the function nr
def deriavtive(x):
    return 2*x;
#this is what user will call
[f_value,counter,x] = nr(func, deriavtive, x=1000, small_value=1.0e-6)
print("************************************************************")
print("Final value of function after selected iterations is:",f_value)
print("Final value of x after selected iterations is:",x)
