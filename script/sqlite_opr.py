
#%% 读取基础库和函数
import sqlite3
import csv



#%% 打开数据库连接
conn = sqlite3.connect(r'..\assets\attck_database\v13\sqlite_db\attck.db')
print("数据库打开成功")
c = conn.cursor()

#%% 创建 tactics 表
c.execute('''CREATE TABLE att_tactics
( `id` INTEGER PRIMARY KEY,
tactic_id TEXT,
tactic_name TEXT,
matric TEXT
);''')

#%% 创建 techniques 表
c.execute('''CREATE TABLE att_techniques
(`id` INTEGER PRIMARY KEY,
tech_id TEXT,
tech_name TEXT,
tactic_id TEXT,
father_tech_id TEXT,
matric TEXT);''')


#%% 插入数据到tatcis表
with open(r'..\assets\attck_database\v13\enterprise_attck\enterprise_tactics.csv',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    data = [row for row in reader]

for row in data:
    c.execute("INSERT INTO att_tactics (tactic_name,tactic_id,matric) VALUES ('{}', '{}', '{}')".format(row[0], row[1], row[2]))




#%% 插入数据到techniques表
with open(r'..\assets\attck_database\v13\enterprise_attck\enterprise_techniques.csv',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    data = [row for row in reader]

n = 0
for row in data:
    tactics_list=row[2].split(",")
    n+=1
    for tt_name in tactics_list:
        tt_id_list = c.execute(" SELECT tactic_id FROM att_tactics WHERE tactic_name like '{}' ".format(tt_name))
        tt_id = tt_id_list.fetchall()[0][0]
        c.execute("INSERT INTO att_techniques (tech_id,tech_name,tactic_id,matric) VALUES ('{}', '{}', '{}','{}')".format(row[0], row[1],tt_id, row[3])) 
        print(n)

#%% 找出sub_tech的父级
# 找出所有父级tech
father_tech = c.execute("SELECT tech_id FROM att_techniques WHERE tech_id NOT LIKE '%.%'")
for f_t in father_tech.fetchall():
    #print(f_t[0])
    sub_tech = c.execute("SELECT tech_id FROM att_techniques WHERE tech_id LIKE '{}.%'".format(f_t[0]))
    for s_t in sub_tech.fetchall():
        c.execute("UPDATE att_techniques set father_tech_id = '{}' where tech_id = '{}'".format(f_t[0],s_t[0]))

#%% 删除表
# c.execute("DROP TABLE att_techniques")

#%% 关闭数据库连接
conn.commit()
conn.close()
# %%
