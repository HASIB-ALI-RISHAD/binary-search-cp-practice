import sys, os, bisect, heapq, math
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
sys.setrecursionlimit(10**6)
sys.set_int_max_str_digits(0) 
inf = 10**18
mod = 1000000007 

# https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/D

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
    arr = get_list()
    arr.sort()
    k = get_int()
    ans = []
    for i in range(k):
        l,r = get_ints()
        idx_r = bisect.bisect_right(arr,r)
        idx_l = bisect.bisect_left(arr,l)
        ans.append(idx_r - idx_l)

    print_list(ans)



 


if __name__ == '__main__':
    # multiple test cases
    # t = get_int()
    # for _ in range(t):
    #     solve()
    
    # single test case
    solve()