# Dictionary is a mutable, ordered and can contain duplicates
# Also it is Heterogeneous 
# Keys are not mutable but Values are
# d = {10: 100, 20: 200, 30:300} 
# d[40] = 400 
# d[10] = 500
# del d[10]
# d.clear()

# print(d[30])

# for i in d:
#     print(d[i], i)

# .copy() method is used to create a shallow copy
# help(dict)

# d1 = d.get(10)
# print(d.items())

# Q1
# d1 = {10: 100, 20: 200, 30:300} 
# d2 = {40: 400, 50: 500, 60:600} 

# for i in d2:
#     d1[i] = d2[i]
# print(d1)

# Q2
# d1 = {10: 100, 20: 200, 30:300}
# sum = 0

# for i in d1:
#     sum = sum + d1[i]
# print(sum)

# Q3
# a = [1,1,1,1,3,3,2,3,4,4,2,3,2]
# diction= {}
# for i in a:
#     if i in diction.keys():
#         diction[i] += 1
#     else:
#         diction[i] = 1
# print(diction)

# Q4
d1 = {10: 100, 20: 200, 40:300} 
d2 = {40: 400, 50: 500, 60:600} 

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]
print(d1)