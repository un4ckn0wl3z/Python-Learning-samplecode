def break_words(stuff) :
    """this function will break up words for use"""
    words = stuff.split(' ')
    return words

def sort_words(words) :
    """Sorts the word."""
    return sorted(words)

def print_first_word(words) :
    """Print 1st word"""
    words = words.pop(0)
    print words
    
def print_last_word(words) :
    words = words.pop(-1)
    print words
    
def sort_sentence(sentence) :
    """Take it a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence) :
    """Print the first and last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence) :
    """Sorts the word then print the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    

    
    
    
    
    
    
    
    
    
    
    