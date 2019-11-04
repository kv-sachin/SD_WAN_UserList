def service_create(request):
    import requests
    import time
    import json
    import collections
    slot_device = request.intent.slots["device_name"].value
    slot_de = slot_device.upper()
    slot_dev = request.intent.slots["device_no"].value
    slot_d = slot_dev.upper()
    slot_value = request.intent.slots["Service_name"].value
    slot_val = request.intent.slots['pw_id'].value
    slot_loopback = request.intent.slots["loopback_ip"].value
    slot_interface = request.intent.slots['interface_number'].value
    slot_interfac = slot_interface.replace(' ', '/')
    slot_interf = request.intent.slots['interface_no'].value
    slot_inte = slot_interf.replace(' ','/')
    slot_remote = request.intent.slots['ip_address'].value
    
    payload = {
    "l2vpn1:l2vpn1": {
        "name": slot_value,
        "pw-id": slot_val,
        "link": [
            {
                "device": slot_de,
                "ios": {
                    "intf-number": str(slot_interfac)
                },
                "remote-ip": str(slot_remote)
            },
            {
                "device": slot_d,
                "iosxr": {
                    "intf-number": str(slot_inte)
                },
                "remote-ip": str(slot_loopback)
            }
         ]
        }
    }
    code = requests.post("http://203.122.19.100:6661/api/running/services/",headers={"Content-Type": "application/vnd.yang.data+json"}, auth=("admin","admin"), data=json.dumps(payload))
    code = requests.post("http://203.122.19.100:6661/api/running/services/",headers={"Content-Type": "application/vnd.yang.data+json"}, auth=("admin","admin"), json=payload)
    cod= requests.get("http://203.122.19.100:6661/api/running/services/l2vpn1/",headers={"Accept": "application/vnd.yang.collection+json"},auth=("admin","admin"))
    y = cod.json()
    w=y['collection']
    m=w['l2vpn1:l2vpn1']
    x=json.dumps(m)
    db=json.loads(x)
    items = []
    for item in db:
        items.append(item['pw-id'])
    if any(list == slot_val for list in items): 
        return "Pw-id has been already exist..... Please try again"
    elif (code.status_code == 400):
        return "Service is not created... Please try again"
    else :
        return "Service has been created"

print(service_create(request))
