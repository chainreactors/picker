---
title: 思科预警，旧版IP电话存在严重RCE零日漏洞
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247545319&idx=3&sn=2db209002ce8351f85f3f4498b2c3b94&chksm=c1e9bdb6f69e34a02ff1e6915bc76b81a03bc6a87ee10fb8a31647c9bdc31dc64cec1ae67a77&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-08-13
fetch_date: 2025-10-06T18:07:23.368126
---

# 思科预警，旧版IP电话存在严重RCE零日漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogu58PSialfxlPibKRibrnETqPYSXBfamD2icTyLR1IckOu1tEiaicO3B7q10NcvZLnY9ViclJzT2N7fX7bMQ/0?wx_fmt=jpeg)

# 思科预警，旧版IP电话存在严重RCE零日漏洞

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogu58PSialfxlPibKRibrnETqPYemZuqvAZKsd2kolLhzRZWt7Sf3JiblxAK57PH8qz2Nwibo4xicdxpE4EA/640?wx_fmt=png&from=appmsg)

思科（Cisco）披露，其两款已终止服务的小型商务SPA 300和SPA 500系列IP电话中，基于Web的管理界面存在多个关键的远程代码执行零日漏洞。

目前思科没有为这些设备提供修复补丁，使用这些产品的用户需要转移使用更新的、仍在支持的型号上。

**1、五个漏洞详情**

思科披露了五个漏洞，其中三个被评为严重（CVSS v3.1评分：9.8），两个被归类为高严重性（CVSS v3.1评分：7.5）。

严重漏洞被跟踪为CVE-2024-20450、CVE-2024-20452和CVE-2024-20454。

这些缓冲区溢出漏洞允许未经身份验证的远程攻击者通过向目标设备发送特别构建的 HTTP请求，以root权限在底层操作系统上执行任意命令。

“如果成功利用此漏洞，攻击者可能会溢出内部缓冲区，并在根权限级别执行任意命令，”思科在公告中警告说。

两个高严重性漏洞是CVE-2024-20451和CVE-2024-20453。它们是由于对HTTP数据包的检查不充分引起的，这允许恶意数据包在受影响的设备上造成拒绝服务。

思科指出，这五个漏洞都会影响在SPA 300和SPA 500系列IP电话上运行的所有软件版本。无论电话配置如何，漏洞彼此独立，可以被单独利用。

**2、已终止服务**

根据思科公司的支持门户提供的信息，SPA 300产品最后一次销售给客户是在2019年2月，并且在三年后，即2022年2月，思科停止了对这个产品的技术支持。

对于SPA 500型号的产品，供应商在2020年6月1日这一天，既停止了对该型号硬件的销售，也结束了对它的技术支持。

值得注意的是，思科将继续为持有服务合同或特殊保修条款的客户保障SPA 500产品，直到2025年5月31日。

对于SPA 300产品，自2024年2月29日起，思科不再提供保障。

两者都不会获得安全更新，因此建议用户过渡到更新的受支持型号，例如Cisco IP Phone 8841或Cisco 6800系列的型号。

思科还提供技术迁移计划（TMP），允许客户以旧换新符合条件的产品并获得新设备的信用额度。

原文来源：E安全

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