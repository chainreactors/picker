---
title: 关于Joomla存在未授权访问漏洞的安全公告
url: https://mp.weixin.qq.com/s?__biz=MzU3ODM2NTg2Mg==&mid=2247493030&idx=1&sn=d854ee809c510d0e5ac627f6fe78ae04&chksm=fd74d56fca035c793aecbaf5f72db5c6861a041f6008e6806df77e7e686ec5eaac2b6f7832bc&scene=58&subscene=0#rd
source: CNVD漏洞平台
date: 2023-02-23
fetch_date: 2025-10-04T07:51:57.183242
---

# 关于Joomla存在未授权访问漏洞的安全公告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/pMINP9OQkbgovGKzPiaPOuvNmqeqCUg2gEzl5sVMBFicZhcfl7Kzn1CajmJCKAeCeibucjnq9QpOvjhB0LKlxQicCw/0?wx_fmt=jpeg)

# 关于Joomla存在未授权访问漏洞的安全公告

原创

CNVD

CNVD漏洞平台

安全公告编号:CNTA-2023-0005

2023年2月22日，国家信息安全漏洞共享平台（CNVD）收录了Joomla未授权访问漏洞（CNVD-2023-11024，对应CVE-2023-23752）。未经授权的攻击者可远程利用该漏洞获得服务器敏感信息。目前，该漏洞的利用细节和测试代码已公开，厂商已发布新版本完成修复。CNVD建议受影响的单位和用户立即升级到最新版本。

**一、漏洞情况分析**

Joomla是由Open Source
Matters开源组织研发和维护的知名内容管理系统（CMS），它使用PHP语言和MySQL数据库开发，兼容Linux、Windows、MacOSX等多种系统平台。

近日，Joomla官方发布安全公告，修复了Joomla未授权访问漏洞。由于Joomla对Web服务端点缺乏必要的访问限制，未经身份认证的攻击者，可以远程利用此漏洞访问服务器REST
API接口，造成服务器敏感信息泄露。

CNVD对该漏洞的综合评级为“高危”。

**二、漏洞影响范围**

漏洞影响的产品和版本：

4.0.0 <= Joomla
<= 4.2.7

**三、漏洞处置建议**

目前，Joomla官方已发布新版本修复该漏洞，CNVD建议受影响的单位和用户立即升级至4.2.8及以上版本：

https://downloads.joomla.org/

https://github.com/joomla/joomla-cms/releases/tag/4.2.8

感谢奇安信网神信息技术（北京）股份有限公司、深信服科技股份有限公司、杭州安恒信息技术股份有限公司和北京知道创宇信息技术股份有限公司为本报告提供的技术支持。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/pMINP9OQkbhv2uDwc7hNMH9gPUUt39C13bYw7EhIhmITpa6692RtN0xDyb4rTiaTpewIpuGUrD1Ckf1lCVStiaRg/0?wx_fmt=png)

CNVD漏洞平台

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/pMINP9OQkbhv2uDwc7hNMH9gPUUt39C13bYw7EhIhmITpa6692RtN0xDyb4rTiaTpewIpuGUrD1Ckf1lCVStiaRg/0?wx_fmt=png)

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