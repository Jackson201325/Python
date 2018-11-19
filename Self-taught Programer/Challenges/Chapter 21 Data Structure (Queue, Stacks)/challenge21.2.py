class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


stack = Stack()

for i in range(1, 6):
    stack.push(str(i))
    print(stack.items)

reverse = ""

for i in range(len(stack.items)):
    reverse += stack.items.pop()


print()

print(reverse)
