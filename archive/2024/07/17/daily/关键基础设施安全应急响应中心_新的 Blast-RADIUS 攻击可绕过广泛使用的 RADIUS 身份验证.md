---
title: 新的 Blast-RADIUS 攻击可绕过广泛使用的 RADIUS 身份验证
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247544903&idx=2&sn=92f7e3697709429816e2f6d510f56df9&chksm=c1e9bc16f69e3500a230d5577ae5f5adf697dd2563354f1541d9644b2b2372367181ff8c0e47&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-07-17
fetch_date: 2025-10-06T17:42:05.189888
---

# 新的 Blast-RADIUS 攻击可绕过广泛使用的 RADIUS 身份验证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogsHicPzxApWEev2pDv8Xwv5sOsAwu1XEAdicnaJ0vSCXAnia0EBFicnZIQQ34CzTkjtZr8L53GgiaTAr9w/0?wx_fmt=jpeg)

# 新的 Blast-RADIUS 攻击可绕过广泛使用的 RADIUS 身份验证

关键基础设施安全应急响应中心

Blast-RADIUS 是广泛使用的 RADIUS/UDP 协议中的一种身份验证绕过方法，它使威胁分子能够通过中间人 MD5 碰撞攻击侵入网络和设备。

企业和电信网络上的许多联网设备（包括交换机、路由器和其他路由基础设施）都使用身份验证和授权 RADIUS（远程身份验证拨入用户服务）协议，有时单个网络上有数万台设备。

该协议具有广泛的应用范围，可用于 DSL 和 FTTH（光纤到户）、802.1X 和 Wi-Fi、2G 和 3G 蜂窝漫游、5G DNN（数据网络名称）、私有 APN 和 VPN 以及关键基础设施网络中的身份验证。

Blast-RADIUS 利用了新的协议漏洞 (CVE-2024-3596) 和 MD5 碰撞攻击，允许有权访问 RADIUS 流量的攻击者操纵服务器响应并添加任意协议属性，从而使他们无需暴力破解或窃取凭据即可获得 RADIUS 设备的管理员权限。

Blast-RADIUS 攻击允许 RADIUS 客户端和服务器之间的中间人攻击者伪造有效的协议接受消息来响应失败的身份验证请求。而这种伪造可以让攻击者访问网络设备和服务，而无需攻击者猜测或暴力破解密码或共享机密。攻击者无法获知用户凭证。

攻击者可以将权限从部分网络访问提升到能够登录任何使用 RADIUS 进行身份验证的设备，或者为自己分配任意网络权限。

在设备上执行身份验证时，RADIUS 协议使用 MD5 哈希请求和响应。研究人员的概念验证漏洞（尚未共享）计算出伪造有效“Access-Accept”响应所需的 MD5 选择前缀哈希碰撞，以表示身份验证请求成功。然后使用中间人攻击将伪造的 MD5 哈希注入网络通信，允许攻击者登录。

该漏洞需要 3 到 6 分钟才能伪造此 MD5 哈希值，比 RADIUS 实际中通常使用的 30 到 60 秒的超时时间要长。

然而，攻击中使用的碰撞算法的每个步骤都可以有效地并行化，并且适合硬件优化，这将使资源充足的攻击者能够使用 GPU、FPGA 或其他更现代、更快的硬件实施攻击，以实现更快的运行时间，可能快几十倍或几百倍。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28ZiaGRiagXibkMtm9Lydxc7cH7G3FRZclKOKrib3BxHgjDygFcoMWog4LTic7h4HeiaicKAx27hCnoJbWiaw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

攻击流

安全研究小组表示：“虽然 MD5 哈希碰撞在 2004 年首次被证明，但人们认为不可能在 RADIUS 协议环境中利用这一点。”“我们的攻击确定了 RADIUS 使用 MD5 的方式中的协议漏洞，该漏洞允许攻击者注入恶意协议属性，从而在服务器生成的响应认证器和攻击者想要的伪造响应数据包之间产生哈希碰撞。

此外，由于攻击是在线的，攻击者需要能够在几分钟或几秒钟内计算出所谓的选择前缀 MD5 碰撞攻击。之前报道的最佳选择前缀碰撞攻击时间需要数小时，并且产生的碰撞与 RADIUS 协议不兼容。

由于此攻击不会危及最终用户凭证，因此用户最终无法采取任何措施来防范此攻击。但是，安全研究人员建议制造和管理 RADIUS 设备的供应商和系统管理员遵循这些最佳实践和指导。

为了防御这种攻击，网络运营商可以升级到 TLS 上的 RADIUS（RADSEC），切换到“多跳” RADIUS 部署，并使用受限访问管理 VLAN 或 TLS/IPsec 隧道将 RADIUS 流量与互联网访问隔离。

**参考及来源：**

https://www.bleepingcomputer.com/news/security/new-blast-radius-attack-bypasses-widely-used-radius-authentication/

原文来源：嘶吼专业版

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