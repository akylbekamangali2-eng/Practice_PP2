class StringHandler:
    def __init__(self,name):
        self.name=name
    
    def up(self):
        return self.name.upper()

x=StringHandler(input())
print(x.up())