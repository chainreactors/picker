---
title: 反弹Shell执行pty泄露黑客命令记录？
url: https://zgao.top/%e5%8f%8d%e5%bc%b9shell%e6%89%a7%e8%a1%8cpty%e6%b3%84%e9%9c%b2%e9%bb%91%e5%ae%a2%e5%91%bd%e4%bb%a4%e8%ae%b0%e5%bd%95%ef%bc%9f/
source: Zgao's blog
date: 2025-07-15
fetch_date: 2025-10-06T23:17:13.868967
---

# 反弹Shell执行pty泄露黑客命令记录？

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# 反弹Shell执行pty泄露黑客命令记录？

* [首页](https://zgao.top)
* [反弹Shell执行pty泄露黑客命令记录？](https://zgao.top:443/%E5%8F%8D%E5%BC%B9shell%E6%89%A7%E8%A1%8Cpty%E6%B3%84%E9%9C%B2%E9%BB%91%E5%AE%A2%E5%91%BD%E4%BB%A4%E8%AE%B0%E5%BD%95%EF%BC%9F/)

[7月 14, 2025](https://zgao.top/2025/07/)

### 反弹Shell执行pty泄露黑客命令记录？

作者 [Zgao](https://zgao.top/author/zgao/)
在[[应急响应](https://zgao.top/category/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/)](https://zgao.top/%E5%8F%8D%E5%BC%B9shell%E6%89%A7%E8%A1%8Cpty%E6%B3%84%E9%9C%B2%E9%BB%91%E5%AE%A2%E5%91%BD%E4%BB%A4%E8%AE%B0%E5%BD%95%EF%BC%9F/)

```
python -c import pty; pty.spawn("/bin/bash")
```

做过渗透的小伙伴对这个命令都不会陌生，通常利用web漏洞进行反弹shell后，都会执行python的pty.spawn得到一个功能相对完善的伪终端，比如支持命令补全、使用vim等需要终端控制的程序。但是这也会导致攻击者执行过的命令被写入到当前用户的.bash\_history中。

文章目录

[ ]

* [凭空出现的history](#%E5%87%AD%E7%A9%BA%E5%87%BA%E7%8E%B0%E7%9A%84history "凭空出现的history")
* [没有SSH登录记录？](#%E6%B2%A1%E6%9C%89SSH%E7%99%BB%E5%BD%95%E8%AE%B0%E5%BD%95%EF%BC%9F "没有SSH登录记录？")
* [pty伪终端竟然会写入.bash\_history？](#pty%E4%BC%AA%E7%BB%88%E7%AB%AF%E7%AB%9F%E7%84%B6%E4%BC%9A%E5%86%99%E5%85%A5bash_history%EF%BC%9F "pty伪终端竟然会写入.bash_history？")
* [为什么主机安全记录的进程链会有ssh\_source？](#%E4%B8%BA%E4%BB%80%E4%B9%88%E4%B8%BB%E6%9C%BA%E5%AE%89%E5%85%A8%E8%AE%B0%E5%BD%95%E7%9A%84%E8%BF%9B%E7%A8%8B%E9%93%BE%E4%BC%9A%E6%9C%89ssh_source%EF%BC%9F "为什么主机安全记录的进程链会有ssh_source？")
* [探究：什么情况下pty会把命令记录写入history？](#%E6%8E%A2%E7%A9%B6%EF%BC%9A%E4%BB%80%E4%B9%88%E6%83%85%E5%86%B5%E4%B8%8Bpty%E4%BC%9A%E6%8A%8A%E5%91%BD%E4%BB%A4%E8%AE%B0%E5%BD%95%E5%86%99%E5%85%A5history%EF%BC%9F "探究：什么情况下pty会把命令记录写入history？")
  + [通过守护进程拉起](#%E9%80%9A%E8%BF%87%E5%AE%88%E6%8A%A4%E8%BF%9B%E7%A8%8B%E6%8B%89%E8%B5%B7 "通过守护进程拉起")
  + [SSH登录后执行](#SSH%E7%99%BB%E5%BD%95%E5%90%8E%E6%89%A7%E8%A1%8C "SSH登录后执行")

## 凭空出现的history

![](https://zgao.top/wp-content/uploads/2025/07/image-1-1024x550.png)

在今年的护网中，攻击队利用某组件的RCE漏洞拿到了云上服务器的权限，执行扫描的行为触发了主机安全的告警，联系客户后上机排查。

SSH登录后发现攻击队执行的所有命令记录都被写入到了history？

我们第一反应是攻击队通过漏洞拿到了权限后，进一步信息收集拿到SSH凭据后，直接通过SSH登录后执行的操作，但是还没有来得及清理痕迹就被关机了。

## 没有SSH登录记录？

初步推测攻击队如果是通过SSH登录操作的话，日志一定会有记录SSH的登录记录。

![](https://zgao.top/wp-content/uploads/2025/07/企业微信截图_471815c2-361c-4ebc-8601-5e803733d70d-1024x314.png)
![](https://zgao.top/wp-content/uploads/2025/07/企业微信截图_8a27e74b-6877-4694-a4e9-c02808516c2b-1024x237.png)

查看secure日志和last命令的记录，除了客户自己登录进行关机的操作，7月7号均未发现其他ip有登录过服务器的行为。

难道是攻击队定向删除过SSH的登录日志？我们又对全盘做了数据恢复，恢复出来的都是2023年的SSH日志，说明这段时间的SSH登录记录并没有被删除过。

为什么history凭空会记录攻击队执行过的命令记录？因为我们都知道正常的反弹shell后执行的命令是不会被记录的，那么究竟是如何触发的呢？

## pty伪终端竟然会写入.bash\_history？

为了找出凭空出现攻击队history的原因，我们又拉取了主机安全的高危命令告警进程树。

```
[
    {
        "pid": 24846,
        "exe": "/www/server/logs/ns",
        "account": "root:root",
        "cmdline": "./ns -h 192.168.1.1/16 -o 192.txt -d",
        "ssh_service": "10.80.12.42:22",
        "ssh_source": "172.18.164.245:59590",
        "start_time": 1751878635,
        "type": 1
    },
    {
        "pid": 6980,
        "exe": "/usr/bin/bash",
        "account": "root:root",
        "cmdline": "/bin/bash",
        "ssh_service": "10.80.12.42:22",
        "ssh_source": "172.18.164.245:59590",
        "start_time": 1751874803,
        "type": 2
    },
    {
        "pid": 6979,
        "exe": "/usr/bin/python2.7",
        "account": "root:root",
        "cmdline": "python -c import pty; pty.spawn(\"/bin/bash\")",
        "ssh_service": "10.80.12.42:22",
        "ssh_source": "172.18.164.245:59590",
        "start_time": 1751874803,
        "type": 3
    },
    {
        "pid": 6977,
        "exe": "/usr/bin/bash",
        "account": "root:root",
        "cmdline": "/bin/bash",
        "ssh_service": "10.80.12.42:22",
        "ssh_source": "172.18.164.245:59590",
        "start_time": 1751874803,
        "type": 4
    }
]
```

可以看到执行扫描动作的父父进程竟然是pty.spawn！说明攻击队拿到反弹shell后，通过执行pty.spawn后拿到功能完善的伪终端。在方便渗透的同时，伪终端也继承了父进程root用户的环境变量，将攻击队所有命令执行的记录写入到了.bash\_history，即便没有用SSH登录过。

估计攻击队也没有预料到自己所有的命令记录会被写入到history中。

## 为什么主机安全记录的进程链会有ssh\_source？

正常来说，反弹shell和SSH登录没有什么关系，为什么高危命令能够记录到ssh\_source？

经过沟通后发现，被攻击的这个漏洞组件并不是通过系统服务systemd拉起的，而是客户SSH登录到服务器后用root用户手动运行的。

所以通过父进程的关联就能拿到初始的父进程是通过SSH执行的。不然很容易被父进程误导，误以为是攻击队是通过SSH登录进来后执行的 `python -c import pty; pty.spawn(\"/bin/bash\")`。

## 探究：什么情况下pty会把命令记录写入history？

### 通过守护进程拉起

![](https://zgao.top/wp-content/uploads/2025/07/image-2.png)

### SSH登录后执行

![](https://zgao.top/wp-content/uploads/2025/07/image-3.png)

而本文出现的恰好是第二种情况，其实是否记录还是取决于当前pty继承的环境变量。

Post Views: 930

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 目前为止有一条评论

###### 匿名 发布于2:58 下午 - 7月 16, 2025

Pornhub的插件無法使用了，大哥能幫忙更新嗎? 謝謝

[回复](https://zgao.top/%E5%8F%8D%E5%BC%B9shell%E6%89%A7%E8%A1%8Cpty%E6%B3%84%E9%9C%B2%E9%BB%91%E5%AE%A2%E5%91%BD%E4%BB%A4%E8%AE%B0%E5%BD%95%EF%BC%9F/?replytocom=10613#respond)

### 发表评论 [取消回复](/%E5%8F%8D%E5%BC%B9shell%E6%89%A7%E8%A1%8Cpty%E6%B3%84%E9%9C%B2%E9%BB%91%E5%AE%A2%E5%91%BD%E4%BB%A4%E8%AE%B0%E5%BD%95%EF%BC%9F/#respond)

Δ

版权©2020 Author By : Zgao