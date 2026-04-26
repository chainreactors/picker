---
title: OpenSSH 10.3升级指南：漏洞修复+新特性，CentOS/Ubuntu一键脚本
url: https://mp.weixin.qq.com/s/6nqoI6MYk77KFFvCKTP9WQ
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:59:28.706260
---

# OpenSSH 10.3升级指南：漏洞修复+新特性，CentOS/Ubuntu一键脚本

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aj4fOOkmqMJNujc7KQVg0PT9RXW6ZHCS7f42JlBu1NbmcoCSFnsI2iaL2eRaKHvskSRib4GMCxYETX4qAeHPYRy0FicsLD0w1t6nAhMGMR2n1Q/0?wx_fmt=jpeg)

# OpenSSH 10.3升级指南：漏洞修复+新特性，CentOS/Ubuntu一键脚本

原创

ralap
ralap

网络个人修炼

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**继去年 10 月发布的 OpenSSH 10.2 版本之后，官方于 2026 年 4 月 2 日推出了 10.3 版本，先来关注一下主要更新内容。**

![](https://mmbiz.qpic.cn/mmbiz_png/aj4fOOkmqMIW7AdcS3jjuhlHJczib53pZqIOr548jiabDLL6sluicrebIsxBHGJCLSwTlnxRntENC1m0kggdK02KVEbqSTmufYAojWQq8dkiavo/640?wx_fmt=png&from=appmsg)

---

## 一、10.3 版本主要更新（重点）

##

* 修复一个 Shell 注入漏洞（特定场景下攻击者可通过用户名执行任意代码）
* 修复证书主体为空时被错误当成通配符匹配任意用户的安全问题
* 移除对老旧不重协商实现的支持
* scp 以 root 下载文件时，正确清除 SetUID/SetGID 位
* 新增 ~I 逃逸命令，以及 ssh -O conninfo 查看多路复用连接状态
* 支持 invaliduser 惩罚机制，可单独封禁无效用户名的暴力扫描
* ssh-keygen

  支持将 ED25519 密钥导出为 PKCS8 格式

本次更新漏洞影响有限，生产环境可按需升级，无需紧急处理。

---

## 二、CentOS 7 升级注意事项

##

[OpenSSH 9.6版本升级指南](https://mp.weixin.qq.com/s?__biz=MzkzMDQ0NzQwNA==&mid=2247484711&idx=1&sn=2c4ffa24b4bedbffbec2f374fd7df90b&scene=21#wechat_redirect)

**升级步骤与之前发布的《OpenSSH 9.6 版本升级指南》完全相同，只需将源码包换成 10.3 即可。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aj4fOOkmqMJzGAicu3YZtp9cnMPqYNruBtDjyTN9TTYDODEsudmcRMwckMCmcoia7KicsyPXGqdFtibUneiaAyeStz1GD3paeMPecMiccyP05ICRM/640?wx_fmt=png&from=appmsg)

---

###

## 三、Ubuntu 22.04 升级注意事项

Ubuntu 22.04 仓库自带最高 只到8.9p1

正常编译安装，直接重启服务即可，没有特殊操作。

![](https://mmbiz.qpic.cn/mmbiz_png/aj4fOOkmqMKqz86v5IX57fuhnpnhABh7q41QiaXK1QJYQKUFicBjF5Jzy9jYv1owNeqRIC1ic27znXX3Ftf7gZtKPEG23jRvPM8nVwrg1epBiaU/640?wx_fmt=png&from=appmsg)

参考以下最简脚本

```
#!/bin/bashcd /optapt install -y wget gcc make perl zlib1g-dev libpam0g-dev libssl-devwget https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-10.3p1.tar.gztar -zxvf openssh-10.3p1.tar.gzcd openssh-10.3p1./configure --prefix=/usr --sysconfdir=/etc/ssh --with-ssl-dir=/usr --with-pammake && make installsed -i 's/^#PermitRootLogin .*/PermitRootLogin yes/' /etc/ssh/sshd_configsed -i 's/^#PubkeyAuthentication .*/PubkeyAuthentication yes/' /etc/ssh/sshd_configsed -i 's/^#PasswordAuthentication .*/PasswordAuthentication yes/' /etc/ssh/sshd_configsystemctl daemon-reloadsystemctl restart sshsystemctl enable ssh
```

---

## 四、Ubuntu 24.04 升级（在线编译安装）注意事项

Ubuntu 24.04 仓库自带最高只到9.6p1

Ubuntu 24.04 默认使用了 socket 激活 方式监听 SSH。
如果编译安装完直接 systemctl restart ssh，可能会出现 旧 socket 仍然占用 22 端口，新版 sshd 起不来的情况。

正确操作顺序（编译安装完成后执行）：

```
systemctl stop ssh.socket 2>/dev/null || truesystemctl disable ssh.socket 2>/dev/null || truesystemctl daemon-reloadsystemctl restart ssh#先干掉 ssh.socket，避免它跟新版 sshd 抢端口，再正常重启 ssh 服务。
```

![](https://mmbiz.qpic.cn/mmbiz_png/aj4fOOkmqMKfDAXduslnwvVHErFdQV9GK9eYVVZKqQebjAdibF1WVngTnna89liaAg2JmlM3jCttRgt5d0M8e2HqiaiaO5bnQXJeFWT7PG7X3EE/640?wx_fmt=png&from=appmsg)

参考以下最简脚本

```
#!/bin/bashcd /optapt install -y wget gcc make perl zlib1g-dev libpam0g-dev libssl-devwget https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-10.3p1.tar.gztar -zxvf openssh-10.3p1.tar.gzcd openssh-10.3p1./configure --prefix=/usr --sysconfdir=/etc/ssh --with-ssl-dir=/usr --with-pammake && make installsystemctl stop ssh.socket 2>/dev/null || truesystemctl disable ssh.socket 2>/dev/null || truesed -i 's/^#PermitRootLogin .*/PermitRootLogin yes/' /etc/ssh/sshd_configsed -i 's/^#PubkeyAuthentication .*/PubkeyAuthentication yes/' /etc/ssh/sshd_configsed -i 's/^#PasswordAuthentication .*/PasswordAuthentication yes/' /etc/ssh/sshd_configsystemctl daemon-reloadsystemctl restart sshsystemctl enable ssh
```

若想回退Ubuntu初始openssh版本执行以下命令

```
apt install --reinstall openssh-server openssh-client -y
```

---

参考链接

https://www.openssh.org/releasenotes.html#10.3

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5y2fUaoQPfKkAnrPt4lEpmGwWaLib4DxIATR0yiaZib3hQAtBDDAMUulZJL39cia5ttpCR5mbu0opYiawr47diaCwhFg/0?wx_fmt=png)

网络个人修炼

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5y2fUaoQPfKkAnrPt4lEpmGwWaLib4DxIATR0yiaZib3hQAtBDDAMUulZJL39cia5ttpCR5mbu0opYiawr47diaCwhFg/0?wx_fmt=png)

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