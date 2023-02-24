import json
from requests import request

def save_info(filename, rates):
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))

def check_steps(s):
    a = json.loads(s)
    save_info(a['timestamp'],a['rates'])
    return a['rates']['IRR']

def get_data(s,t):
    print(check_steps(t)) if s == 200 else print("connection lost")

def req(api_key,url,payload):
    headers= {"apikey": api_key}
    response = request("GET", url, headers=headers, data = payload)
    get_data(response.status_code, response.text)

def req_handler():
    base_money='USD'
    change_to='IRR'
    api_key="VxXok9NmJBnkCP6dM5SUfybMPpa0pFKw"
    url = "https://api.apilayer.com/fixer/latest?symbols="+change_to+"&base="+base_money
    payload = {}
    req(api_key,url,payload)
