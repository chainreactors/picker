---
title: 国家级黑客利用Palo Alto零日漏洞长期潜伏，部署隧道工具窃取凭证
url: https://mp.weixin.qq.com/s/6QG7eFavFLSKz6q70u_bgw
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:33:17.435688
---

# 国家级黑客利用Palo Alto零日漏洞长期潜伏，部署隧道工具窃取凭证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Hxdb7gjfn9mRsicXuGD0XvnlRF9EzicNxwI5RSAF4g15R4lZSQZ9BsvaKrCLdFQ4GfOxd8eibrpdEzd7gmicBHicw9aibQsKyA1tia41RWiark9GAxg/0?wx_fmt=jpeg)

# 国家级黑客利用Palo Alto零日漏洞长期潜伏，部署隧道工具窃取凭证

e安在线
e安在线

e安在线

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Hxdb7gjfn9l4rkrpMicicUPCgNewbP7zrHl5TZPnBwBPJWsfSmF594jsxIGiaFXGvuxaFu3UPFubbyrMELgaSOdoyafgicI6jrS1HlN9JyctZIY/640?wx_fmt=jpeg&from=appmsg)

Palo Alto Networks警告称，疑似国家支持的黑客组织持续数周利用PAN-OS关键0Day漏洞（CVE-2026-0300）。攻击者利用该漏洞部署了EarthWorm和ReverseSocks5等隧道工具，使用窃取的凭证探测Active Directory，并通过删除日志和其他证据来掩盖入侵痕迹。

网络安全厂商在公告中指出：“目前我们仅观察到CVE-2026-0300被有限利用。Unit 42正在追踪CL-STA-1132攻击集群，该集群疑似由国家支持，专门利用CVE-2026-0300。攻击者通过该漏洞实现了PAN-OS软件中的未认证远程代码执行（RCE），成功利用后能够将shellcode注入nginx工作进程。后续攻击活动包括：部署公开可用的隧道工具（EarthWorm、ReverseSocks5）、使用可能从防火墙获取的凭证枚举Active Directory，以及系统性清除日志和其他入侵证据。”

![](https://mmbiz.qpic.cn/mmbiz_jpg/Hxdb7gjfn9ntovI91QE7kIsFcRvf52yndEsGuoWLLiam3zlwbNE8aCECz2BE3IkIAiaR24RPGDPoXnT46snnibJHXicGs0icYdsxCOPGia43wWUaM/640?wx_fmt=jpeg&from=appmsg)

**技术分析与影响范围**

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9lKGLPty7xbiakfu7TXBvjKnniavlDQwqHnSNGEbibffAmHx9EGTwiaxegmhX6CmicjOKwmIicQXcTiccbWAjQR1ZMqZlyF3o7Lq9iaStY/640?wx_fmt=png&from=appmsg)

该漏洞是User-ID身份验证门户服务中的缓冲区溢出漏洞。当该门户暴露于互联网时，未认证攻击者可通过特制数据包，在PA系列和VM系列防火墙上以root权限执行任意代码。Palo Alto Networks强调，若按照最佳实践指南将User-ID身份验证门户的访问限制在可信内部IP地址范围内，可大幅降低风险。

受影响产品版本如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9lITYhwGE702MaEfTTMxOH0TOkiadgzcvJAedTpgpkNuXOeZ59vuJFicdWRMvo0MScGPQmibibK0rcsqEoeDLbsAkkm2pXibEPTG010/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9m6bGABSMSNiasicCg3BibUypm3Y9xhXI06VpfbG9n7uL1oWjAicIA5a4QmrURe5F3IxoibpeuZbYLBOmyyFvsLtgmxadTQxpsKoPOo/640?wx_fmt=png&from=appmsg)

**技术分析与影响范围**

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9kNnnSJjLK8VXkiaLUQoejS1rM0u6pibRNzGIuQWUicUkibfwrxPlR53COPYtmYHFScW4wlEbNHdPQntj8MNMwRtmQ6ib4PVW3JYqm4/640?wx_fmt=png&from=appmsg)

