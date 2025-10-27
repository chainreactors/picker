---
title: 黑客利用 3CX 木马版桌面 app 发动供应链攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516096&idx=2&sn=e116004fbe089b4c4c2973cc6475b5ba&chksm=ea948eaadde307bcf9b88592627fc5ebcd68cade9ac4ccba9b66e8c0c2f74b16c35ef652bf36&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-31
fetch_date: 2025-10-04T11:15:27.830813
---

# 黑客利用 3CX 木马版桌面 app 发动供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQic1chVVVoYoMiatrqFxJo7ibEcj3zR2DBjMz7wDicw3X4Ouic8Ad8Vzr4MHNSdANzJiaL80yicqU2ALhNg/0?wx_fmt=jpeg)

# 黑客利用 3CX 木马版桌面 app 发动供应链攻击

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQic1chVVVoYoMiatrqFxJo7ibXqBhdw2GVBJzfJov21nNwdTICSnaT2B8a0Jley7gByJAXg7ZypPeqQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQic1chVVVoYoMiatrqFxJo7ibRxuOIwscjgDA8rFZCIwVNoAbV3rqdRYbjqMLzkHicEudB8OeMTFMPbA/640?wx_fmt=gif)

**Sophos 和 CrowdStrike 公司的安全研究员发布报告称，攻击者正在利用 3CX 公司的已签名的木马版 VOIP 桌面客户端，针对该 app 的客户发动供应链攻击。**

3CX 是一家 VoIP IPBX 软件开发公司，其 3CX Phone System 用于全球60多万家企业，日均用户超过1200万名。该公司的客户包括很多著名企业和组织机构如美国运通、可口可乐、麦当劳、宝马、本田、AirFrance、NHS、丰田、奔驰、宜家和假日酒店等。

研究人员提到，攻击者正在攻击受陷的 3CX 软件电话 app 的 Windows 和 macOS 用户。CrowdStrike 公司的威胁情报团队指出，“恶意活动包括发送到受攻击者控制的基础设施、部署第二阶段payload以及在某些有限的情况下的键入活动等。” Sophos 公司在安全公告中指出，“目前为止最常见的利用后活动是传播交互式命令 shell。”

虽然 CrowdStrike 公司认为受朝鲜政府支持的黑客组织 Labyrinth Collima 是幕后黑手，但 Sophos 公司的研究员表示“无法十分肯定地验证归属”。Labyrinth Collima 即卡巴斯基所称的 Lazarus Group、Dragos 公司所称的 Covellite、Mandiant 公司所称的 UNC4034、微软公司所称的 Zinc 和 Secureworks 公司所称的 Nickel Academy。

CrowdStrike 公司表示，“CrowdStrike 在命名攻击者的传统方面具有一个深入的分析流程。LABYRINTH CHOLLIMA 是 Lazarus Group 的一部分，后者包括其它朝鲜黑客组织如 SILENT CHOLLIMA 和 STARDUST CHOLLIMA。”

**0****1**

**SmoothOperator 软件供应链攻击**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQic1chVVVoYoMiatrqFxJo7ibXqBhdw2GVBJzfJov21nNwdTICSnaT2B8a0Jley7gByJAXg7ZypPeqQ/640?wx_fmt=gif)

SentinelOne 公司还在上周四发布的一份报告中指出，木马化的 3CX 桌面应用下载的托管在 GitHub 上的图标文件中包括附加在这些镜像的 Base64 编码字符串。

这起软件供应链攻击幕后的攻击者被称为 “SmoothOperator”，在2022年12月7日首次将其中一份图标文件上传到其仓库。该 app 使用这些 Base64 字符串将最终 payload 下载到受陷设备，它是一款此前未知的信息窃取恶意软件。该恶意软件能够从 Chrome、Edge、Brave 和 Firefox 用户配置中窃取系统信息并盗取数据和所存储的凭据。

SentinelOne 公司表示，“此时，我们无法确认 Mac 安装程序也被木马化。我们正在调查的其它应用如Chrome扩展也可被用于发动攻击。威胁行动者从2022年2月开始已注册大量基础设施，但我们尚未看到与现有威胁组织存在明显关联。”

**0****2**

