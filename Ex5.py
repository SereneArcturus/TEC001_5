import random

n = int(input("Enter number of points: "))
inside = 0

for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    if x*x + y*y < 1:
        inside += 1

pi = 4 * inside / n
print(pi)