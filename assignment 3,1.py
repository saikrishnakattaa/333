#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)

# Expected Output : 20

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))


# another way:

def sum_of_lst(list):
    sum = 0

    for i in list:
        sum += i
    return sum

list = [8, 2, 3, 0, 7]

print(sum_of_lst(list))


# In[ ]:




