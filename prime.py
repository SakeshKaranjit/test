
# def check_prime(a):
#     for i in range(2,int(a/2)+1):
#         if a%i==0:
#             return False
#     return True
# if check_prime(11):
#     print("prime")
# else:
#     print("not prime")


# # def check_prime(a):
# #     val=0
# #     for i in range(2,a):
# #         if a%i==0:
# #             return val
# #     return val+1
# # if check_prime(11)!=0:
# #     print("prime")
# # else:
# #     print("not prime")

# #wap to give the multiplication table of 5,10,17
# def mul(a):
#     for i in range(1,11):
#         print(f"{a}*{i}={a*i}")
#     print("-------------------")
# mul(5)
# mul(10)
# mul(17)

# my_string="This is aws restart program"
# print(my_string[0])
# print(my_string[-1])
# print(my_string[4:19])
# print(my_string[::-1])

# user_inp=input("Enter your name:")
# print(type(user_inp))

# print(f"Hi {user_inp}, How are you?")
# print("Hi {}, How are you?".format(user_inp))
# print(f"Hi {user_inp}, Your name has {len(user_inp)} characters")
# print(f"Hi {user_inp.upper()}, Your name has {len(user_inp)} characters")
# print(f"Hi {user_inp.lower()}, Your name has {len(user_inp)} characters")

# message = "Hi Sakesh"
# msg = message.replace("Hi", "Hello")
# print(msg)

# user_inp_name=input("Enter your name:")

# user_inp_color=input("Enter your favourite color:")


# print(f"Hi {user_inp_name}!, Your favourite color is {user_inp_color}")

# user_inp=input("Enter a sentence:")
# message="{user_inp}"
# splitted = message.split(",")
# print(f"Total number of words is {len(splitted)}")

# name= 
# frame,name= name.split(",")
# print(frame,name,upper)


#my_list=["mango","litchi","tomato","medicine"]
#            #0    #1     #2       #3        
# print(my_list[1:])

#my list[0]="potato"
#my_list.append("potato")

#my_list.insert(1,"potato")
#my_list.remove(my_list[1])
# forgot=my_list.pop(2)
# print(f"I forgot:{forgot}")
# print(my_list)

#my_list.sort(reverse=True)
# my_list=["mango","litchi","tomato","medicine"]

# my_list1=[1,2,3,4.0,4j]
# print(my_list+my_list1)

numbers=[1,3,5,7,9]

#print(numbers)

#print(numbers[2])

#numbers.remove(numbers[3])
#numbers.insert(3,10)


#numbers.append(12)

#numbers.remove(numbers[2])
#print(numbers)

sliced_list=numbers[2:]
#print(sliced_list)

combined_list=(numbers+sliced_list)
print(combined_list)

print(9 in combined_list)