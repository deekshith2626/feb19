def isprime(n):
    for i in range(2,n):
        if n%2==0:
            return False
    return True
n=int(input("enter the number of prime : "))
count=0
for i in range(2,n+1):
    if isprime(i):
        count+=1
        print(i,end='    ')
        print(" the count of prime numbers",count)
        
