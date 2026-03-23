import sys, os, bisect, heapq, math
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
sys.setrecursionlimit(10**6)
sys.set_int_max_str_digits(0) 
inf = 10**18
mod = 1000000007 

# https://www.spoj.com/problems/MATHLOVE/

if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')


def get_int(): 
    return int(sys.stdin.readline())

def get_ints(): 
    return map(int, sys.stdin.readline().split())

def get_list(): 
    return list(map(int, sys.stdin.readline().split()))

def get_string(): 
    return sys.stdin.readline().rstrip()

def get_words(): 
    return sys.stdin.readline().split()

def fast_print(ans):
    sys.stdout.write(str(ans) + '\n')

def print_list(arr):
    sys.stdout.write(" ".join(map(str, arr)) + '\n')

def solve():
    n = get_int()

    for i in range(n):
        y = get_int()
        l= 1
        r =  100000

        # Optimized Upper Bound Calculation:
        # Sum formula: Y = n*(n+1)/2
        # Max Y = 3 * 10^9
        # 3 * 10^9 = n*(n+1)/2  =>  6 * 10^9 = n^2 + n
        # n approx sqrt(6 * 10^9) approx 77,459
        # Therefore, n will never exceed 100,000.
        # Setting r = 100,000 reduces binary search steps from ~32 to ~17.
    
        ans = 0
        
        # def predicate(mid):
        #     mid_n = mid * (mid + 1) // 2
        #     return mid_n >= y
        # using this predicate causes TLE, so we will calculate the sum of first mid natural numbers in the main loop itself to avoid redundant calculations

        while l<=r:
            mid = l + (r - l) // 2

            # if predicate(mid):
            if mid * (mid + 1) // 2 >= y:
                ans = mid
                r = mid -1
            else:
                l = mid+1

        ans_sum = ans * (ans + 1) // 2
        if ans_sum == y:
            fast_print(ans) 
        else:
            fast_print("NAI")




if __name__ == '__main__':
    # multiple test cases
    # t = get_int()
    # for _ in range(t):
    #     solve()
    
    # single test case
    solve()