---
title: Uptime Kuma自建服务监控服务
url: https://h4ck.org.cn/2022/12/uptime-kuma%e8%87%aa%e5%bb%ba%e6%9c%8d%e5%8a%a1%e7%9b%91%e6%8e%a7%e6%9c%8d%e5%8a%a1/
source: obaby@mars
date: 2022-12-05
fetch_date: 2025-10-04T00:30:40.952445
---

# Uptime Kuma自建服务监控服务

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

[后台开发『BackEnd』](https://h4ck.org.cn/cats/cxsj/backend)

# Uptime Kuma自建服务监控服务

2022年12月4日
[3 条评论](https://h4ck.org.cn/2022/12/10833#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2022/12/c800deb603caa546472012142477f02b.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2022/12/c800deb603caa546472012142477f02b.jpg) [![](https://image.h4ck.org.cn/wp-content/uploads/2022/12/cbdc3150d2e4fcb9a8cdd1100d2320dd.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2022/12/cbdc3150d2e4fcb9a8cdd1100d2320dd.jpg)

uptime-kuma是一款开源监控工具，类似于“Uptime Robot和statping”，ui非常简洁美观，支持TCP/PING/HTTP监控等，还支持多语言其中包括中文！

项目：https://github.com/louislam/uptime-kuma

安装步骤：

1.安装docker

```
apt install docker.io
```

2.安装uptime-kuma

```
# Create a volume
docker volume create uptime-kuma

# Start the container
docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:1
```

3.配置nginx转发（删除其他的location，否则可能会导致404），添加：

```
location /static {
      alias /static;
    }

    location / {
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;

        proxy_pass http://127.0.0.1:3001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
```

实际效果：

[![](https://image.h4ck.org.cn/wp-content/uploads/2022/12/搜狗截图20221204200956.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2022/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20221204200956.jpg)

[![](https://image.h4ck.org.cn/wp-content/uploads/2022/12/搜狗截图20221204201042.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2022/12/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20221204201042.jpg)

测试页面地址：

<https://up.obaby.org.cn/status/0>

ps：

图片来自最新的爬虫：<https://h4ck.org.cn/2022/12/%E7%A7%80%E4%BA%BA%E7%BE%8E%E5%A5%B3%E7%BD%91%E7%88%AC%E8%99%AB-%E3%80%90windows%E3%80%91%E3%80%9022-12-03%E3%80%91/>

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Uptime Kuma自建服务监控服务》](https://h4ck.org.cn/2022/12/10833)
\* 本文链接：<https://h4ck.org.cn/2022/12/10833>
\* 短链接：<https://oba.by/?p=10833>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Uptime Kuma](https://h4ck.org.cn/tags/uptime-kuma)[网站监控](https://h4ck.org.cn/tags/%E7%BD%91%E7%AB%99%E7%9B%91%E6%8E%A7)

[Previous Post](https://h4ck.org.cn/2022/12/10841)
[Next Post](https://h4ck.org.cn/2022/12/10820)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2021年10月21日

#### [Freeswitch sip Push notifications](https://h4ck.org.cn/2021/10/9190)

2025年1月17日

#### [django TimescaleDB](https://h4ck.org.cn/2025/01/19012)

2022年12月8日

#### [Django Export XLS](https://h4ck.org.cn/2022/12/10850)

### 3 comments

1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r) **[dujun](https://dujun.io)**说道：

   [2022年12月4日 23:52](https://h4ck.org.cn/2022/12/10833#comment-89653)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Safari 16](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/safari.png "Safari 16") Safari 16 ![iPhone iOS 16.1.2](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/iphone.png "iPhone iOS 16.1.2") iPhone iOS 16.1.2 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   好用

   [回复](#comment-89653)
2. ![](https://gg.lang.bi/avatar/1c03767b0691f80231895255661bcf42eceab95dc8b493ee80c835b07f577f49?s=64&d=identicon&r=r)

   [2022年12月5日 01:43](https://h4ck.org.cn/2022/12/10833#comment-89657)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 107](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 107") Microsoft Edge 107 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   你站点也不少！

   [回复](#comment-89657)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2022年12月5日 08:41](https://h4ck.org.cn/2022/12/10833#comment-89668)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      好多都不怎么维护更新了。现在精力实在是有限，关键是还tm天天加班。

      [回复](#comment-89668)

### 发表回复 [取消回复](/2022/12/10833#respond)

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

* [Python](https://h4ck.org.cn/tags/python)
* [游戏](https://h4ck.org.cn/tags/game)
* [IDA](https://h4ck.org.cn/tags/ida)
* [心情](https://h4ck.org.cn/tags/myfeeling)
* [Windows](https://h4ck.org.cn/tags/windows)
* [无题](https://h4ck.org.cn/tags/nomean)
* [CentOS](https://h4ck.org.cn/tags/centos)
* [Linux](https://h4ck.org.cn/tags/linux)
* [ASM](https://h4ck.org.cn/tags/asm)
* [iOS](https://h4ck.org.cn/tags/ios)
* [APK](https://h4ck.org.cn/tags/apk)
* [妹子图](https://h4ck.org.cn/tags/%E5%A6%B9%E5%AD%90%E5%9B%BE)
* [Crack](https://h4ck.org.cn/tags/crack)
* [Delphi](https://h4ck.org.cn/tags/delphi)
* [C/C++](https://h4ck.org.cn/tags/cc)
* [QQ](https://h4ck.org.cn/tags/qq)
* [爬虫](https://h4ck.org.cn/tags/%E7%88%AC%E8%99%AB)
* [闺蜜圈](https://h4ck.org.cn/tags/%E9%97%BA%E8%9C%9C%E5%9C%88)
* [大姨妈](https://h4ck.org.cn/tags/%E5%A4%A7%E5%A7%A8%E5%A6%88)
* [Django](https://h4ck.org.cn/tags/django)
* [PETools](https://h4ck.org.cn/tags/petools)
* [Google](https://h4ck.org.cn/tags/google)
* [月经](https://h4ck.org.cn/tags/%E6%9C%88%E7%BB%8F)
* [spider](https://h4ck.org.cn/tags/spider)
* [驱动开发](https://h4ck.org.cn/tags/driver-develop)
* [Mac OS](https://h4ck.org.cn/tags/mac-os)
* [Debugger](https://h4ck.org.cn/tags/debugger)
* [Plugin](https://h4ck.org.cn/tags/plugin)
* [php](https://h4ck.org.cn/tags/php)
* [WordPress](https://h4ck.org.cn/tags/wordpress)
* [Porn](https://h4ck.org.cn/tags/porn)
* [文本编辑](https://h4ck.org.cn/tags/texteditor)
* [OD](https://h4ck.org.cn/tags/od)
* [jeb](https://h4ck.org.cn/tags/jeb)
* [Android](https://h4ck.org.cn/tags/android)
* [系统美化](https://h4ck.org.cn/tags/os-diy)
* [OSX](https://h4ck.org.cn/tags/osx)
* [Python3](https://h4ck.org.cn/tags/python3)
* [UniApp](https://h4ck.org....