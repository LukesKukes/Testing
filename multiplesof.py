numbers1 = [1,2,3,4,5,6,7,8,9]
numbers2 = []
l = 0

while l != 1000:
    numbers2.append(l)
    l += 1

def getSum(n):
    sum = 0
    for i in n:
        if i%3== 0 or i%5== 0:
            sum += i
    return sum

print(getSum(numbers1))
print(getSum(numbers2))
