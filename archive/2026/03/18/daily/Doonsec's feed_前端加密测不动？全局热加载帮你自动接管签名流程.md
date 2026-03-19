---
title: 前端加密测不动？全局热加载帮你自动接管签名流程
url: https://mp.weixin.qq.com/s/vYzIXAIQXlmuQD8Mb8xZyw
source: Doonsec's feed
date: 2026-03-18
fetch_date: 2026-03-19T04:17:46.516330
---

# 前端加密测不动？全局热加载帮你自动接管签名流程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jibGAup6p72HVzPibFqNJ5lbaLnVqRUv6SPLUaLmKW8UHQZibORAbjoj2xLgt9zcbSX1IySoXs38V1Iic6Wibz4TTO8cjrAFsLo4ibiaKMrZwwBeKI/0?wx_fmt=jpeg)

# 前端加密测不动？全局热加载帮你自动接管签名流程

原创

YAK
YAK

Yak Project

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZcZEfibgt3AwvYxcwGUeXQGpiaWCicPsMEjINYFibjicGYU1WgiaTibAbwUlIPwu8nApytYghVl1icLjAomiaQ/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72FibSvESMovbrUXcKujHk7vO7aUTb78naW6m3nWl8HNdsbNNGLvwW9JK8UliaZBicWBn4EM3yesoadWILgqDNziam1ETsENWJxSDpA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jibGAup6p72FiaaGnEicjZShacHibUPFiafe43MHUpurDdA92OtJAjtq9iaYCjnibfoIEZhbE7uwCmVdwIKNoLcCVWHGnn8AQhEDjsLdmBDb5hlrg4/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72Fqj1afib2rpAwd7MGZA0ET9CYrY9YBbppht5WwHQdoXMFIqT194lSZHgxcdQ0e5o3bGBsDgG0UrMNLWoxpKKricwOgsVpN836l0/640?wx_fmt=png&from=appmsg)

**在开始之前，先启动** Vulinbox。启动之后，可以访问：http://127.0.0.1:18080/ ，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72HSHYRYznRCLn0Wb8ERDYoW899VNcS3x7NmZ5yxdB50hibiccbnDZZ0q516opPgFD8cp9AB0guGUYnWbrg7BU1vW4O0hicIOwB7n8/640?wx_fmt=png&from=appmsg)

本文会用到以下几个入口：

1、靶场说明页：

`http://127.0.0.1:18080/crypto/challenge-api-docs`

2、获取 challenge：

`http://127.0.0.1:18080/api/get-challenge`

3、受保护接口：

`http://127.0.0.1:18080/api/user/info`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72GV9pSq8I0vicsokpsliaQiaykibrCqiaD9rWiaPX7U18jfyTTs88LDynvYWDiabGFNYClrekJVp2R73qJHPVMvATiaHkRkich3oOfcwIbY/640?wx_fmt=png&from=appmsg)

这次使用的靶场不是“固定 AES Key 然后简单改包”的例子，而是一个更接近实际业务的动态 challenge 接口。

它的交互顺序如下：

1、请求 `/api/get-challenge`，服务端返回一段加密后的 challenge。、

2、客户端解密 challenge，得到 nonce。

3、使用 nonce 和约定的 HMAC Key 计算签名。

4、请求 `/api/user/info` 时，把签名写入 `X-Auth-Signature`。

5、服务端校验通过后，返回的业务数据依然是 AES-CBC 加密后的内容。

换句话说，这里至少包含两段“测试前后必须先执行的逻辑”：

1、请求前的自动补签名。

2、响应后的自动解密。

这也正是全局热加载最适合切入的地方。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72E3KnAibsyWDqbPmZqwBdCaj3bSNLUOxhWevpO5GAyEGglPS3XMcYqibf6FFbOiaq113csOn1XbACbA761wwP9MXXicibSlYshUiadGI/640?wx_fmt=png&from=appmsg)

在自动化之前，最好先把这条链路“手工拆开”验证一次。

### 1、先从 `api/get-challenge` 获取

```
HTTP/1.1 200 OKContent-Type: application/json{"challenge":"ifIYn2ChP6pOaedUtwRg8urjclJJazl2N8eSrcEUo1OZz7+AT+9ERWnJVGxtdQUU","iv":"tYJG4EX4pOICNfXbAT2lkg=="}
```

针对上面这个响应包，我们可以先写一个专门计算签名的函数：

