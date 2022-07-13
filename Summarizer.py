# load libraries
import nltk
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.nlp.stemmers import Stemmer

# define function for extracting and summarizing text from web articles
def summarizer(url,sentence_count):
    LANGUAGE = "english"
    SENTENCE_COUNT = sentence_count
    
    url = url
    
    parser = HtmlParser.from_url(url,Tokenizer(LANGUAGE))

    summarizer = LuhnSummarizer()
    summarizer = LuhnSummarizer(Stemmer(LANGUAGE))
    summarizer.stop_words = ("I","am","the","you","are","me","is","than","that")
    
    for sentence in summarizer(parser.document,SENTENCE_COUNT):
    
        print(sentence)
