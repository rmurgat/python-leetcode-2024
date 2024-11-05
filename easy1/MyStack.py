from collections import deque

# https://leetcode.com/problems/implement-stack-using-queues/
class MyStack:

    def __init__(self):
        self.qu = deque()

    def push(self, x: int) -> None:
        self.qu.appendleft(x)
        

    def pop(self) -> int:
        return self.qu.popleft()
    
    def top(self) -> int:
        ans = self.qu.popleft()
        self.qu.appendleft(ans)
        return ans
        

    def empty(self) -> bool:
        if len(self.qu) == 0: return True
        return False
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()