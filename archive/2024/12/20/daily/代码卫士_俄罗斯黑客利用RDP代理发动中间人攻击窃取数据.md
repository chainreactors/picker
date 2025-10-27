---
title: 俄罗斯黑客利用RDP代理发动中间人攻击窃取数据
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521847&idx=1&sn=3574f2fa73eb1444a958326d5c4956db&chksm=ea94a75ddde32e4b88d79174fac0270694aec30a8cb2ce5a0e407271173167da4c5fd1aee1a7&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-20
fetch_date: 2025-10-06T19:38:49.245951
---

# 俄罗斯黑客利用RDP代理发动中间人攻击窃取数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQjsiaomcGsge5ZoRG0sBQzSKyTD0XbClumffCdHQI0cf7bSIRqK1oaGwwggah23c8cHomuwc16h8w/0?wx_fmt=jpeg)

# 俄罗斯黑客利用RDP代理发动中间人攻击窃取数据

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**俄罗斯黑客组织APT29（即“Midnight Blizzard”）正在通过193台桌面协议代理服务器发动中间人攻击，窃取数据和凭据，安装恶意 payload。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQjsiaomcGsge5ZoRG0sBQzSdhkx7ewZ9d9ib6mkt3O5tWcR4uyNiaeuCicRnq5w6paWgWv2sJlGXZdKQ/640?wx_fmt=gif&from=appmsg)

这些中间人攻击利用红队代理工具PyRDP扫描受害者的文件系统，在后台窃取数据并在受陷环境中远程执行恶意应用。趋势科技将这些威胁行动者称为 “地球科西切 (Earth Koshchei)”，并表示攻击者针对的是政府和军事组织机构、外交实体、IT和云服务提供商以及电信和网络安全企业。

从因这起攻击而注册的域名可看出，APT29攻击的实体主要位于美国、法国、澳大利亚、乌克兰、葡萄牙、德国、以色列、法国、希腊、土耳其和荷兰。

**利用 PyRDP 执行中间人攻击**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQjsiaomcGsge5ZoRG0sBQzSMlaV2Lg6cScQxcPNWED2sib1jVjIoibos0LODOwBth2L9v3KdfNEKZ4Q/640?wx_fmt=gif&from=appmsg)

RDP 是由微软开发的专有协议，供用户通过网络远程访问和控制另外一台电脑，常用于远程管理、技术支持以及连接企业环境中的系统。

2024年10月，亚马逊和乌克兰CERT联合发布报告证实称，APT29诱骗受害者运行了含有钓鱼邮件附件的文件后，连接到恶意RDP服务器。一旦设立连接，本地资源如磁盘、网络、打印机、剪贴板、音频设备和COM端口就会与受攻击者控制的RDP服务器共享，使攻击者获得对敏感信息的无条件访问权限。

趋势科技公司发现193个RDP代理服务器将连接重定向到受攻击者控制的34个后端服务器，攻击者借此监控和拦截RDP会话。黑客利用Python 中间人红队工具 PyRDP来拦截受害者与远程会话之间的通信，使连接看似是合法的。攻击者还可使用PyRDP记录明文凭据或NTLM哈希，窃取剪贴板数据、窃取传输的文件、从位于后台的共享驱动窃取数据，并在新连接上运行控制台或 PowerShell 命令。

研究人员指出，该攻击技术由Mike Felch 在2022年率先提出，它可能启发了 APT29 组织的技术利用。趋势科技公司解释称，“在建立连接后，恶意服务器模拟合法RDP服务器的行为并利用该会话执行多种恶意活动。主要的攻击向量涉及攻击者部署恶意脚本或修改受害者机器上的系统设置。此外，PyRDP 代理有助于访问受害者的文件系统，从而使攻击者浏览目录、读取或修改文件并注入恶意payload。”在所分析的恶意配置中，还存在一个为用户提供误导的AWS安全存储连接稳定性测试连接请求的配置。

APT29组织的通过商用VPN产品接受加密付款、TOR退出节点和住宅代理服务来混淆恶意RDP服务器的IP地址。

要防御恶意RDP配置，需要对恶意邮件做出良好的响应，在本案例中，恶意邮件是在攻击发动前，就从受陷的合法地址发出的。更重要的是，Windows 用户应仅允许RDP连接到已知且受信任的服务器并永远不要使用通过邮件附件发送的RDP连接。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[研究员披露修复两次的 Windows RDP 漏洞详情](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512438&idx=2&sn=dc6db27797628706ae9f2892365b1f0b&scene=21#wechat_redirect)

[微软反向 RDP 漏洞补丁不当，第三方 RDP 客户端易受攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247493064&idx=1&sn=519c74d06bd95d3f76b3eb2693449215&scene=21#wechat_redirect)

[首例大规模利用 BlueKeep RDP 漏洞的攻击现身但并非蠕虫](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247491488&idx=3&sn=89b7c0b4eca93ff1d9b21e48f85a7744&scene=21#wechat_redirect)

[黑客暴力攻击企业RDP服务器传播勒索软件](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485766&idx=1&sn=c94279acbf39fa668f037b475ad2a35e&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/russian-hackers-use-rdp-proxies-to-steal-data-in-mitm-attacks/

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