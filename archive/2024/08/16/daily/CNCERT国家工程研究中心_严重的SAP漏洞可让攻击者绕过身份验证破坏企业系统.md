---
title: 严重的SAP漏洞可让攻击者绕过身份验证破坏企业系统
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546452&idx=3&sn=9bfff01554c90d3f5b8ffdc01dc133a2&chksm=fa938095cde409836c7514d175aaa78dfd397150b7ec1615b07bae900fb128468b9d9dd6742c&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-16
fetch_date: 2025-10-06T18:04:39.166561
---

# 严重的SAP漏洞可让攻击者绕过身份验证破坏企业系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kialeQiaq8ywHPrWbq6Iia8ZVOW1q0qfnDCDEYCJU6bzcChPKP1pV64B9ktkED2vkA5qQE9F8VnrPrQ/0?wx_fmt=jpeg)

# 严重的SAP漏洞可让攻击者绕过身份验证破坏企业系统

网络安全应急技术国家工程中心

据BleepingComputer消息，全球最大的ERP供应商SAP在本月修复了一批重要漏洞，其中包含一个关键的身份验证绕过漏洞，该漏洞可能允许攻击者完全破坏系统。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38aFWEYXzWD4MYOEu23mGC0AK8S5p49ELljPm4Pia2Dp5bfCU2lGPa8hoR9MDkVv0Id1FCPfSDVrBQ/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic)

漏洞被跟踪为 CVE-2024-41730，CVSS v3.1 评分高达9.8，影响 SAP BusinessObjects Business Intelligence Platform 430 和 440版本 。根据漏洞描述，如果在企业身份验证上启用了单点登录，则未经授权的用户可以使用REST端点获取登录令牌。攻击者可以完全破坏系统，从而对机密性、完整性和可用性产生重大影响。

另一个评分达9.1的漏洞被追踪为CVE-2024-29415，与 Node.js 的「IP」包中的一个缺陷有关，该包会检查 IP 地址是公共还是私有。当使用八进制表示时，会错误地将「127.0.0.1」识别为公有且全局可路由的地址。该漏洞影响版本低于4.11.130 的 SAP Build Apps。

其他一些评分在7.4至8.2的漏洞也同样不容忽视，包括：

* CVE-2024-42374– SAP BEx Web Java 运行时导出 Web 服务中的 XML 注入问题。影响 BI-BASE-E 7.5、BI-BASE-B 7.5、BI-IBC 7.5、BI-BASE-S 7.5 和 BIWEBAPP 7.5版本。
* CVE-2023-30533– 与 SAP S/4 HANA 中的原型污染相关的漏洞，特别是在「管理供应保护」模块中，影响低于 0.19.3 的 SheetJS CE 库版本。
* CVE-2024-34688– SAP NetWeaver AS Java 中的拒绝服务 （DOS） 漏洞，特别影响 Meta Model Repository 组件的MMR\_SERVER 7.5版本 。
* CVE-2024-33003– 与 SAP Commerce Cloud 中的信息泄露问题相关的漏洞，影响 HY\_COM 1808、1811、1905、2005、2105、2011、2205 和 COM\_CLOUD 2211版本。

由于SAP是全球最大的ERP供应商，福布斯全球2000强榜单中有90%的企业使用了相关产品，因此黑客一直在利用SAP的漏洞，试图攻击这些高价值的企业网络。在2020年6月至2021年3月间，攻击者就利用未及时打补丁的SAP 系统，至少进行了300起公司网络渗透行为。

**参考资料：**

https://www.bleepingcomputer.com/news/security/critical-sap-flaw-allows-remote-attackers-to-bypass-authentication/

原文来源：FreeBuf

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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