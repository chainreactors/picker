---
title: 渗透测试高级技巧（三）：被前端加密后的漏洞测试
url: https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247526919&idx=1&sn=0386721ba5a1ddad7d8d307ba4c159f5&chksm=c2d116a3f5a69fb57e216f9bbdb4727a8e48f48f9929a0f77b192702c0c6d59a71b08a0ae5a8&scene=58&subscene=0#rd
source: Yak Project
date: 2024-12-06
fetch_date: 2025-10-06T19:39:34.752948
---

# 渗透测试高级技巧（三）：被前端加密后的漏洞测试

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPWO6w3DqjNOIoTibcxpUGa5FrOF6EtAMhWHUX1ge1FI8exFdoYtDRka7Q/0?wx_fmt=jpeg)

# 渗透测试高级技巧（三）：被前端加密后的漏洞测试

原创

Yak

Yak Project

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg)

#

#

> **前文指路**
>
> [渗透测试高级技巧（一）：分析验签与前端加密](https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247511526&idx=1&sn=c3a661b71ad9e9108b822cec461d34e6&scene=21#wechat_redirect)
>
> [渗透测试高级技巧（二）：对抗前端动态密钥与非对称加密防护](https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247512499&idx=1&sn=ca603296c94cd7984f340bcd6d818779&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdcRRoJCbdWkNCU257AEVDPZHlnAOwN20Oal3yFuHa7pShbBPh8a5eb2aibHUiarn4jTbxs1rJpFcDw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPWYzagsE0iaxiaelhpoUUXLHzAAdibwNN2UYRke3iab81WRAicYohAa3gfBgA/640?wx_fmt=png&from=appmsg)

#

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPW8fVoecDOb1dkZzYurpca84UPEibmsxE3ZT0not7vic8ZicOkKpXIzB9Yg/640?wx_fmt=png&from=appmsg)

#

我们考虑以下登陆场景，在这个场景中，用户界面和服务器之间通信使用浏览器 JS 加密，前后都用 AES ECB 加密。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPWV3dWZzHCaJXjJsgxqYBqQQ2l1F98IpcJmsjq3TJZqoX3DXLawL2v0A/640?wx_fmt=png&from=appmsg)

这个时序图展示了整个加密登录流程：

1. **用户界面到 JS 层：**

* 用户在界面输入用户名和密码
* 数据以 JSON 格式传递给 JS 层处理

2. **JS 层加密处理：**

* JS 接收到原始 JSON 数据
* 使用 AES ECB 模式进行加密

3. **客户端到服务器传输：**

* 发送加密后的数据到服务器

4. **服务器处理：**

* 服务器接收加密数据并进行解密
* 查询数据库获取用户信息
* 验证用户凭据
* 准备响应数据并进行加密

5. **服务器到客户端响应：**

* 发送加密的响应数据回客户端

6. **客户端处理响应：**

* JS 层解密服务器响应
* 将解密后的结果显示在用户界面

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPWhic86HssFJ5vTj9ptPgCOiaCneahbmlwZYdbJjHOTF3yRllicSse34z1A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPWqXfFdMPsBia6yuyicYh9ibvwgsqDHqFMNswUMEvBRjqYOZ8LxPeyYvddw/640?wx_fmt=png&from=appmsg)

在开始之前，大家需要先启动 Yakit 的 Vulinbox 靶场，在这个靶场中，我们将会开始我们今天要操作的加密和解密处理。点击 2024 - 11 - 25 之后的靶场，在最新的靶场中，将会看到 **CryptoJS.AES(ECB) 被前端加密的 SQL 注入（Bypass认证）**这个靶场，点击进入后会看到一个登录框和一些基本提示。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPWc32HFvJEqibhSp9tOXnRxNjxQFZRr4zMicdp8HRxaZFLBzm5SiaEAt3FQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPWyWq9RzL1mGhP7qCVPBBqIq4hy5e1ibTicrfPQqKibhaGJVT71LPQlwR4A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPWfv4uAHxib08iaQ8BVNqYYiaJdoHMicL4bVk0wexDby0uXprzwMdA7djqOw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPWp4mxfbdPadrCQ50Jib777L5pohbyPpjX8Xfsxp94NWYDscaicktDbiaVg/640?wx_fmt=png&from=appmsg)因为在前两篇文章中，我们已经讲解了 JS 加密算法如何分析，在这里就简略一点，把篇幅留给重要的章节：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPWLXnhWE9CfQHVe3vvrJo8RicpAtxlJA5PKqzo4CJsN4Blx8V8RIvaPkg/640?wx_fmt=png&from=appmsg)

