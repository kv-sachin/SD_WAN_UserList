def sddevdevice_info():
    import requests
    import time
    import json
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/devices", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz})
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db = json.loads(g)
    items = []
    for item in db:
        items.append(item['name'])
    return "Current running devices are", items
print(sddevdevice_info())


def device_count():
    import requests
    import time
    import json
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/devices", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz})
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db = json.loads(g)
    items = []
    return "running device count is", len(db)
print(device_count())





# SDDEV SITES INFO

def sddevsites_info():
    import requests
    import time
    import json
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/sites", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz})
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db = json.loads(g)
    items = []
    for item in db:
        items.append(item['name'])
    return "Current running sites are", items
print(sddevsites_info())


def sites_count():
    import requests
    import time
    import json
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/sites", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz})
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db = json.loads(g)
    return "running sites count is", len(db)
print(sites_count())



# # SDDEV PLID INFO

def sddevpid_count():
    
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
        items.append(item['plid'])
        indexY= indexY + 1
        
        
    return "Current purchased license ID's are", indexY
    return "Current running pid are", x
    #print(len(db['data'][0]['plid']
    #print(len(db['data'][0]['plid'])
#print(indexY)
#print(sddevdevice_info())
x= sddevpid_count()
print(x)

# # SDDEV USER INFO

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
    code = requests.get("http://sddev.infinitylabs.in/api/users/0", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz})
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db = json.loads(g)
    #print(len(db['data'][0]['plid']
    items = []
    for item in db:
        items.append(item['username'])
        indexY= indexY + 1
        
        
    return "Current active users are", indexY
    return "Current running users are", indexY
    #print(len(db['data'][0]['plid']
    #print(len(db['data'][0]['plid'])
#print(indexY)
#print(sddevdevice_info())
x= sddevuser_count()
print(x)


# # SDDEV INTERFACE INFO

def sddevinterface_info():
    import requests
    import time
    import json
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/licenses/purchase", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz})
    v=code.json()
    i=v['data']
    j=i[0]['Plan']
   
    #print(j)
    return "Current active interfaces are", j
print(sddevinterface_info())


# # SDDEV ACTIVE LICENSE

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
        if item['license']['isActive'] :
            indexY= indexY + 1
        
        
    return "Current Active licenses are", indexY
    return "Current Active licenses are", indexY
    #print(len(db['data'][0]['plid']
    #print(len(db['data'][0]['plid'])
#print(indexY)
#print(sddevdevice_info())
x= sddevactivelicense_count()
print(x)



# # SDDEV DEVICE DETAILS

def sddevdevicedetail_info():
    import requests
    import time
    import json
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/devices/", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz})
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db1 = json.loads(g)
    
    serialNo=db1[0]['serial']
    newURL = "http://sddev.infinitylabs.in/api/devices/"+serialNo
    #print(newURL)
    res1= requests.get(newURL, headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz})
    mess = res1.json()
   
    return "Current device installation detail is", mess['message']
print(sddevdevicedetail_info())



# SDDEV DEVICE STATUS

def sddevdevicestatus_info():
    import requests
    import time
    import json
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/devices/", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz})
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db1 = json.loads(g)
    
    serialNo=db1[1]['serial']
    newURL = "http://sddev.infinitylabs.in/api/devices/"+serialNo
    #print(newURL)
    res1= requests.get(newURL, headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz})
    mess = res1.json()
    message = ''
    isActive = mess['data']['isActive']
    if isActive == '1':
        message = "Device Status is activated"
    else :
        message = "Device is Not Activated"
        
    
    return "Current device activation status is", message
print(sddevdevicestatus_info())



##  SDDEV LICENCSE UPDATE STATUS


def put_info():
    import requests
    import time
    import json
    import collections
    
    slot_serial = request.intent.slots["serialNumber"].value

    
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/devices/", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz})
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db1 = json.loads(g)
    
    serialNo=db1[1]['serial']
    param = {
            'serialNumber': slot_serial,
        }
    newURL = "http://sddev.infinitylabs.in/api/devices/"
    #print(newURL)
    res1 = requests.put(newURL, headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz},data=param)
    #res1= requests.get(newURL, headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz})
    mess = res1.json()
    return mess['message']
    #return "working"
print(put_info())
