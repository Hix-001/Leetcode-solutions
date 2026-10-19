# 27/09/2026
# Medium
# LeetCode 155: Min Stack using a state-tracking tuple array.

class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))
    def pop(self) -> None:
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1][0]
    def getMin(self) -> int:
        return self.stack[-1][1]
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin()) 
    minStack.pop()
    print(minStack.top())    
    print(minStack.getMin())