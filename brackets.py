def brackets(arg, ciag):
    if arg == 'check':
        stos = []
        for i in range(len(ciag)):
            if ciag[i] == '[' or ciag[i] == '{' or ciag[i] == '(':
                stos.append(ciag[i])
            if ciag[i] == ']' and stos[-1] == '[':
                stos.pop()
            if ciag[i] == '}' and stos[-1] == '{':
                stos.pop()
            if ciag[i] == ')' and stos[-1] == '(':
                stos.pop()
        if stos == []:
            return True
        else:
            return False


    if arg == 'fix':
        stos = []
        zw = 0
        for i in range(len(ciag)):
            if ciag[i] == '(':
                stos.append(ciag[i])
            if ciag[i] == ')' and stos[-1] == '(' and len(stos)>0:
                stos.pop()
            if len(stos)== 0:
                zw = zw+1

        return(len(stos)+zw)

    if arg == 'list': 
        pass


#a = brackets('check', "()(){([[]])[[{}()]]}([)]")
#print(a)

b = brackets('fix', '()(())())')
print(b)