# A set is a collection of unoredered and unindexed items. In Python, sets are written with curly brackets.
# sets are very useful we do a mathimatical calculations like union, intersection and differences
# why do we use sets? automatically remove duplicates from a list, check for membership, and perform mathematical operations like union, intersection, and difference.
# to perfrom operations like finding the common values between two lists, we can use sets. Sets are also useful for removing duplicates from a list and checking for membership.
# exmaple:
course = {'AI', 'Maths','CS','AI'}
print(course)
# another example:
set1 = {1,2,3,6,7,8,88}
set2 = {3,4,5,6,7,8,99}
print(set1 | set2) # for union
print(set1 & set2)
print(set1 - set2)