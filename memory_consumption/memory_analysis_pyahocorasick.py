import random
import json
import threading
from ahocorasick import Automaton


# python dictionary with trie patterns
file_words = json.load(open("../static_ioc_sample_30k.txt", "r"))
words_to_search = list()
trie_words = list()

total_words_to_search = 1000
total_words_added = 0

t = list()
patterns = dict()
total_initial_words = 0
total_iterations = 10 # CHANGE the number of iterations to perform: +/- 30k patterns per iteration.
A = Automaton()
for x in range(0, total_iterations):
    print("In iteration ",x)
    for key in file_words:
        for value in file_words[key]:
            value_random = value+str(random.randint(10000,500000))
            if total_words_to_search != total_words_added:
                words_to_search.append(value)
                total_words_added += 1
            if x == 0: 
                total_initial_words += 1
            A.add_word(value_random, value)

print(f"Initial words {total_initial_words}")
print(f"Total patterns on AC trie: {total_initial_words*total_iterations+1}")
A.make_automaton()
input() #stop program to measure memory of the built AC trie
