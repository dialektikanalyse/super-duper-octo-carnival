import sqlite3
import threading
import datetime
db = sqlite3.connect('baza.db', check_same_thread=False)
sql = db.cursor()
#print(max(list(buys_id for buys_id in sql.execute(f"SELECT id FROM buys"), key=lambda i: int(i)))
#print([buys_id for buys_id in sql.execute(f"SELECT id FROM buys")])
sql.execute(f"SELECT name, SUM(price) FROM buys WHERE date >= '2021-12-21' AND date <= '2021-12-21' AND tovarid = 1")
# print(list(sql.fetchone())[1])
db.commit()
current_time = str(datetime.date.today())
print(datetime.date(int(current_time.split('-')[0]),1,1))