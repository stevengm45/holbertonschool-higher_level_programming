#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == ():
        sentence[0] = None
        return sentence
    return len(sentence), sentence[0]
