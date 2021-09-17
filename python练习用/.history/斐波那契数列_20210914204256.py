def main():
    n = int(input('你想计算多少位的斐波那契数列？')) - 1
    a = [1, 1]
    if n <= 1:
        print('1')
    else:
        for i in range(1, n - 1):
            b = a[i] + a[i - 1]
            a.append(b)
    print(b)


main()
