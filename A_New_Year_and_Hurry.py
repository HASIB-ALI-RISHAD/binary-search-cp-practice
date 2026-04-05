import sys, os, gc, bisect, heapq, math
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
sys.setrecursionlimit(10**6)
inf = 10**18
mod = 1000000007 
try:
    sys.set_int_max_str_digits(0) 
except AttributeError:
    pass


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


# https://codeforces.com/problemset/problem/750/A

def solve():
    n , k = get_ints()

    l = 0
    r = n
    ans = 0

    def predicate(mid):

        check = 0
        for i in range(1,mid+1):
            check += i * 5
        return check + k <= 240 
        
    while l<=r:

        mid = l + (r-l)//2

        if predicate(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    fast_print(ans)
        


if __name__ == '__main__':
    # multiple test cases
    # t = get_int()
    # for _ in range(t):
    #      solve()
    #      gc.collect()
    
    # single test case
    solve()