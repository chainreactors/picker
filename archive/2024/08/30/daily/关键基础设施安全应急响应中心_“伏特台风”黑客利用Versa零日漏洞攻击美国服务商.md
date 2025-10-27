---
title: “伏特台风”黑客利用Versa零日漏洞攻击美国服务商
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247545541&idx=3&sn=2ffde667d54880ea7961dafc7249ce12&chksm=c1e9be94f69e378215095598a5295a9b92fb3857c31c5f1e5af9439a3f31195ca955cfac8e97&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-08-30
fetch_date: 2025-10-06T18:05:20.379466
---

# “伏特台风”黑客利用Versa零日漏洞攻击美国服务商

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogs6TibDytX0iaBjw9aSGGiaPiasLP54YRgWhbicCqib6Fbj13a7beqR0K19LbVEz5jC7dGOdvt1tLeTrOhg/0?wx_fmt=jpeg)

# “伏特台风”黑客利用Versa零日漏洞攻击美国服务商

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogs6TibDytX0iaBjw9aSGGiaPiasKSibvgPpn8dMjqnOQNOZR47yALCsnkO58HWYlsmPDsCPQAa8DlwQLEQ/640?wx_fmt=png&from=appmsg)

8月27日，外媒BleepingComputer报道，黑客组织Volt Typhoon（伏特台风）利用Versa Director零日漏洞上传自定义Webshell，窃取凭据并破坏美国公司网络。

本周周一8月26日，Versa公司宣布他们修复了一个被追踪为CVE-2024-39717的高风险漏洞。这个漏洞被未具名的民族国家黑客组织至少利用过一次。

该漏洞存在于上传自定义图标Versa Director GUI的功能中。漏洞允许具有管理员权限的威胁行为者上传伪装成PNG图像的恶意Java文件，然后远程执行这些文件。

Versa表示Director版本21.2.3、22.1.2和22.1.3受到该漏洞的影响。升级到最新版本22.1.4将修复漏洞，管理员应查看供应商的系统强化要求和防火墙指南。

在最近的事件中，Volt Typhoon利用Versa Director中的漏洞上传了一个名为 VersaMem的复杂、定制的Webshell。

此WebShell用于拦截和收集凭据，以及在受感染的服务器上执行任意恶意代码，同时避免被发现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QmbJGbR2j6zggdhuQFn2ibDcvfdhOPR3UOJxuaTsrclF7St4Q2FZiaB4JicbBdCwZVgoc69MlLHHDpxFpOBydahYg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

Versa Directo上的Volt Typhoon攻击流程

来源：Lumen的Black Lotus Labs

据报道，Volt Typhoon最新活动目标包括4家美国公司和1家非美国公司，他们属于互联网服务提供商、托管服务提供商和信息技术领域企业。

Lumen的Black Lotus Labs研究人员在6月初发现了Versa零日漏洞。最初版本是从新加坡上传到VirusTotal病毒库的。这个上传时间大约比在美国最早发现Versa Director服务器漏洞事件早了五天。

“我们怀疑威胁行为者可能在对美国目标发起攻击之前，先在其他地区测试了他们的攻击手段。“该公司补充道。当前恶意软件版本在VirusTotal上没有被检测出来。

关于伏特台风，百度百科内容：“伏特台风”（Volt Typhoon），由微软公司根据其黑客组织命名规则命名而来，真实面目是国际勒索软件组织，来自“伏特台风”的恶意程序样本并未表现出明确的国家背景黑客组织行为特征，而是与“暗黑力量”勒索病毒等网络犯罪团伙的关联程度明显。

原文来源：E安全

“投稿联系方式：sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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