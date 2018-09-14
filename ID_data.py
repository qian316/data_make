# _*_ coding:utf-8 _*_
import python_snowflake
from concurrent import futures

# 在其他py文件中调用雪花算法的类
# 以后可以找下有没类似的包，或者是自己整理一个包

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
    futs = [executor.submit(gen_id) for _ in range(10)]

print('{0} IDs in the list'.format(len(id_list)))
print(type(id_list))
for i in range(1,10):
    print(id_list[i])
