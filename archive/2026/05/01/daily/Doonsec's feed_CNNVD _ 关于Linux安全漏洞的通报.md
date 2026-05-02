---
title: CNNVD | 关于Linux安全漏洞的通报
url: https://mp.weixin.qq.com/s/0p44OC5GNHQir6NvdZZjpQ
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:58:40.942391
---

# CNNVD | 关于Linux安全漏洞的通报

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/LJwWAbW20CiaP4aq0TlCmKyIOPN92za7hSa1EmicCOvibRiczlLQdPOQibicKfveq0Srd95LuwmCZ3Y3PlbicEWbqnrkvun1xdFCrAqxL3HgOgXbp4/0?wx_fmt=jpeg)

# CNNVD | 关于Linux安全漏洞的通报

中国信息安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

[![](https://mmbiz.qpic.cn/mmbiz_gif/LJwWAbW20CjVOCNTkiaXMLJZu5EN6FYrWq5QTWg6lH8oG45edcqias2emIIn4ByAKpZE9TnOUzMOozK18Oh9aR0yAKvdZq1iaXJ43JNAIfLAJY/640?wx_fmt=gif&from=appmsg)](https://cisat.cn/all/14915419?from_tag=1)

**漏洞情况**

近日，国家信息安全漏洞库（CNNVD）收到关于Linux kernel安全漏洞（CNNVD-202604-4496、CVE-2026-31431）情况的报送。成功利用漏洞的攻击者，可在目标系统获取root权限。Linux kernel多个版本均受此漏洞影响。目前，Linux官方已发布新版本修复了该漏洞，建议用户及时确认产品版本，尽快采取修补措施。

## 一 **漏洞介绍**

Linux kernel是美国Linux基金会的开源操作系统Linux所使用的内核。该漏洞源于内核加密子系统中的一处逻辑缺陷，攻击者可以利用AF\_ALG加密接口与splice()系统调用的组合，向任意可读文件的页缓存写入受控的4字节数据，从而篡改setuid程序，获取系统root权限。目前该漏洞利用代码和技术细节已公开。

该漏洞于4月22日被国家信息安全漏洞库采集并收录。近期，该漏洞利用代码和技术细节被公开，影响范围迅速扩大，建议用户尽快采取修补措施。

## 二 **危害影响**

Ubuntu 24.04 LTS及以下版本、Amazon Linux 2023及以下版本、Red Hat Enterprise Linux 10及以下版本、Red Hat Enterprise Linux 9及以下版本、Red Hat Enterprise Linux 8及以下版本、SUSE 16及以下版本、Debian/Arch/Fedora/Rocky/Alma/Oracle等同期内核版本均受此漏洞影响。

## 三 **修复建议**

目前，Linux官方已发布新版本修复了该漏洞，建议用户及时确认产品版本，尽快采取修补措施。参考链接：

https://www.kernel.org/

本通报由CNNVD技术支撑单位——奇安信网神信息技术（北京）股份有限公司、深信服科技股份有限公司、天翼云科技有限公司、北京时代新威信息技术有限公司、成都安美勤信息技术股份有限公司、新华三技术有限公司、远江盛邦安全科技集团股份有限公司、北京天融信网络安全技术有限公司、北京长亭科技有限公司、中乾建技术有限公司、广州纬安科技有限公司、中国银联股份有限公司、上海戎磐网络科技有限公司等技术支撑单位提供支持。

CNNVD将继续跟踪上述漏洞的相关情况，及时发布相关信息。如有需要，可与CNNVD联系。联系方式: cnnvd@itsec.gov.cn

（来源：CNNVD）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LJwWAbW20Ch90C0U9HhePiaDDzrHse2xBydmAsYOkj3g1vHTJECnOV5PmwENG3yNvVJibc15jVAgXMuNfzEd5iaoicqbsoS5dkrIs3LvEU5CIpQ/640?wx_fmt=png&from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_png/LJwWAbW20ChpyjG6chE3Tjw23vfFrb9ubWVVA4ERfMMn8cAX6iaVQPyynY3c0PZtjKTjvxGQhGjQuTG2Y4puJHVdgoWqiaZyNWGkaM35oUPGU/640?wx_fmt=png&from=appmsg)](https://cisat.cn/)

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