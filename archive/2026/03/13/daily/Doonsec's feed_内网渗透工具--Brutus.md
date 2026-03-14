---
title: 内网渗透工具--Brutus
url: https://mp.weixin.qq.com/s/FHFMiwhP2Qs1wmo3NrMUAA
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:04:28.254762
---

# 内网渗透工具--Brutus

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EYGYnyEdzQVnfKlBBJF29xcB3yeicp0TgicVNLePc8zGXQX3nqjqs5fW2btaBfCa2WVVreslO3VC0ibwPiaz4XIMM00V6vWseakNKx4zQDWNdAk/0?wx_fmt=jpeg)

# 内网渗透工具--Brutus

原创

Hello888
Hello888

安全天书

![]()

在小说阅读器中沉浸阅读

0x01 工具介绍

Brutus 是一款多协议认证测试工具，旨在弥补攻击性安全工具中的关键空白：在不同网络服务间高效的凭证验证。虽然HTTP相关工具众多，但渗透测试人员和红队操作员经常遇到需要专门开发认证测试功能的数据库、SSH、SMB及其他网络服务。

Brutus 内置于 Go 中，作为单一二进制，零外部依赖，与 Nerva 无缝集成，实现自动化服务发现，使运营商能够快速识别和测试整个网络范围的认证向量。

**主要特点：**

* **零依赖：**

  单一二进制，跨平台（Linux、Windows、macOS）
* **24个协议：**

  SSH、RDP、MySQL、PostgreSQL、MSSQL、Redis、SMB、LDAP、WinRM、SNMP、HTTP Basic Auth 等
* **管道集成：**

  原生支持 Nerva 和 naabu 工作流程
* **嵌入的坏密钥：**

  内置的已知SSH密钥集合（Vagrant、F5、ExaGrid等）
* **去图书馆：**

  直接导入到你的安全自动化工具中
* **量产准备：**

  速率限制、连接池化以及全面的错误处理

![布鲁图斯 - 社交](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQUmhuKcFEib6yUod691mibg5BSjTyM4wzI5uVV264ncA8uHfYnbBZGb2UuicBNXMWLfjKLtjeqosppvBDABjdYwXZ7ia56xVDoBgQI/640?wx_fmt=png&from=appmsg)

GitHub地址：

```
https://github.com/praetorian-inc/brutus
```

注意：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测。

0x02 红蓝偶像练习生小圈子

********更多工具思路文章请加入纷传，圈子主要研究方向渗透测试、红蓝对抗、钓鱼手法思路、武器化，红队工具二开与免杀。圈内不定期分享红队技术文章，攻防经验总结以及自研工具与插件，目前圈子已满300人，欢迎各位进圈子交流学习！****

****圈子目前更新相关技术文章：**

***** HeavenlyBypassAV内部版工具-轻松免杀各大杀软
* Heavenly白加黑自动化生成免杀工具
* HeavenlyProtectionCS内部CS插件
* 冰蝎webshell免杀工具

* 哥斯拉webshell免杀工具
* 红队场景下lnk钓鱼Bypass免杀AV
* Frp免杀隧道工具
* 1day和0dayPOC
* lnk钓鱼思路视频讲解
* lnk钓鱼Bypass天擎
* msi钓鱼
* chm钓鱼
* Kill360核晶
* AV对抗-致盲AV（核晶）
* 捆绑免杀360
* Kill火绒
* 火绒6.0内存免杀
* kill-windows Defender

* Defender分离免杀
* Defender知识点
* EDR对抗思路
* 进程注入知识点

* 自启动思路
* **多种维权手法**

* Fscan免杀核晶
* QVM解决思路
* 红队思路-钓鱼环境下小窗口截屏窃取
* 免杀Todesk/向日葵读取工具

* 渗透测试文章思路
* 内网对抗文章思路
* **还有更多红队工具文章！期待您的加入！！！************

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/EYGYnyEdzQXmVYS9hIoU83xJ7qBXCpsCPnwZDe2aGica6MHawOA5XEx0EIKvolCwvBlxvF1RiboN9ibWkEyll8KA0Hicjr6S4F57J3IKecmeTsQ/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwFJAbuLxnpEkoczbwU8nmFmKaFw3zgem3QN1qrEVzBcicTB89hFKwPia7PYosgibSltTEK1h9YEhiblkA/0?wx_fmt=png)

安全天书

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwFJAbuLxnpEkoczbwU8nmFmKaFw3zgem3QN1qrEVzBcicTB89hFKwPia7PYosgibSltTEK1h9YEhiblkA/0?wx_fmt=png)

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