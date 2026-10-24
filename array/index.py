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
# l=[1,2,3,4,5,6,7,8,9]

# def count_odd_event(l):
#     counts={
#         "count_even":0,
#         "count_odd":0
#     }
#     for i in l:
#         if i%2 ==0:
#             counts["count_even"]+=1
#         else :
#             counts["count_odd"]+=1
#     return counts

# print(count_odd_event(l))

# question 3 
# Problem Description: Find the second-largest distinct element in a list of integers. Return None if fewer than
# l=[1,2,8,4,5]
# first_val=l[0]
# for i in l:
#     if i > first_val:
#         first_val=i
   
# print(first_val) 




# l = [8]

# largest = l[0]
# second_largest = None

# for i in l:
#     if i > largest:
#         second_largest =largest
#         largest = i

#     elif i < largest and (
#         second_largest is None or i > second_largest
#     ):
#         # Update the second largest
#         second_largest = i

# print("Largest:", largest)
# print("Second largest:", second_largest)

# question 4 
# Problem Description: Given a sorted list, remove duplicate elements in place so that each distinct element appears once. Return the number of unique elements.
l=[1,2,3,3,4,5,6,6,18]
new_l=[]
for i in l:
    if i in new_l:
        continue
    else:
        new_l.append(i)
print(new_l) 