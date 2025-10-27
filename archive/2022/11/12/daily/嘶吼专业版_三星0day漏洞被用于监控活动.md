---
title: 三星0day漏洞被用于监控活动
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247553649&idx=1&sn=d14f4ba92f85e724d9482ecdb12de308&chksm=e915c24bde624b5debd29ad82abb67d68f78d004a062f8f49d9ec433c271b264cc4323490b8f&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-11-12
fetch_date: 2025-10-03T22:32:49.522429
---

# 三星0day漏洞被用于监控活动

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD25EE2Y6iccNniaj67UxY0c9iaoWEO5Vo2ll7SdxPFs4jtVL2yxwIz3RtNA/0?wx_fmt=jpeg)

# 三星0day漏洞被用于监控活动

ang010ela

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

谷歌Project Zero研究人员发现有攻击者利用三星手机多个0day漏洞用于监控活动。

近日，谷歌Project Zero研究人员披露了三个三星手机0 day漏洞被监控公司用于监控活动，漏洞CVE编号为CVE-2021-25337、CVE-2021-25369、CVE-2021-25370：

CVE-2021-25337：该漏洞为三星手机设备剪贴板服务访问控制不当的问题，攻击者利用该漏洞可以让不可信的应用读写特定本地文件；

CVE-2021-25369：该漏洞为sec\_log文件的访问控制不当问题，会将敏感kernel信息暴露给用户空间；

CVE-2021-25370：该漏洞是dpu驱动中处理文件描述符的错误实现导致的，会引发内存破坏最终导致影响kernel。

谷歌研究人员指出监控公司使用的监控软件在利用这3个漏洞时漏洞尚未发布补丁，因此属于0 day漏洞。

该漏洞利用链是一个典型的不同攻击面的例子。漏洞利用链中的3个漏洞都位于设备厂商组件中，而非AOSP平台或Linux kernel中。而且其中2个漏洞都是逻辑和设计漏洞，而非内存安全漏洞。

研究人员分析认为，漏洞利用样本攻击的是运行kernel 4.14.113（Exynos SOC）的三星手机。而使用这种SOC的手机主要在欧洲和非洲销售。漏洞利用依赖的Mail GPU驱动和DPU驱动，都是针对基于Exynos的三星手机。

受影响的三星手机包括S10、A50、A51等。谷歌称这3个漏洞已于2021年3月被三星修复。

谷歌在安全公告中并未指出利用这3个三星手机漏洞进行监控的厂商名，但强调与其他攻击意大利和哈萨克斯坦安卓用户的攻击活动有相似之处。

由于三星在发布漏洞补丁时未说明漏洞利用的情况，因此建议使用相关设备的用户尽快检查是否安装补丁。

参考及来源：https://securityaffairs.co/wordpress/138302/hacking/surveillance-vendor-exploited-samsung-phone-zero-days.html

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2yKS6xK2QCicEDKgaicsDWhBsX8Uu2QDRpmLAkUoiawCu74Wtd9mU2s1wg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icicZgjAfeuUpqfbYYlEqWD2icwTaIE88HFq34ibb8D11BAIWHzWOCky6Fc3lcng5dhgDzDPgRhyx66Q/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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