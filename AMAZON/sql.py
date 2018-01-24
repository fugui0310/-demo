import pymysql
from . import settings


MYSQL_HOST=settings.MYSQL_HOST
MYSQL_PORT=settings.MYSQL_PORT
MYSQL_USER=settings.MYSQL_USER
MYSQL_PWD=settings.MYSQL_PWD
MYSQL_DB=settings.MYSQL_DB

conn=pymysql.connect(
    host=MYSQL_HOST,
    port=int(MYSQL_PORT),
    user=MYSQL_USER,
    password=MYSQL_PWD,
    db=MYSQL_DB,
    charset='utf8'
)
cursor=conn.cursor()

class Mysql(object):
    @staticmethod
    def insert_tables_goods(goods_name,goods_price,deliver_mode):
        sql='insert into goods(goods_name,goods_price,delivery_method) values(%s,%s,%s)'
        cursor.execute(sql,args=(goods_name,goods_price,deliver_mode))
        conn.commit()

    @staticmethod
    def is_repeat(goods_name):
        sql='select count(1) from goods where goods_name=%s'
        cursor.execute(sql,args=(goods_name,))
        if cursor.fetchone()[0] >= 1:
            return True

if __name__ == '__main__':
    cursor.execute('select * from goods;')
    print(cursor.fetchall())