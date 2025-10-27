---
title: 漏洞风险提示 | Smartbi 远程命令执行漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIwMDk1MjMyMg==&mid=2247491264&idx=1&sn=cdc5b203155c0997eeddc6494479e0d1&chksm=96f401ada18388bb8da71f9d5033328f5d9c935827bc32a93534551b9c567a08d8704f14f8a3&scene=58&subscene=0#rd
source: 长亭安全课堂
date: 2023-03-03
fetch_date: 2025-10-04T08:32:25.514660
---

# 漏洞风险提示 | Smartbi 远程命令执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FOh11C4BDicTN4ddiciaL3cib93KeLMoV5lNtgbuA6KMWR0Nyt15BiaONlC5Af4ak0iav7cfTIqKTbFMZhYQ7eKia7Lew/0?wx_fmt=jpeg)

# 漏洞风险提示 | Smartbi 远程命令执行漏洞

长亭安全应急响应中心

长亭漏洞风险提示

**Smartbi 远程命令执行漏洞**

Smartbi是广州思迈特软件有限公司旗下的商业智能BI和数据分析品牌，致力于为企业客户提供一站式商业智能解决方案。Smartbi三大产品包括企业报表平台、自助分析平台、数据挖掘平台，覆盖企业从传统BI到自助BI，再到智能BI的三个应用阶段，满足从数据准备到数据分析、交流共享等各个环节的功能需求。

2月28日，Smartbi发布安全更新，修复了一处远程命令执行漏洞。

**漏洞描述**

Smartbi 大数据分析平台存在远程命令执行漏洞，远程且未经授权认证的攻击者可利用stub接口对先前“DB2 命令执行漏洞”的补丁进行绕过，构造并发送恶意数据包到目标服务端利用此漏洞，从而在服务端执行任意恶意命令、获取系统权限。

**影响范围**

* V7 <= Smartbi <= V10.5.8

**解决方案**

Smartbi在2月28日发布安全补丁修复了此漏洞，用户可在官网下载获取补丁包安装：https://www.smartbi.com.cn/patchinfo

Smartbi V9.3及以后版本的用户也可登陆到管理后台，打开系统监控面板，进入“安全补丁”界面，点击“在线更新”按钮，系统会到官网上自动获取最新的安全补丁文件进行更新：

![](https://mmbiz.qpic.cn/mmbiz_png/FOh11C4BDicTN4ddiciaL3cib93KeLMoV5lNFJzmAibSBu8gC1zPkq8eRHZ8ypbRtbd6brKD7TG3a2x7OFf2zbIrxKA/640?wx_fmt=png)

**产品支持**

**全悉**：已发布更新包支持该漏洞检测。

**云图**：默认支持 Smartbi 版本指纹，受影响范围检测规则已发布。

**洞鉴**：已发布更新包支持该漏洞检测。

**参考资料**

* https://wiki.smartbi.com.cn/pages/viewpage.action?pageId=50692623
* https://www.smartbi.com.cn/patchinfo

![](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC7ia5uzmRe9JvNErXe95W4qTgEKhVa7kdaxpwJXC0oKXeFt5vGN4KmJv2mvcYkYtrd7cev0vkAhY7A/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/FOh11C4BDicTN4ddiciaL3cib93KeLMoV5lNwiaHxpmgCqYtGOn49gUHyxAibXxyydwOnLTT2TKTJMs1RsvgAMPXiah1A/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicRRVzLmQjSLiavxtAic7KOwrG3LmOSNQjmWlwYtZXgu57OV1t9yic9E4GkU2noIicAq1nGlNT0MRiaBCMg/0?wx_fmt=png)

长亭安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicRRVzLmQjSLiavxtAic7KOwrG3LmOSNQjmWlwYtZXgu57OV1t9yic9E4GkU2noIicAq1nGlNT0MRiaBCMg/0?wx_fmt=png)

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