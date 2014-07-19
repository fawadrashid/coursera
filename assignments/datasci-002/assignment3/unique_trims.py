import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
dupes = {}
 
def mapper(record):
    # key: document identifier
    # value: document contents
   
   
    sequence_id = record[0]
    nucleotides = record[1]
    nucleotides_trimed = nucleotides[:-10]
    
    mr.emit_intermediate(nucleotides_trimed, sequence_id)
    
	
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #total = 0
    
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)