---
title: Npm 库XMLRPC 插入恶意代码，窃取数据部署密币矿机
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521633&idx=2&sn=4a7d37dee16810a9a2e5aecefb811f16&chksm=ea94a40bdde32d1dac5f2eda6317f6000c6f7fcedea79083b127edcec1f9d186b5bb1ebdf9fc&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-30
fetch_date: 2025-10-06T19:16:12.061091
---

# Npm 库XMLRPC 插入恶意代码，窃取数据部署密币矿机

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQa4MsEI45FdIyWg7I4dPiczYtNkaeO4ormlYoHUa8QnLByBoegpiaoPgxzBaa1xPSRsmgEf4q457Ag/0?wx_fmt=jpeg)

# Npm 库XMLRPC 插入恶意代码，窃取数据部署密币矿机

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**网络安全研究人员在 npm 注册表上发现了已活跃一年多且还在活跃的软件供应链事件，涉及的库原本并非恶意库，但随后增加了恶意代码，从受感染系统上窃取数据并挖掘加密货币。**

该程序包名为 @0xengine/xmlrpc，最初在2023年10月2日作为针对 Node.js的基于 JavaScript 的 XML-RPC 服务器和客户端发布。截止目前该库的下载量已达1790次，且目前仍可从仓库中下载。

发现该程序包的网络安全公司 Checkmarx表示，该恶意代码在1.3.4版本中引入，利用相关功能每隔12小时收割一次有价值的信息如 SSH 密钥、bash历史、系统元数据和环境变量，并通过 Dropbox 和 file.io 等服务提取这些信息。

研究员 Yehuda Gelb 在本周发布的一份技术报告中提到，“该攻击通过多个向量实现了分发：直接的npm 安装和作为看似合法的仓库中的隐藏依赖关系。”第二种方法涉及名为 “yawpp（全称为“Yet Another WordPress Poster”）”的GitHub 项目仓库，旨在WordPress 平台上以编程的方式创建帖子。

该 “package.json” 文件将 @0xengine/xmlrpc 的最新版本作为依赖列出，从而让用户尝试在系统上设置 yawpp 工具时，自动下载和安装该恶意 npm 包。

目前尚不清楚该工具的的开发者是否故意将该包添加为依赖。截止本文发布时，该仓库仅被fork过一次。无需多言，由于这种方式利用了用户对包依赖的信任，因此是另外一种有效的恶意软件分发方式。

一旦被安装后，该恶意软件就会收集系统信息、通过systemd 设立在主机上的持久性，并部署 MMRig 密币挖矿机。目前发现通过攻击者门罗钱包积极挖掘密币的受陷系统已达到68个。

另外，该包不断监控正在运行的进程，检查多种命令是否存在如 top、iostat、sar、glances、dstat、nmon、vmstat和ps，并终止所有与挖矿相关的流程。如检测到用户活动，它还会暂停挖矿操作。

Gelb表示，“这一发现提醒我们程序包的存在时长以及不间断的维护历史并无法保证它的安全性。不管恶意包或合法包最初是否是通过更新攻陷的，该软件供应链要求我们保持警惕，在最初审计和在包的生命周期中都应该保持警惕。”

不久前，Datadog Security Lab发现一起针对 Windows 用户的恶意活动，它利用上传到 npm 和 PyPI 的伪造包，部署开源的窃取恶意软件 Blacnk-Grabber和 Skuld Stealer。该公司在上个月检测到这起供应链攻击事件，将威胁组织命名为 “MUT-8694”（MUT即“神秘的未知威胁”），表示与Socket 公司在本月早些时候检测到的一起攻击活动之间存在关联，当时该攻击通过同样的恶意软件感染 Roblox 用户。

多达18和39个恶意唯一包被分别上传到 npm 和 PyPI 仓库中，企图通过 typosquatting 技术伪装成合法包通过检查。研究人员提到，“使用无数程序包和多个恶意用户，表明 MUT-8694意志坚定地攻陷开发人员。与 PyPI 生态系统不同，多数 npm 包都引用了在线游戏创建平台 Roblox，这说明威胁行动者一直都在有意针对 Roblox 开发人员。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[NPM恶意包利用SSH后门攻击开发人员的以太坊钱包](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521235&idx=2&sn=99c13237279fea36d94e88deab21dab3&scene=21#wechat_redirect)

[Python、npm和开源生态系统中的入口点可用于发动供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521093&idx=1&sn=7723bd7496e2f4b228e3013dd21765b4&scene=21#wechat_redirect)

[NPM恶意包假冒 “noblox.js”，攻陷 Roblox 开发系统](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520645&idx=1&sn=5c21506b72287be7f4b329b57e790e30&scene=21#wechat_redirect)

[朝鲜黑客利用恶意npm包攻击开发者](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520635&idx=1&sn=bca2e1daf7393a8f8b52a89f78ee82e1&scene=21#wechat_redirect)

[恶意npm包利用镜像文件隐藏后门代码](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520084&idx=2&sn=07657bb6d212f2245303aa7ff98e61f2&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/11/xmlrpc-npm-library-turns-malicious.html

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