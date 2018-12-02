from math import sqrt
from numpy import diag
from numpy import dot
from numpy import array
from scipy.linalg import svd
import math

a = array([[0, 1, 1],[math.sqrt(2),2 , 0],[0,1, 1]])
print(a)
u,s,T = svd(A)
Sigma = diag(s)
B = u.dot(Sigma.dot(T))
print(u)
print(B)
print(T)