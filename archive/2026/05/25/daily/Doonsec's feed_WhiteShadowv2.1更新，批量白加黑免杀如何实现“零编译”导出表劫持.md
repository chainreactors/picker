---
title: WhiteShadowv2.1更新，批量白加黑免杀如何实现“零编译”导出表劫持
url: https://mp.weixin.qq.com/s/eHyGcl_2mCbe3tzcjG5HPw
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:02:03.429922
---

# WhiteShadowv2.1更新，批量白加黑免杀如何实现“零编译”导出表劫持

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icm4tzB0NhkjxSntmDvpjicAJrBEGuUcXUboUrcibC6jHWSNETSClgan2soHeibjv8NmZRTkJLaQCoq6B9oRW9our8jTp4eC2uPHhkX8ea8Q5bg/0?wx_fmt=jpeg)

# WhiteShadowv2.1更新，批量白加黑免杀如何实现“零编译”导出表劫持

原创

词不达意
词不达意

词不达意安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### 白影

白影（WhiteShadow） 是一款白加黑免杀自动化生成工具，集成了目标扫描、DLL 导出表劫持（EAT Patch）、Shellcode 混淆载荷生成与批量部署能力，可一键生成多个免杀白加黑，旨在简化白加黑免杀测试的完整流程。
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkjAUBXYKYQUAVYyibdP70QtAupMWXvhKgNq2rS3F0ib9yrq2lNR5pbLwJEIxpX7qPe3XSFYrJ8cJwgQLjBIj5gwd92Lia0revdgwo/640?wx_fmt=png&from=appmsg)

### v2.1版本更新

本次更新了Patch模板，使用使用FNV1a hash 匹配 DLL 名，通过 hash 匹配函数名，使用NT函数。免杀效果更佳。
`payload.bin`模板常规分离执行。
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkgDiasicGGqrsrq7wZCbFpHGibj2OLzvd0segZdCiaibd7HpEc4DQ4hf3Z6PAiaobx5UaIV5h7XIYw2kM9Ox8UiaJKYDoiaCT3KcaGU4jM/640?wx_fmt=png&from=appmsg)`payload_sandbox.bin`模板带反沙箱，可绕过微步、天穹沙箱、virustotal、奇安信情报沙箱。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0Nhkhf1RibvE8DEXdTbxdK6ay1UrvdUBy2QqJcSPibUXOxaYCryga81icyjC8F7LWoUyUfPNQO0xNsSynAuscBBsDOwY65Ko6aH0mO6Y/640?wx_fmt=png&from=appmsg)使用教程：
https://www.bilibili.com/video/BV14nDeBeEZp/
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkjpTVnn0Eicl1yOA2ia8zmHK4Hkwty1ib6GWXROJiaB0Y67tyRncmtIEGuePy3hBCyOv5R8A2TxS6rdjw1pHOakY65awtvWjBDS6AQ/640?wx_fmt=png&from=appmsg)

### 规避效果

使用带反沙箱模板，生成白加黑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0Nhkg6iadAzfylMLPWHu5JLrVYYBNStIdl6Vk5rcib1LrnJMNTuq4JmPQP9wITNvILF630ictZgxLflpCMibBiauebIR2gAl0kxBia6KPAI/640?wx_fmt=png&from=appmsg)微步未查杀
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkiayN2GFhqHZib2Py1lkwkHCbhMS2vKqTq8hACf7jXAia9tLUwRm0WLl5KickoxaYWDmfTrrGHY031wKjqAReCkSz0YTko29EApLfQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0Nhkhl124OlkuiaiclYw5V6cFLpAmgBGXq6aCqHc2KoLRQ7Zcft48guO5fg4hlwLSShEnzAs7UiavGyNnwLUJV6FmjXHtE2xruUp6m5g/640?wx_fmt=png&from=appmsg)vt全绿
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0Nhkiaj7yzVXW2kAo0EtkuvYlnYac8C3EXSbgXOJicia38IeIPBPSKibMSicDTF4CmwRQSPTpicDyIoTd3icfkbrOiaQiabC6vQj6pf6FuJJtw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0NhkgOS438MJ6nfbZ4vN4cEibYTUqSjoY3n0UuBDqVUxV1syf25Xybu3QOYX7jN5zYkW8kMSGJEw4vmdWqjzXhYrrflzcTvngwicib8s/640?wx_fmt=png&from=appmsg)

