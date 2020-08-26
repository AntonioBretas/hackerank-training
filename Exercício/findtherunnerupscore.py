if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = list(set(arr)) #set remove valores duplicados
    result.remove(max(result)) #remove o maior valor
    print(f"{max(result)}")
