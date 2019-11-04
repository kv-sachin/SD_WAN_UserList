def sddevuser_count():
    
    import requests
    import time
    import json
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    indexY = 0
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/users/0", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db = json.loads(g)
    #print(len(db['data'][0]['plid']
    items = []
    for item in db:
        items.append(item['username'])
        indexY= indexY + 1
        
        
    
    return "Current running users are", indexY
   
#print(indexY)
#print(sddevdevice_info())
#x= sddevuser_count()
print(sddevuser_count())