```

```

```
API_AES_KEY = "YakitVulinboxAES"API_SIGN_KEY = "YakitVulinboxHMACKey-SIGNATURE"signChallengeResponse = func(packet) {    body = poc.GetHTTPPacketBody(packet)    params = json.loads(body)    challengeBytes = codec.DecodeBase64(params.challenge)~    ivBytes = codec.DecodeBase64(params.iv)~    nonce = codec.AESCBCDecrypt(API_AES_KEY, challengeBytes, ivBytes)~    return codec.EncodeToHex(codec.HmacSha256(API_SIGN_KEY, nonce))}
```

这段代码本身并不发请求，它只做一件事：把 challenge 响应中的密文解开，然后生成真正需要放进请求头里的签名。

你可以直接在 YAK Runner 这样生成它：

```
API_AES_KEY = "YakitVulinboxAES"API_SIGN_KEY = "YakitVulinboxHMACKey-SIGNATURE"signChallengeResponse = func(packet) {    body = poc.GetHTTPPacketBody(packet)    params = json.loads(body)    challengeBytes = codec.DecodeBase64(params.challenge)~    ivBytes = codec.DecodeBase64(params.iv)~    nonce = codec.AESCBCDecrypt(API_AES_KEY, challengeBytes, ivBytes)~    return codec.EncodeToHex(codec.HmacSha256(API_SIGN_KEY, nonce))}challengePacket = <<<TEXTHTTP/1.1 200 OKContent-Type: application/json{"challenge":"ifIYn2ChP6pOaedUtwRg8urjclJJazl2N8eSrcEUo1OZz7+AT+9ERWnJVGxtdQUU","iv":"tYJG4EX4pOICNfXbAT2lkg=="}TEXTprintln(signChallengeResponse(challengePacket))
```

执行之后，你会得到一段十六进制签名：

```
c9f36e99b46389cefc289002c02f88548403de96d0facf8a6cc99d1ded27f632
```

### 2、把签名手工填回 HTTP Raw 里发请求

拿到签名之后，可以把上一步的签名填进下面这个请求：

```
GET /api/user/info HTTP/1.1Host: 127.0.0.1:18080X-Auth-Signature: c9f36e99b46389cefc289002c02f88548403de96d0facf8a6cc99d1ded27f632
```

发送之后，你会拿到一段新的密文响应。格式大致如下：

```
HTTP/1.1 200 OKContent-Type: application/json{"data":"xLZ8ri0BmAqw72zNycPmzSQ1qkJ+QVASKyqy6j/D7rLjRyBwT/Tpn5BJCjLfEMVEReS9iglSFzikuQvL1q+NSwiMCHHWFRyybPyq9oUXd+xR/1xFIxCCoNM8Ud5JG+3HDlW8lJZ4Yo9dM9snojIf3Ks+dHl8kBTD8ePARUllTJ9MwXst/33X23acG27BtPJycvn/bptDTfqKyknPLdIQYwM0ozrteuCTGcjLWH0DtnH2CW8D46PuMtpgXKd9HyRhcBIu+uuY5Z+vSTPe48TwARuhX9FUG/F/odywOW5EalA=","iv":"4DqWSC1nHDF9AX183lb1DQ=="}
```

### 3、把受保护响应解成明文

拿到这段响应之后，我们继续按照同样的思路，写一个只负责解密响应的函数：

```
API_AES_KEY = "YakitVulinboxAES"decryptProtectedPacket = func(packet) {    body = poc.GetHTTPPacketBody(packet)    params = json.loads(body)    dataBytes = codec.DecodeBase64(params.data)~    ivBytes = codec.DecodeBase64(params.iv)~    plain = codec.AESCBCDecrypt(API_AES_KEY, dataBytes, ivBytes)~    return string(plain)}
```

同样可以把刚才抓到的响应原文直接贴进去验证：

