a = [1,1,3,4,5,5,6,7,6,8,6,9,6,1,1]
b = [1,2,4,3,5, 1]
def bubble_sort(a):
    zm = True
    while zm == True:
        zm = False
        for i in range(len(a)-1):
            
            if a[i]>a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                zm = True
    return(a)

print(bubble_sort(a))            
