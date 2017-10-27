import random

class RecurrentGenerator():

    def __init__(self, A, C, M):
        self.A = A
        self.C = C
        self.M = M
        self.prev_val = random.random()

    def generate_next(self):
        self.prev_val = (self.prev_val * self.A + self.C) % self.M
        return self.prev_val

if __name__ == '__main__':
    #A = input('Введите A:')
    #C = input('Введите C:')
    #gen = RecurrentGenerator(A, C, 8)
    gen = RecurrentGenerator(1, 1, 8)
    for n in range(5):
        hits = [0 for x in range(9)]
        for i in range(1000):
            val = gen.generate_next() / 8
            for h in range(1, 10):
                if val <= h / 10:
                    hits[h - 1] += 1
        print("Выборка {}: ".format(n + 1), end='')
        print(hits)