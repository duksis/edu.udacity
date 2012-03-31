#!/usr/bin/env python

# UNIT 4 HOMEWORK

#1 Gold Star

#################################
## 5 Better splitting

#The built-in <string>.split() procedure works
#okay, but fails to find all the words on a page
#because it only uses whitespace to split the
#string. To do better, we should also use punctuation
#marks to split the page into words.

#Define a procedure, split_string, that takes two
#inputs: the string to split and a string containing
#all of the characters considered separators.

#out = split_string("This is a test-of the,string separation-code!", " ,!-")
#print out => ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

#out = split_string("After  the flood   ...  all the colors came out."," .")
#print out => ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

def split_string(source,splitlist):
    words = source
    result =[]
    for spliter in splitlist:
      words = words.replace(spliter," ")
    for word in words.split(" "):
      if len(word) > 0:
        result.append(word)
    return result


######################################################
## 6 Improving the index

#The current index includes a url in the list of urls
#for a keyword multiple times if the keyword appears
#on that page more than once.

#It might be better to only include the same url
#once in the url list for a keyword, even if it appears
#many times.

#Modify add_to_index so that a given url is only
#included once in the url list for a keyword,
#no matter how many times that keyword appears.

#index = crawl_web("http://www.udacity.com/cs101x/index.html")
#print lookup(index,"is") => ['http://www.udacity.com/cs101x/index.html']


def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword and url not in entry[1]:
            entry[1].append(url)
            return
    # not found, add new keyword to index
    index.append([keyword, [url]])


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

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None
# index = crawl_web("http://www.udacity.com/cs101x/index.html")
# print lookup(index,"is")

#################################################################
## 7 Counting clicks

#2 Gold Stars

#One way search engines rank pages
#is to count the number of times a
#searcher clicks on a returned link.
#This indicates that the person doing
#the query thought this was a useful
#link for the query, so it should be
#higher in the rankings next time.

#(In Unit 6, we will look at a different
#way of ranking pages that does not depend
#on user clicks.)

#Modify the index such that for each url in a
#list for a keyword, there is also a number
#that counts the number of times a user
#clicks on that link for this keyword.

#The result of lookup(index,keyword) should
#now be a list of url entries, where each url
#entry is a list of a url and a number
#indicating the number of times that url
#was clicked for this query keyword.

#You should define a new procedure to simulate
#user clicks for a given link:

#record_user_click(index,word,url)

#that modifies the entry in the index for
#the input word by increasing the count associated
#with the url by 1.

#You also will have to modify add_to_index
#in order to correctly create the new data
#structure.

#Here is an example showing a sequence of interactions:


#index = crawl_web('http://www.udacity.com/cs101x/index.html')
#print lookup(index, 'good') => [['http://www.udacity.com/cs101x/index.html', 0], ['http://www.udacity.com/cs101x/crawling.html', 0]]
#record_user_click(index, 'good', 'http://www.udacity.com/cs101x/crawling.html')
#print lookup(index, 'good') => [['http://www.udacity.com/cs101x/index.html', 0], ['http://www.udacity.com/cs101x/crawling.html', 1]]

def record_user_click(index,keyword,url):
    for entry in index:
      if entry[0] == keyword:
        for link in entry[1]:
          if link[0] == url:
            link[1] += 1
        return

def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append([url,0])
            return
    # not found, add new keyword to index
    index.append([keyword, [[url,0]]])


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

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None

index = crawl_web('http://www.udacity.com/cs101x/index.html')
print lookup(index, 'good')
record_user_click(index, 'good', 'http://www.udacity.com/cs101x/crawling.html')
print lookup(index, 'good')