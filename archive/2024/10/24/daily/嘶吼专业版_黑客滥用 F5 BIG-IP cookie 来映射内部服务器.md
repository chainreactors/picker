---
title: 黑客滥用 F5 BIG-IP cookie 来映射内部服务器
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247578604&idx=1&sn=110acb68d6277bf726f8b7831b679e13&chksm=e91463d6de63eac06d3386a4f614a0bf8dc283bd5d875e60950d136d23735274e0749b981ffd&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-10-24
fetch_date: 2025-10-06T18:53:25.287361
---

# 黑客滥用 F5 BIG-IP cookie 来映射内部服务器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibq1iaibeZMg2yqSs3wykjJCMYCE2IswH5gOc4Hr8ibxibNpo0hFa7jJFCruicCyZC4lyFxnGQuKVW82pQ/0?wx_fmt=jpeg)

# 黑客滥用 F5 BIG-IP cookie 来映射内部服务器

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

CISA 表示，已发现威胁分子滥用未加密的持久性 F5 BIG-IP cookie 来识别和瞄准目标网络上的其他内部设备。

通过绘制内部设备图，威胁者可以潜在地识别网络上易受攻击的设备，作为网络攻击规划阶段的一部分。

据 CISA 表述，“恶意分子可以利用从未加密的持久性 cookie 收集的信息来推断或识别其他网络资源，并可能利用网络上其他设备中发现的漏洞。”

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibq1iaibeZMg2yqSs3wykjJCM05DW8vwyFehh2ZJibic8Wg5VzKliaE2u6BDO4MR316DHfG4lUKSkicGN4A/640?wx_fmt=png&from=appmsg)F5 持久会话 cookie

F5 BIG-IP 是一套应用程序交付和流量管理工具，用于负载平衡 Web 应用程序并提供安全性。其核心模块之一是本地流量管理器（LTM）模块，它提供流量管理和负载平衡，以在多个服务器之间分配网络流量。使用此功能，客户可以优化其负载平衡的服务器资源和高可用性。

产品中的本地流量管理器 (LTM) 模块使用持久性 cookie，通过每次将来自客户端（Web 浏览器）的流量引导到同一后端服务器来帮助维护会话一致性，这对于负载平衡至关重要。

“Cookie 持久性使用 HTTP cookie 强制执行持久性”F5 的文档解释道。

与所有持久模式一样，HTTP cookie 确保来自同一客户端的请求在 BIG-IP 系统最初对它们进行负载平衡后被定向到同一池成员。如果同一池成员不可用，系统会进行新的负载权衡决定。

这些 cookie 默认情况下未加密，可能是为了保持旧配置的操作完整性或出于性能考虑。从版本 11.5.0 及更高版本开始，管理员获得了一个新的“必需”选项来对所有 cookie 强制加密。

那些选择不启用它的人会面临安全风险。但是，这些 cookie 包含内部负载平衡服务器的编码 IP 地址、端口号和负载平衡设置。

多年来，网络安全研究人员一直在分享如何滥用未加密的 cookie 来查找以前隐藏的内部服务器或可能未知的暴露服务器，这些服务器可以扫描漏洞并用于破坏内部网络。还发布了一个 Chrome 扩展程序来解码这些 cookie，以帮助 BIG-IP 管理员排除连接故障。

据 CISA 称，威胁者已经在利用宽松的配置进行网络发现，并建议 F5 BIG-IP 管理员查看供应商有关如何加密这些持久 cookie 的说明。

请注意，“首选”配置选项会生成加密的 cookie，但也允许系统接受未加密的 cookie。可以在迁移阶段使用此设置，以允许先前发出的 cookie 在强制执行加密 cookie 之前继续工作。

当设置为“必需”时，所有持久 cookie 均使用强 AES-192 加密进行加密。据了解，F5 还开发了一种名为“BIG-IP iHealth”的诊断工具，旨在检测产品上的错误配置并向管理员发出警告。

参考及来源：https://www.bleepingcomputer.com/news/security/cisa-hackers-abuse-f5-big-ip-cookies-to-map-internal-servers/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibq1iaibeZMg2yqSs3wykjJCMaG8gPxrs0LFOyqNskRHX7sB625RejTvaZduht3PKaDlM6qUAlCfW2Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibq1iaibeZMg2yqSs3wykjJCMdVS4AQYEJ87uzcZrHVf58C28wvpCu3eEQpqJlqHYuaLnHhEwYicJQVg/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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