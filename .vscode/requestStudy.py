import requests
import json

# 打开一个网页,get,post,pull,delete,head,options
url = "https://www.baidu.com"
response = requests.get(url)

# 设置返回的类型编码，一般都是utf-8或gbk，否则中文会出现乱码，此处非必需
response.encoding = 'utf-8'

# 查看返回的代码，正常为：200，404是找不到网页
print(response.status_code)

# 查看返回的类型：<class 'requests.models.Response'>
print(type(response))

# 查看返回的类型编码
print(response.encoding)

# 查看内容：用于获取文本及源代码的数据（将数据转变为字符串）
print(response.text)
# 查看内容：用于获取图片及音视频等数据（将数据转变为二进制）
print(response.content)

#获得响应头内容
print(response.headers)
print(response.headers['content-type'])

# 将内容追加写入文件里
file = open('temp.txt', 'a+', encoding='utf-8')
file.write(response.text)
file.close()

# 下载一个图片
imgage_url = 'http://c.biancheng.net/uploads/allimg/191009/1-191009162420B7.gif'
response = requests.get(imgage_url)

if response.status_code == 200:
    imagefile = open('imageDemo.jpg', 'wb')
    imagefile.write(response.content)
    imagefile.close()
    print("下载图片成功！")
else:
    print("下载图片出错。")



# Requests 参数相关 两种方式，一种是URL直接用?action=quey&name=aaa方式
url = 'https://www.baidu.com'
paras = {'action': 'quey', 'name': 'aaa'}
response = requests.get(url, params=paras)
print(response.url)