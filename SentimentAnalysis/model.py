import pandas as pd
import pickle
import requests
import codecs

url = 'http://localhost:8000/liste'
headers = {'content-type': 'application/json'}

#servise istek atılır ve dönen json verisi ile dataset oluşturulur.
response = requests.get(url)
json_data = {}
j = 0
f = codecs.open("data.csv", "w", "utf-8")
f.write("yorum,Positivity\n")
for i in response.json():
    j = j + 1
    json_data[j] = response.json()["{}".format(j)]
    f.write(json_data[j]["commint"]+ "," + str(json_data[j]["star"]) + "\n")
    
#Veri setinin eklenip başlığının belirlenmesi
column = ['yorum']
df = pd.read_csv('data.csv', encoding ='utf8', sep=',')

#df.dropna(inplace=True)

#Veri setindeki Türkçe dolgu kelimelerinin kaldırılması
def remove_stopwords(df_fon):
    stopwords = open('turkce-stop-words', 'r').read().split()
    df_fon['stopwords_removed'] = list(map(lambda doc:
        [word for word in doc if word not in stopwords], df_fon['yorum']))

remove_stopwords(df)


X = df['yorum']
y = df['Positivity']

#Şimdi, verileri "yorum" ve "Positivity" sütunlarını kullanarak rastgele eğitim ve test alt kümelerini bölüştürelim ve 
#ardından ilk girişi 
#CountVectorizer'ı başlatıyoruz ve eğitim verilerimize uyguluyoruz.
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(encoding ='iso-8859-9').fit(X)
pickle.dump(vect, open('vect.pkl', 'wb'))
#X_train'deki belgeleri bir belge terim matrisine dönüştürürüz
X_vectorized = vect.transform(X) 

#Bu özellik matrisi X_ train_ vectorized'e dayanarak Lojistik Regresyon sınıflandırıcısını eğiteceğiz
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_vectorized, y)

pickle.dump(model, open('model.pkl','wb'))