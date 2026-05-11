---
title: 2026年第四届“盘古石杯”国际电子数据取证大赛-服务器思路分享（不包含具体解题过程）
url: https://mp.weixin.qq.com/s/mcVK4RV1ogIp8V1JJZ56sg
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:53:35.195431
---

# 2026年第四届“盘古石杯”国际电子数据取证大赛-服务器思路分享（不包含具体解题过程）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8HibB35D4DH6nibVnpaRiaYRftdHbZ5Q70eLicwBncHCDq7XicYVI39g1lUp0pyxuiaY1eA771o5rdAsMn5PDmPXswC502AvokGDg0kic0lVP6Uice8/0?wx_fmt=jpeg)

# 2026年第四届“盘古石杯”国际电子数据取证大赛-服务器思路分享（不包含具体解题过程）

原创

取证额头
取证额头

取证额头

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

配置网络耗时间耗精力

配网络

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8HibB35D4DH5wnkWr8Sd4Phfiaib17OJiahcuF8XISyBP4ohZgqy1MkBywtX3Wu9jXJQhuq2kbxc5xblQpK08JFFia8Y1Fo09SPv6oClWYhzkMic4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8HibB35D4DH6CW1bcnFEFQq88Ptos4wQicpeKz7qnAGBicOmYKIeycNqeicGy2lvbkFQsHYCdNMk1ukaldk9GVAP1UPQw3oia0pjwW4BKE3y96Ic/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8HibB35D4DH46BQmZvM9mlsXtxXibvlvcWMS1mUM5cYC8iajXgZPpnbXecys6XOmybb55r9CDHFHGwicQJeAdH94g7LdpbWrLm8qXjVvicRibDYbU/640?wx_fmt=png&from=appmsg)

Nat按照开机后显示的192.168.0.50/51/52，改子网和分配，从50开始分配

然后输入命令

```
ip link set ens160 up
ip link set vmbr0 up
ip link set ens160 master vmbr0 2>/dev/null || true
ip addr flush dev vmbr0
ip addr add 192.168.0.50/24 dev vmbr0
ip route replace default via 192.168.0.1 dev vmbr0
ip -br a
bridge link
ping -c 3 192.168.0.1
```

还有一个小坑点是黑火眼加载的时候，即使挂了两个镜像，在红火眼仿真的时候，还是会掉一个镜像，要手动在添加上一个镜像，直接在仿真界面挂上就行

![](https://mmbiz.qpic.cn/mmbiz_png/8HibB35D4DH6Zic5icdHSLMAunmx1jEriaIu08de5XJqSW7MJMzicCCcPNg4yM4qg6NwZNxhBpfv5LictDjJ9G7NyVicicU1ibic5vDkC9F27EznvLH10/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8HibB35D4DH52BLtvPQy7oasnIn9VWEsmVjrODm3EXocd8NTYymicwmwiabrTckFYicCzGcaSe8D436o0gjrunTOV7vkibZR3kHqatZSSjmn7ZEU/640?wx_fmt=png&from=appmsg)

然后命令里面记得改192.168.0.51，52 网络配置好后直接让codex连ssh就可以了。

- 本文采用「人言兑.md」自动排版，主题: 春天 -

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/El9TntkKrphJHAd1oyZDnGENLvGnP3TZibRMPbtVILCIwJToFicNzBSsCNmicLtUZMnpEjekZNusABBsjE6ialyxZg/0?wx_fmt=png)

取证额头

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/El9TntkKrphJHAd1oyZDnGENLvGnP3TZibRMPbtVILCIwJToFicNzBSsCNmicLtUZMnpEjekZNusABBsjE6ialyxZg/0?wx_fmt=png)

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