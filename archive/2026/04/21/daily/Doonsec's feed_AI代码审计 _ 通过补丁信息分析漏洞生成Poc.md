---
title: AI代码审计 | 通过补丁信息分析漏洞生成Poc
url: https://mp.weixin.qq.com/s/yvwbaffXsytaE4d8fi3Q2g
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:42:17.150518
---

# AI代码审计 | 通过补丁信息分析漏洞生成Poc

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVnU9K5CC0ia4355Nc6s0elfBNiaB8GtBflqchw1MA3gGZeNAzUc9hPVXAhYdHdd9nuNt4zxXOnwuu6Yzdc5lsH5H5MpAOSiazflcg/0?wx_fmt=jpeg)

# AI代码审计 | 通过补丁信息分析漏洞生成Poc

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 586，阅读大约需 3 分钟

## 前言

通过 ubuntu22 + Cluade Code + CC-Switch + GLM 4.6 air 实现的通过 CVE 编号，获取漏洞版本和已修复版本，然后自动 git 下载项目，比较分支，并生成 Poc。

## Vite 任意文件读取漏洞 (CVE-2026-39363)

CVE 信息
https://nvd.nist.gov/vuln/detail/CVE-2026-39363

已知信息：
**vitejs**
CVE 信息：https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-39363
项目地址：https://github.com/vitejs/vite

```
作为网络安全专家，精通代码审计和漏洞分析，请执行以下任务：

当前已知信息：
已知信息：
**vitejs**
CVE-2026-39363 信息：https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-39363
项目地址：https://github.com/vitejs/vite

1. 根据上面的已知信息，获取漏洞的详细信息，包括漏洞描述、影响范围、CVSS评分等关键数据。

2. 访问项目地址，克隆或下载该项目的源代码。注意：访问GitHub网站时，在命令前添加proxychains；若网络连接不畅，同样需要添加proxychains前缀以确保网络访问正常。

3. 基于漏洞信息，分析该漏洞对项目的影响版本范围，确定受影响的具体版本号。

4. 识别并确认项目中修复相关漏洞的最新版本号，该版本应是漏洞修复后发布的首个稳定版本。

5. 使用git工具比较受影响的版本与修复版本之间的代码差异，具体执行以下操作：
   a. 检出受影响版本的代码
   b. 检出修复版本的代码
   c. 执行git diff命令比较两个版本的差异
   d. 精确定位引入漏洞的代码位置和修复该漏洞的代码变更

6. 根据漏洞分析和代码差异，开发一个可验证的Proof of Concept (PoC)，该PoC应能够清晰演示漏洞的存在和利用过程，包括必要的测试环境说明、操作步骤和预期结果。

7. 整理分析报告，内容应包括：漏洞影响版本确认、修复版本确认、关键代码差异分析、漏洞点精确定位、PoC验证过程及结果。
```

开销：
![0c848554461bc8a220cd12700541159c.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnAacib1EbeunOM9eaXxiaib5wshXcZnvL5eJaOPEdbLaQorHhgXWGAjibsFKP2t2Dx5jRUJrvaqViawwbjIkNIzAntf6mD9BHlK1ib0/640?from=appmsg "null")

0c848554461bc8a220cd12700541159c.png

结果：
![c8ef5239ce61a9a5b7c73221d65e0249.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlvFibBxucowpObrQxXLsmbQd35Oc4WnvqkPEERqAnWLdGAXaLlnlmC6iciazvFy9nkmtzx69XnI0gsdqakianaRgnpUrbAibDx3fNE/640?from=appmsg "null")

c8ef5239ce61a9a5b7c73221d65e0249.png

## 总结

总的来说，大部分开源的github项目的cve漏洞都可以通过类似的方式获取Poc。

## 参考资料

* • 白嫖企业级 AI 进行漏洞补丁分析 [https://mp.weixin.qq.com/s/V0U6t5LrA5S\_HPqAs0vb6A](https://mp.weixin.qq.com/s?__biz=MzIzNDU5Mzk2OQ==&mid=2247486916&idx=1&sn=f5b519a039c0d6e99143c13ea435415f&scene=21#wechat_redirect)
* • https://forum.butian.net/article/808
* • 【代码审计】用友 NCCloudGatewayServlet 命令执行漏洞 补丁分析 [https://mp.weixin.qq.com/s/W86G85XZP3HIWWfR9Mfakw](https://mp.weixin.qq.com/s?__biz=MzkxMjY1NDMxMg==&mid=2247485940&idx=1&sn=32649eb1d6e882cea8162758692fa4b7&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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