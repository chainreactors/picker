---
title: PyCharm 代码自动补全插件体验
url: https://h4ck.org.cn/2022/11/pycharm-%e4%bb%a3%e7%a0%81%e8%87%aa%e5%8a%a8%e8%a1%a5%e5%85%a8%e6%8f%92%e4%bb%b6/
source: obaby@mars
date: 2022-11-24
fetch_date: 2025-10-03T23:37:08.654517
---

# PyCharm 代码自动补全插件体验

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

[微软『Windows』](https://h4ck.org.cn/cats/xtxg/wrxt)

# PyCharm 代码自动补全插件体验

2022年11月23日
[5 条评论](https://h4ck.org.cn/2022/11/10743#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/10/108a170cf25538ea5bd667600043cb50-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/10/108a170cf25538ea5bd667600043cb50-scaled.jpg)

代码自动补全这个功能还是比较需要的，尤其是大项目。在其他模块内定义的数据类型，如果没有代码自动补全写起来太麻烦了。比如django的model中定义的属性，写查询filter的时候，没有代码自动完成，就需要去找各个属性，更恶心的是外键的关联查询直接没有\_\_补全的功能，就得去找对应关系。数据结构复杂了之后这个工作就变成了灾难。

目前使用过的主要有下面几个：

1.kite

Kite 是一家成立于 2014 年的创业公司，主要从事于开发同名的人工智能编程助手，就类似于大家熟悉的 GitHub Copilot。Kite 最初仅支持 Python 和 JavaScript 这两种编程语言，在 2020 年年底，Kite 额外支持了 TypeScript、Java、Go、C、C#、Kotlin 等编程语言，支持的编程语言一下上升到 13 种。Kite 还支持 16 种编辑器 / IDE，其中包括 VS Code、IntelliJ、Vim、Sublime Text 等，在这一点上支持的范围要高于 GitHub Copilot。

[![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/v2-afc6b56c6ffc4c2de3b6188046cf98f2_1440w.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2022/11/v2-afc6b56c6ffc4c2de3b6188046cf98f2_1440w.jpg)

目前已经停止开发了，因为这个我还写了一篇文章：<https://h4ck.org.cn/2022/10/kite-for-pycharm2022/>

如今 Kite 的大部分代码已经在 Github 开源，其中包括数据驱动的 Python 类型推理引擎、Python 公共包分析器、桌面软件、适配各种编辑器的插件、Github 爬虫和分析器等。

项目地址：[https://github.com/kiteco](https://link.zhihu.com/?target=https%3A//github.com/kiteco)

但是在实际的使用过程中有时候会出现一直在warming up状态。所以我又尝试了其他的代码自动补全插件。

2.AiXcoder

[aiXcoder](https://www.aixcoder.com/#/)致力于将人工智能技术应用于软件开发领域，帮助开发者快速、高效地完成软件开发任务。aiXcoder智能编程工具，能够在开发者编写代码时，自动推荐后续的代码片段，以提高编码效率和代码质量。

aiXcoder代码生成与补全提供以下服务：

* Token级代码生成与补全：基于本地服务，支持自动推荐单个或多个Token的代码
* 行级代码生成与补全：基于云端服务，支持自动生成或补全整行代码
* 方法级代码生成与补全：基于云端服务，支持根据自然语言功能描述以及上下文，生成或补全方法级代码

当前aiXcoder支持Java、Python、C#、C/C++、Go、JavaScript等语言，并支持IntelliJ IDE、PyCharm、Eclipse、VS Code等多种IDE。

实际测试下来，代码补全功能还ok，也确实能自动学习一些新的方法，但是对django的支持一般，也有可能是我使用的方式不对？

[![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/下载.png)](https://image.h4ck.org.cn/wp-content/uploads/2022/11/%E4%B8%8B%E8%BD%BD.png)

3.Tabnine

[Tabnine](https://www.tabnine.com/install/pycharm) is an AI code assistant that makes you a better developer. Tabnine will increase your development velocity with real-time code completions in all the most popular coding languages and IDEs.
Whether you call it IntelliSense, intelliCode, autocomplete, AI-assisted code completion, AI-powered code completion, AI copilot, AI code snippets, code suggestion, code prediction, code hinting, or content assist, using Tabnine can massively impact your coding velocity, significantly cutting down your coding time.

[![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/blog_image_36.png)](https://image.h4ck.org.cn/wp-content/uploads/2022/11/blog_image_36.png)

这几个整体用来下对django的支持性都不怎么好，不知道大家都用什么插件，欢迎推荐。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《PyCharm 代码自动补全插件体验》](https://h4ck.org.cn/2022/11/10743)
\* 本文链接：<https://h4ck.org.cn/2022/11/10743>
\* 短链接：<https://oba.by/?p=10743>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[aixcoder](https://h4ck.org.cn/tags/aixcoder)[Kite](https://h4ck.org.cn/tags/kite)[Pycharm](https://h4ck.org.cn/tags/pycharm)[Tabnine](https://h4ck.org.cn/tags/tabnine)

[Previous Post](https://h4ck.org.cn/2022/11/10750)
[Next Post](https://h4ck.org.cn/2022/11/10735)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年11月20日

#### [Java agent: ja-netfilter](https://h4ck.org.cn/2023/11/14557)

2009年12月24日

#### [漂亮的冬季圣诞节主题桌面壁纸下载](https://h4ck.org.cn/2009/12/932)

2022年7月7日

#### [由电源计划导致的CPU占用率100%](https://h4ck.org.cn/2022/07/10292)

### 5 comments

1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r) **[dujun](https://dujun.io)**说道：

   [2022年11月23日 18:08](https://h4ck.org.cn/2022/11/10743#comment-89265)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Safari 16](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/safari.png "Safari 16") Safari 16 ![iPhone iOS 16.1.1](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/iphone.png "iPhone iOS 16.1.1") iPhone iOS 16.1.1 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   这篇文章是不是发过，因为我记得这张图。

   [回复](#comment-89265)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2022年11月23日 18:54](https://h4ck.org.cn/2022/11/10743#comment-89266)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      哈哈哈，并没有啊，其实是两张很相似的图。既然你看过，那我就直接换上两张吧~~

      [回复](#comment-89266)

      1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r)

         [2022年11月23日 19:08](https://h4ck.org.cn/2022/11/10743#comment-89267)

         ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

         ![Google Chrome 107](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 107") Google Chrome 107 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

         哈哈

         [回复](#comment-89267)
2. ![](https://gg.lang.bi/avatar/1c03767b0691f80231895255661bcf42eceab95dc8b493ee80c835b07f577f49?s=64&d=identicon&r=r)

   [2022年11月25日 00:26](https://h4ck.org.cn/2022/11/10743#comment-89315)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 107](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 107") Microsoft Edge 107 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   有一说一，就是来看图的！

   [回复](#comment-89315)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2022年11月25日 09:09](https://h4ck.org.cn/2022/11/10743#comment-89331)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 10...