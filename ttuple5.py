import math


def ifDeno(a1, b1, c1, a2, b2, c2):

    if a2 == b2 == c2 != 0:
        return True

    if a2 == b2:
        if c1 == c2:
            return True
        if c2 == 0:
            return True
        if c1+a2 == c2:
            return True

    if b2 == c2:
        if a1 == a2:
            return True
        if a2 == 0:
            return True
        if a1+b2 == a2:
            return True

    if c2 == a2:
        if b1 == b2:
            return True
        if b2 == 0:
            return True
        if b1+a2 == b2:
            return True

    return False


def ifCombo(x, y, z, x2, y2, z2):
    if x+y == z or y+z == x or z+x == y:
        return True
    if x2 == math.ceil(x2) and y2 == math.ceil(y2) and z2 == math.ceil(z2):
        if x2*y2 == z2 or y2*z2 == x2 or z2*x2 == y2:
            return True

    return False


def ifTwo(a1, b1, c1, a2, b2, c2):

    ints = []
    try:
        if a2 != b2 and a1 != b1:
            if (a2-b2) % (a1-b1) == 0:
                x = (a2-b2)//(a1-b1)
                if a2-a1*x == b2-b1*x:
                    ints.append(x)
    except:
        n = 0

    try:
        if b2 != c2 and b1 != c1:
            if (b2-c2) % (b1-c1) == 0:
                x = (b2-c2)//(b1-c1)
                if b2-b1*x == c2-c1*x:
                    ints.append(x)
    except:
        n = 0

    try:
        if c2 != a2 and c1 != a1:
            if (c2-a2) % (c1-a1) == 0:
                x = (c2-a2)//(c1-a1)
                if c2-c1*x == a2-a1*x:
                    ints.append(x)
    except:
        n = 0

    if len(ints) == 3 and len(set(ints)) == 1:
        # print('yeah')
        return True
    if len(ints) == 3 and len(set(ints)) == 2:
        # print('yeah2')
        return True

    if len(ints) == 3 and len(set(ints)) == 3:
        # print('yeah3')

        try:
            x = (a2-b2)//(a1-b1)
            y = a2-a1*x
            xx = (a1*b2-a2*b1)//(a2-b2)
            yy = a2//(a1+xx)

            if (a1*b2-a2*b1) % (a2-b2) != 0:
                xx = 0.4857454
                yy = 0.294823
            if c1 == c2 or c1+y == c2 or c1*x == c2 or c1+xx == c2 or c1*yy == c2:
                return True
        except:
            n = 0

        try:
            x = (b2-c2)//(b1-c1)
            y = b2-b1*x
            xx = (b1*c2-b2*c1)//(b2-c2)
            yy = b2//(b1+xx)

            if (b1*c2-b2*c1) % (b2-c2) != 0:
                xx = 0.4857454
                yy = 0.294823
            if a1 == a2 or a1+y == a2 or a1*x == a2 or a1+xx == a2 or a1*yy == a2:
                return True
        except:
            n = 0

        try:
            x = (c2-a2)//(c1-a1)
            y = c2-c1*x
            xx = (c1*a2-c2*a1)//(c2-a2)
            yy = c2//(c1+xx)

            if (c1*a2-c2*a1) % (c2-a2) != 0:
                xx = 0.4857454
                yy = 0.294823
            if b1 == b2 or b1+y == b2 or b1*x == b2 or b1+xx == b2 or b1*yy == b2:
                return True
        except:
            n = 0

    if len(ints) == 2 and len(set(ints)) == 1:
        # print('yeah4')
        return True

    if (len(ints) == 2 and len(set(ints)) == 2) or len(ints) == 1:
        # print('yeah5')
        try:
            if a2 != b2 and a1 != b1:
                if (a2-b2) % (a1-b1) == 0:
                    x = (a2-b2)//(a1-b1)
                    if a2-a1*x == b2-b1*x:
                        y = a2-a1*x
                        xx = (a1*b2-a2*b1)//(a2-b2)
                        yy = a2//(a1+xx)

                        if (a1*b2-a2*b1) % (a2-b2) != 0:
                            xx = 0.4857454
                            yy = 0.294823
                        if c1 == c2 or c1+y == c2 or c1*x == c2 or c1+xx == c2 or c1*yy == c2:
                            return True
        except:
            n = 0

        try:
            if b2 != c2 and b1 != c1:

                if (b2-c2) % (b1-c1) == 0:
                    x = (b2-c2)//(b1-c1)
                    if b2-b1*x == c2-c1*x:
                        y = b2-b1*x
                        xx = (b1*c2-b2*c1)//(b2-c2)
                        yy = b2//(b1+xx)

                        if (b1*c2-b2*c1) % (b2-c2) != 0:
                            xx = 0.4857454
                            yy = 0.294823

                        # print(x,y,xx,yy)
                        if a1 == a2 or a1+y == a2 or a1*x == a2 or a1+xx == a2 or a1*yy == a2:

                            return True
        except:
            n = 0

        try:
            if c2 != a2 and c1 != a1:
                if (c2-a2) % (c1-a1) == 0:
                    x = (c2-a2)//(c1-a1)
                    if c2-c1*x == a2-a1*x:
                        y = c2-c1*x
                        xx = (c1*a2-c2*a1)//(c2-a2)
                        yy = c2//(c1+xx)

                        if (c1*a2-c2*a1) % (c2-a2) != 0:
                            xx = 0.4857454
                            yy = 0.294823
                        if b1 == b2 or b1+y == b2 or b1*x == b2 or b1+xx == b2 or b1*yy == b2:

                            return True
        except:
            n = 0

    return False


