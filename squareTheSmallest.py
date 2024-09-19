"""https://projecteuler.net/problem=822"""




n = 10000
m = 10000000000000000
#n = 5
#m = 3
array = []


def getArray(n):
    while n > 1:
        array[:0] = [n]
        n -= 1
        
    return array 

def getSum(a,m):
    while m > 0:
        y = 0
        x = a[0]
        for i in range(0, len(a)):
            if a[i] < x:
                x = a[i]
                y = i
        a[y] = x*x
        m = m-1
    answer = sum(a)%1234567891
    return sum(a)

d = getArray(n)
print(getSum(d,m)%1234567891)