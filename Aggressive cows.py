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

# https://www.spoj.com/problems/AGGRCOW/

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

    n , c = get_ints()
    positions = []
    for i in range(n):
        positions.append(get_int())

    def predicate(mid):
        count = 1
        last_position = positions[0]

        for i in range(1, n):
            if positions[i] - last_position >= mid:
                count += 1
                last_position = positions[i]

            if count >= c:
                return True

        return False
    
    positions.sort()
    low, high = 1, positions[-1] - positions[0]
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if predicate(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    fast_print(ans)



if __name__ == '__main__':
    # multiple test cases
    t = get_int()
    for _ in range(t):
        solve()