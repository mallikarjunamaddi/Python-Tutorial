# # unordered
# # unique, removes duplicates
# # set is mutable
# # Elements must be immuttable (int, float, string, tuple)
# # No indexing
# # type <class 'set'>

# #creating 
# s1 = {1, 2, 3}
# s2 = set(["a", "b", "a", 1, (1, 2)])
# print(s2)

# #creating empty set
# s3 = set()
# print(s3, type(s3))
# d1 = {}
# print(d1, type(d1))

# #set with mutable elements
# s4 = {"a", 1, [1, 2]}

# #To add a single element to set
# s5 = {1, 3}
# print(s5)
# s5.add(2)
# print(s5)

# #To add multiple elements
# s6 = {1, 3, 5}
# print(s6)
# s6.update([2, 4])
# print(s6)

# #To remove an element with discard
# s7 = { 1, 2, 4}
# print(s7)
# s7.discard(2)
# print(s7)
# # s7.discard(0)
# print(s7)

# # To remove an element with remove
# s7 = { 1, 2, 4}
# print(s7)
# s7.remove(2)
# print(s7)
# s7.remove(0)
# print(s7)

# # pop method
# s7 = { 1, 2, 4}
# print(s7)
# s7.pop()
# print(s7)

# #set operations
# s8 = {1, 3, 9}
# s9 = {2, 3, 4}
# print(s8|s9)

# #union method
# print(s8.union(s9))
# print(s8)

# #intersection
# print(s8&s9)
# print(s8.intersection(s9))

# #intersectioin_update, takes common of all sets and assigns to the result set.
# s10 = {3, 4, 9}
# print(s8)
# s8.intersection_update(s9, s10)
# print(s8)

# #difference
# print(s9-s10)
# print(s10-s9)
# print(s10.difference(s9))

# #symmetric difference
# s11 = {1, 2, 5}
# s12 = {2, 7}
# print(s11^s12)
# print(s11.symmetric_difference(s12))


# #set comparision
# s13 = {2, 3, 4}
# s14 = {3, 4}
# print(s13>s14)
# print(s13<s14)
# print(s13==s14)

# #iteration
# for item in s13:
#     print(item)

#frozenset
fset = frozenset([1, 2, 3])
print(fset, type(fset))   

fset.add(5)
fset.remove(2)
