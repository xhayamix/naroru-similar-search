#『なろう小説API』を用いて、なろうの『全作品情報データを一括取得する』Pythonスクリプト
#2020-04-26更新
import requests
import pandas as pd
import json
import time as tm
import datetime
import gzip
from tqdm import tqdm
tqdm.pandas()
import sqlalchemy as sa
from time import sleep

from gensim.models.doc2vec import TaggedDocument
from gensim.models.doc2vec import Doc2Vec
import MeCab


import numpy as np
import schedule

### dbの設定####
user_name = "narou"
password = "naroupass"
host = "db"  # docker-composeで定義したMySQLのサービス名
port = 3306
database_name = "narou_db"

#リクエストの秒数間隔(1以上を推奨)
interval = 2
### なろう小説API・なろう１８禁小説API を設定 ####
is_narou = True
now_day = datetime.datetime.now()
now_day = now_day.strftime("%Y_%m_%d")
if is_narou:
    filename = 'Narou_All_OUTPUT_%s.xlsx'%now_day
    sql_filename = 'Narou_All_OUTPUT_%s.sqlite3'%now_day
    sql_url = f'mysql+pymysql://{user_name}:{password}@{host}:{port}/{database_name}'
    api_url="https://api.syosetu.com/novelapi/api/"    
else:
    filename ='Narou_18_ALL_OUTPUT_%s.xlsx'%now_day
    sql_filename = 'Narou_18_ALL_OUTPUT_%s.sqlite3'%now_day
    sql_url = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
    api_url="https://api.syosetu.com/novel18api/api/"
# データをSqlite3形式でも保存する

engine = sa.create_engine(sql_url, encoding='utf-8', echo=False)


#####　以上設定、以下関数　##############
    
#全作品情報の取得
def get_all_novel_info():
       
    df = pd.DataFrame()
    
    payload = {'out': 'json','gzip':5,'of':'n','lim':1}
    res = requests.get(api_url, params=payload).content
    r =  gzip.decompress(res).decode("utf-8") 
    allcount = json.loads(r)[0]["allcount"]
    print('対象作品数  ',allcount);
    
    
    all_queue_cnt = (allcount // 500) + 10

    #現在時刻を取得
    nowtime = datetime.datetime.now().timestamp()
    lastup = int(nowtime)
                     
    for i in tqdm(range(all_queue_cnt)):
        payload = {'out': 'json','gzip':5,'of':'t-n-u-w-s-g-k-gf-gl-nt-e-ga-l-ti-gp-dp-wp-mp-qp-yp-f-nu','lim':500,'lastup':"1073779200-"+str(lastup)}
        #print(payload)
        
        # なろうAPIにリクエスト
        cnt=0
        while cnt < 5:
            try:
                res = requests.get(api_url, params=payload, timeout=30).content
                break
            except:
                print("Connection Error")
                cnt = cnt + 1
                tm.sleep(120) #接続エラーの場合、120秒後に再リクエストする
            
        r =  gzip.decompress(res).decode("utf-8")   
    
        # pandasのデータフレームに追加する処理
        df_temp = pd.read_json(r)

        df_temp = df_temp.drop(0)
        df = pd.concat([df, df_temp])
        
        last_general_lastup = df.iloc[-1]["general_lastup"]
        lastup = datetime.datetime.strptime(last_general_lastup, "%Y-%m-%d %H:%M:%S").timestamp()
        lastup = int(lastup)
        #print(lastup)
        
        #取得間隔を空ける
        tm.sleep(interval)
        
        df['searchbykey'] = df['title'] + df['story'] + df['keyword']
        
        create_model(df)
        dump_to_sql(df)
        
        
        
def dump_to_sql(df):
    df = df.drop("allcount", axis=1)
    # 重複行を削除する
    df.drop_duplicates(subset='ncode', inplace=True)
    df = df.reset_index(drop=True)
    df.index = df.index + 1

    #df = df["keyword"]
    
    #print(df['searchbykey'])
    df.to_sql('novel_data', engine, index=True, method = "multi",chunksize = 10000 ,if_exists='replace')
    
    #indexをはる
    con = engine.connect()
    
    #con.execute("create index id_index on novel_data(`index`);")
    con.execute("create index ncode_index on novel_data(ncode(8));")
    
    
    con.close()
    
    
def create_model(df):
    df_model = df["story"]
    text = df_model.values.tolist()
    #print(text[0])
    
    tagger = MeCab.Tagger("-Ochasen")
    text_wakati= []

    for w in text:
        str = []
        for d in tagger.parse(w[0]).splitlines():
            if len(d) > 2:
                str.append(d.split()[0])
        text_wakati.append(str)
        
    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(text_wakati)]

    print("start")

    #print(text_wakati[0])

    model = Doc2Vec(documents, dm=0, vector_size=150, window=10, min_count=3, workers=4)
    model.save('doc2vec.model')
    
    
def task():
    print("start",datetime.datetime.now())
    get_all_novel_info()
    print("end",datetime.datetime.now())
    
schedule.every(10).seconds.do(task)
    
#######　関数の実行を指定　##########
task()

"""
while True:
    schedule.run_pending()
    sleep(1)
"""