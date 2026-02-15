---
title: 谷歌将疑似俄罗斯黑客与针对乌克兰组织的CANFAIL恶意软件攻击联系起来
url: https://mp.weixin.qq.com/s/8ncO4BoN_Xvfw_cU8qkpgQ
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:21:37.047720
---

# 谷歌将疑似俄罗斯黑客与针对乌克兰组织的CANFAIL恶意软件攻击联系起来

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7Pjtia78oUstorLmeBStsAJDZnJljQjOUicTBWtGUzVgndYA5bW584dquLyG6AH5Vfe6a8bRm1ZJWYdicpJfcFSQPqtVdKRn745BY/0?wx_fmt=jpeg)

# 谷歌将疑似俄罗斯黑客与针对乌克兰组织的CANFAIL恶意软件攻击联系起来

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

此前未被记录在案的威胁行为者被指使用名为**CANFAIL**的恶意软件攻击乌克兰组织。

谷歌威胁情报小组 (GTIG) 将该黑客组织描述为可能与俄罗斯情报机构有关联。据评估，该威胁行为者曾以乌克兰地方和国家政府的国防、军事、政府和能源机构为攻击目标。

GTIG补充说，该组织还对航空航天组织、与军事和无人机有联系的制造公司、核能和化学研究组织以及参与乌克兰冲突监测和人道主义援助的国际组织表现出越来越浓厚的兴趣。

“尽管该组织的技术水平和资源不如其他俄罗斯威胁组织，但最近它开始利用大型语言模型 (LLM) 克服一些技术限制，” GTIG表示。

“他们通过诱导进行侦察，制造诱饵进行社会工程攻击，并寻求入侵后活动和 C2 基础设施设置的基本技术问题的答案。”

最近的网络钓鱼活动涉及攻击者冒充合法的乌克兰国家和地方能源组织，以获取对组织和个人电子邮件帐户的未经授权的访问权限。

![](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7PuQuB7aFUFQTKx0d3B6OlpFd7CwpK83z7MHiac84y6hfIvcJHADzbtzpb2QDGfHMtwicTBzMquq6unIYfFu9cQIZmkjJQRSBibBo/640?wx_fmt=jpeg)

据称，该组织还伪装成一家与乌克兰客户合作的罗马尼亚能源公司，此外还以一家罗马尼亚公司为目标，并对摩尔多瓦组织进行侦察。

为了实施攻击，攻击者会根据研究结果，生成针对特定地区和行业的定制化电子邮件地址列表。攻击链中似乎包含由LLM生成的诱饵，并嵌入指向包含CANFAIL恶意软件的RAR压缩包的Google Drive链接。

CANFAIL 通常伪装成 PDF 文档（\*.pdf.js），使用双重扩展名。它是一种混淆的 JavaScript 恶意软件，旨在执行一个 PowerShell 脚本，该脚本会下载并执行一个仅占用内存的 PowerShell 投放器。同时，它还会向受害者显示一条虚假的“错误”消息。

谷歌表示，该威胁行为者还与名为PhantomCaptcha的活动有关。该活动由 SentinelOne SentinelLABS 于 2025 年 10 月披露，其目标是与乌克兰战争救援工作相关的组织，通过网络钓鱼电子邮件将收件人引导至虚假页面，这些页面包含ClickFix 式的说明，用于激活感染序列并传播基于 WebSocket 的木马程序。

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