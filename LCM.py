class LinearCongruentialGenerator:
    def __init__(self, sedd, a, c, m):
        self.a = a
        self.c = c
        self.m = m
        self.seed = seed

    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed


if __name__ == "__main__":
    seed = 8

    a = 845487 #Multiplier

    c = 318 #Increment

    m = 2**8 #Modulus

    lcg = LinearCongruentialGenerator(seed, a, c, m)

    for _ in range(10):
        print(lcg.next())