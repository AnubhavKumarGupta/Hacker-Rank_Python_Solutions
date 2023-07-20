if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst = set(arr) 
    a = sorted(lst)
    print(a[-2])
