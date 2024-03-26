## Lab 5: Required Questions - Dictionaries  ##

# RQ1
def merge(dict1, dict2):
    """Merges two Dictionaries. Returns a new dictionary that combines both. You may assume all keys are unique.

    >>> new =  merge({1: 'one', 3:'three', 5:'five'}, {2: 'two', 4: 'four'})
    >>> new == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    True
    """
    "*** YOUR CODE HERE ***"
    merged_dict = {**dict1, **dict2}
    return merged_dict


# RQ2
def counter(message):
    """ Returns a dictionary where the keys are the words in the message, and each
    key is mapped (has associated value) equal 
    to the number of times the word appears in the message.
    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    "*** YOUR CODE HERE ***"

    words = message.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count



# RQ3
def replace_all(d, x, y):
    """ Returns a dictionary where the key/value pairs are the same as d, 
    except when a value is equal to x, then it should be replaced by y.
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> d2= replace_all(d, 3, 'poof')
    >>> d2 == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    "*** YOUR CODE HERE ***"
    new_dict = {}

    for key, value in d.items():
        if value == x:
            new_dict[key] = y
        else:
            new_dict[key] = value

    return new_dict


# RQ4
def sumdicts(lst):
    """ 
    >>> d = sumdicts ([{'a': 5, 'b': 10, 'c': 90, 'd': 19}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}] )
    >>> d == {'b': 88, 'c': 100, 'a': 140, 'd': 19}
    True
    """

    result = {}

    for d in lst:
        for key, value in d.items():
            if key in result:
               result[key]+= value
            else:
               result[key] = value
    return result



#RQ5

#Here is starter code that is explained in the Interactive Worksheet

def build_successors_table():
    """Return a dictionary: keys are words; values are lists of successor words. By default, we set the first word in tokens to be a successor to "."
    """
    f = open("C:\\Users\\jackm\\OneDrive - University of Cincinnati\\Python Programing\\Lab05\\shakespeare.txt", "r", encoding="ascii")
    tokens = f.read().split()
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = []
        table[prev] += [word]
        prev = word
    return table

def construct_tweet(word, table):
    """Returns a string that is a random sentence starting with word, and choosing successors from table.
    """
    import random
    result = ' '
    while word not in ['.', '!', '?']:
        result += word + ' '
        word = random.choice(table[word])
    return result + word

def random_tweet():
    import random
    tweet_table = build_successors_table()
    return construct_tweet(random.choice(tweet_table['.']), tweet_table)
   
def middle_tweet():
    """ Calls the function random_tweet() 5 times. Modify this code to 
    returns one single string which has length in middle value of the 5.
    My experiments showed that with 5 random samples you should usually
    get a tweet that is in range of 60-100 characters. One of the following tests
    may sometimes fail.
    >>> len(middle_tweet()) > 60
    True
    >>> len(middle_tweet()) < 100
    True
    """
    "*** YOUR CODE HERE ***"
    import random
    
    tweets = []
    while len(tweets) < 5:
        tweet = random_tweet()
        if 60 <= len(tweet) <= 100:
            tweets.append(tweet)

    lengths = [len(tweet) for tweet in tweets]

    middle_length = sorted(lengths)[len(lengths) // 2]

    middle_tweet = min(tweets, key=lambda tweet: abs(len(tweet) - middle_length))

    return middle_tweet
        

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)