---
title: memos – 私人微博，开源可自托管的 flomo 替代
url: https://buaq.net/go-150888.html
source: unSafe.sh - 不安全
date: 2023-02-25
fetch_date: 2025-10-04T08:03:07.811108
---

# memos – 私人微博，开源可自托管的 flomo 替代

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/deba0514ad9b9377dc225f5843367d78.jpg)

memos – 私人微博，开源可自托管的 flomo 替代

*2023-2-24 18:58:34
Author: [www.appinn.com(查看原文)](/jump-150888.htm)
阅读量:37
收藏*

---

**memos** 是「一个具有知识管理和社交网络的开源、自托管的备忘录中心」。这是一个类似私人微博的产品，支持标签、过滤、搜索、多账户，可以自用也可以和朋友一起使用，用来碎片话的记录信息，就像 flomo 一样。@Appinn

![memos - 私人微博，开源可自托管的 flomo 替代](https://static1.appinn.com/images/202302/memos.jpg!o "memos - 私人微博，开源可自托管的 flomo 替代 1")

曾经有不少人问过：有没有像微博一样的产品，但是我只想自己用。这，它来了。

## flomo 是什么？

* [flomo – 像聊天一样记笔记，能用微信记录的笔记工具](https://www.appinn.com/flomo/)

**flomo** 是一款在线笔记工具，主打**无压力记笔记**，像聊天一样记录笔记，支持标签、每日回顾等功能，并且可以在微信中记录，非常灵活、快速。

![memos - 私人微博，开源可自托管的 flomo 替代 1](https://static1.appinn.com/images/202012/2020-12-04_14_13_12.jpg!o "memos - 私人微博，开源可自托管的 flomo 替代 2")

flomo 界面

## memos

memos 可以算作开源版本的 flomo，毕竟两者的界面太像了 😂

![memos - 私人微博，开源可自托管的 flomo 替代 2](https://static1.appinn.com/images/202302/screen-appinn2023-02-24-17-32-27.jpg!o "memos - 私人微博，开源可自托管的 flomo 替代 3")

memos 界面

## 主要特征：

* 🦄 开源且永久免费
* 🚀 使用 Docker 几秒内安装托管
* 📜 纯文本，支持 Markdown 语法
* 👥 将备忘录设为私人或公开给
* 🧑‍💻 支持 RESTful API
* 📋 使用 iframe 在其他网站上嵌入备忘录
* 🏷️ 支持标签
* 📆 GitHub 式的交互式日历视图
* ☁️ 数据库可保存至 S3 API（AWS S3、Cloudflare R2、MinIO）
* 👮 支持 SSO 登录（OAuth 2.0）
* 💾 轻松迁移和备份数据

## DEMO / 演示

有一个官方演示站点可以直接使用：

* [https://demo.usememos.com/](https://demo.usememos.com/auth?utm_source=appinn.com) （输入用户名密码点击 `Sign up` 即可注册，每日清空数据）

用起来，还是非常方便的。

如果你打算碎片化的记录内容，即可食用标签，只需要再记录的时候直接写 #标签 就行了，这样在未来更容易检索。当然 memos 本身也支持全文检索，以及捷径（快速过滤）：

![memos - 私人微博，开源可自托管的 flomo 替代 3](https://static1.appinn.com/images/202302/screen-appinn2023-02-24-17-53-29.jpg!o "memos - 私人微博，开源可自托管的 flomo 替代 4")

### 文件、图片、分享

支持通过资源库的方式上传图片、文件、视频，还可以非常方便的将你的「私人微博」通过链接的方式分享给别人。

## 安装

memos 在 GitHub 开源，目前有 6.7k 的 Star，推荐 Docker 安装，太方便了：

```
docker run -d --name memos -p 5230:5230 -v ~/.memos/:/var/opt/memos neosmemo/memos:latest
```

数据将保存在 当前路径下的 **.memos** 文件夹，该文件夹默认会隐藏起来。然后就能通过 IP:5230 来访问了。

登录后可选语言界面、是否允许公开注册、公共 memos、存储位置、SSO、自定义样式/脚本等。

![memos - 私人微博，开源可自托管的 flomo 替代 4](https://static1.appinn.com/images/202302/screen-appinn2023-02-24-18-54-37.jpg!o "memos - 私人微博，开源可自托管的 flomo 替代 5")

所以这个事情其实变成了如果你想免费使用，那么还是需要一台自己的服务器啊，NAS、台式电脑、VPS都行（顺手推荐个VPS：Digitalocean，新用户注册后将获得有效期60天的200美元券，地址：<https://m.do.co/c/973bc576ffef>

---

文章来源: https://www.appinn.com/memos/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)