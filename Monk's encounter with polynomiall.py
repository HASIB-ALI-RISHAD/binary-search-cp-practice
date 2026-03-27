import sys, os, bisect, heapq, math
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations
sys.setrecursionlimit(10**6)
sys.set_int_max_str_digits(0) 
inf = 10**18
mod = 1000000007 

if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

#https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/monks-encounter-with-polynomial/?purpose=login&source=problem-page&update=github

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
    a , b , c , k = get_ints()

    def predicate(mid):
        return a * mid * mid + b * mid + c >= k
    
    l = 0
    r = 10000000000
    ans = 0
    while l<=r:
        mid = (l+r)//2
        if predicate(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    fast_print(ans)

if __name__ == '__main__':
    # multiple test cases
    t = get_int()
    for _ in range(t):
        solve()
