if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))# .split divide uma string em uma lista
    # map mapeia os valores como inteiros(int) dentro da lista
    result = list(set(arr)) #set remove valores duplicados
    result.remove(max(result)) #remove o maior valor
    print(f"{max(result)}")
