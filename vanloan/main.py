# Numerical evaluation (VanLoan)
from numpy import array
from lib.vanloan import numeval

# System values
dt = 0.1   # interval (seconds)
m = 1      # mass (kg)
k = 0.1    # spring constant
c = 0.05   # damper constant

# Dynamics matrix
F = array([[0, 1],
           [-k/m, -c/m]])

# Process noise coefficients
G = array([[0],
           [2]])

# Numerical evaluation
[phi, Q] = numeval(F, G, dt)

print(phi)
print(Q)