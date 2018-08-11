def mean(a):
    return float(sum(a)) /len(a)

print "mean: ",mean([17,19,18,17,19])

def median(a):
    a1 = sorted(a)
    # print a1
    midindex = len(a)/2
    if len(a)%2==0:
        out = (a1[midindex] +a1[midindex-1] )/2
    else:
        out = a1[midindex]
    return out

print "median: ", median([7, 38, 4, 18.0, 23])

def mode(a):
    m=0
    for i in a:
        icount = a.count(i)
        if icount > m:
            mode=i
            m=icount
    return mode
c = [4,3,32,33,4,32,3,38,4.0]
print "mode: ",mode(c)

def variance(a=[]):
    # D(X) = E{[X - E(X)] ^ 2}
    # D(X) = E(X^2) - [E(X)]^2
    mu = mean(a)
    # return mean([(x-mu)**2 for x in a])
    return mean([x*x for x in a]) - mu*mu

def stddev(a):
    from math import sqrt
    return sqrt(variance(a))

data3=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]
print "variance: ",variance(data3)

a = [190,170,165,180,165]
b=[2400.0,125,148,160,110,325,180]
c = [4,3,32,33,4,32,3,38,4.0]
print b[0],mean(a) ,mean(b), mean(c)
print ":",mean([7,38,4,23,18.0])
