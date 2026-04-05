---
title: 一次点击的代价：Lunar Spider 发动近两个月入侵完整分析
url: https://mp.weixin.qq.com/s/AZzxsYUmL5pSEwU0Gx5u6g
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:31:31.490742
---

# 一次点击的代价：Lunar Spider 发动近两个月入侵完整分析

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/PO9bjOzlHYAKojvsRdbdXmburolGMtm4kKibnQu1icUhznTUiaEhF5iceTJSbjwKHMqqx7YbZv9Jsiaib3iccujt69KmqItUw226bNicicMCUkVJeNtc/0?wx_fmt=jpeg)

# 一次点击的代价：Lunar Spider 发动近两个月入侵完整分析

bitbot
bitbot

Desync InfoSec

![]()

在小说阅读器中沉浸阅读

# 一次点击的代价：Lunar Spider 如何发动近两个月的入侵

来源：The DFIR Report · 2025-09-29 · 案例编号 #28761

📌 核心要点

* 攻击始于用户执行恶意 JavaScript 文件，该文件与 **Lunar Spider** 初始访问组织关联
* 恶意 JS 文件伪装为 W-9 税表，触发下载 MSI 包并部署 **Brute Ratel** DLL
* Brute Ratel 加载器将 **Latrodectus** 恶意软件注入 explorer.exe 进程
* 攻击者在第 3 天从 unattend.xml 文件中发现**明文域管理员凭据**
* 随后部署 **Cobalt Strike** 信标，使用 PsExec 横向移动到域控制器
* 攻击者在第 20 天使用 rclone 通过 FTP 外泄数据，持续约 10 小时
* 攻击者在环境中维持了**近两个月**的持久访问，但未部署勒索软件

## 一、案例概述

此次入侵发生在 2024 年 5 月，用户执行了一个恶意 JavaScript 文件。该文件此前已被 EclecticIQ 报告与 **Lunar Spider** 初始访问组织关联。这个严重混淆的 JS 文件伪装为合法税表，仅包含少量分散在大量规避填充内容中的可执行代码。

JavaScript payload 触发了 MSI 包的下载，该包使用 rundll32 部署 Brute Ratel DLL 文件。Brute Ratel 加载器随后将 Latrodectus 恶意软件注入 explorer.exe 进程，并与多个 CloudFlare 代理域名建立 C2 通信。Latrodectus payload 随后被观察到下载了窃密模块。

初始访问后约一小时，威胁行为者使用内置 Windows 命令（ipconfig、systeminfo、nltest、whoami）开始侦察活动。约六小时后，攻击者建立了 BackConnect 会话，启动了 VNC 远程访问功能。

在近两个月的入侵期间，攻击者使用了 **Latrodectus**、**Brute Ratel** 和 **Cobalt Strike** 三种 C2 框架，最终被清除出环境。尽管拥有对关键基础设施的全面访问权限，但**未观察到勒索软件部署**。

## 二、初始访问

感染始于执行 Latrodectus JavaScript 文件 `Form_W-9_Ver-i40_53b043910-86g91352u7972-6495q3.js`。该恶意软件于 2024 年 5 月 9 日首次上传到 VirusTotal，在 **Operation Endgame**（2024 年 5 月 27-29 日，执法部门摧毁多个僵尸网络）之前。

![](https://mmbiz.qpic.cn/mmbiz_png/PO9bjOzlHYAYHseSEtOOngiafpa3UsbFUn3ZK1FmAPcS0ribh29V0Jswnn4Mp1XAtKvdLoLlzKnEZxFsWlRxh56DbUcF0fgQhRiavz0LpFbH5U/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

Desync InfoSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

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