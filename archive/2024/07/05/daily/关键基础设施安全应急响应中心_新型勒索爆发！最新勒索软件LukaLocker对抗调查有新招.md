---
title: 新型勒索爆发！最新勒索软件LukaLocker对抗调查有新招
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247544738&idx=3&sn=dfb7edba4626028f09523e73220bc6ed&chksm=c1e9a3f3f69e2ae5f0e17920d70022e024c153a45cb6214767cbd6c203aca95a14b00fbf3fac&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-07-05
fetch_date: 2025-10-06T17:43:43.292575
---

# 新型勒索爆发！最新勒索软件LukaLocker对抗调查有新招

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogsyFdhrDz0Sx06YKiaBWXP5VzMl4Ndo1RGbeNdS5JFgtsxolNhLk1USAlzS4OGCicPFoRUdOUCmpPXA/0?wx_fmt=jpeg)

# 新型勒索爆发！最新勒索软件LukaLocker对抗调查有新招

关键基础设施安全应急响应中心

Halcyon公司7月1日发布分析报告，称其遭遇了名为Volcano Demon的新型勒索软件组织的攻击。该组织使用的加密器样本LukaLocker专门加密带有.nba扩展名的文件，并在受害者网络中部署了Linux版本的LukaLocker。Volcano Demon通过利用网络中的常见管理凭据锁定Windows工作站和服务器，并在实施攻击前将数据泄露到C2服务上，采用双重勒索策略。攻击者在入侵后清除了日志，且由于受害者的日志记录和监控解决方案有限，导致无法进行彻底的取证分析。在两起案件中，攻击者没有公开泄露数据，而是通过电话以威胁性语气联系公司领导层和IT高管进行勒索和谈判，电话来源不明。新发现的创新的LukaLocker恶意软件和一系列逃避策略来掩盖其行踪，使安全专家难以调查。

![](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icUpFA6RGD1gaEzuxmBLLEriaDFduaQgxPaluXBQer1ZSWia44wR9QhjpHWZYk9odycP9nl0OZJicLaYg/640?wx_fmt=jpeg&from=appmsg&wxfrom=13&tp=wxpic)

新型勒索基本情况

根据发现该攻击者的Halcyon研究人员的说法，这个新发现的对手被称为“火山恶魔”（Volcano Demon），其特点是使用前所未见的锁定恶意软件，名为 LukaLocker，该软件将受害者的文件加密为 .nba文件扩展名。

攻击者的逃避策略包括在攻击前安装有限的受害者日志记录和监控解决方案，以及使用“无来电显示”号码进行“威胁性”电话来勒索或谈判赎金。

Halcyon研究团队在文章中写道：“在攻击前清除了日志，在两起案件中，由于成功掩盖了行踪，无法进行全面的取证评估。”火山恶魔还没有发布其在攻击中窃取数据的泄漏网站，尽管它确实使用双重勒索作为策略，团队说。

在攻击中，火山恶魔使用从受害者网络中收集的常见管理凭证加载了Linux版本的LukaLocker，然后成功锁定了Windows工作站和服务器。攻击者还在勒索软件部署前将数据从网络中提取到其自己的指挥和控制服务器（C2），以便使用双重勒索。

