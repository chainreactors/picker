---
title: RzWeb（Rizin）：浏览器端的在线逆向工程平台
url: https://mp.weixin.qq.com/s/G8h_aZQdFbcgL5ZyXXbbmA
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:12:59.654182
---

# RzWeb（Rizin）：浏览器端的在线逆向工程平台

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicIMjlacwOvR2ibjsErkcmbiaJG04UPZM3GkicaOOU28Q5ULLJ0cWYPe9a5Wpe16yP3NrhlfMZPeNP1Nibia7rCbewFVmzXSh3hicLqW0/0?wx_fmt=jpeg)

# RzWeb（Rizin）：浏览器端的在线逆向工程平台

原创

网安武器库
网安武器库

网安武器库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[内网网络审计工具箱（大牛蛙版）](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486807&idx=1&sn=1b567845a716975b6e522377016aa681&scene=21#wechat_redirect)

·[Glato：GitLab CI/CD 流水线的渗透测试框架](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486813&idx=1&sn=7d6a9888840f5a5c20abcec44152c09e&scene=21#wechat_redirect)

·[近期你还有这些CTF比赛可以参加](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486793&idx=1&sn=cdb32a1bebeda8c4f670d3528be22d1d&scene=21#wechat_redirect)

·[HackerMind：三AI架构自集成MCP的链上对话智能渗透系统工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486640&idx=1&sn=19052c6dd7b1d73d9b8395857276042f&scene=21#wechat_redirect)

·[VulnRadar：集成多模块的Chrome浏览器安全渗透测试扩展](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486780&idx=1&sn=86e51f2d05c04ccb6ecf14104f50f99b&scene=21#wechat_redirect)

·[CTF和实战可用-文件上传漏洞检测专业工具：UploadRanger](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486761&idx=1&sn=ad09098ab205e45600339e0aa9dfa836&scene=21#wechat_redirect)

**背景分析**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLiaibtNSWbrRnibgBRiaibwVdfUlpeNMpAL00Kv3Utb5rZZ88jET1YTp55apiaZ9HwIuLTUWoCCEd7rDft5L1Ym5x5odnWziaWRJgqI8/640?wx_fmt=png&from=appmsg)

逆向工程分析过程中，传统工具往往需要本地安装配置复杂环境，且文件上传至服务器分析存在敏感数据泄露风险，不同操作系统间工具适配性也存在差异。`RzWeb`（`Rizin`）作为基于浏览器的逆向工程平台应运而生，依托`WebAssembly`技术在浏览器端运行，无需上传文件、无需服务器支持，也无需本地安装配置，可解决逆向分析中环境配置繁琐、数据隐私泄露、跨平台适配难等问题，满足安全研究、漏洞分析等场景下的二进制文件分析需求。

**安装介绍**

```
地址：https://rizin.pages.dev/
```

访问与启动步骤：

```
# 1. 打开任意现代浏览器（Chrome、Firefox、Edge等）
# 2. 在地址栏输入链接https://rizin.pages.dev/并访问
# 3. 页面加载完成后即可直接使用，无需本地安装任何软件或依赖
# 4. 支持离线缓存，首次加载后可在无网络环境下使用
```

页面加载完成后，若界面显示`Rizin`相关操作区域且支持文件拖放，说明可正常使用；该工具基于浏览器运行，无本地安装环节，无需验证安装依赖。

功能介绍

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicIZS7UzmpEDYmHqFl43h9bbYnGOQznuJIf1fACv3CTXDnlibpAJakUramoIvaLftBCuvRTKVHgxIU9UMsSEGc6qJPmQsMNHFngM/640?wx_fmt=png&from=appmsg)

反汇编功能可将二进制文件的机器码转换为可读的汇编代码，支持语法高亮显示，帮助用户分析程序的执行逻辑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJMxHrofdXudRTia2tYicUw6Iibkqlia03uZP3SQPiaAq1kiaWicsGKZSn5jUk9xF5opPzibFmibfb6icTvta05HbUcUPbGCIZTKYAaiaMEWQ/640?wx_fmt=png&from=appmsg)

控制流程图功能可可视化展示二进制文件的功能结构，清晰呈现程序各部分的执行流程与逻辑分支，帮助用户快速理解程序架构

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJvpnyF3AJNfK2k0TAjHdDzIXia1a73qhcZ6Tq4ubEO2XsibOic9OE6vTcawialpnGVa2ic2fQ84VyszBJY5FGr9HOjpWWibnNMZ8czU/640?wx_fmt=png&from=appmsg)

十六进制转储功能可展示二进制文件的原始字节数据，支持对原始字节的查看与检查，便于用户分析文件的底层数据结构

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLgdA6M4Vkdm2AVMHFe4daNUcJSUibqdIjlcUr5BicpDGfStuNOdhx66UtSoDSx3WhHWjpYJHlag1q49NMBGrkPtBWaUlWAlibh3w/640?wx_fmt=png&from=appmsg)

字符串提取功能可从二进制文件中自动提取所有可读字符串，帮助用户快速定位文件中的关键信息，如路径、函数名、常量等

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

网安武器库

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

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