# def adding():
#     sum=5+9
#     #print(sum,a+b)
#     multiply=5*9
#     #print(multiply,a*d)
#     return sum,multiply
#     a=5
#     b=6
#     c,d=adding()
# print(c,d)

val=5
a=20
b=10
def adding():
    print("val from function",val)
    # a=3
    # b=2
    print("add of a and b inside function",a+b)
    return(a+b)
print("return value is",adding())
adding()
a=5
b=6
val=val+4
print("val is",val,"and sum of a and b is", a+b)
adding()