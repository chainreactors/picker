---
title: 3DS userland破解那些事
url: https://www.leavesongs.com/PENETRATION/talk-about-3ds-userland-flaw.html
source: 离别歌
date: 2023-06-10
fetch_date: 2025-10-04T11:44:14.476966
---

# 3DS userland破解那些事

* [主页](/)
* 返回

Back to top
Share post

# 3DS userland漏洞那些事

phithon

Jun 10, 2023, 1:48 AM

阅读：35734

[网络安全](/sort/PENETRATION)

[破解](/tag/%E7%A0%B4%E8%A7%A3),
[3ds](/tag/3ds)

我与掌机结缘是从初中时代就开始了，但严格意义上来讲，在我的少年时代，我是没有拥有过掌机的。小时候家里没有给我买过任何游戏机，但我曾拥有过一台学习机——名人Windows CE。虽然被冠以“学习机”的名义，但实际上这是一台搭载Windows CE系统的掌上电脑（PDA），在2008年那个智能手机还没有出世的年代，我竟拥有了一台跨时代的智能大屏设备。

当时我在CE上装了很多原生的Windows游戏，也装了不少模拟器，包括GBA、NES等等，这些游戏陪初中的我度过了许多个日夜。当然，这些就是另一个故事了，以后有机会再讲。

就是因为这段经历，所以我对掌机游戏其实一直有爱好，所以大概在2015年我买了自己人生第一台掌机，就是新大三（New 3DSLL）。当时在电玩巴士淘宝店购买的，到手就是破解好的状态。但当时的我对3DS破解这块一窍不通，以至于一度不敢随便升级它的系统，忍受老系统一堆堆的Bug，直到疫情期间我才摸索着研究了如何将它从A9LH升级到B9S破解，并升级了最新的系统。

今年（2023年）三月我去了趟东京，在中古店花了差不多国内一半的价钱拿下了一台老小三（Old 3DS）和一台新小三（New 3DS），至此我就拥有三台不同型号的3DS了。

[![3b9f5bd30cb2cbe665cd72b0b567a85.jpg](/media/attachment/2023/06/10/1fbdc6ac-42f3-4ad4-8fb2-916edaf4af26.fac8c5fa23a0.jpg)](/media/attachment/2023/06/10/1fbdc6ac-42f3-4ad4-8fb2-916edaf4af26.jpg)

差不多也就在这个月，任天堂正式关闭了3DS的eShop服务器，也就意味着3DS这款设备已经走向了生命周期的尽头。那么如今，回看十多年来安全研究者和任天堂官方的博弈，其实还是蛮有趣的。

自从有了游戏机，“破解”就一定是一个无法跳过的话题，现如今3DS的破解已经比较成熟了，大部分情况下都可以“软破解”——即在无需任何硬件辅助或修改的情况下完成破解。

这些软破解主要使用到了两层漏洞：

* 用户级（Userland）漏洞，攻击者需要首先通过一些用户级漏洞获取系统权限，才能进一步利用内核漏洞
* 内核级（Kernel）漏洞，利用内核漏洞即可加载自定义固件，最后再安装破解游戏

Boot9Strap就是利用内核级漏洞，在系统启动的Boot9阶段加载自定义代码，最后接管系统的控制权，进入用户自定义固件完成破解。这里面涉及的漏洞是硬件原因导致的，所以任天堂官方无法通过升级系统版本的方式修复Boot9Strap。

那么对于官方来讲，如果要与破解行为做对抗，则必须从用户级漏洞入手，让用户无法获得系统权限，也就无法安装Boot9Strap了。

本篇文章就来简单介绍一下，我们破解3DS的过程中都有使用到哪些用户级漏洞，以及官方与安全研究者的对抗过程。

## [Soundhax](#soundhax)

参考：

