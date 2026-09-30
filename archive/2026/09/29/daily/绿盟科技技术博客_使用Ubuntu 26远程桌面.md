---
title: 使用Ubuntu 26远程桌面
url: https://blog.nsfocus.net/%e4%bd%bf%e7%94%a8ubuntu-26%e8%bf%9c%e7%a8%8b%e6%a1%8c%e9%9d%a2/
source: 绿盟科技技术博客
date: 2026-09-29
fetch_date: 2026-09-30T07:42:41.023425
---

# 使用Ubuntu 26远程桌面

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
* 使用Ubuntu 26远程桌面

# 使用Ubuntu 26远程桌面

[0](https://blog.nsfocus.net/%E4%BD%BF%E7%94%A8ubuntu-26%E8%BF%9C%E7%A8%8B%E6%A1%8C%E9%9D%A2/#comments)

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=40&d=identicon&r=g) [NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "written 2026-09-2914:38") 发布于 1 天前

![](https://blog.nsfocus.net/wp-content/uploads/2026/06/2.png)

阅读： 26

过去的工作方向，很少有用Linux GUI的时候，对GUI相关的服务、功能知之甚少。最
近想用Ubuntu 26的远程桌面，临时查阅一些资料，记录备忘。

————————————————————————–
Settings
System
Remote Desktop
Desktop Sharing (可能需要提供普通用户密码Unlock后再操作)
Desktop Sharing
On (可看)
Remote Control
On (可控)
How to Connect
Port
3389 (GUI不可更改)
Login Details
Username
any0 (必须设置，与系统账号无关)
Password
(必须设置，与Linux系统账号无关)
Remote Login (可能需要提供root密码Unlock后再操作)
Remote Login
On (可控)
How to Connect
Port
3389 (GUI不可更改)
Login Details
Username
any1 (必须设置，与Linux系统账号无关)
Password
(必须设置，与系统账号无关)
————————————————————————–

GNOME远程桌面有两种模式，分别是”Desktop Sharing”、”Remote Login”。

“Desktop Sharing”相当于共享屏幕，要求主控台GUI已登录。若未登录(停留在登录
界面)，则不侦听3389，必须GUI登录才会触发侦听3389；logout后3389将不再侦听。
就是说，为用”Desktop Sharing”，主控台GUI必须保持login状态。

“Desktop Sharing”可保持只读模式，即只能远程观摩主控台GUI操作，不能控制。若
同时打开”Remote Control”，则进入读写模式，可远程操控屏幕，且主控台与远程桌
面屏显同步。

若启用”Remote Login”，则OS启动后3389一直侦听中，无需通过主控台GUI登录来触
发侦听。若同时启用”Desktop Sharing”，系统自动安排”Remote Login”侦听3389、
“Desktop Sharing”侦听3390，意味着RDP连接时”Remote Login”优先级更高。这些端
口变动，都是自动的，无法在GUI人工更改。

客户端使用”Remote Login”时，若主控台GUI已登录，会弹框提示。此时有两种选择，
一是在主控台主动logout，二是远程”Force Stop”，后者相当于强制主控台logout。

据说可以命令行设置相关端口，未测试。

一般无需修改3389端口号，毕竟mstsc默认用3389。若同时启用”Desktop Sharing”、
“Remote Login”，想访问前者时，在mstsc初始界面输入”ip:port”(缺省只输ip)，比
如”192.168.65.26:3390″。

“Login Details”处的any0、any1俱是独立user，互不影响。它们与Linux系统账号无
关，填在mstsc中，用于RDP登录第一次认证。认证通过后，若用”Desktop Sharing”，
将直接看到主控台界面；若用”Remote Login”，将面对GUI登录界面，还需用Linux系
统账号完成第二次认证。RDP登录时若提示”内部错误”，先检查”Login Details”处的
user/pass是否已显式设置，这个错误提示相当不友好。

GNOME远程桌面很容易因为超时不动而断掉，这点很烦。可设整如下设置，稍微缓解
一下:

————————————————————————–
Settings
Power
Power Saving
Automatic Screen Blank
Off
Privacy & Security
Screen Lock
Automatic Screen Lock
Off
————————————————————————–

排错时可查看GNOME远程桌面日志:

journalctl –user -u gnome-remote-desktop -n 100 –no-pager | less

最后修改日期: 2026-09-29

### 作者

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=96&d=identicon&r=g)

[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/)

## 最新发布

* [四次进化，绿盟科技将开拓怎样的安全新境？](https://blog.nsfocus.net/%E5%9B%9B%E6%AC%A1%E8%BF%9B%E5%8C%96%EF%BC%8C%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E5%B0%86%E5%BC%80%E6%8B%93%E6%80%8E%E6%A0%B7%E7%9A%84%E5%AE%89%E5%85%A8%E6%96%B0%E5%A2%83%EF%BC%9F/)
* [微软9月安全更新多个产品高危漏洞通告](https://blog.nsfocus.net/%E5%BE%AE%E8%BD%AF9%E6%9C%88%E5%AE%89%E5%85%A8%E6%9B%B4%E6%96%B0%E5%A4%9A%E4%B8%AA%E4%BA%A7%E5%93%81%E9%AB%98%E5%8D%B1%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)
* [微软8月安全更新多个产品高危漏洞通告](https://blog.nsfocus.net/%E5%BE%AE%E8%BD%AF8%E6%9C%88%E5%AE%89%E5%85%A8%E6%9B%B4%E6%96%B0%E5%A4%9A%E4%B8%AA%E4%BA%A7%E5%93%81%E9%AB%98%E5%8D%B1%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)
* [Fastjson 2.x远程代码执行漏洞通告](https://blog.nsfocus.net/fastjson-2-x%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)
* [Fastjson 1.2.x无需gadget远程代码执行漏洞通告](https://blog.nsfocus.net/fastjson-1-2-x%E6%97%A0%E9%9C%80gadget%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)

## 文章导航

[上一篇文章 给英文版Ubuntu 26安装中文输入法](https://blog.nsfocus.net/%E7%BB%99%E8%8B%B1%E6%96%87%E7%89%88ubuntu-26%E5%AE%89%E8%A3%85%E4%B8%AD%E6%96%87%E8%BE%93%E5%85%A5%E6%B3%95/)

[下一篇文章 Fastjson 1.2.x无需gadget远程代码执行漏洞通告](https://blog.nsfocus.net/fastjson-1-2-x%E6%97%A0%E9%9C%80gadget%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)

著作权 © 2026 **[绿盟科技技术博客](https://blog.nsfocus.net/)**. 保留一切权利。 本站采用的布景主题为 [Mynote](https://terryl.in/).