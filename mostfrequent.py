a = [1,1,3,4,5,5,6,7,6,8,6,9,6,1,1]

def most_frequent(a):
    a = sorted(a)
    max = a.count(a[0])
    c = []
    d=[]
    for i in range(len(a)):

        if a.count(a[i])== max:
            max = a.count(a[i])
            c.append(a[i])

        if a.count(a[i])>max:
            c = []
            max = a.count(a[i])
            c.append(a[i])
            
    for i in range(len(c)):
        d.append((c[i],max))
    return (d[::max])

print(most_frequent(a))
print(a)