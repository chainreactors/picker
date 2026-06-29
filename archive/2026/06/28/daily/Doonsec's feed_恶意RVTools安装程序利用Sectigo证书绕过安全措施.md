---
title: 恶意RVTools安装程序利用Sectigo证书绕过安全措施
url: https://mp.weixin.qq.com/s/KgRX5X3aURqOeqfec6ncTg
source: Doonsec's feed
date: 2026-06-28
fetch_date: 2026-06-29T06:33:27.968339
---

# 恶意RVTools安装程序利用Sectigo证书绕过安全措施

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/J7CSmJcRR8mrnW8bib8O2jyQdlict6ITuefia5BXN5aibbsjNfPz7ATRrO8meB2oMwtyhksAqvib2GeELe5mK9pHlpSj0U4NclERzJfXtVC4duZc/0?wx_fmt=jpeg)

# 恶意RVTools安装程序利用Sectigo证书绕过安全措施

Khan安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

•一个伪造的RVTools安装程序使用合法的Sectigo证书来绕过安全措施。

•该恶意软件部署了一个基于Python的远程访问木马 (RAT)，具备深度 AD 侦察能力。

•VMware管理员权限一旦被攻破，攻击者就可能获得域级控制权。

一款伪造的RVTools安装程序利用合法的Sectigo代码签名证书绕过了Microsoft Defender SmartScreen和其他终端安全防护措施。该恶意软件部署了一个基于Python 的多阶段远程访问木马 (RAT)，能够对 Active Directory 进行广泛的侦察，并维持持久的命令与控制 (C2) 访问权限。此次攻击主要针对VMware环境，对依赖RVTools管理虚拟基础架构的 IT 管理员构成重大风险。如果管理员账户被攻破，攻击者即可获得对受影响系统的域级控制权。此次事件凸显了供应链攻击和网络威胁中滥用可信证书所带来的持续挑战。目前，该事件正在调查中，建议各组织保持警惕。

![](https://mmbiz.qpic.cn/mmbiz_png/J7CSmJcRR8nIOwtIiaoEGSBZHayXgVZUQ6Sk9oUBrEaa7V93NjTrNFZ8gA4syfU0ekhiaS8J1mtaPyuTRMG9h18vFQGwWfe6D8f4nCWI3dXnI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8mLd8Lf7Cib1F5AkxOQE7V4RD4jenk4fibxkdvDr5Fo9fEbLUNiaQKgDAlVXysecTDRZLicaMlSNrGdEJ4fOov8SKkVtoHlPnduuFY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/J7CSmJcRR8l5LmaGFfsvzbxTBoQib0vAWLZGZhYulX9utQu6E11mjk1CqJOf4icgVEHDLYibt2JTJZH85RdKRXGz7Rc6GTQsichBjMn2R04dh7M/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

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