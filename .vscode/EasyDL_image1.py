import base64
import json
import urllib

easyDL_AK = 'E0MdVVGQdB1zjriGTYB8ZrSi'
easyDL_SK = 'GPXZ9thIcXyFQzuD9BlXINBXgR9fa8Qy'
request_URL = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/Ainimal_cat_or_dog'

Header_text = 'Content-Type:application/json'

request_URL = request_URL + "?access_token=" + easyDL_AK
request = urllib.request()