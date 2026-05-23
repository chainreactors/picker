---
title: Apache Flink 高危漏洞可导致远程代码执行攻击
url: https://mp.weixin.qq.com/s/WIXEfyxPSfttZoR9cYGX_w
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:34:13.474482
---

# Apache Flink 高危漏洞可导致远程代码执行攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2pdVIaBRXHH59IxKfXWXTxnPbGhBHTHZX6m6XckOhFTqoSLxuJZS01rMKaEsc4jNXGhp3Ypr7cffl8QWeKkjibfa5ic9nicUN7UM/0?wx_fmt=jpeg)

# Apache Flink 高危漏洞可导致远程代码执行攻击

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX13o19L4T4FYZCm8IpIl1FAMy2iaia2VzkjVUOOYDgcIMrmp7Gxf63Nch3Seb6wsPNpmYsTeTf8sMiaBncia2FThABfvFviaXuflM6U/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2KMGAC2GUjGyfiadicX85DkSrYUiaNHQZQdfr8Irs3z1AgW5f3ujHyScltVzEvAtT6ibPibDu6ozqLI69IpYDXpZNvAl6nicA2Ck3pQ/640?wx_fmt=jpeg)

Apache Flink近日披露一个编号为CVE-2026-35194的高危漏洞，该漏洞通过平台代码生成引擎中的SQL注入缺陷，使分布式数据处理环境面临远程代码执行（RCE）攻击风险。

Part01

漏洞技术分析

该漏洞存在于Apache Flink的SQL代码生成机制中，用户提供的输入在嵌入动态生成的Java代码前未经过适当净化处理。这使得具有查询提交权限的认证用户能够注入恶意负载，突破预期的字符串边界并执行任意代码。

具体受影响组件包括：

* Flink 1.15.0 版本引入的JSON函数
* Flink 1.17.0 版本引入的带ESCAPE子句的LIKE表达式

攻击者可通过构造特殊SQL查询操纵代码生成过程，最终在Flink集群的 TaskManager节点上实现任意代码执行。受影响版本包括：

* Apache Flink 1.15.0 至 1.20.x（1.20.4 之前版本）
* Apache Flink 2.0.0 至 2.x（2.0.2、2.1.2 和 2.2.1 之前版本）

Part02

漏洞危害评估

Apache贡献者Martijn Visser于2026年5月15日公开披露该漏洞，鉴于其对生产集群的影响，将其评级为高危。漏洞根本原因在于SQL到Java代码转换过程中的不安全字符串插值：

* 用户控制的输入未经适当转义或验证直接插入生成代码
* 攻击者可突破生成Java代码中的字符串字面量
* 注入任意Java表达式或方法调用
* 在分布式TaskManager节点上执行恶意代码

考虑到Flink的架构特性，成功利用该漏洞可能导致：

* 整个集群被攻陷
* 数据被篡改
* 攻击者在环境中横向移动

Part03

修复建议

Apache已发布修复版本（1.20.4、2.0.2、2.1.2 和 2.2.1），建议用户立即升级。其他缓解措施包括：

* 将查询提交权限限制为可信用户
* 监控异常SQL查询活动模式
* 在TaskManager节点上实施运行时安全控制

由于该漏洞可能造成严重的运营和数据安全风险，建议生产环境中使用Apache Flink的组织优先实施补丁更新。

参考来源：

Critical Apache Flink Vulnerability Enables Remote code execution Attacks

https://cybersecuritynews.com/apache-flink-vulnerability/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0TPDSBGWyOrBX6roghTcfJ7S0Uk6LPc6NiazIJCibS6wTdC64AxlpIAv3YZ2LoZFsJy3UHwic3ohlaRGRMZkKBW03QD5AMj5yuicM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651338385&idx=1&sn=a442efc5bf8726e3e4239bc246e2976b&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2A30nW87bmYJO7PWcHicOLnjA5DRaqykn6a3r9Nvg2PUTX1XkGuXcekoXza0aIXeq8O4ZwnhjLdFba5NEv5NQetNb0KjM9Mnb8/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3hWWNDwlRbiaTEEQj4EIurF3S0vPh9QweSDbsic4yvYiciaKParOk9hkwUeq3mJNo2c1Zo7F2AdxRDbnThPEC6H6lv9ht1D7DEaE4/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1fOwGsWQ1vfZuwVLNHUTvOIJdRl2Mbqia302wddaZvfEibdE4pHtrCAvtapoLamks56Eq4ONW4zygw6baL4Z8nYcT6OZ9xhg7xg/640?wx_fmt=png)

预览时标签不可点

内容含AI生成图片

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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