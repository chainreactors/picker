---
title: “京喜”，什么他妈的叫惊喜！？
url: https://h4ck.org.cn/2025/08/21427
source: obaby@mars
date: 2025-08-28
fetch_date: 2025-10-07T00:47:46.839224
---

# “京喜”，什么他妈的叫惊喜！？

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

# “京喜”，什么他妈的叫惊喜！？

2025年8月27日
[103 条评论](https://h4ck.org.cn/2025/08/21427#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/微信图片_20250827095521_74.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250827095521_74.jpg)

树莓派的系统又双叒叕挂了，还是文件损坏导致的。更深层次的原因，肯定还是内存卡的问题。

原来的卡格式化之后，从写写入 image 似乎也能启动，但是想再次备份文件出来就会失败了。也就没办法去创建一个最新系统的镜像，这就很蛋疼，找了下之前的内存卡，发现只有 16g 的，然而，镜像是直接用 win32diskimage 创建的 32g 的镜像。

去二手东看了下内存卡，有些是真便宜啊。十几块钱 32g，而之前买这些内存卡的时候，还是 99 快 32g。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/微信图片_20250827093231_72-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250827093231_72.jpg)

注意那几个大字 **“足量不虚标”**，其实，这个东西，别的我还真没注意到，就看到这个东西了。想着既然不虚标，那应该是 ok 的。

并且这个东西还不是所谓的次日达，发货之后就开始了漫长的等待。终于昨天下午到了，然而，下午还要加班，等到七点半之后终于下班了。

然而，并不想开车回去，回去找车位也麻烦。所以，那就不如干脆跑回去。之前也跑过几次，距离也不是很远。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/微信图片_20250827093231_69.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250827093231_69.jpg)

到家之后把内存卡查到读卡器上，开始写输入，在写入的时候直接懵逼了：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-26-214607.png)](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-26-214607.png)

32g 的镜像，往 32g 的内存卡写，提示我空间不足，这尼玛是什么神奇的逻辑？说好的足量不虚标呢？

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-28-074711.png)](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-28-074711.png)

强行写入之后，启动就直接卡住了，跟损坏的内存卡是完全一样的。对比下大牌的内存卡容量就会发现少了很多，连 30都不到实际是连 29 都不到，上图是所谓的京喜：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-26-214811-scaled.png)](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-26-214811.png) [![](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-26-214915-scaled.png)](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-26-214915.png)

属性对比，上图是所谓的京喜：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-26-214753.png)](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-26-214753.png) [![](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-26-214942.png)](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-26-214942.png)

所谓的足量不虚标自然就是瞎扯。当然，至于说的直接可以查到摄像头上用更是无稽之谈：

插上去之后，最开始不识别，后来识别了格式化失败：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/微信图片_20250827093231_71-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250827093231_71.jpg)

让我一度以为 360 已经不要脸到识别内存卡品牌了，只识别 360 的内存卡。

然而，原来摄像头用的也不是 360 的内存卡啊，拿出来之后写入镜像是完全没问题的，也不会提示错误：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-26-215208.png)](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-26-215208.png)

同样的容量，同样的镜像，本质上还是新买的内存卡有问题。这个内存卡是从摄像头拿出来的，想着既然容量不足，那用来存视频应该没问题，事实证明，也不行，直接格式化都格式化不了，至于直接用，貌似也用不了。这个就不知道是什么逻辑了。

最后找了个 16g 的内存卡先给塞到了摄像头里，算是临时解决了这个问题。

不同品牌内存卡对比：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/微信图片_20250827093231_70.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250827093231_70.jpg)

不管是 sandisk 还是金士顿的，都没有所谓的写入失败的问题，黑色的 tf 卡是原来树莓派用的。

至于这个 pro plus 是什么品牌，干嘛不写呢？

还京喜？

“京喜”，什么他妈的叫惊喜！？

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《“京喜”，什么他妈的叫惊喜！？》](https://h4ck.org.cn/2025/08/21427)
\* 本文链接：<https://h4ck.org.cn/2025/08/21427>
\* 短链接：<https://oba.by/?p=21427>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[tf 卡](https://h4ck.org.cn/tags/tf-%E5%8D%A1)[内存卡](https://h4ck.org.cn/tags/%E5%86%85%E5%AD%98%E5%8D%A1)[树莓派](https://h4ck.org.cn/tags/%E6%A0%91%E8%8E%93%E6%B4%BE)

[Previous Post](https://h4ck.org.cn/2025/09/21441)
[Next Post](https://h4ck.org.cn/2025/08/21408)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年10月6日

#### [拖车记–大白漏油啦？](https://h4ck.org.cn/2023/10/13686)

2025年4月28日

#### [一劳永逸？](https://h4ck.org.cn/2025/04/20308)

2010年2月9日

#### [360 VS.瑞星](https://h4ck.org.cn/2010/02/1234)

### 103 comments

[« 上一页](https://h4ck.org.cn/2025/08/21427/comment-page-1#comments)
[1](https://h4ck.org.cn/2025/08/21427/comment-page-1#comments)
2

1. ![](https://gg.lang.bi/avatar/d59840a8a260d70cec46fa278b7a983a482211c7f567484469703c4a2894d7a9?s=64&d=identicon&r=r) **[紫慕](https://90zm.net)**说道：

   [2025年8月29日 10:13](https://h4ck.org.cn/2025/08/21427/comment-page-2#comment-128291)

   ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Google Chrome 139](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 139") Google Chrome 139 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   所以最后还是虚标的问题吗？感觉水好深，我相机SD卡直接买了闪迪的。

   [回复](#comment-128291)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年8月29日 10:28](https://h4ck.org.cn/2025/08/21427/comment-page-2#comment-128292)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 134](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 134") Google Chrome 134 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      是的，虚标太严重了。
      大厂的靠谱。

      [回复](#comment-128292)
2. ![](https://gg.lang.bi/avatar/224dcfa27064fc6fbcf00185929f460043af8ae66a6feb8af19a19041bfb6267?s=64&d=identicon&r=r)

   [2025年8月29日 17:44](https://h4ck.org.cn/2025/08/21427/comment-page-2#comment-128299)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![Microsoft Edge 138](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 138") Microsoft Edge 138 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   我同事买这个sd卡，装行车记录仪上，已经坏了3-4个了，每次都是京东买的 0.0

   [回复](#comment-128299)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年8月30日 09:17](https://h4ck.org.cn/2025/08/21427/comment-page-2#comment-128304)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 138](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 138") Google Chrome 138 ![Android ...