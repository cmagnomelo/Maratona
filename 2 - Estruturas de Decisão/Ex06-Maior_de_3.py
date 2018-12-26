n1,n2,n3 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 > n2 and n1 > n3:
    print(n1,'É maior')
elif n2 > n3:
    print(n2, 'É maior')
else:
    print(n3, 'É maior')