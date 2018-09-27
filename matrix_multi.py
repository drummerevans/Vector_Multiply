import scipy as sp

a = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

x = sp.matrix("1 2 3 ; 3 4 5 ; 7 8 10")
print(x)
y = sp.matrix("1 2 3 ; 3 6 9 ; 3 9 3")
print(y)

z = sp.dot(x, y)

print("Matrix multiplication of xy = \n", z)