def ifGrid(a1, b1, c1, a2, b2, c2):
    l = [[None, None, None], [None, None, None]]
    l[0][0] = a2-a1
    l[0][1] = b2-b1
    l[0][2] = c2-c1

    try:
        if a2 % a1 == 0:
            l[1][0] = a2//a1
    except:
        n = 0

    try:
        if b2 % b1 == 0:
            l[1][1] = b2//b1
    except:
        n = 0

    try:
        if c2 % c1 == 0:
            l[1][2] = c2//c1
    except:
        n = 0

    if l[0][1] != None and l[1][2] != None:
        if (a1+l[0][1])*l[1][2] == a2 or l[0][1]+(a1*l[1][2]) == a2:
            return True

    if l[0][2] != None and l[1][1] != None:
        if (a1+l[0][2])*l[1][1] == a2 or l[0][2]+(a1*l[1][1]) == a2:
            return True

    if l[0][0] != None and l[1][2] != None:
        if (b1+l[0][0])*l[1][2] == b2 or l[0][0]+(b1*l[1][2]) == b2:
            return True

    if l[0][2] != None and l[1][0] != None:
        if (b1+l[0][2])*l[1][0] == b2 or l[0][2]+(b1*l[1][0]) == b2:
            return True

    if l[0][0] != None and l[1][1] != None:
        if (c1+l[0][0])*l[1][1] == c2 or l[0][0]+(c1*l[1][1]) == c2:
            return True

    if l[0][1] != None and l[1][0] != None:
        if (c1+l[0][1])*l[1][0] == c2 or l[0][1]+(c1*l[1][0]) == c2:
            return True

    return False


t = int(input())
while t:
    t -= 1
    a1, b1, c1 = map(int, input().split())
    a2, b2, c2 = map(int, input().split())

    ones = 0
    zeros = 0

    x = a2-a1
    y = b2-b1
    z = c2-c1

    try:
        if a2 % a1 == 0:
            x2 = a2//a1
        else:
            x2 = 8.12248952
    except:
        x2 = 8.12248952

    try:
        if b2 % b1 == 0:
            y2 = b2//b1
        else:
            y2 = 43.82248952
    except:
        y2 = 43.82248952

    try:
        if c2 % c1 == 0:
            z2 = c2//c1
        else:
            z2 = 3.81118952
    except:
        z2 = 3.81118952

    same = 0

    if a1 == a2:
        same += 1
    if b1 == b2:
        same += 1
    if c1 == c2:
        same += 1

    if same == 3:
        print(0)
    elif same == 2:
        print(1)
    elif same == 1 and (x == y or y == z or z == x):
        print(1)
    elif same == 1 and ((x2 == y2 and math.ceil(x2) == x2) or (y2 == z2 and math.ceil(y2) == y2) or (z2 == x2 and math.ceil(x2) == x2)):
        print(1)
    elif same == 0 and (x == y == z):
        print(1)
    elif same == 0 and (x2 == y2 == z2 and math.ceil(x2) == x2):
        print(1)

    elif a2 == b2 == c2 == 0:
        print(1)
    elif a2 == b2 == 0 and c1 == c2:
        print(1)
    elif b2 == c2 == 0 and a1 == a2:
        print(1)
    elif c2 == a2 == 0 and b1 == b2:
        print(1)

    elif ifTwo(a1, b1, c1, a2, b2, c2) or ifCombo(x, y, z, x2, y2, z2) or ifDeno(a1, b1, c1, a2, b2, c2) or ifGrid(a1, b1, c1, a2, b2, c2):
        print(2)

    elif same == 1 and a1 == a2 and y != z:
        print(2)
    elif same == 1 and b1 == b2 and x != z:
        print(2)
    elif same == 1 and c1 == c2 and x != y:
        print(2)
    elif same == 0 and (x == y or y == z or z == x):
        print(2)

    elif same == 1 and a1 == a2 and (y2 != z2 or math.ceil(y2) != y2):
        print(2)
    elif same == 1 and b1 == b2 and (x2 != z2 or math.ceil(x2) != x2):
        print(2)
    elif same == 1 and c1 == c2 and (x2 != y2 or math.ceil(x2) != x2):
        print(2)

    elif same == 0 and ((x2 == y2 and math.ceil(x2) == x2) or (y2 == z2 and math.ceil(y2) == y2) or (z2 == x2 and math.ceil(x2) == x2)):
        print(2)

    else:
        print(3)
