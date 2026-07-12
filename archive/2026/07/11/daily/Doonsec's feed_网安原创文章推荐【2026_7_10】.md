---
title: 网安原创文章推荐【2026/7/10】
url: https://mp.weixin.qq.com/s/c1_lPc-fD16pxJCfvgwjrg
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:10:26.930933
---

# 网安原创文章推荐【2026/7/10】

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CZMNsicRfJAAxofufzrWe2LZu9IGavCzgEBibTWxnmPG9mT2R90EyicNhjMFN6lFm8ias2jd4WgibAXJesugboSPvOBLmCjNywNnA57WPExHcoib8/0?wx_fmt=jpeg)

# 网安原创文章推荐【2026/7/10】

AJay13
AJay13

洞见网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 2026-07-10 微信公众号精选安全技术文章总览

> 洞见网安 2026-07-10

---

### 0x1 [群友靶机之Putty](https://mp.weixin.qq.com/s?__biz=Mzg3MjgxMzkzMg==&mid=2247487399&idx=1&sn=c046cd9b92c5c165471452641edebceb&scene=21#wechat_redirect "群友靶机之Putty")

> MS02423 2026-07-10 11:01:33

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8avkpGSKmqdpkeVpuxElYrQvgXto34ankkjMQXYB0BZpI329H8Zlu8d2RsfrAkVq0ibibgYlXO3P3oMeKVN5oKMtcyO8UPBGmrUjnj9IU0OdM/640?wx_fmt=jpeg)

本文记录了一次针对Sublarge佬的网络安全靶机实战过程。作者首先通过rustscan探测靶机开放端口，发现80端口存在信息，随后使用gobusterdir进行目录扫描，并绕过了403错误，成功获取了名为1.zip的文件。通过分析，发现该文件包含PuTTY格式的SSH私钥，但需转换成OpenSSH格式。作者成功连接到系统后，尝试获取rosers用户的shell权限，并通过公钥写入到brendon用户的.ssh/authorized\_keys中，使用SSH密钥登录rosers用户。最后，作者通过将RFC4716格式的公钥写入root用户的.ssh/authorized\_keys，成功以root用户权限登录系统。整个渗透过程详细展示了信息收集、漏洞利用、权限提升和提权等网络安全攻击步骤。

渗透测试

网络安全漏洞

靶场学习

SSH安全

Web安全

信息收集

---

### 0x2 [【CVE-2026-46215】通过 DRM GEM change\_handle 中的UAF功能获得ROOT权限](https://mp.weixin.qq.com/s?__biz=MjM5Mzc4MzUzMQ==&mid=2650265660&idx=1&sn=27a23119e5e86ecb74838f20c2280bc4&scene=21#wechat_redirect "【CVE-2026-46215】通过 DRM GEM change_handle 中的UAF功能获得ROOT权限")

> 骨哥说事 2026-07-10 09:49:24

