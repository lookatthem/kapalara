def func1(arg1, arg2):
    var7 = func2(arg1, arg2)
    var35 = func3(arg1, var7)
    def func7(arg36, arg37):
        var38 = ((arg36 | arg37) ^ arg1) & var7
        var39 = arg37 | var35 ^ (var35 - var7)
        var40 = ((819 | arg37) + 123) ^ var35
        var41 = (var40 | arg2) | var38 & arg1
        var42 = 693 | ((var39 | var40) | 644305208)
        var43 = (arg2 - (arg37 - arg37)) & -670
        var44 = var39 | var43 + arg36 - var38
        var45 = arg1 + var40 - var40 - var40
        var46 = (541 + arg1 + arg2) + var40
        var47 = arg2 | var46 & arg37 - arg2
        if var40 < arg2:
            var48 = var38 & (var45 | arg1 + var42)
        else:
            var48 = var7 & 927369247
        if var47 < var47:
            var49 = var38 ^ var43
        else:
            var49 = (arg37 | var42 & var43) & arg37
        var50 = arg1 - var46
        var51 = var40 - var47
        var52 = var46 - arg37
        var53 = var7 & var46
        if var45 < var43:
            var54 = (var51 | var42 ^ var45) & var35
        else:
            var54 = var50 - (arg1 & var50 ^ var38)
        var55 = var35 + var47
        var56 = -681 + arg36
        var57 = (var56 - (var40 + -207)) ^ var38
        var58 = 2104477049 - var46 ^ var47 | -123
        var59 = var58 - var55 & var43 & arg2
        var60 = var41 ^ ((var38 & var39) - var38)
        var61 = var52 | var41
        var62 = ((var40 ^ arg1) | var42) ^ var57
        result = var57 & ((var42 - (var55 | var56 + var61)) - var57)
        return result
    var63 = func7(arg2, var35)
    var64 = 1770890008 & arg2
    var65 = ((arg1 | var7 ^ (var35 - var63 + var35) & (var64 - -721)) + (var64 - arg1) | var64 | var64) + (((-1606335089 + var7) ^ (var64 & -487 & -525 - -945 & var35)) + arg1 + 1008122343 | 513) ^ var35
    result = (var65 ^ (var64 - (arg2 - arg2 & 2128974720 & arg2 + var64 - var65 - var35 + -1307326472))) ^ -923
    return result
def func3(arg8, arg9):
    var10 = 0
    for var34 in func4(var10, arg9):
        var10 += var34 & (arg8 | var34)
    return var10
def func5(arg13, arg14):
    var19 = func6(arg14, arg13)
    var20 = 662342125 ^ (arg13 & 1201919343 ^ arg13)
    var21 = (310 | var19) | ((arg14 | ((arg14 + -518813975) | 816673104 + var19 - var19) - 1871255580 | 706 - (arg14 - -21209976 | arg13 - 702479096) | ((618 + var20) & var19) - var19 | var19 ^ arg13) + -620 | var20)
    var22 = var19 | (var21 | 260) & var21
    result = 1832550557 ^ 628546547
    return result
def func6(arg15, arg16):
    if arg15 < arg15:
        var17 = (arg15 | (1395844157 ^ (arg16 - ((arg15 ^ arg16 ^ -567610636) ^ 515) | arg16))) + arg16 | ((arg15 + 432) | -24 & 238) & (arg15 ^ (arg15 ^ (arg16 + (arg16 - arg16) | 397) & -699 ^ 168 - arg16))
    else:
        var17 = (arg15 ^ arg15 - ((318 & ((126 & 1896520004 | arg15 & arg15 + arg16 & arg16 ^ ((arg16 - arg16 - -325223938) - arg16)) - arg15)) & -244204620)) & (1751730144 & (162 ^ arg16) - 1227294945)
    var18 = arg16 & arg15 | -427 & arg16
    result = (((-26 & arg16) + -199744423) ^ -653 & arg15 & var18 & (var18 + arg15 ^ -1435007048) - var18 - arg15) - arg16
    return result
def func4(arg11, arg12):
    var23 = func5(-1567609172, arg11)
    yield var23
    var24 = -888 - 48158165
    yield var24
    var25 = (372 + arg11 & arg11) ^ -714
    yield var25
    var26 = arg12 ^ -738 | var24 - var25
    yield var26
    var27 = arg12 - (arg12 & var26) - var25
    yield var27
    var28 = var25 & -74230987
    yield var28
    var29 = arg11 | -628
    yield var29
    var30 = var26 | ((var27 + arg12) & arg12)
    yield var30
    var31 = var27 | 766715015
    yield var31
    var32 = arg11 ^ arg11 + -1696828921 + var24
    yield var32
    var33 = var30 & -781304487
    yield var33
def func2(arg3, arg4):
    var5 = 0
    for var6 in range(31):
        var5 += var5 ^ var6 | arg4
    return var5
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 8'
    print 'arg_number: 66'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
