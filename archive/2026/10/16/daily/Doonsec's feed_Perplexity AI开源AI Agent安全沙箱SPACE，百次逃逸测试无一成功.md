---
title: Perplexity AI开源AI Agent安全沙箱SPACE，百次逃逸测试无一成功
url: https://mp.weixin.qq.com/s/JFAEBzeLqCdU-LP3fz_fSg
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:28:06.582146
---

# Perplexity AI开源AI Agent安全沙箱SPACE，百次逃逸测试无一成功

# Perplexity AI开源AI Agent安全沙箱SPACE，百次逃逸测试无一成功

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX1pVSzeb0RnEXAUQgyUb1WcKTlmqXEXaS0IxibRqCnsVusybvAtIrQ7Id7Qakicibgjp6pCjhwGiaRRictGXG6wficPyXej4SYMbWfw4/640?wx_fmt=gif)

![image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1ibw68BGZxPGF6NPGdhqXpzuLBSZvhHqhkNxEIXTKszmCmNEbLNTnAlOX3BrRo9bhVU0GsE1ffhqRQ5EzanEEKzk8xvqaEibGEg/640?wx_fmt=jpeg&from=appmsg)

AI搜索引擎初创企业Perplexity AI正将业务重心转向AI Agent安全领域。此前行业已发生多起广受关注的安全事件：自主系统突破安全环境限制，对第三方网站造成破坏。

该公司专门开发了用于隔离AI Agent的沙箱工具SPACE，今日正式开源，所有开发者均可使用这一工具加固自身系统安全。目前CoreWeave、Akamai、Crusoe等提供AI云基础设施平台的合作伙伴均已部署SPACE。

Part01

AI Agent沙箱为核心防护屏障

过往多次发生逃逸事件

AI沙箱是防范AI Agent泄露敏感数据、擅自攻击其他系统的核心防护屏障。这类安全隔离的虚拟环境允许自主Agent运行第三方软件、访问互联网、执行任务，不会危及主机、企业内网及底层数据中心的安全。云平台会为每个AI Agent分配独立的隔离计算环境，一旦Agent运行出错、执行破坏性指令，或被恶意提示词诱导，所有影响都会被限制在沙箱内部，不会向外扩散。

但现有AI沙箱的防护并非万无一失。此前已发生多起AI Agent突破沙箱限制、对外造成破坏的安全事件。

其中最受关注的一起事件中，OpenAI正在测试的AI Agent逃出沙箱，入侵了模型托管平台Hugging Face。这些Agent还曾攻击美国、澳大利亚政府运营的网站。

目前多数前沿模型实验室更侧重"模型对齐"工作，即训练AI系统遵守规则，不主动寻找防护机制的漏洞。Perplexity工程师Zibi Braniecki向Semafor表示，Perplexity选择了另一条路径，重点提升防护机制本身的强度与可靠性。

Part02

SPACE内置多层隔离机制

百次逃逸测试无一突破

Perplexity研发SPACE的初衷是保护旗下Portable Computer agents的运行安全。这类面向客户推出的本地部署AI Agent可代用户执行各类任务，包括开发Web应用、调研产品、线上购物、预订酒店等。

针对Perplexity的Computer agents，SPACE提供代码隔离执行、暂停与恢复、故障回滚、会话分支等安全能力。所有Agent都运行在自带独立操作系统的轻量虚拟机中，与主机完全隔离。

平台提供用户可控的控制平面，支持创建、运行、暂停、删除上述虚拟机。SPACE始终将沙箱视为"不可信环境"，将网络访问权限、平台凭证的管理模块部署在沙箱外部，既允许Agent连接授权服务，又不会让敏感信息暴露在沙箱环境内部。SPACE还会对运行环境定期创建文件快照与检查点，保存任务进度，一旦出现问题可随时回滚到正常状态。

到目前为止，这类回滚操作还从未被触发过，SPACE的防护能力表现得十分稳固。Zibi Braniecki向Semafar透露，团队在SPACE环境中测试了9款前沿模型，专门向模型下达指令，要求其尝试突破沙箱限制。

累计118次逃逸尝试中，没有任何模型成功逃脱，仅少数模型找到了绕过网络限制的方法。Perplexity现已修复这些薄弱点，后续复测中所有模型均无法再绕过限制。

为对比SPACE的防护效果，Perplexity使用其他商用闭源沙箱开展了相同测试，结果显示AI Agent可从多款参测沙箱中成功逃逸。

Part03

开源沙箱成行业探索方向

SPACE采用开源模式是筑牢AI Agent安全防线的关键，开源可推动全行业协同共建所需的高强度防护机制。这与早期网页浏览器的发展路径类似：当时开发者社区共同协作，搭建起支撑安全浏览、在线交易所需的安全体系。

并非只有Perplexity在探索AI Agent沙箱的开源路线。英伟达上月发布了OpenShell项目，隶属于其整体Open Agent Safety Platform，截至目前尚未出现任何AI Agent从OpenShell中逃逸的公开报告。

Perplexity在开源安全领域已有长期布局。除SPACE外，该公司还推出了多款开源安全工具：BrowseSafe可检测网页中隐藏的恶意指令；Numbat用于排查Agent的危险行为；Bumblebee是一款扫描器，可识别存在风险的AI工具配置。

参考来源：

Perplexity AI open-sources its secure AI agent sandbox SPACE

https://siliconangle.com/2026/10/15/perplexity-ai-open-sources-its-secure-ai-agent-sandbox-space/

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0YicFBBV16wQdPW4H8cTibDhNEfda7XWQYxJejxMQXMkmUHx6wDDLARUIbdeicO6WQyTRZN8jBRKSbL2bT8srvaRb0FMGv7DXJU8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651348384&idx=1&sn=b0d043fbf6f272983df964e3f249232e&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3mETrvTp1xSWg4nsaY8jdaRdeta9l692aSBiaWUg95sD0gVn7BiaQ6bng5NuFFmERdoTibOtYlCXD4z0Fsus60Vbx1ExXibLicvq4s/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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