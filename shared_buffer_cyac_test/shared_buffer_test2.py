import mmap
import json
import random
from cyac import AC
from memory_profiler import profile


ac_patterns = ["python", "ruby"]
patterns_dict = json.loads(open("static_ioc_sample.json", "r").read())
total_patterns = 0
for x in range(0,1000):
    for key in patterns_dict:
        for value in patterns_dict[key]:
            total_patterns += 1
            ac_patterns.append(value+str(random.randint(0,10000)))
string_to_search = "asdpythonasdasdruby"

# Export to file
ac = AC.build(ac_patterns)
ac.save("ac_trie")
print("Matches before saving:")
for id, start, end in ac.match(string_to_search):
    print(id, string_to_search[start:end])


# Load from file with mmap and share memory
@profile
def load_and_search():
    with open("ac_trie", "r+b") as bf:
        mm = mmap.mmap(bf.fileno(), 0)
    ac_first = AC.from_buff(mm, copy=False)  # it shares memory
    ac_second = AC.from_buff(mm, copy=False)  # it shares memory
    ac_third = AC.from_buff(mm, copy=False)  # it shares memory
    ac_four = AC.from_buff(mm, copy=False)  # it shares memory
    print("Matches after loading shared buffer:")
    for id, start, end in ac_first.match(string_to_search):
        print(id, string_to_search[start:end])

load_and_search()
