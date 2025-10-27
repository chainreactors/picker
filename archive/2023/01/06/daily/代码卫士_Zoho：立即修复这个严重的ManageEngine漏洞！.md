---
title: Zoho：立即修复这个严重的ManageEngine漏洞！
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515203&idx=2&sn=b4c1c37a3e9a0cec0dc518765c86b736&chksm=ea948d29dde3043f45edbaf7748079fecbc26a7462e00af08c08cf7d77d9c07d2ccd669686f9&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-01-06
fetch_date: 2025-10-04T03:10:12.794988
---

# Zoho：立即修复这个严重的ManageEngine漏洞！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRWK42xqr5Pr25UUF1Xc5ficLqUOicHlibiaOBgwKwdm75YMicx2o7Hy0yeh7YXMsU4u3E0VL4Bp2nlAiaw/0?wx_fmt=jpeg)

# Zoho：立即修复这个严重的ManageEngine漏洞！

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Zoho 督促客户修复影响多款ManageEngine产品的一个严重漏洞。本周一，Zoho 公司提醒称，“该安全公告是为了告知大家，我们检测到了一个严重的安全漏洞。”**

该漏洞的编号是CVE-2022-47523，是位于Password Manager Pro 安全密码管理器PAM360特权权限管理软件和Access Manager Plus特权会话管理解决方案中的一个SQL注入漏洞。该漏洞如遭成功利用，可导致攻击者对后台数据库具有未认证访问权限，并导致他们执行自定义查询，访问数据库表条目。

Zoho 公司指出，“我们在内部框架中发现一个SQL注入漏洞（CVE-2022-47523），可导致所有用户获得对后台数据库的未认证访问权限。”该公司还提到，“鉴于该漏洞的严重性，强烈建议客户立即升级至PAM360、Password Manager Pro和Access Manager Plus的最新build版本。”

Zoho 公司表示，上个月通过逃逸特殊字符和增加恰当验证的方式修复了该漏洞。要更新安装，需要受陷下载产品最新版本。接着是根据每个产品Upgrade Pack页面上的可用升级指令，部署最新build。

今年9月份，CISA提醒称另外一个ManageEngine 严重漏洞（CVE-2022-35405）已遭在野利用，用于获得运行PAM360、Access Manger Plus和Password Manager Pro的未修复服务器上的远程代码执行权限。

美国联邦民事行政部门 (FCEB)机构有三个月的时间修复这些易受攻击的系统并确保网络不受利用尝试困扰。

Zoho ManageEngine 服务器近年来一直遭受攻击，例如，Desktop Central 实例被黑，自2020年7月起，受陷组织机构网络的访问权限就在黑客论坛上出售。在2021年8月至10月期间，国家黑客组织被指攻击ManageEngine服务器。为了应对大规模的攻击情况，FBI和CISA联合发布两份安全公告，提醒注意国家黑客组织利用ManageEngine 漏洞在关键基础设施组织机构网络中安装后门。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[CISA提醒修复Zoho ManageEngine RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514082&idx=2&sn=a353a69d6d2c5a3f065ae133b67f4256&chksm=ea948688dde30f9e50183652d6391b23fd17af36c96c1ebcf3a7f40b0034288e9a22f16cbcd8&scene=21#wechat_redirect)

[Zoho：尽快修复已遭利用的 ManageEngine 严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509574&idx=1&sn=4087ce0dae2fc5f7466509361bc75784&chksm=ea94972cdde31e3a15e2a7fe2d009f93789638cd6b891a8e91b22cbee7676592795119f0ebd8&scene=21#wechat_redirect)

[FireEye红队失窃工具大揭秘之：分析复现Zoho ManageEngine RCE (CVE-2020-10189)](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247499078&idx=1&sn=2d07caa663bb17250a5d4d858c1fcd71&chksm=ea94cc2cdde3453a3afe795878114bb9cd5177d68024846d7b633a0fa8ad80611e92c4931ecd&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/zoho-urges-admins-to-patch-critical-manageengine-bug-immediately/

题图：Pexels License‍

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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