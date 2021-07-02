
"""def queue_time(customers, n):
    if len(customers) == 0:
        return 0
    if n == 1:
        return sum(customers)
    new = []
    k=0
    while k < len(customers):
        total = 0
        all = []
        for i in range(k,len(customers),n):
            if k > len(customers):
                break
            else:
                all.append(customers[i])
        total = sum(all)
        k+=1
        new.append(total)
    return max(new)"""



def queue_time(customers, n):
    new=[]
    for i in range(n):
        new.append(0)
    for i in customers:
        new.sort()
        new[0] += i
    return max(new)

#print(queue_time([], 1))
#print(queue_time([2,3,10], 2))
#print(queue_time([1,2,3,4,5], 100))
#print(queue_time([1,3,5,4,2],4))
#print(queue_time([2,2,3,3,4,4], 2))
print(queue_time([24, 24, 50, 49, 21, 6, 7, 37, 4, 36, 6, 23, 50, 32],6)) 