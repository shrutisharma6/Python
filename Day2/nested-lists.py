if __name__ == '__main__':
    ls = []
    ans = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ls.append([name, score])
    ls = sorted(ls, key=lambda x: x[1])
    for i in ls:
        if i[1] > ls[0][1]:
            low = i[1]
            break
    # print(low)
    for i in ls:
        if i[1] == low:
            ans.append(i[0])
    ans.sort()
    for i in ans:
        print(i)


