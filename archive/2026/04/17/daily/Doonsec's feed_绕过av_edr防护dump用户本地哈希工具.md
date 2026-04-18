---
title: 绕过av/edr防护dump用户本地哈希工具
url: https://mp.weixin.qq.com/s/jiNALhn3wEPyCTcFIJHGDQ
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:31:02.361885
---

# 绕过av/edr防护dump用户本地哈希工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icm4tzB0NhkjotXiaqHDWBWZibbBic3euEvia8SEG62HRKwFIhaSib85Dyia4tdxbrZD74guShY5N2jHLB9qGdtoyffdEtzqO8iaq2faQISyjH06Q7E/0?wx_fmt=jpeg)

# 绕过av/edr防护dump用户本地哈希工具

frkngksl
frkngksl

词不达意安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 声明本文所涉及的技术、思路和工具仅用于安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统等目的，一切后果由使用者自行承担，禁止用于任何非法渗透测试，以及无授权违法测试，请遵守中华人民共和国网络安全法。

### SilentNimvest

日常上网冲浪，发现了这个项目：
https://github.com/frkngksl/SilentNimvest
作用是导出本地用户的哈希值、缓存的域登录信息、LSA 密钥。看了下介绍，主打一个规避绕过AV/EDR，对于我们后渗透实战很有价值了，拿到哈希解出密码继续横向攻击。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0Nhkgw7pWos7CUpXcrqsVAL5A0Fy1BDP06mTI7O3XulfibDNTy02SzBQpwCkK9xJOibTBUic0Z7NE6KmaX4klV7IibAdtyluWjPWeNN9s/640?wx_fmt=png&from=appmsg)

### 免杀绕过

该项目nim语言编写编译完成后，放在360环境测试下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0NhkhIEZhKraWf8ic8QnGAB9icmMMj3Y9rNrWDKSPfZia0iaiaJYDIXVnLxquEJqkdyNXvPjfaodvMwpbWrA3XK9mrW5BLiaKN7bpA988Mc/640?wx_fmt=png&from=appmsg)

落地下就被360秒了

![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkhvIMFUnBw0lGHCIRCEOpeZJgKVlmiaW69oDsNPM4GWeRcdg80ibc5IKGgxszvicwKKuzJgwlyo0zyhDibgPQpskl4IRvJJ6uC1cgI/640?wx_fmt=png&from=appmsg)

直接用我的SplitRun工具生成分离免杀

![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0Nhkjw0aVfxQIeenZic4S4j4Hf9OWkiazDiaBicPywU3nJjJtUGjwl578H93XLG5UW8Z9Gib4DCRoFh7gJDAjyuKDqic8jo8vON8MWVjrwA/640?wx_fmt=png&from=appmsg)360扫描
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0NhkjFhfmXLt2mZcpMmYf9Qib4QHibl91Cnlnm1AcIJ4d1dLU845YBNM5xgGHuENbSlFpD2RqgPwZp22W86wUgGRgIyA4WSJ6q26dPc/640?wx_fmt=png&from=appmsg)

工具教程：
https://www.bilibili.com/video/BV1yHQPBLEuy/

### 导出哈希规避效果

360合金开启

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icm4tzB0NhkhrictL20JiaOtf3VDSiaEWO7ZlLeDM3WxxxqImtbPCtgzUjKU5jicno4yo5nPBPpmwFmoJicEgccSZsedPF3sXKDVqhaaj7pwYurus/640?wx_fmt=png&from=appmsg)卡巴斯基企业版
![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0NhkhRFF48kGpk426hPwMdr9Kd5aeIa9FM5p8WlIDhNJuEG1a3vnlLXaicQIvCVMxCTrkYpqNtzGH1Zj5dLaNBASfVO5iaVJEIjKNMI/640?wx_fmt=png&from=appmsg)

Bitdefender企业版

![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0Nhkhrjsx7wf0lkibbVwQVP3hPRSygfYJ3y4ddKsGVib6ibwQ4EpibxdHetyRVGzzBVFa76icQx7TIIdjf35DIwdjzCgRwUkgLN1g7fCms/640?wx_fmt=png&from=appmsg)

### 纷传介绍

工具文件加入纷传获取，圈子专注红队终端安全对抗、社工钓鱼、免杀冲锋马、内网/域渗透。

![](https://mmbiz.qpic.cn/mmbiz_png/icm4tzB0Nhkia3SBpTrd4fWBvfocibWRM5ORvMDppNtvQsoTXITBvqngk3oyJ1QPXz6YW9BpmZGNEfvj6VFibQ2LrO985l1jHBBUj75cBa1z7A4/640?wx_fmt=png&from=appmsg)

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
* •白影(whiteShadow)自动化白加黑免杀工具v2.0
* •Windows恶意软件常见API一览（PDF）
* •Maldev Academy 恶意软件开发完整课程（源码+VM镜像）
* •SplitRun一款exe免杀工具v1.0

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