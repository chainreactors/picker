---
title: 开源工具推荐：S.H.I.T构石期刊无水印PDF下载器
url: https://mp.weixin.qq.com/s/1xQOYM5bIzzemkZdXH441A
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:27:15.755421
---

# 开源工具推荐：S.H.I.T构石期刊无水印PDF下载器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQo0ARCmTO6ia0axaHoXq3J8fu0U93bNSn74TWQy9DVj4nUCKvJEibgMBg2lvyTunTe3cfSlibP4Kh9ibp1JgMJ5wFgdYm8urR1EIWY/0?wx_fmt=jpeg)

# 开源工具推荐：S.H.I.T构石期刊无水印PDF下载器

原创

佚名
佚名

星宇Sec

![]()

在小说阅读器中沉浸阅读

> 仓库名：ShitJournalCrawler
> 地址：https://github.com/ThanatosXingYu/ShitJournalCrawler

最近在看社区里的整活论文时，我遇到一个非常现实的问题：
链接能刷到，资料却很难整理。文章分散在聊天记录、收藏夹和浏览器标签页里，想系统归档很费时间。

所以我做了一个开源小工具：**ShitJournalCrawler**。

它支持从文章链接自动提取元信息，下载 PDF，并按“标题 - 作者”命名，支持单篇和批量。

![](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQrN1gBicHwHr7MOcR4H0QWhNwYP45JnhBq1e4hGiaRZ5EsPHmS4icnlOIPgI4uGYfB3tB4sJAwm1FcrPgQuCicLib7a3RicibsKcmxKE8/640?wx_fmt=png&from=appmsg)

## 这个项目解决了什么？

1. 下载步骤太碎：点开、另存、改名，重复劳动很多。
2. 批量整理困难：几十个链接手工处理容易漏。
3. 文件管理混乱：命名不统一，后续检索困难。
4. 跨平台兼容问题：Windows/macOS 文件名规则不同，容易报错。

## 核心能力

1. 双站点支持：

* `shitspace.xyz`
* `shitjournal.org`

2. 双使用方式：

* 命令行（适合批量与自动化）
* GUI 桌面界面（适合日常点击使用）

3. 批量下载：

* 支持 TXT 多行链接读取并批量执行

4. 自动命名：

* 保存为 `标题 - 作者.pdf`

5. 代理支持：

* 支持 `HTTP/HTTPS/SOCKS5`
* 适配 `shitjournal.org` 等需要代理访问的场景

6. 任务控制：

* 支持“暂停/继续”
* 支持“强行停止”

7. 跨平台安全命名：

* 自动处理非法字符
* 自动处理 Windows 保留名（如 `CON/AUX/NUL/COM1...`）

## 快速开始

```
pip install -r requirements.txt

#GUI版
python3 article_downloader_gui.py

#CLI版
python3 article_downloader_cli.py --url "https://shitjournal.org/preprints/58fa9d57-4aa8-4f18-bad7-25a88b5b5a29" --proxy "socks5h://127.0.0.1:1080"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQpAtIhkh0icIRia7w7PAva5gwrT9noG6PXczpqhnr6EukiaXuNEnyUG37J24A6yOTJXQ1bRO8k2DtbTjGe0QMQEqZcLs3cMwEuQEM/640?wx_fmt=png&from=appmsg)

## 结尾

好工具不一定复杂，但一定能稳定帮你省时间。欢迎各位一起改进这个项目，好用的话可以点个Star

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/O57ZTjAp9KOL0JJPSBRFM8Y3GwpOwWSpDSvWexu4uJ40TCnMzqRM9JQOxx8KibqwUWUXdicAXohNyARfdV9agCFw/0?wx_fmt=png)

星宇Sec

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/O57ZTjAp9KOL0JJPSBRFM8Y3GwpOwWSpDSvWexu4uJ40TCnMzqRM9JQOxx8KibqwUWUXdicAXohNyARfdV9agCFw/0?wx_fmt=png)

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