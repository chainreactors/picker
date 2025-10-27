---
title: 【安全圈】攻击者正滥用Gophish传播远程访问木马程序
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065447&idx=4&sn=7f2209cef48eacf737d769706edac8b2&chksm=f36e62e7c419ebf1a3e4c76ef3bbf7e841d71f32846a696f7fed91ac40fb84bac4155a9f1176&scene=58&subscene=0#rd
source: 安全圈
date: 2024-10-25
fetch_date: 2025-10-06T18:52:11.247900
---

# 【安全圈】攻击者正滥用Gophish传播远程访问木马程序

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljChO1pW8DeTrvJ4hzjZicC14ziaHfVicY3gxO486iat7kFpOV2U70GquQzDceBGUWia9VHN5gjIbkhV8Q/0?wx_fmt=jpeg)

# 【安全圈】攻击者正滥用Gophish传播远程访问木马程序

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络攻击

据The Hacker News消息，名为Gophish 的开源网络钓鱼工具包正被攻击者用来制作DarkCrystal RAT（又名 DCRat）和PowerRAT 远程访问木马，目标针对俄国用户。

Gophish 允许组织通过利用简易的模板来测试其网络钓鱼防御措施，并启动基于电子邮件的跟踪活动。但攻击者利用Gophish制作网络钓鱼邮件，并伪装成Yandex Disk 链接（“disk-yandex[.]ru“），以及伪装成 VK 的 HTML 网页，VK 是俄罗斯最主要使用的社交网络。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljChO1pW8DeTrvJ4hzjZicC1RIHbhFERE4Z1WkUPHQbYb1lYk0icvMchzYr3icXQfOXFM5Mm3RT1fS7A/640?wx_fmt=jpeg&from=appmsg)感染链

据观察，攻击者根据所使用的初始访问载体推送包含DCRat 或 PowerRAT恶意木马的Microsoft Word 文档或嵌入 JavaScript 的 HTML。当受害者打开 maldoc 并启用宏时，就会执行一个恶意 Visual Basic (VB) 来提取 HTML 应用程序 (HTA) 文件（"UserCache.ini.hta"）和 PowerShell 加载器（"UserCache.ini"）。该宏负责配置 Windows 注册表项，以便每次用户在设备上登录其帐户时都会自动启动 HTA 文件。

HTA 会删除一个负责执行 PowerShell 加载程序的 JavaScript 文件（“UserCacheHelper.lnk.js”）。JavaScript 使用名为“cscript.exe”的合法 Windows 二进制文件执行。

研究人员称，伪装成 INI 文件的 PowerShell 加载程序脚本包含PowerRAT 的 base64 编码数据块有效载荷 ，该数据块在受害者的机器内存中解码和执行。

除了执行系统侦察外，该恶意软件还会收集驱动器序列号并连接到位于俄罗斯的远程服务器以接收进一步的指示。如果未从服务器收到响应，PowerRAT 将配备解码和执行嵌入式 PowerShell 脚本的功能。到目前为止，分析的样本中没有一个包含 Base64 编码的字符串，表明该恶意软件正在积极开发中。

与此类似，采用嵌入恶意 JavaScript 的 HTML 文件的替代感染链会触发一个多步骤过程，从而导致部署 DCRat 恶意软件。

DCRat 是一种模块化的恶意软件 ，可以窃取敏感数据、捕获屏幕截图和击键，提供对受感染系统的远程控制访问，并导致其他文件的下载和执行。

除了俄罗斯，在临近的乌克兰、白俄罗斯、哈萨克斯坦、乌兹别克斯坦和阿塞拜疆也监测到了恶意活动，显示整个俄语片区使用者都是攻击者的针对目标。

参考来源：Gophish Framework Used in Phishing Campaigns to Deploy Remote Access Trojans

***END***

阅读推荐

[【安全圈】水军狂喜？Claude AI现在可以控制PC并自己移动鼠标完成任务操作](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065432&idx=1&sn=b934e5d1eacd20db87c29744a60e9747&chksm=f36e62d8c419ebcee92754914fb085938a5fd00ef2e9c04cb09422f2cfe22a02973d1a40af0e&scene=21#wechat_redirect)

[【安全圈】高通64款芯片存在0Day漏洞](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065432&idx=2&sn=c5c869e24ab938b185e97679ede50f75&chksm=f36e62d8c419ebced3dfe7c7c112dd6fa9c2cce62710befa6d8ed1a4619a93818b4963036f5a&scene=21#wechat_redirect)

[【安全圈】K8s曝9.8分漏洞，黑客可获得Root访问权限](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065432&idx=3&sn=8dd024db6fb200b80ea9bd4b0ab86a5a&chksm=f36e62d8c419ebceefe101ff0bc1b587b6e99447dcd96e41f562f8cf9aa4303b7eec61418712&scene=21#wechat_redirect)

[【安全圈】三星设备曝出高危零日漏洞，已在野外被利用](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065432&idx=4&sn=e821667ba35126b55834a52a98cbf559&chksm=f36e62d8c419ebcee6861d148234c4240e97f32ff3ae4d2ecce99feef2c26006edc5b720092f&scene=21#wechat_redirect)

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