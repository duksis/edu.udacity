#!/usr/bin/env python

# UNIT 4 QUESTION NOTES

#############################################
## 3 adding index

#Define a procedure, add_to_index,
#that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

#If the keyword is already
#in the index, add the url
#to the list of urls associated
#with that keyword.

#If the keyword is not in the index,
#add an entry to the index: [keyword,[url]]

index = []


#add_to_index(index,'udacity','http://udacity.com')
#add_to_index(index,'computing','http://acm.org')
#add_to_index(index,'udacity','http://npr.org')
#print index => [['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]

def add_to_index(index,keyword,url):
    for el in index:
        if keyword == el[0]:
            if url not in el[1]:
                el[1].append(url)
            return index
    return index.append([keyword,[url]])

#############################################
## 4 lookup

#Define a procedure, lookup,
#that takes two inputs:

#   - an index
#   - keyword

#The output should be a list
#of the urls associated
#with the keyword. If the keyword
#is not in the index, the output
#should be an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]

#lookup(index,keyword) => ['http://udacity.com','http://npr.org']


def lookup(index,keyword):
    for el in index:
        if keyword == el[0]:
          return el[1]
    return []

#############################################
## 6 add page to index

#Define a procedure, add_page_to_index,
#that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

#It should update the index to include
#all of the word occurences found in the
#page content by adding the url to the
#word's associated url list.


index = []

#add_page_to_index(index,'fake.text',"This is a test")
#print index => [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']], ['test', ['fake.text']]]

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    for word in content.split():
        add_to_index(index,word,url)


