import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
dupes = {}
 
def mapper(record):
    # key: document identifier
    # value: document contents
   
   
    key = record[0]
    value = record[1]
    f = sorted([key, value])
    
    mr.emit_intermediate(tuple(f), 1)
    
	
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #total = 0
    person,friend = key
    if len(list_of_values) == 1:
	mr.emit((person, friend))
	mr.emit((friend, person))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)