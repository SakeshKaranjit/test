#wap to find area of circle with radius 7.5,8.97,20.39,100,129,139,600,1000,5.6,8.9,12.7,11.25,12.13
# radius_circle=[7.5,8.97,20.39,100,129,139,600,1000,5.6,8.9,12.7,11.25,12.13]
# for r in radius_circle:
#     area=3.1414*r*r
#     print(f"area of circle:{area}")
# area2 = 3.14*radius_circle[1]*radius_circle[1]
# print("area of circle in 1st position:",area2)


# for i in (0,10,2,2,3):
#     print(i)

# for i in range(20,2,-3):
#     print(i)

# radius=[3,5,7,8,9]
# for i in radius:
#     print(f"area for radius {i} is {3.14*i*i}")

# from copy import deepcopy
# list_a=[1,2,3,4,5]
# list_b=deepcopy(list_a)
# list_b[0]="ram"
# print("list b: ", list_b)
# print("list a: ", list_a)

# import copy
# list_a=[1,2,3,4,5]
# list_b=copy.deepcopy(list_a)
# list_b[0]="ram"
# print("list b: ", list_b)
# print("list a: ", list_a)

# fruits=["apple","banana","cherry"]
# for index, value in enumerate(fruits):
#     print(index,value)
    
# print(fruits[0])

# text='hello ram'
# for abc in text:
#     print(abc)

# se={1,2,3,4}
# print(type(se))
# print(se)

# a=[1,2,3,4,5,6,7,8,9,10]
# b=[4,5,6,7,8,9,10,11,12,13]
# c=[0,0,0,0,0,0,0,0,0,0]
# for i in range(0,10):
#     for j in range(0,10):
#         for k in range(0,10):
#             print(i,j,k)

# a=[[1,1,1],[2,2,2],[3,3,3]]
# print(a)
# for i in range(0,3):
#     for j in range(0,3):
#         a[i][j]=1+a[i][j]
# print(a)

# a=[[1+a[i][j] for j in range(0,3)] for i in range(0,3)]
# print(a)

#a=[[1,1,1],[2,2,2],[3,3,3]]
#print(a)
# for i in range(0,3):
#     for j in range(0,3):
#         a[i][j]=i+a[i][j]
# print(a)

# a=[[1,2,3],[4,5,6],[7,8,9]]
# print(a)
# for i in range(0,3):
#     for j in range(0,3):
#         a[i][j]=1+a[i][j]
# print(a)

# lst=[2,3,4,5,6]
# a=(x**2 for x in lst)
# print(a)
# a=[]

# for x in lst:
#     a.append(x**2)
#     print(a)


number=float(input("Enter a number: "))
if number < 0:
    print("Number is negative")
elif number == 0:
    print("Number is zero")
elif number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

