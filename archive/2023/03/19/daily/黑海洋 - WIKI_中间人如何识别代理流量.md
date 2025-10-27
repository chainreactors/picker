---
title: 中间人如何识别代理流量
url: https://blog.upx8.com/3295
source: 黑海洋 - WIKI
date: 2023-03-19
fetch_date: 2025-10-04T10:02:52.913884
---

# 中间人如何识别代理流量

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 中间人如何识别代理流量

发布时间:
2023-03-18

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
12718

# 常见的中间人攻击方式

* 被动分析 (流量特征, PoC漏洞)
  常用于分析明文协议, 或者TLS握手
* 主动探测
  一般对于Shadowsocks, V2Ray, TLS 1.3 (获取服务器SSL证书)
* 数据包重放
  主要用于识别客户端

# 代理流量的几大特征

以下特征是任何代理协议都有的, 无法抹除(或者说很难抹除)

* 长连接
  大部分的正常流量都是短连接
* 双向流
  现代代理的一大误区就是伪装Web服务, 互联网中99%的Web流量 都是单向流, 即 一组请求对应一组响应 (Request -> Response), 使用WebSocket的网站更是少之又少, 在Web服务上跑双向流难道不是一种自欺欺人?
* 大流量
  如果你认为伪装Web聊天室就可以解决上面的双向流问题, 那么请你解释一下 哪个Web聊天室的流量这么大?
* 连接数多
  如果你的流量不是很大的话, 那么又怎么解释你对着一个Web服务器开20-30个连接? 一般一个网页(聊天室, 探针)只会创建一个WebSocket连接, 那么你怎么解释连接数多呢？
* 点对点
  你一个人对着一个网站域名, IP 进行连接, 跑的加密长连接, 如果你是中间人, 你会怎么觉得?

# 坊间传闻辟谣

* 套了TLS很安全, 这样就没有办法被识别了
  详细请看后面的TLS连接风险评定
* 开了IP白名单, 任何探测和重放攻击都没用
  防火墙属于旁路设备, 你发送和接收的所有流量都要经过, 所以防火墙完全有能力伪造你的IP, 相反 如果开了白名单, 是不是更可疑呢？ (你越不想让别人看到的东西 那么越更可疑)
* 我从来就没有被墙过
  幸存者偏差, 也许你流量小到没有分析的必要
* 备案域名不会被墙
  并不是，备案域名和未备案域名跨境传输是同等待遇，只是备案域名可以使用大陆服务器直接提供Web服务

# TLS流量风险评定

## 客户端握手 (ClientHello)

TLS ClientHello有指纹 (详细可以谷歌查一下 关键词 "TLS握手指纹") 这里不多讲

如果使用程序默认的指纹 (以 Go TLS 为例)去访问一个网页, 且符合上述流量特征, 那么是代理的风险会很高

实测伊朗的防火墙会阻止curl和wget的指纹对非白名单SNI的请求， Go TLS和浏览器指纹则正常
建议使用浏览器指纹进行连接 (参考项目 [uTLS](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3JlZnJhY3Rpb24tbmV0d29ya2luZy91dGxz))

前排提示 uTLS仓库已经年久失修 Chrome指纹停留在Chrome 83 也许也是一种风险
可以更换[这个](https://blog.upx8.com/go/aHR0cHM6Ly9naXRsYWIuY29tL0NvaWFQcmFudC90bHM)仓库 , 目前加入了 Chrome 104的指纹

## 服务器名称指示 (访问域名/SNI)

免费域名风险最高, 较为便宜的域名也有一定风险

## TLS连接版本号

TLS 1.3是风险最高的, 因为Server Hello后内容全部加密, 中间人需要主动探测才可以拿到服务器证书

TLS 1.2风险为中等, 证书交换全部明文传输, 中间人可以直接截取来校验

SSLv3/TLS 1.0/TLS 1.1 风险最低, 已经没有多少流量了, 能拿到的流量样本少之又少 (不过使用某些加密方式存在被攻击风险 不推荐)

## TLS服务器证书

自签名证书是风险最高的

其次是Cloudflare免费证书和Let's Encrypt 因为人人可免费申请

付费证书的风险最低，因为几乎没有人会花几百几千买一个证书拿去做代理

# 可用于识别FakeTLS流量的新型探测方式

## 分析

MTProto-FakeTLS和Shadow TLS (v1/v2)都是模拟了一个可信证书的TLS握手, 以绕过白名单, 两个协议的设计都是近似完美的, 在握手时可以验证是否为有效客户端

### MTProto FakeTLS如何验证客户端

ClientHello包除去random字段进行整包hmac, 密钥就是secret, 服务器使用相同的hmac方式可验证客户端, random有一次性处理, 失败回落到真的Web服务器

识别方法：MTProto的TLS握手并不规范, 防火墙可以截取到服务器发送的第三个包 (hostCert) 判断包长即可 (此处参考mtg的faketls源代码) hostCert长度为随机生成 长度在1024-4096字节

### Shadow TLS v1 不会验证客户端

识别方法：直接使用curl对着服务器发送一个请求, curl会失败

### Shadow TLS v2如何验证客户端

客户端请求后, 获取服务器返回的原始数据 作为challenge(挑战)的response(响应), 使用password进行hmac, 服务器使用相同的hmac方式可验证客户端

由于服务器返回的数据有随机性, 也可以达到一次性认证, 且中间人拿不到password时无法作出challenge的response返回给服务器, 比MTProto的握手更加安全

## 新的探测方式: 客户端探测

很多协议的安全性只是针对服务器对客户端鉴权, 客户端不会验证服务器有效性（即单向鉴权）。因此防火墙可以通过伪造服务器包来探测客户端反应, 即反向探测, 来区分客户端是否为真的浏览器。（MTProto在ServerHello中使用相同的hmac算法, 天生屏蔽此探测）

## 如何识别Shadow TLS v2

防火墙随机截取一个正常的TCP连接, 在截取到TLS ClientHello后, 根据请求内容中的SNI字段, 将其流量劫持到该SNI的真正服务器。等待TLS握手完成后, Shadow TLS客户端会在Application Data前8个字节插入服务器的challenge的response

此时由于对面服务器并不是一个Shadow TLS服务器, 而是一个真的TLS服务器, Shadow TLS客户端在握手阶段会顺利完成。但是在发送hmac后, 因为并不是TLS协商好的加密, 服务器会直接抛出Alert (Encrypted Application Data), 然后FIN或者RST掉TCP连接, 此时可以确定客户端为ShadowTLS客户端, 从而对其连接的IP精准封杀。

代理协议通常会使用很多连接, 只需要随机抽取一个进行客户端探测, 就可以精准识别其客户端

# 目前推荐的代理协议

* Hysteria, TUIC (基于QUIC)
  防火墙对于QUIC目前没有任何的拦截和干扰, 可以放心使用

# 参考资料

* [https://telegra.ph/报告-中间盒如何识别代理流量-10-17](https://blog.upx8.com/go/aHR0cHM6Ly90ZWxlZ3JhLnBoLyVFNiU4QSVBNSVFNSU5MSU4QS0lRTQlQjglQUQlRTklOTclQjQlRTclOUIlOTIlRTUlQTYlODIlRTQlQkQlOTUlRTglQUYlODYlRTUlODglQUIlRTQlQkIlQTMlRTclOTAlODYlRTYlQjUlODElRTklODclOEYtMTAtMTc)

[取消回复](https://blog.upx8.com/3295#respond-post-3295)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")