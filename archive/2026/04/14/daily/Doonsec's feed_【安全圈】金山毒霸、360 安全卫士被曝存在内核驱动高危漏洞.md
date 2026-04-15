---
title: 【安全圈】金山毒霸、360 安全卫士被曝存在内核驱动高危漏洞
url: https://mp.weixin.qq.com/s/y0N3ebgcZeQZmMnoCBDLLg
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:41:29.157435
---

# 【安全圈】金山毒霸、360 安全卫士被曝存在内核驱动高危漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyEpyM9GkVjtF3OVWE0cmZ42gRpRyfplDlicThqMDOickJhTsozD6nklQYhLr1ldCLJqh5qWM938eqicibyCdPJxhGYWnNXRSgPLTEA/0?wx_fmt=jpeg)

# 【安全圈】金山毒霸、360 安全卫士被曝存在内核驱动高危漏洞

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

安全研究人员 Patrick Saif（@weezerOSINT）昨日（4 月 13 日）在 X 平台发布推文，**披露金山毒霸与 360 安全卫士两款主流杀毒软件的内核驱动存在高危漏洞。**

金山毒霸的 kdhacker64\_ev.sys 驱动在处理用户输入后，分配的缓冲区大小仅为所需的一半，导致 1160 字节数据写入 584 字节空间，直接引发 512 字节的内核池溢出。该驱动拥有有效的 EV 签名，攻击者可利用此漏洞完全控制系统。

360 安全卫士的 DsArk64.sys 驱动允许通过 IOCTL 接口传入 4 字节进程 ID，并在 Ring 0 层级调用 ZwTerminateProcess 强制终止任意进程，甚至能绕过 PPL（受保护进程）机制。

更严重的是，其内核读写功能使用 AES-128-CBC 算法，让解密密钥硬编码在二进制文件的.data 段中，且所有版本使用同一密钥，且该驱动通过了 WHQL 签名认证。

目前两个漏洞已提交至 LOLDrivers 数据库，均未获 CVE 编号且不在 HVCI 屏蔽名单中。攻击者利用这些漏洞可从普通用户提权至 SYSTEM，绕过 KASLR 并窃取内核凭据，甚至修改内核回调表隐藏恶意行为。鉴于涉事驱动具备 EV 或 WHQL 签名，攻击者无需在目标机器安装软件即可加载恶意载荷。

***END***

阅读推荐

[【安全圈】黑客利用 Claude 和 ChatGPT 入侵多家墨西哥政府机构](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075617&idx=1&sn=ae5ccccf31e54fadb3a3ae3a96442518&scene=21#wechat_redirect)

[【安全圈】国际联合行动识别超 2 万名加密货币诈骗受害者](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075617&idx=2&sn=e0977dea287f90ca2172e2f363610190&scene=21#wechat_redirect)

[【安全圈】十亿条 CISA KEV 修复记录分析揭示人力安全模式的极限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075617&idx=3&sn=37b38b70dab479d02d3f08d8edad460b&scene=21#wechat_redirect)

[【安全圈】知名电脑检测软件 CPU-Z、HWMonitor 被入侵！安装包被投毒 开发者回应](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075585&idx=1&sn=beb1c4000130b2ff57bb5d4e98be2556&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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
在看
，轻点两下取消在看
分享
留言
收藏
听过