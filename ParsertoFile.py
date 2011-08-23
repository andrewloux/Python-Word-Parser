"""Python Word Parser

Created by Andrew Louis

Uploaded to GitHub on 23rd August, 2011, v 2.0 @ 8:00 EST
"""
import re,sys
from collections import *

def Parser(textfile,top_x):
    
    FileWords = re.findall ('\w+',open(textfile).read().lower())
    FileWordsC = Counter(FileWords)

    ignore = ['is','if','a','it','the','an','in','of','to','and','that','be',
              'his','he','her','on','not','by','s','ch','are','this','as','for',
              'was','with','which','or','for','from','i','you','at','when','have',
              'but','may','they','their','be','who','your','says','said','all',
              'him','1','2','3','4','5','6','7','8','9','t','o','-','_']

    for word in FileWords:
        if word in ignore:
            del FileWordsC[word]


    sillyfile = open(textfile+".Parsed",'w')
    sillystring = FileWordsC.most_common(top_x)
    
    for word,frequency in sillystring:
        sillyfile.write(str("\n%15s : %s" % (word,frequency)))
    sillyfile.close()

if __name__ == "__main__":
    directory = sys.argv[1]
    arb = sys.argv[2]
    topwhaaat = int(arb)

    Parser(directory,topwhaaat)
    
