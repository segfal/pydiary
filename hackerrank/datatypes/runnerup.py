if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    x = max(list(arr))
    u = float('-inf')
    for i in arr:
        if i != x:
            u = max(i,u)
    print(u)
    
