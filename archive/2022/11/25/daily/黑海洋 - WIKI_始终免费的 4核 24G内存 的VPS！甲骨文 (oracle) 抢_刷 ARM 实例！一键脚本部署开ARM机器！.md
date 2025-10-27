---
title: 始终免费的 4核 24G内存 的VPS！甲骨文 (oracle) 抢/刷 ARM 实例！一键脚本部署开ARM机器！
url: https://blog.upx8.com/3114
source: 黑海洋 - WIKI
date: 2022-11-25
fetch_date: 2025-10-03T23:44:22.273721
---

# 始终免费的 4核 24G内存 的VPS！甲骨文 (oracle) 抢/刷 ARM 实例！一键脚本部署开ARM机器！

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 甲骨文 (oracle) 抢/刷 ARM 实例 一键部署R探长

发布时间:
2022-11-24

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
50796

## 前言

前面为大家讲过了，如何 [申请一个甲骨文 (oracle) 的账号](https://blog.upx8.com/go/aHR0cHM6Ly92MnJheXNzci5jb20vb3JhY2xlLmh0bWw)！很多小伙伴们也是申请到了属于自己的免费的甲骨文 (oracle) VPS，在这里祝福大家。

相信大家在开实例的时候，也看到了很强悍的 ARM 的配置资源，最高可以达到 4核 24G 内存的免费资源。

> 官方原话：每个租户每月可免费获得前 3,000 个 OCPU 小时和 18,000 GB 小时，以使用 VM.Standard.A1.Flex 配置（相当于 4 个 OCPU 和 24 GB 内存）创建 Ampere A1 计算实例。每个租户还可以免费获得两个 VM.Standard.E2.1.Micro 实例。

我们今天就来看看，如何使用一键脚本，日以继夜的刷到自己心仪的、始终免费的甲骨文 ARM 资源！

## 视频教程

[https://www.youtube.com/watch?v=enfvqw0mMnI](https://blog.upx8.com/go/aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g_dj1lbmZ2cXcwbU1uSQ)

## 准备工作

1、VPS 一台（可以科学上网）推荐系统 Ubuntu、Debian

2、确定 VPS 9527 端口开放！可以通过 [**这里**](https://blog.upx8.com/go/aHR0cHM6Ly92MnJheXNzci5jb20vZ28_dXJsPWh0dHBzOi8vdG9vbC5jaGluYXouY29tL3BvcnQ) 检测

3、Telegram 账号一个，并关注 机器人（[R探长的小助理](https://blog.upx8.com/go/aHR0cHM6Ly92MnJheXNzci5jb20vZ28_dXJsPWh0dHBzOi8vdC5tZS9yYWRpYW5jZV9oZWxwZXJfYm90)）、（[R探长](https://blog.upx8.com/go/aHR0cHM6Ly92MnJheXNzci5jb20vZ28_dXJsPWh0dHBzOi8vdC5tZS9hZ2VudE9ORV9S)）

4、甲骨文免费云账号一个，若是没有，请看下面博文

* [始终免费的VPS！油管8K视频秒开，颠覆你对免费资源的看法。Oracle（甲骨文）免费云服务器注册指南及故障解决！](https://blog.upx8.com/go/aHR0cHM6Ly92MnJheXNzci5jb20vb3JhY2xlLmh0bWw)

## 甲骨文 ARM 机器脚本

GitHub 项目地址：[点击访问](https://blog.upx8.com/go/aHR0cHM6Ly92MnJheXNzci5jb20vZ28_dXJsPWh0dHBzOi8vZ2l0aHViLmNvbS9zZW1pY29ucy9qYXZhX29jaV9tYW5hZ2U)

### 获取 VPS INFO

我们打开 telegram，找到刚才关注的机器人，发送指令 `/sart`，开始！（若有什么疑问，可以发送 `/help`）

在输入框里面输入 `/raninfo`，为了防止误触，需要输入两次，机器人会返回两行字符串，这些是我们 VPS 的标识！

记录机器人返回的字符串（配置 VPS 会用到），这些字符串是机器人和 VPS 沟通的链条。

### 获取甲骨文 API 密钥

点击实例，甲骨文右上角的人头像（会员中心），来到会员中心（也就是更改密码的界面），找到左下角的 API 密钥，点击右边的添加 API 密钥。

点击上图的 “下载私有密钥”，并保存到本地设备，这样会得到一个 `****.pem` 的文件，这个是我们的 API 密钥文件，请妥善保管！

点击添加，会弹出 “配置文件预览” 的窗口，我们需要记录里面的：“配置文件预览”！

1. [DEFAULT]
2. user=ocid1.user.oc1..aaaaaaaa\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*nv77n556qwx4br34pmozcex3q
3. fingerprint=49:ab:\*\*:\*\*:\*\*:\*\*:\*\*:\*\*:\*\*:\*\*:\*\*:\*\*:\*\*:\*\*:\*\*:dd
4. tenancy=ocid1.tenancy.oc1..aaaaaaaaqxe77\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*mrdi2e4xd5dqcjssy2q
5. region=us-sanjose-1
6. key\_file= # TODO

完成以后，这样在 API 密钥里面我们可以看到刚才添加的 API 密钥（后续也可以点击后面的三点，来查看刚才的配置信息）

![](https://i.111666.best/image/v0qn0NZp9z7OyPI3FTVB1W.jpg)

### VPS 服务端部署

VPS 端的部署，就更为简单了，一键脚本搞定！

更新及安装组件

1. apt update -y #Debian/Ubuntu 命令
2. apt install -y curl tar wget #Debian/Ubuntu 命令

安装更新完毕以后，执行下面的一键安装脚本

1. wget -O gz\_client\_bot.tar.gz https://github.com/semicons/java\_oci\_manage/releases/latest/download/gz\_client\_bot.tar.gz && tar -zxvf gz\_client\_bot.tar.gz --exclude=client\_config && tar -zxvf gz\_client\_bot.tar.gz --skip-old-files client\_config && chmod +x sh\_client\_bot.sh && bash sh\_client\_bot.sh

脚本部署完毕以后，我们需要把刚才下载下来的 API密钥 文件 `****.pem`（或者是 `***.cer`），上传到 VPS ，并记录文件的路径。

我们可以需要编辑 VPS 如下文件：`/root/client_config`，如下图所示：

![](https://i.111666.best/image/rZ0QUEOUSXmyz8BCs46OPI.png)

确认配置文件无误以后，我们在 VPS 执行：`./sh_client_bot.sh`

![](https://i.111666.best/image/KFdSMSGq1WbChcC7o5DMH0.png)

这样，我们的 VPS 服务端就配置完成了。

### R探长的小助理

消息栏输入 `/oracle` (oracle云管理)，如下图所示：

![](https://i.111666.best/image/9fwsiSkBXoQbCUpw0jHVZI.png)

VPS 日志文件：/root/log\_r\_client.log

开机请务必记录 TG 的提示消息！（里面包含了你的 root 密码等 VPS 相关的参数）

其他就不用多说了，大家看到菜单，应该什么都会了！（带闪电的项目，需要捐赠，多多支持作者吧 ?）

![](https://i.111666.best/image/wZdB05E4CxABJwXHuftCrp.png)

若还是不会配置，**或是想听需要注意的一些事项**：[**观看视频教程**](https://blog.upx8.com/go/aHR0cHM6Ly92MnJheXNzci5jb20vZ28_dXJsPWh0dHBzOi8veW91dHUuYmUvZW5mdnF3MG1Nbkk)

#### 启动、终止、查看日志、卸载

```
请先在配置文件内输入对应的参数，然后运行下方需要的指令

启动或重启
bash sh_client_bot.sh

查看日志(ctrl + c退出日志)
tail -f log_r_client.log

终止程序
ps -ef | grep r_client.jar | grep -v grep | awk '{print $2}' | xargs kill -9

卸载程序
rm -rf gz_client_bot.tar.gz client_config r_client.jar sh_client_bot.sh log_r_client.log debug-.log
如也不需要JDK也可卸载：apt-get remove openjdk*
```

## 后记

> **转自脚本官方：**
>
> 暂未开源，介意请千万勿使用，谢谢
>
> 用途:本系统目前主要应用于甲骨文云的一些快捷操作，不排除将来实现更多功能
>
> 特殊声明：本系统为双端制，机器人不存储任何敏感数据，API 私钥在你的客户端服务器本地，由 bot 驱动你的客户端操作，你可以随时关闭服务

[取消回复](https://blog.upx8.com/3114#respond-post-3114)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")