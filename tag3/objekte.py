class Glass:
    def __init__(self):
        self.max=100
        self.current=25
    def __add__(self, second):
        if self.current+second.current <= self.max:
            self.current+= second.current
            second.current-=second.current
        else:
            free_space = self.max - self.current
            self.current += free_space
            second.current-=free_space
        return self.current

glass1 = Glass()
glass2 = Glass()
print(glass1 + glass2)
print(glass1 + glass2)