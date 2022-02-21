import pymysql
import random
import yaml
from datetime import date, datetime, timedelta

with open('connections.yml', "r") as cnt:
    data = yaml.safe_load(cnt)
host = data['cybernet_calls']['host']
user = data['cybernet_calls']['user']
passwd = data['cybernet_calls']['pass']
database = data['cybernet_calls']['database']
db = pymysql.connect(host=host, user=user, passwd=passwd, database=database)
cur = db.cursor(pymysql.cursors.DictCursor)

datetime_pool=('2022-02-05 10:18:37', '2022-02-06 10:18:37', '2022-02-07 10:18:37', '2022-02-08 10:18:37',
               '2022-02-09 10:18:37', '2022-02-10 10:18:37', '2022-02-11 10:18:37', '2022-02-12 10:18:37',
               '2022-02-13 10:18:37')
promise_pool= ('!oper(raschet)', 'another', 'another', 'another')

for count in range(30):
    date = random.choice(datetime_pool)
    date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    promise = random.choice(promise_pool)
    sql =f"INSERT INTO cybernet_calls.xm9wl_calls_details (start_datetime, status, promise, ccuser_id) VALUES ('{date}', 'completed', '{promise}', 355);"
    cur.execute(sql)
    db.commit()


cur.close()
db.close()