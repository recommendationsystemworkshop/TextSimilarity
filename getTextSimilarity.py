'''
This module contains functions for text similarity
'''

import math

def getBow(text):
    # This function returns bag of words given a text
    # print 'text:', text

    text = text.lower()
    keywordList = text.split(' ')
    # print keywordList

    bowDict = {}

    for keyword in keywordList:

        if keyword in bowDict:
            bowDict[keyword] += 1
        else:
            bowDict[keyword] = 1

    # pprint(bowDict)

    return bowDict


def getDotProduct(bow1, bow2):
    '''
    :param bow1: dictionary of bow1
    :param bow2: dictionary of bow2
    :return: dot product between them
    '''

    dot_product = 0
    for keyword1, freq1 in bow1.items():
        if keyword1 in bow2:
            value1 = freq1
            value2 = bow2[keyword1]
            dot_product += value1*value2

    return dot_product


def getNorm(bow):
    '''

    :param bow1: bag of words dictionary of text
    :return: norm of the vector
    '''

    # print bow
    sum_of_squares = 0
    for keyword, freq in bow.items():
        sum_of_squares += freq*freq

    norm = math.sqrt(sum_of_squares)

    return norm

def getCosineScore(bow1, bow2):
    # print 'Inside cosine score'

    '''
    Get cosine score between two bag of words dictionaries
        {'bow1': {'am': 1, 'anand': 1, 'i': 2}}
        {'bow2': {'a': 1, 'am': 1, 'data': 1, 'i': 1, 'scientist': 1}}

    mycosine = dot(a,b)/(norm(a)*norm(b))
    '''

    dot_product = getDotProduct(bow1, bow2)

    # print dot_product

    norm1 = getNorm(bow1)
    norm2 = getNorm(bow2)

    # print 'norm1:', norm1
    # print 'norm2:', norm2

    mycosine = dot_product / (norm1*norm2)
    # print 'mycosine:', mycosine

    return mycosine

def getSimilarityBetweenTexts(text1, text2):
    # print text1
    # print text2

    # Get bag of words of both texts

    bow1 = getBow(text1)
    bow2 = getBow(text2)

    # pprint({'bow1': bow1})
    # pprint({'bow2': bow2})

    # Compute similarity between the bag of words
    mycosine = getCosineScore(bow1, bow2)

    similarityScore = mycosine
    return similarityScore


if __name__ == '__main__':
    print 'Text Similarity Module'

    # Grab the texts
    text1 = 'I am Anand'
    text2 = 'i am a data scientist'

    # print text1
    # print text2

    # Get bag of words
    # getBow(text1)

    # Get similarity scores between the two texts
    similarityScore = getSimilarityBetweenTexts(text1, text2)
    print 'similarityScore:', similarityScore
    # bow1 = getBow(text1)
    # print bow1
    # norm = getNorm(bow1)
    #
    # print norm
    # print math.sqrt(6)


