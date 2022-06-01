import os
from glob import glob
import MeCab
import pandas as pd
import sqlalchemy as sa
from gensim.models.doc2vec import TaggedDocument
from gensim.models.doc2vec import Doc2Vec


### dbの設定####
user_name = "narou"
password = "naroupass"
host = "db"  # docker-composeで定義したMySQLのサービス名
port = 3306
database_name = "narou_db"




sql_url = f'mysql+pymysql://{user_name}:{password}@{host}:{port}/{database_name}'
engine = sa.create_engine(sql_url, encoding='utf-8', echo=False)

query = "select story from novel_data"
df = pd.read_sql(query,con = engine)
text = df.values.tolist()
print(len(text))


"""
text = []
#家電チャンネル読み込み
for file in glob('kaden-channel/*.txt'):
    with open(file,encoding="utf-8") as f:        
        text.append([f.read()])

l_kaden = len(text)
print('家電チャンネル記事数：',l_kaden)
        
#スポーツウォッチ読み込み
for file in glob('sports-watch/*.txt'):
    with open(file,encoding="utf-8") as f:        
        text.append([f.read()])     

print('スポーツチャンネル記事数：',len(text)-l_kaden)
"""


tagger = MeCab.Tagger("-Ochasen")
text_wakati= []
for w in text:
  print(tagger.parse(w[0]))
"""
for w in text:
  split = tagger.parse(w[0]).split()
  text_wakati.append(' '.join(split))
"""

"""
cnt = 0
doc_train = []
for words in text_wakati:
    doc_train.append(TaggedDocument(words,[cnt]))
    cnt += 1

print("start")

model = Doc2Vec(doc_train, dm=1, vector_size=300, window=10, min_count=1, workers=4)
model.save('doc2vec.model')
"""
