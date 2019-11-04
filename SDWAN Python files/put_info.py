
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
