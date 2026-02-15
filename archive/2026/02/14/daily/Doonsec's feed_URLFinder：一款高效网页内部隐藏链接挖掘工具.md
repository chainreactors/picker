---
title: URLFinder：一款高效网页内部隐藏链接挖掘工具
url: https://mp.weixin.qq.com/s/4927bJZeZvbOAo41iBDwDQ
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:15:32.727913
---

# URLFinder：一款高效网页内部隐藏链接挖掘工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicJXibhSulv3ABaCbhFc8rxosNFzB063X6vk6k1AjCDyzxBmMXywEfMx2bDSWT0GH0xvVyO3fzViaUic23AQYxlhTzHHWu8oNWBdb8/0?wx_fmt=jpeg)

# URLFinder：一款高效网页内部隐藏链接挖掘工具

原创

网安武器库
网安武器库

网安武器库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[PCHunter：一款深度检测隐藏恶意代码的扫描工具（兼容win11）](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486351&idx=1&sn=5ad805f6aa58a79e2f21b777849db642&scene=21#wechat_redirect)

·[Web-SurvivalScan：用于快速验证资产存活的轻量化渗透测试扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486350&idx=1&sn=1a4559b375cda713d02d270ae121bc70&scene=21#wechat_redirect)

·[【已复现】最新版微信v4.1出现远程命令执行漏洞：one-click RCE on Linux WeChat](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486318&idx=1&sn=a39e4ceaadd2fcffea08ecdc48319fc9&scene=21#wechat_redirect)

·[xss\_scanner\_mix：一款自动化深度XSS漏洞扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486302&idx=1&sn=08544ff7835ce01fae582f677ad02a98&scene=21#wechat_redirect)

·[StegoScan：CTF自动化隐写识别和解密工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486301&idx=1&sn=704da2217fce796fe07611b66c3448d4&scene=21#wechat_redirect)

·[Metasploit Pro：可视化的metasploit渗透测试工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486276&idx=1&sn=44e00b0ee13437083417bd8c16f15f0c&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

项目介绍

URLFinder 是一款快速、全面、易用的页面信息提取工具，专为安全测试人员和开发人员设计，用于分析页面中的 JavaScript 与 URL，查找隐藏在其中的敏感信息或未授权 API 接口。

核心功能

1. 多模式抓取 ：

```
正常抓取（模式1）深入抓取（模式2）- URL深入一层，JS深入三层，防止抓偏安全深入抓取（模式3）- 过滤delete、remove等敏感路由
```

2. 强大的分析能力 ：

```
提取页面中的URL分析JavaScript文件中的链接查找敏感信息识别302跳转信息
```

3. 灵活的配置选项 ：

```
自定义User-Agent请求头添加Cookie设置代理配置线程数和超时时间通过YAML配置文件进行高级设置
```

4. 批量处理能力 ：

```
批量URL抓取（-f参数）统一结果处理（-ff参数）
```

5. 智能Fuzz测试 ：

```
对主域名下的404链接进行fuzz测试支持目录递减fuzz、2级目录组合fuzz、3级目录组合fuzz
```

6. 多格式导出 ：

```
CSV格式JSON格式HTML格式
```

工作流程

```
解析命令行参数或配置文件对目标URL进行抓取提取页面中的URL和JavaScript分析JavaScript中的链接验证提取的URL状态码对404链接进行fuzz测试（如果启用）整理和排序结果导出结果（如果指定）
```

优势

```
快速 ：多线程设计，默认50线程，可自定义全面 ：能抓取页面中的各种链接，包括JavaScript中的隐藏链接易用 ：命令行界面简洁明了，参数丰富灵活 ：支持多种抓取模式和配置选项智能 ：支持fuzz测试，能发现更多潜在链接跨平台 ：支持Windows、Linux、macOS等多种平台
```

使用场景

```
安全测试 ：发现网站中的未授权API接口和敏感信息网站审计 ：全面了解网站的URL结构和JavaScript中的链接渗透测试 ：作为渗透测试的前期信息收集工具开发辅助 ：帮助开发人员发现和管理网站中的链接
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

使用

Windows 系统

```
```go build -o URLFinder.exe```
```

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIuDGSicHIToQatLAnL6lWthZ3gXBP8jD8nK6JgXjIevyTloicibzhqroictYnnhOPDXNJUic1X1kf3pHMa1ibiaDTc32sicktEuBdNMlY/640?wx_fmt=png&from=appmsg)

执行完成后，当前目录会生成 URLFinder.exe 可执行文件。

 Linux 系统

```
```go build -o URLFinder```
```

单URL分析

```
```# 显示全部状态码URLFinder.exe -u http://www.baidu.com -s all -m 3# 只显示200和403状态码URLFinder.exe -u http://www.baidu.com -s 200,403 -m 3```
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLw3R5zzcHtx5v4NWiaqIEhZ1Njy1LicPPG1SuiaW5gJKX0F6zupNxmB59koc1aPXscqAupWDTibt2FpT2QqSoicBwAx8bZcS20kTBI/640?wx_fmt=png&from=appmsg)

批量URL处理

```
```# 结果分开保存，导出全部URLFinder.exe -s all -m 3 -f url.txt -o .# 结果统一保存URLFinder.exe -s all -m 3 -ff url.txt -o .```
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

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