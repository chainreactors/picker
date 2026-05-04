---
title: 今日（2026年5月3日）热点网络安全漏洞动态
url: https://mp.weixin.qq.com/s/Gq8qu_V26Q7Q4tjD-p11IQ
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:28:08.575481
---

# 今日（2026年5月3日）热点网络安全漏洞动态

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RwAbCjh555uG2UzXK2TmoMNNQJBGm7FtZEgHVGPE3Judz49TicjKdia2VROlyQyaicRcEXtm72IhIhkFpbD6sbpFTxrA4Viba7UmibFG1UmreNbA/0?wx_fmt=jpeg)

# 今日（2026年5月3日）热点网络安全漏洞动态

奇安信 CERT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**日期：**2026-05-03　　**威胁等级：****High****来源：**Tenable · VulDB · WPScan · NVD

## 一、概要

2026年5月3日最新发布/更新的高热度漏洞：**SGLang 高危漏洞**（CVE-2026-7669，AI推理框架，5月3日Tenable收录）；**Yudao-cloud 高危漏洞**（CVE-2026-7678，企业级低代码框架，5月3日VulDB发布）；以及**WordPress前端文件相关漏洞**（CVE-2026-5337，WPScan 5月3日更新）。

## 二、高危漏洞详情

### CVE-2026-7669：sgl-project SGLang 高危漏洞（5月3日公开）

**CVSS 高危**AI/LLM推理框架

**受影响产品：**sgl-project SGLang（AI/LLM推理框架，最高至0.5.9版本）。

**影响：**高危漏洞（涉及服务端问题），可能导致远程代码执行或严重安全绕过，在AI模型部署环境中风险极高。

**热度原因：**5月3日在Tenable等平台列为最新CVE；AI/ML工具链热度持续攀升，SGLang作为新兴LLM推理框架在企业和开发者中快速普及；当日新鲜数据，具有实时参考价值。

**修复建议：**立即升级 SGLang 至**0.5.10或更高版本**；限制暴露、加强输入验证；使用容器隔离部署AI服务；监控异常API调用。

### CVE-2026-7678：YunaiV yudao-cloud 高危漏洞（5月3日发布）

**CVSS 高危**企业低代码框架

**受影响产品：**YunaiV yudao-cloud（企业级低代码/管理系统框架）。

**影响：**涉及代码/配置问题，可能导致未授权访问或数据泄露，常见于Java/Spring Boot企业应用环境。

**热度原因：**VulDB/CNA在5月3日当天发布/更新；企业低代码平台在国内企业广泛使用；当日新鲜CVE，开发者关注度快速上升。

**修复建议：**升级到最新修复版本；审查并强化权限控制；代码审计输入验证；部署WAF保护后端服务。

### CVE-2026-5337：WordPress 前端文件相关漏洞（5月3日更新）

**CVSS 中高**WordPress生态

**受影响产品：**特定WordPress主题/插件（前端文件处理模块）。

**影响：**可能导致文件泄露或安全绕过，影响站点安全性，严重时可导致敏感配置或源码外泄。

**热度原因：**WPScan等安全工具5月3日更新记录；WordPress生态在全球中小站点中占据主导地位，安全社区关注持续。

**修复建议：**更新相关WordPress主题/插件；禁用不必要文件浏览功能；启用安全插件（如Wordfence）并定期扫描；限制文件上传类型和目录访问。

## 三、总体修复提醒

* **最高优先：**

  SGLang（AI推理框架，升级0.5.10+）和Yudao-cloud（企业框架，升级最新版本）。
* **WordPress用户：**

  立即检查主题/插件版本，禁用文件浏览，更新至最新安全版本。
* **通用防护：**

  启用自动更新和EDR监控；定期扫描资产；关注Tenable NVC和VulDB每日最新条目获取实时威胁情报。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

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