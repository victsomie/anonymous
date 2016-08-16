def fibonacci(n):
    i=0;
    j=1;
    ls=[]
    ls.append(i)
    ls.append(j)
    while i+j<n:
        fib=i+j;
        ls.append(fib)
        i=j;
        j=fib
    return ls
print(fibonacci(20))
