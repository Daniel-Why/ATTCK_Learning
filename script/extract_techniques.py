# 从json中提取techniqueID,tactic
import json
import csv

with open(r'assets\attck_database\v13\enterprise_attck\ics_attack_2023_5.json', 'r') as f:
    data = json.load(f)

techniques = data['techniques']

with open('ics_attack_2023_5.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['techniqueID', 'tactic'])
    for technique in techniques:
        writer.writerow([technique['techniqueID'], technique['tactic']])
