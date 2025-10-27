---
title: Nginx日志分析工具goaccess
url: https://h4ck.org.cn/2023/01/nginx%e6%97%a5%e5%bf%97%e5%88%86%e6%9e%90%e5%b7%a5%e5%85%b7goaccess/
source: obaby@mars
date: 2023-01-14
fetch_date: 2025-10-04T03:50:00.496425
---

# Nginx日志分析工具goaccess

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

# Nginx日志分析工具goaccess

2023年1月13日
[11 条评论](https://h4ck.org.cn/2023/01/11006#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/10/557b504053cb3f7e2dd4bfbfc7c9ab88-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/10/557b504053cb3f7e2dd4bfbfc7c9ab88-scaled.jpg)

时不时地会出现服务器cpu占用率100%的情况，基本到这时候php基本就全挂了，而出问题的也是php-fpm这个进程。说实话对于这个破进程真是没什么好的想法，进程数量怎么设置都不对，反正就是只要开机就各种卡。其实也考虑过是不是被攻击了，但是就这么个破网站，个人感觉攻击也没什么意思啊。图什么呢~~

通过top命令以及trace命令，没有找到什么有用的线索。不过通过查看访问日志可以看到每秒都有数条请求，这尼玛就很神奇啊，每天的访问量不过1k多点，怎么可能会每一秒都那么多请求呢。通过tail命令查看访问日志太蛋疼了，于是就想着找个更加可视化的工具，于是找到了goaccess：

*GoAccess*是一款开源的且具有交互视图界面的实时Web 日志分析工具,通过你的Web 浏览器或者 \*nix 系统下的终端程序(terminal)即可访问。 能为系统管理员提供快速且有价值的 HTTP 统计,并以在线可视化视图。

通过下面的命令即可安装：

```
apt install goaccess
```

安装之后通过下面的命令启动工具：

```
goaccess /home/wwwlogs/h4ck.org.cn.log -c
```

选择日志格式之后就可以查看数据了：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/搜狗截图20230113221904.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230113221904.jpg)

通过tab可以切换数据，日志清空之后不到一天时间已经2万多条请求了，这就很离谱啊，哪里有那么达到访问量。分析之后发现瑞典和德国的两个ip，直接给加到防火墙里面去了，但是并没有什么改观。现在操作系统和浏览器第一的数据还是来源于上面被ban掉的两个ip

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/搜狗截图20230113222130.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230113222130.jpg)

命令行多少有些不直观，可以通过下面的命令生成html报告：

```
LANG="en_US.UTF-8" goaccess --no-global-config --log-format='%h - %^ [%d:%t %^] "%m %U %H" %s %b "%R" "%u" %^ "%v" "%^" %Dms' --date-format='%d/%b/%Y' --time-format='%T' --log-file=/home/wwwlogs/h4ck.org.cn.log  --output=/home/wwwroot/h4ck/report.html
```

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/2023-01-13-22.24.01-h4ck.org_.cn-40c03b040bfb-tuya-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/2023-01-13-22.24.01-h4ck.org_.cn-40c03b040bfb-tuya-scaled.jpg)

也可以通过下面的命令启动实时模式：

```
LANG="en_US.UTF-8" goaccess --no-global-config --addr=0.0.0.0 --port=7890 --ws-url=0.0.0.0 --port=8848 --real-time-html --log-format='%h - %^ [%d:%t %^] "%m %U %H" %s %b "%R" "%u" %^ "%v" "%^" %Dms' --date-format='%d/%b/%Y' --time-format='%T' --log-file=/home/wwwlogs/h4ck.org.cn.log --output=realtime.html
```

不过通过nginx反代websocket之后400错误了，这个还没找到解决办法，谁知道怎么处理的还望不吝赐教。

不过最后解决问题的办法还是升级了一下服务器配置，哎，我就是那个大冤种。是不是阿里云故意的啊~~

当前系统负载：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/01/搜狗截图20230113210139.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/01/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230113210139.jpg)

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Nginx日志分析工具goaccess》](https://h4ck.org.cn/2023/01/11006)
\* 本文链接：<https://h4ck.org.cn/2023/01/11006>
\* 短链接：<https://oba.by/?p=11006>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[goaccess](https://h4ck.org.cn/tags/goaccess)[nginx](https://h4ck.org.cn/tags/nginx)[WordPress](https://h4ck.org.cn/tags/wordpress)

[Previous Post](https://h4ck.org.cn/2023/01/11023)
[Next Post](https://h4ck.org.cn/2023/01/10995)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年3月28日

#### [也谈WordPress说说/微博功能](https://h4ck.org.cn/2023/03/11659)

2022年8月21日

#### [WordPress 评论显示IP归属地](https://h4ck.org.cn/2022/08/10404)

2012年5月10日

#### [WordPress jQuery隐藏侧边栏](https://h4ck.org.cn/2012/05/4061)

### 11 comments

1. ![](https://gg.lang.bi/avatar/1c03767b0691f80231895255661bcf42eceab95dc8b493ee80c835b07f577f49?s=64&d=identicon&r=r) **[TeacherDu](https://dusays.com)**说道：

   [2023年1月14日 03:18](https://h4ck.org.cn/2023/01/11006#comment-91096)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 108](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 108") Microsoft Edge 108 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   增加缓存插件，尽可能静态化文章页面，CPU高但内存用的少，基本是PHP问题！

   [回复](#comment-91096)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2023年1月14日 11:35](https://h4ck.org.cn/2023/01/11006#comment-91103)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 108](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 108") Google Chrome 108 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      嗯嗯，发现是php的问题了，一个index.php执行时间超过了100秒。慢查询也没发现很好资源的东西，但是就是卡死了。之前也出现过几次，这次上个静态插件试试效果吧。 ![dance](https://h4ck.org.cn/wp-content/plugins/kama-wp-smile/packs/qip/dance.gif)

      [回复](#comment-91103)

      1. ![](https://gg.lang.bi/avatar/1c03767b0691f80231895255661bcf42eceab95dc8b493ee80c835b07f577f49?s=64&d=identicon&r=r)

         [2023年1月14日 14:56](https://h4ck.org.cn/2023/01/11006#comment-91111)

         ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

         ![Microsoft Edge 108](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 108") Microsoft Edge 108 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

         WP的数据库优化实在是不好评价，还是加个静态缓存，或是动态缓存，看服务器的配置了！

         [回复](#comment-91111)

         1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

            [2023年1月14日 19:37](https://h4ck.org.cn/2023/01/11006#comment-91118)

            ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

            ![Google Chrome 108](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 108") Google Chrome 108 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

            嗯嗯，试了几个插件，效果都不大好。还是继续litespeed cache吧。

            [回复](#comment-91118)
2. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r)

   [2023年1月14日 10:54](https://h4ck.org.cn/2023/01/11006#comment-91099)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Goog...