通过 “右键” 查看源代码发现，AES-ECB 的加密方式，密钥为 1234123412341234 这个其实非常简单，我们可以很快得到它对应的加密解密代码。

```
raw = codec.DecodeBase64(`zqBATwKGlf9ObCg8Deimijp+OH1VePy6KkhV1Z4xjiDwOuboF7GPuQBCJKx6o9c7`)~result = codec.AESECBDecrypt(`1234123412341234`, raw,"")~dump(result)
```

我们把上个数据包的秘文和密码取出来，使用 Yak Runner 写出证明我们解密成功了：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPWLfsMyCWkNoOdtibROQHY4QsMnbg4iceAXSx5WNwkdHJlkmdcXs6aVkicA/640?wx_fmt=png&from=appmsg)

得到这么一段代码之后，再包装出来，包装成一个 Decrypt 函数，要求这个函数可以对整个数据包进行解密，我已经写好了这段代码，大家可以参考一下，主要涉及到数据包取 body 对应字段之后，再解密，假定我们的数据包长这个样子：

```
POST /crypto/js/lib/aes/ecb/handler/sqli/bypass HTTP/1.1Host: 127.0.0.1:8080Content-Type: application/json
{  "data": "zqBATwKGlf9ObCg8Deimijp+OH1VePy6KkhV1Z4xjiDwOuboF7GPuQBCJKx6o9c7",  "key": "31323334313233343132333431323334"}
```

针对上面这个数据包，我们编写一个函数如下：

```
decryptData = (packet) => {    body = poc.GetHTTPPacketBody(packet)    params = json.loads(body)    raw = codec.DecodeBase64(params.data)~    key = codec.DecodeHex(params.key)~    result = codec.AESECBDecrypt(key, raw, nil)~    return string(result)}
```

在这个函数中，我们经过如下步骤得到了解密的结果：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPWzxwxHYVpX3aMYC77YfqS3sW6QouE0wiaUk7JyQ0aKiaDoTICiaHffWrhA/640?wx_fmt=png&from=appmsg)

具体执行起来是什么样？用户可以根据如下代码在自己的 Yak Runner 运行一下这个函数感受一下：

```
decryptData = (packet) => {    body = poc.GetHTTPPacketBody(packet)    params = json.loads(body)    raw = codec.DecodeBase64(params.data)~    key = codec.DecodeHex(params.key)~    result = codec.AESECBDecrypt(key, raw, nil)~    return string(result)}
packet = <<<TEXTPOST /crypto/js/lib/aes/ecb/handler/sqli/bypass HTTP/1.1Host: 127.0.0.1:8080Content-Type: application/json
{  "data": "zqBATwKGlf9ObCg8Deimijp+OH1VePy6KkhV1Z4xjiDwOuboF7GPuQBCJKx6o9c7",  "key": "31323334313233343132333431323334"}TEXTresult = decryptData(packet)println(result)
```

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPWM27m4gTEfWDnlrBaJoMsmzC833yP2yClIlN8AJKrruJLdFVVjGDbibQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPWNQk4l982ICzAgu82szPxpupNWawksBcgoLoFaRFtic9PPDIcYC7eOng/640?wx_fmt=png&from=appmsg)

#

经过上述简单的分析和实践，我想大家已经知道基本解密上述的代码了，那么可以正式开始我们的第一个任务：让 MITM 看到明文数据包：我们直接把上述的函数复制到热加载代码中，我们再修改一下代码，让 **encryptData** 直接返回整个数据包，这样就可以直接保存到数据库了。

