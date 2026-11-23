class ProductOfNumbers:
    pre=[1]
    
    def __init__(self):
        pass
        

    def add(self, num: int) -> None:
        if(num!=0):
            self.pre.append(self.pre[len(self.pre)-1]*num)
        else:
            self.pre=[]
            self.pre.append(1)
        

    def getProduct(self, k: int) -> int:
        if(len(self.pre)-1<k):
            return 0
        
        return self.pre[len(self.pre)-1]//self.pre[len(self.pre)-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)