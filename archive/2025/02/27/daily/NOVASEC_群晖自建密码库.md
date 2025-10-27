---
title: 群晖自建密码库
url: https://mp.weixin.qq.com/s?__biz=MzUzODU3ODA0MA==&mid=2247490428&idx=1&sn=462f2f2dbdf398dd5fbb9578b27ecc0c&chksm=fad4c66bcda34f7d86b0c26f567a376eaa05e3521534a610255e2c2dbc8dccc72db3affcaf67&scene=58&subscene=0#rd
source: NOVASEC
date: 2025-02-27
fetch_date: 2025-10-06T20:36:57.406827
---

# 群晖自建密码库

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eF6IWHLO7QXHmHTEicdtyyD7qOiazuvJcaOMhYkaq44caRJYVEbOKFnXxpbp5MGWlX0x5EjliavENEboVicdB8tBqQ/0?wx_fmt=jpeg)

# 群晖自建密码库

NOVASEC

以下文章来源于科技早知道Know
，作者科技早知道Know

![](http://wx.qlogo.cn/mmhead/naPHoFY2n5RiaX3070UwlZHdAaAIeYWoYic3Oicj7ffgvR2jVR1XEJiaDT21ZzYkVyduIG2bpIYnDUU/0)

**科技早知道Know**
.

✨「AI未来派」硬核科普站🚀🔥为您分享：✅拆解AI神操作✅狂薅AI生产力工具✅AI爆款玩法 ✅元宇宙新动态📩 评论区提问秒回

# 群晖自建Bitwarden

## 概述

> 当Bitwarden在快速发展的过程中，自建版本发生了开发分支。2022年5月左右，docker image由原来的bitwardenrs/server官宣转为https://hub.docker.com/r/vaultwarden/server。名称也由Bitwarden变为了Vaultwarden。Vaultwarden兼容所有Bitwarden的app，也就是说不论是浏览器的插件、桌面的应用程序，还是安卓、iOS的app，都能够通过Vaultwarden来自建密码管理平台，从而最大限度的保护自己的密码池。

---

## Vaultwarden 是什么

> Vaultwarden 是一个用于本地搭建 Bitwarden 服务器的第三方 Docker 项目。仅在部署的时候使用 Vaultwarden 镜像，桌面端、移动端、浏览器扩展等客户端均使用官方 Bitwarden 客户端。
> Vaultwarden 很轻量，对于不希望使用官方的占用大量资源的自托管部署而言，它是理想的选择。

## Vaultwarden 与 Bitwarden 的区别

> 除不支持官方企业版的部分功能（如目录同步、SSO、群组、自定义角色以及基于企业组织层面的 Duo Security 两步登录）外，其他大部分功能均免费支持。并跟随官方版本保持及时更新。
> Vaultwarden 比官方版更轻量。官方版使用 .Net 开发，使用 MSSQL 数据库，要求至少 2GB 内存；Vaultwarden 使用 Rust 编写，改用 SQLite 数据库（现在也支持 MySQL 和 PostgreSQL），运行时只需要 10M 内存，可以说对硬件基本没有要求。

## 搭建Vaultwarden

在docker搜索vaultwarden，并下载

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QXHmHTEicdtyyD7qOiazuvJca9h7ianyoHh07fCzqVxFYQdjyJB0kN8zSzbCDsNVLngSiaanmYoxMcxqA/640?wx_fmt=png&from=appmsg "null")

配置好容器存储路径，其他的默认就好了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QXHmHTEicdtyyD7qOiazuvJcazyUcuWIkH0h73NsJpTWhJ2HrQOicbp0WV2AfKUrQj0pmO2j8Wu4UxJw/640?wx_fmt=png&from=appmsg "null")

然后运行后点详细，记住这里的端口号![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QXHmHTEicdtyyD7qOiazuvJcaiascWTnLxUpicWWblvnjibxRRojJkUh9ibIJLWOynpibFHoztoX6zLtEH9g/640?wx_fmt=png&from=appmsg "null")

套件中心安装花生壳![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QXHmHTEicdtyyD7qOiazuvJcaN4Fia5KM9BE2ugfEf6V5NugptoYgoNWhJ0Z2mT29BwSXAPr2iaKsgUGQ/640?wx_fmt=png&from=appmsg "null")

然后配置花生壳，设置内网nas的ip还有Vaultwarden的端口号![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QXHmHTEicdtyyD7qOiazuvJcatqF59gxTcnmAaFibMxSibNttFZiceeIBajDWZynKSNnsQficnC5pgtL56w/640?wx_fmt=png&from=appmsg "null")

然后访问外网地址，创建账号密码登录。搞定![](https://mmbiz.qpic.cn/sz_mmbiz_png/eF6IWHLO7QXHmHTEicdtyyD7qOiazuvJcaRtWUJaFGpMPU6CCoGTuibt4eT87WSWfwP2YrWVgKqnI7y7EpIFhzHMQ/640?wx_fmt=png&from=appmsg "null")

### 配合无公网 IP 搭建 Cloudflare 免费隧道穿透

[群晖无公网IP免费隧道穿透](https://mp.weixin.qq.com/s?__biz=Mzk3NTE5MTMzMQ==&mid=2247483900&idx=2&sn=707a768799361ebd54cd019ed1f32441&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

NOVASEC

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

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