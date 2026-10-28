---
title: 一个Docker把800+频道管理起来，全家电视公用一份订阅
url: https://mp.weixin.qq.com/s/q7GGFyqu0QVw40MMGahD6w
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:40:37.271960
---

# 一个Docker把800+频道管理起来，全家电视公用一份订阅

# 一个Docker把800+频道管理起来，全家电视公用一份订阅

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

工具预计阅读 6 分钟 · 共 2011 字

直播源三天两头失效，央视看完找咪咕，你的电视频道该有个统一管家了

IPTV · 直播源管理

#Docker#飞牛NAS#自建#聚合分发

READING PATH

阅读路线

6 个章节

01

这个工具做什么

-

02

部署：一份 compose 的事

-

03

全家设备怎么接：一份订阅走天下

-

04

搭完之后是什么体验

-

05

说清楚边界

-

06

直播源管理，本来就该是一次配置长期受益

家里的电视频道，现在是怎么管理的？想看央视，打开央视频。想看球赛，切咪咕。B站、抖音、虎牙、斗鱼，每个 App 各管一摊。

痛点 01长辈想找个台，你远程指挥半天

痛点 02好不容易配好一份 m3u，用三天失效了，再找再失效——你压根谈不上在看电视，纯粹是在给直播源守灵

痛点 03全家人用不同设备，电视用飞牛TV，手机用别的播放器，每台设备各自配一遍源，改一处其他设备全得重来

这三个问题，指向同一个解法：在自己家里搭一套直播源管理系统，所有来源 **聚合、去重、统一分发**，全家设备共用一份订阅。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfycghjsVC6ib6ugTEtIlO9QyQicJf8QCVcWsFqfRD7ickvjplz0z2I3Qviam4kghtl2T60iacibmHeAgsekyq1Jt3ibmM6D7GQFIaKLqs/640?wx_fmt=png&from=appmsg)

CHAPTER 01

**01****这个工具做什么**WHAT IS IT

IPTV 是一个直播源管理与分发系统，Docker 一键部署，飞牛 NAS 有安装包。

它的核心是一套 可持续维护的内容接入体系，而非一份静态频道表。内置抓取模块：

央视频咪咕B站抖音虎牙斗鱼多地区广电

所有来源统一完成聚合、去重、编排，输出干净的播放列表和 EPG 节目单。几个关键能力：

CAPABILITIES

六大核心能力

1

直播源集中管理

把你合法获得的 m3u8 源集中起来统一输出，支持独立自动刷新，失效源不必手动维护，定时刷新自己续命

2

账号登录支持

对需要登录的平台，可配置你自己已开通会员的账号。注意边界：项目不提供任何账号、密钥或破解手段

3

默认配置就能用

免费频道默认可用，想看更高画质去源管理里配你本人合法持有的账号，凭据只存在你自己的部署里

4

外部源灵活添加

直接加 m3u8 链接，或通过网页播放地址自动抓取，同样支持独立自动刷新

5

可视化 Web 后台

访问 /admin 管理所有频道，增删改 1 到 2 秒内生效，不用重启

6

标清到 4K 支持

画质取决于你用的源本身，工具只负责把它稳定送出去

CHAPTER 02

**02****部署：一份 compose 的事**DEPLOY

群晖和飞牛都能用 Docker 部署。创建 `docker-compose.yml`：

yaml

services:

iptv:

image: akiralereal/iptv:latest

container\_name: iptv

init: true

ports:

- "1905:1905"

environment:

- mport=1905

# - mhost=        # 可选：外部访问地址

# - mpass=        # 可选：访问密码，设置后访问 http://ip:port/密码/...

volumes:

- ./data:/iptv/data

restart: always

启动：

bash

docker compose up -d

升级：

bash

docker compose pull && docker compose up -d

注意

两处别偷懒

#data挂载#mpass密码

- **data 目录必须挂载**：不挂载的话重建容器或升级镜像会丢全部配置 - **mpass 建议设上**：尤其打算给朋友共享的时候，裸奔的服务谁都能进你后台

不擅长动手的飞牛玩家有更省事的路：下载安装包，打开飞牛官方应用商店选手动安装，上传即可。

部署完成后，访问 `http://your-ip:1905/admin` 进入管理后台。设了密码的话，地址是 `http://your-ip:1905/密码/admin`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfycqtdsy9thNwoDvqFUb4KA1kWt7pSJn9fV9x9G1Pxlobzhia1rcF2CE94Gy6qCmWpDTpG9YicS58yNXmAtwcnt8Ca5y6Qv1Knia8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfzRlXUsQRG1DeBNyzIXxnmNt4dmEVgX7STx2ibibJus97zXjGr0zJtyyQrz4nInNoam3vWrhB0YZdDc1PE872vMTGXic6wp5P2DgI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfxLgwcibmX3SY1GxzWRIoQgr0wD93v1DIZZZQia8ZqhVxEDLJOtkq5ewY03r6AhAVTAZFWn78bleIbzse3iaL8wqic8Oh1gmFTREaU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfyAKsGZ1ViaztiaEEq3RnyUHBLQkWOL1VNiakzicmp6bGwuM60QfXeeIOmCpBqcvFPatdk7k7jXCb0CqD2JXHMt8WzU2dfcLyibxuOo/640?wx_fmt=png&from=appmsg)

