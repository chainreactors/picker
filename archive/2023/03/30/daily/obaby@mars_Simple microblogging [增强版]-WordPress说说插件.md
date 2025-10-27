---
title: Simple microblogging [增强版]-WordPress说说插件
url: https://h4ck.org.cn/2023/03/simple-microblogging-%e5%a2%9e%e5%bc%ba%e7%89%88/
source: obaby@mars
date: 2023-03-30
fetch_date: 2025-10-04T11:06:20.626911
---

# Simple microblogging [增强版]-WordPress说说插件

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

# Simple microblogging [增强版]-WordPress说说插件

2023年3月29日
[32 条评论](https://h4ck.org.cn/2023/03/11678#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/ed6f01f2e0da6e5992a57ad70079144a.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/ed6f01f2e0da6e5992a57ad70079144a.jpg)

```
更新记录 0.2
1.优化文章显示
2.增加分页功能
3.替换图标
4.修改菜单名称
```

简介：

```
=== Simple microblogging ===

Contributors: sgcoskey, vgitman, VegetarianZombie,obaby
Donate link: https://boolesrings.org
Tags: tweet, tweets, microblog, microblogging, micropost
Requires at least: 3.0
Tested up to: 6.1.1
Stable tag: 0.1
增强版支持网站：http://oba.by

Add a microblog to your site; display the microposts in a widget or using a shortcode. 增强版优化页面显示，增加分页功能。

== Description ==

This simple plugin allows you to easily post short messages such as thoughts and updates.  These messages will not appear in your stream of posts; instead you can display them in a widget in yours sidebar.  You can also display them in any post or page by using the `[m i c r o b l o g ](使用时去掉空格)` shortcode.

To get started, just look for the new `Microposts` administration panel in your dashboard.  Click `Add new` and then compose a short message in the same way that you normally compose your posts.  If you give the micropost a title, then it will be displayed in bold and used as the first few words of the micropost.

Then, either add the widget to your sidebar or add the `[m i c r o b l o g ](使用时去掉空格)` shortcode into your site, and that's it!

The `[m i c r o b l o g ](使用时去掉空格)` shortcode supports several options:

* **num**: The number of microposts to show.  Defaults to `5`.  Use `-1` to show all microposts.

* **null_text**: If no results are returned, shows this text.  Defaults to `(none)`.

* **show_date**: If defined, the creation date will precede the microposts.

* **date_format**: If showing the date, this php date format will be used.  The default is the Date Format value from the General Settings page.  I recommend `"F j"`, which displays as "May 12".

* **use_excerpt**: If defined, use the post excerpt instead of the entire contents.  We recommend writing short microposts, but if you prefer to write longer ones, this can be used to truncate them.  Unfortunately, WordPress excerpts don't allow links or other html, use the plugin [Advanced Excerpt](http://wordpress.org/extend/plugins/advanced-excerpt/) to remedy this!

* **q**: Arbitrary &-separated arguments to add to the query.  See the [WP_Query](http://codex.wordpress.org/Class_Reference/WP_Query/#Parameters) page for available syntax.  For example, to show only posts from author `sam` in ascending instead of descending order, you would write `[m i c r o b l o g  q="author_name=sam&order=ASC"]`(使用时去掉空格).

The output can then be further formatted using CSS.  We recommend the plugin [Improved Simpler CSS](http://wordpress.org/extend/plugins/imporved-simpler-css/) for quickly styling your post list (and your site)!

Report bugs, give feedback, or fork this plugin on [GitHub](http://github.com/scoskey/Simple-microblogging-wordpress-plugin).

== Installation ==

Nothing unusual here!

== Screenshots ==

1. A rendered widget containing my two microposts
2. The widget configuration box

== Other notes ==

If you are having trouble viewing your microposts, try visiting your permalinks preference pane and clicking `Save changes`.

It is a known issue that some permalink structures do not work with Simple microblogging when the plugin `Salmon for wordpress` is installed.

== Changelog ==
0.2
1.优化文章显示
2.增加分页功能
3.替换图标
4.修改菜单名称

0.1 Added support for authors.  Added use_excerpt option to the shortcode

0.0 initial releasec
```

插件效果：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/Jietu20230328-093407.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/Jietu20230328-093407.jpg)

实例演示：<https://h4ck.org.cn/talk/>

插件下载地址：

温馨提示: 此处隐藏内容需要[发表评论](#respond "发表评论")，并且审核通过后才能查看。
（发表评论请勾选 **在此浏览器中保存我的显示名称、邮箱地址和网站地址，以便下次评论时使用。**）
（请仔细检查自己的昵称和评论内容，以免被识别为垃圾评论而导致无法正常审核。）

代码地址：

温馨提示: 此处隐藏内容需要[发表评论](#respond "发表评论")，并且审核通过后才能查看。
（发表评论请勾选 **在此浏览器中保存我的显示名称、邮箱地址和网站地址，以便下次评论时使用。**）
（请仔细检查自己的昵称和评论内容，以免被识别为垃圾评论而导致无法正常审核。）

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Simple microblogging [增强版]-WordPress说说插件》](https://h4ck.org.cn/2023/03/11678)
\* 本文链接：<https://h4ck.org.cn/2023/03/11678>
\* 短链接：<https://oba.by/?p=11678>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[WordPress](https://h4ck.org.cn/tags/wordpress)[微博](https://h4ck.org.cn/tags/%E5%BE%AE%E5%8D%9A)[微语](https://h4ck.org.cn/tags/%E5%BE%AE%E8%AF%AD)[插件](https://h4ck.org.cn/tags/%E6%8F%92%E4%BB%B6)[说说](https://h4ck.org.cn/tags/%E8%AF%B4%E8%AF%B4)

[Previous Post](https://h4ck.org.cn/2023/03/11695)
[Next Post](https://h4ck.org.cn/2023/03/11659)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年5月3日

#### [给blog添加一个live2d小姐姐](https://h4ck.org.cn/2023/05/11920)

2024年3月11日

#### [再谈评论区亲密度](https://h4ck.org.cn/2024/03/15777)

2024年3月16日

#### [再谈 WordPress 的速度优化 — 优化插件真的是提速的吗？](https://h4ck.org.cn/2024/03/15874)

### 32 comments

1. ![](https://gg.lang.bi/avatar/898a5dc2af6086170c841c729a84c959c7fdc38a0c090e2edc7ebafd0c0ef9c4?s=64&d=identicon&r=r) **[小熊](https://www.saphead.cn/)**说道：

   [2023年3月29日 17:41](https://h4ck.org.cn/2023/03/11678#comment-93937)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Microsoft Edge 111](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 111") Microsoft Edge 111 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   今天有图了，昨晚上是发生了啥大事，云加速崩了吗？

   [回复](#comment-93937)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2023年3月29日 17:44](https://h4ck.org.cn/2023/03/11678#comment-93938)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      嗯呢，百度云加速直接挂了，他们主站都跟着挂了。可能出问题的不仅仅是百度，微信 qq也有登录不了的。
      不知道发生了什么问题，导致整个网络产生了波动。后续百度匀加速的ssl配置全部出错了，直到今天上午我重新部署了才恢复。

      [回复](#comment-93938)

      1. ![](https://gg.lang.bi/avatar/898a5dc2af6086170c841c729a84c959c7fdc38a0c090e2edc7ebafd0c0ef9c4?s=64&d=identicon&r=r)

         [2023年3月29日 17:44](https://h4ck.org.cn/2023/03/...