**被安全软件标记为恶意性质**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQic1chVVVoYoMiatrqFxJo7ibXqBhdw2GVBJzfJov21nNwdTICSnaT2B8a0Jley7gByJAXg7ZypPeqQ/640?wx_fmt=gif)

CrowdStrike 公司指出，3CX 公司的桌面客户端将连接到如下受攻击者控制的域名：

|  |  |
| --- | --- |
| akamaicontainer[.]com | msedgepackageinfo[.]com |
| akamaitechcloudservices[.]com | msstorageazure[.]com |
| azuredeploystore[.]com | msstorageboxes[.]com |
| azureonlinecloud[.]com | officeaddons[.]com |
| azureonlinestorage[.]com | officestoragebox[.]com |
| dunamistrd[.]com | pbxcloudeservices[.]com |
| glcloudservice[.]com | pbxphonenetwork[.]com |
| qwepoi123098[.]com | zacharryblogs[.]com |
| sbmsa[.]wiki | pbxsources[.]com |
| sourceslabs[.]com | journalide[.]org |
| visualstudiofactory[.]com |  |

客户提到的桌面客户端尝试连接的一些域名包括azureonlinestorage[.]com、msstorageboxes[.]com 和 msstorageazure[.]com。BleepingComputer 测试了该软件的木马版本但无法触发和这些域名的任何连接。然而，3CX 论坛上有多名客户表示他们在一周前即3月22日收到告警称，该 VoIP 客户端 app 被 SentinelOne、CrowdStrike、ESET、Palo Alto Networks 和 SonicWall 安全软件被标记为恶意性质。

客户报告称，这些安全告警是在Mac上安装 3CXDesktopApp 18.12.407和18.12.416 Windows 版本或 18.11.1213和最新版本后触发的。CrowdStrike 共享的其中一个木马化3CX 软件电话客户端样本在三周前即3月3日被数字签名，3CX Ltd 证书由 DigiCert 办法。BleepingComputer 证实称该证书用于该软件的老旧版本中。

虽然 SentinelOne 在分析 3CXDesktopApp.exe 二进制时检测到“渗透架构或 shellcode”且ESET 将其标记为 “Win64/Agent.CFM”木马，但由CrowdStrike 公司的 Falcon OverWatch 管理的威胁搜索服务紧急提醒用户调查自己的系统中是否存在恶意活动。

尽管 3CX 公司的支持团队员工在周三的一条写满用户报告的论坛帖子下将其标记为潜在的 SentinelOne 误报，但该公司尚未公开证实这些问题。

3CX公司尚未就此事置评。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[供应链安全这件事，早就被朱元璋玩明白了](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515824&idx=1&sn=dab68a0c49b4d79f50b5c765c3bc2d89&chksm=ea948fdadde306cc2de185ca934b6c63d6e2e02e141f4612180b48e2c4ef56ec4da8bb826dd1&scene=21#wechat_redirect)

[美国发布新的国家网络安全战略：软件安全责任转移，重视软件供应链安全](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515818&idx=1&sn=b5311898cb66921b319dbcd3daaaca1f&chksm=ea948fc0dde306d6047987b8223144cc81342c436e80e04c4a2d0b01b5b9c6248f3bc47053a7&scene=21#wechat_redirect)

[奇安信总裁吴云坤：构建四大关键能力 体系化治理软件供应链安全](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515606&idx=1&sn=be020e0c8715a3f3b2c31a379ca01e0d&chksm=ea948cbcdde305aab8950259a837c775cd6fb12d0db8801e92776fcae41529ce655f3a18ff6c&scene=21#wechat_redirect)

[深度分析：美国多角色参与的软件供应链安全保护措施](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515534&idx=1&sn=32d0d289fcc99c859325f35101773d65&chksm=ea948ce4dde305f2309ea1b9ca9e601ef74b05fdc0b35935a43334c65bb8bc47ca179b818fa9&scene=21#wechat_redirect)

[美国CISA将设立供应链风险管理办公室](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515460&idx=3&sn=e88c34df75275d13d1331d4c0714279e&chksm=ea948c2edde305385fc20864a696ea25c625a2e5604742d8d4cd5026ba6afa9d2223e94cf431&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/hackers-compromise-3cx-desktop-app-in-a-supply-chain-attack/

题图：Pixabay License

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