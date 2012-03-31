#!/usr/bin/env python

## HOMEWORK 2
##
# Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.
# for example, when we enter

# print udacify('dacians')

# the output should be the string 'Udacians'

# Make sure your procedure has a return statement.

def udacify(string):
    return 'U'+string


# Define a procedure, median, that takes three
# numbers as its inputs, and outputs the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    return (a+b+c)/3


# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!

def countdown(n):
    while n>0:
      print n
      n = n -1
      if n == 0:
        print 'Blastoff!'


# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and outputs the last position in the search string
# where the target string appears, or -1 if there
# are no occurences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(string,substring):
    start_at = -1
    while string.find(substring,start_at+1) >= 0:
      start_at = string.find(substring,start_at+1)
    return start_at


#2 GOLD STARS

#Define a procedure,
#print_multiplication_table,
#that takes as input a positive whole
#number, and prints out a multiplication,
#table showing all the whole number
#multiplications up to and including the
#input number. The order in which the
#equations are printed must match exactly.

#print_multiplication_table(2)
#1 * 1 = 1
#1 * 2 = 2
#2 * 1 = 2
#2 * 2 = 4

def print_multiplication_table(n):
    i = 1
    while i<=n:
      j = 1
      while j<=n:
        print str(i)+' * '+str(j)+' = '+str(i*j)
        j=j+1
      i=i+1
