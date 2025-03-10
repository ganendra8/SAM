class MiddleSquareGenerator:
    def __init__(self, seed):
        self.seed = seed
        self.digits = len(str(seed))  

    def next(self):
        squared = self.seed ** 2 
        squared_str = str(squared).zfill(2 * self.digits) 
        middle = len(squared_str) // 2 - self.digits // 2
        next_seed = int(squared_str[middle:middle + self.digits]) 
        self.seed = next_seed
        return next_seed

# Example usage
if __name__ == "__main__":
    seed = 1234 
    generator = MiddleSquareGenerator(seed)

    for _ in range(10):
        print(generator.next())