---
title: 搭建x-ui最稳妥的科学上网节点
url: https://blog.upx8.com/3085
source: 黑海洋 - WIKI
date: 2022-11-13
fetch_date: 2025-10-03T22:38:07.968563
---

# 搭建x-ui最稳妥的科学上网节点

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# x-ui最稳妥的魔术面板

发布时间:
2022-11-12

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
427909

**最近经常有人被封端口，我自己搭的这个方案没被封过，现在分享出来。**

## 系统：Debian10-11

**首先要确保自己的vps是纯净的系统，不要商家预装的，在系统启动后操作DD重装脚本进行安装纯净版系统**

## 第一步：DD重装Debian10系统：

```
wget -N --no-check-certificate https://raw.githubusercontent.com/qingee/dd/master/InstallNET.sh && chmod +x InstallNET.sh && ./InstallNET.sh -d 10 -v 64 -p "notetoday" -port "22"
```

**系统root密码：`notetoday`**
**更改root密码：`passwd` 或者 `passwd root`输入你想要设置的密码即可，在ssh命令窗口输入密码`不显示是正常`的**

[一键DD纯净系统脚本 CentOS/Debian/Ubuntu](https://blog.upx8.com/go/aHR0cHM6Ly93d3cubm90ZXRvZGF5Lm5ldC9ub3RlLzEzLmh0bWw)

## 第二步：安装WARP接管VPS的出站ip（加入香港节点WireGuard异常：可以去[Github](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2ZzY2FybWVuL3dhcnAtc2g)）

> apt update
> apt install curl -y
> apt install gnupg2 -y
> apt install wget -y
> # 自动配置 WARP WireGuard IPv4 网络
> bash <(curl -fsSL git.io/warp.sh) 4
> echo "1" > /proc/sys/net/ipv6/conf/all/disable\_ipv6

**这个配置后你vps向外请求的所有ip都不是本机的真实ip，速度可能会有所影响，但是会很安全**

## 第三步： 安装适用于流媒体的XanMod内核开启BBR2（FQ+PIE）：

> 1. Register the PGP key:
>
> ```
> wget -qO - https://dl.xanmod.org/archive.key | sudo gpg --dearmor -o /usr/share/keyrings/xanmod-archive-keyring.gpg
> ```
>
> 2. Add the repository:
>
> ```
> echo 'deb [signed-by=/usr/share/keyrings/xanmod-archive-keyring.gpg] http://deb.xanmod.org releases main' | sudo tee /etc/apt/sources.list.d/xanmod-release.list
> ```
>
> 3. Then update and install:   **⇲**  Check platform compatibility in **x86-64 psABI level reference** below.
>
> ```
> sudo apt update && sudo apt install linux-xanmod-x64v3
> ```
>
> 4. Reboot.

**执行完命令代码后等待系统重启，重启完成后执行以下脚本开启`BBR2`**

> **`bash <(curl -Lso- https://git.io/kernel.sh)`**

[![2022-10-22T05:09:28.png](https://gcore.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/22/1666415368.png "2022-10-22T05:09:28.png")](https://gcore.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/22/1666415368.png "2022-10-22T05:09:28.png")
[![2022-10-22T05:13:42.png](https://gcore.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/22/1666415622.png "2022-10-22T05:13:42.png")](https://gcore.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/22/1666415622.png "2022-10-22T05:13:42.png")
[![2022-10-22T05:15:10.png](https://gcore.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/22/1666415710.png "2022-10-22T05:15:10.png")](https://gcore.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/22/1666415710.png "2022-10-22T05:15:10.png")
**再次运行上面的代码，查看参数是否和下图一样，如果是一样的就是开启成功了**
[![2022-10-22T05:17:17.png](https://gcore.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/22/1666415837.png "2022-10-22T05:17:17.png")](https://gcore.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/22/1666415837.png "2022-10-22T05:17:17.png")

## **第四步：安装x-ui面板**

```
bash <(curl -Ls https://gitlab.com/rwkgyg/x-ui-yg/raw/main/install.sh)
```

## **PS：安装VPS开源MW控制面板（要装就装，不装也没事）**

**使用这套配置操作，所有IP 都是CDNip**

[Linux主机开源面板：mdserver-web，完全免费，界面仿宝塔面板](https://blog.upx8.com/go/LzMwNTE)

```
curl -fsSL https://gcore.jsdelivr.net/gh/midoks/mdserver-web@latest/scripts/install.sh | bash
curl -fsSL  https://raw.githubusercontent.com/midoks/mdserver-web/dev/scripts/update_dev.sh | bash
```

[![2022-10-22T05:25:00.png](https://gcore.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/22/1666416300.png "2022-10-22T05:25:00.png")](https://gcore.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/22/1666416300.png "2022-10-22T05:25:00.png")
记住控制面板的信息登录上去后在安全里**`关闭防火墙`**

**`或者海外宝塔：[https://www.aapanel.com/new/download.html](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuYWFwYW5lbC5jb20vbmV3L2Rvd25sb2FkLmh0bWw)`**

1. ![登录进去显示Error: Request failed with status code 404怎么办  我用ip+端口](//q2.qlogo.cn/headimg_dl?dst_uin=815936687&spec=100)

   **登录进去显示Error: Request failed with status code 404怎么办 我用ip+端口**

   2024-11-27 11:43:42

   [回复](https://blog.upx8.com/3085/comment-page-1?replyTo=30279#respond-post-3085)

   登录进去显示Error: Request failed with status code 404怎么办 我用ip+端口
2. **[Ubuntu和Debian 初始化](https://blog.upx8.com/go/aHR0cHM6Ly93d3cudXB4OC5jb20vMzEyMA)**

   2024-08-17 23:35:00

   [回复](https://blog.upx8.com/3085/comment-page-1?replyTo=30069#respond-post-3085)

   [...]最近来来回回折腾了上百次服务器，每次折腾总要做一些重复的操作，挺麻烦，干脆记录一些常用操作，方便日后复制粘贴。一键网络DD脚本重装系统组件：apt-get install -y xz-utils openssl gawk file wget screen && screen -S os一键DD脚本：wget --no-check-certificate -O NewReinstal[...]
3. **[Ubuntu和Debian 初始化](https://blog.upx8.com/3120)**

   2024-06-06 13:59:13

   [回复](https://blog.upx8.com/3085/comment-page-1?replyTo=29701#respond-post-3085)

   [...]最近来来回回折腾了上百次服务器，每次折腾总要做一些重复的操作，挺麻烦，干脆记录一些常用操作，方便日后复制粘贴。一键网络DD脚本重装系统组件：apt-get install -y xz-utils openssl gawk file wget screen && screen -S os一键DD脚本：wget --no-check-certificate -O NewReinstal[...]
4. ![999](//q2.qlogo.cn/headimg_dl?dst_uin=1713106295&spec=100)

   **999**

   2023-07-13 20:09:23

   [回复](https://blog.upx8.com/3085/comment-page-1?replyTo=27366#respond-post-3085)

   博主大大，还有新的安装方法吗，这个已经失效了

   1. ![黑海洋](https://gravatar.loli.net/avatar/avatar/d13692d1a13aa29d5c6912c0e83a97e4?s=32&r=&d=)

      **[黑海洋](https://blog.upx8.com)**

      2023-07-14 10:22:39

      [回复](https://blog.upx8.com/3085/comment-page-1?replyTo=27369#respond-post-3085)

      没失效，检查服务器环境，因为链接的github的，如果是国内服务器用不了，或者自己换砖镜像链接

      1. ![999](//q2.qlogo.cn/headimg_dl?dst_uin=1713106295&spec=100)

         **999**

         2023-07-19 02:42:55

         [回复](https://blog.upx8.com/3085/comment-page-1?replyTo=27400#respond-post-3085)

         用了四个月IP被墙了，不知道怎么解冻IP
5. ![EmoTion](//q2.qlogo.cn/headimg_dl?dst_uin=895099991&spec=100)

   **EmoTion**

   2023-06-14 17:39:03

   [回复](https://blog.upx8.com/3085/comment-page-1?replyTo=27268#respond-post-3085)

   [ERR] 无法安装socat,请检查错误日志
6. ![张](//q2.qlogo.cn/headimg_dl?dst_uin=314922301&spec=100)

   **张**

   2023-06-04 15:08:02

   [回复](https://blog.upx8.com/3085/comment-page-1?replyTo=27233#respond-post-3085)

   咨询一下
7. ![a~ha](https://gravatar.loli.net/avatar/avatar/a96972ca26e3476454ced5eed70ab524?s=32&r=&d=)

   **a~ha**

   2023-05-24 02:59:38

   [回复](https://blog.upx8.com/3085/comment-page-1?replyTo=27191#respond-post-3085)

   请问一下，按照教程置好后，本地用v2rayN客户端连接，连接IP正常使用，连接域名就提示
   wsarecv: An existing connection was forcibly closed by the remote host.
   请问怎么处理 谢谢
8. ![james](https://gravatar.loli.net/avatar/avatar/3cdba8584261b4e6f3c98b66cbe43a46?s=32&r=&d=)

   **james**

   2023-05-23 19:00:32

   [回复](https://blog.upx8.com/3085/comment-page-1?replyTo=27186#respond-post-3085)

   bash
9. ![james](https://gravatar.loli.net/avatar/avatar/3cdba8584261b4e6f3c98b66cbe43a46?s=32&r=&d=)

   **james**

   2023-05-23 18:21:59

   [回复](https://blog.upx8.com/3085/comment-page-1?replyTo=27185#respond-post-3085)

   服务器没开通IPv6 Network可以吗？

   1. ![黑海洋](https://gravatar.loli.net/avatar/avatar/d13692d1a13aa29d5c6912c0e83a97e4?s=32&r=&d=)

      **[黑海洋](https://blog.upx8.com)**

      2023-05-23 21:53:36

      [回复](https://blog.upx8.com/3085/comment-page-1?replyTo=27190#respond-post-3085)

      of course
10. ![wuizl](//q2.qlogo.cn/headimg_dl?dst_uin=1713106295&spec=100)

    **wuizl**

    2023-04-19 01:09:06

    [回复](https://blog.upx8.com/3085/comment-page-1?replyTo=27092#respond-post-3085)

    请问安卓如何使用这个vmess节点

    1. ![雷锋](//q2.qlogo.cn/headimg_dl?dst_uin=545646&spec=100)

       **雷锋**

       2023-04-19 10:29:24

       [回复](https://blog.upx8.com/3085/comment-page-1?replyTo=27093#respond-post-3085)

       Matsuri.apk v2NG.apk Clash.apk

1. [1](https://blog.upx8.com/3085/comment-page-1#comments)
2. [2](https://blog.upx8.com/3085/comment-page-2#comments)
3. [后一页 »](https://blog.upx8.com/3085/comment-page-2#comments)

[取消回复](https://blog.upx8.com/3085#respond-post-3085)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral ...