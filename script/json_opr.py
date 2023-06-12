#%% 加载库
import json

rdata = '''

 {
  "type": "bundle",
  "id": "bundle--5c150c1d-d85c-4c50-b4dd-88e4b88a15c5",
  "objects": [
    {
      "a": [1,2,3],
      "b": "B",
      "c": "C",
      "d": [
        {
          "a": "d-0",
          "d-1": "d-1",
          "d-2": "d-2"
        },
        {
          "a": "d-0-2",
          "d-1": "d-1-2",
          "d-2": "d-2-2"
        }
      ]
    },
    {
        "a": [4,5,6],
        "b": "B2",
        "c": "C2",
        "d": [
          {
            "a": "d2-0",
            "d-1": "d2-1",
            "d-2": "d2-2"
          }
        ]
      }
  ],
  "name": {
    "a": [7,8,9],
    "b": "B3",
    "c": "C3",
    "d": [
      {
        "a": "d3-0",
        "d-1": "d3-1",
        "d-2": "d3-2"
      }
    ]
  }
  }
'''

#%% 解析json输出所有type字段的内容，并去重
with open(r'..\assets\attck_database\v13\enterprise_attck\raw.githubusercontent.com_mitre_cti_ATT%26CK-v13.1_enterprise-attack_enterprise-attack.json', 'r',encoding='utf-8') as f:
    data = json.load(f)

#%% 解析出objects对象中所有的tpye值
results = [item['type'] for item in data['objects']]

#%% 解析出objects对象中type为指定内容的对象，并输入name值
results = [item['name'] for item in data['objects'] if item['type'] == 'tool']

#%% 输出去重的result
print(list(set(results)))


# %% test
data = json.loads(rdata)
objects = data['objects']

result = [obj['d'][0]['a'] for obj in objects]

print(result)

# %%
