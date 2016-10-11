#https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        if (len(self.second) == 0):
            for item in reversed(self.first):
                self.second.append(item)
                self.first.pop()
        return self.second[-1]
        
    def pop(self):
        if (len(self.second) == 0):
            for item in reversed(self.first):
                self.second.append(item)
                self.first.pop()
        self.second.pop()
        
    def put(self, value):
        self.first.append(value)


queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        
