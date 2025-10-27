---
title: 【安全圈】不要赎金只破坏基础设施，Twelve 黑客大肆攻击俄罗斯实体
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064619&idx=2&sn=3a5effd204a035c14315a5d25de31778&chksm=f36e672bc419ee3d04e1ae6a7b585f70ac36de9073e859f4e6a4e5791ec883867895df596046&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-24
fetch_date: 2025-10-06T18:28:21.368827
---

# 【安全圈】不要赎金只破坏基础设施，Twelve 黑客大肆攻击俄罗斯实体

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhjvmwBHtTYHpyBYkicGjdiap1hyLm3GHENWia7QOw8Hn201xFv2WNXEjTWOpKiaRveiaWakOLBxga7ib1A/0?wx_fmt=jpeg)

# 【安全圈】不要赎金只破坏基础设施，Twelve 黑客大肆攻击俄罗斯实体

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

网络攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhjvmwBHtTYHpyBYkicGjdiapiaP4q7XlrrjmHVQcObceLSCb4ULUftO0ktyoC4tFicZAyMQv0sQ2vNGQ/640?wx_fmt=jpeg&from=appmsg)

据观察，一个名为 “Twelve ”的黑客组织使用大量公开工具对俄罗斯目标实施破坏性网络攻击。

卡巴斯基在周五的分析中表示：与要求赎金解密数据不同，该组织更倾向于加密受害者的数据，然后使用擦除器破坏他们的基础设施，以防止恢复。

这表明，他们希望对目标组织造成最大程度的损害，而不是直接获得经济利益。

据悉，该黑客组织是在2023年4月俄乌战争爆发后成立的，曾发起过多次网络攻击事件、窃取敏感信息，然后通过其Telegram频道分享这些信息。

卡巴斯基称，Twelve 与一个名为 DARKSTAR（又名 COMET 或 Shadow）的勒索软件组织在基础架构和战术上有重合之处，因此这两个黑客组织很可能相互关联，或者是同一活动集群的一部分。

俄罗斯网络安全厂商说：Twelve 的行动明显具有黑客活动的性质，而 DARKSTAR 则坚持典型的双重勒索模式。集团内部目标的这种变化凸显了现代网络威胁的复杂性和多样性。

攻击链首先通过滥用有效的本地或域账户获得初始访问权限，然后使用远程桌面协议（RDP）进行横向移动。其中一些攻击还通过受害者的承包商实施。

卡巴斯基指出：为此，他们获得了承包商基础设施的访问权限，然后使用其证书连接到客户的 VPN。在获得访问权限后，对手可以通过远程桌面协议（RDP）连接到客户的系统，然后侵入客户的基础设施。

Twelve 使用的其他工具包括 Cobalt Strike、Mimikatz、Chisel、BloodHound、PowerView、adPEAS、CrackMapExec、Advanced IP Scanner 和 PsExec，用于窃取凭证、发现、网络映射和权限升级。与系统的恶意 RDP 连接通过 ngrok 传输。

此外，还部署了具有执行任意命令、移动文件或发送电子邮件功能的 PHP web shell。这些程序（如 WSO web shell）在 GitHub 上随时可用。

在此前的一起事件中，卡巴斯基称威胁分子利用了VMware vCenter中的已知安全漏洞（如CVE-2021-21972和CVE-2021-22005），提供了一个web shell，然后利用这个web shell投放了一个名为FaceFish的后门。

攻击者使用 PowerShell 添加域用户和组，并修改 Active Directory 对象的 ACL（访问控制列表）。而为了避免被发现，攻击者将恶意软件和任务伪装成现有产品或服务的名称。攻击者通过使用包括 “Update Microsoft”、“Yandex”、“YandexUpdate ”和 “intel.exe”等名称伪装成英特尔、微软和 Yandex 的程序来逃避检测。

这些攻击的另一个特点是使用 PowerShell 脚本（“Sophos\_kill\_local.ps1”）来终止受攻击主机上与 Sophos 安全软件相关的进程。

最后阶段需要使用 Windows 任务调度程序来启动勒索软件和清除器有效载荷，但在此之前要通过名为 DropMeFiles 的文件共享服务以 ZIP 压缩文件的形式收集和渗出受害者的敏感信息。

卡巴斯基研究人员说：攻击者使用了一个流行的 LockBit 3.0 勒索软件版本，该版本由公开源代码编译而成，用于加密数据。在开始工作之前，勒索软件会终止可能干扰单个文件加密的进程。

与Shamoon恶意软件相同的擦除器会重写所连接驱动器上的主引导记录（MBR），并用随机生成的字节覆盖所有文件内容，从而有效防止系统恢复。

卡巴斯基研究人员指出：该组织坚持使用公开的、人们熟悉的恶意软件工具，这也表明它没有自制的工具，那么大家就还是有机会能及时发现并阻止 Twelve 的攻击。

> 参考来源：Hacktivist Group Twelve Targets Russian Entities with Destructive Cyber Attacks (thehackernews.com)

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhjvmwBHtTYHpyBYkicGjdiapgJiavpv5eqcRrRWGpN0xoQHXXBQpmoQqEJFScQuddpiaticbqlFlTO3TQ/640?wx_fmt=jpeg)[【安全圈】黑客声称对戴尔公司进行了数据泄露，曝光超过10,000名员工信息](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064597&idx=1&sn=b660f4bc1475f86930a2ea1dc89e683f&chksm=f36e6715c419ee0309ef48753b04421c6f6fe0e73e6820245171281b20d2f216648eac7e7c7d&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgiaaXeNGKfYJo9KNnBhco0Dr4y9Qha5HnpujmVqzrCskyLV4qQUMEFDdTeRZqbTo7n6Dhz80Xh84w/640?wx_fmt=png)[【安全圈】朝鲜 APT 在网络间谍攻击中绕过 DMARC 电子邮件策略](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064597&idx=2&sn=a3278f6d575dc09eb6874e7ec2d6bcdf&chksm=f36e6715c419ee0389ebda2affdd83addfd3cb93eaf29bb92ba15cb0fdb022e3ad9dbf4b2e59&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgiaaXeNGKfYJo9KNnBhco0DfViaolehrE0SLhFzVv5to0UbE4tlDmkibsOKGiaI44LubqLcdz7cK9ia4w/640?wx_fmt=jpeg)[【安全圈】警惕新网络钓鱼手法：虚假 CAPTCHA 页面诱骗用户安装 Lumma Stealer 恶意软件](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064597&idx=3&sn=10396f2711c45e64515ea2d5aeb8b048&chksm=f36e6715c419ee03936d3da0cdb3d3a6f96afe8fdaa6173dcaf004c1dce37846a39fa14a1220&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgiaaXeNGKfYJo9KNnBhco0DlQpAE9wbaGsQzLJNORNYLWKibH2xZ7XRicVFW209BYOiaSwjekSib0jHBQ/640?wx_fmt=png)[【安全圈】代号「神谕的黄鹂」Ubuntu 24.10测试版发布 将在10月10日推出正式版(非LTS)](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064597&idx=4&sn=f37b2475fd9a6fa85f486098df940ec6&chksm=f36e6715c419ee03e661e1699d1e0942843e1294495386adfb91f728bfc61a1dfebe49070ddd&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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