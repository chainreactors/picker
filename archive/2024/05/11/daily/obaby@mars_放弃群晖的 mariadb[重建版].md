---
title: 放弃群晖的 mariadb[重建版]
url: https://h4ck.org.cn/2024/05/16937
source: obaby@mars
date: 2024-05-11
fetch_date: 2025-10-06T17:16:07.419971
---

# 放弃群晖的 mariadb[重建版]

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

[个人日记『Diary』](https://h4ck.org.cn/cats/dddd/grrj)

# 放弃群晖的 mariadb[重建版]

2024年5月10日
[19 条评论](https://h4ck.org.cn/2024/05/16937#comments)

![](https://h4ck.org.cn/wp-content/uploads/2024/05/8041715319650_.pic_.jpg)

就在刚刚，尝试将 mysql 从 5 升级到 8，然后再一次数据全部丢掉了，这篇文章也没了。后来想到[XIGE](https://www.xigeshudong.com) 的 rss 阅读器，过去看了下果然文章还在，于是又给拷贝过来了。❤️，嘻嘻。所以这是一个重制版！（**评论是回不来了**）

刚把服务迁回家里的时候，由于服务器用的是二手工控机。为了避免数据丢失问题，在群晖上安装了mariadb 数据库。但是这个数据库在使用的过程中出现过不少问题。
第一次是maridb 版本升级，升级之后数据库异常的卡。不管是代码连接还是工具连接都得十几秒才能连上。导致整个博客也跟着直接卡死了，页面渲染时间基本要十几秒。后来优化表结构修复表结构，稍微好了一些。
昨天晚上群晖提示固件可以升级，本身不是大版本升级，自认为应该问题不大。但是，升级之后又出现了之前群晖升级的时候 出现的问题了。整个页面生成时间需要 22 秒，测了下速，果然全部都红了。
想着现在服务器换成了 mac mini，那么数据库也就没有必要用群晖的了，但是在迁移数据的时候，让人更崩溃的事情出现了。navicat 无法同步数据，部分表创建失败，直接通过结构同步，发现少了很多关键性表。

![](https://h4ck.org.cn/wp-content/uploads/2024/05/Screenshot-2024-05-10-080410.png)
同步数据库结构依然出错，执行不下去。

![](https://h4ck.org.cn/wp-content/uploads/2024/05/Screenshot-2024-05-10-080434.png)
这时候想起来群晖上有 phpmyadmin，通过 phpmyadmin 导出数据：

![](https://h4ck.org.cn/wp-content/uploads/2024/05/Screenshot-2024-05-10-080248-1.png)
勾选创建对象的配置，最终通过 mysql 的 source 命令算是导入成功了。
到这里第一步算是完成了，然而，在重启 mysql 服务的时候出现了另外一个问题，由于之前数据同步失败，想在服务器上安装 mariadb，结果apt 安装之后，不知道密码，不知道路径，一切信息都没回显，还导致 mysql 启动失败了。
删除错误配置文件之后，从此 mysql 就跑不动了。这尼玛，通过 lnmp 重装结果 php 又安装失败了。并且最终无法执行 lnmp 命令。这就让人很尴尬了。
最终通过投机取巧的办法解决了安装问题，安装之前先完全卸载 mariadb，同时备份好数据库：

```
sudo apt-get remove mysql-*
sudo apt-get autoremove --purge mysql-server -y
apt-get remove mysql-common -y
sudo apt-get purge mariadb-*
sudo apt-get purge mariadb-server
sudo apt-get autoremove
```

清理残留文件：

```
dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P
sudo rm -rf /etc/mysql
sudo rm -rf /var/lib/mysql
dpkg -l |grep mysql 找到后卸载
rm -rf /etc/mysql/
rm -rf /var/log/mysql
rm -rf /usr/share/mysql
rm -rf /run/mysqld
```

1.lnmp 只安装 nginx
./install.sh nginx
2.通过upgrade.sh安装特定版本 php
./upgrade.sh php
安装版本 7.4.29
3.剩下的就是修复结巴分次，以及 redis 的问题。
./addons.sh install redis
这真是让人充满了蛋蛋的忧伤啊，就差点重装系统了。
这个系统的升级跟软件升级总感觉还是有些区别的，群晖的系统版本已经落后了四个小版本，想着升级下，结果又整出这么多幺蛾子来，真是让人无语。虽然说了很多次能跑就不要动，但是有时候自动升级在不知情的情况下就给升级了。
而至于升级之后，有没有问题，这个就完全成了人品问题。感觉也没什么办法能保障系统升级不出问题。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《放弃群晖的 mariadb[重建版]》](https://h4ck.org.cn/2024/05/16937)
\* 本文链接：<https://h4ck.org.cn/2024/05/16937>
\* 短链接：<https://oba.by/?p=16937>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[lnmp](https://h4ck.org.cn/tags/lnmp)[Mariadb](https://h4ck.org.cn/tags/mariadb)[Mysql](https://h4ck.org.cn/tags/mysql)

[Previous Post](https://h4ck.org.cn/2024/05/16942)
[Next Post](https://h4ck.org.cn/2024/05/16929)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2024年2月8日

#### [年年岁岁花相似](https://h4ck.org.cn/2024/02/15417)

2024年11月1日

#### [免费洗车](https://h4ck.org.cn/2024/11/18434)

2025年9月11日

#### [邪修还是正修？ — 解决捷豹 XEL 后排异响](https://h4ck.org.cn/2025/09/21525)

### 19 comments

1. ![](https://gg.lang.bi/avatar/5d3b04c9c4a8b58d5049988184be392b3ce6141900a0f9295c2e4fbee234c9cd?s=64&d=identicon&r=r) **[皇家元林](https://hjyl.org)**说道：

   [2024年5月10日 16:05](https://h4ck.org.cn/2024/05/16937#comment-115046)

   ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Firefox 125](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/firefox.png "Firefox 125") Firefox 125 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   这个操作6啊！
   好像备份都显得没那么重要了

   [回复](#comment-115046)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年5月10日 16:58](https://h4ck.org.cn/2024/05/16937#comment-115049)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 118](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 118") Google Chrome 118 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      哈哈哈。这个是属于骚操作了。还是有必要的，比如文件备份之类的。
      尽量还是做好备份吧，这不，评论数据丢了就回不来了。

      [回复](#comment-115049)
2. ![](https://gg.lang.bi/avatar/9f9183dfbd5ad67b7d170513f32bcb6cdbfbe16f1211ebc5cede32953c449937?s=64&d=identicon&r=r)

   [2024年5月10日 16:17](https://h4ck.org.cn/2024/05/16937#comment-115047)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Google Chrome 124](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 124") Google Chrome 124 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   牛牛牛，姐姐真牛 ![kiss](https://h4ck.org.cn/wp-content/plugins/kama-wp-smile/packs/qip/kiss.gif)

   [回复](#comment-115047)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年5月10日 16:59](https://h4ck.org.cn/2024/05/16937#comment-115050)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 118](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 118") Google Chrome 118 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      ![kiss](https://h4ck.org.cn/wp-content/plugins/kama-wp-smile/packs/qip/kiss.gif)

      [回复](#comment-115050)
3. ![](https://gg.lang.bi/avatar/c8b1c4e066955840427abd9f454b9fb9569d4480ec1b84bb78c8b210d91893d8?s=64&d=identicon&r=r)

   [2024年5月10日 16:21](https://h4ck.org.cn/2024/05/16937#comment-115048)

   ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 124](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 124") Microsoft Edge 124 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![us](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/us.svg "us")

   怪不得早上访问灵妹妹要么502错误，要么数据库连接错误

   [回复](#comment-115048)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年5月10日 16:59](https://h4ck.org.cn/2024/05/16937#comment-115051)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 118](https://h4ck.o...