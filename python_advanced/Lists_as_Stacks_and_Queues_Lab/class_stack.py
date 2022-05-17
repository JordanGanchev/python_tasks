class Stack:
    def __init__(self):
        self.value = []


    def push(self, value):
        self.value.append(value)

    def pop(self):
        return  self.value.pop()


    def peek(self):
        return  self.value[-1]


    def count(self):
        return len(self.value)


s = Stack()

for v in range(5, 10):
    s.push(v)

print(s.pop())
print(s.peek())
print((s.count()))

