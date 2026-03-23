import sys, os, bisect, heapq, math
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
sys.setrecursionlimit(10**6)
sys.set_int_max_str_digits(0) 
inf = 10**18
mod = 1000000007 

# https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/A

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
    n, k = get_ints()
    arr = get_list()
    queries = get_list()

    for q in queries:
        l, r = 0, n - 1
        found = False
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if arr[mid] == q:
                found = True
                break
            elif arr[mid] < q:
                l = mid + 1
            else:
                r = mid - 1
                
        if found:
            fast_print("YES")
        else:
            fast_print("NO")

if __name__ == '__main__':
    # multiple test cases
    # t = get_int()
    # for _ in range(t):
    #     solve()
    
    # single test case
    solve()