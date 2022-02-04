import argparse
from typing import List

from pyspark import SparkContext, SparkConf


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()

    return args


def remove_symbols(line) -> List[str]:
    symbols = ['.', ',', ':', '!', '?', '-', ';', '_', '(', ')', "'"]
    
    for symbol in symbols:
        line = line.replace(symbol, '')
        
    return line


def split_in_words(line) -> List[str]:
    line = line.lower().split()
    line = [x for x in line if not x.isdigit()]

    return line


if __name__ == '__main__':
    conf = SparkConf().setAppName('Bible word counter').setMaster('local')
    sc = SparkContext(conf=conf)

    bible = sc.textFile('bible.txt')

    clean_bible = bible.map(remove_symbols)

    bibleWords = clean_bible.flatMap(split_in_words)

    not_necessery_words = ['or', 'and' ,'the', 'of', 'in', 'be', 'to', 'a', 'is']
    pairs = bibleWords.filter(lambda x: x not in not_necessery_words) \
        .map(lambda word: (word, 1))
    
    wordCount = pairs.reduceByKey(lambda a, b: a + b) \
        .sortBy(lambda x: x[1], ascending=False)
    
    print(wordCount.take(15))
