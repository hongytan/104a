# Math 104A Homework 1
# Problems 16, 17
# Due October 5, 2021

from math import e
import math

# Four digit rounding
# Rounding function
def round_single(a):
    # Separating whole numbers and decimal places
    if '-' in str(a):  
        neg, num = str(a).split('-')
        whole, dec = num.split('.')
    else:
        whole, dec = str(a).split('.')

    # Determining number of decimal places depending on digits in whole number
    if (len(whole) >= 4):
        return int(whole)
    elif (len(whole) == 3):
        return round(a,1)
    elif (len(whole) == 2):
        return round(a,2)
    elif (len(whole) == 1 and whole != "0"):
        return round(a,3)
    else: # 0.0000213002
        return round(a,4)

# Four digit chopping
# Chopping function
def chop(a):
    # Separating whole numbers and decimal places
    if '-' in str(a):  
        neg, num = str(a).split('-')
        whole, dec = num.split('.')
    else:
        whole, dec = str(a).split('.')

    # Chopping num into 4 digits
    if (len(whole) >= 4):
        return int(whole)
    elif (len(whole) == 3):
        return (math.trunc(a*10)/10.0)
    elif (len(whole) == 2):
        return (math.trunc(a*100)/100.0)
    elif (len(whole) == 1 and whole != "0"):
        return (math.trunc(a*1000)/1000.0)
    else: 
        return (math.trunc(a*1000000)/1000000.0)


            
def using_11_x1(a,b,c,f):
    try:
        return f(f(-b + f(math.sqrt( f(f(b**2) - f(4 * f(a*c)))))) / (f(2*a)))
    except ZeroDivisionError:
        print("11_x1: Dividing by 0.")

def using_11_x2(a,b,c,f):
    try:
        return f(f(-b - f(math.sqrt( f(f(b**2) - f(4 * f(a*c)))))) / (f(2*a)))
    except ZeroDivisionError:
        print("11_x2: Dividing by 0.")

def using_12_x1(a,b,c,f):

    try: 
        return f((f(-2 * c)) / (f(b + f(math.sqrt( f(f(b**2) - f(4 * f(a * c))))))))
    except ZeroDivisionError:
        print("12_x1: Dividing by 0.")

def using_13_x2(a,b,c,f):
    try:
        return f((f(-2 * c)) / (f(b - f(math.sqrt( f(f(b**2) - f(4 * f(a * c))))))))
    except ZeroDivisionError:
        print("13_x2: Dividing by 0.")

a = 1.002
b = 11.01
c = 0.01265

print("11.x1", using_11_x1(a,b,c,chop))
print("11.x2", using_11_x2(a,b,c,chop))
print("12.x1", using_12_x1(a,b,c,chop))
print("13.x2", using_13_x2(a,b,c,chop))
