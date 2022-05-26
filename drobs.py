from fractions import Fraction
a = Fraction(5, 4)
b =  Fraction(7, 16)
print(a + b)
print(a * b)

c = a * b
print(c.numerator)
print(c.denominator)

print(float(c))