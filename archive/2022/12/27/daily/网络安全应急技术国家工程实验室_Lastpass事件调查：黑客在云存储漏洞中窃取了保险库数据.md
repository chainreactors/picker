---
title: Lastpass事件调查：黑客在云存储漏洞中窃取了保险库数据
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247533490&idx=3&sn=baae970d2a5f1c24887478ff3acd4bd2&chksm=fa93f573cde47c65b734878c588013b0478eb5b37efdd27df76b95b7f61120e753363e65cd0c&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2022-12-27
fetch_date: 2025-10-04T02:33:39.650204
---

# Lastpass事件调查：黑客在云存储漏洞中窃取了保险库数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kiaYNRfKIQOsGyjxBPUt14naH0qOwWSox7W85QnibOyibBQKfZPAh937y3wiar278u94tmYIulzpOLDA/0?wx_fmt=jpeg)

# Lastpass事件调查：黑客在云存储漏洞中窃取了保险库数据

网络安全应急技术国家工程中心

据Bleeping Computer报道，LastPass当地时间12月22日透露，攻击者在今年早些时候使用2022年8月事件中窃取的信息侵入其云存储，窃取了客户的保险库数据。

此前，11月30日，该公司首席执行官卡里姆·图巴（Karim Toubba）曾公开承认遭黑客攻击致数据泄露，但他表示黑客仅获得了部分客户的关键信息，客户的密码仍被安全加密。这是一年内LastPass发生的两次因云存储漏洞而发生的安全事件。

该公司透露，8月事件的攻击者在被驱逐之前，对其内部系统访问了四天。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39Q1ZXuBOrojcRe5RPNtKpd4IQIbPe0cQk7uWbsqvAnwH7OLOcBS4UmJv7jEkO94mfnEcLFe3kBzA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

攻击者利用从Lastpass开发者环境中窃取的“云存储访问密钥和双存储容器解密密钥”，获得了对Lastpass云存储的访问。

图巴称，LastPass使用云存储服务来存储生产数据的存档备份。“威胁者从备份中复制了包含客户基本账户信息和相关元数据的信息，包括公司名称、最终用户名称、账单地址、电子邮件地址、电话号码以及客户访问LastPass服务的IP地址。”

“威胁者还能够从加密的存储容器中复制客户的保险库数据备份，这些数据以专有的二进制格式存储，既包含未加密的数据如网站URL，也包含完全加密的敏感字段如网站用户名、密码、安全笔记和表格填写的数据。”

但是，LastPass坚称用户的加密数据和主密码仍是安全的。图巴称，LastPass从不知道主密码，它不存储在Lastpass的系统上，LastPass也不维护主密码。

加密数据则采用256位AES加密，只有用每个用户的主密码得出的唯一加密密钥才能解密。

图巴表示，“客户的敏感保险库数据，如用户名和密码、安全笔记、附件和表格填写字段，仍然是基于LastPass的零信任架构进行安全加密。"

公开信息显示，LastPass是一个在线密码管理器和页面过滤器，采用了强大的加密算法，自动登录/云同步/跨平台/支持多款浏览器。该公司声称其产品有超过10万家企业、3300万人员正在使用，是全球最大的在线密码管理软件。

**参考链接：**

https://www.bleepingcomputer.com/news/security/lastpass-hackers-stole-customer-vault-data-in-cloud-storage-breach/

原文来源：FreeBuf

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

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