
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# csv file name 
filename = "data.csv"



with open(filename, 'rb') as f:
     lines = [l.decode('utf8', 'ignore') for l in f.readlines()]
     
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


dataset=[]
for i in range (0,15000):
    dataset.append(lines[i])

target=[]
tweet=[]
for i in range(0,len(dataset)):
    temp=dataset[i].strip()
    target.append(temp[0:temp.index(',')].strip())
    tweet.append(temp[temp.rindex(',')+1:].strip())

ps = PorterStemmer()
    
final_data=[]
bag_of_words=[]
for i in range(0,len(tweet)):
    temp1=[]
    temp2=[]
    tempf=""
    tweet_i=tweet[i].strip()
    w=re.sub('[^a-zA-Z]', ' ',tweet_i)
    temp1=w.split()
    for k in range(0,len(temp1)):
        if temp1[k] not in bag_of_words:
            bag_of_words.append(temp1[k])
    if temp1 not in bag_of_words:
        bag_of_words.append(w)    
    temp2=[ps.stem(word) for word in temp1 if not word in set(stopwords.words('english'))]
    for j in range(0,len(temp2)):
        tempf+=temp2[j]+" "
    final_data.append(tempf)
    print(i)



for i in range(0,len(target)):
    temp_t=target[i]
    target[i]=temp_t.replace("\"","")
    
y=target



