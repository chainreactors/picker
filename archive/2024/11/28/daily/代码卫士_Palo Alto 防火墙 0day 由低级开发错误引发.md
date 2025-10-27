---
title: Palo Alto 防火墙 0day 由低级开发错误引发
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521617&idx=2&sn=0e9ac32a3223e727cd6cd99460e0387e&chksm=ea94a43bdde32d2d156961ca2f3e3020fe479986f24f7b566a4252db8e0cf759e9e2b35cea13&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-28
fetch_date: 2025-10-06T19:20:23.711379
---

# Palo Alto 防火墙 0day 由低级开发错误引发

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRpkFZpBQfl02AnNia2QQCFc9Caj36cZrMrULuEMG8bzEpfsVDQDjJbrA9JNtLW8t2k3kt49ID6TmA/0?wx_fmt=jpeg)

# Palo Alto 防火墙 0day 由低级开发错误引发

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**作者：Lucian Constantin**

**编译：代码卫士**

**攻击者正在利用两个在野漏洞，经由 PAN-OS 管理 web 界面绕过认证并提权，以获得 Palo Alto Networks 防火墙上的root权限。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRpkFZpBQfl02AnNia2QQCFc0hROv47rYJoQw4kmwRjCO1CBKCvLaPSpUGRYsY5D87odXzqIibOn0tw/640?wx_fmt=png&from=appmsg)

Palo Alto Networks 公司已修复这两个影响防护墙和虚拟安全设备的已遭活跃利用漏洞。组合利用这两个漏洞可使攻击者以底层PAN-OS操作系统扇的最高权限执行恶意代码，完全接管设备。

[Palo Alto 公司在本月早些时候曾发布公告](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521440&idx=1&sn=3bf8ff26ce74c0c7fbfeb2701a773a5f&scene=21#wechat_redirect)，提醒客户称正在调查关于可能位于 PAN-OS web 管理界面中的 RCE 漏洞，并建议客户按照建议步骤保护该界面访问权限的安全。

该公司在调查中发现这起RCE攻击并非由一个而是两个漏洞造成，这两个漏洞已被用于攻击那些管理界面暴露到互联网中的设备。

**0****1**

**认证绕过和提权**

第一个漏洞CVE-2024-0012是严重级别的漏洞，CVSS评分为9.3。攻击者可利用该漏洞绕过认证并在管理界面获得管理员权限，从而执行管理员操作并修改配置。

虽然该漏洞造成糟糕后果，但它无法直接导致系统遭完全接管，除非该功能用于在底层操作系统上执行恶意代码。

而事实上，攻击者通过第二个漏洞CVE-2024-9474实现了这一目的。该漏洞可导致任何拥有 web 界面管理员权限的人员在这个基于 Linux 上的操作系统上以root权限执行代码。

这两个漏洞均影响 PAN-OS 10.2、PAN-OS 11.0、PAN-OS 11.1和PAN-OS 11.2，目前这些版本均已收到补丁。

**0****2**

**开发过程中的低级错误导致**

安全公司 watchtower 逆向补丁后发现，这两个漏洞都是由开发过程中的基础错误导致的。

为了验证访问页面是否要求用户进行认证，PAN OS 管理界面检查请求的X-Pan-Authcheck 标头是否开启。Nginx 代理服务器负责将请求转发到托管着web 应用的 Apache 服务器，它根据该请求的路由，自动将 X-Pan-Authcheck 设为开启。在一些实例中，X-Pan-Authcheck被设置为关闭，因为该位置，如/unauth/目录，应该无需认证即可访问，但几乎除了/unauth/以外的一切都应该将标头设置为开启，这应该会将用户重定向至登录页面。

然而，研究人员发现，一个名为 “uniEnvSetup.php” 的重定向脚本预计 HTTP\_X\_PAN\_AUTHECHECK 的值被设为关闭，而如果请求中提供了这一项，则服务器将会全盘接受。

研究人员提到，“我们只是将 off（关闭）值给了 X-PAN-AUTHCHECK HTTP 请求标头，然后服务器就关闭了认证？！都这样了，为什么还会有人感到惊讶呢？”

第二个漏洞的成因也很简单，它是一个命令注入缺陷，可导致命令以用户名的形式被传递给名为 “AuditLog.write()” 的函数，该函数随后将该注入的命令传递给 pexecute()。但将payload传递给该日志函数实际上是因本身就很危险的另外一个功能完成的。

该功能可使 Palo Alto Panorama 设备指定它们希望模拟的用户名及其用户角色，随后获取完全认证的PHP会话ID，而无需提供密码或通过双因素认证。

所有因素叠加起来，加上这种软件设计，攻击者就能够将一个shell payload 作为用户名字段的一部分传递，模拟特定的用户及其角色，而它随后会被传递给 AuditLog.write()，接着是 pexecute()，从而导致在底层OS上执行命令。

研究人员分析提到，“这两个漏洞进入生产设备令人惊讶，而且竟然通过隐藏在PaloAlto设备中的大量shell脚本调用被黑而进入。”

**0****3**

**缓解措施**

除了将受影响防火墙更新至新发布的版本外，管理员应当仅允许受信任的内部IP地址访问该管理界面。也可奖该管理界面隔离到一个专门的管理VLAN，或将其配置为通过首先要求进行单独认证的堡垒机访问。

将PAN-OS 管理界面暴露到互联网风险巨大，因为这并非首次也绝非最后一次在此类设备上发现RCE漏洞的情况。今年早些时候，Palo Alto Networks 公司修复了一个位于PAN-OS中的另外一个 RCE 0day漏洞（CVE-2024-3400），该漏洞遭某国家黑客组织利用。

Palo Alto Networks 威胁捕获团队正在追踪CVE-2024-0012和CVE-2024-9474的利用情况，并发布了相关妥协指标 (IoC)。该攻击活动被称为 “Operation Lunar Peak”。研究人员提到，“该活动主要来自与匿名VPN服务进行代理/隧道流量的IP地址。已观察到的利用后活动包括交互式命令执行和在防火墙上释放恶意软件如 webshell等。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Palo Alto Networks：注意潜在的 PAN-OS RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521440&idx=1&sn=3bf8ff26ce74c0c7fbfeb2701a773a5f&scene=21#wechat_redirect)

[Palo Alto 修复多个严重的防火墙漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521075&idx=1&sn=2987012f618a751eabf08e620add0615&scene=21#wechat_redirect)

[Palo Alto：注意！PAN-OS 防火墙 0day 漏洞已遭利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519289&idx=1&sn=86e226003b5da9dd0d6867f4b45fcb1a&scene=21#wechat_redirect)

[Palo Alto Networks：PAN-OS DDoS 漏洞已遭在野利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513567&idx=1&sn=181b3bb7e1b34dc9dd67bfde798f4c7d&scene=21#wechat_redirect)

[多个漏洞可使Palo Alto Networks 产品遭禁用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511385&idx=2&sn=fc66fda5f3b538000c0534ed4e79a6b7&scene=21#wechat_redirect)

**原文链接**

https://www.csoonline.com/article/3609132/palo-alto-networks-zero-day-firewall-flaws-caused-by-basic-dev-mistakes.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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