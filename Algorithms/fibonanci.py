import click
from ...my_package.most_used_methods import check_time_spent


# fibonanci is a recursive function that returns the nth fibonanci number
# it refer to the population if rabbits in a rabbit farm 
# the first two rabbits are born with 1 pair of offspring each,
# the third rabbit is born with 2 pairs of offspring each,
# the fourth rabbit is born with 3 pairs of offspring each,
# and so on.
# the nth rabbit is born with n pairs of offspring each.
# the first rabbit is always 1
# the second rabbit is always 2, was small and fast

def fibonanci(n):
    if n <= 1:
        return n
    return fibonanci(n-1) + fibonanci(n-2)
# the running time T(n) is 2 for n <= 1  
# T(n) is 3 + T(n-1) + T(n-2) for n > 1
# T(n) denotes the number of recursive calls, number of spaces in memory
# the running time(complexity) is O(2^n)
# the problem is that the running time is exponential as a binary tree is created

# it repeats the recursion for all numbers > 1 multitimes from scratch
# which means that the tree of any number can be repeated
# e.g F(n-3) is repeated 3 times
# the complexity of F(100) is 1.77x10^21

# to customize the problem of repeating the trees
def fibonanci_customed(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonanci_customed(n-1, memo) + fibonanci_customed(n-2, memo)
    return memo[n]
# the running time is O(2n)


# the best algorithm is list the numbers in the fibonanci sequence
# the complexity is O(n)
def fibonanci_list(n):
    fib = [1,1,1]
    for i in range(3,n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]
# the T(n) is 2n+2 for n > 1


def main(n):
    print(fibonanci_customed(n))
    print(fibonanci_list(n))
    print(fibonanci(n))

if __name__ == '__main__':
    n = click.prompt('Enter the number of fibonanci: ', type=int)
    main(int(n))