---
title: 一键DD云虚拟机云容器云桌面云开发
url: https://buaq.net/go-152248.html
source: unSafe.sh - 不安全
date: 2023-03-07
fetch_date: 2025-10-04T08:47:24.326324
---

# 一键DD云虚拟机云容器云桌面云开发

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

![](https://8aqnet.cdn.bcebos.com/224b7773230d381d1c628f374cb975f7.jpg)

一键DD云虚拟机云容器云桌面云开发

onekeydevdesk是一套可在线一键安装系统的脚本和os最小核心，及一套学习编程的语言最小选型方案。作为onekeydevdesk的安装脚本部分
*2023-3-6 21:47:49
Author: [blog.upx8.com(查看原文)](/jump-152248.htm)
阅读量:20
收藏*

---

onekeydevdesk是一套可在线一键安装系统的脚本和os最小核心，及一套学习编程的语言最小选型方案。

* 作为onekeydevdesk的安装脚本部分，基于debianinstaller增强,1keydd支持扩展多机型安装多OS类型，支持自打包，自托管，可将你对应机型包括镜像在内的整个DD方案构建为一个可供DD安装的在线仓库,甚至包括生成编辑镜像在内的全套dd支持方案
* 作为onekeydevdesk的os核心，基于pve增强+racketlang，onekeydevdesk实现了一套统一透明ve+一套统一语言（作为pve的developermode存在），可将你的日用os接入onekeydevdesk核心，变成可一键安装，可同步可集群的容器多版本的虚拟机。

> onekeydevdesk也指代：1keydd,1keynotedevdesk,1keydevabledocker,1keydiskdump,1keydeepindsm,1keydebiandesk,1keydevdeploy,1keydebugdemo,1key desk dock,1key datacenter and desk,1key dir disk,1key deconterized desk,1kilometer distance to dev,1key for dev over dev(second dev),etc ..

项目地址：https://github.com/minlearn/onekeydevdesk

## 演示与特性

1keydd支持多种在线安装方式(wgetdd,liveuntar,nc)，双进度显示(vnc,web)，支持双架构amd,arm，支持自扩硬盘和智能嵌入静态ip参数(包括/32这样的特殊掩码支持)，支持免d坏模式，可达成90%的linux成功率,80%的other os成功率

1keydd支持一键dd多种os，如，支持win uefi/bios gpt二合一兼容，无视机型差别和无须手动，毫无修改毫无感知地以同一效果运行,支持dsm直接安装在云主机上，dsm无须嵌套虚拟化支持>2T硬盘作为启动硬盘,支持osx使用标准全套kvm驱动和bios机型配置，需要安装在支持嵌套虚拟化的2C2G以上云主机上（1c1.5g/2c2g给osx, 2c2g/3c3g给osx母鸡留1c1g最好），与本地组matedesk，win11类同。
![](https://github.com/minlearn/minlearnprogramming/raw/master/_build/assets/1keydevdeskwin.png) ![](https://github.com/minlearn/minlearnprogramming/raw/master/_build/assets/1keydevdeskdsm.png) ![](https://github.com/minlearn/minlearnprogramming/raw/master/_build/assets/1keydevdeskosx.png)

1keydd支持一键dd devdeskos，devdeskos是onekeydevdesk的shell os，作为范例存在。 ![](https://github.com/minlearn/minlearnprogramming/raw/master/p/_contents/assets/intro/1keydirdisk.png)

1keydd+devdeskos支持扩展，包括az,servarica,oracle/oracle arm,ksle,bwg10g512m,及无限增加的机型和系统：

| 机型 | 是否支持裸机win | 是否支持裸机linux/devdeskos | 是否支持裸机osx | 是否支持pveosx | 是否支持静态ip嵌入 | 是否支持win中d win |
| --- | --- | --- | --- | --- | --- | --- |
| azure b1s | √ | √ | × | × | √ | × |
| spartan | √ | √ | × | × | √ | × |
| ikoula c-mem | √ | √ | × | √ | √ | × |
| ksle/ksleplus | √ | √ | × | √ | √ | × |
| SYS-2-SSD-64 | √ | √ | × | √ | √ | × |
| gcp | √ | √ | × | × | √ | × |
| linode | √ | √ | × | × | √ | × |
| orc amd | √ | √ | × | × | √ | × |
| orc arm | × | √ | × | × | √ | × |
| … | … | … | … | … | … | … |

完整支持查看hub页，更多演示和特性请看和项目文档库[《更多文档》](https://minlearn.org/onekeydevdesk/docs/)部分

## 下载安装及用法

以下尽量在debian系linux云主机或本地虚拟机下完成,centos不推荐

基本用法:

* 简单前端交互模式
  `wget -qO- 1keydd.com/inst.sh | bash`
* 指定安装目标os镜像：debian是原生方式安装的纯净debian10,devdeskos是live方式安装的devdeskos,debian10r是dd方式安装的debian10的raw系统硬盘格式经过gzip打包,自定义镜像是dd方式安装的raw系统硬盘格式经过gzip打包后托管的http/https地址（ 安装演示：https://www.bilibili.com/video/BV1ug411N7tn/ https://www.bilibili.com/video/BV17B4y1b79Y/ ）
  `wget -qO- 1keydd.com/inst.sh | bash -s - -t debian,devdeskos,debian10r,或自定gz镜像`

dd过程中，如有网络直接访问ip:80，会看到vnc进度，如果要进一步查看问题，用sshd用户无密码方式访问ssh或访问ip:8000。如无网络5分钟后会重启,并进入DD前的正常系统。免破坏系统。 目标os安装后，会自动扩展磁盘空间和调整网络,用户名为root/admininistraor，密码为1keydd，不做说明的情况下，上述镜像均为脚本内置镜像，第三方gz镜像并不提供开放托管和安装。

高级用法:

* 指定debian镜像源
  `wget -qO- 1keydd.com/inst.sh | bash -s - -m http/https/xxxx ......`
* 指定第一张网卡名
  `wget -qO- 1keydd.com/inst.sh | bash -s - -i enp0s1 ......`
* 指定静态网络配置（ 安装演示：https://www.bilibili.com/video/BV1pr4y1j75w/ ）
  `wget -qO- 1keydd.com/inst.sh | bash -s - -n ipv4,netmask,gateway .....`
* 指定第一个硬盘名(你也可以填分区名把镜像d到仅一个分区里)
  `wget -qO- 1keydd.com/inst.sh | bash -s - -p nvme0n1 ......`
* 指定grub启动分区(支持deb和devdeskos,tarball需要镜像配合)
  `wget -qO- 1keydd.com/inst.sh | bash -s - -e nvme0n1 ......`

更多模式:

* 进入dump模式：提供blkdevname:ip:port参数形式将作为源端/发送端/连接端/客户端(请自备开启了nc port:保存形态，作为参数的目标端/接收端/本地代理端/守护服务端的被DD机器，并首先开启)
  `wget -qO- 1keydd.com/inst.sh | bash -s - -t dumpblkdevname:sendtoip:sendtoport`
* 进入救援/DRYRUN/DEBUG模式,此模式HOLD不重启不插入改写硬盘的操作,可作DD前验证
  `wget -qO- 1keydd.com/inst.sh | bash -s - -d`

自托管1keydd:

* 通过git仓库:
  `fork本仓库后,新的debian镜像源将变成https://github.com/你的用户名/onekeydevdesk/raw/master'`
  `或修改inst.sh头二行debian镜像源地址export autoDEBMIRROR0,export autoDEBMIRROR1为你的仓库对应debian镜像源地址,或修改export FORCEMIRROR指定为新的镜像源地址`
* 通过docker:
  `docker pull minlearn/onekeydevdesk`
  `docker run -d --name myonekeydevdesk -e m=你的新debian镜像源地址 -p 80:80 minlearn/onekeydevdesk`

建立托管后，用新的inst.sh脚本地址调用脚本即可

## 服务

免费

* 只提供inst.sh，可一站式解决你DD中大部分问题，去上面仓库，一键DD即可
  `注：仅拥有常见vps和独服机型上DD常见系统能力`

文章来源: https://blog.upx8.com/3250
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)