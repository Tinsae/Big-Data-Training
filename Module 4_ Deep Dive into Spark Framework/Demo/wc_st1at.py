import sys
from pyspark import SparkContext, SparkConf

if __name__ == '__main__':
    # create SparkContext with SparkConf
    conf = SparkConf().setAppName("Edureka_121039 - WordCount")
    sc = SparkContext(conf=conf)
    
    # read in text file and split each document into words
    words = sc.textFile('/user/edureka_121039/sample.txt').flatMap(lambda line: line.split(' '))
    
    # count occurences of each word
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda x, y: x + y)
    
    wordCounts.saveAsTextFile('/user/edureka_121039/output/')