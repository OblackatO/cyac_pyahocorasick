import mmap
import time
import json
import random
from cyac import AC
from memory_profiler import profile
from multiprocessing import Process
from multiprocessing import shared_memory


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
# Force garbage collector, to avoid possible copy to child processes.
string_to_search = None  
ac = None
ac_patterns = None

# Load from file with mmap and share memory
with open("ac_trie", "r+b") as bf:
    mm = mmap.mmap(bf.fileno(), 0)
ac_first = AC.from_buff(mm, copy=False)
ac_size = ac_first.buff_size()
print("Size of AC automaton:Total patterns: {}bytes:{}patterns".format(ac_size, total_patterns))
ac_first = None # Force garbage collector.

# Function used by the children processes.
@profile
def get_shared_memory_find_matches(processname, shared_memory_tag, ac_size):
    shm = shared_memory.SharedMemory(shared_memory_tag)
    AC_in_bytes = shm.buf[0:ac_size]
    ac_in_process = AC.from_buff(AC_in_bytes, copy=False)
    string_to_search = "asdpythonasdasdruby"
    print("Executing search in {}".format(processname))
    for id, start, end in ac_in_process.match(string_to_search):
        print(id, string_to_search[start:end])
    #time.sleep(100)
    ac_in_process = None
    AC_in_bytes.release() # MUST release memory beforing closing shm insance, otherwise error is raised.
    shm.close()
    
if __name__ == "__main__":
    shared_memory_tag = "shared_ac"
    # Put mm in shared memory of py3.8
    shm = shared_memory.SharedMemory(name=shared_memory_tag, create=True, size=ac_size)
    shm.buf[0:ac_size] = mm
    mm.close()
    processes_list = list()
    for x in range(0, 6):
        p = Process(
            target=get_shared_memory_find_matches,
            args=(
                "process_" + str(x),
                shared_memory_tag,
                ac_size
            )
        )
        p.start()
        processes_list.append(p)
    for p in processes_list:
        p.join()
    #input()
    shm.unlink()