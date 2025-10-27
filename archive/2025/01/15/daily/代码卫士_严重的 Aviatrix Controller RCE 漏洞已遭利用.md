---
title: 严重的 Aviatrix Controller RCE 漏洞已遭利用
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522060&idx=2&sn=77945a6bc936ca2cbd6fe400e106a420&chksm=ea94a666dde32f702c05d9f642f0ea1c7cbc525dd3805a10ce8441a93f2412a10b40fc913587&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-01-15
fetch_date: 2025-10-06T20:10:57.336277
---

# 严重的 Aviatrix Controller RCE 漏洞已遭利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRTIPXhgnNfFDpTOjlCZibEZdIEh7v9Tk0l8zc4tcB44z6ZflhGnhGJFQEXSicibAfictbSsJHicAporibg/0?wx_fmt=jpeg)

# 严重的 Aviatrix Controller RCE 漏洞已遭利用

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**威胁行动者们正在利用Aviatrix Controller 实例中的一个严重的远程命令执行漏洞 (CVE-2024-50603)，安装后门和密币挖矿机。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRTIPXhgnNfFDpTOjlCZibEZuHvpYTpiaXnZftniaS2ibmKkG9iaBM5RU5oBMLuQxqibHS6CjkGEYlA1vkA/640?wx_fmt=gif&from=appmsg)

Aviatrix Controller 是 Aviatrix 云网络平台的一部分，用于增强多云设备中的网络、安全和运营可见性，客户包括企业、DevOps 团队、网络工程师、云架构师和管理服务提供商。

该漏洞由 Jakub Korepta 在2024年10月7日发现，是因为在某些API操作中对输入清理函数使用不当造成的，可导致攻击者将恶意命令注入系统级别的操作中。这就导致威胁行动者使用特殊构造的API请求，在无需认证的情况下实现远程命令执行。

该漏洞影响 Aviatrix Controller 7.x至7.2.4820的所有版本。建议用户升级至7.1.4191或7.2.4996，修复该漏洞。

**漏洞已遭利用**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRTIPXhgnNfFDpTOjlCZibEZP423N0swKEkfDbGB2Vicp14cffsSDFbREkdKFPpsx77HslmfnIsJ3JA/640?wx_fmt=gif&from=appmsg)

Wiz 公司报道称GitHub 已出现 PoC 利用，推动了该漏洞的在野利用。

黑客正在利用该漏洞植入 Sliver 后门并通过XMRig（密币劫持）执行越权门罗币挖掘。研究人员表示，虽然只有比例较少的云企业环境部署了 Aviatrix Controller，但多数具有横向网络移动和提权风险。研究人员表示，“从数据来看，约3%的云企业环境部署了 Aviatrix Controller。然而，数据显示，在65%的已部署环境中，托管着 Aviatrix Controller的虚拟机具有向管理员云控制板权限的横向移动路径。”

Wiz 提到，目前虽然没有证据表明执行横向移动的证据，但他们认为威胁行动者在利用 CVE-2024-50603枚举主机的云权限并探索数据提取的机会。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[GFI KerioControl 防火墙存在严重的RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522044&idx=1&sn=71bbcad32c9a0753d8385256ee5dad03&scene=21#wechat_redirect)

[联发科芯片集存在严重的RCE漏洞，影响数百万台设备](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522013&idx=1&sn=9f3081df1533336e5c1747667ca72291&scene=21#wechat_redirect)

[Apache MINA 存在严重的满分漏洞，可导致RCE](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521918&idx=1&sn=acf8324d4a36ec4e8d37b16375da9e75&scene=21#wechat_redirect)

[Apache Tomcat 漏洞导致服务器易受RCE攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521893&idx=1&sn=867f98595849107577a98fcaf043a177&scene=21#wechat_redirect)

[Apache修复 Struts 2 中的严重 RCE 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521787&idx=1&sn=aa7443d590ca0182f0cbd4386c81152a&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-aviatrix-controller-rce-flaw-in-attacks/

题图：Pexels License

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