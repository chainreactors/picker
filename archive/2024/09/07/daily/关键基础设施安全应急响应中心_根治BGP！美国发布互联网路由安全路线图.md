---
title: 根治BGP！美国发布互联网路由安全路线图
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247545669&idx=4&sn=f34ae6052088fdfc551f7cf8fe50f201&chksm=c1e9bf14f69e36026ceb885a7c7d876e3ca7d07e3127f6867b485d37b5dd962b8ed620dcb3f8&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-09-07
fetch_date: 2025-10-06T18:28:41.438152
---

# 根治BGP！美国发布互联网路由安全路线图

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogtZ17otShtbHTC4iccVibXHVRT0ibnZgvLEGicva3Jp13seOz2LYI50lYJ17aTia2NIc7Q9OLUiaTVsXuSw/0?wx_fmt=jpeg)

# 根治BGP！美国发布互联网路由安全路线图

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogtZ17otShtbHTC4iccVibXHVRrrERXODLJwyB9LIG6MXqrCtMuWcRaKGrmq9W8CXeu0PJ6GLctz7d9w/640?wx_fmt=png&from=appmsg)

为加固互联网路由安全的薄弱环节，美国国家网络安全办公室（ONCD）近日发布了一个提升互联网路由安全的路线图，主要针对边界网关协议（BGP）相关漏洞进行改进。

BGP作为全球互联网的基础协议，负责全球超过7万个独立网络间的流量管理，广泛应用于ISP、云服务提供商、政府机构、大学和能源供应商等。ONCD指出，BGP的设计缺乏现代互联网所需的安全措施，这使得网络流量可能被意外或恶意重定向，导致关键基础设施面临风险，并可能为间谍活动、数据盗窃和安全漏洞提供掩护。

**推动RPKI成为全球标准**

ONCD路线图中提出了广泛采用资源公钥基础设施（RPKI）的建议。RPKI是由IETF制定的标准框架，能够通过防止路由劫持、路由泄漏和IP资源劫持等手段来提升安全性。通过实施RPKI，互联网服务提供商（ISP）和运营自己的路由网络的企业可以确保BGP公告和路由更新的合法性和安全性，避免数据传输中断或被恶意篡改。

**RPKI与BGP的对比明显，如文末所示**

国家网络安全办公室呼吁所有网络类型的运营商，包括ISP、企业网络和拥有自己IP资源的组织，尽快采用RPKI标准。特别是对于关键基础设施的运营商、州和地方政府，以及依赖互联网进行“高价值”任务的组织，BGP的安全尤为重要。

白宫国家网络安全主任Harry Coker Jr.在发布报告时表示：“互联网安全事关重大，联邦政府将率先推动BGP安全措施的快速普及。”

除了发布报告，ONCD还设立了公私合作的利益相关者工作组，并共同主持了互联网路由安全工作组。该工作组将制定框架，帮助网络运营商评估风险，优先处理关键的IP地址资源和路由源。

**BGP漏洞的安全风险**

BGP作为全球互联网的基础协议，广泛应用于ISP、云服务提供商、政府机构、大学和能源供应商等。然而，ONCD指出，BGP的设计缺乏现代互联网所需的安全措施，这使得网络流量可能被意外或恶意重定向，导致关键基础设施面临风险，并可能为间谍活动、数据盗窃和安全漏洞提供掩护。

互联网基础设施提供商Cloudflare指出，全球只有约一半的网络采用了RPKI。过去几年，曾发生过多起重大BGP安全事件，例如：

* 2021年4月：全球性BGP泄漏事件。这次BGP路由泄漏导致全球数千个网络受到影响。事件的起因是一个错误的BGP路由配置，导致原本不应该被广告的路由被传播到全球，影响了多个国家的互联网连接(。
* 2022年8月：加密货币服务Celer Bridge的BGP劫持。黑客通过伪造的BGP公告成功劫持了Celer Bridge的加密货币交易，重定向资金到攻击者的账户。此次事件通过更改AltDB数据库的内容欺骗了传输提供商，使攻击者得以冒充亚马逊网络服务（AWS）来进行劫持。
* 2008年：YouTube被封锁事件。巴基斯坦电信公司（PTCL）通过BGP劫持全球范围内的YouTube流量，试图在国内封锁该服务。虽然该举动本应仅影响巴基斯坦境内的访问，但错误的路由公告传播到了全球，导致YouTube在全世界范围内下线。

这些事件凸显了BGP的脆弱性，无论是有意的攻击还是无意的配置错误，都会导致全球互联网服务中断和安全隐患。

专家们认为，全球互联网路由依赖信任而非安全是不可持续的。Team8风投集团的首席技术官Eidan Siniver指出：“企业经常在全球站点之间传输敏感数据，而被劫持的路由将带来重大安全风险。网络运营商应当广泛采用RPKI等框架，优先考虑安全而非信任，建立可靠的标准。”

**参考链接：**

https://www.whitehouse.gov/wp-content/uploads/2024/09/Roadmap-to-Enhancing-Internet-Routing-Security.pdf

原文来源：GoUpSec

“投稿联系方式：sunzhonghao@cert.org.cn”

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