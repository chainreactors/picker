---
title: 【攻防演练】Apollofish-安全风险演练平台V1.10更新（媲美Gophish）
url: https://mp.weixin.qq.com/s/wH1xkV5Axf2dbJDjfFpsxg
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:32:52.495038
---

# 【攻防演练】Apollofish-安全风险演练平台V1.10更新（媲美Gophish）

# 【攻防演练】Apollofish-安全风险演练平台V1.10更新（媲美Gophish）

原创

亦
亦

Polaris安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明

由于传播、利用Polaris本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，仅记录学习、宣传网络安全意识使用。

## 平台简介

阿波罗钓鱼演练平台（ApolloFish）是一款专注于企业安全意识提升的模拟演练平台，支持Windows、Linux、macos、国产信创平台运行。通过仿真的钓鱼攻击场景（诱导网页、恶意邮件）形式，模拟真实风险环境，以此检验员工对钓鱼风险的识别与防护能力。最终帮助企业系统性强化全员网络安全意识，筑牢网络安全防线。

整体页面如下：

![](https://mmbiz.qpic.cn/mmbiz_png/anNjib1gD6SpOrvzL0Rmtw76FT0PBTpJyR2Xl9Qwwtzs96ZtBc8l7j3eZo2cQNIlmylDTviaDZeD3Cx8PrAvSgvAPb5fUB8mecBcibRt4EUEvE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/anNjib1gD6SppBMEsicplKqbK6HRcpOAyr0u1nHu8yht0Snb6peK2Dg4bfxicojefDoq7hdr45NskGuCJcDy2ibd47NbKKc30LJ8EGfTsW6UxBs/640?wx_fmt=png&from=appmsg)

## 部署方式

项目下载地址：

```
https://github.com/safe1024/apollofish/releases
```

阿波罗安全风险演练平台支持多系统运行，支持x86架构和arm架构。

```
若您是Windows，且CPU是Intel、AMD，请下载：ApolloFish_windows_amd64.exe
若您是Windows，且CPU是骁龙、联发科，请下载：ApolloFish_windows_arm.exe
若您是Macbook/Mac mini/Mac Studio，且CPU是Intel，请下载：ApolloFish_mac_amd64
若您是Macbook/Mac mini/Mac Studio，且CPU是M系列，请下载：ApolloFish_mac_arm
若您是Linux或基于Linux内核的国产信创系统，且CPU是Intel、AMD、海光系列，请下载：ApolloFish_linux_amd64
若您是Linux或基于Linux内核的国产信创系统，且CPU是鲲鹏系列，请下载：ApolloFish_linux_arm
```

命令行执行，例如:

```
./ApolloFish_windows_amd64.exe
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/anNjib1gD6Sqoy6ib2icol23puE1Y8ZRnoZdBsEOCK2wUJf0IyRBJ8MsIAkYNuFpibd0kSsb55PIISCMicFn7WBPY023OxVZ6JLn9dQYPpklzsSY/640?wx_fmt=webp&from=appmsg)

首次运行，会在同目录下生成config.yaml文件，并随机生成后台路径、登录账号、登录密码。请前往config.yaml文件中查看。

```
panel:
    path: 76cd36b08d6a11c2237f7be87075ce43
    port: 3333
    username: 9bqz38hz
    password: ky9je64t
```

使用浏览器访问平台后台，访问路径:

```
http://127.0.0.1:{panel.port}/{panel.path}/功能说明
```

# 更新说明

# 即1.10版本后，首次部署Apollofish仅需要确认使用授权：本平台仅用于已获得合法书面授权的网络安全意识提升、内部安全演练和防御能力验证；不用于未经授权的钓鱼、欺诈、骚扰、窃取凭证、入侵系统或任何违法活动。我对使用行为及后果承担全部责任。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/anNjib1gD6SpwYSDrDVOaFicZ0E7xXAZia3HrlGFkY1yRZJmWsQVpFuRwdlpvYSSE1ialKR8OL5noVkVbJQuVIdosZcHiaVXTiaOfQ5niarW66DIfg/640?wx_fmt=png&from=appmsg)

阅读完法律与用途声明后，手动输入使用承诺。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/anNjib1gD6Srx9Ml376sdEURyaiceV9QW4kIqmZP8aVj1R6h7ZJYCvwuuGm5zlCKaHtmLEJ86EMReib5TtQxibjcWW1najl0j53kTAE0m9ibTxTw/640?wx_fmt=png&from=appmsg)

# 完成使用承诺后，导入离线激活授权文件即可开始使用Apollofish进行开展安全风险演练。

# 访问Apollofish授权下载页

```
http://apollofish.safe1024.com
```

# 下载口令：Apollofish

![](https://mmbiz.qpic.cn/mmbiz_png/anNjib1gD6SoYk8Zn7EfU3cRb1tIYg6LPH9T4ZrCw9BXeJic36SlPWlLOGkvCFF4F5YxJgKoyiaMSkoNEC0XKdy6aicKBOKppv4B4GMjDj0oKvQ/640?wx_fmt=png&from=appmsg)

# 下载授权文件，导入Apollofish中，即可开始使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/anNjib1gD6SoAsOYsibfw7moCBd4Apxd6dVHRWwg4FQv4ibVdKE99lK2GGxic6Sa2jqre28Cv1ficyzpWPXwsSZor0ZrqAamPMiaJMneSTcaap5ow/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/anNjib1gD6SqVjZvJyba9qEDyPoJmFeKDGOx5ictyz8BcveZuPTcjegK4FhcqxEExvpBBErhIfjXiapClVQ3xnPzmxcfdOXD0zmABYIgwuRYbg/640?wx_fmt=png&from=appmsg)

# 更新后功能演示

# 推送日志：

![](https://mmbiz.qpic.cn/mmbiz_png/anNjib1gD6SrqNemV98aiaN4yuK6Pk9rrHhwBVLTvwc9pfXCdTL2E9vLlZjypkmQY4PAdsl9jqVHib8wA3xLHN2PFvJiad6zVc1AoOVbqSuyia7c/640?wx_fmt=png&from=appmsg)

上钩记录：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/anNjib1gD6SoicMSfBF9EXian2jjAeA6bANBwMh2sn4wT6pckb2ZTMgQRABjkTbleVDYX4Zo2CrFeA7oI5GOqhkNav9V2s1hUECj4Y0kicmm2Sk/640?wx_fmt=png&from=appmsg)

邮箱钓鱼：

![](https://mmbiz.qpic.cn/mmbiz_png/anNjib1gD6SpqbOEgmv2ICpg9vDFzcaTDOP2ibpIB7wrNraMFCCCNsOro4StuicwlG82hrmvErqWE5lg8ZrNpNl8PvSvPXxz4IkvECibMKtsXqM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/anNjib1gD6SqHj5fSGHe9ndXYvhSHJySFz2zquMNAonBiaticwIZeTVh5xiapgu6egXx2mrGxpqpH53hWKA14Yf31aVu4Sxj6sV9RsFcibw7QOpE/640?wx_fmt=png&from=appmsg)

内置Link附件-一键生成

![](https://mmbiz.qpic.cn/sz_mmbiz_png/anNjib1gD6SonTXuJHcvZZMz6xM74VmRf4dgQAIFXeu5GPuFzh2soA5T8hAtb2qj5VPCT6RIQxgLC9QtKYNmkiagDWyDtNjvZRf0UHKs2fUOk/640?wx_fmt=png&from=appmsg)

# Ai模板生成

![](https://mmbiz.qpic.cn/mmbiz_png/anNjib1gD6Spic5aZkye5RrZIIlcXRxWsTaciaxXNKDsjGIKlib4xEpoKcsZAibFT98Iedric6JiaicqiaCiaJFicRw6beznhbsJ2eShnCzWib1RAk6CYvM/640?wx_fmt=png&from=appmsg)

# 设置-配置大模型

![](https://mmbiz.qpic.cn/sz_mmbiz_png/anNjib1gD6Sq4fQF8n0QjL8SvTz1PyicuUcPpzyXYQt5kQzQDn6ElunicHrupibEeX4ZpdVbG5Yribt8kyk9zic85oeZJfFatDhVeCmzSAM1iaLpeY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/anNjib1gD6SrsJv1p6Cf2Kezw9icdwhwibh5SOffnbCib3jPqpI9laWU91MHNkBz64uZNd5eOHMvUfhLxo4I7aTPY7It7TjWwWIohsTzxtafbu4/640?wx_fmt=png&from=appmsg)

# 大屏优化

# 网页大屏

# 邮箱大屏

Apollofish后续将保持每月一次更新！永久免费维护~

项目地址：

```
https://github.com/safe1024/apollofish/releases
```

内部知识圈子

加入知识星球获取，若您使用本产品进行商业用途，请进行尊重劳动者创作。仅199，获取enterprise企业版。

1、加入知识星球可享受最新版本，功能更全面。内部更新更快，优先解决内部知识圈内成员问题，赠送一次，免费协助指导完成内部演练服务。

2、知识圈子邀请行业安全厂商病毒专家、反诈专家，定期分享最近钓鱼木马原理，揭秘最近钓鱼技术手段。

3、分享近年国内外最近钓鱼手段、Hw钓鱼案例。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/anNjib1gD6Sr9925OpoVEESn2VdIo6pS8bGsCbjsMD5aJ0pFx7bVdZMY9bmUPyYXdibuzNsgROzMncpWClBUjvawStibJfGtoLfxehlzibYB7Yc/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/blxFaPuVSrdkdNArXd903euUicWTicXE5ibCTp8abjOreZD4iaiajbWSPpPz2e8PSibcF6WIxfu4JictFR7rwEglVvIyQ/0?wx_fmt=png)

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