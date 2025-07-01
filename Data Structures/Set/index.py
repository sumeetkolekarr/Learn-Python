# Sets are Mutable, Unordered and can't contain Duplicates
# Sets can store data types like string, numbers and tuples but not everything
# s = {1,2,3,4,5,5,4,1}
# for i in s:
#     print(i)

# Methods in Set 
# s.add(6)
# s.remove(8)
# pop_elem = s.pop()
# s.discard(5)
# s.clear()

s1 = {1,2,3}
s2 = {3,4,5}
union = s1|s2
intersect = s1&s2
diff = s1-s2 
symm_diff = s1^s2
print(union, intersect)