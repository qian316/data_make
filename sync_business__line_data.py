# _*_ coding:utf-8 _*_
import pymysql
import python_snowflake
from concurrent import futures

# mysql数据库连接配置
conn = pymysql.connect(
     host = "localhost",
     user = "user",
     password = "password",
     database = "database",
     charset = "utf8",
     cursorclass = pymysql.cursors.DictCursor)

# 雪花ID
id_list = list()
snowflake = python_snowflake.Snowflake(1)

def gen_id():
    try:
        _id = snowflake.generate()
    except Exception as e:
        print(e)
    else:
        assert _id not in id_list
        id_list.append(_id)

with futures.ThreadPoolExecutor(max_workers=16) as executor:
    futs = [executor.submit(gen_id) for _ in range(11)]



# 插入数据
try:
    with conn.cursor() as cursor:
        values = []
        sql = "INSERT INTO `sync_business_line`  VALUES (%s, %s, %s, %s ,%s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        for i in range(1, 1001):
            values.append((i, 'test1', 'wsp_data' + str(i), 1,2,0,1,1,1.0,0,123,1, 0,0 ,0,'2018-08-23 20:44:35',4666033844311900100,'admin','2018-08-27 17:52:32',4666033844311900100,'admin',0,'2018-08-27 17:52:33',0,0,0))
            # 插入雪花ID
            # values.append((id_list[i], 'test1', 'wsp_data' + str(i), 1,2,0,1,1,1.0,0,123,1, 0,0 ,0,'2018-08-23 20:44:35',4666033844311900100,'admin','2018-08-27 17:52:32',4666033844311900100,'admin',0,'2018-08-27 17:52:33',0,0,0))
        cursor.executemany(sql, values)

        conn.commit()
finally:
    conn.close()

# 清空表数据
# cursor = conn.cursor()
# trun = "TRUNCATE  sync_business_line "
# cursor.execute(trun)
# conn.commit()
# cursor.close()
# conn.close()



