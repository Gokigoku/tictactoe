import sys
class Queue:
    def __init__(self):
        self.max=5
        self.q=[]

    def is_empty(self):
        return self.q==[]
    def enqueue(self,item):
        if len(self.q)==self.max:
            print("Reached maximum size unable insert")
        else:
            self.q.append(item)
    def dequqeue(self):
        i=0
        print("deleted element is ",self.q.pop(i))
        i+=1
    def getsize(self):
        print("lenth of Queue is: ",len(self.q))
    def dispaly(self):
        print("Queue consist: ")
        for g in self.q:
            print(g ,end=" ")


queu=Queue()
while True:
    print("\n-----QUEUE MENU------ \n  1.inserting\n  2.deleting \n  3.displaysize \n  4.dispaly \n  5.exit")
    try:
        choice = int(input("Enter your choice:\n"))
    except:
        print("Invalid Input")
    if choice==1:
        queu.enqueue(int(input("Enter the item")))
    if choice==2:
        if queu.is_empty():
            print("unamble to delete queue is empty")
        else:
            queu.dequqeue()
    if choice==3:
        queu.getsize()
    if choice==4:
        queu.dispaly()
    if choice==5:
        sys.exit()
print("Enjoy the coding")