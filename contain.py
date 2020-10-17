t = int(input())
while t:
    t -= 1
    x = []
    y = []
    n, q = map(int, input().split())
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)

    for i in range(q):
        right = 0
        left = 0
        up = 0
        down = 0

        a, b = map(int, input().split())
        if n < 3:
            print(0)

        else:
            for j in range(n):
                if x[j] < a:
                    left += 1
                if x[j] > a:
                    right += 1
                if y[j] > b:
                    up += 1
                if y[j] < b:
                    down += 1

                if right>=1 and left>=1 and up>=1 and down>=1:
                    print(randint(1, 4))
                else:
                    print(0)
