

# x=[(i,str(i)) for i in range(1,22)]
# print(x)


# def get(x,y):
#     return x+y,True

# print(get(5,6))


class go:
    def __init__(self):
     
        self.mylist=0

    def __iter__(self):
        print('hello')
        
        for c in range(3):
            self.mylist=1
            yield c,self.mylist

 

m=go()
print(m)
print('lis',m.mylist)
for x in m:
    print(x)
