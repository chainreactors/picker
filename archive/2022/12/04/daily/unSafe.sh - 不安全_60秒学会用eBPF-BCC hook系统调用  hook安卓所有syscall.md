---
title: 60秒学会用eBPF-BCC hook系统调用  hook安卓所有syscall
url: https://buaq.net/go-138400.html
source: unSafe.sh - 不安全
date: 2022-12-04
fetch_date: 2025-10-04T00:28:22.558645
---

# 60秒学会用eBPF-BCC hook系统调用  hook安卓所有syscall

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

![](https://8aqnet.cdn.bcebos.com/daebc72bce4c1fc84afe5401d0f5cd38.jpg)

60秒学会用eBPF-BCC hook系统调用 hook安卓所有syscall

本文为看雪论坛优秀文章看雪论坛作者ID：爱吃菠菜( 1 ) 在Android手机上搭一个完整的ARM Linux来跑BCC在Android机上建立完整的Linux环境，然后去拉BCC项目运行bcc即可
*2022-12-3 17:59:58
Author: [mp.weixin.qq.com(查看原文)](/jump-138400.htm)
阅读量:33
收藏*

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8ErDZhhVA7zXnLAkicmAgB9DgNMqAULRkW3Eh1zpSAv576J3fXdibW6k453T3ZuNZH8KCE4I0LiazIYw/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：爱吃菠菜

( 1 ) 在Android手机上搭一个完整的ARM Linux来跑BCC

在Android机上建立完整的Linux环境，然后去拉BCC项目运行bcc即可，在这个完整的ARM Linux上跑bcc，和之前在x86 pc上跑bcc，过程没区别，搭好后ssh连上就ok。

目前的情况是，安装ARMLinux环境难题，已经被大佬解决了，下载他现成的工具，一个命令60秒就弄好了。用新内核的手机，没有门槛。

也就是说，没有要死磕内容，Android跑通BCC的门槛非常低，看一眼步骤3就学会。奥卡姆剃刀，直接充钱买个新小米/Pixel == 学会。
(本帖只讲这种方式)

( 2 ) 静态编译独立的二进制eBPF程序

第一种方式简单/敏捷，但缺点也明显，要运行eBPF程序，始终没法脱离那个armLinux BCC环境，每个新手机都要搭一个运行环境。

我们需要的可能是，编好一个eBPF程序,别人拿起来就用。(或反过来,捡大佬工具/模块)

实际上当前是有办法在x86PC机上，交叉编译二进制的eBPF程序的，不需要ARM Debian或是AOSP环境。(CORE / Compile Once Run Everywhere / 一次编译到处运行)

这篇帖子不涉及这类内容，但具体效果你可以参考和关注:
SeeFlowerX/stackplz（

*https://github.com/SeeFlowerX/stackplz*）
ehids/ecapture（*https://github.com/ehids/ecapture*）

eadb（*https://github.com/tiann/eadb*）

本文是对seeflower eBPF系列文章的copy和实践记录。

seeflower（*https://blog.seeflower.dev/archives/111/*）

本文是对好友maiyao1988/ebpf-plugin hook脚本的学习实践。

ebpf-plugin（*https://github.com/maiyao1988/ebpf-plugin*）

手机为Pixel 6 / Kernel 5.10，需要的内核功能默认已打开，开箱即用。

```
uname -a
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HHrGkwvdyJ3Al28aUgUDQudR03X9wlpsIEbfMvKZNFWpCX6xB9rdDZwCb5icrtVbohMPnkvSiapibCA/640?wx_fmt=png)

```
zcat /proc/config.gz | grep PROBE
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HHrGkwvdyJ3Al28aUgUDQu9dkiaE31d61YenugfQEJDyPJ8Idxkoh5w7jQxYnlCovpibN0IiaFTia3fg/640?wx_fmt=png)

**下载eadb和debianfs-arm64-full.tar.gz**

*https://github.com/tiann/eadb/releases*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HHrGkwvdyJ3Al28aUgUDQu9smbrMM9hAxo7pcaRN6icxF33sGiaynR0vOV8P2mkvf80jFH5MWzictiaw/640?wx_fmt=png)

