---
title: Unix CUPS 远程代码执行漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI5MzY2MzM0Mw==&mid=2247486358&idx=1&sn=aaa326ccbda26617b134607032873818&chksm=ec6fec96db186580a977e00197d6d466c3106efd5efd42c98d42b8e177b4c6afdd0fa1f9fe5c&scene=58&subscene=0#rd
source: 阿里云应急响应
date: 2024-09-28
fetch_date: 2025-10-06T18:27:36.587192
---

# Unix CUPS 远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fwNqC4xHXIoNX5wvKBGTMqfgAMgZbqFAo9ddjAl4fzlPT6aJKf8C2ibCicdBFGGGA7NhvhJjQETOibzo1qZpHALNQ/0?wx_fmt=jpeg)

# Unix CUPS 远程代码执行漏洞

风险通告

阿里云应急响应

2024年9月27日，互联网上披露 Unix CUPS 远程代码执行漏洞详情。

01

风险描述

CUPS（Common UNIX Printing System，通用Unix打印系统）是一个打印系统，它主要是使用 IPP（Internet Printing Protocol）等协议来管理打印工作及队列。

2024年9月27日，互联网上披露 Unix CUPS 远程代码执行详情，利用链涉及多个CVE（CVE-2024-47176/CVE-2024-47076/CVE-2024-47175/CVE-2024-47177等）。当cups-browsed进程监听（默认631端口）接收UDP数据包时，攻击者可构造恶意请求，在无需认证的情况下可能在受害者机器上执行任意命令，控制服务器。漏洞实际是否可利用和触发需要依赖具体环境（例如存在打印任务等）。

02

风险评级

Unix CUPS 远程代码执行漏洞 高危

03

初步影响范围

CVE-2024-47176 cups-browsed <= 2.0.1

CVE-2024-47076 libcupsfilters <= 2.1b1

CVE-2024-47175 libppd <= 2.1b1

CVE-2024-47177 cups-filters <= 2.0.1

由于各软件方以及各操作系统发行方尚未发布新版本，具体影响范围仍可能有变动

04

安全建议

1、若无需要，建议关闭 cups-browsed 进程。

2、利用安全组设置 cups-browsed 进程端口（默认631）禁止接收UDP数据包，或者仅对可信地址开放。

3、截止目前尚未有安全更新版本或补丁正式发布，待发布后建议升级更新至最新版本。

05

相关链接

https://www.evilsocket.net/2024/09/26/Attacking-UNIX-systems-via-CUPS-Part-I/

https://github.com/OpenPrinting/cups-browsed/security/advisories/GHSA-rj88-6mr5-rcw8

https://github.com/OpenPrinting/libcupsfilters/security/advisories/GHSA-w63j-6g73-wmg5

https://github.com/OpenPrinting/libppd/security/advisories/GHSA-7xfx-47qg-grp6

https://github.com/OpenPrinting/cups-filters/security/advisories/GHSA-p9rh-jxmq-gq47

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/fwNqC4xHXIqM8ZJsq2Ja8gNicGZzA8O6q0lPfCQQw64mudJwf7CUtyApwibDT3iaP5GDPxwtvRADE5H5BOsibYdWcg/0?wx_fmt=png)

阿里云应急响应

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fwNqC4xHXIqM8ZJsq2Ja8gNicGZzA8O6q0lPfCQQw64mudJwf7CUtyApwibDT3iaP5GDPxwtvRADE5H5BOsibYdWcg/0?wx_fmt=png)

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