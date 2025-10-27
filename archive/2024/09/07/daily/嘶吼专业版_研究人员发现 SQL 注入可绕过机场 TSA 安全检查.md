---
title: 研究人员发现 SQL 注入可绕过机场 TSA 安全检查
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247577850&idx=2&sn=fc511f23499cc2514d93f8b6f42dbdd2&chksm=e91460c0de63e9d6577c772f21f3bf1060666b115fe75af29da29c8f2a8d4ccaeb2742e4e6a1&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-09-07
fetch_date: 2025-10-06T18:28:55.518722
---

# 研究人员发现 SQL 注入可绕过机场 TSA 安全检查

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ib5aZ2jnToWLicWJaLsa8IOlhKXtBGt9dzGnsLN78dj6QMHAbVBxXvxsOia5GUatSTibOUSeW8CGTibLw/0?wx_fmt=jpeg)

# 研究人员发现 SQL 注入可绕过机场 TSA 安全检查

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

安全研究人员发现了 FlyCASS 中的漏洞，FlyCASS 是一项第三方网络服务，一些航空公司使用它来管理已知机组人员 (KCM) 计划和驾驶舱进入安全系统 (CASS)。

KCM 是一项运输安全管理局 (TSA) 计划，允许飞行员和乘务员跳过安全检查，而 CASS 允许授权飞行员在旅行时使用驾驶舱中的折叠座椅。

KCM 系统通过在线平台验证航空公司员工的证件。该过程包括扫描 KCM 条形码或输入员工编号，然后与航空公司的数据库进行交叉核对以授予访问权限，而无需进行安全检查。同样，CASS 系统在飞行员需要通勤或旅行时验证他们是否有权进入驾驶舱折叠座椅。

研究人员发现 FlyCASS 的登录系统容易受到 SQL 注入攻击，这种漏洞可让攻击者插入 SQL 语句进行恶意数据库查询。通过利用此漏洞，他们可以以参与的航空公司 Air Transport International 的管理员身份登录，并在系统内操纵员工数据。

他们添加了一个虚构的员工“Test TestOnly”，并授予该帐户访问 KCM 和 CASS 的权限，这实际上使他们能够“跳过安全检查，然后进入商用客机的驾驶舱”。

据了解，目前任何具备 SQL 注入基本知识的人都可以登录该网站，并将任何人添加到 KCM 和 CASS，这样他们既可以跳过安全检查，又可以进入商用客机的驾驶舱。

意识到问题的严重性后，研究人员立即开始了披露流程，并于 2024 年 4 月联系了相关机构。他们承认了漏洞的严重性，并确认 FlyCASS 已于 2024 年 5 月 7 日与 KCM/CASS 系统断开连接，作为预防措施。

不久之后，FyCASS 上的漏洞得到了修复。然而，在进一步协调安全披露漏洞时却遭到了抵制。

TSA 新闻办公室还向研究人员发送了一份声明，否认该漏洞的影响，声称该系统的审查过程将防止未经授权的访问。在得到研究人员的通知后，TSA 还悄悄地从其网站上删除了与其声明相矛盾的信息。

该漏洞可能会导致更广泛的安全漏洞，例如更改现有的 KCM 成员资料以绕过对新成员的任何审查程序。

研究人员的报告发布后，另一位研究人员发现，FlyCASS 似乎在 2024 年 2 月遭受了 MedusaLocker 勒索软件攻击，Joe Sandbox 分析显示了加密文件和勒索信。

今年 4 月，TSA 获悉一份报告称，第三方数据库中存在一个漏洞，其中包含航空公司机组人员信息，通过对该漏洞的测试，一个未经验证的姓名被添加到了数据库的机组人员名单中。目前，政府数据或系统没有受到损害，这些活动也没有对交通安全造成影响。

截止到发稿前，TSA 已制定程序来验证机组人员的身份，只有经过验证的机组人员才被允许进入机场的安全区域。

参考及来源：https://www.bleepingcomputer.com/news/security/researchers-find-sql-injection-to-bypass-airport-tsa-security-checks/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib5aZ2jnToWLicWJaLsa8IOlVlMEwnwNdE8gUOhAkLf0Zzg0l0yjx0kfXV3aGuf4WT7QDvy8o0U9dQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib5aZ2jnToWLicWJaLsa8IOlCzGMj54icEicicWkU0snOz4DfPB7OudgGeH8QmhGUzPbZ5STqQiazrezyw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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