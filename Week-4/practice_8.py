total = 50#this is a global variable
def sum(arg1,arg2):
    #add both the parameters
    total = arg1 + arg2
    print("Inside the function local total: ",total)
    return total
#now you can call sum function
sum(10,20)
print("Outside the function global total: ",total)