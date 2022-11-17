import json
with open(r'C:\Users\administrator1\Desktop\blibli-ws-master\resources\getDangerEvent_example.json', encoding='utf8') as fp:
    json_data =json.load(fp)
    print(json_data)