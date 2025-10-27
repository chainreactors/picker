---
title: 勒索病毒战术进化：新型跨平台勒索病毒NotLockBit威胁Windows和macOS用户
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787665&idx=1&sn=7e13d49ca3618726a17745bf772405c6&chksm=8893bd7ebfe434688825c7fefb72ee438b63d5f571291cd60e9a6b95e06353c0a446c2eeba1d&scene=58&subscene=0#rd
source: 安全客
date: 2024-12-24
fetch_date: 2025-10-06T19:40:19.526102
---

# 勒索病毒战术进化：新型跨平台勒索病毒NotLockBit威胁Windows和macOS用户

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb4tf01L4CsWbgnukg2N2OVMKHb54ZAb0W2CnVlYaZXiajwnPpnWMNGLSpiaKJj9icJI1XD5NbvJ0h4bw/0?wx_fmt=jpeg)

# 勒索病毒战术进化：新型跨平台勒索病毒NotLockBit威胁Windows和macOS用户

安全客

News

随着勒索病毒技术的不断发展，攻击者的战术也在不断进化。最近，Qualys的高级威胁研究工程师Pranita Pradeep Kulkarni揭示了一种新型勒索病毒——NotLockBit，这一病毒不仅在功能上与LockBit勒索病毒极为相似，还具有一个显著的特点——**跨平台能力，能够同时攻击Windows和macOS操作系统。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb4tf01L4CsWbgnukg2N2OVMgBEvibFLHvl8fWvyibE4O8vYn8HymicZNhoVIcrlllic4iaf1HOrbgCKLQQ/640?wx_fmt=jpeg&from=appmsg)

与传统勒索病毒主要依赖Windows系统不同，NotLockBit采用了Go语言进行编写，充分利用了Go语言的跨平台兼容性和高效的开发特点，使得它可以在多个操作系统上有效运行。NotLockBit的开发者显然意识到，单一操作系统的攻击已经无法满足其扩展需求，因此有意将攻击面扩展到macOS，实现了真正意义上的跨平台攻击。研究者详细揭示了其攻击原理：

1

**初始感染：信息收集与系统侦察**

在感染初期，NotLockBit会通过收集受害者系统的关键信息来进行自我调整。特别是在macOS上，NotLockBit会通过**系统模块收集硬件规格、网络配置、操作系统版本**等数据，这些信息帮助勒索病毒了解目标系统的环境，从而决定下一步的攻击路径。

该过程类似于传统的“侦察”阶段，目的是获取足够的情报，以便对系统进行定制化的攻击。而这种基于具体系统环境的信息收集，是NotLockBit与其它勒索病毒的显著区别之一。

2

**双重加密：AES与RSA联合加密**

NotLockBit的加密过程比许多传统勒索病毒要复杂，它使用了双重加密策略。首先，勒索病毒会使用一个随机生成的AES密钥对目标文件进行加密，AES是一种对称加密算法，速度较快，适合大规模加密。为了进一步增强加密的安全性，NotLockBit还通过RSA加密算法对AES密钥进行保护，RSA是一种非对称加密算法，只有拥有对应私钥的人才能解密AES密钥。

被加密的文件会被重新命名，文件扩展名会被修改，使得文件在没有解密密钥的情况下无法被恢复。NotLockBit特别针对重要的文件类型进行攻击，如**文档、图片和虚拟机文件**等。同时，它还会故意跳过一些系统文件和目录，如/proc/和/sys/等，这些目录通常包含**系统核心文件和配置文件**，跳过这些目录能够帮助勒索病毒减少被检测的风险。

3

**数据外泄：双重勒索的战略**

与许多现代勒索病毒一样，NotLockBit不仅实施传统的加密勒索，还通过数据外泄加大威胁。它会将受害者的重要数据上传到攻击者控制的远程存储服务，通常使用Amazon S3等云存储服务。这种“双重勒索”策略意味着，**除非受害者支付赎金，否则不仅会失去加密的文件，敏感数据也可能被公开，导致更严重的声誉损害和财务损失。**

4

**自我删除与篡改：隐蔽性与逃避检测**

为了增强隐蔽性并减少被检测的风险，NotLockBit具有强大的自我删除功能。在完成加密和数据外泄后，病毒会删除系统的影像副本和恢复点，防止受害者通过系统恢复功能找回数据。此外，勒索病毒还会修改受害者的桌面壁纸，显示一条带有威胁信息的勒索公告，以增加心理压力。最令人担忧的是，NotLockBit在完成攻击后，会自我销毁，彻底删除自己在受害者系统中的痕迹，进一步避免安全软件的检测和防御措施的介入。

NotLockBit的一个重要特征就是它同时攻击Windows和macOS操作系统，针对macOS的攻击尤为引人注目，**因为这是首个完全能够影响这一系统的勒索病毒变种之一**。macOS系统曾经被认为相对安全，较少受到勒索病毒的攻击。然而，NotLockBit的出现打破了这一常规，它使用特定的osascript命令来修改macOS的系统设置，展示了攻击者对macOS内部结构的深刻了解。

在macOS环境中，NotLockBit表现出了极高的隐蔽性和针对性攻击能力，它不仅能够加密文件，还能绕过一些macOS特有的安全机制。这使得苹果用户也不再能高枕无忧，macOS系统的用户同样需要加强对勒索病毒的防护意识。

NotLockBit勒索病毒的出现，标志着勒索病毒战术的又一次进化。其跨平台攻击能力、双重勒索策略、自我删除机制等创新手段，使其成为当前最为复杂和危险的恶意软件之一。随着勒索病毒攻击的不断升级，无论是Windows还是macOS用户，都不能掉以轻心。面对这一新型勒索病毒，用户必须提高警惕，采取有效的安全措施，以应对越来越复杂的网络威胁。

文章参考：

https://securityonline.info/notlockbit-new-cross-platform-ransomware-threatens-windows-and-macos/

**推荐阅读**

|  |
| --- |
| **01**  ｜[Meta因数据泄露再遭重罚](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787658&idx=1&sn=e9828965cba2dd8d085022dc8969e9da&scene=21#wechat_redirect) |
| **02**  ｜[攻击者在GitHub上使用伪造PoC窃取凭证](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787651&idx=1&sn=3ec2660ca7270d7114baa4c06baf3c9e&scene=21#wechat_redirect) |
| **03**  ｜[微软Azure MFA漏洞曝光](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787627&idx=1&sn=4aca62c5aa480dccf358e90b043f3dcc&scene=21#wechat_redirect) |

**安全KER**

安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb4tf01L4CsWbgnukg2N2OVMmHXaLQr8b2dWsxQIXgGFfwb2Mol1TbjyYmuoiaibOiaPOzzIwk99bQhRA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb4tf01L4CsWbgnukg2N2OVMiaeD8ZDJSZMPt9s2iatpzOztx1pHU7k8XBoS2rZictcakZ32DFLxNF1sg/640?wx_fmt=png&from=appmsg)

**注册安全KER社区**

**链接最新“圈子”动态**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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