'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_helper(words, count):
    if len(words) < 2:
        # we have reached the end of the text
        return count

    if words.startswith('th'):
        count += 1
        return count_helper(words[2:], count)

    return count_helper(words[1:], count)


def count_th(words):
    # TBC
    return count_helper(words, 0)
