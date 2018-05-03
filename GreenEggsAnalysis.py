from collections import defaultdict
import pandas as pd

f = open('GreenEggsAndHam.txt', 'r') #
text_list = f.readlines()

word_freq = defaultdict(int)

for text in text_list:
    for word in text.split():
        word_freq[word] += 1

pd.DataFrame.from_dict(word_freq,orient='index').sort_values(0,ascending = False)
