"""
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def rec_factorial(n):
    if n == 1:
        return n
    return n * rec_factorial(n - 1)


print(rec_factorial(100))

a = 1
c = 0
for i in range(2, 100):
    a*=i
print(a)

while a > 0:
    c += a % 10
    a //= 10

print(c)

