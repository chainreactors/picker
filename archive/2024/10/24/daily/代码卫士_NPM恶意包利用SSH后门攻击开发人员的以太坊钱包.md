---
title: NPM恶意包利用SSH后门攻击开发人员的以太坊钱包
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521235&idx=2&sn=99c13237279fea36d94e88deab21dab3&chksm=ea94a2b9dde32baf235babb16ceaf3febef0246b6477a8d02d52cae5e02fb7dc580f8f230a9e&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-24
fetch_date: 2025-10-06T18:52:16.801818
---

# NPM恶意包利用SSH后门攻击开发人员的以太坊钱包

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRSGttW5pdgSoUPfu7txtiacQdlURQNCBicx4KfNoV5CI2libcibHQg2veMDcZQbnMcuUuKJhFJO3a0DQ/0?wx_fmt=jpeg)

# NPM恶意包利用SSH后门攻击开发人员的以太坊钱包

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRSGttW5pdgSoUPfu7txtiacIEuneB1zRhnYTKMtt1AFrCj9GUG6FYxjFibUvOzS1D0duCiaQPl0zZQg/640?wx_fmt=gif&from=appmsg)

**安全研究员发现大量可疑包被发布在注册表中，收割以太坊密钥并通过SSH协议来获得对设备的远程访问权限。**

Phylum 公司的研究人员在上周发布的分析报告中提到，这些包试图“通过在根用户的 authorized\_keys 文件中写入攻击者的SSH公钥，获得对受害者设备的SSH访问权限。”

这些恶意包的目的是模拟合法的 ethers 包，如下：

* ethers-mew（62次下载）
* ethers-web3 （110次下载）
* ethers-6（56次下载）
* ethers-eth（58次下载）
* ethers-aaa（781次下载）
* ethers-audit （69次下载）
* ethers-test（336次下载）

其中一些包（多数由账户名为 “crstianokavic” 和 “timyorks” 发布）被指是为了进行测试，因为它们内含最少得变化。最新和最完整的包是 ethers-mew。这并非npm注册表中首次出现具有类似功能的恶意包。2023年8月，Phylum 公司详述了名为 “ethereum-cryptographyy” 的包，它伪装成一个热门密币库，将用户私钥通过引入恶意依赖进行提取。而最新的攻击方式略有不同，恶意代码被直接嵌入这些包中，使威胁行动者将以太坊私钥嗅探到受控制的域 “ether-sign[.]com” 中。而这种攻击的隐秘之处在于，它要求开发人员在代码中真实使用该包，如使用导入的包创建新的钱包实例。

另外，ethers-mew 包还能够修改 "/root/.ssh/authorized\_keys" 文件，增加受攻击者控制的SSH密钥并使它们能够永久远程访问受陷的主机。研究人员表示，“所有这些程序包，加上作者的账户，只持续了非常短暂的时间，似乎是由作者移除了。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Python、npm和开源生态系统中的入口点可用于发动供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521093&idx=1&sn=7723bd7496e2f4b228e3013dd21765b4&chksm=ea94a22fdde32b396a0c379623e7d047d6762947c21f033e10a0d1e0f8567a584c4d74c12e27&scene=21#wechat_redirect)

[NPM恶意包假冒 “noblox.js”，攻陷 Roblox 开发系统](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520645&idx=1&sn=5c21506b72287be7f4b329b57e790e30&chksm=ea94a0efdde329f9ad2d8aeb345bc8abbc9c850e4352100732abc69077d910cccc0ce2259be5&scene=21#wechat_redirect)

[恶意npm包利用镜像文件隐藏后门代码](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520084&idx=2&sn=07657bb6d212f2245303aa7ff98e61f2&chksm=ea94be3edde33728bb8224656ce3ac1a88ba9ebb495c26fb1b3a31d7a63bc26b9e33180851f5&scene=21#wechat_redirect)

[NPM恶意包利用招聘诱骗开发人员安装恶意软件](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519374&idx=1&sn=3fbf5576659950047d9bc0dcc5ce061e&chksm=ea94bde4dde334f2adf3531901e2c95aea07bf3a099b0125048228dac88779dac4e96a334141&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/10/malicious-npm-packages-target.html

题图：网络

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