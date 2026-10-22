#Category: Arrays
# question 1 
# Problem Description: Given a list of integers, calculate the sum of all elements without using Python's built-in sum() function. Return 0 for an empty list.

# l=[1,2,3,4,5]
# def cal_sum(l):
#     sum=0
#     for i in l:
#         sum += i
#     return sum
# print(cal_sum(l))

# question 2 
# Problem Description: Given a list of integers, count how many numbers are even and how many are odd.
l=[1,2,3,4,5,6,7,8,9]

def count_odd_event(l):
    counts={
        "count_even":0,
        "count_odd":0
    }
    for i in l:
        if i%2 ==0:
            counts["count_even"]+=1
        else :
            counts["count_odd"]+=1
    return counts

print(count_odd_event(l))