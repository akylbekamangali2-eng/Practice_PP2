class shape:
    def __init__(self,val):
        self.val=val

    def length(self):
        return self.val*self.val

x=shape(int(input()))
print(x.length())