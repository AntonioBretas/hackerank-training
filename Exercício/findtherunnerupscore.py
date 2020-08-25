if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maxi = max(arr)
for i in range(len(arr)):
    if maxi in arr:
        arr.remove(maxi)
print(max(arr))
