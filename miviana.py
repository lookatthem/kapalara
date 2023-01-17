def func1(arg1, arg2):
    var47 = var5(arg1, arg2)
    var52 = func7(arg1, arg2)
    var53 = ((var52 | -265) | arg1) - ((((arg1 - var52 | -83532721 | 1144179774) & (-225805765 ^ var47)) + 160) | -828)
    result = arg1 & (arg1 - var53) ^ arg2
    return result
def func7(arg48, arg49):
    var50 = 0
    for var51 in xrange(3):
        var50 += arg49 ^ var51 | var50
    return var50
def func4(arg6, arg7):
    var12 = func5(arg7, arg6)
    var26 = func6(arg7, arg6)
    var27 = (208 + 7762431 ^ arg7) | arg6
    var28 = -644 & (arg7 & var26) & 1078851577
    var29 = var12 & -288 - var12 - var26
    var30 = var27 - var26 & (var26 ^ var26)
    var31 = (var26 & var27) + 371 + var30
    var32 = (var27 & var29) ^ arg6 ^ var29
    var33 = (var31 - 682) - (var32 & var29)
    var34 = (arg6 & arg7) & arg6 | var30
    var35 = var33 - ((var12 - var28) | var31)
    var36 = (var29 - -930 ^ var12) - var12
    var37 = (var31 ^ var34 & 422) ^ var31
    var38 = var30 - (var28 | var35)
    if var27 < arg7:
        var39 = arg6 & var26 ^ var36 & var35
    else:
        var39 = var34 | var31
    var40 = var35 | var27
    if var27 < var34:
        var41 = (var28 - var30 & var28) + var29
    else:
        var41 = (-217 | var29) + var30
    var42 = var38 + var35 ^ var34 + var26
    var43 = -128 & -875454364
    var44 = -186 | var12 ^ var43 | arg7
    var45 = var31 + (var37 & (var12 ^ -174))
    var46 = var36 ^ var33
    result = (var45 + var27 ^ (var40 ^ (-407 + (arg6 + (var42 | var38))) + 141 ^ var45)) & (var37 | var30 & var44)
    return result
def func6(arg13, arg14):
    if arg13 < arg14:
        var15 = (-474958360 | arg13 + arg14) | arg13
    else:
        var15 = 2072924097 & arg13
    var16 = -392 & (arg13 + 650) - arg13
    if arg14 < arg13:
        var17 = -233682275 ^ ((475 - -1304482141) + arg13)
    else:
        var17 = arg14 - arg14
    var18 = arg13 | var16 | arg14
    var19 = 233 | arg13
    var20 = var18 ^ var16 & -1054316672 & var19
    var21 = var18 | arg13 ^ -855994220 | var18
    var22 = 1895035990 ^ arg13
    var23 = ((arg13 - -434) | arg13) ^ var16
    var24 = var22 + (var21 ^ (var21 + var23))
    var25 = var19 + arg13
    result = var22 - var22
    return result
def func5(arg8, arg9):
    var10 = 0
    for var11 in (arg8 - arg9 ^ -9 for i in range(46)):
        var10 += var11 - var11
    return var10
def func3():
    closure = [-1]
    def func2(arg3, arg4):
        closure[0] += func4(arg3, arg4)
        return closure[0]
    func = func2
    return func
var5 = func3()
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 8'
    print 'arg_number: 54'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
