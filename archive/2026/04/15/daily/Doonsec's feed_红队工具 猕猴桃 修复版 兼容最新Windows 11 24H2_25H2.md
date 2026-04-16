---
title: 红队工具 猕猴桃 修复版 兼容最新Windows 11 24H2/25H2
url: https://mp.weixin.qq.com/s/uT7H8Gm1RG4FtjHrcJRTSw
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:51:27.226336
---

# 红队工具 猕猴桃 修复版 兼容最新Windows 11 24H2/25H2

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9mJNQIzib3Q2q28K4f0lEWsUeWiaiaIv0TLhjYw6b7icH3zNbo4UhHJ8ib7dewkWcIRFrefmZ3V8h0WdpPiaQbvpGl5sNNgrDprbQfLR4DuoFrkqA/0?wx_fmt=jpeg)

# 红队工具 猕猴桃 修复版 兼容最新Windows 11 24H2/25H2

原创

JunYi
JunYi

毅心安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 内网渗透 猕猴桃 修复版 兼容最新Windows 11 24H2/25H2

安全研究员 @0xIr0h 通过对比 23H2 和 24H2 的 lsasrv.dll 符号文件（PDB）和反汇编代码，找到了新版本中管理登录会话的函数。

### 核心步骤：

1、定位关键函数： 在 lsasrv.dll 中寻找初始化或操作登录会话的函数（通常是 LsaSrvInitialize 或相关子函数）。

2、提取新特征码： @0xIr0h 确定了在 24H2/25H2 中定位 LogonSessionList 所需的新指令序列。这些序列通常涉及 lea（取地址）或 mov 等汇编指令，用于指向全局变量。

3、更新特征码表： 将这些新的 16 进制特征码添加到 Mimikatz 源代码的 kuhl\_m\_sekurlsa\_utils\_libraries 结构体中，使其能够识别新版本的系统构架。

通过 @0xIr0h 的修复，安全人员可以在最新的 Windows 11 预览版和正式版中重新使用 sekurlsa::logonpasswords。

### 使用效果

![](https://mmbiz.qpic.cn/mmbiz_jpg/9mJNQIzib3Q3E282FPLCGALOEzBb9gfsuAUeYE8mlZ4JnDT7tatKErK4f1SRXvwMCmHsxefokrfkHbdkvRSXqQAzfw21FibLXXUm2m2Se7F5w/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9mJNQIzib3Q1Pd26PjcQpUzACgJ8prZku6g0yhToVdDJh2CP4t8HdFv45ap3aQHDRn7ZWTsBO3ia1rxiaxpVnfGZj2wGJHNjI7b7nnNaAqWBLk/640?wx_fmt=webp&from=appmsg)

目标版本： Windows 11 专业版 24H2（内部版本 26100.8037），也在 25H2（内部版本 26200.8037）上验证过。

基准版本： Windows 11 22H2（内部版本 22621）

### Github

https://github.com/tanrikuluatahan/mimikatz

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/kzkqdAEDfXdKQzSjUmtSu9wlia18CPwm2k8nmiapVP04SYnXtghKHZquWfRclUc501UHoS9nOrAnBSuhKc1Y2nfw/0?wx_fmt=png)

毅心安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/kzkqdAEDfXdKQzSjUmtSu9wlia18CPwm2k8nmiapVP04SYnXtghKHZquWfRclUc501UHoS9nOrAnBSuhKc1Y2nfw/0?wx_fmt=png)

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