### 使用场景

用于维权或者lnk钓鱼，使用的是分离免杀，支持跨路径运行。
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkgOn9ANYne45afuY6BjL0XMxAMicmQMusphEQXG0bwKztzM1SWe3zBMPOLHmiaH5fNIasDgicgCBsYUYM66IgIlicHKBxwjNZria1wg/640?wx_fmt=png&from=appmsg)
正常上线
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkiaXMxqC7BB9Mbvs6cPmvTpic9lIocZpaW7SBsDc2Ydzlz2ZddN3Y0hiclpHNyDFZGrU4QM4TT3QWeISyV56EC25SlR68P7Q4sRVc/640?wx_fmt=png&from=appmsg)

### 技术细节

相比传统转发 DLL导出函数白加黑，`需源码以及本地编译环境`，本工具在 PE 文件末尾追加独立可执行节，为每个导出函数生成相对跳转存根。核心优势：`无需编译 DLL，直接二进制修改DLL原始文件`，兼具兼容性与灵活性，免杀效果较佳。

### 纷传介绍

工具文件加入纷传获取，圈子专注红队终端安全对抗、社工钓鱼、免杀冲锋马、内网/域渗透。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0Nhkia6eQl94a02VtIdQeBDpclMLyleXfAZuAXtVJccRSpMErWGRBfrF1ddaI9xtVagDvfKMKCHrtsdnVVx8R8FAQTohea43vcAwCg/640?wx_fmt=png&from=appmsg)

### 圈子往期文件内容如下

* •冲锋马一键生成工具（一键生成免杀loader）
* •lnk文件一键生成工具（一键生成免杀钓鱼lnk文件）
* •bypass内存扫描插件（可绕过火绒、卡巴斯基等杀软内存扫描cs插件）
* •暗涌在线免杀平台（白文件patch免杀loader（分离、单文件）一键生成平台、支持反沙箱）
* •bypass任务计划工具（普通权限可添加、钓鱼快速免杀维权）
* •后渗透工具免杀（petobin，分离加载避免静态落地被秒）
* •BYOVD攻击一键结束赛门铁克进程
* •BinPatch免杀工具过国内主流杀软
* •白影(whiteShadow)自动化白加黑免杀工具v1.0
* •白影(whiteShadow)自动化白加黑免杀工具v2.1
* •Windows恶意软件常见API一览（PDF）
* •Maldev Academy 恶意软件开发完整课程（源码+VM镜像）
* •SplitRun一款exe免杀工具v1.0
* •cs4.5二开过火绒内存扫描
* •binfileBinder文件捆绑工具
* •RPC添加计划任务绕过360核晶

### 重要声明

本文所涉及的技术、思路和工具仅用于安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统等目的，一切后果由使用者自行承担，禁止用于任何非法渗透测试，以及无授权违法测试，请遵守中华人民共和国网络安全法。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/fQ2Bdxy1C5nUgyJyyHvl33mCCUsSib26NxViaiamWM5qOT7NAVcjlGAkGlkBYQF4j3dSHMprGM9aRTxjQ7ThqugRQ/0?wx_fmt=png)

词不达意安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fQ2Bdxy1C5nUgyJyyHvl33mCCUsSib26NxViaiamWM5qOT7NAVcjlGAkGlkBYQF4j3dSHMprGM9aRTxjQ7ThqugRQ/0?wx_fmt=png)

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