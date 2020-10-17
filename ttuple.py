import math
t = int(input())
while t:
    t -= 1
    a, b, c = map(int, input().split())
    d, e, f = map(int, input().split())

    x = d-a
    y = e-b
    z = f-c

    ad = 5
    m = 5
    cs = 5

    if x == y and y == z and z == x and x == 0:
        ad = 0
    elif x == y and y == z and z == x and x != 0:
        ad = 1
    elif x == y or y == z or z == x:
        if x == y == 0:
            ad = 1
        elif y == z == 0:
            ad = 1
        elif z == x == 0:
            ad = 1

        elif x == y and y != 0:
            if z == 0:
                ad = 1
            else:
                ad = 2

        elif y == z and z != 0:
            if x == 0:
                ad = 1
            else:
                ad = 2

        elif z == x and x != 0:
            if y == 0:
                ad = 1
            else:
                ad = 2

    if x != y and y != z and z != x:
        if x == 0 or y == 0 or z == 0:
            ad = 2
        else:
            ad = 3

    validCount = 0

    if a != 0 and b != 0 and c != 0:
        if d % a == 0 or abs(d) < abs(a):
            validCount += 1
            x = d//a

        if e % b == 0 or abs(e) < abs(b):
            validCount += 1
            y = e//b

        if f % c == 0 or abs(f) < abs(c):
            validCount += 1
            z = f//c

    if validCount == 3:
        if x == y and y == z and z == x and x == 1:
            m = 0
        elif x == y == 0 or y == z == 0 or z == x == 0:
            m = 5
        elif x == y and y == z and z == x and x != 1:
            m = 1
        elif x == y or y == z or z == x:
            if x == y == 1:
                m = 1
            elif y == z == 1:
                m = 1
            elif z == x == 1:
                m = 1

            elif x == y and y != 1:
                if z == 1:
                    m = 1
                else:
                    m = 2

            elif y == z and z != 1:
                if x == 1:
                    m = 1
                else:
                    m = 2

            elif z == x and x != 1:
                if y == 1:
                    m = 1
                else:
                    m = 2

        if x != y and y != z and z != x:
            if x == 1 or y == 1 or z == 1:
                m = 2
            else:
                m = 3

    if validCount == 2:
        try:
            x = d//a
            y = e//b

            if x == y and y == 1:
                m = 1
            elif x == y and y != 1:
                m = 2
            elif x != y:
                m = 3
        except:
            none = 0

        try:

            y = e//b
            z = f//c

            if y == z and y == 1:
                m = 1
            elif y == z and y != 1:
                m = 2
            elif y != z:
                m = 3
        except:
            none = 0

        try:
            x = d//a
            z = f//c

            if x == z and z == 1:
                m = 1
            elif x == z and z != 1:
                m = 2
            elif x != z:
                m = 3
        except:
            none = 0

    if d == e and e == f and f == d and d == 0:
        cs = 1
    elif d == e and e == f and f == d and d != 0:
        cs = 2
    elif d == e == 0 or e == f == 0 or f == d == 0:
        if (a == d and d != e and d != f) or (b == e and e != d and e != f) or (c == f and f != e and d != f):
            cs = 1
        else:
            cs = 2
    elif d == e != 0 or e == f != 0 or f == d != 0:
        if d == e and (f == c or f == 0):
            cs = 2
        elif e == f and (d == a or d == 0):
            cs = 2
        elif f == d and (e == b or e == 0):
            cs = 2
        else:
            cs = 3
    ds = 3
    ints = []

    if (d-e) != 0 and a != b:
        if (a*e-b*d) % (d-e) == 0:
            x = ((a*e-b*d)//(d-e))
            if (a+x) != 0:
                if math.floor(d/(a+x)) == d/(a+x):
                    ints.append(x)
    if (e-f) != 0 and b != c:
        if (b*f-e*c) % (e-f) == 0:
            x = ((b*f-e*c)//(e-f))
            if (b+x) != 0:
                if math.floor(e/(b+x)) == e/(b+x):
                    ints.append(x)
    if (f-d) != 0 and a != c:
        if (c*d-a*f) % (f-d) == 0:
            x = ((c*d-a*f)//(f-d))
            if (c+x) != 0:
                if math.floor(f/(c+x)) == f/(c+x):
                    ints.append(x)

    # print(ints)

    if len(ints) == 1:
        if (d-e) != 0 and a != b:
            x = ((a*e-b*d)//(d-e))
            if (a+x) != 0 and c != 0:
                if math.floor(d/(a+x)) == d/(a+x):
                    if c == f or (f % c == 0 and f//c == d//(x+a)):
                        ds = 2

        if (e-f) != 0 and b != c:
            x = ((b*f-e*c)//(e-f))
            if (b+x) != 0 and a != 0:
                if math.floor(e/(b+x)) == e/(b+x):
                    if a == d or (d % a == 0 and d//a == e//(x+b)):
                        ds = 2

        if (f-d) != 0 and a != c:
            x = ((c*d-a*f)//(f-d))
            if (c+x) != 0 and b != 0:
                if math.floor(f/(c+x)) == f/(c+x) and (x+a) != 0:
                    if b == e or (e % b == 0 and e//b == d//(x+a)):
                        ds = 2

    elif len(ints) == 3 and len(set(ints)) == 1:
        ds = 2

    elif len(ints) == 3 and len(set(ints)) == 2:
        ds = 2
    elif len(ints) == 2 and len(set(ints)) == 1:
        ds = 2
    elif len(ints) == 2 and len(set(ints)) == 2:
        personalFlag = 0

        if (d-e) != 0 and (e-f) != 0 and a != b and b != c:
            if (a*e-b*d) % (d-e) == 0 and (b*f-e*c) % (e-f) == 0:
                x1 = ((a*e-b*d)//(d-e))
                x2 = ((b*f-e*c)//(e-f))

                if (a+x1) != 0 and (b+x2) and c != 0:
                    if math.floor(d/(a+x1)) == d/(a+x1) and math.floor(e/(b+x2)) == e/(b+x2):
                        if x1 == x2:
                            if c == f or (f % c == 0 and f//c == d//(x1+a)):
                                personalFlag = 1

        if (e-f) != 0 and (f-d) != 0 and b != c and a != c:
            if (b*f-e*c) % (e-f) == 0 and (c*d-a*f) % (f-d) == 0:
                x1 = ((b*f-e*c)//(e-f))
                x2 = ((c*d-a*f)//(f-d))

                if (b+x1) != 0 and (c+x2) != 0 and a != 0:
                    if math.floor(e/(b+x1)) == e/(b+x1) and math.floor(f/(c+x2)) == f/(c+x2):
                        if x1 == x2:
                            if a == d or (d % a == 0 and d//a == e//(x1+b)):
                                personalFlag = 1

        if (f-d) != 0 and (d-e) != 0 and a != c and a != b:
            if (c*d-a*f) % (f-d) == 0 and (a*e-b*d) % (d-e) == 0:
                x1 = ((c*d-a*f)//(f-d))
                x2 = ((a*e-b*d)//(d-e))

                if (c+x1) != 0 and (a+x2) != 0 and b != 0 and (x1+a) != 0:
                    if math.floor(f/(c+x1)) == f/(c+x1) and math.floor(d/(a+x2)) == d/(a+x2):
                        if x1 == x2:
                            if b == e or (e % b == 0 and e//b == d//(x1+a)):
                                personalFlag = 1

        if personalFlag:
            ds = 2
        else:
            ds = 3

    print(min(ad, m, cs, ds))
