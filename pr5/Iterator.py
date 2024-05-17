class MyIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.max_num<0:
            if self.current > self.max_num:
                self.current -= 1
                return self.current
            else:
                raise StopIteration
        else:    
            if self.current < self.max_num:
                self.current += 1
                return self.current
            else:
                raise StopIteration

# Использование итератора
iterator = MyIterator(12)
for num in iterator:
    print(num)
