
#%% 读取基础库和函数
import sqlite3
import csv



#%% 打开数据库连接
conn = sqlite3.connect('attck.db')
print("数据库打开成功")
c = conn.cursor()

#%% 创建 tactics 表
c.execute('''CREATE TABLE att_tactics
(id INTEGER PRIMARY KEY,
tatic_id TEXT,
tatic_name TEXT,
matric TEXT
);''')

#%% 创建 techniques 表
c.execute('''CREATE TABLE att_techniques
('id' INT PRIMARY KEY,
tech_id TEXT,
tech_name TEXT,
tatic_id TEXT,
father_tech_id TEXT,
matric TEXT);''')


#%% 插入数据到tatcis表
with open(r'..\assets\attck_database\v13\enterprise_attck\enterprise_tactics.csv',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    data = [row for row in reader]

for row in data:
    c.execute("INSERT INTO att_tactics (tatic_name,tatic_id,matric) VALUES ('{}', '{}', '{}')".format(row[0], row[1], row[2]))

#%% 关闭数据库连接
conn.commit()
conn.close()
# %%