![](https://mmbiz.qpic.cn/mmbiz_jpg/TKdPSwEibsZhbU5gKhdWoEmFIv8Vz3zBrODtb8yibDX0uqGrRS8B07YRMPrdnVFJmdn41F1icyC0J9wSDJZtZxpNJWULvicY6bBDeVtNjDXWct8/640?wx_fmt=jpeg)

本文详细介绍了一个存在于DRM GEM核心ioctl DRM\_IOCTL\_GEM\_CHANGE\_HANDLE 中的释放后重用漏洞，该漏洞允许任何能访问渲染节点的本地用户提升至root权限。漏洞源于drm\_gem\_change\_handle\_ioctl()在移动GEM对象句柄时，未正确调整对象的handle\_count，导致在短暂的时间窗口内，对象存在两个IDR条目而其句柄计数仍显示为1。在此期间，若对旧句柄执行并发DRM\_IOCTL\_GEM\_CLOSE，会导致计数降至0并释放对象，而新句柄仍指向该已释放的对象，形成悬垂句柄，造成释放后重用。由于相关ioctl标记为DRM\_RENDER\_ALLOW，任何能打开/dev/dri/renderD\*的本地用户均可触发此漏洞。在主流桌面发行版上，systemd-logind 默认授予活动会话读写该节点的权限，因此普通登录用户无需特殊权限即可利用此漏洞。文章还描述了利用链的构建过程，包括通过喷洒pipe\_buffer数组回收其slab槽位、泄漏内核指针以绕过KASLR、设置PIPE\_BUF\_FLAG\_CAN\_MERGE来绕过DirtyPipe修复，以及通过页面缓存覆盖只读的/etc/passwd，最终实现无密码root权限获取。修复方案由David Francis和Dave Airlie提出，他们选择直接禁用change\_handle ioctl而非持续修补，并在7.1版本中彻底移除该接口。

内核漏洞

竞争条件

提升权限

本地漏洞

引用计数错误

DRM

内核安全

利用链

---

### 0x3 [OPNsense Root RCE 漏洞(CVE-2026-57155，CVSS 9.9) PoC已公开，建议立即升级！](https://mp.weixin.qq.com/s?__biz=Mzk2OTAzNjI0OQ==&mid=2247486365&idx=1&sn=bd252745a95c59647e31727e39a4ff32&scene=21#wechat_redirect "OPNsense Root RCE 漏洞(CVE-2026-57155，CVSS 9.9) PoC已公开，建议立即升级！")

> 杂杂咱谈 2026-07-10 08:55:31

![](https://mmbiz.qpic.cn/mmbiz_jpg/xoBWaEOhvRHKbF3VUarJA9Pqiaz329kXP8ReQscHW5VYIMOI4ICtMic0C9OTWSdoSLTo73zjjzbGYZBmlA5xjoGV4dpIdS42Y6v3a5SwgZo6Y/640?wx_fmt=jpeg)

本文详细介绍了OPNsense防火墙中一个严重的高危漏洞CVE-2026-57155。该漏洞CVSS评分高达9.9，允许攻击者通过拥有Firewall: Alias: Edit权限，利用GeoIP Alias Importer功能中的任意文件写入缺陷，最终获取Root权限并执行任意代码。漏洞允许攻击者从任意URL下载恶意数据库，通过构造恶意路径写入系统任意位置。官方已发布修复更新，建议用户升级至最新版本以消除风险。文章还提供了漏洞的详细技术分析、影响版本、修复版本以及安全建议，包括立即升级、收紧权限管理、检查异常配置和加强日志监控等，以帮助用户降低被攻击的风险。

漏洞分析

安全漏洞

防火墙安全

权限提升

PoC公开

安全建议

开源安全

---

### 0x4 [你的 Claude Code 可能在偷偷“汇报”——官方通报后门，附处置 checklist](https://mp.weixin.qq.com/s?__biz=MzkxNDg4MDk4Mw==&mid=2247484171&idx=1&sn=afae4bac73d2faeb648e79fb20645acd&scene=21#wechat_redirect "你的 Claude Code 可能在偷偷“汇报”——官方通报后门，附处置 checklist")

> 重生之咸鱼说安全 2026-07-10 08:54:48

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wKN9JEVmFPGkr1lWcAUnwSdicvy68foO9F6blJLZKA8pxKyVeyug7LYKpwhSUMFFLtv9wShXH1YfwEVjKZPxDZ21LIEyic8CKNUsYKWz7Wqnc/640?wx_fmt=jpeg)

近日，工信部网络安全威胁和漏洞信息共享平台（NVDB）发布风险提示，指出美国Anthropic公司开发的AI编程工具Claude Code存在安全后门隐患。该工具在v2.1.91至v2.1.196版本中，未经用户同意向远程服务器回传地域、身份标识等敏感信息。Claude Code的监控机制通过静默扫描环境、使用Unicode撇号变体打隐写水印、随正常请求回传水印等手段，几乎不被防火墙检测到。事件暴露出AI coding工具在运行于最高权限的开发终端时，可能对代码仓库和本地配置构成威胁。NVDB建议受影响终端立即卸载或升级至最新版本，并加强网络层、终端层和治理层的防护措施。

AI工具安全

安全后门

数据泄露风险

软件供应链安全

监管与合规

漏洞分析

网络安全事件

逆向工程

隐私保护

---

### 0x5 [【应急响应】 护网中，蓝队该如何撰写技法？](https://mp.weixin.qq.com/s?__biz=Mzk3NTIwNDg5NQ==&mid=2247484393&idx=1&sn=beedccfe2978ce07905756506b09c563&scene=21#wechat_redirect "【应急响应】 护网中，蓝队该如何撰写技法？")

> 那夜的雨夹雪 2026-07-10 08:13:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/87RZbucUFbPOo7l6ibBp968SVianeVkLT9Z96wBibLoKzXsgs1mM568H5aZolVhjV3kObq8dxTqF5ic5SzUm9kWGCJRwr1CicA2vgmD7sllGqkvI/640?wx_fmt=jpeg)

