# _*_ coding:utf-8 _*_
import random
import time

# 构造表t_user_weight
def create_t_user_weight():
    start = time.time()
    # 定义需要生成的数据量
    count = 10000 # 1千万
    beginID = 2020031
    # 打开文件，并动态生成sql数据，将数据存在文件中
    try:
        with open("./insert_t_user_weight.txt", "wb") as fo:
            length = count + 1
            for i in range(1, length):
                # 定义数据，以下只是测试数据，可以根据自己的业务通过调用函数去随机生成对应的值
                id = str(i)
                userId = str(beginID + i)
                name = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 4)).replace('', '')
                sex = str(random.choice(['男', '女']))
                weight = str(random.randrange(10, 99))
                address = str(random.choice(['北京', '上海', '深圳', '广州', '杭州']))
                insert_t_user_weight = (
                    "INSERT INTO t_user_weight VALUES ('%s', '%s', '%s','%s', '%s', '%s', '%s');"
                    % (id, userId, name, sex, weight, address, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                )
                insert_t_user_weight = insert_t_user_weight + '\n'
                # print(insert_t_user_weight)
                fo.write(insert_t_user_weight.encode('UTF-8'))
            print('共创建1千万条sql耗时：', time.time() - start)
    except Exception as e:
        print(Exception, ":", e)

if __name__ == "__main__":
    create_t_user_weight()