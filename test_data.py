# _*_ coding:utf-8 _*_
import json
import time

i = 5
t=2
while (i  < 6 ):
    lineCode_test = "data" + str(i)
    #sourName = "sync_test_source" + str(i)
    targName = "sync_test_targer" + str(i)
    script = {"frequency": 1, ""
                              "lineCode": lineCode_test,
              "source": "source",
              "sql": {"columns":
                          [{"isPk": 1 ==1 ,
                            "souFieldName": "Id",
                            "tarFieldName": "Id"},
                           {"isPk": 1 != 1,
                            "souFieldName": "Name",
                            "tarFieldName": "Name"}
                           ],
                      "foreignKey": "",
                      "parentKey": "",
                      "parentTableName": "",
                      "query": "select Id,Name from " + targName  + " where timestamp >  #{timestamp} order by timestamp limit 3000",
                      "souName": targName,
                      "tarName": targName},
              # "target": "target", 单站点，一对一
              "target": "target",  # 多站点，一对多
              "version": float(i)}
    j = json.dumps(script)
    # print(j)
    with open("test.txt", "a+", encoding="utf-8") as f:
        # f.truncate()
        f.write( str(t) + '|'+ lineCode_test +'|'+ str(i) +'|'+ j + '\n')
    i += 1


#time.sleep(3)


# 清除test.txt数据，方便调试
# # with open("test.txt", "w", encoding="utf-8") as f:
# #     pass