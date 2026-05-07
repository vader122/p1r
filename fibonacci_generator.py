class FibGenerator():
    def __init__(self):
        self.first = 1
        self.second = 1

    def __iter__(self):
        self.current = self.first
        self.second, self.first = self.second+self.first, self.second
        return self
    
    def __next__(self):
        

        return self.current
        

N = 100

# for x in FibGenerator():
#     if x > N:
#         print(x)
#         break

f = FibGenerator()
print(next(iter(f)))
print(next(iter(f)))
print(next(iter(f)))
print(next(iter(f)))
