---
title: Ubuntu 26+MobaXterm 26.4+X11转发
url: https://blog.nsfocus.net/ubuntu-26mobaxterm-26-4x11%e8%bd%ac%e5%8f%91/
source: 绿盟科技技术博客
date: 2026-09-28
fetch_date: 2026-09-29T07:40:21.961827
---

# Ubuntu 26+MobaXterm 26.4+X11转发

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)
* [登录](https://blog.nsfocus.net/wp-login.php)

* [首页](https://blog.nsfocus.net)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* Ubuntu 26+MobaXterm 26.4+X11转发

# Ubuntu 26+MobaXterm 26.4+X11转发

[0](https://blog.nsfocus.net/ubuntu-26mobaxterm-26-4x11%E8%BD%AC%E5%8F%91/#comments)

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=40&d=identicon&r=g) [NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "written 2026-09-2811:30") 发布于 1 天前

![](https://blog.nsfocus.net/wp-content/uploads/2026/05/bb.jpg)

阅读： 28

创建: 2026-09-18 16:00
更新:
链接: https://scz.617.cn/unix/202609181600.txt

————————————————————————–

目录:

☆ X11架构简介
☆ X11 Forwarding简介
1) SSH Server+X11 Proxy+X Client
2) SSH Client+X Server(以MobaXterm为例)
3) 在sudo/su之后继续访问之前的DISPLAY
4) MobaXterm 26.4不支持”ssh -X”
☆ 实测若干GUI程序
1) xterm
2) firefox
3) gedit
4) ptyxis
☆ 参考资源

————————————————————————–

☆ X11架构简介

传统\*nix系统的图形界面(GUI)基于X11协议，一出生就是C/S架构，有X Client、X
Server两种角色。X Client负责运算，将画图指令通过X11协议交给X Server，X
Server负责执行画图指令，将图形画出来。

当X Client、X Server位于同一Linux主机时，二者之间默认用AF\_UNIX套接字通信，
以获得更高性能和安全性。

既然是C/S架构，X Server可运行在其他主机上。当二者位于不同主机时，X Server
般侦听6000/TCP，X Client主动连接之。

☆ X11 Forwarding简介

假设从Windows用SSH登录Ubuntu 26，可启用X11 Forwarding，之后在SSH shell中启
动X Client，X Client不会直接连接Windows的6000，而是通过SSH信道转发X11请求，
复用SSH信道。X11转发，要求SSH Server、SSH Client予以配合。

1) SSH Server+X11 Proxy+X Client

Ubuntu 26的SSH Server缺省启用X11转发。触发X11转发时，SSH Server扮演X11
Proxy角色，动态侦听127.0.0.1:6010/TCP，这是X11转发端口，X Client会去连这个
端口。

SSH Server会在SSH shell中自动设置DISPLAY环境变量，X Client靠此环境变量指引，
去连X11 Proxy。

SSH Server提供的X11 Proxy不会永久侦听6010口，只在启用X11转发的SSH Client登
录成功时，动态侦听6010口，生命周期同SSH Session。SSH Session结束后，SSH
Server端没有6010口处于侦听状态。

2) SSH Client+X Server(以MobaXterm为例)

支持X11转发的SSH Client有许多种，本文以MobaXterm便携版举例说明，个人使用
MobaXterm时无需License，可能有一些功能限制，但不在本文范围内。

MobaXterm便携版的ZIP包展开即用，无需安装。简单配置如下

————————————————————————–
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
————————————————————————–
User sessions
New session (右键菜单)
SSH
Advanced SSH settings
X11-Forwarding
On
————————————————————————–

MobaXterm便携版每次启动时会临时释放出X Server对应的PE，就是它侦听6000。

用MobaXterm发起SSH登录，在SSH shell中启动X Client，初始TCP连接路径如下:

X Client -> X11 Proxy (Linux 6010) -> SSH信道 -> MobaXterm -> Windows 6000 -> X Server

X11通信经SSH信道到达Windows，无需调整Windows的防火墙策略，无需放行6000的入
连接。Windows侧只会出现到127.0.0.1:6000的TCP连接请求，这个无需PFW放行。

3) 在sudo/su之后继续访问之前的DISPLAY

以scz身份SSH登录，启用X11转发，xterm正常弹出。但切换到root身份后，失败。有
两个原因，一是缺DISPLAY环境变量，二是X Client没有认证凭据。解决如下

export DISPLAY=localhost:10.0
xauth add $(xauth -f ~scz/.Xauthority list | tail -1)
xterm&

4) MobaXterm 26.4不支持”ssh -X”

MobaXterm的各种组件都被阉割过，从一开始就没打算支持”ssh -X”。

