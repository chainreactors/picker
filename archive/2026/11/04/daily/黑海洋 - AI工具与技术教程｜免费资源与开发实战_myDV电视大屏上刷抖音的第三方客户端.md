---
title: myDV电视大屏上刷抖音的第三方客户端
url: https://blog.upx8.com/myDV
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-11-04
fetch_date: 2026-11-05T08:43:44.884029
---

# myDV电视大屏上刷抖音的第三方客户端

[![黑海洋](https://blog.upx8.com/logo.webp)
黑海洋
WIKI](https://blog.upx8.com/)

[首页](https://blog.upx8.com/)
[资源](https://blog.upx8.com/Free)
[安全](https://blog.upx8.com/os_security)
[开发](https://blog.upx8.com/code)
[资讯](https://blog.upx8.com/news)
[关于](/about.html)

在线工具

[极

**极简文本**
*txt.upx8.com*](https://txt.upx8.com/)
[I

**IP查询**
*ip.upx8.com*](https://ip.upx8.com/)
[哈

**哈希计算**
*blog.upx8.com*](https://blog.upx8.com/app/bs64/#hash)
[U

**USTD交易查询**
*18u.in*](https://18u.in)
[三

**三角洲辅助站**
*sjz.upx8.com*](https://sjz.upx8.com/)
[开

**开发者工具箱**
*tools.upx8.com*](https://tools.upx8.com/)
[晴

**晴空图床**
*tp.776161.xyz*](https://tp.776161.xyz/)

[首页](https://blog.upx8.com)
/
[资源](https://blog.upx8.com/Free)
/
myDV电视大屏上刷抖音的第三方客户端

# myDV电视大屏上刷抖音的第三方客户端

[资源](https://blog.upx8.com/Free)
11-04
·
约 3 分钟
·
黑海洋
·

4,557

刷抖音已经是很多人的日常，但手机屏幕终究太小，窝在沙发上用电视大屏看才够爽。抖音官方没有电视版，myDV 补上了这个空缺：一款专为电视打造的**抖音第三方客户端**，为电视遥控器操作量身定制，躺着就能大屏刷视频。

![项目主页 my Debug Video TV，开源协议 GPL-3.0，要求 Android 8.0+](https://i0.wp.com/cdn.skyimg.net/up/2026/11/4/475ddcb57d85d87703234a6b1d6d3f2f.webp)

## 三大核心功能

* **刷视频**：首页推荐流，遥控器上下键切换。
* **看直播**：查看已关注作者的直播。
* **搜索**：支持视频、用户、直播分块展示，还有热搜榜和虚拟键盘。

![首页视频流：顶栏为首页/直播/搜索/用户/设置，支持弹幕](https://i0.wp.com/cdn.skyimg.net/up/2026/11/4/1e56ccfdaf4da5f762012e3d33cc401b.webp)

## 遥控器怎么操作

| 按键 | 作用 |
| --- | --- |
| 上下键 | 切换上/下一个视频 |
| 确定键 | 显示 / 隐藏视频详情 |
| 长按菜单键 | 弹出选项：弹幕开关、分辨率切换、倍速播放、查看主页等 |
| 左右键 | 调整视频进度 |
| 返回键 | 回到导航栏 |

![搜索页：屏幕虚拟键盘，附大家都在搜与热搜榜](https://i0.wp.com/cdn.skyimg.net/up/2026/11/4/9cdbaafb757edec394d992abce74501e.webp)

![播放菜单：弹幕开关、画质切换（自动/1080P/720P/480P）、0.5x~3x 倍速、查看发布者主页](https://i0.wp.com/cdn.skyimg.net/up/2026/11/4/6784c1ff812f88194d1d639c0e201348.webp)

## 登录：Cookie 填写是关键

抖音没有开放公开 API，myDV 通过 **Cookie** 登录你的账号。Cookie 从抖音网页端获取：

![设置页认证配置：内置 Cookie 获取步骤说明](https://i0.wp.com/cdn.skyimg.net/up/2026/11/4/0b44a6a215fbf720b1065933ed821590.webp)

1. 电脑浏览器打开 douyin.com 并登录。
2. 按 `F12` 打开开发者工具。
3. 在 Network 标签中找到任意请求。
4. 复制 Request Headers 中的 Cookie 值（如果显示的是预检请求，改用浏览器插件提取 Cookie）。
5. 粘贴到 myDV 设置中的 Cookie 输入框。

两点提醒：

* **Cookie 等同于账号的临时通行证**，别截图外发、别分享给别人，用在自己设备上就好。
* Cookie 有有效期，哪天刷着刷着变成未登录状态，按上面步骤重新提取一份即可。

## 实际体验与近期更新

原作者体验后评价：遥控器操作确实方便，但部分视频刷起来会卡，还需要优化。作为目前少有的专为遥控器开发的抖音第三方版本，值得电视盒子用户一试。

**v2.3.42（当前版本）**

* 修复小组件加载在 DE 上下文设备中触发应用闪退的问题。

**近期版本主要更新**

* 修复部分电视点「退出」后黑屏不退、要再按一次返回才离场的问题。
* 全页面支持预测性返回手势；支持双屏和折叠屏界面；新增桌面小组件。
* 播放器新增 GLSurfaceView 渲染方式，可修复部分电视盒子 SDR 画面发白（默认仍为 SurfaceView）。
* 支持扫码登录（依赖 WebView，加载耗时长，部分设备不可用）。
* 修复手动推送 Cookie 页面在开启 Wi-Fi Direct 的电视上显示 p2p0 地址、手机访问不到的问题。
* 车机方控/电视媒体键经 MediaSession 接收，上一曲/下一曲切换视频。
* 修复评论区加载更多时崩溃、倍速播放背景音失真、换页黑闪等多个稳定性问题。
* 设置新增「画面边缘绿条修复」选项，搜索页支持系统语音搜索。

## 下载地址

[迅雷网盘](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4ueHVubGVpLmNvbS9zL1ZPdFN6VDNQNFd5OVdKdjZiV24zekxjbUExP3B3ZD14OXZj)（提取码 x9vc）[夸克网盘](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4ucXVhcmsuY24vcy81Zjc2ZjhkZWRhOTQ)     [百度网盘](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4uYmFpZHUuY29tL3MvMWlTWlZZOG5vV0FPMDBaUWZNMm1BOUE_cHdkPWNuejg)（提取码 cnz8）

## 几点说明

* **这是非官方客户端**，接口与登录方式依赖社区维护，功能变化以项目更新为准。
* 部分视频卡顿与设备性能、网络和接口状态有关，遇到时先排查网络，或等待版本更新。
* 电视盒子架构不一，APK 按设备选择对应版本，不确定就选 al

收藏

分享

报告错误

分享这篇文章

微信扫一扫

在手机上继续阅读

复制

扫码后直接打开这一页

[下载](https://blog.upx8.com/tag/%E4%B8%8B%E8%BD%BD/)
[工具](https://blog.upx8.com/tag/%E5%B7%A5%E5%85%B7/)
[视频](https://blog.upx8.com/tag/%E8%A7%86%E9%A2%91/)
[软件](https://blog.upx8.com/tag/%E8%BD%AF%E4%BB%B6/)
[AI](https://blog.upx8.com/tag/AI/)

[上一篇
红果TV电视大屏上看红果短剧和漫剧](https://blog.upx8.com/TV)
[下一篇
用 Docker 自建在线阅读服务：把 Legado 书源搬进 Reader](https://blog.upx8.com/Docker-Legado-Reader)

## 相关文档

* [红果TV电视大屏上看红果短剧和漫剧
  11-04](https://blog.upx8.com/TV)
* [迅雷下载地址修改工具下载 绿色版
  2014-09-02](https://blog.upx8.com/%E8%BF%85%E9%9B%B7%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80%E4%BF%AE%E6%94%B9%E5%B7%A5%E5%85%B7%E4%B8%8B%E8%BD%BD-%E7%BB%BF%E8%89%B2%E7%89%88)
* [疯狂外链4.5 upx8版
  2014-09-07](https://blog.upx8.com/%E7%96%AF%E7%8B%82%E5%A4%96%E9%93%BE4-5-upx8%E7%89%88)
* [战旗TV直播粉丝订阅软件
  2015-04-19](https://blog.upx8.com/%E6%88%98%E6%97%97tv%E7%9B%B4%E6%92%AD%E7%B2%89%E4%B8%9D%E8%AE%A2%E9%98%85%E8%BD%AF%E4%BB%B6)

## 评论与补充0

有问题或想补充的，写在下面 · 选中正文文字再点「报告错误」会自动引用

还没有评论。有疑问、补充，或者发现错字，都可以写在下面。

回复
取消

请勿填写此栏

就事论事，别发广告 · 正常评论
发表评论

本文目录

* [三大核心功能](#%E4%B8%89%E5%A4%A7%E6%A0%B8%E5%BF%83%E5%8A%9F%E8%83%BD)
* [遥控器怎么操作](#%E9%81%A5%E6%8E%A7%E5%99%A8%E6%80%8E%E4%B9%88%E6%93%8D%E4%BD%9C)
* [登录：Cookie 填写是关键](#%E7%99%BB%E5%BD%95%EF%BC%9Acookie-%E5%A1%AB%E5%86%99%E6%98%AF%E5%85%B3%E9%94%AE)
* [实际体验与近期更新](#%E5%AE%9E%E9%99%85%E4%BD%93%E9%AA%8C%E4%B8%8E%E8%BF%91%E6%9C%9F%E6%9B%B4%E6%96%B0)
* [下载地址](#%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80)
* [几点说明](#%E5%87%A0%E7%82%B9%E8%AF%B4%E6%98%8E)

[![黑海洋](https://blog.upx8.com/logo.webp)
**黑海洋**
WIKI](https://blog.upx8.com/)

黑海洋专注 AI 智能体、程序开发、开源工具与免费资源分享，提供保姆级部署教程、源码下载、云服务器运维与安全资讯。

分类

[资源](https://blog.upx8.com/Free)
[安全](https://blog.upx8.com/os_security)
[开发](https://blog.upx8.com/code)
[资讯](https://blog.upx8.com/news)

常用

[全部文档](https://blog.upx8.com/all.html)
[RSS 订阅](https://blog.upx8.com/feed/)
[RSS 评论](https://blog.upx8.com/feed/comments/)
[Sitemap](/sitemap.xml)

关于

[关于本站](/about.html)
[友情链接](https://blog.upx8.com/links.html)
[我的收藏](https://blog.upx8.com/library.html)

Copyright © 2026 黑海洋

[浙ICP备2021040518号-1](https://beian.miit.gov.cn)

站点正常

[首页](https://blog.upx8.com/)

分类

搜索
[收藏](https://blog.upx8.com/library.html)

**全部分类**

[资源
2013](https://blog.upx8.com/Free)
[安全
375](https://blog.upx8.com/os_security)
[开发
536](https://blog.upx8.com/code)
[资讯
1955](https://blog.upx8.com/news)
[全部文档](https://blog.upx8.com/all.html)