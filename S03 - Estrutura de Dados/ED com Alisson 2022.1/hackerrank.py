# Plus Minus

def plusMinus(arr):
    
    contP = 0
    contN = 0
    contZ = 0
    
    for valor in arr:
        if valor > 0:
            contP +=1
        elif valor < 0:
            contN += 1
        else:
            contZ +=1
    tamanho = len(arr)
    print("%.6f" % (contP/tamanho))
    print("%.6f" % (contN/tamanho))
    print("%.6f" % (contZ/tamanho))

# Mini-Max Sum

def miniMaxSum(arr):
    print(sum(arr) - max(arr),sum(arr) - min(arr) ) 

# Time Conversion

def timeConversion(s):
    m = s[-2:]
    if m == 'PM' and s[:2] != '12':
        s = str(12 + int(s[:2])) + s[2:]
    if m == 'AM' and s[:2] == '12':
        s = '00' + s[2:]
    return s[:-2]

# Lonely Integer

def lonelyinteger(a):
    return list(filter(lambda x: a.count(x) == 1, a))[0]

# Diagonal Difference    

def diagonalDifference(arr):
    somaDP = 0
    somaDS = 0
    
    for i in range(len(arr)):
        
        somaDP += arr[i][i]
        somaDS += arr[i][len(arr) - 1 - i]
    
    return abs(somaDP - somaDS)

# Counting Sort 1

def countingSort(arr):
    
    count = [0]*100
    for j in arr:
        count[j] += 1
    return count

# Zig Zag Sequence

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) - 1
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)

# Tower Breakers

def towerBreakers(n, m):
    if m == 1:
        return 2
    else:
        return 1 if n%2 == 1 else 2

# Caesar Cipher

def caesarCipher(s, k):
    temp = []
    
    for char in s:
        temp.append(ord(char))
        
    for i in range(n):
        if 65 <= temp[i] <= 90:
            temp[i] = (65 + (temp[i] - 65 + k) %26)
        elif 97 <= temp[i] <= 122:
            temp[i] = (97 + (temp[i] - 97 + k) %26)
    return "".join(map(chr, temp))

# Grid Challenge

def gridChallenge(grid):
    grid = [list(row) for row in grid]
    r = len(grid)
    c = len(grid[0])
    
    for i in range(r):
        grid[i].sort()
    
    for j in range(c):
        for i in range(1, r):
            if not grid[i-1][j] <= grid[i][j]:
                return "NO"
    return "YES"

# Recursive Digit Sum

def superDigit(n, k):
    def sum_digit(v):
        if v < 10:
            return v
        s = sum(int(i) for i in str(v))
        return sum_digit(s)
    x = sum_digit(int(n))
    return sum_digit(x * k)

# New Year Chaos

def minimumBribes(q):
    
    q = [i-1 for i in q]
    bribes = 0
    
    for i, o in enumerate(q):
        cur = i 
        if o - cur > 2:
            print("Too chaotic")
            return
        for k in q[max(o - 1, 0):i]:
            if k > o:
                bribes += 1

    print(bribes)

# Merge two sorted linked lists

import sys
sys.setrecursionlimit(100000)

def mergeLists(head1, head2):
    if head1 == None and head2 == None:
        return None
    
    if head1 == None: 
        return head2
    
    if head2 == None:
        return head1
    
    if head1.data < head2.data:
        temp = head1
        temp.next = mergeLists(head1.next, head2)
    else:
        temp = head2
        temp.next = mergeLists(head1, head2.next)
        
    return temp

# Queue using Two Stacks

x = int(input())
stackP = []
stackD = []

for i in range(x):
    y = list(input().split())
    if y[0] == '1':
        stackP.append(y[1])
        
    elif y[0] == '2':
        if not stackD:
            while stackP:
                stackD.append(stackP.pop())
        stackD.pop()
    else:
        if not stackD:
            while stackP:
                stackD.append(stackP.pop())
        print(stackD[-1])

# Balanced Brackets

def isBalanced(s):
    stack = []
    bracker = {
        '{' : '}',
        '(' : ')',
        '[' : ']'
    }
    
    for char in s:
        if char in ['{', '(', '[']:
            stack.append(char)
        else:
            if stack:
                top = stack.pop()
                if bracker[top] != char:
                    return "NO"
            else:
                return "NO"
    return "NO" if stack else "YES"

# Simple Text Editor

stack = []
string = ""

for _ in range(int(input())):
    x = input().split()
    
    if x[0] == '1':
        stack.append(string)
        string += x[1]
        
    elif x[0] == '2':
        stack.append(string)
        string = string[:-int(x[1])]
        
    elif x[0] == '3':
        print(string[int(x[1])-1])
        
    else:
        string = stack.pop()

# Lego Blocks

def tetranacci(n): 
    arr = [1, 2, 4, 8]
    if n <= 4: 
        return arr[:n]
    else: 
        for i in range(4, n):
            arr.append(sum(arr[i-4:i])%(10**9 + 7))
    return arr

def legoBlocks(n, m):
    MOD = (10**9 +7)
    a, s = [(v**n)%MOD for v in tetranacci(m)], [1]

    for i in range(1, len(a)):
        sums = sum([x*y for x,y in zip(a[:i], s[::-1])])
        s.append( (a[i]-sums)%MOD)
    return s[-1]

# Jesse and Cookies

from heapq import heapify, heappop, heappush

def cookies(k, A):
    result = 0
    heapify(A)
    
    while True:
        x = heappop(A)
        
        if x >= k:
            return result
        if A:
            y = heappop(A)
            z = x + 2 * y
            heappush(A, z)
            result += 1
        else:
            return -1

# Tree: Preorder Traversal

def preOrder(root):
    
    if root is None:
        return
    
    print(root.info, end = ' ')
    
    preOrder(root.left)
    preOrder(root.right)

# Tree: Huffman Decoding

def decodeHuff(root, s):

    temp = root
    result = []
    
    for char in s:
        if char is '0':
            temp = temp.left
        else:
            temp = temp.right
        if temp.left is None and temp.right is None:
            result.append(temp.data)
            temp = root
    
    print("".join(result))
