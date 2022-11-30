from typing import List

class StockSpanner:

    def __init__(self):
        self.data = [] # empty stack to hold prices and consec. days for that price 

    def next(self, price: int) -> int:
        s = 1
        while self.data and self.data[-1][0] <= price:
            print(self.data)
            s += self.data[-1][1] # grab # of consec days for the one b4 
            self.data.pop() # remove it, dont need it anymore 
        self.data.append((price, s))
        return s