n=int(input("digite el inicio "))
m=int(input("digite el final "))
if n>m:
    print("lo siento digite unos valores de modo que el primero sea el menor")
else:
    for i in range(n,m+1):
        print(i)