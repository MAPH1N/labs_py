def even_generator(n):
    for i in range(0,n+1):
        if i%2==0:
            yield i

n = int(input("Enter a value for n: "))

Even = even_generator(n)

for i in Even:
    print(i)