---
title: 研究人员称，Fiverr 涉嫌向谷歌索引泄露用户信息
url: https://mp.weixin.qq.com/s/Q7j1MLCA3TT8oHSzh0C76Q
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:47:11.925518
---

# 研究人员称，Fiverr 涉嫌向谷歌索引泄露用户信息

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7M98DRIs3eum7owMogPSzDn2s1hCIUlv2YnEqpCFwVn9eCpibVhicRgMVG0icbZtbJxtTaT6miataia6Lk16srZJSXfULxsPO3uggZI/0?wx_fmt=jpeg)

# 研究人员称，Fiverr 涉嫌向谷歌索引泄露用户信息

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

自由职业服务平台 Fiverr 面临重大隐私事件，研究人员发现敏感的客户文件可以公开访问，并被谷歌搜索收录。

根据 Hacker News 上最近的披露，不安全的文件托管配置泄露了自由职业者和客户之间交换的个人身份信息 (PII)，包括已填写的税务表格。

## **Cloudinary配置错误**

数据泄露的根源在于 Fiverr 在其内部消息系统中处理文件共享的方式。

该平台依赖于名为 Cloudinary 的第三方服务来处理和托管图像和 PDF 文档，包括交付给客户的最终工作成果。

虽然 Cloudinary 的运行方式与Amazon S3 数字存储桶类似，并支持安全、过期的网络链接，但据报道 Fiverr 对该服务的配置有误。

Fiverr 没有要求用户进行身份验证，而是选择为这些敏感附件生成完全公开的 URL。由于这些文件是公开的，因此像 Google 这样的搜索引擎能够抓取并索引它们。

这表明，公共文件链接可能通过 Fiverr 网络上的某些未受保护的 HTML 页面暴露出来。

这一疏忽的影响十分严重，因为任何人都可以使用特定的谷歌搜索查询来查找私人文件。

例如，在 Fiverr 的 Cloudinary 域名上进行“表格 1040”的特定网站搜索，即可立即显示包含高度敏感的财务和个人数据的私人税务文件。

有趣的是，研究人员指出了一个令人担忧的矛盾之处。Fiverr积极购买谷歌广告来推广报税服务，但该平台却未能保障最终的财务成果安全。

此次泄露事件立即引发了监管方面的担忧。由于未能妥善保管财务文件，该平台及其税务筹划自由职业者可能直接违反了联邦贸易委员会的《保障规则》和《格雷姆-里奇-比利雷法案》（GLBA），这两项法规均对消费者财务数据提供严格保护。

发现该问题的研究人员声称遵循了标准的负责任披露协议。一份详细的漏洞报告已在公开发布前40天发送给了Fiverr指定的安全团队。

在未收到该公司的任何回应或补救措施后，研究人员选择在 Hacker News 上发布调查结果，以警告受影响的用户。

## **关键要点和应对措施**

在Fiverr解决此次公开曝光事件之前，用户面临身份盗窃和金融诈骗的风险。自由职业者和客户都应立即采取预防措施：

* **停止敏感文件传输：** 用户应暂时停止通过 Fiverr 的消息系统发送敏感文件，例如税务表格或医疗记录。
* **实施签名 URL：**  Fiverr 必须紧急更新其 Cloudinary 集成，以对所有用户之间的文件传输使用签名、有时限的 URL，以确保文件在下载后过期。
* **请求取消搜索索引：** 该公司需要向谷歌发出紧急下架请求，要求其从公共搜索结果中删除暴露的域名目录。
* **警惕身份盗窃：** 在 Fiverr 上购买财务或税务筹划服务的客户应密切关注其信用报告，以防未经授权的活动。

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