#!/usr/bin/env python

# UNIT 3 question notes

# Q 3 Days in month
#Given the variable,

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

#define a procedure, how_many_days,
#that takes as input a number
#representing a month, and outputs
#the number of days in that month.

def how_many_days(month):
    return days_in_month[month-1]


# print how_many_days(1) # => 31
# print how_many_days(9) # => 30

# Q 5 Countries
#Given the variable countries defined as:


#             Name      Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

#Write code to print out the capital of India
#by accessing the array.

# print countries[1][1]

# Q 6 Relative size
#What multiple of Romania's population is the population
#of China? Please print your result.

# print countries[0][2]/countries[2][2]

# Q 9 Different Stooges
#We defined:

stooges = ['Moe','Larry','Curly']

#but in some Stooges films, Curly was
#replaced by Shemp.

#Write one line of code that changes
#the value of stooges to be:

['Moe','Larry','Shemp']

#but does not create a new List
#object.

stooges[2]='Shemp'


# Q 13 replace spy
#Define a procedure, replace_spy,
#that takes as its input a list of
#three numbers, and modifies the
#value of the third element in the
#input list to be one more than its
#previous value.

spy = [0,0,7]

def replace_spy(spy):
    spy[2]=spy[2]+1

# replace_spy(spy)
# print spy # => [0,0,8]


# Q 24 summ list
#Define a procedure, sum_list,
#that takes as its input a
#List of numbers, and produces
#as its output the sum of all
#the elements in the input list.

def sum_list(list):
    # return sum(list)
    sum = 0
    for element in list:
        sum += element
    return sum

#For example,
# print sum_list([1,7,4]) # => 12


# Q 25 Measure Udacity

#Define a procedure, measure_udacity,
#that takes its input a list of Strings,
#and outputs a number that is a count
#of the number of elements in the input
#list that start with the letter 'U'
#(uppercase).

def measure_udacity(li):
    count = 0
    for el in li:
        if el[0] == 'U':
            count += 1
    return count

#For example,

# print measure_udacity(['Dave','Sebastian','Katy']) # => 0
#
# print measure_udacity(['Umika','Umberto']) # => 2

#Define a procedure, find_element,
#that takes as its inputs a List
#and a value of any type, and
#outputs the index of the first
#element in the input list that
#matches the value.

#If there is no matching element,
#output -1.

def find_element(li,el):
    for i in range(0,len(li)):
        if li[i] == el:
            return i
    return -1

def find_element(li,el):
    if el in li:
        return li.index(el)
    return -1

#find_element([1,2,3],3) => 2

#find_element(['alpha','beta'],'gamma') => -1

# Q 29 Union
#Define a procedure, union,
#that takes as inputs two lists.
#It should modify the first input
#list to be the set union of the two
#lists.

def union(a,b):
    for el in b:
        if el not in a:
          a.append(el)


# a = [1,2,3]
# b = [2,4,6]
# union(a,b)
# print a # => [1,2,3,4,6]
# print b # => [2,4,6]



