## Given a 32-bit signed integer, reverse digits of an integer.


def reverse(x):
    res=0
    if x>0:
        res= int(str(x)[::-1])
    else:
        x=-x
        res= -int(str(x)[::-1])

    if res >= 2**31-1 or res <= -2**31:
        return 0
    else:
        return res