```
API_AES_KEY = "YakitVulinboxAES"decryptProtectedPacket = func(packet) {    body = poc.GetHTTPPacketBody(packet)    params = json.loads(body)    dataBytes = codec.DecodeBase64(params.data)~    ivBytes = codec.DecodeBase64(params.iv)~    plain = codec.AESCBCDecrypt(API_AES_KEY, dataBytes, ivBytes)~    return string(plain)}responsePacket = <<<TEXTHTTP/1.1 200 OKContent-Type: application/json{"data":"xLZ8ri0BmAqw72zNycPmzSQ1qkJ+QVASKyqy6j/D7rLjRyBwT/Tpn5BJCjLfEMVEReS9iglSFzikuQvL1q+NSwiMCHHWFRyybPyq9oUXd+xR/1xFIxCCoNM8Ud5JG+3HDlW8lJZ4Yo9dM9snojIf3Ks+dHl8kBTD8ePARUllTJ9MwXst/33X23acG27BtPJycvn/bptDTfqKyknPLdIQYwM0ozrteuCTGcjLWH0DtnH2CW8D46PuMtpgXKd9HyRhcBIu+uuY5Z+vSTPe48TwARuhX9FUG/F/odywOW5EalA=","iv":"4DqWSC1nHDF9AX183lb1DQ=="}TEXTprintln(decryptProtectedPacket(responsePacket))
```

运行之后，你就会得到最终的明文结果：

```
{"email":"admin@yaklang.io","message":"Congratulations! You have successfully passed the challenge.","permission":"all","used_nonce":"bc13cef03c7d2f3427902e45300cd3d6ca0551afdb3422adb4e639431b0ae6e3","user":"admin"}
```

到这里为止，才算是真正把这条链路“手工验证”完毕。可以发现，还是比较繁琐的，而且很有"割裂感”，需要在不同的地方跳来跳去，整个调试过程十分不流畅。下面我们看看用全局热加载的方式，如何提升流畅度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72FFW0k4T2wyHHhV14cpIKvae9q88CPmFhqNAQbZgkNblv8kH0hlelaWpDAVmExR0HrF8EsweiaeIwu26y5CkvOFeYqOMr2B4bWA/640?wx_fmt=png&from=appmsg)

既然整条链路已经清楚，那么热加载脚本最核心的内容其实只有两块：

1、自动获取 challenge 并生成签名。

2、自动解密受保护接口的响应。

#### 1、获取 challenge 并计算签名

我们先把 challenge 获取和签名计算封装成一个函数。它做的事情非常直接：

1、从当前 HTTP 数据包里取出 Host。

2、构造一个到 `/api/get-challenge` 的请求。

3、解析返回的 `challenge` 和 `iv`。

4、解密出 nonce。

5、用 HMAC-SHA256 计算签名。

代码如下：

```
fetchChallengeSignature = func(isHttps, packet) {    host = poc.GetHTTPPacketHeader(packet, "Host")    if host == "" {        panic("global hotpatch: request host is empty")    }    challengeReq = "GET /api/get-challenge HTTP/1.1\r\n" +        "Host: " + host + "\r\n" +        "User-Agent: yak-global-hotpatch-demo\r\n" +        "Connection: close\r\n\r\n"    challengeRsp, _ = poc.HTTP(        challengeReq,        poc.https(isHttps),        poc.timeout(5),        poc.save(false),    )~    body = poc.GetHTTPPacketBody(challengeRsp)    params = json.loads(body)    challengeBytes = codec.DecodeBase64(params.challenge)~    ivBytes = codec.DecodeBase64(params.iv)~    nonce = codec.AESCBCDecrypt(API_AES_KEY, challengeBytes, ivBytes)~    return codec.EncodeToHex(codec.HmacSha256(API_SIGN_KEY, nonce))}
```

在这个函数里，最重要的返回值就是最终的 `signature`。、

后面无论是 Web Fuzzer 还是 MITM，只要请求命中了目标接口，都可以复用这段逻辑。

#### 2、解密受保护接口响应

第二个函数负责对响应做还原。这个函数要处理的是 `/api/user/info` 返回的 `data + iv` 结构：

```
decryptProtectedResponse = func(packet) {    body = string(poc.GetHTTPPacketBody(packet))    if !str.Contains(body, `"data"`) || !str.Contains(body, `"iv"`) {        return packet    }    params = json.loads(body)    dataBytes = codec.DecodeBase64(params.data)~    ivBytes = codec.DecodeBase64(params.iv)~    plain = codec.AESCBCDecrypt(API_AES_KEY, dataBytes, ivBytes)~    return poc.ReplaceHTTPPacketBody(packet, plain)}
```

这段代码做了三件事：

1、取出 HTTP Body。

2、解析 `data` 和 `iv`。

3、解密之后，把 HTTP Body 替换成明文。

这里的重点不在“会不会 AES...