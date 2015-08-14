"""
Write a function to calculate the Nth Fibonacci number using both iteration and recursion. *

Write a function that takes as input some text and returns the top 5 most used words in the text.

Longest Palindromic substring. Given a string, find the longest substring which is palindrome. For example, if the given string is "forgeeksskeegfor", the output should be "geeksskeeg".
"""

TEXT = """One reason people are reading on phones is convenience. If you’re standing in line at the deli, waiting at the DMV or riding home on the train, you may not have a print book or an e-reader or tablet. But chances are, you are carrying a smartphone. Some 64% of American adults now own a smartphone, up from 35% in the spring of 2011, according to the Pew Research Center. Forrester Research, a research and advisory firm, projects that smartphone subscribers will number 80.8% of the U.S. population by 2019.

“The best device to read on is the one you have with you,” said Willem Van Lancker, co-founder and chief product officer of the subscription-book service Oyster. “It requires no planning. My bookshelf at home isn’t any good to me when I’m at the park.”

Another reason people are turning to phones is the size and clarity of new smartphone models, which make reading much easier. The average smartphone screen in 2014 was 5.1 inches—compared with a 3.9-inch average in 2011, according to eMarketer.

Since the release of the bigger, sharper iPhone 6 and 6 Plus last September, Apple has seen an increase in the number of people downloading books onto iPhones through its iBooks app. Some 45% of iBooks purchases are now downloaded onto iPhones, an Apple spokeswoman said. Before that, only 28% were downloaded onto phones, with most of the remainder downloaded onto iPads and a small percentage onto computers.

Amazon has also noted the development. Among all new customers using Kindles or the Kindle app, phone readers are by far the fastest-growing segment, an Amazon spokeswoman said, declining to disclose figures. Among those who use the Kindle app, more people now read books on the iPhone 6 or 6 Plus than on any other Apple device, even the popular iPad Mini, she said."""
TEXT_WORDS = [w.strip().lower() for w in TEXT.split()]


WORDS = [w.strip().lower() for w in open('words.txt')]

def sortword(word):
    return ''.join(sorted(word))

def anagram(word, wordlist):
    import collections
    d = collections.defaultdict(list)
    # YOUR CODE HERE


def top5words(text_words):
    # YOUR CODE HERE
    return []


if __name__ == '__main__':

    assert anagram('reward', WORDS) == ['drawer', 'redraw', 'reward', 'warder', 'warred']
    assert anagram('mister', WORDS) == ['mister', 'merits', 'mister', 'miters', 'remits', 'timers']
    assert anagram('nails', WORDS) == ['nails', 'slain', 'snail']

    assert top5words(TEXT_WORDS) == [('the', 21), ('of', 9), ('to', 6), ('a', 6), ('are', 5)]