```
decryptData = (packet) => {    body = poc.GetHTTPPacketBody(packet)    params = json.loads(body)    raw = codec.DecodeBase64(params.data)~    key = codec.DecodeHex(params.key)~    result = codec.AESECBDecrypt(key, raw, nil)~    body = string(result)    return string(poc.ReplaceBody(packet, body, false))}
# hijackSaveHTTPFlow 是 Yakit 开放的 MITM 存储过程的 Hook 函数# 这个函数允许用户在 HTTP 数据包存入数据库前进行过滤或者修改，增加字段，染色等# 类似 hijackHTTPRequest#    1. hijackSaveHTTPFlow 也采用了 JS Promise 的回调处理方案，用户可以在这个方法体内进行修改，修改完通过 modify(flow) 来进行保存#    2. 如果用户不想保存数据包，使用 drop() 即可# hijackSaveHTTPFlow = func(flow /* *yakit.HTTPFlow */, modify /* func(modified *yakit.HTTPFlow) */, drop/* func() */) {    request = codec.StrconvUnquote(flow.Request)~    newRequest = decryptData(request)    flow.Request = codec.StrconvQuote(newRequest)    modify(flow)}
```

在这里我们需要使用到 **hijackSaveHTTPFlow** 这个函数，这个函数可以在数据包进入数据库之前进行一次修改，我们可以在这里解密数据包，保证数据包传入的是正确的。

跟随如下步骤，点击热加载，我们就发现，请求包已经变成了明文：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPWagcAy16CtibLGxtA8qw5ibKXuMBEebx9IjqsOprXWaQZf5Z0NPtkykXw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPWyiclw1X8Gpe9EQDJsnHsQa8burSBIAMasX7lBmb2MMbE52HsjORwpxA/640?wx_fmt=png&from=appmsg)

#

现在我们在 MITM 中可以看到明文的请求包了，那么如何发送这个数据包，同时让他在发送的时候，自动进行加密？

类似的，我们首先需要准备一下加密数据包的函数：

```
```
encryptData = (packet, key) => {    body = poc.GetHTTPPacketBody(packet)    result = string(codec.AESECBEncrypt(key, body, nil)~)    data = {        "data": codec.EncodeBase64(result),        "key": codec.EncodeToHex(key),    }    body = json.dumps(data)    return string(poc.ReplaceBody(packet, body /*type: []byte*/, false))}
```
```

我们在这个数据包发送之前，最后进行一步处理即可。

接下来，点开 Web Fuzzer ，把刚才的解密后的数据包放在这里，并且在热加载中处理好相应的代码：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPW0FjOVp4ickF6iaPja2WgBeR9TYaib6vLgAZxuKjvq230G0643miaibsZniaQ/640?wx_fmt=png&from=appmsg)

经过上面的处理，我们发送这个数据包将会看到如下结果：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPW4zCQBkT3iae8P92OmOOfAhWa6VR7PdGTlJo0o443QU6vR1JSEMDczcA/640?wx_fmt=png&from=appmsg)

虽然我们解密成功了，但是认证密码却失败了，不过不重要，我们在这个时候已经可以让测试的成本变低了，接下来只需要调整或者爆破就行了。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPWbg8OFOnwichruDXZMQIey9AlaPlkQKLr9P7ibIwaibtm71mRdaEzj6QeQ/640?wx_fmt=png&from=appmsg)

#

虽然这一步是最简单的，但是我们可以把这一步当成是一个胜利的象征：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeklQWT1tkhB4rgdUgHObPW6EvgDdRmbiay25ATyIzsXmv61QaKHLtWo5pxmdahdF2ERzEm7efmDbQ/640?wx_fmt=png&from=appmsg)

直接发送上述数据包，服务器接收到的核心数据是已经加密后的内容，返回的内容包含 “解密成功” - “密码验证成功”，“登陆成功”。

我们通过热加载主动去修改了数据包的内容，进行了加密，直接绕过了上述加密和...