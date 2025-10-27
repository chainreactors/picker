---
title: 如何快速命令行使用牧云主机助手
url: https://mp.weixin.qq.com/s?__biz=MzIzOTE1ODczMg==&mid=2247495243&idx=1&sn=1399fe3cd7a1390275f56ebf8e982222&chksm=e92cfae8de5b73fe58a670fa8c3144f59b4bf94634a0cad6a20335f2ac0f7def967802cbb4a9&scene=58&subscene=0#rd
source: CT Stack 安全社区
date: 2023-03-15
fetch_date: 2025-10-04T09:36:06.653444
---

# 如何快速命令行使用牧云主机助手

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1HSdSibDdRfspYIBibkREZ14VibT0M7BSmMJ3MFQEhFCc0ohBjYLYCIW6228rd2R9TG1Nic4BKT4XicugVTacTCgBTA/0?wx_fmt=jpeg)

# 如何快速命令行使用牧云主机助手

CT Stack 安全社区

以下文章来源于长亭百川云平台
，作者DVKunion

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM56bWiaa6ic0ZJu9qGoOKP5dobAVNOxcfxgial7YI8dpTLwg/0)

**长亭百川云平台**
.

百川云平台（Rivers）是长亭面向企业开放的在线安全产品服务，包含了多个安全产品，如问脉容器安全产品，关山WebShell检测产品，牧云主机安全产品，以及其他第三方安全公司提供的安全产品等。

---

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/1HSdSibDdRfsuwavWhyGrAic5x5ibJUjjhibfwvBLa5EzL0vvLwibgM2ibMpBeNg2vJZ2ax9QzorCqabpaZjoe0BBfGw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/xLk5PwibzMpRAjsMFX9Hgv7qicvPTaYkyJDbFyiawz0zLdtw3pSklQM5zkBX58d5ATll9uA5sMUwnIXia5w7D1gZvQ/640?wx_fmt=jpeg)

作者介绍

DVKunion

致力于不断寻找创新和有趣的安全解决方案
  擅长领域：web安全/云原生安全/Golang开发
  Github:  https://github.com/DVKunion

**· 前言 ·**

[前面](http://mp.weixin.qq.com/s?__biz=Mzg4MjgyNDIzOA==&mid=2247484580&idx=1&sn=5fb8563de3e38d70d4f3e1068bc74c10&chksm=cf5181e5f82608f37437114461a664252f0c3177f649a1fb04020657e63c8b6a37dcbca1edfc&scene=21#wechat_redirect)说过 Collie[牧云主机助手](http://mp.weixin.qq.com/s?__biz=Mzg4MjgyNDIzOA==&mid=2247484277&idx=1&sn=dd1cb556d1058bad1d030a8004f9592c&chksm=cf518634f8260f229c2caf2abac33bea00c45ff285012a67eeb2b49e6d7d55b6b6d71c47e163&scene=21#wechat_redirect)非常便捷，但当我管理的机器为终端、无法登录浏览器或批量显示所有主机 CPU 数据时，还是需要启用命令行，于是研究了一番Collie 的 API Token ，糊了一个工具 Collar，作为Collie 牧羊犬的项圈，希望能让师傅们更加舒适的管理和使用 Collie。目前已支持的功能模块：

* shell终端
* 进程列表(输出优化中)
* 主机列表(输出优化中)

> 下载Collar：https://github.com/DVKunion/Collar

**0x01 开始使用**

**1. 1  获取 Collie Token**

注册百川云平台(https://rivers.chaitin.cn)，并开通牧云主机管理助手应用。

点击工作台 - API Token - 生成Token，勾选所有牧云主机助手相关权限，生成您的Token信息。

![](https://mmbiz.qpic.cn/mmbiz_png/1HSdSibDdRfuwPib4GntGEEOqZNgUFXFAyiaBWuMAdqfCBAHFuV2icibjWpb89gQNBYgDLbB2LLAy12eeTNiaLibJyI0g/640?wx_fmt=png)

> 请注意，token 存在有效期，为了方便使用，您可以申请一个时间比较长的 token。

然后在github-release页面下载符合自己操作系统的二进制文件，放置在$PATH目录下，执行:

```
collar auth -t YOUT_TOKEN
```

初始化身份认证成功，即可开始使用。

**1. 2  使用手册**

* 主机列表

```
collar hosts
```

获取主机列表信息

* 进程列表

```
collar top [hostId/host_name/host_ip/host_inner_ip]
```

获取主机进程信息， 每3s更新一次

* 登录主机 Terminal

```
collar shell [hostId/host_name/host_ip/host_inner_ip]
```

可以通过主机ID/主机名/主机IP/主机内网IP 进行登录

* 自动登录主机

```
collar shell -a [hostId/host_name/host_ip/host_inner_ip]
```

这将会使用您配置的自动登录用户名进行登录（暂不支持通过cli设置自动登录用户名)

**0x02 写在最后**

Collar 目前的规划是以核心功能(文件管理、在线终端)为主，后续逐步填齐其余的全部的功能(Docker、资源负载显示、登录历史、进程清单等)，并在这个基础上，可能还会做一些功能的优化，比如多主机的数据聚合、多主机同步执行命令(类ansible)等... 走过路过的老板们给个Srar![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/newemoji/Social.png)

.

END

---

→ 了解牧云主机管理助手：[**点击查看**](http://mp.weixin.qq.com/s?__biz=Mzg4MjgyNDIzOA==&mid=2247484277&idx=1&sn=dd1cb556d1058bad1d030a8004f9592c&chksm=cf518634f8260f229c2caf2abac33bea00c45ff285012a67eeb2b49e6d7d55b6b6d71c47e163&scene=21#wechat_redirect)

→ 技术交流微信群：**CTRivers**

![](https://mmbiz.qpic.cn/mmbiz_jpg/xLk5PwibzMpQ7pNT43j6psz5uZ9LickbLOTunA8kd4cFAcNJEY2XxrsbPjdnqzPAIZjUZ1P1mAfzFUwF2w9LVu2w/640?wx_fmt=jpeg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpRbyCZNQHcXYS8ZnGg2SLZEey7tficiaJdAaAMsDMX62UV6ClbgNUF6CMyay80xjnX9qrCRKLHHGnIg/0?wx_fmt=png)

CT Stack 安全社区

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/xLk5PwibzMpRbyCZNQHcXYS8ZnGg2SLZEey7tficiaJdAaAMsDMX62UV6ClbgNUF6CMyay80xjnX9qrCRKLHHGnIg/0?wx_fmt=png)

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