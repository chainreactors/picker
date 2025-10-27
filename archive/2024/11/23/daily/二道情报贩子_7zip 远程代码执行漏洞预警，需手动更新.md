---
title: 7zip 远程代码执行漏洞预警，需手动更新
url: https://mp.weixin.qq.com/s?__biz=MzU5NTA3MTk5Ng==&mid=2247489645&idx=1&sn=dc385caabf6e354e8b3f586013cfed8e&chksm=fe76defec90157e835ae85c463b0ae6e799306276e550ac85a8dd802a1a61e56d88d976294ee&scene=58&subscene=0#rd
source: 二道情报贩子
date: 2024-11-23
fetch_date: 2025-10-06T19:18:36.951743
---

# 7zip 远程代码执行漏洞预警，需手动更新

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sY7YiaX0Dh2jicxyLOwJ4Fpgwvxt1t0cxVcnb0mrNgmTXQ6KSSc66ib9py2xHfqjoUicQic3VDDgSIEhvYuibAtdmjbA/0?wx_fmt=jpeg)

# 7zip 远程代码执行漏洞预警，需手动更新

二道情报贩子

7-zip zstandard 解压缩整数下溢远程代码执行漏洞

|  |  |
| --- | --- |
| CVE 编号 | CVE-2024-11477漏洞 |
| CVSS 评分 | 7.8 |

|  |  |
| --- | --- |
| 漏洞详情 | 此漏洞允许远程攻击者在受影响的 7-Zip 安装上执行任意代码。要利用此漏洞，需要与此库交互，但攻击媒介可能因实施而异。  具体缺陷存在于 Zstandard 解压缩的实现中。此问题是由于未正确验证用户提供的数据而导致的，这可能导致在写入内存之前出现整数下溢。攻击者可以利用此漏洞在当前进程的上下文中执行代码。 |
| 其他详细信息 | 已在 7-Zip 24.07 中修复  公告时间2024年11月20日 |

**注意：7zip没有任何更新按钮，必须手动去官网下载然后更新。**

https://www.7-zip.org/

需要注意，不要去其他网站下载最新版7zip，基本一大半都是银狐木马！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sY7YiaX0Dh2iaS8mtrK1dUrIzGbM7UYdiajsuibtSMXj2aYsQnZ5mwhTupx5rDHVU4n7XlXghkUcecCfeuCX0icJMoA/0?wx_fmt=png)

二道情报贩子

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sY7YiaX0Dh2iaS8mtrK1dUrIzGbM7UYdiajsuibtSMXj2aYsQnZ5mwhTupx5rDHVU4n7XlXghkUcecCfeuCX0icJMoA/0?wx_fmt=png)

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