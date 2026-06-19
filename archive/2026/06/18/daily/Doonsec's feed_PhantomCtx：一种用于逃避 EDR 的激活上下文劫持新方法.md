---
title: PhantomCtx：一种用于逃避 EDR 的激活上下文劫持新方法
url: https://mp.weixin.qq.com/s/ZhAgr31ND0GaSbZIeGPcXQ
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:05:49.632946
---

# PhantomCtx：一种用于逃避 EDR 的激活上下文劫持新方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icm4tzB0NhkjSuM3A7oOJF3JmAvARicjg8Un3VSaricJ9DhCbRWKMlR8qEsAictIKrqE5DRV9X169ZqzKmdfmia8icSZKZ6NcFiaJdIbes3t3GDhPM/0?wx_fmt=jpeg)

# PhantomCtx：一种用于逃避 EDR 的激活上下文劫持新方法

r3xmax
r3xmax

词不达意安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### 什么是 PhantomCtx

PhantomCtx 是一款能够自动劫持激活上下文的工具，其目的是将任意 DLL 加载到绝大多数已签名的可执行文件中（例如 Microsoft、Adobe、Mozilla）。

该加载器被视为传统 DLL 劫持和侧加载技术的现代替代方案：与传统方法需要在目标系统上找到已签名的易受攻击的二进制文件，或者依赖于 HijackLibs 等页面上列出的已知易受攻击的 Microsoft 二进制文件（这些文件通常会受到监控）不同，该工具不需要特定的易受 DLL 劫持的二进制文件。

只要目标可执行文件通过其导入地址表 (IAT) 导入 DLL（几乎涵盖系统上的所有二进制文件），它就是 PhantomCtx 的有效目标。

![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkgpCbIZgXnibk4unfuwDpcInOEib5pYKqPJwLPyM6fCIArocdgUgWiavEPyx8JymjFILovF4H9btLazF8J6hcb3kmS18dDzUjOuibs/640?wx_fmt=png&from=appmsg)Elastic Cloud XDR，没有触发任何警报
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0Nhkj76V8XQrgL281GjpgZgMibLXzMGS5g7Bq89nE47ibbnHFjjZbgnBeMyQPGhvhZBOOJUmEKARMTm2hDJaicNXYUJt6er5xWJ4icupA/640?wx_fmt=png&from=appmsg)

### 下载

Github地址：
https://github.com/r3xmax/PhantomCtx

文章：
https://rexmax.dev/posts/phantomctx-new-approach-to-activation-context-hijacking-for-edr-evasion/

### 纷传介绍

![](https://mmbiz.qpic.cn/mmbiz_jpg/icm4tzB0Nhkgc3uvkBIMzv5VQ4sD7IaLbibE5y29KwxFDBibibwBtUfbiahflrBTU8yqt6lu4iaYFkqyrFqUFV6bssg4FlQlLTldVbclhkujA1c6Q/640?wx_fmt=jpeg&from=appmsg)

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
* •DarkTide内部版单文件免杀

### 重要声明

本文所涉及的技术、思路和工具仅用于本地靶场安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统等目的，一切后果由使用者自行承担，禁止用于任何非法渗透测试，以及无授权违法测试，请遵守中华人民共和国网络安全法。

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