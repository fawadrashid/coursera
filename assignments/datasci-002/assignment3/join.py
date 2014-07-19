import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
     
    key = record[1]
    value = record
    #words = value.split()
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    orders = []
    list_items = []    
    
    for o in list_of_values:
      if o[0] == "order": 
        orders.append(o)
      else:
        list_items.append(o)
    #print(list_items)

    for i in list_items:
      mr.emit(orders[0] + i)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper,reducer)
