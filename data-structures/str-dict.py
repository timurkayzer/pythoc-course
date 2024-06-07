import string
from collections import defaultdict

trans_table = str.maketrans('','',string.punctuation)
target_string = "this is text which is long enough, for the exercise"
target_string = target_string.translate(trans_table)
result = defaultdict(int)
for word in target_string.split(' '):
    word = word.lower()
    result[word]+=1

print(result)