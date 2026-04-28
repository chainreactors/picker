---
title: CSDN、知乎、公众号再也别想卡我了！code-box 一键解锁全部内容
url: https://mp.weixin.qq.com/s/_srmbf7oJYblZrErifcMAg
source: Doonsec's feed
date: 2026-04-27
fetch_date: 2026-04-28T05:23:25.885335
---

# CSDN、知乎、公众号再也别想卡我了！code-box 一键解锁全部内容

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4T1PVwJicwk8Zia7ibN209nsgjAU9AnrbzxibYSjyziaDicCb5jtnYnbULQxm2GCWaic8T9Esd4vTsh61Vd6fia0ToSIicZx6Og68gTrzY4MXHXtmYlI/0?wx_fmt=jpeg)

# CSDN、知乎、公众号再也别想卡我了！code-box 一键解锁全部内容

原创

宀十八
宀十八

泷羽Sec-Norsea

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

报道先生归也，杏花春雨江南。

> ```
>  免责声明
> ```
>
> 本系列工具仅供安全专业人员进行已授权环境使用，此工具所提供的功能只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用工具中的功能对任何计算机系统进行入侵操作。利用此工具所提供的信息而造成的直接或间接后果和损>失，均由使用者本人负责。
>
> 工具集合：https://pan.quark.cn/s/f113bdb29fd7

## 一、什么是 code-box？

code-box 是一款开源浏览器插件，主要用于优化在 CSDN、知乎、掘金、微信公众号、博客园、脚本之家等主流技术平台上的阅读体验。它能帮助用户实现一键下载文章（支持 HTML、Markdown、PDF 格式）和无登录状态下一键复制代码，同时自动移除登录弹窗、关注博主提示、跳转 APP 弹窗等干扰内容，让用户可以更专注、高效地阅读和保存技术文章。该插件基于 Plasmo 框架开发，支持 Chrome、Edge、Firefox、360 浏览器等多平台使用，是一款实用性很强的阅读辅助工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4T1PVwJicwk9KWvOtDBn2xRZO44ljL5CwM4L2gx17y9xFYCgThzEM49jQmEzGsaz86FK9PxYcqc9rLs94jedQfHzZjM1EA5FFq1iaL6Tq5yBY/640?wx_fmt=jpeg&from=appmsg)

## 二、功能介绍

code-box 的功能设计围绕“解放阅读体验”展开，主要包括以下几个方面：

* **文章下载功能**：支持一键将文章导出为 HTML、Markdown 或 PDF 格式，方便后续笔记整理、离线阅读或存档。特别支持微信公众号文章，可同时下载文章中的所有图片。
* **代码复制优化**：无需登录账号，即可选中代码块进行复制，或直接点击代码块右上角的复制按钮。支持自动展开 CSDN 等平台折叠的代码块，极大提升复制效率。
* **干扰内容移除**：自动屏蔽强制登录弹窗、“关注博主阅读全文”提示、跳转 APP 弹窗、VIP 限制等常见干扰元素，让用户无需关注即可阅读完整内容。
* **自定义与个性化**：支持注入自定义 CSS 样式美化阅读界面，可灵活选择下载格式，还能批量下载文章中的图片。
* **多平台支持**：覆盖 CSDN、知乎、掘金、微信公众号、简书、脚本之家、博客园、51CTO、php中文网 等主流技术网站，移动端同样可用。
* **其他实用功能**：一键关闭百度等平台的 AI 对话框、生成二维码海报、复制微信公众号图片链接等。

这些功能让 code-box 成为开发者、技术博主和知识管理者的常用工具。

三、框架架构code-box 采用现代浏览器扩展开发框架，主要技术架构如下：

* **核心框架**：Plasmo（Chrome/Edge/Firefox 扩展开发框架）
* **开发语言**：TypeScript（占比约 90%）、HTML、JavaScript、SCSS/CSS
* **包管理工具**：pnpm
* **构建流程**：支持 pnpm dev（开发模式）和 pnpm build（生产打包）
* **扩展机制**：基于 Chrome 扩展 API，实现内容脚本注入、页面修改和功能增强
* **AI 辅助**：部分版本集成 KIMI AI 用于文章解析（可选功能）
* **多语言支持**：包含 locales 文件夹，支持多语言界面

整体架构轻量且高效，注重用户隐私，所有操作均在本地完成，不依赖云端服务。

四、如何使用安装方式（推荐顺序）：

1. `插件商店安装`（最简单）

* Chrome / Edge / 360 浏览器 / Firefox 应用商店搜索 “codebox” 或 “code-box”，一键安装即可。
* ![](https://mmbiz.qpic.cn/sz_mmbiz_png/4T1PVwJicwkib9jZguTw6RUIibE0qeSJHVibQ351jCV8cXlmvxr8tNC0uYc5ShqibC0MWoExvfj7mCdHsic1F6e8v5ObxIU1tEtR6GHxXiaAE19JpA/640?wx_fmt=png&from=appmsg)
* ![](https://mmbiz.qpic.cn/mmbiz_png/4T1PVwJicwk9TGnliaThEoWZxxulxelCpBicjpsEavqdcgxI68Re42SsoiaVk44IibxiaVlfxhfn88mNCTQRpGzG9nP06CeY6fYZjdjHQPBloibsaM/640?wx_fmt=png&from=appmsg)

2. `源码安装`（适合开发者或需要最新功能的用户）

   ```
   git clone https://github.com/027xiguapi/code-box.git
   cd code-box
   pnpm install
   pnpm dev     # 开发模式
   pnpm build   # 生产打包
   ```

   然后在浏览器扩展管理页面（chrome://extensions/）开启开发者模式，加载已解压的插件文件夹。

安装完成后，打开支持的网站（如 CSDN、知乎等），插件会自动生效。用户可在插件图标处进行设置，如自定义 CSS、选择下载格式等。

五、其他适用场景：

* 开发者日常阅读和保存技术文章
* 技术博主整理素材
* 学生/研究者离线学习和笔记管理
* 需要频繁复制代码的编程学习者

```
项目地址：
https://github.com/027xiguapi/code-box
```

## 学习交流群

刚加入网络安全行业的小白，可以加入学习交流群，大家一起互相学习，互相进步，不会的难题大家一起学习，一起攻克。

想要进学习交流群的师傅们，可以扫描下方二维码添加好友，我再拉你进群（Ps：防止广告进群）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/IkpoxULsr9dEclFnKnAAurt1AlnO1HBLiaRymULG1ibJJhXlNjMH1rd1SgQQWIyFBVTRMteWWfiby3FCWfpB7n2oA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fbWSl52zKqe5AN711UM8IFNbS9rZLM7reGeUZs0XqdtM8X5L5mdRibicHpxmu3iaPGct9UztVKAT6AA/0?wx_fmt=png)

泷羽Sec-Norsea

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fbWSl52zKqe5AN711UM8IFNbS9rZLM7reGeUZs0XqdtM8X5L5mdRibicHpxmu3iaPGct9UztVKAT6AA/0?wx_fmt=png)

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