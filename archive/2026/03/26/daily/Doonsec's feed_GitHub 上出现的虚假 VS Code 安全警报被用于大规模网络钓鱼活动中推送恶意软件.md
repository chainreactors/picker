---
title: GitHub 上出现的虚假 VS Code 安全警报被用于大规模网络钓鱼活动中推送恶意软件
url: https://mp.weixin.qq.com/s/WJOEbague6gECUUMjHYzHQ
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:29:30.301192
---

# GitHub 上出现的虚假 VS Code 安全警报被用于大规模网络钓鱼活动中推送恶意软件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7PVVM8UeNtXSF2H5t25qoyYhJVGEzs9euk6yiaTALSAvsAllID5R7vodyiaQKp88PWiawvlT5xkwuOeOtO9rgxaWHBHx3GFM4SCL4/0?wx_fmt=jpeg)

# GitHub 上出现的虚假 VS Code 安全警报被用于大规模网络钓鱼活动中推送恶意软件

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

一场大规模的网络钓鱼活动正在针对 GitHub 上的软件开发人员，利用发布在 GitHub Discussions 中的虚假 Visual Studio Code 安全警报，诱骗用户下载恶意软件。

这些攻击旨在伪装成合法的安全公告，警告开发者 VS Code 中存在严重漏洞，并敦促他们通过外部链接安装所谓的“已修补”版本。

这场运动的起因是成千上万篇几乎完全相同的帖子在几分钟内涌入 GitHub 代码库。

每篇帖子都模仿官方安全公告，标题耸人听闻，例如“Visual Studio Code – 严重漏洞 – 需要立即更新”、“关键漏洞利用 – 需要紧急行动”和“严重威胁 – 立即更新”。

这些帖子经常引用捏造的 CVE 和虚假的版本范围，以使警告看起来可信。

由于 GitHub Discussions 会自动向仓库参与者和关注者发送电子邮件通知，这些虚假警报也会直接发送到开发者的收件箱，从而将活动的影响范围远远扩展到平台本身之外。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7OHRm8dmbvKyDPNH3OOFuTnwjY8YhcRX2ZT0uocpJJyBazMwPUusMzhgwaVEEUe8yApzS4n49Rb6kg1TgFvI5vPk3ddpIRfcics/640?wx_fmt=png&from=appmsg)

Socket.dev 分析师认定这是一场有组织的垃圾邮件行动，并指出帖子是由新创建的或低活跃度的帐户创建的，这些帐户标记了大量不相关存储库中的开发人员，以最大限度地提高曝光率。

研究人员发现，该活动滥用 GitHub 自身的通知系统，使虚假警报看起来既紧急又合法——这种策略降低了开发者在阅读看似可信平台警告时自然产生的怀疑态度。

每个虚假讨论帖都包含一个下载所谓更新版 VS Code 的链接，但这些链接指向的是文件共享服务，而不是官方分发渠道。

官方的VS Code更新从来不会以这种方式分发，但这些帖子营造的紧迫感足以促使开发者毫不犹豫地点击。

该攻击能够无缝融入 GitHub 的协作环境，将开发者的日常工作空间变成恶意软件的传播渠道。

此次活动的规模之大尤其令人担忧。成百上千条此类帖子在GitHub搜索结果中迅速出现，表明这是一场高度自动化的行动。

开发者们每天都在他们信任的平台内部成为攻击目标，而不是通过传统的网络钓鱼邮件，这标志着攻击者应对以开发者为中心的威胁的方式发生了显著转变。

## **多步骤重定向和浏览器指纹识别**

Socket.dev 的分析师追踪了虚假讨论区中的一个有效载荷链接，并发现了一个精心构建的多步骤重定向链。点击该链接首先会将受害者重定向到一个 Google 分享端点。

之后，路径会根据用户浏览器是否携带有效的谷歌 cookie 而分叉。携带 cookie 的用户会被自动通过 301 重定向到攻击者控制的域名 drnatashachinn[.]com，该域名充当此次攻击活动的命令与控制服务器。

没有 cookie 的用户将直接从 Google 端点获得指纹识别页面，这可能是为了过滤掉机器人和自动安全扫描程序而采取的备用方案。

一旦真实用户访问攻击者的基础设施，混淆的 JavaScript 有效载荷就会立即执行。

该脚本收集浏览器指纹数据，包括时区、语言环境、平台、用户代理和自动化信号等 `navigator.webdriver`，用于识别访问者是真人还是机器人。

一个隐藏的 iframe 会进一步交叉检查用户代理，以检测伪造的环境。所有收集到的数据随后都会通过自动 POST 请求静默地提交到攻击者的端点，无需受害者进行任何交互。

此分析阶段起到过滤层的作用，将真实用户与扫描者区分开来，然后再将确认的目标路由到后续有效载荷，例如钓鱼页面或漏洞利用工具包。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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