---
title: CNNVD | 关于Apache OFBiz安全漏洞的通报
url: https://mp.weixin.qq.com/s?__biz=MzA5MzE5MDAzOA==&mid=2664230091&idx=5&sn=9950f25047c9a9cdb95f448751bcd9de&chksm=8b59ee32bc2e6724148267ee2381f2c8eb7cbce86d470cd00dc98942c246dde4f28c288844ba&scene=58&subscene=0#rd
source: 中国信息安全
date: 2024-11-21
fetch_date: 2025-10-06T19:16:40.246528
---

# CNNVD | 关于Apache OFBiz安全漏洞的通报

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1brjUjbpg5yu2TSIxOZGKwVpP76gQo2M0RxMDPtia7IOTm0JiccvFsPeKv8D4p90hSHvnWhevZVZVgtfkmZRFZ8w/0?wx_fmt=jpeg)

# CNNVD | 关于Apache OFBiz安全漏洞的通报

中国信息安全

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1brjUjbpg5yu2TSIxOZGKwVpP76gQo2MfX7ibtlhTaY67PtD9e3t07YjgazE1ND8gGfMic9TdW0piaXVT39EO8JKA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5yu2TSIxOZGKwVpP76gQo2MBicjiae1FlDHspS1icKI5DPchRAiabVUjGwSYgL2zre1AC5ZSd8VdOvFYQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1brjUjbpg5yu2TSIxOZGKwVpP76gQo2MfX7ibtlhTaY67PtD9e3t07YjgazE1ND8gGfMic9TdW0piaXVT39EO8JKA/640?wx_fmt=gif&from=appmsg)

**扫码订阅《中国信息安全》**

邮发代号 2-786

征订热线：010-82341063

**漏洞情况**

近日，国家信息安全漏洞库（CNNVD）收到关于Apache OFBiz安全漏洞(CNNVD-202411-2279、CVE-2024-47208)情况的报送。攻击者可以利用漏洞向目标发送恶意请求，通过服务端请求伪造的方式远程执行任意代码。Apache OFBiz 18.12.17以下版本受此漏洞影响。目前，Apache官方已发布新版本修复了该漏洞，建议用户及时确认产品版本，尽快采取修补措施。

## 一 **漏洞介绍**

Apache OFBiz是美国阿帕奇（Apache）基金会的一套企业资源计划（ERP）系统。该系统提供了一整套基于Java的Web应用程序组件和工具。漏洞源于程序对URL校验不严格，攻击者可通过构造恶意URL绕过校验并注入Groovy 表达式代码或触发服务器端请求伪造（SSRF）攻击，导致远程代码执行。

## 二 **危害影响**

Apache OFBiz 18.12.17以下版本受此漏洞影响。

## 三 **修复建议**

目前，Apache官方已发布新版本修复了该漏洞，建议用户及时确认产品版本，尽快采取修补措施。官方下载链接如下：

https://ofbiz.apache.org/download.html

本通报由CNNVD技术支撑单位——北京神州绿盟科技有限公司、深信服科技股份有限公司、西安交大捷普网络科技有限公司、数字新时代（山东）数据科技服务有限公司、安恒愿景（成都）信息科技有限公司、网宿科技股份有限公司等技术支撑单位提供支持。

CNNVD将继续跟踪上述漏洞的相关情况，及时发布相关信息。如有需要，可与CNNVD联系。

联系方式：cnnvd@itsec.gov.cn

（来源：CNNVD）

**分享网络安全知识 强化网络安全意识**

**欢迎关注《中国信息安全》杂志官方抖音号**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1brjUjbpg5yu2TSIxOZGKwVpP76gQo2M2F0GT7xiboynjVmCL5sOibaNp9GaEQxpA1KBZ2HZgaxXibOHG8Uz5ItDQ/640?wx_fmt=jpeg&from=appmsg)

**《中国信息安全》杂志倾力推荐**

**“企业成长计划”**

**点击下图 了解详情**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5yu2TSIxOZGKwVpP76gQo2MaMPZBQIhrrkFDVqDiaARRn9qEYJ7yUAry3G0jq1AEicuX6ichb2ATagiaw/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzA5MzE5MDAzOA==&mid=2664162643&idx=1&sn=fcc4f3a6047a0c2f4e4cc0181243ee18&chksm=8b5ee7aabc296ebc7c8c9b145f16e6a5cf8316143db3edce69f2a312214d50a00f65d775198d&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5xcg6pmGiagMsJTqnHObJGHSj6TEe6InbwlHLIxFVhPohvicQibAcuia5wDEoRISsAkUyYPUB06cU9mibw/0?wx_fmt=png)

中国信息安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5xcg6pmGiagMsJTqnHObJGHSj6TEe6InbwlHLIxFVhPohvicQibAcuia5wDEoRISsAkUyYPUB06cU9mibw/0?wx_fmt=png)

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