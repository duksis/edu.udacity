#!/usr/bin/env python

# # Question 11
# #Modify the program to find and print the sum of all
# #the entries in the list p.
#
# p=[0.2, 0.2, 0.2, 0.2, 0.2]
# pHit = 0.6
# pMiss = 0.2
#
# for i in range(0,len(p)):
#   if [1,2].count(i) > 0:
#     p[i] = p[i]*pHit
#   else:
#     p[i] = p[i]*pMiss
#
# print sum(p)

# # # Question 13
# #Modify the code below so that the function sense, which
# #takes p and Z as inputs, will output the NON-normalized
# #probability distribution, q, after multiplying the entries
# #in p by pHit or pMiss according to the color in the
# #corresponding cell in world.
#
# p=[0.2, 0.2, 0.2, 0.2, 0.2]
# world=['green', 'red', 'red', 'green', 'green']
# Z = 'red'
# pHit = 0.6
# pMiss = 0.2
#
# def sense(p, Z):
#   q=[]
#   for i in range(0,len(p)):
#     if world[i] == Z:
#       q.append(p[i]*pHit)
#     else:
#       q.append(p[i]*pMiss)
#
#   s = sum(q)
#   for i in q:
#     i = i / s
#
#   return q
#
# print sense(p,Z)

# # Question 15
# #and gives the posterior distribution after both
# #measurements are incorporated. Make sure that your code
# #allows for any sequence of measurement of any length.
#
# p=[0.2, 0.2, 0.2, 0.2, 0.2]
# world=['green', 'red', 'red', 'green', 'green']
# measurements = ['red', 'green']
# pHit = 0.6
# pMiss = 0.2
#
# def sense(p, Z):
#     q=[]
#     for i in range(len(p)):
#         hit = (Z == world[i])
#         q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
#     s = sum(q)
#     for i in range(len(q)):
#         q[i] = q[i] / s
#     return q
#
# for m in measurements:
#   p = sense(p,m)
#
# print p


# # Question 17
# #Program a function that returns a new distribution
# #q, shifted to the right by U units. If U=0, q should
# #be the same as p.
#
# p=[0, 1, 0, 0, 0]
# world=['green', 'red', 'red', 'green', 'green']
# measurements = ['red', 'green']
# pHit = 0.6
# pMiss = 0.2
#
# def sense(p, Z):
#   q=[]
#   for i in range(len(p)):
#       hit = (Z == world[i])
#       q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
#   s = sum(q)
#   for i in range(len(q)):
#       q[i] = q[i] / s
#   return q
#
# def move(p, U):
#   q=[]
#   for i in range(0,len(p)):
#     q.append(p[(i-U) % len(p)])
#   return q
#
# print move(p, 1)

# # Question 21
# #Modify the move function to accommodate the added
# #probabilities of overshooting or undershooting
# #the intended destination.
#
# p=[0, 1, 0, 0, 0]
# world=['green', 'red', 'red', 'green', 'green']
# measurements = ['red', 'green']
# pHit = 0.6
# pMiss = 0.2
# pExact = 0.8
# pOvershoot = 0.1
# pUndershoot = 0.1
#
# def sense(p, Z):
#     q=[]
#     for i in range(len(p)):
#         hit = (Z == world[i])
#         q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
#     s = sum(q)
#     for i in range(len(q)):
#         q[i] = q[i] / s
#     return q
#
# def move(p, U):
#     q=[0]*len(p)
#     for i in range(len(p)):
#         index=(i-U)%len(p)
#         if i == len(p)-1:
#           next_index = 0
#           previous_index = i-1
#         else:
#           next_index = i+1
#           previous_index = i-1
#
#         q[previous_index]+=p[index]*pUndershoot
#         q[i]+=p[index]*pExact
#         q[next_index]+=p[index]*pOvershoot
#     return q
#
#
# print move(p, 1)
#
# # Question 23
# #Modify the move function to accommodate the added
# #probabilities of overshooting or undershooting
# #the intended destination.
#
# p=[0, 1, 0, 0, 0]
# world=['green', 'red', 'red', 'green', 'green']
# measurements = ['red', 'green']
# pHit = 0.6
# pMiss = 0.2
# pExact = 0.8
# pOvershoot = 0.1
# pUndershoot = 0.1
#
# def sense(p, Z):
#     q=[]
#     for i in range(len(p)):
#         hit = (Z == world[i])
#         q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
#     s = sum(q)
#     for i in range(len(q)):
#         q[i] = q[i] / s
#     return q
#
# def move(p, U):
#     q=[0]*len(p)
#     for i in range(len(p)):
#         index=(i-U)%len(p)
#         if i == len(p)-1:
#           next_index = 0
#           previous_index = i-1
#         else:
#           next_index = i+1
#           previous_index = i-1
#
#         q[previous_index]+=p[index]*pUndershoot
#         q[i]+=p[index]*pExact
#         q[next_index]+=p[index]*pOvershoot
#     return q
#
# for i in range(1000):
#   p = move(p, 1)
#
# print p

# Question 25
#Given the list motions=[1,1] which means the robot
#moves right and then right again, compute the posterior
#distribution if the robot first senses red, then moves
#right one, then senses green, then moves right again,
#starting with a uniform prior distribution.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

for i in range(len(motions)):
  p = sense(p,measurements[i])
  p = move(p,motions[i])

print p


