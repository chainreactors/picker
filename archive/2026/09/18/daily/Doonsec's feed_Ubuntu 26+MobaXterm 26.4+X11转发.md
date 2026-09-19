---
title: Ubuntu 26+MobaXterm 26.4+X11转发
url: https://mp.weixin.qq.com/s/KQXMdgQfbMKOazPJT9LaCw
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:54:20.317278
---

# Ubuntu 26+MobaXterm 26.4+X11转发

# Ubuntu 26+MobaXterm 26.4+X11转发

原创

沈沉舟
沈沉舟

青衣十三楼飞花堂

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

```
创建: 2026-09-18 16:00
链接: https://scz.617.cn/unix/202609181600.txt
```

---

```
目录:

    ☆ X11架构简介
    ☆ X11 Forwarding简介
        1) SSH Server+X11 Proxy+X Client
        2) SSH Client+X Server(以MobaXterm为例)
        3) 在sudo/su之后继续访问之前的DISPLAY
        4) MobaXterm 26.4不支持"ssh -X"
    ☆ 实测若干GUI程序
        1) xterm
        2) firefox
        3) gedit
        4) ptyxis
    ☆ 参考资源
```

☆ X11架构简介

这是给普通用户的简版介绍。

传统\*nix系统的图形界面(GUI)基于X11协议，一出生就是C/S架构，有X Client、X Server两种角色。X Client负责运算，将画图指令通过X11协议交给X Server，X Server负责执行画图指令，将图形画出来。

当X Client、X Server位于同一Linux主机时，二者之间默认用AF\_UNIX套接字通信，以获得更高性能和安全性。

既然是C/S架构，X Server可运行在其他主机上。当二者位于不同主机时，X Server般侦听6000/TCP，X Client主动连接之。

☆ X11 Forwarding简介

假设从Windows用SSH登录Ubuntu 26，可启用X11 Forwarding，之后在SSH shell中启动X Client，X Client不会直接连接Windows的6000，而是通过SSH信道转发X11请求，复用SSH信道。X11转发，要求SSH Server、SSH Client予以配合。

1) SSH Server+X11 Proxy+X Client

Ubuntu 26的SSH Server缺省启用X11转发。触发X11转发时，SSH Server扮演X11 Proxy角色，动态侦听127.0.0.1:6010/TCP，这是X11转发端口，X Client会去连这个端口。

SSH Server会在SSH shell中自动设置DISPLAY环境变量，X Client靠此环境变量指引，去连X11 Proxy。

SSH Server提供的X11 Proxy不会永久侦听6010口，只在启用X11转发的SSH Client登录成功时，动态侦听6010口，生命周期同SSH Session。SSH Session结束后，SSH Server端没有6010口处于侦听状态。

2) SSH Client+X Server(以MobaXterm为例)

支持X11转发的SSH Client有许多种，本文以MobaXterm便携版举例说明，个人使用MobaXterm时无需License，可能有一些功能限制，但不在本文范围内。

MobaXterm便携版的ZIP包展开即用，无需安装。简单配置如下

```
Settings
  X11
    Automatically start X server at MobaXterm start up
      On
    Xorg version
      MobaX
    X11 server display mode
      Multiwindow mode (Transparent X11 server integrated in Windows desktop)
    Display offset
      0 (对应6000+0)
    X11 remote access
      disabled
```

---

```
User sessions
  New session (右键菜单)
    SSH
      Advanced SSH settings
        X11-Forwarding
          On
```

MobaXterm便携版每次启动时会临时释放出X Server对应的PE，就是它侦听6000。

用MobaXterm发起SSH登录，在SSH shell中启动X Client，初始TCP连接路径如下:

```
X Client -> X11 Proxy (Linux 6010) -> SSH信道 -> MobaXterm -> Windows 6000 -> X Server
```

X11通信经SSH信道到达Windows，无需调整Windows的防火墙策略，无需放行6000的入连接。Windows侧只会出现到127.0.0.1:6000的TCP连接请求，这个无需PFW放行。

3) 在sudo/su之后继续访问之前的DISPLAY

以scz身份SSH登录，启用X11转发，xterm正常弹出。但切换到root身份后，失败。有两个原因，一是缺DISPLAY环境变量，二是X Client没有认证凭据。解决如下

```
export DISPLAY=localhost:10.0
xauth add $(xauth -f ~scz/.Xauthority list | tail -1)
xterm&
```

4) MobaXterm 26.4不支持"ssh -X"

MobaXterm的各种组件都被阉割过，从一开始就没打算支持"ssh -X"。

```
a. GUI不提供-X选项
b. 后台Cygwin不提供xauth
c. X11转发默认"ForwardX11Trusted=yes"
d. 后台魔改的"ssh -vv"不提供真实日志
e. MobaXterm X Server不提供SECURITY扩展
```

这可能是基于商业考量，增加开箱即用的概率，避免陷入技术支持的泥潭。

☆ 实测若干GUI程序

1) xterm

最简测试，在SSH shell中执行xterm，Windows侧弹出xterm界面，整个过程非常透明。

2) firefox

Ubuntu 26的firefox是snap版本，想在X11转发场景中使用snap版firefox，必须确保
主控台logout中，再在SSH shell中执行

```
XAUTHORITY=~/.Xauthority firefox&
```

3) gedit

Ubuntu 26的gedit是基于GTK3的，若想在X11转发中弹出gedit，幺蛾子不少。

a. 假设主控台logout中，SSH shell中执行gedit，等十几秒后在Windows侧弹出，滞后明显。
b. 假设主控台login中，SSH shell中执行gedit，Windows侧不会弹出，居然在主控台弹出，这什么奇葩现象？注意，DISPLAY=localhost:10.0，指向X11 Proxy。

简单研究了一下，这些现象与gedit连接缺省Session/User Bus相关。为在Windows侧快速弹出gedit，其中一种方案是

```
unset DBUS_SESSION_BUS_ADDRESS
unset XDG_RUNTIME_DIR
gedit&
```

4) ptyxis

Ubuntu 26默认终端不再是传统的gnome-terminal，而是GTK4应用ptyxis。

在X11转发中测试ptyxis

a. 假设主控台logout中，SSH shell中执行ptyxis，等一分钟后在Windows侧弹出，滞后更明显。
b. 假设主控台login中，SSH shell中执行ptyxis，Windows侧不会弹出，在主控台弹出。

两种现象类似gedit。但不适用gedit的dbus快速弹出方案。目前只能忍受慢速弹出，至少可用，弹出后操作并不迟缓。

☆ 参考资源

```
https://mobaxterm.mobatek.net/
https://mobaxterm.mobatek.net/download-home-edition.html
```

---

```
How to keep X11 display after su or sudo - [2015-11-28]
https://blog.mobatek.net/post/how-to-keep-X11-display-after-su-or-sudo/
```

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPOa7YUszQ2zP2AFStE4UScicKMwhEqpde0j0FEheXVmbxSG8JFKDG3K8piaJjMHLjicL5zKemTibjvuQg/0?wx_fmt=png)

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