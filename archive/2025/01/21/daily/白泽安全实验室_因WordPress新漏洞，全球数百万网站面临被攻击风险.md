---
title: 因WordPress新漏洞，全球数百万网站面临被攻击风险
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492526&idx=1&sn=247ea35cbbd8abee04db13ecd2a84025&chksm=e90dc984de7a4092b4afde879c894da6d97959d30ded3154090dba8f222c4e460b1ee2a8519b&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2025-01-21
fetch_date: 2025-10-06T20:12:45.759118
---

# 因WordPress新漏洞，全球数百万网站面临被攻击风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 因WordPress新漏洞，全球数百万网站面临被攻击风险

BaizeSec

白泽安全实验室

### **一、事件背景概述**

W3 Total Cache是一款在WordPress社区中广受欢迎的性能优化插件，安装量超过一百万。它通过综合的缓存策略和优化技术，显著提升了网站的加载速度和用户体验，同时降低了服务器负载。然而，根据最新披露的信息，该插件存在一个严重的安全漏洞，可能使网站面临未经授权的数据访问和信息泄露的风险。近日，全球网络安全社区高度关注WordPress网站中广泛使用的W3 Total Cache插件被曝出严重安全漏洞（CVE-2024-12365）。这一漏洞可能导致数百万WordPress网站面临未经授权的信息泄露和被攻击风险，安全专家呼吁网站管理员尽快采取措施进行修复。

### **二、W3 Total Cache 插件介绍**

W3 Total Cache是一款功能强大的WordPress缓存插件，其核心理念是通过多种缓存技术（包括页面缓存、数据库缓存和对象缓存）减少服务器的重复计算和资源请求。它通过缓存网页的静态版本、数据库查询结果以及对象数据，将原本动态生成的内容转化为高效的静态资源，从而显著加快页面加载速度。此外，该插件还支持对CSS、JavaScript和HTML文件的压缩和精简，进一步优化资源加载速度，并通过延迟加载技术减少不必要的资源请求。为了实现全球范围内的快速分发，W3 Total Cache提供了与多种CDN服务的集成选项，允许用户将静态资源托管到CDN上，进一步降低服务器负载并提高用户体验。它还通过优化浏览器缓存策略，减少不必要的重复请求，进一步提升了网站的整体性能。凭借其灵活的配置选项，W3 Total Cache能够满足从初学者到专业开发者的需求，是许多高流量网站和需要全球快速分发的平台的首选性能优化工具。

### **三、漏洞分析**

根据CVE官方记录（CVE-2024-12365），该漏洞的CVSS评分为8.5，属于高危漏洞。漏洞源于W3 Total Cache插件在版本2.8.1及以下版本中存在一个权限检查缺失问题。具体而言，is\_w3tc\_admin\_page函数未对用户权限进行充分验证，导致经过身份验证的攻击者（如订阅者级别或更高权限的用户）可以获取插件的nonce值，并执行未经授权的操作。这可能引发信息泄露、服务计划限制被恶意消耗，甚至允许攻击者向任意位置发起网络请求，从而查询内部服务信息，包括云应用的实例元数据。

### **四、影响范围与修复建议**

据安全专家估计，全球有数十万甚至数百万WordPress网站可能受到该漏洞的影响。尽管W3 Total Cache插件的开发者已于2024年10月23日发布了修复该漏洞的2.8.2版本，但目前仍有大量网站尚未升级至最新版本，这使得它们仍然处于潜在攻击的风险之中。安全专家呼吁所有使用W3 Total Cache插件的WordPress网站管理员尽快升级至2.8.2或更高版本，以修复该高危漏洞并保护网站免受未经授权的访问和信息泄露风险。同时，建议网站管理员定期检查插件和WordPress核心的安全更新，以确保网站的安全性。

参考链接：

https://securityaffairs.com/173219/security/w3-total-cache-wordpress-plugin-cve-2024-12365.html

https://www.cve.org/CVERecord?id=CVE-2024-12365

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

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