# List is mutable and Heterogeneous
a = [12,5,4,23,78,2,True, print()]

# print(a[1])
# print(a[1:5])
# print(a[-2])

# Avoid This
# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i])

# Some Methods 
l = [30,5,3,5,1,3,6]

# Inserts at the end of the list 
l.append(5)

# Inserts at a specified location 
l.insert(1,2)

# Removes the First Occurance
l.remove(5)

# List Mutability
l[0] = 1

# print(l)

# Q1
# nums = [-4,5,-6,4,-5]
# print('Positive Nums are ')
# for i in nums:
#     if i >= 0:
#         print(i)
# print('Negative Nums are ')
# for i in nums:
#     if i < 0:
#         print(i)

# Q2
# nums = [4,5,6,4,5]
# sum = 0
# for i in nums:
#     sum+=i
# print(f'The mean is {sum/len(nums)}')

# Q3
# nums = [4,5,6,4,5]
# largest = nums[0]
# index = 0
# for i in range(len(nums)):
#     if nums[i] > largest:
#         largest = nums[i]
#         index = i
# print(largest, index)

# Q4
# nums = [4,5,6,4,5]
# largest = nums[0]
# sec_large = nums[0]
# for i in range(len(nums)):
#     if nums[i] > largest:
#         sec_large = largest
#         largest = nums[i]
#     elif nums[i] > sec_large:
#         sec_large = nums[i]
# print(sec_large)

# Q5
nums = [4,5,6,7,8]

for i in range(len(nums)-1):
    if nums[i] < nums[i+1]:
        continue
    else:
        print('Your list is not sorted!')
        break
else:
    print('Your List is sorted')