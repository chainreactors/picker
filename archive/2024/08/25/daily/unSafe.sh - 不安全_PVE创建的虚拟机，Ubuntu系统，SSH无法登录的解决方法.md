---
title: PVE创建的虚拟机，Ubuntu系统，SSH无法登录的解决方法
url: https://buaq.net/go-257994.html
source: unSafe.sh - 不安全
date: 2024-08-25
fetch_date: 2025-10-06T18:01:54.634346
---

# PVE创建的虚拟机，Ubuntu系统，SSH无法登录的解决方法

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

![]()

PVE创建的虚拟机，Ubuntu系统，SSH无法登录的解决方法

无法SSH的问题是Ubuntu的安全选项问题，只需要修改ssh配置文件即可在编辑之前,输入date获取一下时间、如果时间对不上则需要同步一下时区sudo
*2024-8-24 23:13:20
Author: [www.upx8.com(查看原文)](/jump-257994.htm)
阅读量:33
收藏*

---

无法SSH的问题是Ubuntu的安全选项问题，只需要修改ssh配置文件即可

在编辑之前,输入`date`获取一下时间、如果时间对不上则需要同步一下时区

直接在PVE的控制台中编辑

```
# 修改sshd配置文件
vi /etc/ssh/sshd_config

# 需要修改的内容
PermitRootLogin no 改 PermitRootLogin yes //不存在就自行添加
PasswordAuthentication no 改 PasswordAuthentication yes
```

然后重启
`reboot`

如还是无法连接，则需要重新安装SSH，执行以下命令选第一个（很多人安装系统的时候，为了精简，一堆依赖没勾选安装，所以导致无法登录，一直在主路由网络找原因。）
`sudo apt-get install --reinstall openssh-server`

然后大概率就可以连接了！

文章来源: https://www.upx8.com/4296
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)