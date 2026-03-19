---
title: 聊一下我的“多源日志采集与智能分析平台”：支持两种 syslog 日志外发啦！
url: https://mp.weixin.qq.com/s/SBZq0k9AZLM_eZTZ_0Hcgg
source: Doonsec's feed
date: 2026-03-18
fetch_date: 2026-03-19T04:15:13.846820
---

# 聊一下我的“多源日志采集与智能分析平台”：支持两种 syslog 日志外发啦！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Q71mAqQaURNzyVxC1xKfB9UM7X7CBpTH71G3ktsyppNsHYsywGa8qu8ichZIlqvWibwgQKsIZNQlQg4icPWjkYTM0Uw3z3y6zeRCUlMDAbJv3w/0?wx_fmt=jpeg)

# 聊一下我的“多源日志采集与智能分析平台”：支持两种 syslog 日志外发啦！

原创

网路游侠
网路游侠

游侠安全网

![]()

在小说阅读器中沉浸阅读

相信看到此文的很多朋友知道我用AI写了几款软件，其中投入精力最多的是“多源日志采集与智能分析平台”（俗称“日志审计”），总得隔三差五给我的各位朋友们汇报下进度！

今天完成的：

1、今天凌晨完成了2个文档。一个是技术白皮书、一个是产品介绍幻灯片。中午和晚上已经和一些朋友同步了；

2、刚刚：完成了声音告警、syslog告警的调试，在多源日志菜就只能分析平台上发了测试告警给GreenLogAudit免费版日志审计，测试成功。

![](https://mmbiz.qpic.cn/mmbiz_png/Q71mAqQaURPPoIYTaP8N8eI4TK402MEib3wGDbiaTuqNnA2FZLLVvhgvjlG8Ort832KY1RXXFIUIdibVBgtshibG7CzLhXZBBJl46cXlBaGzljU/640?wx_fmt=png&from=appmsg)

目前这款日志审计支持两种syslog外发：

一、收到的各类日志（如交换机、路由器、防火墙、Windows和Linux服务器、入侵检测等）中，如果有告警，可以仅把告警转出去，如给SOC或SIEM；

二、某些场合可能需要全量收取日志审计的数据，如你仅仅是把日志审计当成SOC或SIEM的日志采集探针，那么就可以用这种方式把所有日志（而不仅仅是告警）转发出去。

其它功能，慢慢优化。

暂时不会增加新功能了，目前功能已经够用且好用了。

对了：目前这算是有四款小产品了：

**第1款：Windows日志采集WinLogAgent下载：**

https://github.com/youxia029/WinLogAgent/releases

**第2款：多源日志采集与智能分析平台，是否出免费版待定；**

https://www.syslog.cn （大概再过几天会在这里介绍）

**第3款：永久免费、U盘可用的GreenLogAudit日志审计下载：**

https://github.com/youxia029/GreenLogAudit/releases

**第4款：SaaS版离线日志分析系统，可以直接注册**

https://log.youxia.org/ （目前可以免费使用）

**欢迎联系游侠合作（微信 cnbrian 或扫码），可OEM，价格相当美丽**

相关阅读：

[昨天做了两件事！日志采集、日志审计，同步推进！相关产品有四款啦！](https://mp.weixin.qq.com/s?__biz=MjM5NjI0NjcwMg==&mid=2652155207&idx=1&sn=f78d6b92353a9f27493dedb41140e122&scene=21#wechat_redirect)

[4.63MB就能跑日志审计？GreenLogAudit 绿色免费版上手实测（附下载与配置指南）](https://mp.weixin.qq.com/s?__biz=MjM5NjI0NjcwMg==&mid=2652155202&idx=1&sn=bf71cc15ec4c9a66647d8356d35fa9fe&scene=21#wechat_redirect)

[给Windows离线日志分析SaaS平台增加了个注册功能](https://mp.weixin.qq.com/s?__biz=MjM5NjI0NjcwMg==&mid=2652155197&idx=1&sn=a8be1ca9e1260fdb6609d7b5be454e05&scene=21#wechat_redirect)

[写了一款Windows日志采集器](https://mp.weixin.qq.com/s?__biz=MjM5NjI0NjcwMg==&mid=2652155180&idx=1&sn=ec801e43a4259fb6939d9eff17e7a860&scene=21#wechat_redirect)

[写了一款syslog实时日志审计系统](https://mp.weixin.qq.com/s?__biz=MjM5NjI0NjcwMg==&mid=2652155167&idx=1&sn=6754e0841d90903faf4701f13aa1d99e&scene=21#wechat_redirect)

[写了个SaaS版本的Windows日志审计](https://mp.weixin.qq.com/s?__biz=MjM5NjI0NjcwMg==&mid=2652155159&idx=1&sn=1fc7921f39b4f8cf26e2e2cd85b41802&scene=21#wechat_redirect)

[USBLogClear - U盘使用记录查看和删除工具](https://mp.weixin.qq.com/s?__biz=MjM5NjI0NjcwMg==&mid=2652155145&idx=1&sn=541172a3f5fbfe9c8d2b1524fc21c740&scene=21#wechat_redirect)

[45岁，裸辞 | 这几个月，已经46岁的我在做什么？](https://mp.weixin.qq.com/s?__biz=MjM5NjI0NjcwMg==&mid=2652155136&idx=1&sn=a1b9ce6179876c99bfb86f03d49a1aa6&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/bgkwFOXObJpyJMF6qbW4AlsQrwQUrZ6nIvql5pwiciaiatSSWcKc7qKIRDsy7baaScKe4VpVibesiaJ66FbOzCmdx4g/0?wx_fmt=png)

游侠安全网

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/bgkwFOXObJpyJMF6qbW4AlsQrwQUrZ6nIvql5pwiciaiatSSWcKc7qKIRDsy7baaScKe4VpVibesiaJ66FbOzCmdx4g/0?wx_fmt=png)

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