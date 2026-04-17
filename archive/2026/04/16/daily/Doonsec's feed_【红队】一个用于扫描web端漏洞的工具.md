---
title: 【红队】一个用于扫描web端漏洞的工具
url: https://mp.weixin.qq.com/s/LOp_Rpv4-lAl1iWNya3gBg
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:48:14.485465
---

# 【红队】一个用于扫描web端漏洞的工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/k2PJfskYECnx8t67xQibITDCGVG0QtlsofFE0QNUgQjucxZxTIwCGuRE0icO7EMw22Zle7b4BwHib5XsYoPj2pXQRjurt0S2md3KzU0vBgLw7A/0?wx_fmt=jpeg)

# 【红队】一个用于扫描web端漏洞的工具

vulcat
vulcat

贝雷帽SEC

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**免责声明**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_gif/HVNK6rZ71oofHnCicjcYq2y5pSeBUgibJg8K4djZgn6iaWb6NGmqxIhX2oPlRmGe6Yk0xBODwnibFF8XCjxhEV3K7w/640?wx_fmt=gif&wxfrom=13&wx_lazy=1&tp=wxpic)

本公众号所提供的文字和信息仅供学习和研究使用，请读者自觉遵守法律法规，不得利用本公众号所提供的信息从事任何违法活动。本公众号不对读者的任何违法行为承担任何责任。工具来自网络，安全性自测，如有侵权请联系删除。

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**工具介绍**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

vulcat是一个用于扫描web端漏洞的工具，支持WAF检测、指纹识别、POC扫描、自定义POC等功能，当vulcat发现问题时会输出漏洞信息、漏洞利用的Request数据包等，使用者可以根据提示对漏洞进行手工验证、深入利用等

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**工具使用**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

```
git clone https://github.com/CLincat/vulcat.gitcd vulcatpip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simplepython3 vulcat.py -h
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k2PJfskYEClxWDYKftJ9pRYiaD9wpDK3xjX4YYq9IRWxj3FXiaTaG9lXp7ZSKlrQUWe7m6WfiaaDGapyFG8icnibib2fbTKYAdAZB1r00SfFT2QU4/640?wx_fmt=png&from=appmsg)

```
Usage:使用本工具, 代表您同意"vulcat/README.md"中的"行为规范和免责声明"; 如果您不同意, 请勿使用本工具

Usage: python3 vulcat.py <options>Examples:python3 vulcat.py -hpython3 vulcat.py --listpython3 vulcat.py -u https://www.example.com/python3 vulcat.py -f url.txt -o htmlpython3 vulcat.py -u https://www.example.com/ -v httpd --log 3python3 vulcat.py -u https://www.example.com/ -v cnvd-2018-24942 --shell
```

**下载链接**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

```
https://github.com/CLincat/vulcat
```

End

“点赞、在看与分享都是莫大的支持”

**工具精选**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

[【红队】一款安全测试工具集——Onyx](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494121&idx=1&sn=8675cf1677352620a57d68ff9f0b0686&scene=21#wechat_redirect)

[【红队】一款 AI 原生安全测试平台](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494139&idx=1&sn=5d8a98e0d0cb700c124aeaecae595d4c&scene=21#wechat_redirect)

[【红队】Webshell 管理与后渗透平台](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494098&idx=1&sn=cb7bc8f3cc7f59e6f80f4b56e7d4c1f9&scene=21#wechat_redirect)

[【红队】BProxy - 多级 SOCKS5 代理工具](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494084&idx=1&sn=dbc658a17e6ddc0dcd7c7857c841478a&scene=21#wechat_redirect)

[【红队】攻击面管理平台 (ASM)](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494076&idx=1&sn=e9c2ff60ccd065dc223c71042515268d&scene=21#wechat_redirect)

[【红队】ParrotOS 7.0 正式发布 代号：Echo](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494038&idx=1&sn=243e1105a439eb986fdc34534e6a8d19&scene=21#wechat_redirect)

[【红队】一款专为红队打造的主动资产指纹识别工具](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493898&idx=1&sn=3e395ade15061739c89f5d0a13645af4&scene=21#wechat_redirect)

[【蓝队】SamWaf开源轻量级网站防火墙](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493939&idx=1&sn=e56702a24dcae461024668aaea6aced3&scene=21#wechat_redirect)

[[蓝队] FastMonitor - 网络流量监控与威胁检测工具](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493925&idx=1&sn=a952c400c3ee63c8401ff57692745dd1&scene=21#wechat_redirect)

[【蓝队】漏洞全生命周期管理平台](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493803&idx=1&sn=10daa12b5a3523bf4a1ecc665890f917&scene=21#wechat_redirect)

[【蓝队】蓝队Ark神器 OpenArk v1.5.0](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493788&idx=1&sn=91a31e2d507cb9e0111c19dac98b315e&scene=21#wechat_redirect)

[【红队】矛·盾 武器库 v3.2](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493701&idx=2&sn=9cf7e304fee21328bac6d9bd97b81183&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/pM2klgicgT5dylTzXyrXBmex6dlAsZ0QJOQdzqcw2HpC49rnL0dTHNsWsOze4QmRYN7fPRoLdVK5MXs0DXtOvZw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/lcbWX2ticDCAOTEpzWaKCrzpsFeD3icYkGgVtUujgdbvmcria9XiaA4DMcYYnPh5ic6aFXVQPX7lNH11yfUEicgicXIZA/0?wx_fmt=png)

贝雷帽SEC

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/lcbWX2ticDCAOTEpzWaKCrzpsFeD3icYkGgVtUujgdbvmcria9XiaA4DMcYYnPh5ic6aFXVQPX7lNH11yfUEicgicXIZA/0?wx_fmt=png)

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