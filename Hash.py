

class Hash_Table():
    def __init__(self):
        self.max=100
        self.arr=[None for i in range(self.max)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
    
        return h%100

    def __add__(self,key,val):
        h=self.get_hash(key)
        self.arr[h]=val
        
    def __get_item__(self,key):
        h=self.get_hash(key)
        return self.arr[h]




    


hash1=Hash_Table()
print(hash1.get_hash('march 6'))




print(hash1.arr)
print(hash1.__add__('march 6',130))
print(hash1.__add__('march 7',20))
print(hash1.__get_item__('march 7'))



