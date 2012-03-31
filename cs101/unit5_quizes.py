#!/usr/bin/env python

## Quize 19 Better hash function

#Define a function, hash_string,
#that takes as inputs a keyword
#(string) and a number of buckets,
#and outputs a number representing
#the bucket for that keyword.

#print hash_string('a',12) => 1
#print hash_string('b',12) => 2
#print hash_string('a',13) => 6

#print hash_string('au',12) => 10
#print hash_string('udacity',12) => 11

def hash_string(keyword,buckets):
    sum = 0
    for char in keyword:
        sum += ord(char)
    return sum % buckets


## Quize 23 Empty hash table
#Creating an Empty Hash Table
#Define a procedure, make_hashtable,
#that takes as input a number, nbuckets,
#and outputs an empty hash table with
#nbuckets empty buckets.

def make_hashtable(nbuckets):
    table = []
    for i in range(0,nbuckets):
        table.append([])
    return table

## Quize 25 finding buckets
#Define a procedure, hashtable_get_bucket,
#that takes two inputs - a hashtable, and
#a keyword, and outputs the bucket where the
#keyword could occur.

#hash_string(keyword,nbuckets) => index of bucket

def hashtable_get_bucket(htable,keyword):
  # YOUR CODE GOES HERE:
    return htable[hash_string(keyword,len(htable))]
  # END

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

## Quize 26 Adding key words
#Define a procedure,

#hashtable_add(htable,key,value)

#that adds the key to the hashtable
#(in the correct bucket), with the
#correct value.

def hashtable_add(htable,key,value):
    hashtable_get_bucket(htable,key).append([key,value])

## Quize 27 Lookup
#Define a procedure,

#hashtable_lookup(htable,key)

#that takes two inputs, a hashtable
#and a key (string),
#and outputs the value associated
#with that key.

def hashtable_lookup(htable,key):
    for entry in hashtable_get_bucket(htable,key):
        if entry[0] == key:
          return entry[1]
    return None


## Quize 28 Update
#Define a procedure,

#hashtable_update(htable,key,value)

#that updates the value associated
#with key. If key is already in the
#table, change the value to the new
#value. Otherwise, add a new entry
#for the key and value.

#Hint: Use hashtable_lookup as a
#starting point.

def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return
    bucket.append([key,value])

## Question 31 Population
#Define a Dictionary, population,
#that provides information
#on the world's largest cities.
#The key is the name of a city
#(a string), and the associated
#value is its population in
#millions.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {'Shanghai':17.8,'Istanbul':13.3, 'Karachi':13.0, 'Mumbai':12.0, 'Riga':0.7}

## Question 34 Changing Lookup
#Change the lookup procedure
#to now work with dictionaries.

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    return None

