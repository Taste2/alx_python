#!/usr/bin/python3
def multiple_returns(sentence):
    s_length = len(sentence)

    if s_length == 0:
        tup = (s_length, None)
        return tup
    else:
        tup = (s_length, sentence[0])
        return tup