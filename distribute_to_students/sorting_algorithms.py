from ds import *

def bubble_sort( theSeq ):
    if(isinstance(theSeq, list)):
        n = len( theSeq )
        for i in range( n - 1 ):
            for j in range( n-(i+1) ):
                if (theSeq[j] > theSeq[j+1]):
                    tmp = theSeq[j]
                    theSeq[j] = theSeq[j + 1]
                    theSeq[j + 1] = tmp
            #print(theSeq)
        return theSeq
    
        
