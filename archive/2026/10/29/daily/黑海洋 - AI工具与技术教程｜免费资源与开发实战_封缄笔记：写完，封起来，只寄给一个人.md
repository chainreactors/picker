---
title: 封缄笔记：写完，封起来，只寄给一个人
url: https://blog.upx8.com/10906
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-10-29
fetch_date: 2026-10-30T07:55:08.637638
---

# 封缄笔记：写完，封起来，只寄给一个人

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

[首页](https://blog.upx8.com)
/
[开发](https://blog.upx8.com/code)
/
封缄笔记：写完，封起来，只寄给一个人

# 封缄笔记：写完，封起来，只寄给一个人

[开发](https://blog.upx8.com/code)
10-30
·
约 3 分钟
·
黑海洋
·

3,333
·
[2 条评论](#comments)

![封缄笔记：写完，封起来，只寄给一个人](https://pic1.imgdb.cn/i/034oQ4tJTsDcQ1dren2e84.png)

> 一个能写字、能盖火漆、能生成一次性分享链接的笔记本。没有账号，没有关注，没有已读回执式的压迫感——只有一封信，和拆开它的那一下。

---

## 正文

我一直有个很小的需求，小到不值得为它装一个 App：**有些话，只想让一个人看到。**​

发朋友圈是公开的，发微信是永久的，写进备忘录又寄不出去。我想要的是介于两者之间的东西：像递一封信那样递出去，对方拆开才看得到，看完可以留着，也可以到期就没了。

所以有了「封缄」。

**封缄 · 写给一个人看的笔记：**[https://time-rings.app.workbuddy.host/?sharecode=IRYESUGT5Y](https://blog.upx8.com/go/aHR0cHM6Ly90aW1lLXJpbmdzLmFwcC53b3JrYnVkZHkuaG9zdC8_c2hhcmVjb2RlPUlSWUVTVUdUNVk)

### 它是一本笔记本，也是一枚蜡封

打开就是一本纸色的笔记本，横线信纸，宋体正文。不用注册，不用登录，左边是你的笔记，中间是纸，右边是你已经发出去的封缄。

写完之后，点纸上的「封起来」：

* 在封皮上写一句话（比如「写给十年后的自己」）
* 选一个期限：1 天、3 天、7 天、30 天，或者不限
* 可以再加一枚口令，也可以不加
* 选对方只能读，还是可以改

按「盖下蜡封」，你会看到一团蜡落下来、压开、回弹，然后得到一条链接。

### 对方看到的不是密码框，是一封信

这是我做这个产品最在意的一点。

拿到链接的人不会看到一个「请输入密码」的面板，而是一封盖着火漆的信：封皮上写着标题，旁边盖着一枚「剩 30 天」的印。点一下，蜡封先轻轻一震，中间裂开一道缝，然后整枚蜡分成两半飞出去，信纸才从下面浮上来。

整个过程不到两秒，但它让「打开一封信」这件事重新有了分量。

### 封缄之后

发出去不是结束：

* **到期自动作废**，链接打不开，页面上只留一句「这封已经过期，信纸留在这里」
* **随时可以收回**，收回后立刻失效
* **拆封回执**：被拆开过几次、最后一次是什么时候、从哪里
* **六位恢复码**：换设备、换浏览器，输入恢复码就能接上原来那本笔记本

我一直觉得，私密的话不该只有「公开」和「永久」两个选项。它应该有开始，也应该有结束。

### 适合谁

* 写给未来自己的信（默认那篇就是「写给十年后的自己」，你可以直接拆开看）
* 给家人的一段话，不想发在群里
* 给同事的交接说明，看完就失效
* 不想被任何人翻到的日记

### 技术与隐私

服务端是 Python 标准库加 SQLite，零第三方依赖；前端是原生 JS，没有框架。每位访客按照浏览器隔离，互不干扰，不需要账号体系；没有埋点，没有外部请求，数据只存在自己的服务器上。

那枚火漆是手写 SVG 画的，不是图片：蜡边用几个不同频率的正弦波叠出不规则的形状，字是三层叠出来的浮雕，所以放大也不糊，加载也不慢。

手机上也重新排过：顶栏收成三个按钮，笔记变成一条横滑的卡片，「已发出的封缄」改成从底部升起的抽屉，单手就能写完一封并盖下蜡封。

### 去拆一封

链接在这里，打开就是一本属于你的笔记本，里面放好了三篇示例和一封已经封好的信：

不用注册，点开就能用。想先看效果，就点右边那封「写给十年后的自己」下面的「拆封预览」——你会看到火漆裂开。

收藏

分享

报告错误

分享这篇文章

微信扫一扫

在手机上继续阅读

复制

扫码后直接打开这一页

[上一篇
群晖NAS遭大规模L0CK3D勒索病毒攻击（修复方案）](https://blog.upx8.com/%E7%BE%A4%E6%99%96NAS%E9%81%AD%E5%A4%A7%E8%A7%84%E6%A8%A1L0CK3D%E5%8B%92%E7%B4%A2%E7%97%85%E6%AF%92%E6%94%BB%E5%87%BB)
[下一篇
赵长鹏称币安可能遭遇史上最大规模加密货币盗窃案](https://blog.upx8.com/%E8%B5%B5%E9%95%BF%E9%B9%8F%E7%A7%B0%E5%B8%81%E5%AE%89%E5%8F%AF%E8%83%BD%E9%81%AD%E9%81%87%E5%8F%B2%E4%B8%8A%E6%9C%80%E5%A4%A7%E8%A7%84%E6%A8%A1%E5%8A%A0%E5%AF%86%E8%B4%A7%E5%B8%81%E7%9B%97%E7%AA%83%E6%A1%88)

## 相关文档

* [一文看懂 Agent Skills：从编写第一个 Skill 到理解底层架构
  10-26](https://blog.upx8.com/Agent-Skills-Skill)
* [解决 1Panel PHP 容器时间 UTC 偏差8小时问题
  06-29](https://blog.upx8.com/1Panel-PHP-UTC-8)
* [双色球开奖与 AI 预测数据展示系统
  02-12](https://blog.upx8.com/AI-2)
* [Zelay: 轻量级·高性能·原生 Realm 免费转发面板
  02-12](https://blog.upx8.com/Zelay-Realm)

## 评论与补充2

有问题或想补充的，写在下面 · 选中正文文字再点「报告错误」会自动引用

* ![](https://blog.upx8.com/usr/themes/upx8wiki/assets/img/tx/9447.svg)

  **芒果**#2今天 12:24Chrome 148 · Windows 10/11回复

  能不能加个二维码分享，方便电脑打开手机扫码
* ![](https://blog.upx8.com/usr/themes/upx8wiki/assets/img/tx/15931.svg)

  **菊斗罗**#1今天 01:00微信 8 · iOS回复

  这个不错，可以当备忘笔记 存东西。

回复
取消

请勿填写此栏

就事论事，别发广告 · 正常评论
发表评论

本文目录

* [正文](#sec-1)
  + [它是一本笔记本，也是一枚蜡封](#sec-2)
  + [对方看到的不是密码框，是一封信](#sec-3)
  + [封缄之后](#sec-4)
  + [适合谁](#sec-5)
  + [技术与隐私](#sec-6)
  + [去拆一封](#sec-7)

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
2003](https://blog.upx8.com/Free)
[安全
374](https://blog.upx8.com/os_security)
[开发
534](https://blog.upx8.com/code)
[资讯
2121](https://blog.upx8.com/news)
[全部文档](https://blog.upx8.com/all.html)