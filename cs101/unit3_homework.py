#!/usr/bin/env python

#Define a procedure, product_list,
#takes as input a list of numbers,
#and returns a number that is
#the result of multiplying all
#those numbers together.

#product_list([9]) => 9
#product_list([1,2,3,4]) => 24

def product_list(n):
    result = 1
    for i in range(0,len(n)):
        result = result * n[i]
    return result


#Define a procedure, greatest,
#that takes as input a list
#of positive numbers, and
#returns the greatest number
#in that list. If the input
#list is empty, the output
#should be 0.

#greatest([4,23,1]) => 23
#greatest([]) => 0

def greatest(n):
    greatest = 0
    for i in range(0,len(n)):
        if n[i] > greatest:
            greatest = n[i]
    return greatest

#Define a procedure, total_enrollment,
#that takes as an input a list of elements,
#where each element is a list containing
#three elements: a university name,
#the total number of students enrollect,
#and the annual tuition.

#The procedure should return two numbers,
#not a string,
#giving the total number of students
#enrolled at all of the universities
#in the list, and the total tuition
#(which is the sum of the number
#of students enrolled times the
#tuition for each university).

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

#>>> print total_enrollment(udacious_univs)
#(90000,0)

#>>> print total_enrollment(usa_univs)
#(77285,3058581079L)

def total_enrollment(universities):
    students,total_tuition = 0,0
    for i in range(0,len(universities)):
        students += universities[i][1]
        total_tuition += universities[i][1] *universities[i][2]
    return students,total_tuition


#The web crawler we built at the
#end of Unit 2 has some serious
#flaws if we were going to use
#it in a real crawler. One
#problem is if we start with
#a good seed page, it might
#run for an extremely long
#time (even forever, since the
#number of URLS on the web is not
#actually finite). The final two
#questions of the homework ask
#you to explore two different ways
#to limit the pages that it can
#crawl.


#######


#Modify the crawl_web procedure
#to take a second parameter,
#max_pages, that limits the
#number of pages to crawl.
#Your procedure should
#terminate the crawl after
#max_pages different pages
#have been crawled, or when
#there are no more pages to crawl.



#The following definition of
#get_page provides an interface
#to the website found at
#http://www.udacity.com/cs101x/index.html

#The function output order does not affect grading.

#crawl_web("http://www.udacity.com/cs101x/index.html",1) => ['http://www.udacity.com/cs101x/index.html']
#crawl_web("http://www.udacity.com/cs101x/index.html",3) => ['http://www.udacity.com/cs101x/index.html', 'http://www.udacity.com/cs101x/flying.html', 'http://www.udacity.com/cs101x/walking.html']
#crawl_web("http://www.udacity.com/cs101x/index.html",500) => ['http://www.udacity.com/cs101x/index.html', 'http://www.udacity.com/cs101x/flying.html', 'http://www.udacity.com/cs101x/walking.html', 'http://www.udacity.com/cs101x/crawling.html', 'http://www.udacity.com/cs101x/kicking.html']

def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return  '<html> <body> This is a test page for learning to crawl! <p> It is a good idea to  <a href="http://www.udacity.com/cs101x/crawling.html">learn to crawl</a> before you try to  <a href="http://www.udacity.com/cs101x/walking.html">walk</a> or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. </p> </body> </html> '
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return  '<html> <body> I have not learned to crawl yet, but I am quite good at  <a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>. </body> </html>'
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return '<html> <body> I cant get enough  <a href="http://www.udacity.com/cs101x/index.html">crawling</a>! </body> </html>'
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return '<html> <body> The magic words are Squeamish Ossifrage! </body> </html>'
    except:
        return ""
    return ""

# Actual get pages
# import urllib
# def get_page(url):
#     try:
#         return urllib.urlopen(url).read()
#     except:
#         return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def crawl_web(seed,max_pages):
    tocrawl = [seed]
    crawled = []
    while tocrawl and len(crawled)<max_pages:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled


