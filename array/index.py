# question 1 
# Problem Description: Given a list of integers, calculate the sum of all elements without using Python's built-in sum() function. Return 0 for an empty list.

l=[1,2,3,4,5]
def cal_sum(l):
    sum=0
    for i in l:
        sum += i
    return sum
print(cal_sum(l))
        