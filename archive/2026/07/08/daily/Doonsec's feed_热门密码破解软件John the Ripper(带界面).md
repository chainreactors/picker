---
title: 热门密码破解软件John the Ripper(带界面)
url: https://mp.weixin.qq.com/s/z0fKzFeeeAnL5UlV4uBumw
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T06:00:01.263231
---

# 热门密码破解软件John the Ripper(带界面)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6O1ydpI9PItP5CacbNWuSX5teIqCYvwSGfTNVUH29WeLn3HS9SCJpWfYWq8R0nAy5ft0BacI3zzAg4tAicAlBAQGliaSajD2I6DI/0?wx_fmt=jpeg)

# 热门密码破解软件John the Ripper(带界面)

原创

播风者
播风者

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PEtrnib92D2oK87RibXnQvpZCZAkK3atZrcptiahK7489EsepicU8jY03gBQqJmM9H50cKQRKIY72vFj6hjQLAHDmMSOQic6mQ150A/640?wx_fmt=png)
> **导语**：Johnny是一款跨平台开源图形化工具，作为热门密码破解软件John the Ripper的前端界面，降低了命令行操作门槛，让密码破解工作更加直观高效。当前版本为2.2。

![Johnny on Debian](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6OyejV1Hm3kyibVKyqPpTnicJEJoC150Kicj1X5iaeWK56MPlS4qqkWE2rScc70nfWAWbzWMrpLE4iaN7Vr8Hud1ruqd2hFp83QpsQw/640?wx_fmt=png "Johnny on Debian")

![Johnny on Ubuntu](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NesrYPVgrl0PjHuoHDdA42oW4s6FlhoM4lK2u1xPMy8gHxC0coZFmkU2ibU44d4SIibxC6N9CHicnQEQk1U4KEkkQKRgicSYQVHlk/640?wx_fmt=png "Johnny on Ubuntu")

![Johnny on Windows](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6OIhMbiaIbIrCqLGrMOOjSLaVmtyiacBS1mDyXHL6nwv9ic5upNdWPXFZxQ1pxpeAKPEibn9nIPloU28PWDFqqIiaxrcCzxM1YNeJVw/640?wx_fmt=png "Johnny on Windows")

---

## 一、项目简介

Johnny是John the Ripper的跨平台开源图形化前端（GUI），旨在简化和自动化密码破解流程。该项目由Shinnok提出并设计初稿，1.0版本由Aleksey Cherepanov在2012年Google Summer of Code期间实现，Mathieu Laprise在2015年GSoC中进一步推动其向2.0版本演进。

Johnny基于最强大且稳定的密码破解软件构建，同时支持John core/proper和jumbo版本，并在此基础上增加了桌面和GUI特有的功能，如改进的哈希和密码工作流、多种攻击模式和会话管理、可视化反馈和统计等。

## 二、主要功能

* **跨平台支持**：可在所有主流桌面平台构建和运行
* **强大后盾**：基于John the Ripper，支持JtR core和jumbo版本
* **攻击模式**：在简洁易用的界面中暴露最常用的JtR攻击模式和选项
* **哈希管理**：通过复杂过滤和选择简化密码/哈希管理和攻击结果查看
* **会话管理**：轻松定义新攻击，支持多个攻击会话管理
* **手动猜测**：通过Guess功能手动猜测密码
* **导出功能**：支持将密码表导出为CSV和冒号分隔的密码文件格式
* **导入功能**：通过2john功能导入多种加密或受密码保护的文件类型
* **多语言**：完全可翻译（目前支持英语和法语）

## 三、技术架构

Johnny构建于John the Ripper强大功能之上，继承了JtR在密码破解领域的核心能力：

* 支持多种哈希算法和加密格式
* 提供字典攻击、暴力攻击、混合攻击等多种模式
* 可利用GPU加速（如支持CUDA、OpenCL）
* 丰富的规则引擎支持自定义破解策略

## 四、下载与安装

当前版本：**2.2**

### Linux系统

Deb包（适用于Debian、Linux Mint、Ubuntu等）： 从官方GitHub releases下载.deb包后执行：

```
sudo dpkg -i johnny_*.deb
```

RPM包（适用于Fedora、Mageia、OpenSUSE等）： 从官方GitHub releases下载.rpm包后执行：

```
sudo rpm -i johnny-*.rpm
```

通用 tarball（手动安装或不安装）：

```
tar -xzf johnny-*.tar.gz
cd johnny
```

### 启动方式

Johnny目前没有系统菜单快捷方式，需在终端中输入以下命令启动：

```
johnny
```

## 五、源码获取

* **官方版本 2.2 源码**：GitHub仓库
* **开发版源码**（可能不稳定，不推荐）：同上仓库的dev分支

## 六、开发历史

Johnny项目始于2011年夏季安全计划，由Aleksey Cherepanov开发，Shinnok担任导师。2012年Aleksey Cherepanov在Google Summer of Code中继续开发，Frank Dittrich提供宝贵指导。2015年Mathieu Laprise在Google Summer of Code中进一步推动项目发展。

项目欢迎任何新贡献者通过GitHub参与，也欢迎通过john-dev或john-users邮件列表提供反馈。

## 七、相关资源

* John the Ripper官方网站
* Johnny项目GitHub
* Johnny更新日志
* 开发路线图

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6Puc8HNiaVFMibMWyXuRCjam9iat0x1rCpsp1iatD7HveaKn7X0FMG8AlYEYZQbWQjAzjbYJjgdDQYTxLsn3W66vehH9V8LV2z9XnE/640?wx_fmt=jpeg)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NJaWlOgGNt6DbZUibIWJ1CIhPX5Be64ePAYnHxT3Q4ThVqTKzMNiaQAYEjNaDlY9AthbLcIsrN4kPU1dqTEyiaAr3nialmYqMQh9o/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650618755&idx=1&sn=48e0a85464fb20c73b6f338928a8f850&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PKBzibJnbda0CMK3x60eudMe9sX2keic0hP6ibj4r1vchm8wLibbC2LvvlTBXKJbfDqhJQQKCpqDeWnsEoxndVribgNu4ZZGlZ5KEw/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650618776&idx=2&sn=a8fc65fd2a71822830022fc52d967bcd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6M31JAE8U9E4F6SwkHX5V8dmziavPTqVQc7JdOHLa6PRExE28VUOIRk770kATgFwwvMibngxp6OBwXhjHATN3lVheGl5dVrSiaVa4/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650618496&idx=1&sn=96ecdff99136258a4bf2cb156542311e&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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