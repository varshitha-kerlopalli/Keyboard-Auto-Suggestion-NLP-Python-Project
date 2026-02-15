import numpy as np
import pandas as pd
import textdistance 
from collections import Counter
import re

#file cleaning and changing format

words = []
with open('autocorrect book.txt','r',encoding='utf-8') as f:
    data = f.read()
    data = data.lower()
    word = re.findall(r'\w+', data)
    words +=word

#Build vocabulary
V = set(words)

#Build the frequency of those words
word_freq_dict = Counter(words)

#Calculating relative frequency of the words in the vocabulary
Total_words_freq = sum(word_freq_dict.values())


probs = {}
for k in word_freq_dict.keys():
    probs[k] = word_freq_dict[k] / Total_words_freq

#Function to find similar words
def autocorrect(word):
    word = word.lower()
    
    if word in word_freq_dict:
        print('The word is already correct:', word)
    else:
        
        jaccard = textdistance.Jaccard(qval=2)
        
        
        similarities = [1 - jaccard.distance(w, word) for w in word_freq_dict.keys()]
        
        
        df = pd.DataFrame({
            'Word': word_freq_dict.keys(),
            'Prob': [word_freq_dict[w] for w in word_freq_dict.keys()],
            'Similarity': similarities
        })
        
        
        output = df.sort_values(['Similarity', 'Prob'], ascending=False).head(10)
        return output
    
#Printing out similar words
print(autocorrect('whe'))