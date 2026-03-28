---
title: FireKylin：一款开源安全应急响应系统痕迹采集工具
url: https://mp.weixin.qq.com/s/NYeNiB8LQdxF5K6uz8UmIw
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:12:29.440893
---

# FireKylin：一款开源安全应急响应系统痕迹采集工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicK9qLRgMKGwPCic1gAczvFMqbIJE9ZTvAoQY344dibvev3FZlx7zfprpQb71YNibxm7Rz3Pib4aQLvQ2Gn6Ncwbq0UGIu99dwJicGoU/0?wx_fmt=jpeg)

# FireKylin：一款开源安全应急响应系统痕迹采集工具

原创

网安工具库
网安工具库

网安工具库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[WatchVuln-web：一款开源漏洞情报监测工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486855&idx=1&sn=191e6b51306d5da6dc65388dc623ac0e&scene=21#wechat_redirect)

·[CTF-Web神器：让ai去帮你打CTF好了](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486849&idx=1&sn=19904be3904d7492f131658fca2fed3f&scene=21#wechat_redirect)

·[MDUT-Extend：数据库安全综合测试工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486840&idx=1&sn=ebc0e80ec4e9b9bd6670090fce379561&scene=21#wechat_redirect)

·[Glato：GitLab CI/CD 流水线的渗透测试框架](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486813&idx=1&sn=7d6a9888840f5a5c20abcec44152c09e&scene=21#wechat_redirect)

·[内网网络审计工具箱（大牛蛙版）](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486807&idx=1&sn=1b567845a716975b6e522377016aa681&scene=21#wechat_redirect)

·[近期你还有这些CTF比赛可以参加](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486793&idx=1&sn=cdb32a1bebeda8c4f670d3528be22d1d&scene=21#wechat_redirect)

**背景分析**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKgniayqVHSrFQtcXJ7sicialTM2WJcibnqNCkG7fTa5Tx08no4Jb7D9W49IXUfyNkRck08Z8gOlS3iaOeI1YmeEy3nJUfBGWqtt0W0/640?wx_fmt=png&from=appmsg)

网络安全事件应急响应工作中，`Windows`与`Linux`服务器的系统痕迹采集是核心环节，传统排查方式依赖命令行操作，易触发安全软件误报，且多人远程登录主机存在密钥泄露、跳板机安全风险，同时远程无接入环境的服务器难以开展有效排查。`FireKylin`作为专为安全应急响应设计的系统痕迹采集工具，采用免安装运行模式，通过0命令采集机制降低拦截概率，分离采集端与解析端程序，仅需单人上机采集即可完成数据共享，有效解决传统应急排查的操作门槛高、安全风险大、场景适配性不足等问题，为安全事件研判提供可靠的数据支撑。

**安装介绍**

```
●●●

地址：https://github.com/MountCloud/FireKylin
```

工具获取方式：

```
●●●

# 前往项目GitHub Release页面
# 下载对应系统版本的编译后程序包
# 包含Windows/Linux版本Agent程序与Windows版本GUI程序
```

工具无需本地安装，下载解压后可直接运行，`Agent`程序用于目标主机数据采集，`GUI`程序用于采集结果解析查看。

功能介绍

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJaaeVXVEMgtynOM195fPUIU1mt7Su4F11AjTdkwZyCWA9q35jTFOQZXeia2E26fib9YBicXZGK12BeFMZ5MsHzzBpNksk1tOickTA/640?wx_fmt=png&from=appmsg)

将`Agent`程序上传至目标`Windows`或`Linux`主机后直接运行，进入命令交互模式，可执行基础控制指令，核心指令如下：

```
●●●

start # 开启系统痕迹采集任务
exit # 退出Agent程序
print # 打印当前采集配置信息
ls # 打印当前采集配置信息
```

支持对采集任务进行开关配置，可自定义开启或关闭指定采集项，配置指令如下：

```
●●●

No=true|false # 全局开关采集任务
taskname=true|false # 开关指定名称的采集任务
config No # 查看全局采集配置帮助
config taskname # 查看指定采集任务配置帮助
config No.No=value # 修改全局配置参数值
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLJIhsvM4ic0Uq4X94hlzvnGwukNrZf5jo4WzWs3YUW9bfvzA4uOglEqYT2hpvqXYrbAWTnTa2KGrLWxPhlFFAffhfmT9uo4PMI/640?wx_fmt=png&from=appmsg)

支持自定义系统日志采集时间段，精准筛选所需日志数据，时间配置指令如下：

```
●●●

config syslog # 查看系统日志采集配置项
config syslog.begintime=TIME # 设置日志采集开始时间
config 7.begintime=TIME # 设置日志采集开始时间（简写格式）
config syslog.endtime=TIME # 设置日志采集结束时间
config 7.endtime=TIME # 设置日志采集结束时间（简写格式）
```

时间参数支持`yyyy-MM-dd HH`:`mm`:`ss`或`yyyyMMddHHmmss`格式，开始时间设为0表示不限制，结束时间设为0或`Now`表示不限制。

`Agent`程序完成采集后生成`.fkld`格式数据文件，将文件下载至本地，通过`Windows`平台`GUI`程序加载文件，可查看目标主机完整系统痕迹信息。

工具支持采集主机用户信息、进程信息、系统服务、开机启动项、网络连接信息、计划任务、系统日志，`Linux`系统还可采集历史命令数据，v1.4.0版本集成`FireDog`病毒检测引擎，支持进程内存、进程路径、链接库及自定义路径的病毒检测，所有采集与检测结果均通过`GUI`界面直观展示，助力安全人员完成事件排查与溯源工作。

我们建立了交流群，一起来交流吧！！！

![](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicLkq53AeInelxIX84UvU0tEVdKEF1Lex0bgxL5VXEDa5sp7Ft70qZnefIYDibxvexEPPrSqg9jNricY4gR4FWKIS76wLzGUzHOibo/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJVRBMdib7K3ZtqZv8Yl8uRmgwoJjcDRPibW9TfdiaaibJnTboUxTXo5C0iacxMHS0JnjVbGextpYnIfUquG9E3icJmibOWcPSVNJOOIk/0?wx_fmt=png)

网安工具库

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJVRBMdib7K3ZtqZv8Yl8uRmgwoJjcDRPibW9TfdiaaibJnTboUxTXo5C0iacxMHS0JnjVbGextpYnIfUquG9E3icJmibOWcPSVNJOOIk/0?wx_fmt=png)

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