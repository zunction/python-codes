import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from sys import argv
script, filename = argv
f = open(filename,'r')

words=[]

for line in f:
 try:
  temp = line.split(': ')[2];
  if('Media' not in temp): # If any form of media is sent, WhatsApp prints "<Media Omitted>". Getting rid of this. TO DO: Improve this functionality. 
   print temp 
   words.append(temp)
 except:
	print " "
f.close()

#print words


data = ' '.join(words)

wc = WordCloud(
                      stopwords=STOPWORDS,
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(data)
plt.axis('off')
plt.imshow(wc)
plt.savefig('wordcloud.png', dpi=300)					 
