---
title: 【安全圈】物联网云平台 OvrC 曝一系列漏洞，黑客可远程执行恶意代码
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066040&idx=3&sn=628c0be39463e5a5db076252eae42974&chksm=f36e7cb8c419f5ae9694e18d60dde2a26e6a3cdec1633acf1fe266e96be9e59868eaad6f37a5&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-18
fetch_date: 2025-10-06T19:14:56.041877
---

# 【安全圈】物联网云平台 OvrC 曝一系列漏洞，黑客可远程执行恶意代码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaZ8picWZtpojNtG0Sd01FibnEO6XboFG3r3t0dKHpkMJToBI4V03Q8YYlFjeSavbpaWhwwC1znLslw/0?wx_fmt=jpeg)

# 【安全圈】物联网云平台 OvrC 曝一系列漏洞，黑客可远程执行恶意代码

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

安全公司 Claroty 发布报告，曝光了一款海外流行的物联网设备云端管理平台 Ovr 内含的一系列重大漏洞。安全公司声称黑客可以接连利用这些漏洞实现在物联网设备上远程执行恶意代码，而根据 CVSS 风险评估，部分曝光的漏洞风险评分高达 9.2（满分 10 分）。

据悉，OvrC 物联网平台的主要功能是通过移动应用或基于 Web Socket 的界面为用户提供远程配置管理、运行状态监控等服务。自动化公司 SnapOne 在 2014 年收购了该平台，在 2020 年声称 OvrC 已拥有约 920 万台设备，而如今该平台预计坐拥 1000 万台设备。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaZ8picWZtpojNtG0Sd01FibnT69TF3VZKRU5YdaiaWk1c3suL95grRM6hU2jfDPh7bNayicBvDo72png/640?wx_fmt=jpeg&from=appmsg)

▲ OvrC 物联网平台下的设备

IT 之家参考安全报告获悉，相关漏洞主要包括输入验证不足、不当的访问控制、敏感信息以明文传输、数据完整性验证不足、开放式重定向、硬编码密码、绕过身份验证等，此类漏洞大多源于设备与云端接口的安全设计缺陷，黑客可利用漏洞绕过防火墙，避开网络地址转换（NAT）等安全机制，从而在平台设备上运行恶意代码。

参考 CVSS 风险评分，4 个被评为高危的漏洞分别是：输入验证不足漏洞 CVE-2023-28649、不当访问控制漏洞 CVE-2023-31241、数据完整性验证不足漏洞 CVE-2023-28386，以及关键功能缺乏认证漏洞 CVE-2024-50381，**这些漏洞的评分在 9.1 至 9.2 之间**。

关于漏洞的具体利用方式，研究人员指出，黑客可以先利用 CVE-2023-28412 漏洞获取所有受管设备的列表，再通过 CVE-2023-28649 和 CVE-2024-50381 漏洞强制设备进入 " 未声明所有权 "（Unclaim）状态。随后黑客即可利用 CVE-2023-31241 漏洞将 MAC 地址与设备 ID 匹配，并通过设备 ID 重新声明设备所有权，最终实现远程执行代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaZ8picWZtpojNtG0Sd01FibnK1hIED4ic75Qp6jSljSPP11lOR66PJ4KHb9mGGoGiaVNU0pmlCX7D48Q/640?wx_fmt=jpeg&from=appmsg)

值得注意的是，在研究人员报告后，大部分问题已于去年 5 月被修复，但仍有两个漏洞直到本月才得到解决，目前，该平台已完全修复相应漏洞。

***END***

阅读推荐

[【安全圈】手机主板植入恶意软件，98万部手机被远程操控！他在深圳被抓](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066024&idx=1&sn=1f067ab157601babcd85f75fb2d922a9&chksm=f36e7ca8c419f5be9fff3e8d1553cb7aebf180697c5d3b407014247a0aa1cbbba084b9acb79c&scene=21#wechat_redirect)

[【安全圈】非法购买38万条个人信息获利 获刑3年1个月](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066024&idx=2&sn=0992fce67c63d8241382ad131084b639&chksm=f36e7ca8c419f5be90f76bf60938259deed1098709925a964d4699975ce428aefef533f804a3&scene=21#wechat_redirect)

[【安全圈】利用“爬虫”技术非法抓取电商数据](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066024&idx=3&sn=168ceadc13c78d0c128517b6cfe7df0b&chksm=f36e7ca8c419f5bedf9c689eb7c76cd562abee0f8331f373e8494d8f1cf80322fb0b68c56086&scene=21#wechat_redirect)

[【安全圈】俄罗斯黑客利用文件拖放、删除操作触发 Windows 0day 漏洞攻击乌克兰目标](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066024&idx=4&sn=46592438737abae8701b9ba1b7160d86&chksm=f36e7ca8c419f5be0b5de8218474b566a05a2871e02c5f1b86f0a13769a0651d6087bd35a84d&scene=21#wechat_redirect)

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