CHAPTER 03

**03****全家设备怎么接：一份订阅走天下**CONNECT

不同播放器，订阅地址不一样，对照这张表：

| 播放器 | 订阅地址 |
| --- | --- |
| **DIYP / 百川影音** | TXT 订阅：`/txt` |
| **TiviMate / APTV / Kodi / OK影视** | 标准 M3U：`/interface.m3u` |
| **飞牛影视 / 飞牛TV** | 标准 M3U：`/interface.m3u`，必须保留 `.m3u` 后缀 |
| **极空间极影视、部分老电视盒** | 兼容版：`/interface.m3u?relay=1` |
| **兼容版还不行的设备** | 全代理版：`/interface.m3u?relay=2`，服务器转发视频分片 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfwdIQauW9FibEWZziahzFkfa8oyRfu10Y7qOgNKC6BeeaLEHPpYQImbpPYCDqFIuSyEFySxLjB7A6zromQGESIia5otfdicLfRiaM9M/640?wx_fmt=png&from=appmsg)

以飞牛 TV 为例，三步接完：

3 STEPS

飞牛TV 接入三步

1

第一步 复制订阅

管理后台「我的频道」找到订阅地址复制

2

第二步 飞牛影视新增

新增媒体库，选电视直播，粘贴订阅链接

3

第三步 勾统一显示名

系统设置里勾上「统一频道显示名」，最容易漏

01

复制订阅地址

登录管理后台，点顶部导航栏"我的频道"，找到订阅地址复制下来。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfyEOT9SsB00ZDBTSAp4Ffiah3PEicFjKYzicgYk9RGyOwUN4iamwSfBOttNpS9Mic4bACpia5k5uXNY2xBTzWNxZEds6GCQH5OLeqm3k/640?wx_fmt=png&from=appmsg)

02

飞牛影视新增媒体库

打开飞牛影视，点右上角设置，新增媒体库。内容类型选电视直播，填直播源名称，粘贴订阅链接，确认创建。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfzuicKC3cicHr6UyTL9leichWHJN9eHMOynsol32fWAIJnIfOdEicVibgVwyFfBdp0zV72b3q7siaW5vVExjibJRNxxHyjIw4EM5T6D7A/640?wx_fmt=png&from=appmsg)

03

勾选统一频道显示名

回到管理后台的系统设置，把"统一频道显示名"勾上——这一步最容易漏。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfzc2rlRHk1kyZFEe45ohg8hBvqz2W1HM8hECkfpN87Z36OgcWjuHXTgCRq9f3oXNicHILg7hNVn0YLGhmKiaEyjwILyj7ubLyhXQ/640?wx_fmt=png&from=appmsg)

关键开关

统一频道显示名

#去重#统一命名

这个开关解决一个经典折磨：不同源里同一个台，写法五花八门，CCTV1、CCTV-1、CCTV1综合，列表里占三个位置。开启后按内置规则自动统一成同一个显示名，CCTV 系列和清晰度后缀已内置。手动重命名优先级更高，规则兜不住的写法去频道别名标签里补规则。默认是关的，记得手动开。

CHAPTER 04

**04****搭完之后是什么体验**EXPERIENCE

一套部署全家共用源失效自动刷新1-2秒生效长辈只记一个入口可公网分享

电视、手机、平板，全用同一份订阅地址。源失效不用你管，定时自动刷新续命。新频道后台加完 1 到 2 秒生效。

长辈只用记一个入口，想看什么列表里翻，频道名是干净的统一命名。

有公网 IP 的话，还能把订阅分享给朋友。记得设好 mpass 密码，别把后台裸奔出去。

CHAPTER 05

**05****说清楚边界**BOUNDARY

边界

管的是组织和分发，不生产内容

#中立#合法#自部署

- 免费频道默认可用 - 付费平台的画质，靠的是你自己开通的会员账号，凭据存在你自己的部署里 - 项目本身不提供、也不该被用来提供任何账号、密钥或破解手段

工具中立，用法看人。这个边界守住，它能一直用下去。

CHAPTER 06

**06****直播源管理，本来就该是一次配置长期受益**CONCLUSION

你现在维护直播源的方式，是 **坏了就找，找到就配，配完再坏**。

换个思路：把聚合、去重、刷新、分发交给系统，你只管偶尔打开后台看一眼。

工具已经把脏活干完了，你还在手动换源，那就只是习惯问题。

你家电视现在用什么看直播？

运营商机顶盒、各平台 App 换着开、还是自建 IPTV？评论区聊聊直播源失效的坑

· 点赞 ·

喜欢就点个赞吧

· 转发 ·

分享给更多朋友

· 推荐 ·

推荐给身边的人

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtLPfoEoNn5zJQjy6nMKW0GVf41zsKNsIVKdWJsxm2gSyIToAJOFI8x2wryVm4GqQib0ibno9KzEa9A/0?wx_fmt=png)

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