a. GUI不提供-X选项
b. 后台Cygwin不提供xauth
c. X11转发默认”ForwardX11Trusted=yes”
d. 后台魔改的”ssh -vv”不提供真实日志
e. MobaXterm X Server不提供SECURITY扩展

这可能是基于商业考量，增加开箱即用的概率，避免陷入技术支持的泥潭。

☆ 实测若干GUI程序

1) xterm

最简测试，在SSH shell中执行xterm，Windows侧弹出xterm界面，整个过程非常透明。

2) firefox

Ubuntu 26的firefox是snap版本，想在X11转发场景中使用snap版firefox，必须确保
主控台logout中，再在SSH shell中执行

XAUTHORITY=~/.Xauthority firefox&

3) gedit

Ubuntu 26的gedit是基于GTK3的，若想在X11转发中弹出gedit，幺蛾子不少。

a. 假设主控台logout中，SSH shell中执行gedit，等十几秒后在Windows侧弹出，滞
后明显。

b. 假设主控台login中，SSH shell中执行gedit，Windows侧不会弹出，居然在主控
台弹出，这什么奇葩现象？注意，DISPLAY=localhost:10.0，指向X11 Proxy。

简单研究了一下，这些现象与gedit连接缺省Session/User Bus相关。为在Windows侧
快速弹出gedit，其中一种方案是

unset DBUS\_SESSION\_BUS\_ADDRESS
unset XDG\_RUNTIME\_DIR
gedit&

4) ptyxis

Ubuntu 26默认终端不再是传统的gnome-terminal，而是GTK4应用ptyxis。

在X11转发中测试ptyxis

a. 假设主控台logout中，SSH shell中执行ptyxis，等一分钟后在Windows侧弹出，
滞后更明显。

b. 假设主控台login中，SSH shell中执行ptyxis，Windows侧不会弹出，在主控台弹
出。

两种现象类似gedit。但不适用gedit的dbus快速弹出方案。目前只能忍受慢速弹出，
至少可用，弹出后操作并不迟缓。

☆ 参考资源

[1] MobaXterm
https://mobaxterm.mobatek.net/
https://mobaxterm.mobatek.net/download-home-edition.html

How to keep X11 display after su or sudo – [2015-11-28]
https://blog.mobatek.net/post/how-to-keep-X11-display-after-su-or-sudo/

最后修改日期: 2026-09-28

### 作者

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=96&d=identicon&r=g)

[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/)

## 最新发布

* [微软9月安全更新多个产品高危漏洞通告](https://blog.nsfocus.net/%E5%BE%AE%E8%BD%AF9%E6%9C%88%E5%AE%89%E5%85%A8%E6%9B%B4%E6%96%B0%E5%A4%9A%E4%B8%AA%E4%BA%A7%E5%93%81%E9%AB%98%E5%8D%B1%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)
* [微软8月安全更新多个产品高危漏洞通告](https://blog.nsfocus.net/%E5%BE%AE%E8%BD%AF8%E6%9C%88%E5%AE%89%E5%85%A8%E6%9B%B4%E6%96%B0%E5%A4%9A%E4%B8%AA%E4%BA%A7%E5%93%81%E9%AB%98%E5%8D%B1%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)
* [Fastjson 2.x远程代码执行漏洞通告](https://blog.nsfocus.net/fastjson-2-x%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)
* [Fastjson 1.2.x无需gadget远程代码执行漏洞通告](https://blog.nsfocus.net/fastjson-1-2-x%E6%97%A0%E9%9C%80gadget%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)
* [使用Ubuntu 26远程桌面](https://blog.nsfocus.net/%E4%BD%BF%E7%94%A8ubuntu-26%E8%BF%9C%E7%A8%8B%E6%A1%8C%E9%9D%A2/)

## 文章导航

[上一篇文章 高频业务：一种IP网段判断重叠的算法（其四）](https://blog.nsfocus.net/%E9%AB%98%E9%A2%91%E4%B8%9A%E5%8A%A1%EF%BC%9A%E4%B8%80%E7%A7%8Dip%E7%BD%91%E6%AE%B5%E5%88%A4%E6%96%AD%E9%87%8D%E5%8F%A0%E7%9A%84%E7%AE%97%E6%B3%95%EF%BC%88%E5%85%B6%E5%9B%9B%EF%BC%89/)

[下一篇文章 给X11转发环境配置中文输入](https://blog.nsfocus.net/%E7%BB%99x11%E8%BD%AC%E5%8F%91%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE%E4%B8%AD%E6%96%87%E8%BE%93%E5%85%A5/)

著作权 © 2026 **[绿盟科技技术博客](https://blog.nsfocus.net/)**. 保留一切权利。 本站采用的布景主题为 [Mynote](https://terryl.in/).