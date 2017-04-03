from __future__ import division

## define entropy calc as a function
import math
print "P_of_i values are 0.5 and 0.5"
P_of_i = [0.5,0.5]
i = 0
ent_i = 0
while i < len (P_of_i):
    ent_i = ent_i + (-(P_of_i[i]*math.log(P_of_i[i], 2)))
    i += 1

print "entropy of parent is: ", ent_i
import math
P_of_i = 0
P_of_i = []
P1 = 2/3
P_of_i.append(P1)
P2 = 1/3
P_of_i.append(P2)
i = 0
print "P_of_i values are: "
print P_of_i
ent_i = 0
while i < len (P_of_i):
    ent_i = ent_i + (-(P_of_i[i]*math.log(P_of_i[i], 2)))
    i += 1

print "entropy of child 1 is: ", ent_i
print "entropy of child 2 is: 0"

ent_children = ((3/4)*ent_i) + ((1/4)*0)
print "entropy of children is: "
print ent_children
info_gain = 1 - ent_children
print "information gain is:"
print info_gain


print "For bumpiness"
print "Entropy of bumpy is: 1"
print "Entropy of smooth is: 1"
P_of_i = 0
P_of_i =[0.5,0.5]
i = 0
print "P_of_i values are: "
print P_of_i
ent_i = 0
while i < len (P_of_i):
    ent_i = ent_i + (-(P_of_i[i]*math.log(P_of_i[i], 2)))
    i += 1
print "Entropy of bumpiness is: "
print ent_i
print "Entropy of children for bumpiness is: "
ent_children = (0.5*1) + (0.5*1)
print ent_children
print "info gain for bumpiness is: "
info_gain = 1 - ent_children
print info_gain


print "For speed limit"
P_of_i = 0
P_of_i =[1,1]
i = 0
print "P_of_i values are: "
print P_of_i
ent_i = 0
while i < len (P_of_i):
    ent_i = ent_i + (-(P_of_i[i]*math.log(P_of_i[i], 2)))
    i += 1
print "Entropy of speedlimit is: "
print ent_i
print "Entropy of slow is: 0"
ent_slow = 0
print "Entropy of fast is: 0"
ent_fast = 0
print "Weighted avg Entropy of children is: "
ent_children = (0.5*ent_slow) + (0.5*ent_fast)
print ent_children
print "info gain for speed is: "
info_gain = 1 - ent_children
print info_gain


