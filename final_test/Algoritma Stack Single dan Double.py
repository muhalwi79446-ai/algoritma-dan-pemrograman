# stack_single.py

class StackSingle:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Push: {item}")

    def pop(self):
        if self.is_empty():
            print("Stack kosong, tidak bisa pop!")
            return None
        removed = self.stack.pop()
        print(f"Pop : {removed}")
        return removed

    def peek(self):
        if self.is_empty():
            print("Stack kosong!")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Isi Stack:", self.stack)


# Contoh penggunaan
if __name__ == "__main__":
    s = StackSingle()
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()
    s.pop()
    print("Peek:", s.peek())
    s.display()


# stack_double.py

class StackDouble:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
        self.top1 = -1               # Stack 1 mulai dari kiri
        self.top2 = size             # Stack 2 mulai dari kanan

    def push1(self, item):
        if self.top1 + 1 == self.top2:
            print("Stack1 penuh!")
            return
        self.top1 += 1
        self.array[self.top1] = item
        print(f"Push1: {item}")

    def push2(self, item):
        if self.top2 - 1 == self.top1:
            print("Stack2 penuh!")
            return
        self.top2 -= 1
        self.array[self.top2] = item
        print(f"Push2: {item}")

    def pop1(self):
        if self.top1 == -1:
            print("Stack1 kosong!")
            return None
        removed = self.array[self.top1]
        self.top1 -= 1
        print(f"Pop1 : {removed}")
        return removed

    def pop2(self):
        if self.top2 == self.size:
            print("Stack2 kosong!")
            return None
        removed = self.array[self.top2]
        self.top2 += 1
        print(f"Pop2 : {removed}")
        return removed

    def display(self):
        print("Array :", self.array)
        print("Stack1:", self.array[:self.top1 + 1])
        print("Stack2:", self.array[self.top2:])


# Contoh penggunaan
if __name__ == "__main__":
    sd = StackDouble(10)

    sd.push1(10)
    sd.push1(20)
    sd.push2(99)
    sd.push2(88)

    sd.display()

    sd.pop1()
    sd.pop2()

    sd.display()

