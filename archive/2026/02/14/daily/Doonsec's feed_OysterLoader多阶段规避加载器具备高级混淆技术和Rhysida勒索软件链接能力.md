---
title: OysterLoader多阶段规避加载器具备高级混淆技术和Rhysida勒索软件链接能力
url: https://mp.weixin.qq.com/s/KGs8pm8cJe1kD_jJcnUPyw
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:23:57.983612
---

# OysterLoader多阶段规避加载器具备高级混淆技术和Rhysida勒索软件链接能力

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zdwoicOrrJb0c47QAdlOHCRYv1FGgbvZgoKAH2OFBQibz89fQ2vuAMNraj4oYtHUBck03aqkrricSJYMibcCSUT6rYOCial3BxgtqFsMBiapYqEZU/0?wx_fmt=jpeg)

# OysterLoader多阶段规避加载器具备高级混淆技术和Rhysida勒索软件链接能力

原创

ZM
ZM

暗镜

![]()

在小说阅读器中沉浸阅读

一种名为 OysterLoader 的复杂恶意软件加载器已成为网络安全领域的重大威胁，它采用多层混淆技术来逃避检测并传递危险的有效载荷。

该 C++ 恶意软件于 2024 年 6 月由 Rapid7 首次发现，主要通过伪装成合法软件应用程序（如 PuTTY、WinSCP、Google Authenticator 和各种AI 工具）的虚假网站进行传播。

该恶意软件伪装成 Microsoft Installer (MSI) 文件，通常带有数字签名以使其看起来合法，因此对毫无戒心的用户具有特别强的欺骗性。

OysterLoader 通过复杂的四阶段感染链运行，从 TextShell 打包器开始，通过自定义 shellcode 执行，最终传递核心恶意有效载荷。

该加载器主要与Rhysida 勒索软件活动有关，但安全研究人员也观察到它分发了 Vidar 等通用恶意软件，Vidar 是截至 2026 年 1 月传播最广的信息窃取程序之一。

与 Rhysida 勒索软件组织（该组织与 WIZARD SPIDER 威胁行为体密切相关）的联系，凸显了这一威胁的严重性。

Sekoia 分析师发现，OysterLoader维护着一个两层的命令与控制基础设施，交付服务器处理初始连接，最终的 C2 服务器管理受害者交互。

该恶意软件展现出高级反分析能力，包括 API 攻击、通过自定义哈希算法动态解析 API 以及基于时间的沙箱检测。

其开发者不断改进恶意软件的代码，更新通信协议和混淆技术，以保持其对抗安全解决方案的有效性。

感染过程展现了 OysterLoader 在隐藏和部署其恶意组件方面的高超技术水平。

在初步环境检查确认受感染系统至少有 60 个正在运行的进程后，恶意软件会通过 HTTPS 与命令和控制服务器建立通信。

在此阶段，它利用隐写术将下一阶段的有效载荷隐藏在图标图像文件中，将恶意代码伪装成合法的视觉内容

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zdwoicOrrJb2MmttdTdovK1y0jdOFpKGib0gB2rHibXbUjQuAK57tHk6DZabSibXnnv0rich7zSOxuGj4N23JJzCTcLqMHib9hHhB46RmVlhce4ib8/640?wx_fmt=png&from=appmsg)

该恶意软件使用 RC4 加密，并采用硬编码密钥来保护这些图像文件中嵌入的有效载荷。

该有效载荷隐藏在标记为“endico”的特定标记模式之后，使得使用传统安全工具进行检测变得极其困难。

解密后，有效载荷会以 DLL 文件的形式写入用户的 AppData 目录，并通过每 13 分钟运行一次的计划任务执行，从而确保对受感染系统的持续访问。

该恶意软件使用自定义 JSON 编码进行通信，采用非标准的 Base64 字母表和随机偏移值，这使得监控受感染环境的安全团队对网络流量进行分析变得尤为困难。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

暗镜

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

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