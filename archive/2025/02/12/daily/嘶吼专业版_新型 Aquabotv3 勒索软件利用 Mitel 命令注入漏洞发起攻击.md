---
title: 新型 Aquabotv3 勒索软件利用 Mitel 命令注入漏洞发起攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247581088&idx=1&sn=6f659e38152e18f130196a1c00b075df&chksm=e9146d9ade63e48ca17d4b701dad4ace777dd6c60ca7e49f2b1d7ed66e41688ff1922c4e54dd&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-02-12
fetch_date: 2025-10-06T20:37:33.883090
---

# 新型 Aquabotv3 勒索软件利用 Mitel 命令注入漏洞发起攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ic3qYSfXT9kiaC5mK6vSdwT1BuvMkNqysJBLV5WW8wk9RetDLKVDDhicXcNKq5FQTtKh9feBmvgibCibg/0?wx_fmt=jpeg)

# 新型 Aquabotv3 勒索软件利用 Mitel 命令注入漏洞发起攻击

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

一种基于“Mirai”的僵尸网络恶意软件“Aquabot”的新变种已被发现正在积极利用 Mitel SIP 电话中的命令注入漏洞 CVE-2024-41710。

这项活动是由Akamai的安全情报和响应小组（SIRT）发现的，报告说这是属于其雷达的Aquabot的第三种变体。恶意软件系列是在2023年引入的，第二版增加了持久机制。第三个变体“ aquabotv3”引入了一个系统，该系统检测终止信号并将信息发送到命令和控制服务器（C2）服务器。

AquaboTV3报告阻断尝试的机制对于僵尸网络来说不同寻常，并且可能已添加以使其运营商更好地进行监控。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic3qYSfXT9kiaC5mK6vSdwT1V0w4rFPZJwxPwryNpIOqibdfu0d2SxApXYO63HYKwYTGQrvkTgKJY0Q/640?wx_fmt=png&from=appmsg)

报告过程阻断C2的尝试

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic3qYSfXT9kiaC5mK6vSdwT11JloTeygPKRNhiay1EZZUjuqiaY16tGbicNibYKMW8b4gVuBQ0FB97fqfA/640?wx_fmt=png&from=appmsg)针对Mitel手机

CVE-2024-41710是影响Mitel 6800系列，6900系列和6900W系列SIP电话的指挥注射漏洞，通常用于公司办公室，企业，政府机构，医院，医院，教育机构，教育机构，酒店和金融机构。

这是一个中等严重的漏洞，它允许具有管理员特权的身份验证的攻击者，由于启动过程中的参数消毒不足而进行参数注射攻击，从而导致任意命令执行。

Mitel于2024年7月17日发布了有关此漏洞的修复程序和安全咨询，敦促用户进行升级。两周后，安全研究员Kyle Burns在Github上发表了概念验证（POC）。

AquaboTV3在攻击中使用该POC利用CVE-2024-41710，是利用此漏洞的第一个记录案例。研究人员解释说：“ Akamai Sirt在2025年1月初，通过全球蜜罐网络使用有效载荷几乎与POC相同，检测到针对这种脆弱性的利用尝试。”

攻击需要身份验证的事实表明，恶意软件僵尸网络使用蛮力来获得初始访问。

攻击者制作的HTTP POST请求针对脆弱的端点8021xSupport.html，负责Mitel SIP电话中的802.1X身份验证设置。该应用程序不当处理用户输入，允许将畸形的数据插入手机的本地配置（/nvdata/etc/local.cfg）。

通过注入线路结束字符（％dt→％0D），攻击者可以操纵设备启动过程中如何解析配置文件以从其服务器中执行远程壳脚本（BIN.SH）。

该脚本下载并安装了定义的体系结构（X86，ARM，MIPS等）的Aquabot有效载荷，使用“ CHMOD 777”设置其执行权限，然后清理任何痕迹。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic3qYSfXT9kiaC5mK6vSdwT11JloTeygPKRNhiay1EZZUjuqiaY16tGbicNibYKMW8b4gVuBQ0FB97fqfA/640?wx_fmt=png&from=appmsg)Aquabotv3活性

一旦确保了持久性，Aquabotv3将通过TCP连接到其C2，以接收说明、攻击命令，更新或其他有效负载。

接下来，它尝试使用MITEL Exploit，CVE-2018-17532（TP-Link），CVE-2023-26801（IOT固件RCE），CVE-2022-31137（Web App RCE），Linksys E E linksys e，尝试使用MITEL Exploit（TP-Link），CVE-2018-17532（TP-Link）（TP-Link）（TP-Link）（TP-Link）（TP-Link），Linksys E - 系列RCE，Hadoop纱和CVE-2018-10562 / CVE-2018-10561（Dasan Router Router Bugs）。该恶意软件还试图违反强制默认或弱SSH/TELNET凭据，以扩展到同一网络上固定较差的设备。

AquaboTV3的目标是将设备纳入其分配拒绝服务（DDOS）群，并使用它们执行TCP SYN，TCP ACK，UDP，GRE IP和应用程序层攻击。

Akamai在其报告底部列出了与 Aquabotv3 相关的入侵指标（IoC），以及用于检测该恶意软件的 Snort 和 YARA 规则。

参考及来源：https://www.bleepingcomputer.com/news/security/new-aquabotv3-botnet-malware-targets-mitel-command-injection-flaw/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ic3qYSfXT9kiaC5mK6vSdwT1oHXTnUP75zDCu1KKExTreyylnbm1gwtLSqPj77kkiaJswNHKVOUDo1A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icEjy5ZrpCcgr4BicXicPv08DSsrgibDcJQpvwkZoO4OqdIpJNhj6TO5xV0ic0AnVf7f2kcPnNevQlTtQ/640?wx_fmt=png)

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