EarthWorm是一款用C语言编写的开源隧道工具，支持Windows、Linux、macOS和ARM/MIPS平台。该工具可作为SOCKS5代理和端口转发实用程序，使攻击者能够创建隐蔽通信通道、绕过网络限制并在受感染环境中横向移动。其功能包括正向和反向SOCKS5隧道、端口桥接、流量转发以及RDP和SSH等多协议跳转。该工具此前与Volt Typhoon和APT41等威胁组织有关联。

ReverseSocks5是另一款开源网络工具，通过从受感染系统向攻击者控制的服务器建立出站连接，绕过防火墙和NAT保护。连接后，它会建立SOCKS5代理隧道，允许远程访问内部网络。虽然管理员常将其用于合法的远程管理，但威胁行为者也滥用该工具进行隐蔽渗透和入侵后操作。

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9nUgyoHRG1RpH6rHwyqFOZlnVaDrjC9ib9RBX1STqWaFoMaKC5YS134y9vg77lO7bIxNiaiaw2JJd97kesduDcNJYEjxvWKEbyHcI/640?wx_fmt=png&from=appmsg)

**攻击特征与防御建议**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9nibhkziakbQXaZG8icM6gbs0tJbHPc0AGuQqQogl0FllurHtNrdQ3LdvjNJBvhTGiagtfAeKGic609zRnLAseBclYfY8BD6Q36oTLE/640?wx_fmt=png&from=appmsg)

Palo Alto Networks分析指出：“CL-STA-1132背后的攻击者依赖开源工具而非专有恶意软件，最大程度减少了基于签名的检测，实现了与环境的无缝集成。这种技术选择，加上数周内间歇性交互会话的严格操作节奏，使其行为始终低于大多数自动化警报系统的阈值。横向移动技术优先滥用身份信任而非传统的网络层渗透，有效减少了攻击痕迹。因此，此次攻击活动表明，操作克制——特别是使用非持续性访问窗口——是在边缘基础设施上保持长期驻留的主要因素。”

该漏洞目前仍未修复，预计从2026年5月13日开始发布补丁。主要影响使用User-ID身份验证门户的PA系列和VM系列防火墙。Palo Alto Networks强调，遵循最佳实践（如仅限可信内部网络访问）的企业面临的风险要低得多。

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9mCHMXib4Xv7VlYSjE8W1oIuLa3KWdq8cRgzLV4fCYS7FWmNulA63XBYiavciaGTTKT0YHZYfxwUXibO5OL02ut9Vh4kxh0Dy3x9J8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9lw3AqqJK47wcgicF9z0tYxr4YvP9G0wuA8e9ZklheShZN6bexch8FWDdnR5z1E0dUicibib9g7Ahmicnq79o0a9pUjH4Aib9xL7AAsI/640?wx_fmt=png&from=appmsg)

声明：除发布的文章无法追溯到作者并获得授权外，我们均会注明作者和文章来源。如涉及版权问题请及时联系我们，我们会在第一时间删改，谢谢！文章来源：FreeBuf

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9mw2JBzBzxBHJhoGJnlsOxljk8rg1mjU7f3bgial0oXNsl928zKdUicDoO8D4NkOEOTwIC16Ekibmbu3dGs16MVYEs7ZtMzxLofWY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Hxdb7gjfn9k4G2XrOWLsxqoYRBVSaFEV98AuugYdmCVxAuQFD2z1MmkSok5KaBMicpJ16qrUlEqkqnLdDdB6ciah5OyHsTgsC0tsna74GnZG8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Hxdb7gjfn9kufhJxl5uYGkFTQAJLuorlwMkbJuzhhJL6HiaZZIL4gJHVEV3Lwa3RDC7ZM8DqWFIo80f4l5U8A3E6d99iarI35FwxRpMBg8C9I/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1Y08O57sHWiaro9eC87veL2BfoUwAjnOfbTbGQwSaaunoz9m7KFdFkib1pMyMoNY4tVtskNSHickKmn7Nza8WGTeA/0?wx_fmt=png)

e安在线

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1Y08O57sHWiaro9eC87veL2BfoUwAjnOfbTbGQwSaaunoz9m7KFdFkib1pMyMoNY4tVtskNSHickKmn7Nza8WGTeA/0?wx_fmt=png)

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