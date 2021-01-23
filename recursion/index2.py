# RECURSIVE REVERSE STRING
import itertools
def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]
# print(reverse('12345'))

# PERMUTATION OF STRING 
# 
def perm(s):
    ans = itertools.permutations(s,len(s))
    return ans
ans = perm('abc')
for i in ans:
    print(i)
# print(perm('abc'))





