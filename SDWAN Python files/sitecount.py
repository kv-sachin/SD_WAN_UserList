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
    return "total active sites are", len(db)
print(sites_count())
