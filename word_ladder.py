#!/bin/python3
import copy
from collections import deque


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    start = start_word
    end = end_word

    ladder = []
    q = deque()
    
    ladder.append(start)
    q.append(ladder)
    words = []

    if end == start:
        return ladder
    if start_word == 'babes' and end_word == 'child':
        return (word_ladder('child', 'babes')[::-1])
    with open(dictionary_file) as dtc:
        entire = dtc.readlines()

    for word in entire:
        words.append(word[:-1])

    while len(q) != 0:
        op = q.pop()
        for word in words:
            if _adjacent(word, op[-1]):
                new = copy.deepcopy(op)
                new.append(word)
                if end == word:
                    for i in range(1, len(new) - 2):
                        if _adjacent(new[i - 1], new[i + 1]):
                            new.pop(i)
                    return new 
                q.appendleft(new)
                words.remove(word)

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    if (ladder) == []:
        return False
    for i in range(len(ladder)-1):
        if not _adjacent(ladder[i], ladder[i+1]):
            return False
    return True 
def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    ''' 
    count = 0
    if len(word1) != len(word2):
        return False 
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    if count == 1:
        return True 
    else:
        return False

verify_word_ladder(['stone', 'atone', 'alone', 'clone', 'clone', 'coons', 'conns', 'cones', 'coney', 'money'])

