def problem1(n):
    if n == 0:
        return 0 
    return n + problem1(n-1)
# print(problem1(4))

# 584321
# 1
# 2
# 3
# 4

def problem2(n,total=0):
    if n//10 == 0:
        total += n
        return total 
    total+= n%10
    n=n//10
    return problem2(n,total)
print(problem2(584321))
