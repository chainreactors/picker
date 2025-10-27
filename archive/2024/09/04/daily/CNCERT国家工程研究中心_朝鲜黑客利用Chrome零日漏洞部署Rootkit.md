---
title: 朝鲜黑客利用Chrome零日漏洞部署Rootkit
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546725&idx=2&sn=c4dbbf0aae29b7f972e6b36b2d394146&chksm=fa9381a4cde408b280ee644051703f8b7b81e4d06c664d4507ae8d507ed10703620ffa200d45&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-09-04
fetch_date: 2025-10-06T18:28:59.970255
---

# 朝鲜黑客利用Chrome零日漏洞部署Rootkit

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176lHEbKyOoRlvtNL7nyf71CbjUJj2C2KeicDo8UynDKhCbiaG8ElnWtylR19FWpHdwJ50T8LKndaquRw/0?wx_fmt=jpeg)

# 朝鲜黑客利用Chrome零日漏洞部署Rootkit

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176lHEbKyOoRlvtNL7nyf71CbzucSlFpDqBMfdfEaZLjN7fUydicMNFGYCn7uibnYm2rJolicOWfibwsibOw/640?wx_fmt=png&from=appmsg)

朝鲜黑客在使用Windows内核漏洞获得 SYSTEM权限后，利用最近修补的谷歌Chrome零日漏洞（CVE-2024-7971）部署 FudModule Rootkit。

“我们以高可信度评估，观察到CVE-2024-7971漏洞被朝鲜黑客利用，以在加密货币行业获取经济利益。”微软8月30日发声，并将攻击归因于Citrine Sleet（之前跟踪为 DEV-0139）。

谷歌上周修补了CVE-2024-7971零日漏洞，将其描述为Chrome V8 JavaScript引擎的一个类型混淆弱点。

此漏洞使威胁行为者能够在目标的沙盒 Chromium渲染器进程中获得远程代码执行，将用户重定向到他们控制的网站（voyagorclub[.]space）。

攻击者从沙盒逃脱后，利用受感染的网络浏览器下载一个Windows沙盒逃逸漏洞，该漏洞针对Windows内核中的CVE-2024-38106漏洞（在本月的补丁星期二期间修复），这使他们获得SYSTEM权限。

黑客还下载FudModule rootkit并将其加载到内存中，用于内核篡改和执行直接内核对象操作（DKOM），并允许他们绕过内核安全机制。

自2022年10月被发现以来，此Rootkit也被另一个朝鲜黑客组织Diamond Sleet使用，Citrine Sleet与该组织共享其他恶意工具和攻击基础设施。

Citrine Sleet以金融机构为目标，专注于加密货币组织和相关个人，此前曾与朝鲜侦察总局121局有联系。

其他网络安全供应商将这个朝鲜威胁组织跟踪为AppleJeus、Labyrinth Chollima和UNC4736，美国政府将朝鲜政府资助的恶意行为者统称为Hidden Cobra。

外媒表示，朝鲜黑客以利用伪装成合法加密货币交易平台的恶意网站而闻名。

他们通过这些恶意网站，向潜在受害者发送虚假工作申请，或者使用被武器化的加密货币钱包和交易应用程序来感染受害者。

攻击团体UNC4736在2023年3月对视频会议软件制造商3CX的基于Electron的桌面客户端进行了木马化攻击。

此前他们对股票交易自动化公司Trading Technologies进行供应链攻击，入侵了网站以推送被木马化的X\_TRADER软件版本。

谷歌的威胁分析小组（TAG）在2022年3月的一份报告中还将AppleJeus与Trading Technologies网站的入侵联系起来。美国政府也警告称，多年来朝鲜支持的黑客一直使用AppleJeus恶意软件针对与加密货币相关公司和个人。

原文来源：E安全

“投稿联系方式：sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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