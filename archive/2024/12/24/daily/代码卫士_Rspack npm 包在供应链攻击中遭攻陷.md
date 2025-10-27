---
title: Rspack npm 包在供应链攻击中遭攻陷
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521868&idx=2&sn=23c837c94f498de516eae2dd4ecc8c27&chksm=ea94a726dde32e3073487dbfb6c4534cf51a610a0c97bcaf69086b93700433902c9f58c103fc&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-24
fetch_date: 2025-10-06T19:40:25.437977
---

# Rspack npm 包在供应链攻击中遭攻陷

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS3dSnia69SWCrt9NxYPZMibooZnSldZ7dIALTLLC2O5KB4bzCCicqOdtUVUe1CGgEKJwW15ueUGLnqw/0?wx_fmt=jpeg)

# Rspack npm 包在供应链攻击中遭攻陷

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Rspack 披露称，其两个npm 包 @rspack/core 和 @rspack/cli 在一次软件供应链攻击中遭攻陷，可导致恶意人员利用密币挖掘恶意软件，将恶意版本推送到官方程序包注册表中。**

之后，这两个库的1.1.7版本在npm 注册表中的发布已被下架，最新的安全版本是1.1.8。Socket 在分析报告中提到，“1.1.7版本是获得越权npm发布访问权限的攻击者发布的，其中包含恶意代码。”

Rspack 是 webpack 的替代选择，提供“用Rust编写的高性能JavaScript 捆绑版本”。该包最初由字节跳动发布，之后用于多家企业如阿里巴巴、亚马逊、Discord和微软等。@rspack/core和@rspack/cli每周的下载量分别超过30万次和14.5万次，非常受欢迎。

分析这两个恶意版本库发现，它们集成代码，向远程服务器 (“80.78.28[.]72”) 通信，传输敏感的配置详情如云服务凭据，同时通过向 “ipinfo[.]io/json” 发出HTTP GET请求，收集IP地址和位置详情。不过有意思的是攻击者将感染仅限于位于中国、俄罗斯、中国香港、白俄罗斯、伊朗等特定国家或地区的机器。

该攻击的最终目标是，通过 “package.json” 文件中制定的安装后脚本安装程序包时，下载并在受陷的Linux 主机上执行 XMRig 密币挖矿机。Socket 公司指出，“该恶意软件通过安装后脚本执行，而该脚本在程序包安装后自动运行，这就确保无需任何用户操作就能，将其嵌入目标环境中，执行恶意 payload。”

除了发布新版本消除恶意代码外，该项目维护人员表示还将所有的现有 npm 令牌和 GitHub 令牌变得无效，检查该仓库和npm包的权限，并审计源代码中的任何潜在漏洞。目前正在调查令牌被盗的根因。Socket 表示，“该攻击凸显了包管理器采用更严格防护措施保护开发人员的重要性，如执行证明检查以阻止更新到未经验证版本，但这并非完全无懈可击。如 Python 生态系统中发生的 Ultralytics 供应链攻击那样，攻击者可能让然能够通过缓存投毒，攻陷 GitHub Actions，发布获证明的版本。”

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMS3dSnia69SWCrt9NxYPZMiboa78Wzg3gbmI6KYXMZRBJrQR2NWmHeVibqIhiamzaK4p5z9k4lv8D4zbw/640?wx_fmt=gif&from=appmsg)

**Npm 包 vant 也遭受供应链攻击**

攻击 Rspack 的供应链攻击据称也攻击另外一个Npm 包vant。Vant的每周下载量超过4.1万次。Sonatype 公司表示，威胁行动者们设法在npm注册表中发布了多个已失陷版本：2.13.3、2.13.4、2.13.5、3.6.13、3.6.14、3.6.15、4.9.11、4.9.12、4.9.13和4.9.14。

Vant的项目维护人员表示，“该发布时为了修复一个安全问题。我们发现其中一名团队人员的npm令牌被盗且被用于发布多个含安全漏洞的版本。我们已经采取措施修复该版本并预先发布了最新版本。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[在线阅读版：《2024中国软件供应链安全分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520484&idx=1&sn=8a845b39720a318c297075e98f5fe5e0&scene=21#wechat_redirect)

[Solana 热门 Web3.js npm库有后门，可触发软件供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521692&idx=1&sn=5adc287296024b676e739e74bb3e0ca5&scene=21#wechat_redirect)

[Npm 库XMLRPC 插入恶意代码，窃取数据部署密币矿机](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521633&idx=2&sn=4a7d37dee16810a9a2e5aecefb811f16&scene=21#wechat_redirect)

[NPM恶意包利用SSH后门攻击开发人员的以太坊钱包](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521235&idx=2&sn=99c13237279fea36d94e88deab21dab3&scene=21#wechat_redirect)

[Python、npm和开源生态系统中的入口点可用于发动供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521093&idx=1&sn=7723bd7496e2f4b228e3013dd21765b4&scene=21#wechat_redirect)

[NPM恶意包假冒 “noblox.js”，攻陷 Roblox 开发系统](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520645&idx=1&sn=5c21506b72287be7f4b329b57e790e30&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/12/rspack-npm-packages-compromised-with.html

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