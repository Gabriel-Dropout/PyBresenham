class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, p):
        return point(self.x + p.x, self.y + p.y)
    def __sub__(self, p):
        return point(self.x - p.x, self.y - p.y)
    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"

if __name__ == "__main__":
    p1 = point(2, 4)
    p2 = point(5, 3)
    print("p1    is ", end="");
    print(p1);
    print("p2    is ", end="");
    print(p2);
    print("p1+p2 is ", end="");
    print(p1+p2);
    print("p1-p2 is ", end="");
    print(p1-p2);
