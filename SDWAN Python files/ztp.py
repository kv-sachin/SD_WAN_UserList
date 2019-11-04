def ztp():
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
    code = requests.get("http://sddev.infinitylabs.in/api/devices/", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz})
    v=code.json()
    i=v['data']
    print(i)
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

    res1 = requests.post(newURL, headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz},data=payload)
    
    mess = res1.json()

    return mess['message']
    # else :
    #     return "Please Enter Serial Number"
    #return "working"
print(ztp())
