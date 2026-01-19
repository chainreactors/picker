---
title: APT组织HoneyMyte利用Rootkit劫持亚洲多国政府网络
url: https://mp.weixin.qq.com/s/NrMGhAYwwZvEriQ_W3VVZg
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:41:23.873712
---

# APT组织HoneyMyte利用Rootkit劫持亚洲多国政府网络

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3xxicXNlTXL8K6Nv1bvc5JOMBW4iaMA48LrDZy2J9PZMUo7edEica1tOIFeVRc46knAl0xQicwjODXOywraicLzCib7g/0?wx_fmt=jpeg)

# APT组织HoneyMyte利用Rootkit劫持亚洲多国政府网络

黑白之道

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/3xxicXNlTXLicwgPqvK8QgwnCr09iaSllrsXJLMkThiaHibEntZKkJiaicEd4ibWQxyn3gtAWbyGqtHVb0qqsHFC9jW3oQ/640?wx_fmt=gif)

#

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icX0tZiaHoQpDticaCIl8xqcqDbWvicvKhRau7yAZOibh8HXbgINyQCkRuiadbHDPQqBiaoUWLePoxfJhLw/640?wx_fmt=png&from=appmsg)

团臭名昭著的APT组织HoneyMyte（又称Mustang Panda或Bronze President）近期大幅升级攻击手段，通过部署复杂的内核模式Rootkit，深度渗透东南亚和东亚多国政府网络。卡巴斯基实验室最新报告披露，该组织在2025年年中发起的攻击活动展现出危险的技术演进。

**Part01**

## ****攻击活动与技术特征****

研究人员推测此次攻击始于2025年2月，主要针对缅甸和泰国机构。攻击核心是一个名为ProjectConfiguration.sys的恶意驱动文件，攻击者使用合法但疑似被盗的数字证书进行签名以绕过安全检查。

**Part02**

## ****Rootkit工作机制****

```

```

该驱动并非被动存在，而是充当恶意软件的"保镖"。报告指出：感染设备上，该驱动文件会注册为迷你过滤驱动，最终目标是将后门木马注入系统进程，并为恶意文件、用户模式进程及注册表键提供保护。通过操纵系统驱动的加载顺序，该恶意软件能有效致盲安全软件，甚至公然篡改Microsoft Defender，包括修改关键驱动WdFilter的高度值，使其无法加载至I/O堆栈。

**Part03**

## ****载荷投递技术革新****

这套复杂机制的终极目标是部署该组织标志性后门ToneShell，但投递方式发生重大变化。卡巴斯基研究人员强调：这是首次发现ToneShell通过内核模式加载器投递，使其免受用户模式监控。新变种采用伪造TLS 1.3标头（如avocadomechanism[.]com域名）与C2服务器通信，将数据窃取伪装成正常网络流量。

![banner](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icX0tZiaHoQpDticaCIl8xqcqDJibBsdm7rQONGVVz4ibS4GZp7fDXt6Ric6iau2yCnTjhOeXpAR86ficeicg/640?wx_fmt=jpeg&from=appmsg)

**Part04**

## ****攻击者溯源与战术演进****

目标选择和工具使用明确指向ToneShell。研究人员表示：高度确信本报告所述活动与HoneyMyte组织相关。除ToneShell外，攻击还涉及PlugX和ToneDisk USB蠕虫等已知工具。该活动显然旨在维持对高价值情报目标的长期访问，HoneyMyte在2025年的行动显示出向内核模式注入器部署ToneShell的明显演进，同时提升了隐蔽性和持久性。

由于恶意软件完全在内存中执行并隐藏于内核驱动之后，传统检测方法可能失效。安全人员需注意：内存取证已成为发现和分析此类入侵的关键手段。

**参考来源：**

The Ghost in the Kernel: How HoneyMyte Weaponized a Rootkit to Hijack Asian Governments

https://securityonline.info/the-ghost-in-the-kernel-how-honeymyte-weaponized-a-rootkit-to-hijack-asian-governments/

> **文章来源：FreeBuf**

黑白之道发布、转载的文章中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途及盈利等目的，否则后果自行承担！

如侵权请私聊我们删文

**END**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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