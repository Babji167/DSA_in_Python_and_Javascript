'''n="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
k=int(input("enter your sequence: "))
for i in range(len(n)):
    if i==k:
        break
    else:
        for j in range(i+1):
            print(n[j],end=" ")
        print()

for i in range(len(n)):
    if i==k:
        break
    else:
        for j in range(0,k-i):
            print(n[j],end=" ")
        print()'''

'''n=int(input("enter a sequence: "))
c=1
for i in range(n):
    for j in range(i+1):
        print(c,end=" ")
    print()
    c=c+1

k=n-1
for i in range(n):
    for j in range(n-i-1):
        print(k,end=" ")
    print()
    k=k-1'''

'''n="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
k=int(input("enter your sequence: "))
for i in range(len(n)):
    if i==k:
        break
    else:
        for j in range(i+1):
            print(n[i],end=" ")
        print()

m=k
for i in range(len(n)):
    for j in range(k-i-1):
        print(n[k-i-2],end=" ")
    print()
    m=m-1'''

'''print(ord("A"))
print(chr(97))'''

'''myArray = [int(i) for i in input("enter the elements: ").split()]
first= -1
second=-1 
for i in range(len(myArray)):
    if first<myArray[i]:
        second=first
        first=myArray[i]
print("the second highest number in the Array is {}".format(second))'''










