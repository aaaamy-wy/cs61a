""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
"*** YOUR CODE HERE ***"
#question 1
def lines_from_file(path):
    f = open(path, mode='r')
    lines = f.readlines()
    new_lines = []
    for line in lines:
        new_lines.append(line.strip())
    return new_lines

def new_sample(path, i):
    final_lst = lines_from_file(path)
    return final_lst[i]


#problem 2
def analyze(sample_paragraph,typed_string, start_time, end_time):
    def words_per_minute(t1, t2):
        total_time = (t2 - t1) / 60
        time = (len(typed_string) / 5) / total_time
        return [time]
    def accuracy(sample, typed):
        sample_word = sample.split()
        typed_word = typed.split()
        word_len = min(len(sample_word), len(typed_word))
        if word_len == 0:
            return [0.0]
        else:
            count = 0
            for i in range (word_len):
                if typed_word[i] == sample_word[i]:
                    count += 1
            accuracy_percentage = (count / word_len) * 100
            return [accuracy_percentage]
    return words_per_minute(start_time, end_time) + accuracy(sample_paragraph, typed_string)

#probelm 3
def pig_latin(string):
    if string[0] in ['a', 'e', 'i', 'o', 'u']:
        return string + 'way'
    else:
        keep = string[0]
        for i in range(1, len(string)):
            if string[i] not in ['a', 'e', 'i', 'o', 'u']:
                keep += string[i]
            else:
                return string[i:] + keep + 'ay'
        return keep + 'ay'

#problem 4
def autocorrect(user_input, words_list, score_function):
    if user_input in words_list:
        return user_input
    else:
        result = {i: score_function(user_input, i) for i in words_list}
        return min(result, key = lambda x: result[x])

# problem 5
def swap_score(word1, word2):
    """
    >>> swap_score("nice", "rice")  # Substitute n to r
    1
    >>> swap_score("range", "rungs")  # Substitute a to u, e to s
    2
    >>> swap_score("pill", "pillage")  # Don't substitute anything
    0
    >>> swap_score("byte", "bit")  # Substitute y to i
    1
    """
    if word1 == word2:
        return 0
    elif not word1 or not word2:
        return 0
    elif word1[0] == word2[0]:
        return swap_score(word1[1:], word2[1:])
    else:
        return 1 + swap_score(word1[1:], word2[1:])

# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if word1 == word2: # Fill in the condition
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        return 0
        # END Q6

    elif not word2: # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        return len(word1)
        # END Q6
    elif not word1:  # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6
        return len(word2)
    elif word1[0] == word2[0]:
        return score_function(word1[1:], word2[1:])
    else:
        add_char = score_function(word1, word2[1:])  # Fill in these lines
        remove_char = score_function(word1[1:], word2)
        substitute_char = score_function(word1[1:], word2[1:])
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        return 1 + min(add_char, remove_char, substitute_char)
        # END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
# problem 7
def score_function_accurate(word1, word2):
    if word1 == word2:
        return 0
    elif not word2:
        return len(word1)
    elif not word1:
        return len(word2)
    elif word1[0] == word2[0]:
        return score_function_accurate(word1[1:], word2[1:])
    else:
        add_char = 1 + score_function_accurate(word1, word2[1:])
        remove_char = 1 + score_function_accurate(word1[1:], word2)
        substitute_char = score_function_accurate(word1[1:], word2[1:]) + KEY_DISTANCES[word1[0], word2[0]]
        return min(add_char, remove_char, substitute_char)

#problem 8
def score_function_final(word1, word2):
    """
    >>> score_function_final("wird", "wiry")

    """
    cache = {}
    n = len(word1)
    return score_function_final_helper(word1, word2, 0, 0, cache, n)

def score_function_final_helper(word1, word2, i, j, cache, n):
    if i == len(word1) and j == len(word2):
        return 0
    elif i == len(word1):
        return len(word2) - j
    elif j == len(word2):
        return len(word1) - i

    key = i + j * n
    if key in cache:
        return cache[key]
    elif word1[i] == word2[j]:
        cache[key] = score_function_final_helper(word1, word2, i + 1, j + 1, cache, n)
    else:
        add_char = 1 + score_function_final_helper(word1, word2, i, j + 1, cache, n)
        remove_char = 1 + score_function_final_helper(word1, word2, i + 1, j, cache, n)
        substitute_char = score_function_final_helper(word1, word2, i + 1, j + 1, cache, n) + KEY_DISTANCES[word1[i], word2[j]]
        cache[key] = min(add_char, remove_char, substitute_char)
    return cache[key]

# END Q7-8
