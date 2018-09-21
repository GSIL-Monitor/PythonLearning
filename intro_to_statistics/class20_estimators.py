#In class you wrote a function mean that computed the mean of a set of numbers
#Consider a case where you have already computed the mean of a set of data and
#get a single additional number. Given the number of observations in the
#existing data, the old mean and the new value, complete the function to return
#the correct mean

from __future__ import division

def mean(oldmean,n,x):
    #Insert your code here
    return (oldmean*n+x)/(n+1)

currentmean=10
currentcount=5
new=4

print(mean(currentmean, currentcount, new))  # Should print 9


def mean(age,freq):
    return sum([ a*b for (a,b) in zip(age,freq) ])/sum(freq)
    
age=range(19 ,25)
freq=[2,1,1,3,2,1,1]

print(mean(age, freq))


def likelihood(dist,data):
    #Insert your answer here
    l=1
    for i in data:
        l*=dist[i]
    return l

tests= [(({'A':0.2,'B':0.2,'C':0.2,'D':0.2,'E':0.2},'ABCEDDECAB'), 1.024e-07),
        (({'Good':0.6,'Bad':0.2,'Indifferent':0.2},['Good','Bad','Indifferent','Good','Good','Bad']), 0.001728),
        (({'Z':0.6,'X':0.333,'Y':0.067},'ZXYYZXYXYZY'), 1.07686302456e-08),
        (({'Z':0.6,'X':0.233,'Y':0.067,'W':0.1},'WXYZYZZZZW'), 8.133206112e-07)]

for t,l in tests:
    print(t)
    print(l)
    if abs(likelihood(*t)/l-1)<0.01:
        print('Correct')
    else:
        print('Incorrect')
