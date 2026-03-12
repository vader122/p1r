import random
def lotto():
    
    a = [0,0,0,0,0,0]
    for i in range(6):
        a[i]=random.randint(1,49)

        if i>0:
            for j in range(i-1):
                if a[i]==a[j]:
                    while a[i]==a[j]:
                        a[i] = random.randint(1,49)
    return a

print(lotto())