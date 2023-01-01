class DigitalCounter:
    def __init__(self, start=0, end=100, current=None):
        self.start = start
        self.end = end
        self.current = current
        if self.current is None:
            self.current = self.start

    def increase(self):
        self.current += 1
        if self.current >= self.end:
            self.current = self.start

    def get_current_value(self):
        return self.current


if __name__ == '__main__':
    c = DigitalCounter()
    print(c.get_current_value())
    for i in range(111):
        c.increase()
    print(c.get_current_value())
