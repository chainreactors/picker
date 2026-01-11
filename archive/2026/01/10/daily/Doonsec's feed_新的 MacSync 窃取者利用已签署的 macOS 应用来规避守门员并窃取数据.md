---
title: 新的 MacSync 窃取者利用已签署的 macOS 应用来规避守门员并窃取数据
url: https://mp.weixin.qq.com/s/ThCB3M2knGriq-EysrITFQ
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:36:52.788716
---

# 新的 MacSync 窃取者利用已签署的 macOS 应用来规避守门员并窃取数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dzJiaU8Wt1qzbUGSFLmaBdvia1ZicSxKvHw3r2KSS9QRQnRJF2bHe0DoqIg2TicNDuFIyCSpJicBLgic6A2GuPQSb2zA/0?wx_fmt=jpeg)

# 新的 MacSync 窃取者利用已签署的 macOS 应用来规避守门员并窃取数据

原创

O安全研究员

O安全研究员

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qzbUGSFLmaBdvia1ZicSxKvHww33UKST5DSOyLjCb6sTPwVKYKC3ugAQJDmXKIWA4jsE3NUnWYrOJicg/640?wx_fmt=png&from=appmsg)

网络安全研究人员发现了MacSync恶意软件的一种新变种，针对macOS用户。

与之前依赖复杂ClickFix技术的版本不同，这一版本伪装成一个合法签署、经过公证的苹果应用程序，从而绕过macOS Gatekeeper的安全防护，窃取了敏感数据。

## **代码签名恶意软件绕过安全**

Jamf Threat Labs 最近发现了这个进化版的 MacSync 窃取器，其中包含两项重大技术变更。

该恶意软件现以代码签名和公证的Swift应用程序形式出现，Swift是苹果官方macOS开发的编程语言。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qzbUGSFLmaBdvia1ZicSxKvHwicZlQmdq6Fia24eEcvJ5M66PDmicVQ2ibO6vPTRuBbma7GvEu2yeNVTibbg/640?wx_fmt=png&from=appmsg)

这种巧妙的伪装帮助恶意软件通过伪装成经过验证开发者的可信应用来规避检测。

网络犯罪分子通过盗窃、购买被盗的开发者账户，或使用虚假身份建立假开发者公司来获得合法开发者证书。

通过利用这些证书，MacSync避免了触发macOS关于“未识别开发者”的安全警告，这些警告通常会提醒用户潜在威胁。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qzbUGSFLmaBdvia1ZicSxKvHwHYFEEmMKHyLRtaaGa62YibRWobbicJ3IF53leEjiad0n5jDT55WZVeYMw/640?wx_fmt=png&from=appmsg)

新版本模仿在线消息平台，特别针对像 zk-Call 这样爱沙尼亚的呼叫和即告服务感兴趣的用户。

这种社会工程手法增加了受害者在无疑情况下安装恶意软件的可能性。

这个 MacSync 版本与前作有显著不同。早期变体较轻，直接在内存中运行模块化有效载荷，且磁盘占地较大。

不过，Jamf研究人员指出该版本拥有25.5MB的巨大磁盘映像，显示出功能增强和嵌入式组件。

MacSync 对被感染的系统构成严重威胁。该恶意软件可以安装后门进行远程系统控制，窃取存储的数据和浏览器信息，针对加密货币钱包凭证，并持续保持隐藏访问。

Jamf认定了FocusGroovy[.]com作为一个命令与控制服务器，过去用于获取额外的有效载荷，网页浏览器现在会将该网站标记为疑似钓鱼活动，正如Moonlock报道的那样。

虽然具体传播方式尚不清楚，但潜在的感染途径包括恶意广告活动、社交媒体利用、搜索引擎控以及定向鱼叉式钓鱼攻击。

Mac用户应保持警惕，避免从不可信来源下载应用，即使这些应用看起来是合法签名的。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dzJiaU8Wt1qwqJgvgiaEEbM4iaLlwQUhMic3TfI1ibRVlBcl7tiblcrRxgzBrF0UMhRtHtSuVfKdgVibQjjB7OoUYIU5w/0?wx_fmt=png)

O安全研究员

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dzJiaU8Wt1qwqJgvgiaEEbM4iaLlwQUhMic3TfI1ibRVlBcl7tiblcrRxgzBrF0UMhRtHtSuVfKdgVibQjjB7OoUYIU5w/0?wx_fmt=png)

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