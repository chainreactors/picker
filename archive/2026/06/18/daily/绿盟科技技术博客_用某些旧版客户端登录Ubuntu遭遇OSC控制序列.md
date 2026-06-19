---
title: 用某些旧版客户端登录Ubuntu遭遇OSC控制序列
url: https://blog.nsfocus.net/%e7%94%a8%e6%9f%90%e4%ba%9b%e6%97%a7%e7%89%88%e5%ae%a2%e6%88%b7%e7%ab%af%e7%99%bb%e5%bd%95ubuntu%e9%81%ad%e9%81%87osc%e6%8e%a7%e5%88%b6%e5%ba%8f%e5%88%97/
source: 绿盟科技技术博客
date: 2026-06-18
fetch_date: 2026-06-19T07:07:24.271315
---

# 用某些旧版客户端登录Ubuntu遭遇OSC控制序列

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 用某些旧版客户端登录Ubuntu遭遇OSC控制序列

### 用某些旧版客户端登录Ubuntu遭遇OSC控制序列

[2026-06-18](https://blog.nsfocus.net/%E7%94%A8%E6%9F%90%E4%BA%9B%E6%97%A7%E7%89%88%E5%AE%A2%E6%88%B7%E7%AB%AF%E7%99%BB%E5%BD%95ubuntu%E9%81%AD%E9%81%87osc%E6%8E%A7%E5%88%B6%E5%BA%8F%E5%88%97/ "用某些旧版客户端登录Ubuntu遭遇OSC控制序列")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 60

Q:

用某些旧版客户端SSH登录Ubuntu 26后，bash中总能看到类似下面这种信息

08;
start=2fca083b-a593-404c-8570-0dabd6441acf;
machineid=ebc7387fc82944d6ba9dbe5b8470e471;
user=scz;
hostname=Ubuntu-26;
bootid=bc81f634-419d-4443-a6c5-927297e02283;
pid=00000000000000007613;
type=command;
cwd=/home/scz

这是哪来的？

A:

这不是PS1提示符内容，而是终端Shell Integration的OSC控制序列被错误地显示出
来。这些OSC(Operating System Command)控制序列，用于告诉支持OSC的终端某些信
息，比如

. 用户
. 主机名
. 当前目录

新版Ubuntu(24.04以后)默认启用了这套机制，某些SSH客户端或终端模拟器不支持这
些OSC序列，就将原始内容直接显示出来。

正经解决办法是升级客户端、终端模拟器，使之支持OSC序列。但会遇上不想、不便
升级的情形，此时只能从服务端解决，即不要发送OSC序列。

先找出发送OSC序列的源头，罪魁祸首应该是80-systemd-osc-context.sh，而非vte-2.91.sh。

解决办法之一

vi ~/.bashrc (针对普通用户)

在尾部增加

if [[ -n “$SSH\_CONNECTION” ]]; then
PROMPT\_COMMAND=(
“${PROMPT\_COMMAND[@]/\_\_systemd\_osc\_context\_precmdline}”
)
PS0=
fi

之后，SSH登录时不再发送OSC序列，同时不影响XWindow桌面里的终端模拟器。上例
也可检查”$SSH\_TTY”变量。但这样对付不了”su -“情形，原因很显然。

若确实不需要OSC序列，全局禁用最省事。比如

vi /etc/profile.d/99-disable-osc3008.sh

PROMPT\_COMMAND=(
“${PROMPT\_COMMAND[@]/\_\_systemd\_osc\_context\_precmdline}”
)
PS0=

创建99-disable-osc3008.sh，它将在80-systemd-osc-context.sh之后执行，会清理
两个环境变量。这样做，将极大减少OSC序列，但未彻底解决。”su -“进去的一瞬间，
仍有一次OSC；exit离开”su -“时，也有一次OSC。

$ su –
Password:
08;start=…;hostname=Ubuntu-26;…;comm=su;targetuser=root;type=session
# exit
logout
08;end=275368b7e16e43eeb5d78f9b8f93c233

这两次OSC不是bash发送的，而是pam\_systemd.so发送的，没有配置文件改变此行为。

$ strings /usr/lib/x86\_64-linux-gnu/security/pam\_systemd.so | grep “;type=session”
;type=session

可以

vi /etc/pam.d/common-session

注释掉下面这行

#session optional pam\_systemd.so

这将消除”;type=session”所属的OSC序列，但有其他隐患，不细说。若只是自己的虚
拟测试环境，问题不大。

若不想动pam\_systemd.so，另一种临时解决办法是

export TERM=dumb
su –

或

TERM=dumb su –

将TERM从vt100或其他值改成dumb，可消除所有OSC序列，但对vi之类的工具有影响，
临时应急可以，非长久之计。可以

vi ~/.bashrc (针对普通用户)

alias su=’TERM=dumb su’

vi /root/.bashrc

if [ “$TERM” = “dumb” ]; then
export TERM=vt100
fi

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E3%80%8Aapt%E7%BB%84%E7%BB%87%E7%A0%94%E7%A9%B6%E5%B9%B4%E9%89%B4%E3%80%8B%EF%BC%882026-%E7%89%88%EF%BC%89%E6%AD%A3%E5%BC%8F%E5%8F%91%E5%B8%83/)

[Next](https://blog.nsfocus.net/%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E4%BA%AE%E7%9B%B82026%E5%85%A8%E5%9B%BDcio%E5%A4%A7%E4%BC%9A%EF%BC%8C%E5%88%86%E4%BA%AB%E6%99%BA%E8%83%BD%E4%BD%93%E5%85%A8%E5%91%A8%E6%9C%9F%E5%AE%89%E5%85%A8/)

### Meet The Author

NSFOCUS

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)