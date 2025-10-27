---
title: sh 脚本给 screen 传递命令【非交互模式】
url: https://h4ck.org.cn/2024/10/18372
source: obaby@mars
date: 2024-10-20
fetch_date: 2025-10-06T18:46:15.201752
---

# sh 脚本给 screen 传递命令【非交互模式】

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

# sh 脚本给 screen 传递命令【非交互模式】

2024年10月19日
[34 条评论](https://h4ck.org.cn/2024/10/18372#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/10/2024_09_29_15_10_IMG_5571.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/10/2024_09_29_15_10_IMG_5571.jpg)

之所以要在 sh 中给 screen 传递命令是因为阿里云的 99 的服务器实在是[太拉跨了](https://h4ck.org.cn/microposts/%E9%98%BF%E9%87%8C%E4%BA%91-99-%E7%9A%84%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%A4%AA%E6%8B%89%E5%9E%AE%E4%BA%86)，并且经常会出现各种诡异的 cpu 跑满的情况。目前上面部署了几个静态站点还有 umami 的统计。

先介绍下 screen：

> screen是linux下的一种视窗多重复用管理程序。在使用[telnet](https://baike.baidu.com/item/telnet/810597?fromModule=lemma_inlink)或[SSH](https://baike.baidu.com/item/SSH/10407?fromModule=lemma_inlink)远程登录[linux](https://baike.baidu.com/item/linux/27050?fromModule=lemma_inlink)时，如果连接非正常中断，重新连接时，系统将开一个新的session，无法恢复原来的session.screen命令可以解决这个问题。

umami、moe-conter 都是通过 screen 启动的，这就导致如果服务器重启了就得重新启动 screen，然后在 screen 中运行命令来启动服务。

阿里云的服务器经常莫名其妙 cpu 就 100 了，当然也可能是收到了攻击，但是具体情况感觉还是太频繁了，此时最简单的办法就是直接强制重启。

如果直接把要执行的命令加到 screen 命令之后写入到 sh 脚本，命令无法正常运行。合格的写法应该是下面的样子（一种形式，还有其他形式）：

```
screen -S moe  -dmS
screen -x -S moe -p 0 -X stuff "cd /root/Moe-Counter
"
screen -x -S moe -p 0 -X stuff "sh start.sh
"
```

注意screen -x -S moe -p 0 -X stuff “cd /root/Moe-Counter 一行指令是回车换行编写的，相当于把回车代入到了 cd 命令后面，这样写的好处是省去了插入回车，也可以用下面的写法：

```
screen -xS screenName -p0 -X stuff $'\n'
```

$’\n’ 代表回车，我觉得直接换行是最简单的。

有了启动脚本，剩下的就是编辑服务，添加自启动功能：

```
vim /etc/systemd/system/myautostart.service
```

创建自定义服务，添加代码：

```
[Unit]
Description=My autostart Service
After=network.target

[Service]
User=firefly
ExecStart=/root/sh/start_all.sh
Restart=always
RestartSec=1

[Install]
WantedBy=multi-user.target
```

重新加载服务：

```
systemctl daemon-reload
```

此时在重启，服务就可以自动启动了，省去了人工启动的麻烦。

[![](https://h4ck.org.cn/wp-content/uploads/2024/10/Jietu20241019-105541.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/10/Jietu20241019-105541.jpg)

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《sh 脚本给 screen 传递命令【非交互模式】》](https://h4ck.org.cn/2024/10/18372)
\* 本文链接：<https://h4ck.org.cn/2024/10/18372>
\* 短链接：<https://oba.by/?p=18372>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[screen](https://h4ck.org.cn/tags/screen)[systemctl](https://h4ck.org.cn/tags/systemctl)[阿里云](https://h4ck.org.cn/tags/%E9%98%BF%E9%87%8C%E4%BA%91)

[Previous Post](https://h4ck.org.cn/2024/10/18393)
[Next Post](https://h4ck.org.cn/2024/10/18337)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年2月11日

#### [是UPS吖（三）–-树莓派](https://h4ck.org.cn/2023/02/11176)

2013年4月14日

#### [BackTrack5 RC3（2）System](https://h4ck.org.cn/2013/04/5098)

2023年2月11日

#### [是UPS吖（二）–-群晖](https://h4ck.org.cn/2023/02/11167)

### 34 comments

1. ![](https://gg.lang.bi/avatar/950deeb4218c9ed0022292e431abf0c097f984521c4dadd7d6316402f2b273fc?s=64&d=identicon&r=r) **[klcdm](https://koxiuqiu.cn/)**说道：

   [2024年10月19日 11:18](https://h4ck.org.cn/2024/10/18372#comment-119924)

   ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![Microsoft Edge 129](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 129") Microsoft Edge 129 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   沙发

   [回复](#comment-119924)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年10月19日 11:44](https://h4ck.org.cn/2024/10/18372#comment-119927)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      ![dance](https://h4ck.org.cn/wp-content/plugins/kama-wp-smile/packs/qip/dance.gif)

      [回复](#comment-119927)
2. ![](https://gg.lang.bi/avatar/d98dfdf4e1f6a84bbf50554abbd9fa5f81431acef40126d2fdcb5bb3b99d444a?s=64&d=identicon&r=r)

   [2024年10月19日 11:27](https://h4ck.org.cn/2024/10/18372#comment-119925)

   ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Google Chrome 127](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 127") Google Chrome 127 ![GNU/Linux](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/linux.png "GNU/Linux") GNU/Linux ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   这 纹身和腿太明显了 下面的文章和代码都没心思看了😂

   [回复](#comment-119925)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年10月19日 11:44](https://h4ck.org.cn/2024/10/18372#comment-119926)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      腿太粗了是吧？😂

      [回复](#comment-119926)

      1. ![](https://gg.lang.bi/avatar/d98dfdf4e1f6a84bbf50554abbd9fa5f81431acef40126d2fdcb5bb3b99d444a?s=64&d=identicon&r=r)

         [2024年10月20日 09:00](https://h4ck.org.cn/2024/10/18372#comment-119956)

         ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

         ![Google Chrome 127](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 127") Google Chrome 127 ![GNU/Linux](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/linux.png "GNU/Linux") GNU/Linux ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

         不是不是 是纹身有创意😂😂

         [回复](#comment-119956)
      2. ![](https://gg.lang.bi/avatar/7247a9c7bdf7ee3989075882e5a445c87a462c93a971ffc16c11819e8da6f93b?s=64&d=identicon&r=r)

         [2024年10月21日 09:10](https://h4ck.org.cn/2024/10/18372#comment-119967)

         ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

         ![Google Chrome 130](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 130") Google Chrome 130 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10...