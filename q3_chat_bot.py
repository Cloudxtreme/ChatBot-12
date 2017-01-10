#!/usr/bin/env python

__author__ = "Tristan Saumure Toupin"
__McGillID__ = "260688712"
__credits__ = ["Tristan Saumure Toupin"]
__version__ = "1.0"
__date__ = "november 23, 2016"
__email__ = "tristan.saumuretoupin@mail.mcgill.ca"


import os, sys, random

def firstCharToUpperCase( str ):
   return str[0].upper() + str[1:]

def normalizeInput( str ):
    # Convert string to lowercase
    str = str.lower()
    # Delete enter characters
    str = str.replace('\n', ' ')
    # Replace hyphenated words
    str = str.replace('-', ' ')
    for char in range(0, ord('a')) + range((ord('z')+1), 256):
        if (chr(char) != ' '):
            # This char is not a space and not in the a lowercase letter
            # so remove it (replace it with nothing)
            str = str.replace(chr(char), '')
    # Remove multiple spaces
    while '  ' in str:
        str = str.replace('  ', ' ')
        #return normalized string
    return str

def getLastWord( str ):
    return (str.split()[-1]);

def addWord( str ):
    space = ' '
    if str == ('[RECEIVED]: '):
        nothing = ''
        str = nothing.join( ['[RECEIVED]: ' , output] )
        return str
    else:
        space = ' '
        str = space.join( [output, str] )
        return str

def deleteR1( str ):
    str = str.split(' ', 1)[1]
    return str

def getDictionnary (  ):
    str = ''
    for x in range ( 0,len(sys.argv) ):
        if len(sys.argv) > 1:
            filename = sys.argv[x]
        else:
            print "The arguments are wrong. Please correct them."
            quit()
        try:
            file = open(filename, 'r')
        except:
            print "Error reading the file."
            quit()
        else:
            str_temp = file.read()
            file.close()
        str += str_temp
    # Convert string to lowercase
    str = str.lower()
    # Delete enter characters
    str = str.replace('\n', ' ')
    # Replace hyphenated words
    str = str.replace('-', ' ')


    for char in range(0, ord('a')) + range((ord('z')+1), 256):
        if ( chr(char) != ' ') and (chr(char) != '.') and (chr(char) != '!') and (chr(char) != '?' ):
            # This char is not a space and not in the a lowercase letter
            # so remove it (replace it with nothing)
            str = str.replace(chr(char), '')


    # Remove multiple spaces
    while '  ' in str:
        str = str.replace('  ', ' ')

    # Create dictionary
    dict = {}
    lastElement = '';

    for word in str.split(' '):
        if (lastElement != '') and (word != '') and (lastElement[-1] != '.') and ( lastElement[-1] != ','):
            newWord = '-'.join([lastElement, word])
            if dict.get(newWord):
                dict[newWord] = int(dict.get(newWord)) + 1
            elif word != '':
                dict[newWord] = 1
        lastElement = word
    return dict

def addPeriod():
    nothing = ''
    str = nothing.join( [output, '.'] )
    return str

def noConsecutiveWords( input_temp ):
    list = input_temp.split()
    m = 0
    while m < len(list)-1:
        if list[m] == list[m+1]:
            del list[m]
        else:
            m = m+1
    return ' '.join( list )

#MAIN FONCTION
if __name__ == '__main__':
    dictionary = getDictionnary( )
    while 1:        #repeat the [ SEND ]:
        #initialize output
        output = ''
        wordInOutput = 0
        msgIn = raw_input('[SEND] : ')        #get input
        msgIn = normalizeInput( msgIn )        #normalize input

        #get the last word of input
        lastWordIn = getLastWord( msgIn )

        #check if last word in input is first word in the word-pair, if not get a random word-pair
        iterator = 0
        for k in dictionary:
            iterator = iterator + 1
            if k.split('-')[0] == lastWordIn:
                output = k
                break
            if iterator == len(dictionary):
                output = random.choice(dictionary.keys())
        #maximum of 20 words
        for x in range(0, 18):
            previousWord = output.split('-')[-1]
            for k in dictionary:
                if k.split('-')[0] == previousWord:
                    output = addWord( k )
                    break

        #normalize input, erase consecutuve words
        output = normalizeInput( output )
        output = noConsecutiveWords( output )
        output = deleteR1( output ) #I believe the last word (QN), where N is the last word of the message sent, should not be in the answer
        #set the first char of output to its capital letter and period, then print
        output = firstCharToUpperCase( output )
        output = addPeriod()
        output = addWord( '[RECEIVED]: ')
        print( output )
