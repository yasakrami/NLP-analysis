import requests
import nltk
from matplotlib import pyplot as plt
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import pandas as pd
nltk.download('stopwords')
nltk.download('brown')
print('a:')
response_1 = requests.get('https://www.python.org')
soup_1 = BeautifulSoup(response_1.content,'html5lib')
text_1 = soup_1.get_text(strip=True)
stopwords = set(stopwords.words('english'))
cloud = WordCloud(collocations=False,  background_color='white', stopwords=stopwords, contour_color='firebrick').generate(text_1)
plt.imshow(cloud)
plt.axis('off')
plt.show()

print('b:')
from textblob import TextBlob
response.content
textblob = TextBlob(text1)  
print('Noun Phrases', '\n', textblob.noun_phrases, '\n')
blobword = [word for word in textblob.words if word not in stopwords]
blob_sent = textblob.sentences
print('Blob Word', '\n', blobword, '\n')
print('Blob Sentences', '\n', blob_sent)

print('c:')
import requests
import nltk
from matplotlib import pyplot as plt
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import pandas as pd
response_2 = requests.get('https://edition.cnn.com/2022/01/24/europe/thomas-pesquet-iss-climate-change-c2e-scn-spc-intl/index.html')#new
response_2.content
soup_2 = BeautifulSoup(response_2.content,'html5lib')
text_2 = soup_2.get_text(strip=True)
textblob2 = TextBlob(text_2)
sentimate_anls= textblob2.sentiment
sent = textblob2.sentences
snt=[]
textblob_senti=[]
for i in sent:
    snt.append(i)
for s in snt:
    polar= s.sentiment.polarity
    subject= s.sentiment.subjectivity
    if polar>0:
        c='positive'
    else:
        c= 'negative'
    textblob_senti.append([s,a,b,c])
df_textblob = pd.DataFrame(textblob_sentiment, columns =['Sentence', 'Polarity', 'Subjectivity', 'c'])
print('sentiment analysis for the text:', sentimate_anls)
print('sentiment analysis for each sentence', df_textblob)



print('d:')
from textblob.sentiments import NaiveBayesAnalyzer
nltk.download('movie_reviews')
text_blob_Naive = TextBlob(text2, analyzer=NaiveBayesAnalyzer())
print(text_blob_Naive.sentiment)


print('e:')
import spacy
from spacy import displacy
nlp = spacy.load('en') 
nlp = spacy.load('en_core_web_md')
nlp.max_length = 1500000
response_2 = requests.get('https://edition.cnn.com/2022/01/24/europe/thomas-pesquet-iss-climate-change-c2e-scn-spc-intl/index.html')#new
response_2.content
soup_2 = BeautifulSoup(response_2.content,'html5lib')
text_2 = soup_2.get_text(strip=True)
textblob2 = TextBlob(text_2)
text_3 = nlp(text_2)
for entity in text3.ents:
    print(f'{entity.text}: {entity.label_}')


print('f:')
import spacy
from spacy import displacy
import requests
import nltk
n = spacy.load('en_core_web_md') 
response_3 = requests.get('https://edition.cnn.com/2022/06/24/investing/crypto-hack/index.html') 
response_4 = requests.get('https://edition.cnn.com/2022/06/24/investing/dow-stock-market-today/index.html')
response_5 = requests.get('https://edition.cnn.com/2022/06/23/economy/china-tariffs-inflation-gary-cohn/index.html')
response_6 = requests.get('https://edition.cnn.com/2022/06/23/business/inflation-convenience-store-shopping-arko/index.html')
soup_3 = BeautifulSoup(response3.content,'html5lib')
soup_4 = BeautifulSoup(response4.content,'html5lib')
soup_5 = BeautifulSoup(response5.content,'html5lib')
soup_6 = BeautifulSoup(response6.content,'html5lib')
text_4 = soup3.get_text(strip=True)
text_5 = soup4.get_text(strip=True)
text_6 = soup5.get_text(strip=True)
text_7 = soup6.get_text(strip=True)
nlp = spacy.load('en') 
nlp = spacy.load('en_core_web_md')
nlp.max_length = 1500000
document = nlp(text_4)
document1 = nlp(text_5)
document2 = nlp(text_6)
document3 = nlp(text_7)
listt = [document, document1, document2, document3]
print('document1 and document2 relation:', document.similarity(document_2))

print('document1 and document3 relation:',document.similarity(document_3))

print('document1 and document4 relation:',document.similarity(document_4))

print('document2 and document3 relation:',document1.similarity(document_3))

print('document2 and document4 relation:',document1.similarity(document_4))

print('document3 and document4 relation:',document2.similarity(document_4))


