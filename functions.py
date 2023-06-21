#wap to show use case for return value and argument

#adding
def adding(a,b,c):
    print("hello numbers",a,b,c)
    print("their sum=", a+b+c)
    adding(10,20,30)

def adding(a,b,c):
    print("hello numbers",a,b,c)
    
    return(a+b+c)
    print ("their sum =", adding(10,20,30))


