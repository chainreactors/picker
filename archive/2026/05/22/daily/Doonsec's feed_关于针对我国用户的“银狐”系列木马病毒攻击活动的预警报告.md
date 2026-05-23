---
title: 关于针对我国用户的“银狐”系列木马病毒攻击活动的预警报告
url: https://mp.weixin.qq.com/s/T1lcdMUF3yg7HjVAtuHT3g
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:37:17.693754
---

# 关于针对我国用户的“银狐”系列木马病毒攻击活动的预警报告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pCMriaDGbE4tmibYOVzo8Th76kibRR42cHzDWITtwibPCB7GvoCZtvfbwBwYRHvX64D6BcsNG1VicquysPQOIJBN9cXL8E9SiagDpkiaZTmFVQK4n8/0?wx_fmt=jpeg)

# 关于针对我国用户的“银狐”系列木马病毒攻击活动的预警报告

公安部网安局

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于国家计算机病毒应急处理中心
，作者CVERC

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6E8qJgL2NUiajd3icaTQYee1BSo341iaNyQXib4BIJSaBQvQ/0)

**国家计算机病毒应急处理中心**
.

集专业与趣味的官方账号，致力于守护您的安全。

一

基本情况

![](https://mmbiz.qpic.cn/mmbiz_png/UR9cvRK2SWxZw8kHGIleiadib4H8ElvDH5jnnYjljw6gRfhdvLaymhmcPfMQYNpc6mdT05DUP6B3DEqtSkFnsAaCr2FRgjpk0J5efQMdyGJJc/640?wx_fmt=png&from=appmsg)

近日，国家计算机病毒应急处理中心和计算机病毒防治技术国家工程实验室依托国家计算机病毒协同分析平台（https://virus.cverc.org.cn）捕获多个文件名中包含“内部调查结果”“违纪名单”“违纪通报信息”“裁员补偿”等词汇的恶意程序，这些恶意程序表面上伪装成快捷方式、文件夹、文档文件或压缩包文件，实际为针对Windows平台用户的远程控制木马病毒。经分析，发现这些木马病毒均为针对我国用户的“银狐”(又名“游蛇”“谷堕大盗”“UTG－Q－1000”“Silver Fox”等）木马病毒攻击活动的最新变种。如果用户不慎运行相关恶意程序文件，将被攻击者实施远程控制、窃密等恶意操作，并可能被网络犯罪分子利用充当进一步实施电信网络诈骗活动的“跳板”。

![](https://mmbiz.qpic.cn/mmbiz_png/UR9cvRK2SWw93fD9QMM61OTNicsDDgk966Q6M8eFuh403IYXxEgibPn6ib658Cu6dVUPiaC6SFnrRKrwMa8PWK2pibuwddCx0JtYsedOzeeYNRsc/640?wx_fmt=png&from=appmsg)

图1 攻击活动过程示意图

二

病毒特征

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UR9cvRK2SWxuWr1GvS5JGWrLRkjg7nQs6IXtHZyQxkibibxqeKkJGcoKQhIEdF2le45Mmpic4n4YTa2nAicEMhaqanleOeuScEckUULNS9ciaLLc/640?wx_fmt=png&from=appmsg)

1. 文件名特征

本次发现的木马病毒新变种继续采用钓鱼欺诈手段，大量采用人事业务相关的诱导性文件名，文件名以“XX季度违纪名单”“通报人员信息”“裁员名单”“补偿方案”等为主，并将图标伪装成文件夹、快捷方式、回收站等，并添加“pdf”后缀迷惑用户。如图2所示。

![](https://mmbiz.qpic.cn/mmbiz_png/UR9cvRK2SWxxFM8Rl7GMCQd0JrTGyG3TH8s1f4ImWibwKFsJP4ibLOgSLhQZHK3m2zpgtaG1naicNehibMyMFrnEiaib1jafOQYuuVH1xQzr5DlQg/640?wx_fmt=png&from=appmsg)

图2 相关病毒样本

2. 文件操作特征

木马病毒运行后，会在“C:\Program Files\Internet Explorer\”文件夹下投放下一步所需的载荷文件。其中关键文件log.dll为下一步运行的加载器，该dll文件通过白文件installer.exe进行加载，如图3所示。

![](https://mmbiz.qpic.cn/mmbiz_png/UR9cvRK2SWwSmJHOf1LCAWiaMdvlv4LafnM58Lob4GUEQ5SysTymU36QaS8ZNSXMTpSAUyB2mwOTy3sT6k7heu8DCicLV36BGH5jJb9Oy7Qtw/640?wx_fmt=png&from=appmsg)

图3 投放下一阶段恶意载荷

3. 网络通信特征

本次发现的病毒样本具有相似的网络通信特征，回联地址URL特征如下所示：

http://[域名]:8880/

http://[域名]:8880/getinstall64

单位网络安全管理员可通过附录获取更多相关特征，并可通过国家计算机病毒协同分析平台（https://virus.cverc.org.cn）查询相关病毒样本的详细信息。

三

防范措施

![](https://mmbiz.qpic.cn/mmbiz_png/UR9cvRK2SWyXiceDcjGBVIqjgJqW7KWrunxx3Kfs4CWyhv6ozpPZTIJQJV9hnFaF8ibEVeicpYibzV5C8zJKx4L1VUyB8gN48UglQIuPQ8JaibUg/640?wx_fmt=png&from=appmsg)

“银狐”系列木马病毒攻击活动与电信网络诈骗活动联系密切，长期将我国用户作为攻击目标，具有变种速度快、隐蔽性强等特点。本次发现的病毒木马攻击活动的攻击目标较为广泛，重点针对具有一定规模的组织机构工作人员，特别是人事相关业务工作人员，主要目的仍然是通过木马病毒控制大量受害者主机，窃取受害企业敏感数据和公民个人信息，进而实施勒索或欺诈。建议采取以下综合防范措施：

01

在使用即时通讯工具（如：微信、QQ、钉钉、飞书等）或电子邮件处理工作事务期间，警惕新增临时工作群组和电子邮件中传播的“违纪”“裁员”等相关主题文件，拒绝点击陌生人发送的文件，对本单位或外单位同事发送的相关文件应与其本人或正式渠道核实。

02

用户可将可疑的文档文件、可执行文件、压缩包文件或解压后的可疑文件先行上传至国家计算机病毒协同分析平台（https://virus.cverc.org.cn）进行安全检测，并保持防病毒软件实时监控功能开启，将计算机操作系统和防病毒软件更新到最新版本。

03

一旦发现本人即时通讯工具或电子邮件发生被盗用现象，应立即停止使用可能感染病毒的计算机设备，将其断开网络链接，并向单位网络管理员、相关同事和亲友告知相关情况，在备份重要数据的前提下，对相关计算机设备进行杀毒和安全检查，更换常用口令且应具有较高强度。

本预警报告得到了安天科技集团股份有限公司、北京瑞星网安技术股份有限公司、奇安信科技集团股份有限公司、北京神州绿盟科技有限公司和计算机病毒防治技术国家工程实验室以及国家计算机病毒协同分析平台各共建单位的技术和信息支持，特此致谢。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/UR9cvRK2SWzuFuSMTkIJAyBFb1wb7W2CLgwgDIkEzLf4qODu32KgkEk0s1Z87wqxTiajYnXDIZoWetyDETmPRwfUypMQNibF1tjWrUr6j3Zms/640?wx_fmt=gif&from=appmsg)

点击“阅读原文”查看详细报告

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/E1iauzlb2BTn7wvyIQ71iaKIJr6icdmdiarF3K2hcQI9JGE5iaFgXHK59ogKDLEJPYJ30TqbT6w8dJGoJ1rtkia7Uaiag/0?wx_fmt=png)

公安部网安局

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/E1iauzlb2BTn7wvyIQ71iaKIJr6icdmdiarF3K2hcQI9JGE5iaFgXHK59ogKDLEJPYJ30TqbT6w8dJGoJ1rtkia7Uaiag/0?wx_fmt=png)

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