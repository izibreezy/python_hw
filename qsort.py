
# coding: utf-8

# In[47]:

def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p - 1)
        quicksort(A, p + 1, hi)

def partition(A, lo, hi):
    pivot = A[hi]
    i = lo - 1    
    for j in range(lo,hi - 1):
        if A[j] <= pivot:
            i = i + 1
            t=A[i]
            A[i]=A[j]
            A[j]=t
    k=A[i+1]
    A[i+1]=A[hi]
    A[hi]=k
    return i + 1


# In[48]:

A=[100,10,15,900,300,1,2000,4]
quicksort(A, 0,7)
print A


# In[ ]:



