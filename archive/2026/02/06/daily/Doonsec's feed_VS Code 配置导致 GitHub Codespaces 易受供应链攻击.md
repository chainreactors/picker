---
title: VS Code 配置导致 GitHub Codespaces 易受供应链攻击
url: https://mp.weixin.qq.com/s/ksRD6IamKocOS2eCqJfhaA
source: Doonsec's feed
date: 2026-02-06
fetch_date: 2026-02-07T04:04:31.848648
---

# VS Code 配置导致 GitHub Codespaces 易受供应链攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfVCr1AWGiaCB9Vdh6ZVoj4SuCa87HJ6UgvmoZzxZIFibFdyA4SojWsUZd6LiccoXTkXmxgtZiatej5VYRS2JibOHfnjdKyoJH64rViag/0?wx_fmt=jpeg)

# VS Code 配置导致 GitHub Codespaces 易受供应链攻击

Ionut Arghire
Ionut Arghire

代码卫士

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Orca****安全公司发布报告称，在GitHub Codespaces中打开代码仓库或拉取请求时，VS Code集成配置文件自动执行的功能可能引发供应链攻击。**

Codespaces作为云端托管的开发环境，允许用户几乎即时创建完全配置的Visual Studio Code实例，提供紧密的仓库集成和容器支持。Orca表示，该环境虽然便于开发者测试代码、审查拉取请求等操作，但也可能通过仓库定义的配置文件使其面临攻击风险。

这家网络安全公司指出：“Codespaces本质上是运行在云端的VS Code，后端采用Ubuntu容器，内置GitHub身份验证和仓库集成功能。这意味着当攻击者控制仓库内容时，任何涉及代码执行、密钥管理或扩展操作的VS Code功能都可能被滥用。”

该公司解释称，问题在于当用户打开仓库或拉取请求时，甚至从现有Codespace环境检查拉取请求时，Codespaces会自动应用所有VS Code配置。攻击者可在.vscode/文件夹的JSON文件中植入恶意命令，当用户打开任意文件夹时，这些命令将在未经用户批准的情况下被自动化流程执行。

此外，攻击者可通过在另一个JSON文件中嵌入集成终端的变量来攻击Linux系统，将导致恶意负载通过bash执行。攻击者还可利用devcontainer.json文件嵌入任意命令，这些命令将在容器初始化完成后自动在机器上执行。Orca表示，这些攻击途径可能导致GitHub令牌、Codespaces密钥及其他敏感信息被窃取。GitHub令牌允许以受害者用户身份进行读写操作，同时也可被滥用以向公共仓库提交恶意拉取请求。

Orca进一步解释称，攻击者可在供应链攻击中滥用GitHub Codespaces的远程代码执行漏洞——通过分叉公共仓库创建恶意拉取请求，当维护者通过Codespaces打开该请求时，其GitHub令牌即会泄露。攻击者随后便能以已验证维护者身份推送代码。攻击者可创建恶意VS Code扩展程序发起跨站脚本攻击，并通过2024年8月披露的“0.0.0.0 Day”漏洞访问本地服务。Orca同时警告称："攻击者可将窃取的GitHub令牌与隐藏的未公开API结合使用，从而以受害者名义调用付费高级AI模型。"

Orca称已向微软报告相关发现，微软回应称此行为属于系统设计预期。GitHub 尚未就此事置评。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[VS Code 分支版本推荐不存在的扩展，在 Open VSX 中引发供应链风险](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524812&idx=2&sn=0edf75f3aa3c9f7e12f65bcbeed9b91f&scene=21#wechat_redirect)

[微软决定不修复 Visual Studio 中的一次点击 RCE 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517894&idx=1&sn=670ff70804d3fe5c06fd2977fd2824f5&scene=21#wechat_redirect)

[详述Visual Studio 代码远程开发扩展中的远程命令执行漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247508212&idx=1&sn=86d703dae7098e040955c7396564be6e&scene=21#wechat_redirect)

[微软紧急修复两个 RCE，影响 Windows Codecs 库和 Visual Studio](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247495685&idx=2&sn=c3a8830b130373e79183518ff25ee02c&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/vs-code-configs-expose-github-codespaces-to-attacks/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

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