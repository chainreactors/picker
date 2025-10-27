---
title: 伊朗网络组织Emennet Pasargad利用WezRat恶意软件发起攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492416&idx=1&sn=56e31c02aa497b57fc1b7536ce1e0250&chksm=e90dc96ade7a407c725c16a2cf2008580394a743fcbaa68e9c1307c92eb766cc77ad0ff11b54&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-11-18
fetch_date: 2025-10-06T19:16:43.150107
---

# 伊朗网络组织Emennet Pasargad利用WezRat恶意软件发起攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 伊朗网络组织Emennet Pasargad利用WezRat恶意软件发起攻击

BaizeSec

白泽安全实验室

**一、事件概述：**

在2024年10月21日，一系列伪装成以色列国家网络局（INCD）的电子邮件被发送至多个以色列组织。这些邮件来自一个欺诈性地址，警告收件人紧急更新他们的Chrome浏览器。美国联邦调查局（FBI）、美国财政部和以色列国家网络安全局（INCD）联合发布的网络安全咨询报告将此次活动中使用的恶意软件，由Check Point Research命名为WezRat，归咎于伊朗网络组织Emennet Pasargad。该组织对美国、法国、瑞典和以色列的多个目标进行了网络操作。

**二、组织事件及背景**

Emennet Pasargad是一个与伊朗伊斯兰革命卫队（IRGC）有关联的网络组织，多年来一直受到网络防御组织的监视。该组织的历史活动包括：

* 2021年10月20日，纽约大陪审团起诉两名与Emennet Pasargad有关的伊朗国民，指控他们涉嫌参与破坏2020年美国总统选举的计划。
* 2023年中期，Anzu Team（Emennet Pasargad的一个分支）攻击了瑞典的SMS服务，发送了呼吁对焚烧古兰经事件进行报复的信息。
* 2023年12月，该组织以“For-Humanity”的名义获得了对美国IPTV流媒体服务的未授权访问，传播与以色列-哈马斯冲突相关的定制信息。
* 2024年中期，该组织在夏季奥运会期间通过攻击法国显示提供商，投射反以色列图像，并向以色列运动员发送威胁，伪装成极右翼组织Regiment GUD。

**三、攻击过程技术分析：**

Check Point Research在FBI、美国财政部和INCD的联合网络安全咨询后，对WezRat进行了深入分析。WezRat的早期版本可以追溯到2023年8月，也被归咎于Emennet Pasargad。

* **钓鱼邮件：**钓鱼邮件包含了一个链接，看似指向官方的INCD网站，但实际上是一个欺骗性的相似域名。受害者点击链接后，会自动下载名为“Google Chrome Installer”的文件，然后被重定向到真正的INCD网站。
* **感染链：**下载的“Google Chrome Installer”包含了合法的Google Chrome安装程序和相关文件，但也包含了WezRat的最新版本，一个名为Updater.exe的后门。
* **WezRat功能：**WezRat能够执行命令、截屏、上传文件、执行键盘记录和窃取剪贴板内容及cookie文件。某些功能由从命令和控制（C&C）服务器下载的DLL文件形式的个别模块执行，使后门的主要组件看起来不那么可疑。
* **后端代码：**Check Point Research在分析中发现了WezRat后端的部分源代码，并找到了证据表明可能有不同组织负责恶意软件的开发和操作。通常，一个攻击者会开发并操作工具，但在这个案例中，很明显有一个拥有开发和操作部门的组织在背后支持恶意软件。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMINbvOHEVtklnFL0uias5sFP3lOdZiayCW594QrJ9NmtMNNTc2VRxCr48b3ibibX5GV8dpe59UxtRor12w/640?wx_fmt=png&from=appmsg)图 1 WezRat感染链

**四、事件总结**

在本次事件中，发现伊朗网络组织Emennet Pasargad利用精心设计的钓鱼邮件和高级定制的WezRat恶意软件，展现了其在技术层面的先进性和执行复杂网络间谍活动的灵活性。WezRat的多功能性和模块化设计不仅使其成为一个难以检测和防御的威胁，而且能够执行包括远程命令注入和数据窃取在内的多种攻击阶段的恶意活动。此外，Emennet Pasarga组织还展示了其根据不同的目标和情境调整攻击策略的能力，这进一步证明了该组织在国际网络空间中的威胁潜力。

参考链接：

https://blog.checkpoint.com/research/spotlight-on-iranian-cyber-group-emennet-pasargads-malware/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

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