---
title: 使用不限流量的cloudflare VPN并且自选IP
url: https://buaq.net/go-172162.html
source: unSafe.sh - 不安全
date: 2023-07-17
fetch_date: 2025-10-04T11:51:02.500509
---

# 使用不限流量的cloudflare VPN并且自选IP

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

![](https://8aqnet.cdn.bcebos.com/d1c6ade22fd60da8671c47a177532705.jpg)

使用不限流量的cloudflare VPN并且自选IP

前言优选IP速度不一定合适，目前github项目上面只有按照ping和丢包筛选节点，并且IP库不多，希望以后能有更多大佬做出更好的优选IP脚本，优选的I
*2023-7-16 21:55:0
Author: [blog.upx8.com(查看原文)](/jump-172162.htm)
阅读量:388
收藏*

---

## 前言

优选IP速度不一定合适，目前github项目上面只有按照ping和丢包筛选节点，并且IP库不多，希望以后能有更多大佬做出更好的优选IP脚本，优选的IP具有临时性，所以需要经常优选。并且本文教程不基于warp官方客户端，而是基于wireguard这个全平台工具，所以不管是windows还是ios等都适用。

## 1 优选IP

首先下载并解压文件：<https://tc.duangks.com/warpip.zip>

打开文件夹里面的**手动方式1：生成优选IP端口结果文件.bat**

然后等待结果，会提示**测试结果已经写入result.csv**

打开文件夹里面的**result.csv**，里面是优选好的IP，按照丢包和ping延迟排序，选择最上方的几个即可。

[![](https://tc.duangks.com/img/202307111335748.webp)](https://tc.duangks.com/img/202307111335748.webp)

我这里选择的是第一个，**162.159.192.235:1070**

记住这个IP

请注意，优选IP需要定期更换，甚至几小时就要换一次，所以大家最好自己定时优选IP

## 2 获取warp账号和WG配置

其实咱们自己注册的账号流量并不多，获取流量的方式有很多，包括cloudflare刚出的那个zero trust，或者自己找网站或者bot刷流量都行，今天咱们介绍一个最方便的方式，直接找机器人获取别人已经刷好的账号。
最过分的是昨天看到一个发卡网站卖warp不限流量的账户，一个要199，这不是糊弄傻子吗，手动搞一个账户一两分钟就完事。

telegram机器人：<https://t.me/generatewarpplusbot>

首先，使用你的账号私聊这个机器人，然后点击 /start ，后续的弹窗中会告诉你发送/generate获取账号，你需要关注机器人所在的两个频道才可以，而其中一个频道每天都会分享warp账户，直接复制那个频道里面的就可以，当然也可以继续使用这个机器人，关注完成验证以后，继续发送/generate，机器人会要求你验证，比如我的验证问题是5×1，那就根据机器人给的格式，发送/generate 后面跟上答案，我这里就是/generate 5。机器人就会返回给你 1.1.1.1的账户的key。

[![](https://tc.duangks.com/img/202307111024524.webp)](https://tc.duangks.com/img/202307111024524.webp)

图上给出的wg-config.conf就是wireguard的配置文件。

鼠标放到文件上，右键另存为一个位置。

## 3 wireguard配置

首先去下载wireguard并安装：<https://www.wireguard.com/install/>

选择刚刚保存的wg-config.conf导入配置文件。

右键点击wireguard里面的配置文件，选择**编辑所选隧道**

[![](https://tc.duangks.com/img/202307111336813.webp)](https://tc.duangks.com/img/202307111336813.webp)

将图中深色的区域换成刚刚优选的IP，点击保存。

[![](https://tc.duangks.com/img/202307111355359.webp)](https://tc.duangks.com/img/202307111355359.webp)

回到wireguard，点击连接即可科学上网。如果速度不理想可以多换几个IP试一下。

下面是我优选以后的油管速度

[![](https://tc.duangks.com/img/202307111342528.webp)](https://tc.duangks.com/img/202307111342528.webp)

## 安卓和IOS使用

由于wireguard是通用客户端，咱们的配置也是通用配置，所以上面的配置文件是通用的，如果你有windows电脑，直接将优选后的wireguard的配置文件界面右键-导出所有隧道，然后传给手机，手机上安装好wireguard客户端，导入文件，即可使用。

下面咱们讲一下没有windows电脑的时候如何优选IP。

### IOS使用

IOS区的wireguard需要使用美区账号下载，这个是没办法跳过的。
IOS优选IP需要去商店下载ISH shell这个软件，然后打开，输入命令 `apk add openssh curl bash` 然后回车等待依赖安装完成，然后执行下面的命令

`curl -sSL https://gitlab.com/rwkgyg/CFwarp/raw/main/point/endip.sh -o endip.sh && chmod +x endip.sh && ./endip.sh` 然后回车

把优选出来的IP第一个，复制粘贴到wireguard配置的对端地址里。

### 安卓使用

和IOS使用大同小异，需要下载wireguard软件，这里从官网下载即可<https://www.wireguard.com/install/>

下载软件termux，选择后缀为arm64-v8a.apk的版本下载。

然后打开软件，升级依赖。

`pkg upgrade` 然后回车

然后同样输入命令

`curl -sSL https://gitlab.com/rwkgyg/CFwarp/raw/main/point/endip.sh -o endip.sh && chmod +x endip.sh && ./endip.sh` 然后回车

把优选出来的IP第一个，复制粘贴到wireguard配置的对端地址里。

## 如何用密钥获取wireguard配置文件

如果你从别的渠道获取的warp密钥，想要自己生成wireguard配置文件，可以使用下面的网站

[https://replit.com/@ygkkkk/WARP-Wireguard-Register](https://replit.com/%40ygkkkk/WARP-Wireguard-Register)

首先输入2，然后输入2，将我们刚刚获取的warp+账户的许可密钥填写进去

[![](https://tc.duangks.com/img/202307111403098.webp)](https://tc.duangks.com/img/202307111403098.webp)

即可生成wireguard配置。

## 海外无限流量高速上网教程

一份网友写的**Warp自选IP海外无限流量高速上网教程**：**使用不限流量的cloudflare V某N并且自选IP**，教程不基于warp官方客户端，而是基于wireguard这个全平台工具，所以**不管是windows还是ios等都适用**，教程不长也不难，有截图步骤，感兴趣的同学可以试试，或者使用以前发过一遍也不错：[自动获取1.1.1.1 Warp+ 24PB 无限流量密钥 出海无忧](https://blog.upx8.com/3423)

文章来源: https://blog.upx8.com/3693
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)