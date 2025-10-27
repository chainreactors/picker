---
title: MySQL datetime default 0000-00-00 00:00:00❤
url: https://h4ck.org.cn/2024/05/16942
source: obaby@mars
date: 2024-05-11
fetch_date: 2025-10-06T17:16:06.543595
---

# MySQL datetime default 0000-00-00 00:00:00❤

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

[博客相关『Blogger/WordPress』](https://h4ck.org.cn/cats/jyzj/wordp)

# MySQL datetime default 0000-00-00 00:00:00❤

2024年5月10日
[20 条评论](https://h4ck.org.cn/2024/05/16942#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/05/default-8-e1715346663855.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/05/default-8.jpg)

本来以为是mysql版本的问题，上午搜索的时候也是这个错误，搜索了一下有的人说是mysql版本问题。于是上午尝试将mysql 从5.7升级到8.0，不出意外，又失败了，数据库丢失，并且mysql安装失败了。

下午晚上尝试优化数据库的时候又出现了这个错误：

[![](https://h4ck.org.cn/wp-content/uploads/2024/05/Screenshot-2024-05-10-205941.png)](https://h4ck.org.cn/wp-content/uploads/2024/05/Screenshot-2024-05-10-205941.png)

[![](https://h4ck.org.cn/wp-content/uploads/2024/05/Screenshot-2024-05-10-205947.png)](https://h4ck.org.cn/wp-content/uploads/2024/05/Screenshot-2024-05-10-205947.png)

又搜索了一下发现是mysql设置问题，下面是抄的百度ai的，不得不说，这段答复质量还是可以的：

在MySQL中，如果你尝试将一个日期时间字段（DATETIME）的默认值设置为’0000-00-00 00:00:00’，你可能会遇到一个错误，因为MySQL不允许使用’0000-00-00 00:00:00’作为有效的日期时间值。

解决方案：

修改MySQL配置文件：

你可以在MySQL的配置文件（通常是my.cnf或者my.ini）中设置sql\_mode，将其设置为允许’0000-00-00 00:00:00’。

```
[mysqld]
sql_mode=NO_ENGINE_SUBSTITUTION
```

然后重启MySQL服务。

使用NOW()或CURRENT\_TIMESTAMP作为默认值：

如果你不需要’0000-00-00 00:00:00’作为默认值，你可以使用NOW()或CURRENT\_TIMESTAMP作为默认值，这样在插入新行时，如果没有为DATETIME字段指定值，它将自动使用当前的日期时间。

```
CREATE TABLE example (
id INT PRIMARY KEY,
created_at DATETIME DEFAULT NOW()
);
```

使用ON INSERT触发器：

如果你需要’0000-00-00 00:00:00’作为默认值，但MySQL不允许，你可以使用INSERT触发器来在插入新行时设置默认值。

```
CREATE TABLE example (
id INT PRIMARY KEY,
created_at DATETIME DEFAULT '0000-00-00 00:00:00'
);

CREATE TRIGGER before_insert_example
BEFORE INSERT ON example
FOR EACH ROW
BEGIN
IF NEW.created_at = '0000-00-00 00:00:00' THEN
SET NEW.created_at = NOW();
END IF;
END;
```

请注意，在任何情况下，你都需要确保你的应用程序或数据库操作能够处理’0000-00-00 00:00:00’作为有效的日期时间值，因为它在MySQL中是一个特殊的标记。如果你的应用程序或者框架不支持这个值，你可能需要进行一些额外的处理。

只需要修改[mysqld] sql\_mode=NO\_ENGINE\_SUBSTITUTION 配置，重启服务就可以了。😔白折腾半天，不过好处是用上么mysql8了。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《MySQL datetime default 0000-00-00 00:00:00❤》](https://h4ck.org.cn/2024/05/16942)
\* 本文链接：<https://h4ck.org.cn/2024/05/16942>
\* 短链接：<https://oba.by/?p=16942>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Mysql](https://h4ck.org.cn/tags/mysql)

[Previous Post](https://h4ck.org.cn/2024/05/16947)
[Next Post](https://h4ck.org.cn/2024/05/16937)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2024年12月18日

#### [四谈自建Gravatar镜像](https://h4ck.org.cn/2024/12/18819)

2023年11月17日

#### [退路](https://h4ck.org.cn/2023/11/14296)

2012年12月21日

#### [也谈《Linux脚本自动备份网站数据到Dropbox》](https://h4ck.org.cn/2012/12/4867)

### 20 comments

1. ![](https://gg.lang.bi/avatar/06d172713b38d1b1966d9595ff105e0e4b2bc4cb2abfe412c6d1bf62b80dcf32?s=64&d=identicon&r=r) **[老狼](https://itlu.net)**说道：

   [2024年5月10日 21:29](https://h4ck.org.cn/2024/05/16942#comment-115058)

   ![Level 5](https://badgen.net/badge/亲密度/Level 5/orange?icon=codebeat)

   ![Microsoft Edge 120](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 120") Microsoft Edge 120 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   新版本要求更严格，跟PHP一样，很多在就版本没问题的函数，在新版本直接warning

   [回复](#comment-115058)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年5月10日 21:41](https://h4ck.org.cn/2024/05/16942#comment-115059)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 120](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 120") Google Chrome 120 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      这个默认值旧版本也会报错，所以才升级的。现在看来不是版本问题。

      [回复](#comment-115059)
2. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r)

   [2024年5月10日 21:46](https://h4ck.org.cn/2024/05/16942#comment-115060)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Safari 17](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/safari.png "Safari 17") Safari 17 ![iPhone iOS 17.4.1](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/iphone.png "iPhone iOS 17.4.1") iPhone iOS 17.4.1 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   所以我用 int 不用 datetime

   [回复](#comment-115060)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年5月10日 21:58](https://h4ck.org.cn/2024/05/16942#comment-115061)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 124](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 124") Google Chrome 124 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      机智如你，🥰

      [回复](#comment-115061)
   2. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年5月10日 21:59](https://h4ck.org.cn/2024/05/16942#comment-115062)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 124](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 124") Google Chrome 124 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      顺便把字符集的问题也解决啦 之前有的emoji存储🈶问题

      [回复](#comment-115062)

      1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r)

         [2024年5月10日 22:12](https://h4ck.org.cn/2024/05/16942#comment-115063)

         ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

         ![Safari 17](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/safari.png "Safari 17") Safari 17 ![iPhone iOS 17.4.1](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/iphone.png "iPhone iOS 17.4.1")...