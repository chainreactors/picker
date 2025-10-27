---
title: 树莓派UPS自定义关机脚本（NUT）
url: https://h4ck.org.cn/2023/02/%e6%a0%91%e8%8e%93%e6%b4%be%e8%87%aa%e5%ae%9a%e4%b9%89%e5%85%b3%e6%9c%ba%e8%84%9a%e6%9c%ac%ef%bc%88nut%ef%bc%89/
source: obaby@mars
date: 2023-02-14
fetch_date: 2025-10-04T06:29:16.555560
---

# 树莓派UPS自定义关机脚本（NUT）

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[Linux『Linux』](https://h4ck.org.cn/cats/xtxg/linux%E3%80%8Elinux%E3%80%8F)

# 树莓派UPS自定义关机脚本（NUT）

2023年2月13日
[12 条评论](https://h4ck.org.cn/2023/02/11197#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/10/557b504053cb3f7e2dd4bfbfc7c9ab88-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/10/557b504053cb3f7e2dd4bfbfc7c9ab88-scaled.jpg)

NUT 树莓派自定义关机逻辑，上一篇文章太长了，拉出来一些：

默认关机逻辑貌似是：nut服务会在UPS发送`LOWBATT`时通知机器关机，触发时机默认为ups电量剩余`20%`。

如果要自定义关机设置需要进行如下设置（因为群辉提供的ups服务器在ups断电之前就关闭了，不清楚服务器在关机之前是不是会发送lowbatt消息）

1.编辑upsmon.conf,添加以下内容：

```
vim /etc/nut/upsmon.conf
```

```
NOTIFYCMD /sbin/upssched
NOTIFYFLAG ONBATT SYSLOG+WALL+EXEC
```

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230212194008.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230212194008.jpg)

通知类型定义：

```
NOTIFYMSG type message
upsmon comes with a set of stock messages for various events. You can change them if you like.

NOTIFYMSG ONLINE "UPS %s is getting line power"
NOTIFYMSG ONBATT "Someone pulled the plug on %s"
Note that %s is replaced with the identifier of the UPS in question.

The message must be one element in the configuration file, so if it contains spaces, you must wrap it in quotes.

NOTIFYMSG NOCOMM "Someone stole UPS %s"
Possible values for type:

ONLINE
UPS is back online

ONBATT
UPS is on battery

LOWBATT
UPS is on battery and has a low battery (is critical)

FSD
UPS is being shutdown by the primary (FSD = "Forced Shutdown")

COMMOK
Communications established with the UPS

COMMBAD
Communications lost to the UPS

SHUTDOWN
The system is being shutdown

REPLBATT
The UPS battery is bad and needs to be replaced

NOCOMM
A UPS is unavailable (can’t be contacted for monitoring)

NOTIFYFLAG type flag[+flag]…
By default, upsmon sends walls global messages to all logged in users) via /bin/wall and writes to the syslog when things happen. Except for Windows where upsmon only writes to the syslog by default. You can change this.

Examples:

NOTIFYFLAG ONLINE SYSLOG
NOTIFYFLAG ONBATT SYSLOG+WALL+EXEC
Possible values for the flags:

SYSLOG
Write the message to the syslog

WALL
Write the message to all users with /bin/wall

EXEC
Execute NOTIFYCMD (see above) with the message

IGNORE
Don’t do anything

If you use IGNORE, don’t use any other flags on the same line.
```

2.修改upssched.conf添加以下内容

```
vim /etc/nut/upssched.conf
```

```
CMDSCRIPT /etc/nut/upssched-cmd #编写此脚本设置
# NOTIFYCMD /sbin/upssched
# NOTIFYFLAG ONBATT SYSLOG+WALL+EXEC
PIPEFN /etc/nut/upssched.pipe
LOCKFN /etc/nut/upssched.lock

AT ONBATT * START-TIMER power-off 60
AT ONLINE * CANCEL-TIMER power-off
AT ONLINE * EXECUTE power-on
```

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/搜狗截图20230212192943-1.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230212192943-1.jpg)

3.编辑upssched-cmd脚本

```
vim /etc/nut/upssched-cmd
```

文件内容：

```
#!/bin/sh
 case $1 in
       onbatt)
          logger -t upssched-cmd "UPS running on battery"
          # do somethings ,e.g.send email \ wechat
       /usr/sbin/upsmon -c fsd
          ;;
       power-off)
          logger -t upssched-cmd "UPS running on battery power off"
          /usr/sbin/upsmon -c fsd
          ;;
       shutdowncritical)
          logger -t upssched-cmd "UPS on battery critical, forced shutdown"
          /usr/sbin/upsmon -c fsd
          ;;
       upsgone)
          logger -t upssched-cmd "UPS has been gone too long, can't reach"
          ;;
       *)
          logger -t upssched-cmd "Unrecognized command: $1"
          ;;
 esac
```

修改完成之后重启服务。

https://h4ck.org.cn/2023/02/%E6%98%AFups%E5%90%96%EF%BC%88%E4%B8%89%EF%BC%89-%E6%A0%91%E8%8E%93%E6%B4%BE/

我的博客即将同步至腾讯云开发者社区，邀请大家一同入驻：https://cloud.tencent.com/developer/support-plan?invite\_code=155gv09voxk2

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《树莓派UPS自定义关机脚本（NUT）》](https://h4ck.org.cn/2023/02/11197)
\* 本文链接：<https://h4ck.org.cn/2023/02/11197>
\* 短链接：<https://oba.by/?p=11197>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[NUT](https://h4ck.org.cn/tags/nut)[UPS](https://h4ck.org.cn/tags/ups)[树莓派](https://h4ck.org.cn/tags/%E6%A0%91%E8%8E%93%E6%B4%BE)

[Previous Post](https://h4ck.org.cn/2023/02/11232)
[Next Post](https://h4ck.org.cn/2023/02/11176)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2021年10月18日

#### [基于Freeswitch的语音视频通话](https://h4ck.org.cn/2021/10/9153)

2024年8月15日

#### [通过 CF 自建 Docker 镜像](https://h4ck.org.cn/2024/08/17841)

2023年2月11日

#### [是UPS吖（一）–开箱](https://h4ck.org.cn/2023/02/11157)

### 12 comments

1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r) **[dujun](https://dujun.io)**说道：

   [2023年2月13日 13:40](https://h4ck.org.cn/2023/02/11197#comment-92248)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Google Chrome 109](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 109") Google Chrome 109 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   树莓派是 arm 架构的太麻烦了。所以我搞了个工控机～

   [回复](#comment-92248)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2023年2月13日 13:45](https://h4ck.org.cn/2023/02/11197#comment-92249)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      其实多数情况下linux系统的arm支持还算不错，使用起来体验差别不大。就当成个普通linux系统用就可以啦~~

      [回复](#comment-92249)
2. ![](https://gg.lang.bi/avatar/8824e297c4534b8bd95cf3935277fe4f08f4cd576cbecad8166587874e97a036?s=64&d=identicon&r=r)

   [2023年2月13日 20:45](https://h4ck.org.cn/2023/02/11197#comment-92256)

   ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![Firefox 109](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/firefox.png "Firefox 109") Firefox 109 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   我看“杜老师“也在玩这个 ups啊。

   <https://dusays.com/554/> UPS 的使用体验

   [回复](#comment-92256)

   1. ![](https://gg.lang.bi/avatar/d6ebc...