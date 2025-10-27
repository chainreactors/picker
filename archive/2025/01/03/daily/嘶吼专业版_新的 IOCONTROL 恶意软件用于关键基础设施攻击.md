---
title: 新的 IOCONTROL 恶意软件用于关键基础设施攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247580564&idx=1&sn=b8689abfa62f761f32105a853f2ec51d&chksm=e9146baede63e2b88b317a2de4783a98c0a06ea2398735a8d049bf8ebc2ed09d5c80efb5ea6d&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-01-03
fetch_date: 2025-10-06T20:10:09.241424
---

# 新的 IOCONTROL 恶意软件用于关键基础设施攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibTg7aqlUfbnBVR55Y6LrWXFmuib8UvR0l4oNgRFgVALo5lrHYTpniaS0wgfFWCMgib0GR4hJ32nLyDw/0?wx_fmt=jpeg)

# 新的 IOCONTROL 恶意软件用于关键基础设施攻击

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

伊朗恶意分子正在利用名为 IOCONTROL 的新恶意软件来破坏以色列和美国关键基础设施使用的物联网 (IoT) 设备和 OT/SCADA 系统。

目标设备包括路由器、可编程逻辑控制器 (PLC)、人机界面 (HMI)、IP 摄像头、防火墙和燃料管理系统。该恶意软件的模块化特性使其能够危害不同制造商的各种设备，包括 D-Link、Hikvision、Baicells、Red Lion、Orpak、Phoenix Contact、Teltonika 和 Unitronics。

Claroty 的 Team82 研究人员发现了 IOCONTROL 并对其进行了采样进行分析，他们报告说，这是一种民族国家网络武器，可以对关键基础设施造成严重破坏。

鉴于持续的地缘政治冲突，IOCONTROL 目前用于针对以色列和美国的系统，例如 Orpak 和 Gasboy 燃料管理系统。据报道，该工具与一个名为 CyberAv3ngers 的伊朗黑客组织有关，该组织过去曾对攻击工业系统表现出兴趣。

OpenAI 最近还报告称，该威胁组织使用 ChatGPT 来破解 PLC、开发自定义 bash 和 Python 漏洞利用脚本，并计划入侵。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTg7aqlUfbnBVR55Y6LrWXtP832G2icuiave0JooGOU1wDyiabkbicuznM5a2hSSeUGSOZ4r88Hmzh9Q/640?wx_fmt=png&from=appmsg)IOCONTROL 攻击

Claroty 从 Gasboy 燃油控制系统中提取了恶意软件样本，特别是该设备的支付终端 (OrPT)，但研究人员并不确切知道黑客是如何用 IOCONTROL 感染它的。

在这些设备内部，IOCONTROL 可以控制泵、支付终端和其他外围系统，从而可能导致中断或数据被盗。

威胁者在 Telegram 上声称破坏了以色列和美国的 200 个加油站，这与 Claroty 的调查结果一致。这些攻击发生在 2023 年末，大约与水处理设施中的 Unitronics Vision PLC/HMI 设备遭到破坏的时间相同，但研究人员报告称，新的攻击活动于 2024 年中期出现。截至 2024 年 12 月 10 日，66 个 VirusTotal 防病毒引擎均未检测到 UPX 打包的恶意软件二进制文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTg7aqlUfbnBVR55Y6LrWXBI3RPI7SLEuAFvtakwJMh1xEIXSKLb0RMibmY00xPWZuCsKs1rjYoWA/640?wx_fmt=png&from=appmsg)

Gasboy 燃油控制系统是从中提取恶意软件的地方

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTg7aqlUfbnBVR55Y6LrWXtP832G2icuiave0JooGOU1wDyiabkbicuznM5a2hSSeUGSOZ4r88Hmzh9Q/640?wx_fmt=png&from=appmsg)恶意软件功能

该恶意软件以“iocontrol”名称存储在“/usr/bin/”目录中，使用模块化配置来适应不同的供应商和设备类型，针对广泛的系统架构。它使用持久性脚本（“S93InitSystemd.sh”）在系统启动时执行恶意软件进程（“iocontrol”），因此重新启动设备不会将其停用。

它通过端口 8883 使用 MQTT 协议与其命令和控制 (C2) 服务器进行通信，这是物联网设备的标准通道和协议。唯一的设备 ID 嵌入到 MQTT 凭证中，以实现更好的控制。

DNS over HTTPS (DoH) 用于解析 C2 域，同时规避网络流量监控工具，并且恶意软件的配置使用 AES-256-CBC 进行加密。

IOCONTROL 支持的命令如下：

**·发送“hello”**：向C2报告详细的系统信息（例如主机名、当前用户、设备型号）。

**·检查执行**：确认恶意软件二进制文件已正确安装且可执行。

**·执行命令**：通过系统调用运行任意操作系统命令并报告输出。

**·自删除**：删除自己的二进制文件、脚本和日志以逃避检测。

**·端口扫描**：扫描指定的 IP 范围和端口以识别其他潜在目标。

上述命令是使用从“libc”库动态检索的系统调用执行的，并将输出写入临时文件以进行报告。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTg7aqlUfbnBVR55Y6LrWXQIaM7zm7cX9rbdlUsGob7M7gHvvZjGibOC1L2ianoLStcGgTlDHt2E9w/640?wx_fmt=png&from=appmsg)

简化的攻击流程

鉴于 IOCONTROL 目标在关键基础设施中的作用以及该组织的持续活动，Claroty 的报告为防御者提供了宝贵的资源，可以帮助他们识别和阻止威胁。

参考及来源：https://www.bleepingcomputer.com/news/security/new-iocontrol-malware-used-in-critical-infrastructure-attacks/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTg7aqlUfbnBVR55Y6LrWXyibUTD3zYw8mnibicOIlg4ZzRIm7Uw6iaf94bs6Wq1AofcBmOOCwFDyicYw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTg7aqlUfbnBVR55Y6LrWXwWwialLA1a2S6BS0owdIRd0lzQGIMWwGLxJmuqEhL0Br9LI8YZRpSEA/640?wx_fmt=png&from=appmsg)

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