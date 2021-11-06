# Math 104A Homework #2 
# Hong Yuan Tan
# Due October 12, 2021

import math

########## Section 1.3 ##########
# Problem 1b

# Three digit chopping
# Chopping function
def chop(a):
    # Separating whole numbers and decimal places
    whole, dec = str(a).split('.')

    # Chopping num into 3 digits
    if (whole != '0'):
        return (math.trunc(a*1000)/1000.0)
    else: 
        sig_num = '0.'
        count = 4
        for digit in dec:
            if digit == '0':
                sig_num += '0'
            else:
                sig_num += digit
                count -= 1
                if count == 0:
                    return float(sig_num)
        return float(sig_num)

def problem1():
    asc_list = [chop(1/(i**3)) for i in range(1,11)]
    desc_list = [chop(1/(i**3)) for i in range(10,0,-1)]
    print(asc_list)
    print(desc_list)
    total = 0
    for num in asc_list:
        total = chop(total + num)
    print(total)

# Problem 2a. 
def problem2():
    sum_list = [chop(1/math.factorial(i)) for i in range(6)]
    print(sum_list)

    total = 0
    for num in sum_list:
        total = chop(total + num)
    print(total)
    print(sum([(1/math.factorial(i)) for i in range(6)]))

# Problem 4.
def problem4(terms):
    def arctan(x, terms):
        sum_list = [((-1)**(i+1) * (x**(2*i-1)) / (2*i-1)) for i in range(1,terms+1)]
        return sum(sum_list)

    print(4 * (arctan(1/2,terms) + arctan(1/3,terms)))

# Problem 8b. 
def problem8b(n):
    print(1/n)
    print(1/n**2)
    print(1/n**3)
    print(1/n**4)

# Problem 11. 
def problem11(n):
    def fib(n):
        if n == 0 or n == 1:
            return 1
        else: 
            return fib(n-2) + fib(n-1)

    print(fib(n)/fib(n-1))

##### Section 2.1 ######

# Bisection method
def bisection(a, b, TOL, N, f):
    i = 0
    FA = f(a)

    while (i < N):
        p = a + (b-a)/2
        FP = f(p)

        if FP == 0 or (b-a)/2 < TOL:
            return p
        
        i += 1
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
    
    return f"Method failed after {N} iterations."

# Function for bisection method - input manually
def f(x):
    return (10*(  0.5*math.pi - math.atan(x) - x*(1-x**2)**(1/2) ) - 12.4)

# Problem 4
def problem4(a,b):
    i = 1
    while (bisection(a,b,0.01, i, f) == f"Method failed after {i} iterations."):
        i+=1 
    print(i, bisection(a,b,0.01, i, f))

# Problem 6
def problem6(a,b):
    i = 1
    while (bisection(a,b,0.00001, i, f) == f"Method failed after {i} iterations."):
        i+=1 
    print(i, bisection(a,b,0.00001, i, f))

# Problem 11
def problem11(a,b):
    i = 1
    while (bisection(a,b,0.0, i, f) == f"Method failed after {i} iterations."):
        i+=1 
    print(i, bisection(a,b,0.0, i, f))

# Problem 15
def problem15(a,b):
    i = 1
    while (bisection(a,b,0.01, i, f) == f"Method failed after {i} iterations."):
        i+=1 
    print(i, bisection(a,b,0.01, i, f))


###### Section 2.2 #########

# Fixed point iteration
def fixed_point_iter(p0, TOL, N, g):
    i = 1
    while (i < N):
        p = g(p0)
        print(i,p)
        if abs(p-p0) < TOL:
            return p

        i += 1
        p0 = p

    return "Failed"

# Function for fpi - input manually
def g(x):
    return (3*x**2 + 3)**(1/4)

# Problem 3
def problem3():
    print(fixed_point_iter(1, 0.01, 5, g))

# Problem 5a
def problem5a_22(n):
    if n == 0:
        return 1
    else:
        n_1 = problem5a_22(n-1)
        return (20 * n_1 + 21/n_1**2)/21

# Problem 5b
def problem5b_22(n):
    if n == 0:
        return 1
    else:
        n_1 = problem5a_22(n-1)
        return n_1 - ((n_1**3 - 21) / (3*n_1**2))

# Problem 7
def problem7_22():
    print(fixed_point_iter(1, 0.01, 7, g))

