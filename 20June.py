# # my_tuple=(99,98,1,2,3,4,5,1,1)
# # # my_tuple2=(99,1,2,3,4,5)
# # # print(my_tuple+my_tuple2)
# # # count_1=my_tuple.count(1)
# # # new_tuple=sorted(my_tuple)
# # new_tuple=sorted(my_tuple,reverse=True)
# # print(new_tuple)
# # print(3 in my_tuple)
# # print(tuple(my_tuple))
# # print(max(my_tuple))
# # print(min(my_tuple))

# my_tuple=(10,20,'a','b',True)

# # # print(my_tuple[3])

# tuple1=(1,2,3)
# tuple2=('x','y','z')
# concatenated_tuple=(tuple1+tuple2)
# # print(concatenated_tuple)

# # repeated_tuple=(my_tuple*3)
# # print(repeated_tuple)

# print(len(concatenated_tuple))

# sliced_tuple=my_tuple[2:4]
# print(sliced_tuple)



# my_dist ={
#     "Name":"Rishab"
#     "Age":16,
#     "Address":{
#         "Address1":"Kathmandu",
#         "Zip":{
#             "Zip1":44800
#             "Zip2":44600
#         }
#     }
# }

# #my_dist["Age"]=21
# #my_dist={"College":"KMC"}
# #print(my_dist["Address"]["Zip"]["Zip1"])
# #del my_dist["Age"]
# #new_age=my_dist.pop("Age")
# #print(new_age)
# print(my_dist)


#wap to show multiplication table of first 20 prime numbers using nested for loop

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# primes = []
# num = 2

# while len(primes) < 20:
#     if is_prime(num):
#         primes.append(num)
#     num += 1

# for i in primes:
#     print(f"Multiplication table of {i}:")
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print()




# def check_prime(a):
#     val=0
#     for i in range(2,a):
#         if a%i==0:
#             return val
        
#     return val+1
    
        
# prime_list = []
# a = 2

# while len(prime_list) < 20:
#     if check_prime(a):
#         prime_list.append(a)
#     a += 1

# for i in prime_list:
#     print(f"Multiplication table of {i}:")
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print("-------------------------------")

# list=[]
# for j in range(20,30):
#     prime=1
#     for i in range(2,j):
#         if j%i==0:
#             prime=0
#             break
#     if prime==1:
#             list.append(j)
# print(list)


# list=[]
# for j in range(20,30):
#     prime=True
#     for i in range(2,j):
#         if j%i==0:
#             prime=False
#             break
#     if prime:
#             list.append(j)
# print(list)

#wap to find a simple interest
# p=float(input("Enter principal amount"))
# t=float(input("Enter time period in years"))
# r=float(input("Enter rate of interest in number"))
# si=(p*t*r)/100
# print("simpleinterest",si)

#wap to find perimeter of rectanguar ground
# l=float(input("Enter length:"))
# b=float(input("Enter breadth:"))

# p=2*(l+b)
# print("perimeter",p)

#find volume of irregular body
#drop body on fully filled water tank and the spilled volume of water is volume of irregular body

#wap to calculate volume of cube
# a=float(input("Enter edge value: "))
# v=(a*a*a)
# print("Volume of cube:",v)

#wap to find square root of a number

num=float(input("Enter k ko square root nikalne:"))
squareroot= sqrt(num)
print("Square root of {num} is",squareroot)

#wap to find error percentage

#take a string as input and check whether the string is Rishab Karki or not.
a=" Rishab Karki"