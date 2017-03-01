
# coding: utf-8


def fibonacci_rec (n):
    if n<=1: 
        return 1
    else: 
        return fibonacci_rec(n-1)+fibonacci_rec(n-2)



import scipy.special
def fibonacci_no_rec (n):
    temp_var=1
    for i in range(1,n):
        temp_var=temp_var+scipy.special.binom(n-i, i)
    return temp_var

fibonacci_rec(5)

fibonacci_no_rec(5)
