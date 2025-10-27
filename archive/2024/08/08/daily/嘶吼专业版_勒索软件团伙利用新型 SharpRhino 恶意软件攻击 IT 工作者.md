---
title: 勒索软件团伙利用新型 SharpRhino 恶意软件攻击 IT 工作者
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247577424&idx=2&sn=7ab302209d6e90118cd3aef911163c91&chksm=e9147f6ade63f67c70c9c5ca86aad22449d80d9b21bc3b7f84158cd9a9ea328ba727f7d54225&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-08-08
fetch_date: 2025-10-06T18:06:21.739732
---

# 勒索软件团伙利用新型 SharpRhino 恶意软件攻击 IT 工作者

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29icy9iar5qAHcRzn6RKC08xczRjLY1T1GpxFiakUqxvrfzlZx5j5nUDKvzn5lmia00oAqe15xJoaC1mQ/0?wx_fmt=jpeg)

# 勒索软件团伙利用新型 SharpRhino 恶意软件攻击 IT 工作者

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

Hunters International 勒索软件组织正利用一种名为 SharpRhino 的新型远程访问木马 (RAT) 攻击 IT 工作者，侵入公司网络。

该恶意软件可帮助 Hunters International 实现初始感染，提升他们在受感染系统上的权限，执行 PowerShell 命令，并最终部署勒索软件负载。

Quorum Cyber 的研究人员观察到勒索软件攻击中使用的恶意软件是由一个冒充 Angry IP Scanner 网站的域名抢注网站传播的，Angry IP Scanner 是 IT 专业人员使用的合法网络工具。

2024 年 1 月，网络安全公司 eSentire 和研究员 0xBurgers 就曾发现该恶意软件通过一个假冒的 Advanced IP Scanner 网站传播。

Hunters International 是一个在 2023 年底开始活跃的勒索软件组织，由于其代码相似性而被标记为可能是 Hive 的品牌重塑。著名的受害者包括美国海军承包商 Austal USA、日本光学巨头 Hoya、Integris Health 和弗雷德哈金森癌症中心。

到目前为止，2024 年该威胁组织已宣布对全球各个组织（CIS 除外）发动了 134 起勒索软件攻击，在该领域最活跃的组织中排名第十。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29icy9iar5qAHcRzn6RKC08xcGaMlumwziaXjhYCKmQS9iaJqeibRPKQoriaxboiaDlA3S6EpKCicZpcOfvYQ/640?wx_fmt=png&from=appmsg)SharpRhino RAT

SharpRhino 利用数字签名的 32 位安装程序进行传播，其中包含自解压的受密码保护的 7z 存档以及用于执行感染的附加文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29icy9iar5qAHcRzn6RKC08xc1K89DMMENUQWe2joMKHGXfVWkVN95IW9aXGT8kEoFzttZ2kibm7vjag/640?wx_fmt=png&from=appmsg)

存档内容

安装程序会修改 Windows 注册表以实现持久性，并创建 Microsoft.AnyKey.exe 的快捷方式，该快捷方式通常是 Microsoft Visual Studio 二进制文件，在本例中被滥用。

此外，安装程序还会释放“LogUpdate.bat”，它会在设备上执行 PowerShell 脚本，将 C# 编译到内存中，以隐秘地执行恶意软件。

为了实现冗余，安装程序会创建两个目录“C:\ProgramData\Microsoft: WindowsUpdater24”和“LogUpdateWindows”，这两个目录都用于命令和控制 (C2) 交换。恶意软件中硬编码了两个命令，分别是“delay”（延迟）和“exit”（退出），前者用于设置下一个 POST 请求的计时器，后者用于终止通信。

分析表明，该恶意软件可以在主机上执行 PowerShell，可用于执行各种危险操作。Quorum 通过 SharpRhino 成功启动 Windows 计算器，测试了这一机制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29icy9iar5qAHcRzn6RKC08xcjpH0qvy68awIBuH9Ls6OTNCx7JxPJeaQLYIXfC2jfg2icbTVQeFiaa1g/640?wx_fmt=png&from=appmsg)

负责 PowerShell 执行的 QFunction

他们采用的新策略是部署网站来冒充合法的开源网络扫描工具，他们将目标瞄准 IT 工作者，希望能够窃取具有提升权限的账户。

因此，用户应谨慎对待搜索结果中的赞助结果，以避开恶意广告，激活广告拦截器以完全隐藏这些显示，并收藏已知可获取安全安装程序的官方项目网站。

为了减轻勒索软件攻击的影响，请制定备份计划，执行网络分段，并确保所有软件都是最新的，以减少特权提升和横向移动的机会。

参考及来源：https://www.bleepingcomputer.com/news/security/hunters-international-ransomware-gang-targets-it-workers-with-new-sharprhino-malware/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29icy9iar5qAHcRzn6RKC08xca0eIo7Rdx3YwXth0MfU7edMg9CP24n5qmPBtZeZibWaQlGeSicxhtChg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icEjy5ZrpCcgr4BicXicPv08DSsrgibDcJQpvwkZoO4OqdIpJNhj6TO5xV0ic0AnVf7f2kcPnNevQlTtQ/640?wx_fmt=png)

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