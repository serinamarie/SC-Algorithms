'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
#word = 'hello'

def count_th(word):

    index = len(word) - 1

    new_word = word[0:index]

    if len(word) <= 1:
        return 0
        
    elif word[index-1:index+1] == 'th':
        return 1 + count_th(new_word)

    else:
        return count_th(new_word)

# plan: from the tests, it seems like we could remove letters around 'th' 
# nah. we could get a slice of the word, then  

count_th('hethath')