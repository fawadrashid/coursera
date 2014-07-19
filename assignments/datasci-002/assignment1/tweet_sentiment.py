import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def bigrams(text):
    input_list = text.split(' ')
    bigram_list = []
    for i in range(len(input_list)-1):
        bigram_list.append((input_list[i], input_list[i+1]))
    return bigram_list


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    tweetsdata = []
    processedtweets = []
    
    with tweet_file as t:
    	for tweet in t:
        	tweetsdata.append(json.loads(tweet))
    
    
    for tweet in tweetsdata:
	if 'text' in tweet and tweet['text']:
		processedtweets.append(tweet['text'])
		 
		print bigrams(tweet['text'])
		#print tweet['text']	

    scores = {}
    for line in sent_file:
    	term, score  = line.split("\t")  

    	scores[term] = int(score) 
	#print scores[term]
	lines = term
	#print str(lines) .str(scores[term])
	#print  str(scores[term])
	#json.loads(lines)
	#print str(lines).split(',')
	#print ','.join(str(i) for i in lines) 
	#print lines.split(",")
    	#print '\n' .scores.items()

   


if __name__ == '__main__':
    main()
