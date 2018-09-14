# _*_ coding:utf-8 _*_
import pymysql
import time

# mysql数据库连接配置
conn = pymysql.connect(
     host = "localhost",
     user = "user",
     password = "password",
     database = "database",
     charset = "utf8",
     cursorclass = pymysql.cursors.DictCursor)

# 建立表和删除表,单表逻辑
try:
   with conn.cursor() as cursor:
        cursor = conn.cursor()

        i = 1
        values = []
        sql = """CREATE TABLE `sync_test_targer%s` (
                `Id` bigint(20) NOT NULL ,
                `Name` varchar(50) NOT NULL,
                `timestamp` timestamp NULL DEFAULT NULL,
                PRIMARY KEY (`Id`),
                KEY `timestamp`(`timestamp`)
                ) ENGINE=InnoDB AUTO_INCREMENT=2147483647 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;"""
        # sql_drop = "DROP TABLE `sync_test_targer%s`;"
        for i in range(1,1001):
                 values.append(i)

        cursor.executemany(sql,values)

        # cursor.executemany(sql_drop,values)
        conn.commit()

finally:
    pass
#
# #
# # time.sleep(2)
#
# # 写入一个表多条数据
# #
# # values 作用域的问题......values习惯性放在全局中,坑
try:
    with conn.cursor() as cursor:
        ticks = time.time()
        i = 1
        j = 1
        for i in range(1,1001):
            for j in range(1,1001):
                values = []
                ticks = ticks + 1
                time_local = time.localtime(ticks)
                dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                sql_data = "INSERT INTO sync_test_targer{}  VALUES (%s ,%s ,%s );".format(i)
                values.append((j,j,dt))
                cursor.executemany(sql_data,values)
            conn.commit()

finally:
        conn.close()


# # 清空表数据
# cursor = conn.cursor()
# i = 1
# for i in range(1,1001 ):
#     trun = "TRUNCATE  sync_test_targer{} ".format(i)
#     cursor.execute(trun)
# conn.commit()
# cursor.close()
# conn.close()

# ticks = time.time()
# ticks = ticks + 1500000
# time_local = time.localtime(ticks)
# dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
# print(dt)