* [https://3ds.hacks.guide/installing-boot9strap-(soundhax)](https://3ds.hacks.guide/installing-boot9strap-%28soundhax%29)
* <https://github.com/nedwill/soundhax>

Soundhax漏洞是3DS中第一个免费、离线、稳定的漏洞与利用方法，利用涵盖了11.3以前的所有版本。

Soundhax实际上是一个Sound应用的堆溢出漏洞，Sound是3DS中的播放器，在播放恶意的m4a文件的过程中存在堆溢出漏洞，利用该漏洞就可以方便地在应用层执行任意代码。

我在日本买的Old 3DS就是通过这个方式破解，过程非常美妙。

该漏洞适配的3ds版本如下：

| Version | N3DS/N2DS | O3DS/2DS |
| --- | --- | --- |
| US 1.0-11.3 | ✓ | ✓ |
| JPN 1.0-11.3 | ✓ | ✓ |
| EUR 1.0-11.3 | ✓ | ✓ |
| KOR 4.0-11.3 | ✓ | ✓ |
| CHN 4.0-11.3 | N/A | ✓ |
| TWN 4.1-11.3 | N/A | ✓ |

## [Browserhax+SSLoth](#browserhaxssloth)

参考：

* <https://mrnbayoh.github.io/blog/exploiting-the-3ds-browsers-p1/>
* <https://mrnbayoh.github.io/blog/exploiting-the-3ds-browsers-p2/>
* <https://github.com/zoogie/old-browserhax>
* <https://github.com/zoogie/new-browserhax>
* <https://github.com/MrNbaYoh/3ds-ssloth>

这是以下三个漏洞的集合：

* old-browserhax
* new-browserhax
* ssloth

其中，old-browserhax和new-browserhax分别是Old 3DS和New 3DS使用的利用方式。虽然Old 3DS和New 3DS使用的浏览器存在区别（SPIDER和SKATER），但二者均基于老版本的Webkit，所以通过浏览器漏洞进行破解是常见操作。

old-browserhax对应的漏洞是[mrnbayoh](https://github.com/mrnbayoh)通过fuzz找到的UAF漏洞，new-browserhax对应的漏洞是[CVE-2013-2857](https://bugs.chromium.org/p/chromium/issues/detail?id=240124)。

由于使用了Webkit内核，3DS浏览器需要遵守LGPL开源协议将[源码](https://www.nintendo.co.jp/support/oss/index.html)开放下载，导致大量安全研究者可以直接通过代码审计的方式寻找漏洞。

对于层出不穷的浏览器漏洞，任天堂官方在9.9.0系统中增加了浏览器版本检查——3DS只有在升级了最新版系统后才能使用浏览器，这导致很多基于老版本浏览器漏洞的破解方式受到影响。

**SSLoth**漏洞就用来解决这个问题，它是存在于系统SSL模块中的一个漏洞，允许攻击者伪造证书，进而伪造任天堂官方服务器进行中间人攻击，让机器认为自己当前版本就是最新版，这样就可以使用浏览器了。

互联网上有一个使用了SSLoth搭建的公开代理服务器`192.9.234.11:8080`，只要将系统代理设置成这个服务器，即可完成版本欺骗攻击。结合这两个漏洞，打开浏览器即可触发漏洞。

SSLoth漏洞影响版本：

| Firmware | Version | N3DS/N2DS | O3DS/2DS |
| --- | --- | --- | --- |
| SAFE\_FIRM（3DS安全模式） | <11.15 | ✓ | ✓ |
| NATIVE\_FIRM | 1.0-11.13 | ✓ | ✓ |
| NATIVE\_FIRM | > 11.13 | ✗ | ✗ |

old-browserhax影响版本：

```
11.9.0-42 -> 11.13.0-45 for USA, EUROPE, JAPAN, KOREA, CHINA, TAIWAN (hbmenu and boot9strap)
11.10.0-43 -> 11.13.0-45 EUROPE (hbmenu and boot9strap)
11.4.0-37 -> 11.8.0-41 for USA, EUROPE, JAPAN (boot9strap only)
```

new-browserhax影响版本：

```
11.9.0-42 -> 11.13.0-45 for USA, JAPAN (hbmenu and boot9strap)
11.10.0-43 -> 11.13.0-45 for EUROPE (hbmenu and boot9strap)
11.9.0-36 -> 11.13.0-39 for KOREA (hbmenu and boot9strap)
11.4.0-37 -> 11.8.0-41 for USA, EUROPE, JAPAN (boot9strap only)
```

## [browserhax-XL+SSLoth](#browserhax-xlssloth)

参考：

* <https://github.com/zoogie/old-browserhax-XL/>
* <https://github.com/zoogie/new-browserhax-XL>

这个利用是old-browserhax和new-browserhax的继任者，因为这两个漏洞在11.14系统版本中被修复了，所以作者先尝试继续进行fuzz，并在SPIDER和SKATER中分别找到两个新的UAF漏洞并编写了利用。

当然，因为同样是浏览器漏洞，所以需要配合SSLoth使用。

值得注意的一点是，在11.14版本中其实SSLoth漏洞已经被修复了，无法直接在正常系统模式下使用；但是3DS有个安全模式（SAFE\_FIRM）仍然存在这个问题，我们重启系统时按住L+R+Up+A即可进入安全模式并联网更新。此时使用SSLoth漏洞劫持更新服务器，运行我们的利用即可。

这两个新漏洞生命周期都很短，只影响`11.14.0-46`，很快被修复。

## [Seedminer+BannerBomb3](#seedminerbannerbomb3)

参考：

* <https://github.com/zoogie/Bannerbomb3>
* <https://seedminer.hacks.guide/>

BannerBomb3是利用主机DSiWare数据管理中的一个漏洞，我们构造恶意的DSiWare备份并让主机加载，即可触发漏洞。

但是构造恶意DSiWare备份需要计算（爆破）出主机的加密密钥，需要一定的算力支持，可以在上面的网站中进行云爆破。

完整破解过程如下：

1. 数据收集： 首先，需要收集一些关键信息，包括用户的3DS友好码（Friend Code）和设备的可移动（movable）种子（一个关键的加密数据文件）。
2. 种子破解（Bruteforce）： 这一步是Seedminer破解的核心。这里利用一个称为“bruteforcemovable”的工具，通过尝试大量的可能性来破解用户可移动种子的LFCS（Local Friend Code Seed）。这个过程可能需要一些时间，因为需要在多个可能的种子中找到正确的一个。这是一个暴力破解（bruteforce）过程，通常需要借助GPU计算能力来加速。
3. 安装自制启动器（boot9strap）： 成功获取可移动种子后，使用一个名为“Frogtool”的工具将种子注入到一个特定的DSiWare游戏中。在这个过程中，会将DSiWare游戏修改为一个能够引导自制固件（如Luma3DS）的启动器。用户需要将这个修改过的游戏安装到3DS设备上。
4. 安装自制固件（如Luma3DS）： 通过修改的DSiWare游戏启动后，用户需要安装一个自制固件，通常是Luma3DS。自制固件允许用户运行未经任天堂官方认证的软件和游戏，实现更多的自定义功能。

原本这个Seedminer的漏洞是所有3DS破解的终极解，任何系统不用考虑前面所有的利用方法，直接将系统升级到最新版即可使用该方式破解。

但是2023年5月23日，任地狱突然给走向生命终结的3DS更新了新版系统11.17.0，在US/EU/JP地区修复了BannerBomb3漏洞。所以该漏洞最终影响版本仅为：

```
VERSION < 11.17.0-50 for US/EU/JP
```

## [super-skaterhax](#super-skaterhax)

参考：<https://github.com/zoogie/super-skaterhax>

前面的new-browserhax-XL被修复后，作者继续努力，找到了新的漏洞。不过这次作者只研究了New 3DS的浏览器SKATER，所以super-skaterhax这个利用仅限于New 3DS中。

这虽然仍是一个浏览器的UAF漏洞，但因为这个漏洞截止到今天（2023年6月9日）为止的最新版本11.17.0都没有修复，所以我们只需要把系统升级到最新版本即可，不再需要配合SSLoth漏洞使用。

漏洞影响版本：

```
11.15 - 11.17 on all 4 new3ds regions US,EU,JP,KR
```

这个漏洞就是目前为止New 3DS的终极解。

## [safecerthax](#safecerthax)

参考：

* <https://github.com/MrNbaYoh/safecerthax>
* <https://safecerthax.rocks/>

Old 3DS的安全模式（SAFE\_FIRM）基于非常老的3.0系统版本，所以很多新版本已经修复的漏洞可以通过安全模式继续利用。

safecerthax就是利用这个原理，在进入Old 3DS安全模式后，利用了5.0.0以前存在的一处漏洞（`PXIAM:ImportCertificates`堆溢出），在ARM9 CPU上执行任意代码（3DS有两块CPU，ARM9和ARM11）。

漏洞影响版本：

| Model | Firmware | Version | Vulnerable? |
| --- | --- | --- | --- |
| O3DS/2DS | SAFE\_FIRM | <11.15.0 | ✓ |
| O3DS/2DS | NATIVE\_FIRM | 1.0.0-4.4.0 | ✓ |
| O3DS/2DS | NATIVE\_FIRM | >=5.0.0 | ✗ |
| N3DS/N2DS | all | all | ✗ |

但这个漏洞也不是Old 3DS的终极解决方案，在11.15.0后被修掉。（修掉的应该是SSLoth，这点我不太确定）

~~所以，截止到2023年6月9日，在BannerBomb3不能使用的最新版11.17.0中，Old 3DS是无法软破解的。所以，如果你的机器是在这个版本以下，千万不要升级最新版。~~

## [MSET9](#mset9)

> 本章节于2024年5月20日更新

参考：

* [https://3ds.hacks.guide/installing-boot9strap-(mset9)](https://3ds.hacks.guide/installing-boot9strap-%28mset9%29)
* <https://github.com/zoogie/MSET9>

由于任天堂在2023年5月发布了11.17.0-50版本并修复Bannerbomb3，导致Old 3DS在该时间点变得无法软破解。2023年7月30日，Bannerbomb3的作者zoogie发布了最新破解方式MSET9，再次实现3DS全版本破解。

ID0和ID1是任天堂3DS中两个关键的目录名，ID1目录位于ID0目录下，正常来说这两个ID均为32位长度的十六进制字符串。MSET9利用了3DS在解析ID0文件名过程中出现的空指针漏洞，该漏洞导致处理器崩溃后，错误地将处理器指向了保存ID1字符串的内存空间中。而3DS并没有严格检查ID1文件名的内容，只要求长度等于32位，这样攻击者就可以将恶意代码设置为ID1文件名，并最终执行。

该漏洞对于3DS型号没有限制，可以利用在之前无法破解的Old 3DS中，影响的版本有：

```
11.4 - 11.17 on all regions
```

## [ntrboot+R4烧录卡硬破](#ntrbootr4)

参考：

* <https://3ds.hacks.guide/ntrboot>

这个就是最后的办法，如果上面的所有软破解方法都不能使用，比如最新版本Old 3DS，那么就只能使用硬破解的方式。

如果之前买过R4烧录卡，那么就不用在买额外的硬件设备，可以直接将ntrboot安装进烧录卡中。

然后通过磁铁，让3DS在启动时引导加载带ntrboot的固件，最后完成漏洞利用。

# 赞赏

喜欢这篇文章？打赏1元

![](/static/wx.jpg)

# 评论

![captcha](/captcha/image/c0a140bc6b55993beefdcb8d0d7320c70123a2b0/)

Copyright © 2025 Powered by talkbook

* [首页](/)
* [RSS订阅](/feed/)
* [微博](http://weibo.com/101yx)
* [项目](https://github.com/phith0n)
* [更换模板](/template/change/)