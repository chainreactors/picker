---
title: 因服务器配置错误，跨国集团汤森路透泄露了3TB敏感数据
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458480122&idx=2&sn=7a43e20ea2ba0796030b2c3e20320dbd&chksm=b18e5d7086f9d4664cf2062e9cb6ff32f79ff7397b1fb2d13978fdf641d2ed9b3a25a561e6a7&scene=58&subscene=0#rd
source: 看雪学院
date: 2022-11-01
fetch_date: 2025-10-03T21:26:22.921392
---

# 因服务器配置错误，跨国集团汤森路透泄露了3TB敏感数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPREJkFFAC2KsCic6kAVarNd5ia5OutSrJRVrNE0uncY6IQJllkzTPBNDtw/0?wx_fmt=jpeg)

# 因服务器配置错误，跨国集团汤森路透泄露了3TB敏感数据

看雪学苑

看雪学苑

10月27日，据外媒报道，跨国集团汤森路透（Thomson Reuters）在网络上意外开放了数个数据库，其中一个存储着敏感的客户及公司数据，包括以明文格式存储的第三方服务器密码，这些数据可能会被攻击者用以进行供应链攻击。

> Thomson Reuters，由加拿大汤姆森公司The Thomson Corporation与英国路透集团Reuters Group PLC合并组成的商务和专业智能信息提供商，产品有B2B媒体工具Reuters Connect、法律研究服务及数据库Westlaw、税务自动化系统ONESOURCE等。

Cybernews的研究团队通过对可访问 Web 服务器的 SSL（安全套接层）证书、DNS（域名系统）数据以及 ElasticSearch 数据库本身的信息进行彻底检查，确认了该开放数据库属于汤森路透公司。并且自10月21日以来，该服务器就一直处于可供访问状态。一个开放的服务器只需要不到几小时的时间就会被机器人爬取，而该数据库持续开放了超过三天。

研究团队指出，汤森路透开放着三个可供任何人查看的数据库，其中一个是面向公众的3TB ElasticSearch数据库（受需要处理大量且持续更新的数据的企业所青睐）。汤森路透服务器中ElasticSearch索引的命名表明，其被用作日志记录服务器，以收集用户-客户端交互的大量数据。Cybernews研究人员认为这些数据在地下犯罪论坛上可价值数百万美元。

据研究人员称，开放数据库的日志包含着敏感信息，若被不法分子访问，则有可能会导致供应链攻击。例如，本事件中的开放数据库包含对第三方服务器的访问凭据，并且以纯文本格式保存，可被任何爬取了该开放数据库的人看到。Cybernews的安全研究主管Mantas Sasnauskas对此表示，这种类型的信息将使攻击者能够在与汤森路透合作的公司使用的系统中获得初步立足点。

“……这为恶意行为者提供了一个很大的攻击面，不仅可以利用内部系统，还可以利用供应链攻击。一个简单的人为错误可能导致毁灭性的攻击，从数据泄露到勒索软件。” Mantas Sasnauskas补充道。

该团队还发现开放的数据库中包含用户登录名和密码重置日志。该日志会显示帐户持有人的电子邮件地址，并且可以看到发送密码更改的确切时间。其他敏感信息还包括SQL日志，这些日志能够显示汤森路透客户正在搜寻的信息。此外，数据库还包含有关特定企业或个人的公司和法律信息的文件等。

Cybernews在发现此事后联系了汤森路透，该公司立即关闭了开放的数据库。该公司对此展开了调查，目前的主流说法是“产品环境中的孤立错误导致非生产环境的意外配置错误”。汤森路透表示已开始通知受影响的客户。

编辑：左右里

资讯来源：Cybernews

转载请注明出处和本文链接

**每日涨知识**

自评估（self-assessment）

由组织自身发起，依据国家有关法规与标准，对信息系统及其管理进行的风险评估活动。

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/1UG7KPNHN8FxuBNT7e2ZEfQZgBuH2GkFjvK4tzErD5Q56kwaEL0N099icLfx1ZvVvqzcRG3oMtIXqUz5T9HYKicA/640?wx_fmt=gif)

戳“阅读原文”一起来充电吧！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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