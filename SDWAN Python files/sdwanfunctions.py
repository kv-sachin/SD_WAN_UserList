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
    code = requests.get("http://sddev.infinitylabs.in/api/devices", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db = json.loads(g)
    items = []
    for item in db:
        items.append(item['name'])
    return "Current active devices are", items
print(sddevdevice_info())


# # DEVICE COUNT

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
    code = requests.get("http://sddev.infinitylabs.in/api/devices", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
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
    code = requests.get("http://sddev.infinitylabs.in/api/sites", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db = json.loads(g)
    items = []
    for item in db:
        items.append(item['name'])
    return "Current active sites are", items
print(sddevsites_info())





# ### SITES COUNT



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
    code = requests.get("http://sddev.infinitylabs.in/api/sites", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
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
    code = requests.get("http://sddev.infinitylabs.in/api/licenses", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db = json.loads(g)
    #print(len(db['data'][0]['plid']
    items = []
    for item in db:
        items.append(item['plid'])
        indexY= indexY + 1
        
        
    return "my purchased licenses are", indexY
    return "Current running pid are", x
    #print(len(db['data'][0]['plid']
    #print(len(db['data'][0]['plid'])
#print(indexY)
#print(sddevdevice_info())
x= sddevpid_count()
print(x)



# # ### SDDEV USER INFO



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
        
        
    #return "current active users are", indexY
    return "Current running users are", indexY
    #print(len(db['data'][0]['plid']
    #print(len(db['data'][0]['plid'])
#print(indexY)
#print(sddevdevice_info())
#x= sddevuser_count()
print(sddevuser_count())


### SDDEV INTERFACE INFO

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
    code = requests.get("http://sddev.infinitylabs.in/api/licenses/purchase", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    #print(i)
    j=i[0]['Plan']
   
    #print(j)
    return "Current active interfaces are", j
print(sddevinterface_info())


### SDDEV ACTIVE LICENSE

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
    code = requests.get("http://sddev.infinitylabs.in/api/licenses", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db = json.loads(g)
    #print(len(db['data'][0]['plid']
    items = []
    for item in db:
        if item['license']['isActive'] :
            indexY= indexY + 1
        
        
    #return indexY
    return "Current Active licenses are", indexY
    #print(len(db['data'][0]['plid']
    #print(len(db['data'][0]['plid'])
#print(indexY)
#print(sddevdevice_info())
x= sddevactivelicense_count()
print(x)



### SDDEV DEVICE DETAILS

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
    code = requests.get("http://sddev.infinitylabs.in/api/devices/", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db1 = json.loads(g)
    
    serialNo=db1[0]['serial']
    newURL = "http://sddev.infinitylabs.in/api/devices/"+serialNo
    #print(newURL)
    res1= requests.get(newURL, headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    mess = res1.json()
   
    return "Current device installation status is", mess['message']
print(sddevdevicedetail_info())



### SDDEV DEVICE STATUS

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
    code = requests.get("http://sddev.infinitylabs.in/api/devices/", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db1 = json.loads(g)
    
    serialNo=db1[0]['serial']
    newURL = "http://sddev.infinitylabs.in/api/devices/"+serialNo
    #print(newURL)
    res1= requests.get(newURL, headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    mess = res1.json()
    #print(mess)
    message = ''
    try :
        isActive = mess['data']['isActive']
        if isActive == '1':
            message = "Device Status is activated"
        else :
            message = "Device is Not Activated"
    except:
        message = "Service Not Available" 
         
    return  message
    
        
print(sddevdevicestatus_info())




# SDDEV LICENCSE UPDATE STATUS


def putinfo(request):
    import requests
    import time
    import json
    import collections
    
    slot_serial = request.intent.slots["serialNumber"].value
    
    # if slot_serial is not None:
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/devices/", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
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
    res1 = requests.put(newURL, headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz},data=param, timeout = 60)
    #res1= requests.get(newURL, headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz})
    mess = res1.json()
    return mess['message']
    # else :
    #     return "Please Enter Serial Number"
    #return "working"
#print(put_info())



# ################## ZTP #####################


def ztp(request):
    import requests
    import time
    import json
    import collections
    
    slot_serial = request.intent.slots["serialNumber"].value
    slot_lid = request.intent.slots["lid"].value
    #slot_latitude = request.intent.slots["latitude"].value
    #slot_longitude = request.intent.slots["longitude"].value
    slot_name = request.intent.slots["name"].value
    slot_type = request.intent.slots["type"].value
    slot_dname = request.intent.slots["dname"].value
    
    # if slot_serial is not None:
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/devices/", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    #print(i)
    g = json.dumps(i)
    db1 = json.loads(g)
        
    serialNo=db1[0]['serial']
    payload = {
                'serialNumber': slot_serial,
                'lid': slot_lid,
                #'latitude': slot_latitude,
                #'longitude': slot_longitude,
                'name': slot_name,
                'type': slot_type,
                'dname': slot_dname,
            }

    
    newURL = "http://sddev.infinitylabs.in/api/devices/"

    print(newURL)

    res1 = requests.post(newURL, headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz},data=payload, timeout = 60)
    
    mess = res1.json()

    return mess['message']
    # else :
    #     return "Please Enter Serial Number"
    #return "working"
#print(ztp())
