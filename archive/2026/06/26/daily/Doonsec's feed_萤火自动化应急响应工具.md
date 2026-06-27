---
title: 萤火自动化应急响应工具
url: https://mp.weixin.qq.com/s/WtfbtDnkA-uKDwl_OKkuUg
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:46:36.405302
---

# 萤火自动化应急响应工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVkKyAKalNsEH8rnyHTVHuENn89zzQKhsWUvQUhhNs00NzXLpibpZ7hibKibRglIsJWrVuoDQhGaX3dApdD0g2Fwg07qLZ5ibpR4lJo/0?wx_fmt=jpeg)

# 萤火自动化应急响应工具

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 686，阅读大约需 4 分钟

## 前言

`萤火应急响应工具` 是一个面向 Windows 主机应急响应场景的轻量化图形客户端。工具核心目标是把现场常用的账号、进程、网络、持久化、日志、文件取证、报告输出和辅助工具箱整合到一个可双击运行的客户端里，帮助应急人员快速完成“采集证据、提取异常、辅助处置、输出报告”的闭环。

项目地址：https://github.com/11firefly11/yinghuo

![7ae3a75eed794b901fca2bf901d32ab9.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkDkHmicUvibAOFhR0CzVwQeGwRGYtx2mBGqOzCp6aib26ZcGhsxIY2IM3vd2BmibO2Lg6eFib2e3TyibvIoLhxzuBsZSReGLmWo1RsE/640?from=appmsg "null")

7ae3a75eed794b901fca2bf901d32ab9.png

**注意：**
下载后，可能出现火绒的警告信息

警告是说 exe 中存在 Mimikatz 的特征值，因为工具存在检测系统中是否存在 Mimikatz 的功能，因为有相关的字符串，所以被警告了。

![45253022839e29def5ce91d951795fcb.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlxNJTmOaxFq1n8kHs3csowKV02hWpMbNFKDRxGRCSIFdev4I5NJgqPoib9kaUtL08pKENoNJ82N4RiadnCmb9iclrQF23MueZBOI/640?from=appmsg "null")

45253022839e29def5ce91d951795fcb.png

警告也只是说存在 hack 工具的特征，用不用见仁见智。

## 功能

除了应急响应工具正常具有的功能外，还添加了 AI 审计的功能，配置大模型的 URL 和 KEY 即可。
![5bfe4611a4332f61fe98f9044084954f.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlUcaWRYfgdyPHOKiazmhggLALKTteflvyFE3wichicAH1voELwfljN4R5TX3DNaV6vj9pkreU082InnOSDQBqacOfqNaaDrSfGhc/640?from=appmsg "null")

5bfe4611a4332f61fe98f9044084954f.png

### 核心能力

* • 单文件 Windows 客户端：`release\萤火应急响应工具.exe` 可直接双击运行，前端资源已嵌入 Go 后端。
* • 本地化采集：所有采集接口默认运行在本机 `127.0.0.1`，用于客户端 UI 调用。
* • 图形化模块：左侧为应急响应模块导航，右侧展示结构化摘要、异常发现、完整响应和处置入口。
* • 并发采集：智能排查任务按模块并行执行，完成后汇总结果并生成 HTML 报告。
* • 异常提取：从进程、外联、DNS、路由、启动项、计划任务、服务、WMI、日志、账号、文件落地等数据中提取可疑点。
* • 完整响应：每个模块都保留原始响应入口，便于复核命令输出和证据链。
* • 右键定位：网络连接、持久化、文件取证等包含路径的行支持右键选择“打开所在目录”。
* • 处置辅助：支持进程结束、计划任务删除、服务删除、注册表启动项删除、WMI 订阅删除、启动目录文件备份后删除。
* • AI 审计：可配置 BaseURL、API Key、模型，让外部大模型基于当前采集证据生成审计结论和 HTML 报告。
* • 应急工具箱：集成火绒剑、D 盾、Arthas 内存马查杀、银狐查杀、Everything 文件搜索等工具入口。

## 作者的其他工具

都挺好用的

* • 一个轮换代理的图形化代理池程序 https://github.com/11firefly11/fir-proxy
* • 通过谷歌语法自动收集敏感信息的信息搜集工具 https://github.com/11firefly11/Fir-Fetch
* • api 接口测试工具,包括 swagger 文档，asp 接口文档,wsdl 接口,wadl 接口,一键自动跑接口 https://github.com/11firefly11/ApiHunter

## 总结

https://github.com/11firefly11/yinghuo

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DuibU3GqmxVmRsdItbBVRKegNHicHQvAHDdZsGpLVU7touSU1AU1twHTfRjG3Vu5aUh0RnPPllfVUhs4qdWF5QYQ/640?wx_fmt=png&wxfrom=13)

声明：文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途给予盈利等目的，否则后果自行承担！

如有侵权烦请告知，我会立即删除并致歉。谢谢！

文章有疑问的，可以公众号发消息问我，或者留言。我每天都会看的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9zYJrD2VibHmqgf4y9Bqh9nDynW5fHvgbgkSGAfRboFPuCGjVoC3qMl6wlFucsx3Y3jt4gibQgZ6LxpoozE0Tdow/640?wx_fmt=png&wxfrom=13)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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