#The web crawler we built at the
#end of Unit 2 has some serious
#flaws if we were going to use
#it in a real crawler. One
#problem is if we start with
#a good seed page, it might
#run for an extremely long
#time (even forever, since the
#number of URLS on the web is not
#actually finite). The final two
#questions of the homework ask
#you to explore two different ways
#to limit the pages that it can
#crawl.


#######

#TWO GOLD STARS#

#Modify the crawl_web procedure
#to take a second parameter,
#max_depth, that limits the
#minimum number of consecutive
#links that would need to be followed
#from the seed page to reach this
#page. For example, if max_depth
#is 0, the only page that should
#be crawled is the seed page.
#If max_depth is 1, the pages
#that should be crawled are the
#seed page and every page that links
#to it directly. If max_depth is 2,
#the crawl should also include all pages
#that are linked to by these pages.


#The following definition of
#get_page provides an interface
#to the website found at
#http://www.udacity.com/cs101x/index.html

#The function output order does not affect grading.

#crawl_web("http://www.udacity.com/cs101x/index.html",0) => ['http://www.udacity.com/cs101x/index.html']
#crawl_web("http://www.udacity.com/cs101x/index.html",1) => ['http://www.udacity.com/cs101x/index.html', 'http://www.udacity.com/cs101x/flying.html', 'http://www.udacity.com/cs101x/walking.html', 'http://www.udacity.com/cs101x/crawling.html']
#crawl_web("http://www.udacity.com/cs101x/index.html",50) => ['http://www.udacity.com/cs101x/index.html', 'http://www.udacity.com/cs101x/flying.html', 'http://www.udacity.com/cs101x/walking.html', 'http://www.udacity.com/cs101x/crawling.html', 'http://www.udacity.com/cs101x/kicking.html']


def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return  '<html> <body> This is a test page for learning to crawl! <p> It is a good idea to  <a href="http://www.udacity.com/cs101x/crawling.html">learn to crawl</a> before you try to  <a href="http://www.udacity.com/cs101x/walking.html">walk</a> or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. </p> </body> </html> '
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return  '<html> <body> I have not learned to crawl yet, but I am quite good at  <a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>. </body> </html>'
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return '<html> <body> I cant get enough  <a href="http://www.udacity.com/cs101x/index.html">crawling</a>! </body> </html>'
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return '<html> <body> The magic words are Squeamish Ossifrage! </body> </html>'
    except:
        return ""
    return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def crawl_web(seed,max_depth):
    tocrawl = [seed]
    tocrawlnext = []
    crawled = []
    i = 0
    while tocrawl and i<=max_depth:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawlnext, get_all_links(get_page(page)))
            crawled.append(page)
        if len(tocrawl) < 1:
            union(tocrawl,tocrawlnext)
            tocrawlnext = []
            i += 1
    return crawled


#THREE GOLD STARS

#Sudoku [http://en.wikipedia.org/wiki/Sudoku]
#is a logic puzzle where a game
#is defined by a partially filled
#9 x 9 square of digits where each square
#contains one of the digits 1,2,3,4,5,6,7,8,9.
#For this question we will generalize
#and simplify the game.


#Define a procedure, check_sudoku,
#that takes as input a square list
#of lists representing an n x n
#sudoku puzzle solution and returns
#True if the input is a valid
#sudoku square and returns False
#otherwise.

#A valid sudoku square satisfies these
#two properties:

#   1. Each column of the square contains
#       each of the numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the numbers from 1 to n exactly once.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]


def check_sudoku(puzzle):
    validity = True
    for i in range(0,len(puzzle)):
        if sorted(puzzle[i]) != range(1,len(puzzle[i])+1):
            validity = False
        column = []
        for n in range(0,len(puzzle)):
            column.append(puzzle[n][i])
        if sorted(column) != range(1,len(puzzle)+1):
            validity = False
    return validity

# print check_sudoku(correct)
# print check_sudoku(incorrect)
