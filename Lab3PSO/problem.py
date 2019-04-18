class Problem:
    def __init__(self):
        self.n = None
        self.m = None
        self.A = None
        self.S = []
        self.loadData()

    def loadData(self):
        with open("data.txt") as f:
            self.n = int(f.readline())
            self.A = (f.readline().split())
            self.A = [int(x) for x in self.A]
            self.m = int(f.readline())
            for i in range(self.m):
                Si = f.readline().split()
                Si = [int(x) for x in Si]
                self.S.append(Si)

