---
title: 🦞龙虾初体验
url: https://zhongxiaojie.cn/2026/03/610/
source: obaby 𝐢‍𝐧⃝ void
date: 2026-03-19
fetch_date: 2026-03-20T04:07:16.480644
---

# 🦞龙虾初体验

[![obaby 𝐢‍𝐧⃝ void](https://zhongxiaojie.cn/wp-content/uploads/2026/01/new-logo-27.png)](https://zhongxiaojie.cn)

程序媛 / 独立开发者 / 智商不稳定的女神经

* [❈闺蜜圈|Pink Daily❈](https://zhongxiaojie.cn/pinkdaily/)
* [❈说说|Tweet❈](https://zhongxiaojie.cn/tweet/)
* [❈留言|Talk❈](https://zhongxiaojie.cn/talk/)
* [❈集美们|Besties❈](https://zhongxiaojie.cn/besties/)
* [❈关于|About❈](https://zhongxiaojie.cn/about/)

 [Menu](#mobilemenu)

* [❈闺蜜圈|Pink Daily❈](https://zhongxiaojie.cn/pinkdaily/)
* [❈说说|Tweet❈](https://zhongxiaojie.cn/tweet/)
* [❈留言|Talk❈](https://zhongxiaojie.cn/talk/)
* [❈集美们|Besties❈](https://zhongxiaojie.cn/besties/)
* [❈关于|About❈](https://zhongxiaojie.cn/about/)

[程序媛](https://zhongxiaojie.cn/category/code-girl/)

# 🦞龙虾初体验

2026年3月19日 16:04
[49 条评论](https://zhongxiaojie.cn/2026/03/610/#comments)

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/03/微信图片_20260319160339_607_42-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/03/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20260319160339_607_42.jpg)

龙虾刚出来的时候，我无动于衷；龙虾爆火的时候，我依然无动于衷；龙虾开始被卸载的时候，我终于不再无动于衷了。

从春节的时候，龙虾忽然就开始变得热度极高。几乎所有人都在讨论龙虾，以及养虾的话题。这儿东西最开始的时候，给我的感觉就是，如果本地没有足够多的资源，龙虾就发挥不出自己的作用；如果直接用自己的电脑去安装，又会出现龙虾权限过高的问题。

龙虾做得事情，可能在我的预期范围之外。单纯为龙虾创建一个沙盒环境，意义感觉也不是很大。如果一个问题需要解决两遍，那感觉和不解决似乎也没太多的区别。

尽管如此，龙虾的热度还是越来越高，一度出现各种上门安装的服务。

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Cache_6eb8d89b71548277.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Cache_6eb8d89b71548277.jpg) [![](https://zhongxiaojie.cn/wp-content/uploads/2026/03/D432B90692D8225449D29A6E17F4C40F.png)](https://zhongxiaojie.cn/wp-content/uploads/2026/03/D432B90692D8225449D29A6E17F4C40F.png)

再后来出现线了，各种收费卸载的服务。果然是此一时，彼一时，三十年河东三十年河西。

然而，在这滚滚的卸载浪潮中，我逆流而上，反其道而行之，我安装龙虾了。

不得不多，openclaw基于node的服务还是蛮笨重的，安装的确有点麻烦，刚开始为了省事，直接百度云买了个所谓的9.9的open claw实例，然而订阅coding plan的时候发现根本抢不到。

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-152751-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-152751.jpg)

使用按量付费之后，简单尝试了以下，发现效果还是可以的，不过就是太费token了。千帆大模型感觉体验也还ok。

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-152926-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-152926.jpg)

可以理解你的意图，也能正常的推进任务。然而，不能订阅，这个长期跑费用是个问题。

于是再次尝试别的方式，直接腾讯清凉弄了台99的服务器，干净安装openclaw，模型选择参考的[杜郎](https://dujun.io/28c43a95-478f-5e2a-8805-510244c99494.html)的文章里提到的[nvidia nim](https://build.nvidia.com/z-ai/glm5)。好处是免费，当然，速率还是有限制的。

昨天的时候，第一次玩这个东西没啥经验，还是用的kimi，后来尝试minimax，但是效果怎么说呢，不知道是配置问题还是啥问题，总是不尽如意。

再后来看到了zero claw，号称体积更小，占用资源更少。直接二进制安装，下载之后启动：

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-153609-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-153609.jpg)

至于怎么在公网访问，直接使用nginx反代即可，参考： <https://cnb.cool/oba.by/baby-claw>

这次直接用glm5，配置好之后，整体体验感觉有些差，就是非常智障的感jio。

[<https://zhongxiaojie.cn/wp-content/uploads/2026/03/2.mp4>](https://zhongxiaojie.cn/wp-content/uploads/2026/03/2.mp4?_=1)

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-134616.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-134616.jpg) [![](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-134641.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-134641.jpg)

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-154946.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-154946.jpg)

假装执行，这种处理逻辑真是可以，如果我不知道文章分类都有啥，差点就信了。在这种状况下不得不再切回openclaw。鉴于昨天的配置问题，今天reset之后，尝试重新配置运行，依然用与zero claw同样的glm5，这次相对来说还是比较顺利的。

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-154756-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-154756.jpg) [![](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-154824-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-154824.jpg)

与之前zero claw的对比就会发现了，这次好歹是真的获取到相关的分类了，而不是假装执行。

所以，有的时候虽然都说自己很厉害，但是不对比永远都不知道谁更厉害。很多东西不是单纯说说就可以的，当然zero的优势在于部署方便，占用资源更低，但是作为一个agent，实际的效果并没有赶上open claw。

所以，现在各种龙虾层出不穷，如果不知道选择哪一只，建议还是选择原版，open claw，虽然安装费劲点。但是相对来说，没那么弱智（在同样的模型glm5下）。

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-155734-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-155734.jpg)

上图为三小时token消耗量。

微信公众号文章，自动发布wp效果：

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-160036-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/03/Jietu20260319-160036.jpg)

相关资源：

<https://cnb.cool/oba.by/baby-claw>

<https://dujun.io/28c43a95-478f-5e2a-8805-510244c99494.html>

<https://build.nvidia.com/z-ai/glm5>

<https://q.qq.com/qqbot/openclaw/index.html>

---

[![闺蜜圈APP](/support/guimiquan-ads2.jpg)](https://guimiquan.cn "闺蜜圈APP")

**博客：** [obaby 𝐢‍𝐧⃝ void](https://zhongxiaojie.cn/)

**地址：** <https://zhongxiaojie.cn/>

**文章：** [《🦞龙虾初体验》](https://zhongxiaojie.cn/2026/03/610/)

[open claw](https://zhongxiaojie.cn/tag/open-claw/)[zero claw](https://zhongxiaojie.cn/tag/zero-claw/)[养虾](https://zhongxiaojie.cn/tag/%E5%85%BB%E8%99%BE/)[龙虾](https://zhongxiaojie.cn/tag/%E9%BE%99%E8%99%BE/)

[Previous Post](https://zhongxiaojie.cn/2026/03/654/)
[Next Post](https://zhongxiaojie.cn/2026/03/602/)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=initials&r=pg&initials=ob)

#### obaby

独立 APP 开发者
偶尔写点东西
希望与过往一刀两断

#### You may also like

2026年1月22日 09:27

#### [卡巴斯基引发的网络异常](https://zhongxiaojie.cn/2026/01/208/)

2026年2月9日 09:06

#### [WP RSS.Beauty 插件](https://zhongxiaojie.cn/2026/02/416/)

2026年1月16日 14:08

#### [PHP 8 探针 粉萌版](https://zhongxiaojie.cn/2026/01/79/)

### 49 comments

1. ![](https://gg.lang.bi/avatar/35f5b036116cd9e4772887e32f5505296b5286160160fc3bbfd6263465f856c4?s=64&d=initials&r=pg&initials=%E8%80%81%E4%BD%95) **[老何](https://www.mrhe.net)**说道：

   [2026年3月19日 4:44 下午](https://zhongxiaojie.cn/2026/03/610/#comment-1595)

   ![Level 2](https://badgen.h4ck.org.cn/badge/亲密度/Level 2/cyan?icon=codebeat)

   ![Google Chrome 134.0.0.0](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 134.0.0.0") Google Chrome 134.0.0.0 ![Windows 10 x64 Edition](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10 x64 Edition") Windows 10 x64 Edition ![cn](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   看来你已经会安装了，体验结束后，要不要提供上门卸载服务？ ![smile](https://zhongxiaojie.cn/wp-content/plugins/kama-wp-smile-packs/qip_dark_all/smile.gif)

   [回复](#comment-1595)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=initials&r=pg&initials=ob) **[obaby](https://zhongxiaojie.cn)**说道：

      [2026年3月19日 5:07 下午](https://zhongxiaojie.cn/2026/03/610/#comment-1599)

      ![公主](https://badgen.h4ck.org.cn/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.h4ck.org.cn/badge/角色/女王/red?icon=matrix) ![Queen](https://badgen.h4ck.org.cn/badge/精神状态/恬静/pink?icon=codebeat)

      ![Google Chrome 142.0.0.0](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 142.0.0.0") Google Chrome 142.0.0.0 ![Mac OS X  10.15.7](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X  10.15.7") Mac OS X 10.15.7 ![cn](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      目前还不需要卸载呢，gege

      [回复](#comment-1599)
   2. ![](https://gg.lang.bi/avatar/133bc875734b0ed88b899d5c707257cb9e7eced66b6593f37dca50942cd856c1?s=64&d=initials&r=pg&initials=%E5%A4%8F%E6%9C%AB)

      [2026年3月19日 6:54 下午](https://zhongxiaojie.cn/2026/03/610/#comment-1606)

      ![Level 1](https://badgen.h4ck.org.cn/badge/亲密度/Level 1/gray?icon=codebeat)

      ![IBrowse r](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/ibrowse.png "IBrowse r") IBrowse r ![Android 16](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/1...