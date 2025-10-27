---
title: mosquitto not authorised
url: https://h4ck.org.cn/2022/11/mosquitto-not-authorised/
source: obaby@mars
date: 2022-11-08
fetch_date: 2025-10-03T21:54:10.094278
---

# mosquitto not authorised

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

[后台开发『BackEnd』](https://h4ck.org.cn/cats/cxsj/backend), [物联网『IoT』](https://h4ck.org.cn/cats/cxsj/internet-of-things)

# mosquitto not authorised

2022年11月7日
[2 条评论](https://h4ck.org.cn/2022/11/10691#comments)

![](https://image.h4ck.org.cn/wp-content/uploads/2022/10/4a17c76d3883816e7587c476d193e065.jpg)

> Eclipse Mosquitto is an open source (EPL/EDL licensed) message broker that implements the MQTT protocol versions 5.0, 3.1.1 and 3.1. Mosquitto is lightweight and is suitable for use on all devices from low power single board computers to full servers.
> The MQTT protocol provides a lightweight method of carrying out messaging using a publish/subscribe model. This makes it suitable for Internet of Things messaging such as with low power sensors or mobile devices such as phones, embedded computers or microcontrollers.
> The Mosquitto project also provides a C library for implementing MQTT clients, and the very popular mosquitto\_pub and mosquitto\_sub command line MQTT clients.

最近需要用mqtt来实现消息处理，在windows上安装Mosquitto之后，不使用用户名密码提示connection refused: not authorised。结果添加用户名密码之后还是提示同样的错误。

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/捕获.jpg)

搜索了一下有人是安装路径问题，安装路径不能有空格。于是奔着简单粗暴的解决方式，直接重新安装。操作之后还是同样的问题，打开配置文件发现这个版本没有定义password\_file,修改为:

```
# -----------------------------------------------------------------
# Default authentication and topic access control
# -----------------------------------------------------------------

# Control access to the broker using a password file. This file can be
# generated using the mosquitto_passwd utility. If TLS support is not compiled
# into mosquitto (it is recommended that TLS support should be included) then
# plain text passwords are used, in which case the file should be a text file
# with lines in the format:
# username:password
# The password (and colon) may be omitted if desired, although this
# offers very little in the way of security.
#
# See the TLS client require_certificate and use_identity_as_username options
# for alternative authentication options. If a plugin is used as well as
# password_file, the plugin check will be made first.
password_file E:\mosquitto\pwfile.example
```

并且没有定义默认监听端口，修改为（7788改成自己想要使用的端口）：

```
# =================================================================
# Listeners
# =================================================================

# Listen on a port/ip address combination. By using this variable
# multiple times, mosquitto can listen on more than one port. If
# this variable is used and neither bind_address nor port given,
# then the default listener will not be started.
# The port number to listen on must be given. Optionally, an ip
# address or host name may be supplied as a second argument. In
# this case, mosquitto will attempt to bind the listener to that
# address and so restrict access to the associated network and
# interface. By default, mosquitto will listen on all interfaces.
# Note that for a websockets listener it is not possible to bind to a host
# name.
#
# On systems that support Unix Domain Sockets, it is also possible
# to create a # Unix socket rather than opening a TCP socket. In
# this case, the port number should be set to 0 and a unix socket
# path must be provided, e.g.
# listener 0 /tmp/mosquitto.sock
#
# listener port-number [ip address/host name/unix socket path]
listener 7788
```

重启服务就ok了。

遇到验证失败可以根据下面的检查内容尝试：

1.安装路径（我不确定是否和这个有关）

2.服务有没有启动

3.有没有创建用户

4.密码文件是否已经配置号

5.监听端口是否一致

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《mosquitto not authorised》](https://h4ck.org.cn/2022/11/10691)
\* 本文链接：<https://h4ck.org.cn/2022/11/10691>
\* 短链接：<https://oba.by/?p=10691>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[mosquitto](https://h4ck.org.cn/tags/mosquitto)[mqtt](https://h4ck.org.cn/tags/mqtt)

[Previous Post](https://h4ck.org.cn/2022/11/10698)
[Next Post](https://h4ck.org.cn/2022/11/10683)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2025年8月9日

#### [偶然？还是必然？ — 谁是罪魁祸首](https://h4ck.org.cn/2025/08/21237)

2023年3月23日

#### [若依Django框架soft-delete导致的数据查询异常](https://h4ck.org.cn/2023/03/11588)

2021年5月10日

#### [WordPress 回复可见【非插件】](https://h4ck.org.cn/2021/05/8116)

### 2 comments

1. ![](https://gg.lang.bi/avatar/1041ccacc8debe6fed1ab9a6e3faefe31906ec67691f418d56dcf74673e548ff?s=64&d=identicon&r=r) **[子痕](https://blog.mzihen.com/)**说道：

   [2022年11月9日 09:35](https://h4ck.org.cn/2022/11/10691#comment-88728)

   ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![Microsoft Edge 107](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 107") Microsoft Edge 107 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   看不懂文章不要紧，图片就能引来绅士们的热烈讨论。

   [回复](#comment-88728)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2022年11月9日 09:36](https://h4ck.org.cn/2022/11/10691#comment-88729)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      不要在意这些细节~~~

      [回复](#comment-88729)

### 发表回复 [取消回复](/2022/11/10691#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

评论 \*

显示名称 \*

邮箱 \*

网站

[ ]  在此浏览器中保存我的显示名称、邮箱地址和网站地址，以便下次评论时使用。

[x] 如果有人回复我的评论，请通过电子邮件通知我。

[x]

Δ

### 标签云[Tag Cloud]

Your browser doesn't support the HTML5 CANVAS tag.

* [CDN](https://h4ck.org.cn/tags/cdn)
* [Virus Analysit](https://h4ck.org.cn/tags/virus-analysit)
* [Python](https://h4ck.org.cn/tags/python)
* [OD](https://h4ck.org.cn/tags/od)
* [Mac OS](https://h4ck.org.cn/tags/mac-os)
* [Porn](https://h4ck.org.cn/tags/porn)
* [m3u8](https://h4ck.org.cn/tags/m3u8)
* [大姨妈](https://h4ck.org.cn/tags/%E5%A4%A7%E5%A7%A8%E5%A6%88)
* [php](https://h4ck.org.cn/tags/php)
* [ubuntu](https://h4ck.org.cn/tags/ubuntu)
* [Google](https://h4ck.org.cn/tags/google)
* [PETools](https://h4ck.org.cn/tags/petools)
* [游戏](https://h4ck.org.cn/tags/game)
* [Crack](https://h4ck.org.cn/tags/crack)
* [IDA](https://h4ck.org.cn/tags/ida)
* [ASM](https://h4ck.org.cn/tags/asm)
* [月经](https://h4ck.org.cn/tags/%E6%9C%88%E7%BB%8F)
* [Windows](https://h4ck.org.cn/tags/windows)
* [爬虫](https://h4ck.org.cn/tags/%E7%88%AC%E8%99%AB)
* [Plugin](https://h4ck.org.cn/tags/plugin)
* [spider](https://h4ck.org.cn/tags/spider)
* [iOS](https://h4ck.org.cn/tags/ios)
* [Unpack](https://h4ck.org.cn/tags/tuoke)
* [yolov5](https://h4ck.org.cn/tags/yo...