---
title: 第98篇：Struts2全版本漏洞检测工具19.32版本更新
url: https://mp.weixin.qq.com/s?__biz=MzkzMjI1NjI3Ng==&mid=2247486801&idx=1&sn=72a8c7921aa79da5d7bf4e41738ba9d3&chksm=c25fc22af5284b3c29e420c5c719d0b6ba4c2839dc0182985a203cb3dd1867a1d8babd0496b4&scene=58&subscene=0#rd
source: 希潭实验室
date: 2024-07-12
fetch_date: 2025-10-06T17:45:22.257971
---

# 第98篇：Struts2全版本漏洞检测工具19.32版本更新

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/OAz0RNU450Ch5THbGDooyicFbAXp8dcYYzBJpLiaQACbQmEtNvQpJKcnVmGiakroibK7xqYoRFgyicw5Td61Ricn1tbQ/0?wx_fmt=jpeg)

# 第98篇：Struts2全版本漏洞检测工具19.32版本更新

原创

abc123info

希潭实验室

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9Lbc0INLwTJTZT1GaNutZrfDn6csvjBoS2ox0efLUEexXqPEcVbYfbLo8w/640?wx_fmt=png)

##

## **Part1 前言**

**大家好，我是ABC\_123**。在8年前（2016年5月）使用netbeans依靠java语言编写了Struts2漏洞检测工具，期间一直不断更新，更新时间已达8年之久。现在ABC\_123对于此工具的更新，更多是一种情怀，也是一种研究性实验性工作。目前Struts2框架在外网还能见到一些，在内网环境中仍然会遇到很多，于是它更多地成为了一个内网横向的漏洞选择。最近根据几个网友的反馈，对工具进行了几个重要更新，文末有漏洞检测工具的下载。

**建议大家把公众号“希潭实验室”设为星标，否则可能就看不到啦！**因为公众号现在只对常读和星标的公众号才能展示大图推送。操作方法：点击右上角的【...】，然后点击【设为星标】即可。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OAz0RNU450Dq1Q8s4COc7InkMO0jIGjiaGho1fcJicpibWB4vzvIM1wAib9TiakVECbIM5S0mHCTTeGJJibWtCe25vXw/640?wx_fmt=jpeg&from=appmsg)

## **Part2 技术研究过程**

* ## **新增自定义HTTP请求头功能**

当前网站的鉴权方式除了Cookie，还存在JWT鉴权、HTTP Basic验证、HTTP请求头校验、Referer校验等等。因此，我重新封装了HTTP发包模块，使工具支持自定义多行HTTP请求头，程序会在每次发送请求上自动加上。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450Ch5THbGDooyicFbAXp8dcYY7jibnW5dX5VLnAUAKFiaFBnF8Oicawaicf1ic8PYnudVo47OiaKp8TjHRcwA/640?wx_fmt=png&from=appmsg)

* ## **优化S2框架的Log4j2漏洞的检测**

此版本对功能的检测语句进行了更新，提升S2框架下Log4j2漏洞检测的准确度。我原本想做成添加dnslog配置文件进行自动化检测，但是考虑到现在的dnslog服务都不太稳定，而且dnslog经常容易被安全设备加入规则，所以放弃了自动化检测的想法，还是需要靠大家手工填写dnslog进行漏洞判断。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450Ch5THbGDooyicFbAXp8dcYY9QUu8FN1pcIQCDxxren5DIZuav8HPVyBYcFibIlXdicIZckC7XQFxohg/640?wx_fmt=png&from=appmsg)

* ## **更正S2-048漏洞的检测逻辑**

之前的S2-048漏洞的检测流程，还是有一些不完善的地方，所以我对检测语句进行了优化。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450Ch5THbGDooyicFbAXp8dcYYNhf73epdWWYEguZZJNgEcvf0UpB2LwwxFMgFS25xicYjNXzQiam19Ricg/640?wx_fmt=png&from=appmsg)

* ## **新增S2-052漏洞利用**

S2-052漏洞在代码审计或者一些情况下还是可以遇到的，只是这种漏洞基本上只能结合人工进行利用，工具很难实现自动化。所以我在这里提供了EXP生成功能，方便大家使用，对于S2-052漏洞的利用，请注意**Content-Type: application/xml**的部分，判断漏洞建议可以先**ping dnslog**一下，判断漏洞是否存在。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450Ch5THbGDooyicFbAXp8dcYYKDr1FdichJ1ZSxfY2QVicElJXWbiaiaZ0zcX9Lgb9AKKhtO0A8uaxVEia9Q/640?wx_fmt=png&from=appmsg)

* ## **新增S2-053漏洞利用**

S2-053这个漏洞基本上很难实现自动化的检测与利用，在代码审计或者一些特殊情况下可以派上用场。所以我在这里也是提供了EXP生成功能，方便大家日常的渗透测试。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450Ch5THbGDooyicFbAXp8dcYY2zW5HtcUK75nwmsEmcE2LlZMGZ4ia8KRBe4DvgvPdcOQ6WFly5JKIEA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450Ch5THbGDooyicFbAXp8dcYYPgaXu7iaAibBr4JJyZ9GXVFHsynmE3ek1OpgicEdEUQM31DEt0jxCRPWQ/640?wx_fmt=png&from=appmsg)

关注公众号"**希潭实验室**”，回复“**0711**”，即可得到此版本Struts2漏洞检测工具的下载地址。

## **Part3 总结**

**1.**  技术总是不断革新的，工具也需要跟着更新。

**2.**  对于工具有什么建议，欢迎公众号后台给我反馈或者在github上给我留言。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450A5qqg2iaK6KIYYR8y6pF5Rh3JHDibOKOop204nXz618iawdRb8dABicMPtHb2PkJE8x6koJO5HyuwZJQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**公众号专注于网络安全技术，包括安全咨询、APT事件分析、红队攻防、蓝队分析、渗透测试、代码审计等，99%原创，敬请关注。**

**Contact me: 0day123abc#gmail.com**

**(replace # with @)**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

希潭实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

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