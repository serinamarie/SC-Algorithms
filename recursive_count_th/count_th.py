'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
#word = 'hello'

def count_th(word):

    # get the index we will check 
    index = len(word) - 1

    # ready our new word to iterate through (cutting off the last letter)
    new_word = word[0:index]

    # if the word cannot contain 'th'
    if len(word) <= 1:

        return 0

    # if the slice contains 'th' 
    elif word[index-1:index+1] == 'th':

        # add a count of 1 and run the new word through
        return 1 + count_th(new_word)

    # if the slice does not contain 'th'
    else:

        # run the new word through
        return count_th(new_word)

# plan: from the tests, it seems like we could remove letters around 'th' 
# nah. we could get a slice of the word, then  

count_th('hethath')