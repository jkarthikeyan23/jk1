filename=("path\para.txt")
withopen(filename,'r')as file:
lines_in_file=file.read()
print lines_in_file
import nltk
filename=("path\para.txt")
with open(filename,'r')as file:
lines_in_file=file.read()
nltk_tokens=nltk.word_tokenize(lines_in_file)
print nltk_tokens
print"\n"
print "number of words:",len(nltk_tokens)
