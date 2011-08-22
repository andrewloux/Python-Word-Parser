"""Python Word Parser

Created by Andrew Louis

Uploaded to GitHub on 23rd August, 2011
"""
#Sample Input: aggregator('/home/andrew/Documents/PythonParser/Aggregator/source.txt')

import re,operator,sys

def aggregator(texty):
    
    filenom = open(texty,'r')
    text = filenom.read()    
    list_block = []
    finalsort = []

    #Creating punctuation-less version of text.
    punct = re.compile (r'([.?;,!"\\//])')

    
    text = punct.sub("",text) 
    #Splitting into the list and sorting by alphabetical
    text = text.split()
    for word in text:
        if not word in list_block:
            finalsort.insert(0,(word,text.count(word)))
            list_block.insert(0,word)
    list_block = [] #For contingencies
    #Sorting by position [1] in the list
    finalsort = sorted(finalsort,key=operator.itemgetter(1))
    #Reversing and printing because it appears in the opposite direction.
    finalsort.reverse()
    

    ignore = ('and','in','of','the','is','at','he','his','her',
              'And','to','that','a','for','with','was','it','him')

    
    outputfile = open(texty+".wordcount.txt",'w')
    for tuplething in finalsort:
        if tuplething[1]== 1: continue
        elif tuplething[0] in ignore: continue
        else:
            sillystring = (str("\t\t\t\t%s : %s\n\n"%(tuplething[0],tuplething[1])))
            outputfile.write(sillystring)
    outputfile.close()

if __name__ == "__main__":
    aggregator (sys.argv[1])
    
