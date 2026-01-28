---
title: APT黑客利用GOGITTER工具和GITSHELLPAD恶意软件攻击印度政府
url: https://mp.weixin.qq.com/s/rzxrEg4HiNj0A-7fi4dnSQ
source: Doonsec's feed
date: 2026-01-27
fetch_date: 2026-01-28T03:33:27.476221
---

# APT黑客利用GOGITTER工具和GITSHELLPAD恶意软件攻击印度政府

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dzJiaU8Wt1qzsvicowOhyOoAXZHa9Z17Y0TzuhBIy8N9cCzO8nlZDib3P6Tra1RexsThjZgyGJITRgiaBSLBV4TORw/0?wx_fmt=jpeg)

# APT黑客利用GOGITTER工具和GITSHELLPAD恶意软件攻击印度政府

O安全研究员
O安全研究员

O安全研究员

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qzsvicowOhyOoAXZHa9Z17Y0508pQG4Funb7dj2ibV98E55CYs0icRhCsNMoRciasNNnwn4oZWy252gmg/640?wx_fmt=png&from=appmsg)

来自巴基斯坦的高级持续威胁行为者利用新发现的工具和恶意软件，针对印度政府组织发动协调攻击，旨在绕过安全防御。

该行动被称为“Gopher Strike”，于2025年9月出现，代表针对敏感政府基础设施的有针对性网络行动的显著升级。

此次协调攻击显示出国家支持的威胁行为者日益精进，他们不断完善技术能力和作程序。

攻击链始于精心设计的钓鱼邮件，其中包含冒充合法政府通信的欺骗性PDF文件。

这些PDF显示的是官方文件的模糊图像，并利用社会工程手法，通过点击标有“下载并安装”的按钮诱骗接收者下载ISO文件，这似乎是在请求假装的Adobe Acrobat更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qzsvicowOhyOoAXZHa9Z17Y0Onoouj4ZM3Nml1nC0jSoFMa9VtjiaTyGMTiajib9rW05UXrfAzkNLGnZA/640?wx_fmt=png&from=appmsg)

恶意ISO文件会处于休眠状态，直到被激活，内含旨在对被攻破系统建立持续访问的隐藏恶意软件。

感染机制依赖于三种用 Golang 编写的定制工具协同工作，以建立对目标机器的控制。

Zscaler的分析师和研究人员确认GOGITTER是初始下载组件，通过嵌入的认证令牌从威胁行为者控制的GitHub仓库获取额外负载。

部署后，GOGITTER 会创建一个名为 windows\_api.vbs 的 VBScript 文件，每 30 秒持续轮询命令与控制服务器，检查感染机器上是否有新指令执行。

**GITSHELLPAD创新的基于GitHub的持久化机制**

GITSHELLPAD代表了该活动最独特的元素，作为一个轻量级后门，利用私有的GitHub仓库进行所有命令与控制通信。

这种方法使威胁行为者能够在看似合法的 GitHub 活动中隐藏恶意流量，使安全监控工具的检测变得更加困难。

感染后，GITSHELLPAD通过在威胁行为者的私有仓库中创建新目录（格式为SYSTEM-[hostname]）来注册受害者，然后添加包含Base64编码系统信息的info.txt文件，描述被攻破机器。

后门每15秒轮询GitHub的API，查找存储在command.txt文件中的新指令，使操作员能够远程执行侦察命令、下载额外工具或部署进一步的恶意软件。

这种设计特别有效，因为它避免了传统的网络指示器，同时通过数百万组织已信任并为合法开发目的列入白名单的服务，保持可靠的双向通信。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qzsvicowOhyOoAXZHa9Z17Y0MBxrmA9FotpHJcLIzFR8D1QxxPw4tD6OIz6IncklWBia08yfJFzea9Q/640?wx_fmt=png&from=appmsg)

最后阶段是通过GOSHELL部署Cobalt Strike Beacon，GOSHELL是一个自定义壳码加载器，仅在特定硬编码主机名的机器上执行，进一步限制有效载荷对目标。

安全研究人员持续追踪这一不断演变的威胁，以保护政府网络免受未来攻击。

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