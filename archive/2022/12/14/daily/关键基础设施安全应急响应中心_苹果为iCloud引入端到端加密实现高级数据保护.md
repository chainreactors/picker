---
title: 苹果为iCloud引入端到端加密实现高级数据保护
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247533281&idx=2&sn=13788070f8af6d1b23d01025bba6fb5c&chksm=c1e9ceb0f69e47a6d665aa6c8f032ecf7007098128c48c6f702bcaea47e1f05733405fe21f04&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2022-12-14
fetch_date: 2025-10-04T01:24:30.032076
---

# 苹果为iCloud引入端到端加密实现高级数据保护

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGoguv3YI6o3bq7vnNT47hW8MwWokXqvoU8YlwpGntvrNaPvQNKxH5u6ib9ia8mkGicI7tDcMw4YYW4oPtA/0?wx_fmt=jpeg)

# 苹果为iCloud引入端到端加密实现高级数据保护

关键基础设施安全应急响应中心

苹果在iCloud中引入基于端到端加密的高级数据保护功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29b79LoesMBOBFoKat0A3xZyG4gdp7sHkHGwNCK5aiakB5W8ACPXyrMWOIRxnqo4LmZvrL2yz8MAcA/640?wx_fmt=png)

图 iCloud高级数据保护功能

12月7日，苹果为iCloud引入高级数据保护功能，该功能使用端到端加密来保护敏感iCloud数据，包括备份、图片、笔记等内容。苹果称，从iOS 16.2、iPadOS 16.2、macOS 13.1系统开始，用户可以选择高级数据保护功能来保护大部分的iCloud数据。

苹果系统为iCloud提供2种数据保护功能：标准数据保护和高级数据保护。

**标准数据保护：**标准数据保护是iCloud账户的默认安全设置。iCloud中数据是加密的，加密密钥保存在苹果数据中心，苹果可以帮助用户进行数据恢复，只有特定数据是端到端加密的。

**高级数据保护：**高级数据保护是iCloud的可选数据安全设置功能，可以通过最高等级的云数据安全保护。如果用户选择高级数据保护功能，只有拥有加密密钥的被信任的设备才能够访问iCloud数据，这一功能是通过端到端加密实现的。高级数据保护功能保护的数据包括iCloud 备份、相册、笔记等。

在端到端加密中，只有Apple ID登录的被信任的设备可以解密加密的数据。包括苹果公司在内的其他用户都无法访问端到端加密的数据，即使云端数据泄露，也无法访问。只有用户自己才可以恢复数据，可以用设备密码、恢复联系人、恢复密钥等进行恢复。

对于使用该安全特征的用户，高级数据保护可以确保大多数iCloud数据的安全，即使在数据泄露的情况下也可以确保加密的云数据智能在用户的信任设备上解密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29b79LoesMBOBFoKat0A3xZgaGa6sTVOrCnUyxc06age6LgGUvj0W71iaDXMbKSurh1n3Ps0GBTpUA/640?wx_fmt=png)

使用端到端加密保护的数据类型包括设备和消息备份、iCloud Drive、相册、提醒、Safari书签、语音留言等。iCloud邮箱、联系人、日历数据并不会被加密，因为需要与其他邮箱、联系人、日历系统进行通信。

目前，参与苹果beta software项目的美国用户已可以试用高级数据保护功能，其他用户预计本月底可以使用该功能。其他国家和地区的用户预计2023年初可以使用该功能。

此外，苹果还引入了2个新的安全特征：iMessage Contact Key Verification（联系人密钥验证）和Apple ID安全密钥。

联系人密钥验证可以使iMessage用户验证另外一段用户的身份，确保iMessage的另一端是用户想要会话的联系人。如果有攻击者将攻击设备加入会话来监听加密的通信信道系统会自动预警。

Apple ID安全密钥使得苹果客户在设置Apple ID账户的过程中需要一个物理安全密钥才能完成登录过程。该特征适用于名人、记者、政府工作人员等在线账户面临持续威胁的用户。

更多高级数据保护功能的细节参见：https://support.apple.com/en-us/HT202303<advanced

**参考及来源：**

https://www.bleepingcomputer.com/news/apple/apple-rolls-out-end-to-end-encryption-for-icloud-backups/

原文来源：嘶吼专业版

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogucKMiatGyfBHlfj74r3CyPxEBrV0oOOuHICibgHwtoIGayOIcmJCIsAn02z2yibtfQylib07asMqYAEw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

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