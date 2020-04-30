import requests
import json


host = 'https://adnmb2.com'
api = '/Api/getForumList'

resp = requests.get("%s%s" % (host, api))
try:
    js = json.loads(resp.content)
except Exception as e:
    print(e)
    exit()

print(json.dumps(js))