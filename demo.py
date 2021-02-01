# encoding:utf-8

import requests
import json

ak = 'KSfb3HMNWdjCmjiiXpvBxfaM'
sk = 'dLRRCAmEBbXpbTG3hgmFDrXvrxTGayDr'

url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + ak + '&client_secret=' + sk

response = requests.post(url)
content = response.json()
access_token = content['access_token']
print(access_token)




import base64
import time
imagecontent = open(r'E:\pythonstudy\image54.jpg', 'rb').read()
data = {'image': base64.b64encode(imagecontent).decode()}


for i in range(20):
    request_url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/detection/Annimal_cd' + "?access_token=" + access_token

    response = requests.post(request_url, data = json.dumps(data))
    content = response.json()
    print(i)
    time.sleep(5)

# print(content)