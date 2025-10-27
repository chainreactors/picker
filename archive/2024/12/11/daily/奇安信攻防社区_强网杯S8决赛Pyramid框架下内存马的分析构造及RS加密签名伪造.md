---
title: 强网杯S8决赛Pyramid框架下内存马的分析构造及RS加密签名伪造
url: https://forum.butian.net/share/3974
source: 奇安信攻防社区
date: 2024-12-11
fetch_date: 2025-10-06T19:36:40.630880
---

# 强网杯S8决赛Pyramid框架下内存马的分析构造及RS加密签名伪造

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 强网杯S8决赛Pyramid框架下内存马的分析构造及RS加密签名伪造

* [CTF](https://forum.butian.net/topic/52)

这两天去线下参加了强网杯S8的决赛，WEB一共两题这个题目代码并不多但是考察点很创新，并且涉及了从没出现过的Pyramid框架下内存马，线下时间紧张最后20分钟才调试出来，特此记录本篇文章详细解析Pyramid框架下内存马的分析构造及RS加密签名伪造便于师傅们交流学习。

Pyramid框架下内存马的分析构造及RS加密签名伪造
---------------------------
题目源代码如下
app.py
```python
from wsgiref.simple\_server import make\_server
from pyramid.config import Configurator
from pyramid.events import NewResponse
from pyramid.response import Response
import util
users = []
super\_user = ["admin"]
default\_alg = "RS"
def register\_api(request):
try:
username = request.params['username']
if username in super\_user:
return Response("Not Allowed!")
password = request.params['password']
except:
return Response('Please Input username & password', status="500 Internal Server")
data = {"username": username, "password": password}
users.append(data)
token = util.data\_encode(data, default\_alg)
return Response("Here is your token: "+ token)
def register\_front(request):
return Response(util.read\_html('register.html'))
def front\_test(request):
eval()
return Response(util.read\_html('test.html'))
def system\_test(request):
try:
code = request.params['code']
token = request.params['token']
data = util.data\_decode(token)
if data:
username = data['username']
print(username)
if username in super\_user:
print("Welcome super\_user!")
else:
return Response('Unauthorized', status="401 Unauthorized")
else:
return Response('Unauthorized', status="401 Unauthorized")
except:
return Response('Please Input code & token')
print(exec(code))
return Response("Success!")
if \_\_name\_\_ == '\_\_main\_\_':
with Configurator() as config:
config.add\_route('register\_front', '/')
config.add\_route('register\_api', '/api/register')
config.add\_route('system\_test', '/api/test')
config.add\_route('front\_test', '/test')
config.add\_view(system\_test, route\_name='system\_test')
config.add\_view(front\_test, route\_name='front\_test')
config.add\_view(register\_api, route\_name='register\_api')
config.add\_view(register\_front, route\_name='register\_front')
app = config.make\_wsgi\_app()
server = make\_server('0.0.0.0', 6543, app)
server.serve\_forever()
```
还有一个工具util.py
```python
import base64
import json
import uuid
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1\_15
from Crypto.Hash import SHA256
import hashlib
secret = str(uuid.uuid4())
def generate\_keys():
key = RSA.generate(2048)
private\_key = key.export\_key()
public\_key = key.publickey().export\_key()
return private\_key, public\_key
def sign\_data(private\_key, data):
rsakey = RSA.import\_key(private\_key)
# 将JSON数据转换为字符串
data\_str = json.dumps(data)
hash\_obj = SHA256.new(data\_str.encode('utf-8'))
signature = pkcs1\_15.new(rsakey).sign(hash\_obj)
return signature
def verify\_signature(secret, data, signature, alg):
if alg == 'RS':
rsakey = RSA.import\_key(secret)
# 将JSON数据转换为字符串
data\_str = json.dumps(data)
hash\_obj = SHA256.new(data\_str.encode('utf-8'))
try:
pkcs1\_15.new(rsakey).verify(hash\_obj, signature)
print("Signature is valid. Transmitted data:", data)
return True
except (ValueError, TypeError):
print("Signature is invalid.")
return False
elif alg == 'HS':
hash\_object = hashlib.sha256()
data\_bytes = (json.dumps(data) + secret.decode()).encode('utf-8')
print(data\_bytes)
hash\_object.update(data\_bytes)
hex\_dig = hash\_object.hexdigest()
if hex\_dig == signature.decode():
return True
else:
return False
def data\_encode(data, alg):
if alg not in ['HS', 'RS']:
raise "Algorithm must be HS or RS!"
else:
private\_key, public\_key = generate\_keys()
if alg == 'RS':
signature = sign\_data(private\_key, data)
data\_bytes = json.dumps(data).encode('utf-8')
encoded\_data1 = base64.b64encode(data\_bytes) # data
encoded\_data2 = base64.b64encode(signature) # signature
print(encoded\_data2)
encoded\_data3 = base64.b64encode(alg.encode('utf-8')) # alg
encoded\_data4 = base64.b64encode(public\_key) # public\_key
encoded\_data = encoded\_data1.decode() + '.' + encoded\_data2.decode() + '.' + encoded\_data3.decode() + '.' + encoded\_data4.decode()
print("The encoded data is: ", encoded\_data)
return encoded\_data
else:
hash\_object = hashlib.sha256()
data\_bytes = (json.dumps(data) + secret).encode('utf-8')
inputdata = json.dumps(data).encode('utf-8')
hash\_object.update(data\_bytes)
hex\_dig = hash\_object.hexdigest()
signature = base64.b64encode(hex\_dig.encode('utf-8'))
encoded\_data1 = base64.b64encode(inputdata) # data
encoded\_data3 = base64.b64encode(alg.encode('utf-8')) # alg
encoded\_data = encoded\_data1.decode() + '.' + signature.decode() + '.' + encoded\_data3.decode()
print("The encoded data is: ", encoded\_data)
return encoded\_data
def data\_decode(encode\_data):
try:
all\_data = encode\_data.split('.')
sig\_bytes = all\_data[1].replace(' ', '+').encode('utf-8')
print(sig\_bytes)
data = base64.b64decode(all\_data[0].replace(' ', '+')).decode('utf-8')
json\_data = json.loads(data)
signature = base64.b64decode(sig\_bytes)
alg = base64.b64decode(all\_data[2]).decode('utf-8')
key = secret
if len(all\_data) == 4:
key\_bytes = all\_data[3].replace(' ', '+').encode('utf-8')
key = base64.b64decode(key\_bytes) # bytes
# 验证签名
is\_valid = verify\_signature(key, json\_data, signature, alg)
if is\_valid:
return json\_data
else:
return False
except:
raise "something error"
def read\_html(filname):
with open('C:\\Users\\86150\\Desktop\\attachment\\src\\static\\' + filname, 'r', encoding='utf-8') as file:
# 读取文件内容
html\_content = file.read()
return html\_content
```
### RS加密伪造
由以上源码发现首先需要伪造admin用户token才能进入test路由进行命令执行，但是由于RS算法的密钥是随机的我们不能够伪造admin
```python
def generate\_keys():
key = RSA.generate(2048)
private\_key = key.export\_key()
public\_key = key.publickey().export\_key()
return private\_key, public\_key
```
![82dd4579fddf444658e30f5738fc0e07.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-6f25f9b1296894479fac96cea25f164e16a3df7f.png)
成功注册会返回token
![087953315a7380c82001c0a87dbfb32e.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-89aaca9d5146879779e1396eea7f5d0a9ca981a2.png)
我们本地调试解密函数
```python
def data\_decode(encode\_data):
try:
all\_data = encode\_data.split('.')
sig\_bytes = all\_data[1].replace(' ', '+').encode('utf-8')
print(sig\_bytes)
data = base64.b64decode(all\_data[0].replace(' ', '+')).decode('utf-8')
json\_data = json.loads(data)
signature = base64.b64decode(sig\_bytes)
alg = base64.b64decode(all\_data[2]).decode('utf-8')
key = secret
if len(all\_data) == 4:
key\_bytes = all\_data[3].replace(' ', '+').encode('utf-8')
key = base64.b64decode(key\_bytes) # bytes
# 验证签名
is\_valid = verify\_signature(key, json\_data, signature, alg)
if is\_valid:
return json\_data
else:
return False
except:
raise "something error"
```
调试发现加密token的第四个字段如果存在就是自定义的key
![c7edd4514741e51df28deb8484e2f847.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-08f6694936df58925529610962b523aba9f04b77.png)
之后验证签名的正确性，这个key就是RSA的公钥
![fa805ce2455a500162a535994e5224b5.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-af50183c95b76d43199b56a171c45ad5410d6da2.png)
既然第四个字段是我们自己可控，我们就可以本地生成RSA的私钥和公钥来伪造admin
编写脚本
```python
import util
import base64
import json
import uuid
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1\_15
from Cryp...