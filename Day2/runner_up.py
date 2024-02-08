if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    ls = arr
    winner = max(arr)
    runner_up = -100
    for i in ls:
        if runner_up < i and i != winner:
            runner_up = i
    print(runner_up)
