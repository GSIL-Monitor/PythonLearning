def f(p):
    return 1 - p


def g(p):
    return p * p


def pc(p0, p1, p2):
    return p1 * p0 + (1 - p0) * (1 - p2)


def p_c_pos(p0, p1, p2):
    # return p0 * p1 / pc(p0, p1, p2)  # or
    return p0 * p1 / ( p1 * p0 + (1 - p0) * (1 - p2) )


print pc(0.1, 0.9, 0.8)
print p_c_pos(0.1, 0.9, 0.8)
# print "1-p=",f(0.3),"\tp*p=",g(0.3)
