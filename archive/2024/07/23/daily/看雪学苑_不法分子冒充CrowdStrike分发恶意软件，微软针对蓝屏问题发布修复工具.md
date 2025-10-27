---
title: 不法分子冒充CrowdStrike分发恶意软件，微软针对蓝屏问题发布修复工具
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458564568&idx=2&sn=cac24406ee69765fb9ea36342035c674&chksm=b18d875286fa0e44aae2e1a5e435022ccb68e5ba854fe498f9653f0478486e44c4f434f461d6&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-07-23
fetch_date: 2025-10-06T17:43:25.844998
---

# 不法分子冒充CrowdStrike分发恶意软件，微软针对蓝屏问题发布修复工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EHmwEcxqraXpz8upssgxlk0WHZb6Ljo139ySKPEUnf1VtX1s4WGkK2AnhSWoTuenQEM6jk0SaApw/0?wx_fmt=jpeg)

# 不法分子冒充CrowdStrike分发恶意软件，微软针对蓝屏问题发布修复工具

看雪学苑

看雪学苑

上周五，网络安全公司 CrowdStrike 因推送有缺陷的软件更新而导致Windows 设备蓝屏死机，全球IT中断。现今世界各地都在热议这一事故。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EHmwEcxqraXpz8upssgxlkpOnh6P892mMa0hicYHOzCZtyrYKGQDIXakxTh3iaUCC9ib9Q2jfCVNtXA/640?wx_fmt=png&from=appmsg)

在周六的事后分析博客文章中，CrowdStrike解释说，故障原因是其终端安全响应系统 CrowdStrike Falcon的通道文件（传感器配置）例行更新触发了逻辑错误，从而导致设备崩溃，影响范围为7.11 及更高版本。

该公司另外特别指出，现今有黑客正以提供修补程序为幌子，向客户分发 Remcos RAT恶意软件。英国国家网络安全中心（NCSC）和美国网络安全与基础设施安全局 CISA也警告称，“威胁行为者继续利用广泛的 IT 中断进行网络钓鱼和其他恶意活动。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EHmwEcxqraXpz8upssgxlkKicAw4vqapIPVmE6ec1rjwWicSk9ULJwlp9tnXic8afDvy1DmcCSEcR4Q/640?wx_fmt=png&from=appmsg)

据了解，网络犯罪分子迅速通过社会工程攻击利用了这一情况。他们设置了诈骗域名和网络钓鱼页面，伪装成此次蓝屏死机问题的解决方案。例如，黑客组织 Handala 通过从“crowdstrike.com.vc”域发送电子邮件来冒充 CrowdStrike，向客户声称其创建了一个工具用以恢复Windows系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EHmwEcxqraXpz8upssgxlkcCfNQkfs2rnzYw6REd79bJS1Ap0FbIsibEqpkGITIwuShqmd6CFic2TA/640?wx_fmt=png&from=appmsg)

实际上，要解决此问题，管理员需要将受影响的 Windows 设备重新启动到安全模式或恢复环境，并在C:\Windows\System32\drivers\CrowdStrike目录下手动删除有问题的内核驱动程序。然而，由于组织可能面临数百甚至上千台受影响的 Windows 设备，手动执行这些修复可能会存在耗时等问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EHmwEcxqraXpz8upssgxlkSrWH1JrUCZmib9k3mq5t4QIqIbH9YnRHo6pflfIk8Ygy5J6Egswl91A/640?wx_fmt=png&from=appmsg)

针对这一情况，Microsoft专门发布了一款恢复工具，能够自动从Windows设备中删除有问题的CrowdStrike更新，以使其正常启动。微软支持公告中写道：“作为影响 Windows 客户端和服务器的 CrowdStrike Falcon 代理问题的后续措施，我们发布了一个 USB 工具来帮助 IT 管理员加快修复过程。用户可在 Microsoft 下载中心找到已签名的 Microsoft 恢复工具：https://go.microsoft.com/fwlink/?linkid=2280386。”

编辑：左右里

资讯来源：Microsoft

转载请注明出处和本文链接

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