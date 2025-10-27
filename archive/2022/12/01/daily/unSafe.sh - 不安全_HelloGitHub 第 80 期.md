---
title: HelloGitHub 第 80 期
url: https://buaq.net/go-137924.html
source: unSafe.sh - 不安全
date: 2022-12-01
fetch_date: 2025-10-04T00:09:49.227103
---

# HelloGitHub 第 80 期

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/cc8c12dcd76a20cae70014344f7f7a2c.jpg)

HelloGitHub 第 80 期

《HelloGitHub》第 80 期HelloGitHub 分享 GitHub 上有趣、入门级的开源项目，每月 28 号更新一期。 这里有好玩和入门级的开源项目、开源书籍、实战项目、企业级项目，让你
*2022-11-30 19:31:33
Author: [hellogithub.com(查看原文)](/jump-137924.htm)
阅读量:48
收藏*

---

## 《HelloGitHub》第 80 期

HelloGitHub 分享 GitHub 上有趣、入门级的开源项目，每月 28 号更新一期。 这里有好玩和入门级的开源项目、开源书籍、实战项目、企业级项目，让你用极短的时间感受到开源的魅力，对开源产生兴趣。

Star 7.5kFork 895Watch 190

基于 Web 的服务器图形界面。这是一款开源的服务器管理工具，让你可以通过 Web 界面轻松管理 Linux 服务器，支持配置防火墙、Web 终端、容器管理、查看系统日志等功能。

