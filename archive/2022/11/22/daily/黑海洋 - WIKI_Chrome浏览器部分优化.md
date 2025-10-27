---
title: Chrome浏览器部分优化
url: https://blog.upx8.com/3105
source: 黑海洋 - WIKI
date: 2022-11-22
fetch_date: 2025-10-03T23:24:14.664495
---

# Chrome浏览器部分优化

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Chrome浏览器部分优化

发布时间:
2022-11-21

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
13250

## Chrome浏览器离线版独立安装包下载：

* [Chrome浏览器离线版(国外)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS9pbnRsL3poLUNOL2Nocm9tZS8_c3RhbmRhbG9uZT0x)
* [Chrome浏览器离线版(国内)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZ29vZ2xlLmNuL2ludGwvemgtQ04vY2hyb21lLz9zdGFuZGFsb25lPTE)

## 开启 Chrome 浏览器高分辨率：

在启动图标 **属性 -> 目标** 后面添加：

```
--high-dpi-support=1 --force-device-scale-factor=1
```

## 取消 Google Chrome 浏览器隐藏网址栏中的 WWW

**注：78+版本中仅可通过安装 Suspicious Site Reporter 扩展解决。**
通过更改标记设置来停用Chrome 75 中的“网址截断”功能
在地址栏输入

```
chrome://flags/#omnibox-ui-hide-steady-state-url-trivial-subdomains
```

找到 `Omnibox UI Hide Steady-State URL Trivial Subdomains` 并禁用(设置为 `Disabled`)

## 取消 Chrome 由贵单位管理

打开注册表并找到路径：`计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome`
找到 `EnabledPlugins` 目录并删除，然后重启 Chrome 即可。

## 开启当前页面二维码共享（85+）

在地址栏输入

```
chrome://flags/#sharing-qr-code-generator
```

找到 `Enable sharing page via QR Code` 并禁用(设置为 `Enabled`)

## 开启多线程下载

在地址栏输入

```
chrome://flags/#enable-parallel-downloading
```

找到 `Parallel downloading` 并启用(设置为 `Enabled`)

## 开启悬停预览标签

在地址栏输入

```
chrome://flags/#tab-hover-cards
和
chrome://flags/#tab-hover-card-images
```

找到 `Tab Hover Cards` 和 `Tab Hover Card Images` 并启用(设置为 `Enabled`)

## 开启标签分组

在地址栏输入

```
chrome://flags/#tab-groups
```

找到 `Tab Groups` 并启用(设置为 `Enabled`)

## 预添加Global Media Controls按钮

在地址栏输入

```
chrome://flags/#global-media-controls
```

找到 `Global Media Controls` 并启用(设置为 `Enabled`)

## 开启 Chrome 浏览器 QUIC 特性

在地址栏输入

```
chrome://flags/#enable-quic
```

找到 `Experimental QUIC protocol` 项并开启(设置为 `Enabled`)

测试QUIC开启状态：
重新访问支持 QUIC 的站点，然后在浏览器中打开：`chrome://net-internals/#quic`
如果你看到了 QUIC sessins，则开启成功。
当然，你也可以给 Chrome 安装一个 HTTP/2 and SPDY indicator(An indicator button for HTTP/2, SPDY and QUIC support by each website) 更加直观的观察网站对 http/2 和 QUIC 的支持情况。

[取消回复](https://blog.upx8.com/3105#respond-post-3105)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")