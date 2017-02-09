import feather
from pandas import DataFrame
path = 'my_data.feather'


with open("./data/u.data") as input:
    line = zip(*(line.strip().split('\t') for line in input))
#print line[0]

#df = DataFrame(line, colums=['user_id' 'item_id', 'rating', 'timestamp'])
data = {'user_id':line[0], 'item_id':line[1], 'rating':line[2], 'timestamp':line[3]}
frame = DataFrame(data)
feather.write_dataframe(frame, path)
