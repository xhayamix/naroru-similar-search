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

tagger = MeCab.Tagger("-Ochasen")
text_wakati= []

for w in text:
    str = []
    for d in tagger.parse(w[0]).splitlines():
        if len(d) > 2:
            str.append(d.split()[0])
    text_wakati.append(str)

"""
for w in text:
    text_wakati.append([d.split()[0] for d in tagger.parse(w[0]).splitlines()])
"""    

"""
for w in text:
  print(tagger.parse(w[0]))
"""

documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(text_wakati)]

print("start")

#print(text_wakati[0])

model = Doc2Vec(documents, dm=0, vector_size=150, window=10, min_count=3, workers=4)
model.save('doc2vec.model')

