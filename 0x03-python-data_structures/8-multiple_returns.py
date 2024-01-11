#!/usr/bin/python3
def multiple_returns(sentence):
    val = len(sentence)
    if not val:
        return (val, None)
    else:
        return (val, sentence[0])
