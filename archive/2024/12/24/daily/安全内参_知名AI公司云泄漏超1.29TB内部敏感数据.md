---
title: 知名AI公司云泄漏超1.29TB内部敏感数据
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513336&idx=1&sn=39a58da25f5f0469bad2256e61f8b6f2&chksm=ebfaf3d8dc8d7ace77a3b5193f40b4fd2b21b97af244fc5987289ae89de9b629930765ea01ca&scene=58&subscene=0#rd
source: 安全内参
date: 2024-12-24
fetch_date: 2025-10-06T19:40:28.981515
---

# 知名AI公司云泄漏超1.29TB内部敏感数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7uhEj4ewxkU3qWjG2pO1vc8GzI9bWEnDia5tEGCiaplgoCS5DnQeCS89UOwicr05TFzicibBseJzTfkU4g/0?wx_fmt=jpeg)

# 知名AI公司云泄漏超1.29TB内部敏感数据

安全内参编译

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tOiaW1QLOL6usmkMDCU0wCorXE2Of8aL4MtmOXyIJN3QTQfibQL7gcTL5GS4FMQr1A7MqyaUTXmRkA/640?wx_fmt=jpeg)

**据悉，暴露的数据库包含个人敏感数据和公司运营数据，事件归因为云存储配置不当。**

前情回顾·**全球数据泄漏态势**

* [背调公司发生超大规模数据泄漏，一亿美国人隐私信息暴露](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512681&idx=2&sn=dd2b1e9df9f50d9784a77a51d1958eca&scene=21#wechat_redirect)
* [国内某上市公司疑遭勒索攻击泄漏2.3TB数据](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512435&idx=2&sn=b2e7d6f0b8dd43d15ae1184a66ab5a1b&scene=21#wechat_redirect)
* [被指泄露半个美国的隐私，AT&T数据泄漏事件持续发酵](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512208&idx=2&sn=ad8fca1fa944c31ee539d2f2085c20e1&scene=21#wechat_redirect)
* [7.5亿印度公民身份信息在线泄漏：疑似源自运营商](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247510960&idx=2&sn=f956d1b04df5910fb02c9d3307e1886a&scene=21#wechat_redirect)

安全内参12月23日消息，英国知名人工智能初创公司因配置错误的云存储系统，导致1.29TB数据和超过300万条记录被曝光。

据安全研究员Jeremiah Fowler发现并由Website Planet披露，这个未受保护的数据库据称属于Builder.ai。这是一家提供AI驱动软件开发平台的公司。该公司已获得4.5亿美元（约合人民币32.84亿元）的风险投资，其中包括2023年5月的D轮2.5亿美元融资。

**泄露数据涉及个人信息和内部项目细节**

暴露的数据库包含敏感数据和运营数据，这可能对Builder.ai的客户以及内部运营构成风险。

在300多万条记录中，包含可识别个人身份的信息，例如姓名、电子邮件地址、电话号码及实际地址。数据库还记录了项目细节，包括正在进行和已完成的软件开发计划、客户互动记录及时间表。这些信息可能导致知识产权泄露，进而被恶意行为者或竞争对手利用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FzZb53e8g7uhEj4ewxkU3qWjG2pO1vc8sw8akj5Cuk2N7bFk7z7RRzD4gqw7fZ8zjQYNIJpeg9kq8D2Pj0VnRw/640?wx_fmt=png&from=appmsg)

除了客户数据，数据库还暴露了Builder.ai员工之间的内部通信。据Fowler介绍，这些电子邮件和消息涉及客户项目、运营挑战以及机密商业策略。此外，数据库还包含财务记录，例如发票和支付详情，这进一步增加了欺诈活动和财务被滥用的风险。

**事件归因为云存储配置不当**

此次数据泄露被归因于云存储系统配置错误。该系统缺乏足够的安全设置，从而允许未经授权的访问。虽然Builder.ai并非首个因类似问题暴露数据的公司，但作为一家已获得4.5亿美元风险投资的企业，Builder.ai理应具备避免此类风险的数据保护流程和机制。

如果说上述问题还能归结于Builder.ai尚不知情的话，接下来的情况更令人担忧。Fowler详细说明，自10月28日以来，他多次发送通知，提醒数据库暴露的问题。然而，在接近一个月的时间内，该数据库依然处于暴露状态，任何人均可访问。据悉，Builder.ai显然知晓这一问题。一名员工在电子邮件中回复Fowler称：“不幸的是，由于依赖系统的某些复杂性，解决问题的速度比我们预期的要慢。”

尽管Fowler未披露数据库托管的云服务提供商，但他指出，如果托管在亚马逊AWS上，仅修改AWS服务（如S3）的读取权限可能不到10秒钟即可完成。

Fowler还提到，目前尚不清楚该数据库是由Builder.ai直接管理，还是通过第三方管理。但是，像Builder.ai这样获得巨额风投资金的公司，无论是直接还是通过第三方都未能解决如此基础的安全问题，这确实值得质疑。

此外，数据库暴露的时间长度以及Builder.ai（总部位于英国）在被告知后的迟缓反应，也引发了对其在多项隐私法下的法律责任的担忧。这包括《英国2018年数据保护法》、《欧盟通用数据保护条例》以及作为补充的《英国通用数据保护条例》。

**参考资料：siliconangle.com**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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