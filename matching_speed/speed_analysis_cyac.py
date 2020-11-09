import random
import json
import threading
from cyac import AC
from time import process_time
from statistics import mean


# python dictionary with trie patterns
file_words = json.load(open("../static_ioc_sample_30k.txt", "r"))
words_to_search = list()
trie_words = list()

total_words_to_search = 25_000
total_words_added = 0

t = list()
patterns = dict()
total_initial_words = 0
total_iterations = 2
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
            t.append(value)

print(f"Initial words {total_initial_words}")
print(f"Total patterns on AC trie: {total_initial_words*total_iterations}")
ac = AC.build(t)


#code to measure time for several hits one after another.
start1 = process_time()
for word_to_search in words_to_search:
    start = process_time()
    end = 0
    for id, start, end in ac.match(word_to_search):
        pass
end1 = process_time()
print(f"Took {end1-start1}sec to match {len(words_to_search)} patterns on a AC automaton with {total_initial_words*total_iterations}")


"""
#code to measure average time per hit.
times = list()
for word_to_search in words_to_search:
    start = process_time()
    for id, start, end in ac.match(word_to_search):
        end = process_time()
        times.append(end-start)
print(times)
print(f"Took {mean(times)}sec on average per hit for {len(words_to_search)} patterns")
"""

#Took 0.06114350699999993sec for 25000 patterns
#Took 0.20337147300000002sec for 100000 patterns
#Took 0.38791057500000004sec for 200000 patterns
#Took 0.580509948sec for 300000 patterns

#Took 0.055477443000000015sec to match 25000 patterns on a AC automaton with 63000
#Took 0.05616510200000002sec to match 25000 patterns on a AC automaton with 126000
#Took 0.059204495999999995sec to match 25000 patterns on a AC automaton with 189000
#Took 0.061755475000000004sec to match 25000 patterns on a AC automaton with 315000