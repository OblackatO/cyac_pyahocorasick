import random
import json
import threading
from ahocorasick import Automaton
from statistics import mean
from time import process_time


# python dictionary with trie patterns
file_words = json.load(open("../static_ioc_sample_30k.txt", "r"))
words_to_search = list()
trie_words = list()

total_words_to_search = 25_000
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
            value = value+str(random.randint(10000,500000))
            if total_words_to_search != total_words_added:
                words_to_search.append(value)
                total_words_added += 1
            if x == 0: 
                total_initial_words += 1
            A.add_word(value, value)

print(f"Initial words {total_initial_words}")
print(f"Total patterns on AC trie: {total_initial_words*total_iterations+1}")
A.make_automaton()

start1 = process_time()
for word_to_search in words_to_search:
    start = process_time()
    end = 0
    for match in A.iter(word_to_search):
        pass
end1 = process_time()
print(f"Took {end1-start1}sec to match {len(words_to_search)} patterns on a AC automaton with {total_initial_words*total_iterations}")



#Took 0.0668650930000001sec for 25000 patterns (change var total_words_to_search, above.)
#Took 0.23291606600000003sec for 100000 patterns
#Took 0.4542991380000001sec for 200000 patterns
#Took 0.684820883sec for 300000 patterns

# Took 0.061951500999999964sec to match 25000 patterns on a AC automaton with 63000
# Took 0.06499120199999997sec to match 25000 patterns on a AC automaton with 126000
# Took 0.066342342sec to match 25000 patterns on a AC automaton with 189000
# Took 0.07048644500000001sec to match 25000 patterns on a AC automaton with 315000