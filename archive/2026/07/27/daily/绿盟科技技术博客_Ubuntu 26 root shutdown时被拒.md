---
title: Ubuntu 26 root shutdown时被拒
url: https://blog.nsfocus.net/ubuntu-26-root-shutdown%e6%97%b6%e8%a2%ab%e6%8b%92/
source: 绿盟科技技术博客
date: 2026-07-27
fetch_date: 2026-07-28T04:59:09.883320
---

# Ubuntu 26 root shutdown时被拒

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
* Ubuntu 26 root shutdown时被拒

# Ubuntu 26 root shutdown时被拒

[0](https://blog.nsfocus.net/ubuntu-26-root-shutdown%E6%97%B6%E8%A2%AB%E6%8B%92/#comments)

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=40&d=identicon&r=g) [NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "written 2026-07-2709:55") 发布于 1 天前

![](https://blog.nsfocus.net/wp-content/uploads/2026/05/封面-25.jpg)

阅读： 37

Q:

Ubuntu 26，以root身份shutdown时，提示被拒

# shutdown -P now
Operation inhibited by “scz” (PID 3423 “gnome-session-s”, user scz), reason is “user session inhibited”.
User scz is logged in on tty2.
Please retry operation after closing inhibitors and logging out other users.
‘systemd-inhibit’ can be used to list active inhibitors.
Alternatively, ignore inhibitors and users with ‘systemctl poweroff -i’.

这是什么情况？

A:

精确复现方案，在X用scz登录，开Terminal，执行

python3

此时root已无法shutdown，出现前述提示。一定在X的Terminal中执行python3进行测
试，在SSH Shell中执行python3，无此效果。

Ubuntu 26中init是到systemd的符号链接，shutdown是到systemctl的符号链接。

$ readlink -f $(which init)
/usr/lib/systemd/systemd

$ readlink -f $(which shutdown)
/usr/bin/systemctl

这种系统”init 0″不对应关机。”shutdown -P”实际执行”systemctl poweroff”。
systemctl通过systemd、systemd-logind完成关机、重启等操作，这套机制遵循一种
名为”Inhibitor Locks”的东西，参看:

https://systemd.io/INHIBITOR\_LOCKS

普通进程可通过D-Bus向systemd-logind注册指定类型的inhibitor，比如说，我正在
升级，请勿关机。之后的”systemctl poweroff”会通过systemd询问systemd-logind，
发现有个shutdown inhibitor，systemd将拒绝关机。

可用如下命令查看当前注册生效中的inhibitor

systemd-inhibit –list
systemd-inhibit –no-pager –no-legend –list

或者更底层、更直接的命令

gdbus call \
–system \
–dest org.freedesktop.login1 \
–object-path /org/freedesktop/login1 \
–method org.freedesktop.login1.Manager.ListInhibitors

可用systemd-inhibit注册shutdown inhibitor，同时执行一个长期驻留的子进程，
在子进程存活期间，inhibitor对应的fd(文件句柄)不会自动关闭，inhibitor不会自
动注销。比如

systemd-inhibit \
–what=shutdown \
–who=”any” \
–why=”some” \
–mode=block \
bash

bash可换成”pauseme sleep 0″之类的，只要子进程能长期驻留即可。上述操作对系
统有潜在影响，普通用户执行时要求输入root密码。

若遭遇root shutdown被拒，提示信息中已给出解决方案之一

systemctl poweroff -i

“-i”是忽略inhibitor的意思。但这样过于简单粗暴，更好的解决之道是，找出那个
注册了shutdown inhibitor的进程，正常结束它，再关机。

D:

D-Bus是个较大的攻击面，但我从未研究过，这次稍微多做点实验。

gdbus introspect \
–system \
–dest org.freedesktop.login1 \
–object-path /org/freedesktop/login1

上述命令向systemd-logind查询「你这个D-Bus服务提供哪些接口」，部分输出如下

————————————————————————–
interface org.freedesktop.login1.Manager {
methods:
…
ListSessions(out a(susso) sessions);
ListSessionsEx(out a(sussussbto) sessions);
ListUsers(out a(uso) users);
…
ListInhibitors(out a(ssssuu) inhibitors);
…
LockSessions();
UnlockSessions();
…
PowerOff(in b interactive);
…
Reboot(in b interactive);
…
————————————————————————–

gdbus可直接调用这些API。

gdbus call \
–system \
–dest org.freedesktop.login1 \
–object-path /org/freedesktop/login1 \
–method org.freedesktop.login1.Manager.LockSessions

在SSH Shell中以root身份执行LockSessions，将在主控台产生锁屏的效果，简单类
比成Windows cmd中执行:

rundll32.exe user32.dll,LockWorkStation

针对LockSessions，可用gdbus取消锁屏:

gdbus call \
–system \
–dest org.freedesktop.login1 \
–object-path /org/freedesktop/login1 \
–method org.freedesktop.login1.Manager.UnlockSessions

若在主控台交互式取消锁屏，需输入密码，gdbus取消锁屏则不需要，有趣。不过，
若主控台处于登录界面，UnlockSessions无法取消录登界面。

gdbus call \
–system \
–dest org.freedesktop.login1 \
–object-path /org/freedesktop/login1 \
–method org.freedesktop.login1.Manager.ListSessions

可通过D-Bus关机，以root身份执行:

gdbus call \
–system \
–dest org.freedesktop.login1 \
–object-path /org/freedesktop/login1 \
–method org.freedesktop.login1.Manager.PowerOff \
true

对于root，无论PowerOff的参数是false还是true，均不会交互式授权，因为已经是
root。对于普通用户，上述命令过于底层，无法进入交互式授权环节，因为这是由其
他组件配合提供的，gdbus无此能力，只会报错:

Error: GDBus.Error:org.freedesktop.DBus.Error.InteractiveAuthorizationRequired:
Access denied as the requested operation requires interactive authentication.
However, interactive authentication has not been enabled by the calling program.

可监控D-Bus消息，比如

dbus-monitor –system –monitor \
type=method\_call,interface=org.freedesktop.login1.Manager,member=Inhibit

在X Terminal中执行python3，在dbus-monitor中将看到

method call … path=/org/freedesktop/login1; interface=org.freedesktop.login1.Manager; member=Inhibit
string “shutdown”
string “scz”
string “user session inhibited”
string “block”

在root shell中执行

gdbus call \
–system \
–dest org.freedesktop.login1 \
–object-path /org/freedesktop/login1 \
–method org.freedesktop.login1.Manager.Inhibit \
shutdown \
any \
some \
block

在dbus-monitor中将看到

method call …
string “shutdown”
string “any”
string “some”
string “block”

最后修改日期: 2026-07-27

### 作者

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=96&d=identicon&r=g)

[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/)

## 最新发布

* [Ubuntu 26 root shutdown时被拒](https://blog.nsfocus.net/ubuntu-26-root-shutdown%E6%97%B6%E8%A2%AB%E6%8B%92/)
* [有准可循 互联互通 | 《大模型安全网关产品安全指南》国标项目启动会顺利召开](https://blog.nsfocus.net/%E6%9C%89%E5%87%86%E5%8F%AF%E5%BE%AA-%E4%BA%92%E8%81%94%E4%BA%92%E9%80%9A-%E3%80%8A%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%AE%89%E5%85%A8%E7%BD%91%E5%85%B3%E4%BA%A7%E5%93%81%E5%AE%89%E5%85%A8%E6%8C%87/)
* [全国工商联领导一行莅临绿盟科技调研指导，共商安全产业发展新路径](https://blog.nsfocus.net/%E5%85%A8%E5%9B%BD%E5%B7%A5%E5%95%86%E8%81%94%E9%A2%86%E5%AF%BC%E4%B8%80%E8%A1%8C%E8%8E%85%E4%B8%B4%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E8%B0%83%E7%A0%94%E6%8C%87%E5%AF%BC%EF%BC%8C%E5%85%B1%E5%95%86/)
* [001号！绿盟科技斩获国内首张智能体管理能力成熟度L2认证证书](https://blog.nsfocus.net/001%E5%8F%B7%EF%BC%81%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E6%96%A9%E8%8E%B7%E5%9B%BD%E5%86%85%E9%A6%96%E5%BC%A0%E6%99%BA%E8%83%BD%E4%BD%93%E7%AE%A1%E7%90%86%E8%83%BD%E5%8A%9B%E6%88%90%E7%86%9F/)
* [半场见分晓 「AI」见真章 | 绿盟科技2026年中AI安全成果实录](https://blog.nsfocus.net/%E5%8D%8A%E5%9C%BA%E8%A7%81%E5%88%86%E6%99%93-%E3%80%8Cai%E3%80%8D%E8%A7%81%E7%9C%9F%E7%AB%A0-%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%802026%E5%B9%B4%E4%B8%ADai%E5%AE%89%E5%85%A8%E6%88%90%E6%9E%9C/)

## 文章导航

[上一篇文章 有准可循 互联互通 | 《大模型安全网关产品安全指南》国标项目启动会顺利召开](https://blog.nsfocus.net/%E6%9C%89%E5%87%86%E5%8F%AF%E5%BE%AA-%E4%BA%92%E8%81%94%E4%BA%92%E9%80%9A-%E3%80%8A%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%AE%89%E5%85%A8%E7%BD%91%E5%85%B3%E4%BA%A7%E5%93%81%E5%AE%89%E5%85%A8%E6%8C%87/)

著作权 © 2026 **[绿盟科技技术博客](https://blog.nsfocus.net/)**. 保留一切权利。 本站采用的布景主题为 [Mynote](https://terryl.in/).