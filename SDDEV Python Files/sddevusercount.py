def sddevactivelicense_count():
    
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
    code = requests.get("http://sddev.infinitylabs.in/api/licenses", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz})
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db = json.loads(g)
    #print(len(db['data'][0]['plid']
    items = []
    for item in db:
        items.append(item['isActive'])
        indexY= indexY + 1
        
        
    return indexY
    return "Current running Active licenses are", indexY
    #print(len(db['data'][0]['plid']
    #print(len(db['data'][0]['plid'])
#print(indexY)
#print(sddevdevice_info())
x= sddevactivelicense_count()
print(x)
