    # def __init__(self, k: int):
    #     self.size= k
    #     self.array = [None] * self.size
    #     self.front=0
    #     self.last=0
    #     self.count=0
    

    # def isEmpty(self) -> bool:
    #     return self.count == 0

    # def isFull(self) -> bool:
    #     return self.count == self.size
  

    # def insertFront(self, value: int) -> bool:
    #     if self.isFull():
    #         raise False
    #     self.array[self.front]= value
    #     self.front= (self.front - 1) % self.size
    #     self.count += 1
    #     return True

        

    # def insertLast(self, value: int) -> bool:
    #     if self.isFull():
    #         return False
    #     self.array[self.last]= value
    #     self.last = (self.last + 1) % self.size
    #     self.count += 1
    #     return True
        

    # def deleteFront(self) -> bool:
    #     if self.isEmpty():
    #         raise False
       
    #     self.front +=1
    #     self.count -=1  
    #     return True
        

    # def deleteLast(self) -> bool:
    #     if self.isEmpty():
    #         raise False
    #     self.last -=1
    #     self.count -=1
    #     return True 
        

    # def getFront(self) -> int:
    #     if self.isEmpty():
    #         return -1
    #     return self.array[self.front]
        

    # def getRear(self) -> int:
    #     if self.isEmpty():
    #         return -1
    #     return self.array[self.last]