![](https://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icUpFA6RGD1gaEzuxmBLLEriaP5qAAiaB57tb2Y8K7DqYyWWeV26iachib8vjQOib16pbx6Dj2LRiaKl2eyA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

赎金通知指示受害者通过qTox消息软件联系攻击者，然后等待技术支持回电，这使得跟踪双方之间的通信变得困难。

### Conti的残余？

根据文章，Halcyon研究人员于6月15日首次发现了现在称之为LukaLocker的样本。团队写道：“勒索软件是一个用C++编写和编译的x64 PE二进制文件。”LukaLocker勒索软件使用AP 混淆和动态API解析来隐藏其恶意功能——以逃避检测、分析和逆向工程。”

执行后，除非指定“--sd-killer-off”，否则LukaLocker会立即终止网络中存在的一些安全和监控服务，类似于现已不复存在的Conti勒索软件中的服务，可能是从 Conti勒索软件中复制的。这些服务包括各种杀毒和端点保护；备份和恢复工具；由 Microsoft、IBM和Oracle提供的数据库软件等；Microsoft Exchange服务器；虚拟化软件；以及远程访问和监控工具。它还会终止其他进程，包括Web浏览器、Microsoft Office和云及远程访问软件，如TeamViewer。

### 勒索软件停止的服务和进程主要包括如下类别：

停止的服务

#### 杀毒和端点保护服务

* Sophos
* Symantec
* McAfee
* Avast
* Defender
* Malwarebytes
* Windows Defender
* BitDefender
* Spyhunter
* Kaspersky
* SentinelOne

#### 备份和恢复服务

* Acronis
* Symantec
* Veeam
* SQL Safe

#### 数据库服务

* Microsoft SQL Server
* MySQL
* IBM DB2
* Oracle

#### 电子邮件服务器

* Microsoft Exchange

#### 虚拟化和云服务

* VMWare
* BlueStripe
* ProLiant

#### 远程访问和监控服务

* Alerter
* Eventlog
* UI0Detect
* WinVNC4

### 勒索软件停止的进程

#### 杀毒和安全软件进程

* Symantec/Norton
* McAfee
* AVG
* Kaspersky
* Bitdefender
* Trend Micro
* Malware Bytes

#### 系统监控和管理进程

* VMware
* Proficy
* Microsoft
* IBM
* BMC

#### 数据库和存储服务进程

* Microsoft SQL Server
* Oracle
* MySQL

#### 云和远程访问工具进程

* TeamViewer
* VNC
* Google

#### 网络浏览器进程

* Firefox
* Chrome

#### 办公和生产力软件进程

* Microsoft Office

该锁定器使用Chacha8密码进行批量数据加密，通过Elliptic-curve Diffie-Hellman (ECDH)密钥协商算法在Curve25519上随机生成Chacha8密钥和 nonce。文件可以完全加密或按不同的百分比加密，包括50%、20%或10%。

### 高度警惕

由于火山恶魔的广泛逃避能力，Halcyon团队难以对攻击进行全面的取证分析；此外，研究人员没有透露威胁行为者针对的组织类型。然而，Halcyon设法识别了一些攻击者的多种妥协指标（IoC），其中一些已上传到Virus Total。

![](https://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icUpFA6RGD1gaEzuxmBLLEriaTR9ISNoVcHciaZl7IyvicWib2KKjUNE4BCwfOU1xyJkuaYhr0s20cBhGw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

这些IoC 包括一个木马，Protector.exe和加密器Locker.exe。一个名为Linux locker/bin 的Linux加密文件和在加密前执行的命令行脚本Reboot.bat也是该新型勒索软件行为者攻击的标志。

尽管各种执法行动已经取缔了主要的网络犯罪团伙，但勒索软件仍然是全球组织面临的普遍和破坏性威胁，防守人员需要保持警惕。鉴于火山恶魔使用组织网络的管理密码作为最初的攻击手段，防御策略如多因素认证 (MFA) 和员工培训以识别将凭证交给攻击者的网络钓鱼活动可以帮助避免被攻击。

附录 Halcyon公司介绍

Halcyon.ai是一家领先的反勒索软件公司，致力于为全球2000强公司提供先进的勒索软件防护解决方案。Halcyon平台通过内置的绕过和逃避保护、密钥材料捕获、自动解密以及数据泄露和勒索预防等功能，以最小的业务中断帮助企业击败勒索软件攻击。主要服务和能力包括：绕过和逃避保护：预防勒索软件的绕过和逃避技术，确保企业安全。密钥材料捕获：捕获勒索软件使用的密钥材料，提供解密能力。自动解密：在遭受勒索软件攻击时，自动解密被加密的数据，减少业务中断。数据泄露和勒索预防：防止数据泄露和勒索事件的发生。Halcyon还发布了《权力排名：勒索软件恶意四分位数》，这是一个季度RaaS（勒索软件即服务）和勒索组织参考指南，为企业提供最新的勒索软件攻击信息和趋势分析。

**参考资源：**

1.https://www.halcyon.ai/blog/halcyon-identifies-new-ransomware-operator-volcano-demon-serving-up-lukalocker

2.https://www.darkreading.com/cyberattacks-data-breaches/ransomware-eruption-novel-locker-malware-flows-from-volcano-demon

原文来源：网空闲话plus

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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