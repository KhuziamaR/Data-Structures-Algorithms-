from collections import deque
import threading
import time

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    def front(self):
        res = self.buffer.pop()
        self.buffer.append(res)
        return res
        
    
    def size(self):
        return len(self.buffer)



def placeOrder(orders,que):
    for item in orders:
        time.sleep(0.5)
        que.enqueue(item)
        print('placing order: ', item )
def serveOrder(orders,que):
    for item in orders:
        time.sleep(0.5)
        if(que.size()>0):
            print('serving: ', que.dequeue())

t=time.time()
Q = Queue()

orders = ['pizza','samosa','pasta','biryani','burger']

t1 = threading.Thread(target=placeOrder,args=(orders,Q,))
t2 = threading.Thread(target=serveOrder,args=(orders,Q,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Orders served")

q1 = Queue()



