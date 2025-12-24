# Union:
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using the union() method
union_set = set1.union(set2)
print(f"Union using method: {union_set}")

# Using the | operator
union_set_op = set1 | set2
print(f"Union using operator: {union_set_op}")

#  Intersection:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using the intersection() method
intersection_set = set1.intersection(set2)
print(f"Intersection using method: {intersection_set}")

# Using the & operator
intersection_set_op = set1 & set2
print(f"Intersection using operator: {intersection_set_op}")

# Difference
set11 = {1, 2, 3, 4}
set21 = {3, 4, 5, 6}

# Using the difference() method
difference_set = set11.difference(set21)
print(f"Difference using method: {difference_set}")

# Using the - operator
difference_set_op = set1 - set2
print(f"Difference using operator: {difference_set_op}")


# Symmetric Difference:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using the symmetric_difference() method
sym_diff_set = set1.symmetric_difference(set2)
print(f"Symmetric difference using method: {sym_diff_set}")

# Using the ^ operator
sym_diff_set_op = set1 ^ set2
print(f"Symmetric difference using operator: {sym_diff_set_op}")

# Update Methods:
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_a.update(set_b) # equivalent to set_a |= set_b
print(f"Set A after update: {set_a}")

set_c = {1, 2, 3, 4}
set_d = {3, 4, 5, 6}
set_c.intersection_update(set_d) # equivalent to set_c &= set_d
print(f"Set C after intersection_update: {set_c}")

# Output
# Union using method: {1, 2, 3, 4, 5}
# Union using operator: {1, 2, 3, 4, 5}
# Intersection using method: {3, 4}
# Intersection using operator: {3, 4}
# Difference using method: {1, 2}
# Difference using operator: {1, 2}
# Symmetric difference using method: {1, 2, 5, 6}
# Symmetric difference using operator: {1, 2, 5, 6}
# Set A after update: {1, 2, 3, 4, 5}
# Set C after intersection_update: {3, 4}