![cockpit](https://img.hellogithub.com/i/8jkOdaXLFhuMgeV_1669461142.png)

Star 2.1kFork 122Watch 20

阻止 Windows 流氓软件授权的工具。它轻巧、无需后台运行，可用于阻止指定软件的管理员授权。

![Malware-Patch](https://img.hellogithub.com/i/yug7zKD2dEBrCqj_1669462198.png)

Star 3.1wFork 8.1kWatch 1.3k

Android 获取 Root 权限的工具。它可以快速、无痛地获得 Android 的超级用户权限，支持 Android 5.0 以上的设备。

![Magisk](https://img.hellogithub.com/i/QCxAe2b0kpW1j8G_1669519959.png)

Star 2wFork 2.4kWatch 690

像数据库一样查询设备的工具。它将操作系统抽象成一个数据库，让用户可以通过 SQL 查询操作系统的运行情况，比如运行中的进程、网络连接、文件和用户。攻击者一般会在运行恶意程序后删掉程序，通过 osquery 可以轻松找到没有源文件的进程。

```
osquery> SELECT name, path, pid FROM processes WHERE on_disk = 0;
name = Drop_Agent
path = /Users/jim/bin/dropage
pid = 561
```

![osquery](https://img.hellogithub.com/i/bl58xNwFSBvMZKp_1669521310.png)

Star 5.9kFork 270Watch 79

仅用 CSS 实现网络聊天。前端不用 JavaScript 只用 CSS 实现网络聊天的功能，秘诀是伪选择器加载的背景图像和永远加载的索引页。

```
.some-button:active {
  background-image: url('some_image.jpg')
}
```

![css-only-chat](https://img.hellogithub.com/i/oZ3C5GN8qrhmxBf_1669523697.gif)

Star 2.9kFork 115Watch 18

可直接用 SQL 查询数据文件的命令行工具。通过该项目无需将数据导入数据库，就能用 SQL 查询文件内的数据，可执行模糊查询、计数、排序等命令，支持 JSON、CSV、Excel、Parquet、YAML 等类型的文件。还可以搭配其它命令行工具(jq)，实现更丰富的功能。

```
$ dsq testdata/userdata.parquet 'select count(*) from {}' | jq
[
  {
    "count(*)": 1000
  }
]
```

Star 1.4wFork 2.1kWatch 401

一款由 Google 开源的容器监控工具。它可以实时统计容器运行时占用的资源，包括 CPU 利用率、内存使用量、网络传输等信息。提供了 Web 可视化页面，能方便用户分析和监控容器运行状态，支持包括 Docker 在内的几乎所有类型的容器。

```
sudo docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:ro \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --volume=/dev/disk/:/dev/disk:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  --privileged \
  --device=/dev/kmsg \
  gcr.io/cadvisor/cadvisor:$VERSION
```

![cadvisor](https://img.hellogithub.com/i/z2ur1pi3nNaTSJP_1669212080.png)

Star 3.1kFork 443Watch 85

用 Go 重新实现的 supervisord 。开源项目 supervisord 作为 Python 项目中常用的进程管理工具，深受广大开发爱好者的喜欢。但如果在非 Python 环境的情况下，用起来就不是那么顺手啦，所以作者用 Go 重写了 supervisord，编译后可以方便地运行在任何环境下。

```
$ cat supervisor.conf
[program:test]
command = /your/program args
$ supervisord -c supervisor.conf
```

![supervisord](https://img.hellogithub.com/i/pnkyE2bCgclH9uG_1669259567.png)

Star 3.9kFork 462Watch 57

立刻将 JSON 转化为 Go 类型定义的工具。这是一个用 JavaScript 写的在线小工具，可以直接将输入的 JSON 转成对应的 Go 类型定义。

![json-to-go](https://img.hellogithub.com/i/7hiOdVlULspaynz_1669260840.png)

Star 1.7wFork 602Watch 110

仅一个文件的开源后端。将 SQLite 数据库、接口服务、登录认证、管理后台等服务器端的功能，做成一个开箱即用的可执行文件。让原本不懂后端开发的用户，也可以通过用户界面快速构建起接口服务。

![pocketbase](https://img.hellogithub.com/i/1kxWEQqFgphYiXa_1669271839.png)

Star 4.4kFork 234Watch 65

一款免费、安全、开源的 2FA 安卓应用。双重认证(2FA) 就是使用两种不同的元素来确认用户身份，比如用户名和密码是一种元素，手机号和短信验证码也是一种元素，两种元素结合就是双重认证。除了短信之外还有一种 APP 可生成和验证码功能类似的一次性密码(TOTP)，Aegis 就是一款支持 HOTP 和 TOTP 算法的开源 2FA 应用，使用时要先将手机和账号绑定，绑定后 APP 就会定时刷新一组随机数字，需要双重认证时输入这串数字即可。

![Aegis](https://img.hellogithub.com/i/NYfWehtZRXGcQ16_1669360380.png)

Star 2wFork 7.8kWatch 871

一款由 Java 编写的开源持续集成工具。做为开源 CI/CD 软件的王者，它专注于自动化你的开发工作流程，具有安装简单、友好的操作页面、易于扩展、分布式的特点，常用来优化项目开发流程或自动化各种任务。

```
1. 下载 jar 包
2. 运行：java -jar jenkins.war --httpPort=8080
3. 打开浏览器访问：http://localhost:8080
4. 根据提示完成安装
```

![jenkins](https://img.hellogithub.com/i/0GfViM4RWr5sdcS_1669362693.jpg)

Star 2.3kFork 754Watch 60

开箱即用的网络视频平台。基于 GB28181 标准实现的网络视频平台，能够接入摄像机、平台、NVR 等设备、支持视频预览、云台控制、录像查询和回放、无人观看自动断流等功能。

![wvp-GB28181-pro](https://img.hellogithub.com/i/yQOhxLdg8kqUANm_1669365788.png)

Star 3.4wFork 7.8kWatch 902

一款可自由定制的企业级开源通信平台。功能丰富的通信平台，可自托管做为 Slack 的开源替代品。支持创建频道、团队和讨论等多种不同功能的群聊，消息支持图片、文件、视频和语音，拥有包括 Windows、Linux、macOS、Android 和 iOS 在内的多种客户端。

![Rocket.Chat](https://img.hellogithub.com/i/cA1QUwLtivnxdJN_1669283861.jpg)

Star 2.4wFork 2.6kWatch 478

可能是最小的编译器。仅用 1000 行 JavaScript 代码实现的迷你编译器，其中注释还占了一大半，实际代码只有 200 行左右。它虽然代码量不多，但完整地实现了编译器基本功能，可以用来学习编译器原理。

![the-super-tiny-compiler](https://img.hellogithub.com/i/VrqlgBWE9QkmGSw_1669276900.png)

Star 4.2wFork 2.6kWatch 610

基于 JavaScript 的下一代前端测试工具。主要用于浏览器端到端测试的自动化工具，端到端(E2E)测试就是站在用户的角度，模拟实际使用场景的测试方式。Cypress 目前已成主流浏览器端到端测试工具，它运行速度快、上手简单，支持图形化界面可实时观察执行情况，以及截屏和视频记录测试结果。

![cypress](https://img.hellogithub.com/i/0YAraqH4hjnuZgS_1669279803.gif)

Star 528Fork 63Watch 3

一款完全自定义配置的浏览器起始页。基于 Vite+Vue3+TypeScript 构建的浏览器起始页，预设了多款简洁清爽的主题开箱即用，能够随心所欲地添加组件，编辑模式下可拖拽组件更改大小和位置，支持浏览器插件和网页两种使用方式。

![Dashboard](https://img.hellogithub.com/i/a3Bi8Crd19vFSG2_1669286451.png)

Star 2.4wFork 917Watch 123

专为程序员打造的演示文稿工具。该项目是基于 Web 的幻灯片制作和演示工具，让用户可以使用 纯文本+Markdown 语法制作幻灯片，支持导出为 PDF 或 PNG 格式的文件，或以单页面展示幻灯片。对于大多数不擅长做 PPT 的程序员，基于提供的现成主题也可以制作出看起来不错的演示文稿。

![slidev](https://img.hellogithub.com/i/Uu7ejnYEfdPK5wm_1669282085.png)

Star 8.7kFork 1.8kWatch 329

完全免费的短网址服务。采用 PHP 编写的短网址服务，它完全开源可自行搭建服务，支持数据统计、地理位置、可视化等功能。

![YOURLS](https://img.hellogithub.com/i/ucJionQysNjwDUz_1669518562.gif)

Star 2.4kFork 52Watch 12

更加人性化的 Python 调度库。可通过 Python 装饰器语法，进行任务调度的 Python 库。它简单、优雅、高效，支持定时、并发（异步、多线程、多进程）、条件触发等功能。

```
from rocketry import Rocketry
from rocketry.conds import daily

app = Rocketry()

@app.task(daily)
def do_daily():
    ...

@app.task(daily & file_exists("data.csv"))
def do_things():
    ...

if __name__ == '__main__':
    app.run()
```

Star 4.1kFork 259Watch 40

一款轻巧的投屏接收器。该项目可以让电脑接收来自手机的视频、图片和音乐投屏，支持手机上的主流视频和音乐软件，以及其它符合 DLNA 协议的软件。无打扰地运行在状态栏和菜单栏，适用于 Windows、macOS、Linux 操作系统。

![Macast](https://img.hellogithub.com/i/6KghlyXL2Ybd5H7_1669389550.png)

Star 1.7kFork 21Watch 22

Python 热重载调试工具。在不重启程序的前提下，通过这个项目可以查看改动后、最新的 Python 代码运行效果，以及每行代码的耗时。有了它可以更高效地调试 Python 代码，强烈推荐在 PyCharm 和 VSCode 上使用。

![reloadium](https://img.hellogithub.com/i/YkZWMHSXlepg3Qx_1669384088.gif)

Star 6.6kFork 369Watch 43

简单好用的网站变更检测、监控和通知服务。基于 Flask+Selenium 构建的 Web 服务，可以在目标网站发生变化时发出通知，可用于监控商品降价、工作机会、版本发布、最新内容等，支持 Docker 的安装方式。

![changedetection.io](https://img.hellogithub.com/i/Tu597zvUPIemdaV_1669432621.png)

Star 1.4wFork 1.8kWatch 366

一款功能强大的电子书管理工具。它是集下载、格式转化、制作、管理于一体的电子书工具，比如可以将 txt 文本，转化成包含作者信息和书籍封面的 mobi 文件，制作完成后还可以直接发送到 Kindle 设备上。

![calibre](https://img.hellogithub.com/i/6lbWTN9BnYewZgz_1669437239.png)

Star 4.9kFork 200Watch 59

WebSockets 的命令行客户端。一条命令连接或建立 WebSockets 服务，适用于 Windows、macOS、Linux。

```
A$ websocat -s 1234
Listening on ws://127.0.0.1:1234/
ABC
123

B$ websocat ws://127.0.0.1:1234/
ABC
123
```

Star 1.6kFork 30Watch 10

可轻松监控网络流量的工具。这是一个简单、可靠、炫酷的网络监控应用，可以让你一目了然地了解设备的网络流量。

![sniffnet](https://img.hellogithub.com/i/zkcnxiTuOLBY3US_1669522318.gif)

Star 1.4wFork 205Watch 51

命令行文件对比工具。一种可根据文件的语法，进行结构化比较的工具，支持 30 多种编程语言。

![difftastic](https://img.hellogithub.com/i/KtPyNjx90nGLOav_1669543875.png)

Star 5.1kFork 382Watch 112

一款适用于 macOS 的轻量级纯文本编辑器。它免费、整洁、启动速度快，拥有看起来十分舒服的界面。

![CotEditor](https://img.hellogithub.com/i/pCyxZAwPV8s3g65_1669390573.png)

Star 178Fork 21Watch 2

超低成本的短信转发器。通过该项目仅需 50 元就可以制作出一个短信转发器，实现不用手机接收验证码。

![sms_forwarding](https://img.hellogithub.com/i/0Z8UWsNupEK53TF_1669468579.jpg)

Star 1.6kFork 94Watch 15

玩游戏学习 Shell。这是一款帮助入门 shell 命令的文字游戏。

![GameShell](https://img.hellogithub.com/i/EJw3zLMlbHiajfd_1669517340.gif)

Star 6.3wFork 6.9kWatch 1.5k

专为程序员准备的免费服务清单。现在虽然有大量免费的服务，但大多数开发者很难找到它们，这是一份免费服务(SaaS、PaaS、IaaS 等)和产品的列表。

Star 1kFork 292Watch 54

在线字体编辑器。在线编...