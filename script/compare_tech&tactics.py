import pandas as pd

# 读取csv文件并命名列名为'tech_id'和'tactics'
df = pd.read_csv(r'assets\attck_database\v13\enterprise_attck\enterprise_attack_2023_5.csv', header=None, names=['tech_id','tactics'])

# 使用groupby方法按照Letter列进行分组，并将结果连接为字符串
result = df.groupby('tech_id')['tactics'].apply(','.join).reset_index()

# 将处理好的数据保存为csv文件
result.to_csv('result.csv', index=False)

# 打印整理后的结果
print(result.to_string(index=False))