**通过eadb安装debian环境**

```
./eadb --ssh [email protected] -p xxxx prepare -a debianfs-arm64-full.tar.gz
```

eadb是对adeb的重新实现(rust重写的)，eadb的作用是可以给Android安装一个完整健全的arm debian环境。
(注意：配置ssh密钥的过程这里略过，可通过Magisk模块完成。)

**安装后, 通过eadb ssh连接手机即可**

```
./eadb --ssh [email protected] shell
```

**4、在手机Debian中, 编译运行bcc helloworld**

**编译安装后, 运行helloworld测试**
可以跑的话，到这就算成功了，缺陷是还没有IDE，不方便开发。

```
cd /bcc/examplespython hello_world.py
```

**安装proxychains**
被墙的话，在手机Deabian里git和wget比较慢，还是要在手机Debian里配置proxychains之类的代理。

```
apt-get install proxychainsvim /etc/proxychains.conf# ---- 配置proxychains.conf ----socks5 192.168.?.?  12345  # 填写代理ip端口# ---- 配置proxychains.conf ----
```

**安装pip**

```
proxychains apt-get install python3-pip# 或者proxychains wget https://bootstrap.pypa.io/get-pip.pyproxychains python get-pip.py
```

**目的**
有了这个步骤，就可以不用eadb了，后面可以直接拿vscode ssh登录到手机的Debian上。

**在手机Debian中执行以下操作,配置ssh**

```
apt-get updateapt-get install sshvim /etc/ssh/sshd_config     # 编辑详细服务配置vim id_rsa.pub               # 手动粘贴导入公钥cat id_rsa.pub >> ~/.ssh/authorized_keyschmod 600 ~/.ssh/authorized_keyschmod 700 ~/.sshservice ssh restart          # 手机每次重启后,第一次进入debian,可能都需要手动启动下ssh服务
```

**sshd\_config的详细配置**

```
vim /etc/ssh/sshd_configAuthorizedKeysFile .ssh/authorized_keysPort 11111PubkeyAuthentication yesPermitRootLogin yesPasswordAuthentication yesGSSAPIAuthentication  no  # 加速SSHUseDNS no   # 加速SSH
```

**修改Debian的root密码**
需要重新修改Debian root密码，登ssh时需要。

```
passwd root
```

**PC客户端上配置一下私钥，然后连接测试**

```
$ ssh-add            # 密钥文件添加到ssh-agent$ ssh-add -L         # 检查$ ping 192.168.x.x   # 测试网络$ ssh [email protected]168.x.x -p 11111Enter passphrase for key '/home/ccc/.ssh/id_rsa':[email protected]168.x.x's password:Last login: Fri Nov 11 12:25:33 2022 from 192.168.x.x.The programs included with the Debian GNU/Linux system are free software;the exact distribution terms for each program are described in theindividual files in /usr/share/doc/*/copyright..Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extentpermitted by applicable law.[email protected]:~#
```

**6、通过VSCODE SSH登陆到手机Debian, 进行开发**

**安装vscode ssh插件**
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HHrGkwvdyJ3Al28aUgUDQuT8icCCl4yP6iarhNglY6W9lyzj5oIicoiakJHA8tUwtM93Tb8vG0nviaU4Q/640?wx_fmt=png)

**客户端ssh配置**
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HHrGkwvdyJ3Al28aUgUDQuK8hlvyHpugbPdicTsGPONzzo79IibtxCIxcC2zS2lLe1pn7028iaOLSqg/640?wx_fmt=png)

**连接后,可访问debian服务端上的文件,这个就是资源管理器**
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HHrGkwvdyJ3Al28aUgUDQuibEM9tH49r1mz4xmYxULic5RGzh7bqMFHoruOyAUNA2JZfA2hIkSkIwg/640?wx_fmt=png)

**打开bash**
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HHrGkwvdyJ3Al28aUgUDQutE4aCNWLUibB08o9NJU5yeRhjC0kibKWo7cv4u7BceX5jRZscRK1JQaQ/640?wx_fmt=png)

