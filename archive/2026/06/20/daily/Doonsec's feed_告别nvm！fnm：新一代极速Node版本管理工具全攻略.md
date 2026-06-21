---
title: 告别nvm！fnm：新一代极速Node版本管理工具全攻略
url: https://mp.weixin.qq.com/s/IpnzUCzpRc9DcNlAsALEHQ
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:48:16.518061
---

# 告别nvm！fnm：新一代极速Node版本管理工具全攻略

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RJrNBTwulveG8HiaLk4RwEmgSSoWLTZ8X3Q8r4QVrOviaSprk7EOicbsou5IHAAPaPOxAZ8HNpxVpeXiciayAA5iaj1BnRy79T51GUVzMXFHKtdOg/0?wx_fmt=jpeg)

# 告别nvm！fnm：新一代极速Node版本管理工具全攻略

原创

一只岸上的鱼
一只岸上的鱼

一只岸上的鱼

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 告别nvm！fnm：新一代极速Node版本管理工具全攻略

## 缘起

对于工具，我一直是比较专情（aka：懒）的，关于 Node ，一直是使用 nvm 来管理不同版本的。

理由很简单：

1. 这个工具我已经会用了
2. 这个工具满足了我的需求

这种情况下，大部分时候我都不愿意去尝试其他的工具

直到有一天，我终于忍受不了将nvm ls-remote 敲成nvm list available 的时候，我知道我对他的感情已经尽了😴

***简单解释***

nvm并不原生支持windows，需要使用nvm-windows来支持windows，但是nvm-windows的指令和nvm的一致性存在差异，让我很郁闷，例如上面说的，查询可用版本的时候，nvm-windows 的指令是 nvm list available，而 nvm 的指令是 nvm ls-remote。

## 介绍fnm

fnm，全称 **Fast Node Manager**，是一款用 **Rust** 编写的 Node.js 版本管理工具

然后还有人专门把他和nvm做了比对：

| 问题 | nvm 的短板 | fnm 的破局之道 |
| --- | --- | --- |
| **启动慢** | Shell 脚本执行，每次切换都像“加载动画” | Rust 编译为原生二进制，毫秒级响应 |
| **跨平台难** | Windows 需依赖 WSL，配置复杂 | 原生支持 macOS / Linux / Windows，无需折腾 |
| **配置繁琐** | 需手动配置 `.bashrc`/`.zshrc，`易出错 | 一键安装 + 自动注入，配置简单到“无感” |

1和3都是扯：谁频繁安装node，谁频繁切换node（一个新项目才切换一次），一台电脑才配置一次

然后2是我心动的，我有mac，大部分使用远程linux开发，但是我也是在放不下windows，他也许安全性性能都比不上mac和linux，但是他gui的响应性确实很习惯的，而且针对一些文档办公环境也更友好，所以我也很喜欢在windows下写代码。

## 安装

linux可以直接使用提供的安装脚本，windows使用winget：

```
# linux
curl -fsSL https://fnm.vercel.app/install | bash

#windows
winget install --id Schniz.fnm
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvfv0bz2GPPCNMHWRicbfAFDnf9C1aIQcyccpEwhjjJH3ic3PocIHBVibTKkezZLUDBKGeOssKJq8vZNGspQrSngWIbLrc6oPx7YWs/640?wx_fmt=png&from=appmsg)

## 使用

我对node办公管理工具的要求只有：安装卸载node、切换node环境

### 安装卸载node

```
# 查看可用版本
fnm list-remote

# 安装指定版本
fnm install v22.22.3

# 知道名字还可以不用查：安装最新lts版本
fnm install --lts
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvdQTop4nSv9W8Svib24sZvH1NzbZpqbvFakhaCic92MFW1vicdsFB6kdHRTLRHsiaTAsmzMCOxSpMxibIAQckzLX3FJNuBF8hSVfiaiag/640?wx_fmt=png&from=appmsg)

卸载

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvekjgQcGKIr52RIwIZU1G65JbwW5SIAJ5sdicYNjxITtPWtSzPRaD5d4P1RTjp0b7oc3L7oszG5In4Yadot7hric5z7wzygGXZqw/640?wx_fmt=png&from=appmsg)

### 切换node环境

```
# 查看已安装版本
fnm list

# 切换指定版本
fnm use v22.22.3
fnm use v24.17.0
```

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvdWrwrT2fkYwUH2kV6JhmDW9w7WzWN55c1mVxIfGbQz9QQVuRCzAs3lVibaXbGjGUnyGsObs8MQMMbyBTfhA0AxKR3c1aFhfzI8/640?wx_fmt=png&from=appmsg)

### 别名

这也是我常用的一个功能： 总有一些古董项目需要修复bug，版本要求也比较老，经常记不住，所以直接给他起一个项目的名字：

```
fnm list-remote|grep v16.20
fnm install v16.20.2
fnm alias v16.20.2 erp
fnm list
fnm use erp
```

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvda881uYZWARnfwNicFqHvKvuUb28JkYtnib088GPlgepBYDUbibpkyERB9P6ubELtkJzxL1tFXI6qSdm5WHZcDJlc4OVwXjvV5Og/640?wx_fmt=png&from=appmsg)

## 小结

终于准备告别nvm，全面拥抱fnm了

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ZG8Fru1tL1whh58JUwn0GLYzvqhGcECfmoW1O5J0JY0h7tksUWibmqwhwmEkL7kf1TTb37avJialEYsc7GfDhBCw/0?wx_fmt=png)

一只岸上的鱼

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ZG8Fru1tL1whh58JUwn0GLYzvqhGcECfmoW1O5J0JY0h7tksUWibmqwhwmEkL7kf1TTb37avJialEYsc7GfDhBCw/0?wx_fmt=png)

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