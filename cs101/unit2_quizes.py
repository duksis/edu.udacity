#!/usr/bin/env python

# UNIT 2

#Define a procedure, square, that
#takes one number as its input,
#and outputs the square of that
#number (result of multiplying
#the number by itself).

#print square(5) => 25

def square(n):
    return n*n


#Define a procedure, sum3, that takes three
#inputs, and outputs the sum of the three
#input numbers.

#print sum3(1,2,3) => 6

def sum3(n1,n2,n3):
    return n1+n2+n3


#Define a procedure, abbaize, that takes
#two strings as its inputs, and outputs
#a string that is the first input,
#followed by two repetitions of the second input,
#followed by the first input.

#abbaize('a','b') => 'abba'
#abbaize('dog','cat') => 'dogcatcatdog'

def abbaize(string1,string2):
    return string1+string2*2+string1


#Define a procedure, find_second, that takes
#two strings as its inputs: a search string
#and a target string. It should output a
#number that is the position of the second
#occurence of the target string in the
#search string.

#danton = "De l'audace, encore de l'audace, toujours de l'audace"
#print find_second(danton, 'audace') => 25

def find_second(string,substring):
    end_of_first_occurance = string.find(substring)+len(substring)
    return string.find(substring,end_of_first_occurance)

#Define a procedure, bigger, that takes in
#two numbers as inputs, and outputs the
#greater of the two inputs.

#bigger(2,7) => 7
#bigger(3,2) => 3
#bigger(3,3) => 3

def bigger(a,b):
    if a < b:
      return b
    else:
      return a

#Define a procedure, is_friend, that
#takes a string as its input, and
#outputs a Boolean indicating if
#the input string is the name of
#a friend. Assume I am friends with
#everyone whose name starts with D
#and N no one else.

#print is_friend('Diane') => True
#print is_friend('Fred')  => False

def is_friend(name):
    return ['D','N'].count(name[:1]) > 0

#Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(a,b,c):
    return max([a,b,c])


# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(n):
    i = 1
    while (n >= i):
      print i
      i = i + 1

#Define a procedure, factorial, that
#takes one number as its input
#and returns the factorial of
#that number.

def factorial(n):
    i = 1
    factorial = n
    while (n-i)>0:
      factorial = factorial * (n-i)
      i = i+1
    return factorial

# Return all links from http://xkcd.com/353 using Python 2 interpreter

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return "error"

# Modify the get_next_target procedure so that
# if there is a link it behaves as before, but
# if there is no link tag in the input string,
# it outputs None, 0.

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
      url,end_quote = None,0

    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

# Print All Links

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break
print_all_links(get_page('http://xkcd.com/353'))
    
