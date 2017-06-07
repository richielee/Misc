#Given an integer n, return the list of prime numbers that are inferior to n
l = [2, 3]
def prime(n):
    for i in range(2,n):
        if (sum([i % d == 0 for d in l]) == 0):
            l.append(i)
    return (l)

print (prime(10000))
