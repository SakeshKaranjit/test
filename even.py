def find_even(a,b):
    sum=0
    for i in range(a,b):
        if i%2==0:
            sum+=i
    print("sum is",sum)
find_even(2,51)
