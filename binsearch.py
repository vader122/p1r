a = [1, 2, 6, 7, 9, 7, 8, 8, 12, 34]

def bin_search(szuk, c, min=0, max=None):
    
    if max is None:
        max = len(c)-1

    c = sorted(c)
    
    print(c[min:(max+1)])

    if max-min+1 > 1:
        if (max+min+1) % 2 == 0:
            if szuk < c[int(((max+min+1)/2))]:
                print('szuk mniejszy')
                bin_search(szuk, c, min, int(((max+min+1)/2)-1))
                
            if szuk > c[int(((max+min+1)/2))]:
                print('szuk wiekszy')
                bin_search(szuk, c, int((max+min+1)/2+1), max)
                
            if szuk == c[int(((max+min+1)/2))]:
                print(f'szukana pozycja to {int(((max+min+1)/2))}')
        if (max+min+1) % 2 == 1:
            if szuk < c[int(((max+min)/2))]:
                print('szuk mniejszy')
                bin_search(szuk, c, min, int(((max+min)/2)-1))
            if szuk > c[int(((max+min)/2))]:
                print('szuk wiekszy')
                bin_search(szuk, c, int(((max+min)/2)+1), max)
            if szuk == c[int(((max+min)/2))]:
                print(f'szukana pozycja to {(max+min)/2}')
    

    else:
        if c[min] == szuk:
            print(f'szukana pozycja to {min}')
        else:
            print('brak szukanego elementu w liście')


bin_search(34, a)