**安装Remote Development插件, 即远程开发插件**
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HHrGkwvdyJ3Al28aUgUDQu7IsLFnqcmGJCNdpxJ9JzdEty3G1UZKibLlEBbSiav64e6wklO9bVQI2A/640?wx_fmt=png)

**安装python插件**
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HHrGkwvdyJ3Al28aUgUDQuNvt0AM71k8Nlj72z7abniaaXn3FDvneX2GDLJdu81ncEE1LmAoND2hw/640?wx_fmt=png)

**如果要debug启动python脚本, 想传递参数的话, 需要配置一个启动文件**
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HHrGkwvdyJ3Al28aUgUDQuOlEf8eSo57lTOkS5FdnbdkRfF1yXIuEJupsjcttFoo0zPTTumYw1Eg/640?wx_fmt=png)

**配置中,你可能还需要补充一下环境变量**
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HHrGkwvdyJ3Al28aUgUDQu4KtRZfH0YEvk678c8AUicmMxeQOWmXfkRjqTD17TC3J2yiaWUEuE5yOw/640?wx_fmt=png)

```
"cwd": "${fileDirname}","env": {"PYTHONPATH": "${workspaceFolder}${pathSeparator}${env:PYTHONPATH}"},
```

**最后用这个配置文件,调试启动python脚本**
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HHrGkwvdyJ3Al28aUgUDQudmqFsY3LkBg5DC7jAxJiahuOq0KpNIPT2rRibNtPjjHVc3yxKEHesUTA/640?wx_fmt=png)

**项目推荐**
通过maiyao1988/ebpf-plugin项目，可一键一次性的HOOK全部syscall。代码逻辑清晰，可根据需求自由修改。(本文只关注eBPF亮点,无痕hook系统调用)**项目地址**

*https://github.com/maiyao1988/ebpf-plugin*

**在手机Debian上运行一下, 看看效果**

```
# mkdir bcc/my# cd bcc/my# git clone https://github.com/maiyao1988/ebpf-plugin# cd ebpf-plugin# python btrace.py -m64 -n com.android.bankabc
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HHrGkwvdyJ3Al28aUgUDQuqibxoTmNQ0hlBN2nRC6GzuibxxACQ6aSxwWXSxmo6j3OnaVsv20hXvrQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HHrGkwvdyJ3Al28aUgUDQuQn1po9A0dKPfLPuP4RZ1DpmOBffiakFbicD3552y0VOrLPvY0EvXRJUg/640?wx_fmt=png)

**看雪ID：爱吃菠菜**

https://bbs.pediy.com/user-home-760871.htm

\*本文由看雪论坛 爱吃菠菜 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EUvNq2rQycZibURG09OtYP0XCHXZ3icZXcMlqrP9xKN6J9cwRouvpXMfRrRxdE0xCpPmeqybJGOPibw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458479751&idx=1&sn=ca684920ebd23cc09080ba6eefb94165&chksm=b18e5c0d86f9d51b3b31b8a99231416b78566b3365abfbe25625aeba78a44b769576548b316f&scene=21#wechat_redirect)

看雪2022KCTF秋季赛官网：https://ctf.pediy.com/game-team\_list-18-29.htm

**#****往期推荐**

1.[CVE-2022-21882提权漏洞学习笔记](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471430&idx=1&sn=6a47d0c5c8f3f6204548e80977ecd059&chksm=b18e7c8c86f9f59a88d9b8e83c8297e0ef65034a73436998ab835531baadaa51f3d630793b95&scene=21#wechat_redirect)

2.[wibu证书 - 初探](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471429&idx=1&sn=a85188de9b9697fd1b9e708bb8bb1fdb&chksm=b18e7c8f86f9f59933d6cbf0040ed796f06e37b23f17f1ae842eb22257de02338e1a8d751f6b&scene=21#wechat_redirect)

3.[win10 1909逆向之APIC中断和实验](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471421&idx=2&sn=e83cf7220dc1c4c06a2efc78593e30cc&chksm=b18e7b7786f9f2614ecce34e23be7f71a3d3516766aabda8f25ae41c81ef359a2c245503cf86&scene=21#wechat_redirect)

4.[EMET下EAF机制分析...