本文探讨了网络安全攻防演练中蓝队如何撰写技战法文档。文章首先明确了技战法的定义和重要性，指出技战法是攻防对抗过程中实战技巧的系统化总结，能够为参赛人员提供攻防思路参考与实战指导。接着，文章从多个角度分析了技战法的选题方向，包括溯源反制、资产漏洞管控、装备设备工具产品、情报分析、应急处置和整体防御策略等。此外，文章还提供了几个技战法主题的参考，并介绍了技战法文章的常见架构，包括背景、目的、思路、主要内容、总结等。最后，文章以一个反制红队AI的技战法示例进行说明，并推荐了一些相关文章和博客，供读者参考学习。

网络安全应急响应

网络安全攻防演练

技战法撰写

溯源反制

资产漏洞管控

安全设备工具

情报分析

应急处置

整体防御策略

人工智能在网络安全

---

### 0x6 [CVE复现 | CVE-2026-31816漏洞复现](https://mp.weixin.qq.com/s?__biz=MzkxNjcyMTc0NQ==&mid=2247485426&idx=1&sn=5d1ee2a8dda094bf58d16dea079b72e4&scene=21#wechat_redirect "CVE复现 | CVE-2026-31816漏洞复现")

> 凌日网络与信息安全团队LapR1skT 2026-07-10 08:00:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/oltLnnib9JXRGWVVFWXejn3mFhdcq4CWle17TfibiapTqhXuutTDmicIAbgKrBGOYFG9m2bZQTfhAHsWUT4Pib7xug2gGKO8BrTibjibDSHPJ6e4Qo/640?wx_fmt=jpeg)

本文详细介绍了CVE-2026-31816漏洞的复现过程。该漏洞存在于Budibase开源低代码平台中，由于服务端authorized()中间件在处理Webhook路径时使用了非锚定正则表达式，导致攻击者可以通过在API请求末尾拼接特定的Webhook路径字符串来绕过身份认证和CSRF防护，实现对服务端所有API端点的完全访问和操作。文章中提供了漏洞逻辑源码地址、代码定位、环境配置和漏洞验证的详细步骤，包括基于docker-compose搭建环境、启动服务、创建workspace以及如何通过附加Webhook路径模式来获取appid和敏感信息。同时，文章还引用了相关参考资料，并提出了免责声明。

漏洞复现

低代码平台安全

Webhook安全

身份认证漏洞

CSRF防护

API安全

开源软件安全

---

### 0x7 [TLCP（ECC\_SM4\_CBC\_SM3）流量包验签解密](https://mp.weixin.qq.com/s?__biz=MzU1Mjk3MDY1OA==&mid=2247525830&idx=1&sn=f6453c1e7118cc1b40fb486cf6e3d3e8&scene=21#wechat_redirect "TLCP（ECC_SM4_CBC_SM3）流量包验签解密")

> 利刃信安 2026-07-10 00:30:00

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZaibroIiatwe0KVibmR3v8TU8odc2gnQAUic5c1vmKbmm1S9ONNXia02OyazO8lStqQgOPFVOBy5JibJLDhj2jT5uma8dDKQTzStu6cttwouDZ0dM/640?wx_fmt=jpeg)

本文详细分析了TLCP（ECC\_SM4\_CBC\_SM3）协议的流量包验签解密过程，涉及SM2验签、SM4-CBC解密和HMAC-SM3完整性校验。文章首先介绍了协议概览，包括协议类型、鉴别类型、密码套件、加密算法、杂凑算法和签名算法等。接着，详细描述了TLCP握手流程，包括客户端和服务端的交互过程。在SM2签名验签过程中，文章解释了随机数生成、服务端证书、签名值、签名源数据和验签过程。密钥派生过程部分，介绍了预主密钥、主密钥和工作密钥的派生方法。SM4-CBC逐条解密过程部分，详细解析了EtM算法、记录1（客户端Handshake）、记录2（服务端Handshake）、记录3（客户端AppData）和记录4（服务端AppData）的解密和HMAC验证过程。最后，文章总结了密码学算法参数和HMAC-SM3验证详解，验证了所有记录的HMAC有效性。

---

> 本站文章为人工采集，目的是为了方便更好的提供免费聚合服务，如有侵权请告知。具体请在留言告知，我们将清除对此公众号的监控，并清空相关文章。所有内容，均摘自于互联网，不得以任何方式将其用于商业目的。由于传播，利用此文所提供的信息而造成的任何直接或间接的后果和损失，均由使用者本人负责，本站以及文章作者不承担任何责任。

预览时标签不可点

内容含AI生成图片

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vML07fExwAdpcFbk9icEKB6QPwpicFcfu6QHCmkibP2yszUiaajx3CdP1cmNyq7ZGL40Q92d5QRpsY9yBTcgGlLNcg/0?wx_fmt=png)

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