---
title: FBI：Hive勒索软件团伙在过去一年勒索得利1亿美元
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458484391&idx=2&sn=91affd1dcf1702183265685244bbbf31&chksm=b18e4e2d86f9c73b8f142e4adb42fcb32d8f8ea01c0ee965d9ee6479046ec2acb1901417159d&scene=58&subscene=0#rd
source: 看雪学院
date: 2022-11-22
fetch_date: 2025-10-03T23:23:57.939385
---

# FBI：Hive勒索软件团伙在过去一年勒索得利1亿美元

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8ELvOAp0Wq5nvsc461v9L6DleDPZVuRRgaZuxS76yXjlswNmsibcmkqBvCsAagrXibvxMZ3icQLeicsPg/0?wx_fmt=jpeg)

# FBI：Hive勒索软件团伙在过去一年勒索得利1亿美元

看雪学苑

看雪学苑

11月17日，美国联邦调查局FBI、网络安全和基础设施安全局CISA以及卫生与公众服务部HHS联合发布了一则关于Hive勒索软件的联合网络安全公告。该公告上写道，根据FBI的信息，截至2022年11月，Hive勒索软件团伙已使全球1300多家公司受害，收取了约1亿美元的赎金。

Hive属于常规的勒索软件，遵循勒索软件即服务RaaS商业模式，由开发人员开发、维护及更新恶意软件，而具体实施勒索软件攻击则交由另一方附属公司负责。从2021年6月到2022年11月，Hive勒索软件的主要攻击目标为广泛的企业和关键基础设施部门，如政府设施、通信、关键制造、信息技术，尤其是医疗保健和公共卫生。根据区块链分析公司Chainalysis发布的一份报告，Hive勒索软件是2021年收入排名前10的勒索软件之一。

Hive攻击者通过远程桌面协议（RDP）、虚拟专用网络（VPN）和其他远程网络连接协议使用单因素登录获得对受害者网络的初始访问权限。在一类实例中，攻击者绕过了多重身份验证（MFA），并通过利用CVE-2020-12812漏洞（该漏洞使攻击者能够在更改用户名大小写时登录，无需输入用户的第二个身份验证因素）获得了对FortiOS服务器的访问权限。

除此之外，Hive勒索软件团伙还通过分发带有恶意附件的网络钓鱼电子邮件并利用以下针对Microsoft Exchange Server的漏洞，获得对受害者网络的初始访问权限：

CVE-2021-31207 – Microsoft Exchange安全功能绕过漏洞；

CVE-2021-34473 – Microsoft Exchange远程执行代码漏洞；

CVE-2021-34523 – Microsoft Exchange Server权限提升漏洞。

在获得访问权限后，Hive勒索软件会锁定并终止与备份、防病毒/反间谍软件以及文件复制相关的进程，为后续文件加密清理障碍；接着会停止卷影复制服务，并通过命令行的vssadmin或PowerShell删除全部现有卷影副本；最后，Hive会删除Windows事件日志，特别是系统、安全和应用程序日志。

据称，Hive勒索软件团伙可能是使用Rclone和云存储服务Mega来泄露数据的。除针对Microsoft Windows操作系统外，Hive勒索软件也有被发现存在Linux、VMware ESXi和FreeBSD的已知变体。

针对Hive勒索软件，FBI、CISA和HHS为各机构列举了一系列缓解措施，以期能够减少勒索软件事件发生的可能性及造成的影响。具体请看：*https://www.cisa.gov/uscert/ncas/alerts/aa22-321a*

编辑：左右里

资讯来源：CISA

转载请注明出处和本文链接

**每日涨知识**

密码杂凑算法（hash algorithm）

又称杂凑算法、密码散列算法或哈希算法。该算法将一个任意长的比特串映射到一个固定长的比特串，且满足下列三个特性：

（1）为一个给定的输出找出能映射到该输出的一个输入是计算上困难的；

（2）为一个给定的输入找出能映射到同一个输出的另一个输入是计算上困难的。

（3）要发现不同的输入映射到同一输出是计算上困难的。

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