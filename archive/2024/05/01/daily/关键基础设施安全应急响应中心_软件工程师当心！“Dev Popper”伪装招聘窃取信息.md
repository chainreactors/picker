---
title: 软件工程师当心！“Dev Popper”伪装招聘窃取信息
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247543539&idx=3&sn=2c160b6db7d27a9a28f09908516f7c26&chksm=c1e9a6a2f69e2fb4e76e828bf26df3ab7fa88dbf06606186cd07b1b9c3f4e67f6d6f5a51c8bc&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-05-01
fetch_date: 2025-10-06T17:19:26.733459
---

# 软件工程师当心！“Dev Popper”伪装招聘窃取信息

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogtQwb7z1ouPCnCE870kNxnLpdHMwicGyjH5LOch0wfaicJsraUpboqhAibVGGibXhgibficF2TVEyQselkQ/0?wx_fmt=jpeg)

# 软件工程师当心！“Dev Popper”伪装招聘窃取信息

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogtQwb7z1ouPCnCE870kNxnLAXkTVW3OWbZZAxkeFmCf1FSOCFngMkQ4Zicw0GrKMFFNxHYpVN4Cm6A/640?wx_fmt=png&from=appmsg)

网络安全公司Securonix近日发现了一个名为“Dev Popper”的新型网络攻击活动，该活动针对软件开发人员，利用虚假的面试流程诱使受害者安装恶意软件，进而窃取受害者供职企业的机密信息。

攻击者会伪装成企业招聘人员，通过邮件或社交媒体联系目标开发者，提供虚假的软件开发职位。在面试过程中，攻击者会要求受害者下载并运行声称来自GitHub的“标准编码任务”，以此让整个过程看起来合法合规。

然而，该代码实际上是一个恶意压缩文件，其中包含一个恶意NPM软件包。这个软件包内嵌了一个名为“imageDetails.js”的混淆JavaScript文件，该文件会通过Node.js进程执行“curl”命令，从外部服务器下载另一个恶意存档“p.zi”。

“p.zi”存档中包含下一个阶段的攻击载荷，也就是一个混淆的Python脚本，充当远程访问木马(RAT)。

一旦RAT在受害者的系统上激活，它就会收集并发送基本系统信息到攻击者的控制服务器，这些信息包括操作系统类型、主机名和网络数据。

Securonix报告称，此RAT具备以下功能：

* 长期驻留，供攻击者持续控制受害者系统。
* 执行文件系统命令，以搜索并窃取特定文件或数据。
* 远程执行命令，用于实施额外的漏洞利用或部署恶意软件。
* 直接从“文档”和“下载”等重要文件夹窃取数据，通过FTP传输到攻击者服务器。
* 记录剪贴板内容和按键记录，以监控用户活动并可能窃取凭证。

虽然目前尚无法确定“DevPopper”攻击的幕后黑手，但利用虚假工作机会作为诱饵传播恶意软件的做法仍然屡见不鲜。软件开发人员在求职过程中应该保持警惕，不要轻易下载或运行来历不明的代码，以免遭受网络攻击。

值得注意的是，攻击者正是利用了软件开发人员（包括网络安全专业人士）的职业操守及其对招聘流程的信任。求职者担心拒绝面试官的要求会影响求职机会，因此更容易落入陷阱。

原文来源：GoUpSec

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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