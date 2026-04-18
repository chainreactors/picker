---
title: 偷梁换柱 — 解决『出境易暂不支持此应用。』
url: https://zhongxiaojie.cn/2026/04/990/
source: obaby 𝐢‍𝐧⃝ void
date: 2026-04-17
fetch_date: 2026-04-18T04:31:49.882314
---

# 偷梁换柱 — 解决『出境易暂不支持此应用。』

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

# 偷梁换柱 — 解决『出境易暂不支持此应用。』

2026年4月17日 15:30
[33 条评论](https://zhongxiaojie.cn/2026/04/990/#comments)

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/30A4093-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/30A4093.jpg)

前几天去买手机的时候，销售小哥说，如果你不喜欢这个纯血鸿蒙，或者感觉无法满足需求可以回来去二楼，找技术把系统进行降级。

当时我在想：对于我这种买手机不怎么玩游戏或者需求没那么多的人来说，应该能解决我的绝大多数需求，毕竟系统上还有 出境易、卓易通。

然而事情总有例外，自己常用的浏览器vivaldi发现竟然无法安装，这就让人非常的抑郁了。

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/微信图片_20260417151247_32_62-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20260417151247_32_62.jpg)

下载apk安装的时候提示：出境易暂不支持此应用。

哎，咱们可不兴这么搞啊，这就离谱啦。我已我不稳定的智商来猜测这个东西肯定是有个神马白名单或者黑名单机制，至于黑白名单，到时也没那么关键，大不了就改个包名嘛。然而安装 apktool m的时候同样的提示也出现了，这个东西大概率就是黑名单了。

算鸟，算鸟，直接用模拟器改吧：

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/MuMu-20260416-222237-497-scaled.png)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/MuMu-20260416-222237-497.png)

点击快速编辑：

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/MuMu-20260416-222250-659-scaled.png)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/MuMu-20260416-222250-659.png)

原来的包名：com.vivaldi.brower,咱们假装是uc咋样呢：

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/MuMu-20260416-222307-315-scaled.png)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/MuMu-20260416-222307-315.png)

反正我也不用uc浏览器，嘎嘎。

修改之后，发送到手机进行安装，一切顺利，嘻嘻：

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/微信图片_20260417151248_33_62-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20260417151248_33_62.jpg)

**鸿蒙next：我要验牌！牌没有问题！**

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/微信图片_20260417152230_36_62-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20260417152230_36_62.jpg)

尝试同步功能：

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/微信图片_20260417151249_34_62-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20260417151249_34_62.jpg) [![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/微信图片_20260417151250_35_62-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20260417151250_35_62.jpg)

完美！

到这里就结束啦，对于同步问题，有的宝子说非得搭梯子，也不一定。可以直接修改hosts，可以在路由器配置或者dns配置，或者神马别的地方配置：

```
vivaldi.com. 172.66.165.60
bifrost.vivaldi.com. 31.209.137.10
cdn.jsdelivr.net. 151.101.89.229
```

---

[![闺蜜圈APP](/support/guimiquan-ads2.jpg)](https://guimiquan.cn "闺蜜圈APP")

**博客：** [obaby 𝐢‍𝐧⃝ void](https://zhongxiaojie.cn/)

**地址：** <https://zhongxiaojie.cn/>

**文章：** [《偷梁换柱 — 解决『出境易暂不支持此应用。』》](https://zhongxiaojie.cn/2026/04/990/)

[Pure80](https://zhongxiaojie.cn/tag/pure80/)[出境易](https://zhongxiaojie.cn/tag/%E5%87%BA%E5%A2%83%E6%98%93/)[卓易通](https://zhongxiaojie.cn/tag/%E5%8D%93%E6%98%93%E9%80%9A/)[纯血鸿蒙](https://zhongxiaojie.cn/tag/%E7%BA%AF%E8%A1%80%E9%B8%BF%E8%92%99/)[鸿蒙](https://zhongxiaojie.cn/tag/%E9%B8%BF%E8%92%99/)

[Next Post](https://zhongxiaojie.cn/2026/04/955/)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=initials&r=pg&initials=ob)

#### obaby

独立 APP 开发者
偶尔写点东西
希望与过往一刀两断

#### You may also like

2026年3月14日 16:14

#### [开源项目目录📇](https://zhongxiaojie.cn/2026/03/593/)

2026年4月1日 11:18

#### [弱弱的问一下，我的网站怎么被镜像了嗫？](https://zhongxiaojie.cn/2026/04/768/)

2026年2月9日 09:06

#### [WP RSS.Beauty 插件](https://zhongxiaojie.cn/2026/02/416/)

### 33 comments

1. ![](https://gg.lang.bi/avatar/0b3b8cb95165c8e438337c47068ca52924eb8c720204352f7173082960b42c74?s=64&d=initials&r=pg&initials=%E8%8A%B1%E9%9D%9E) **[花非花](https://www.941741.xyz)**说道：

   [2026年4月17日 4:05 下午](https://zhongxiaojie.cn/2026/04/990/#comment-2796)

   ![Level 4](https://badgen.h4ck.org.cn/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Google Chrome 147.0.0.0](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 147.0.0.0") Google Chrome 147.0.0.0 ![Windows 11 x64 Edition](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11 x64 Edition") Windows 11 x64 Edition ![cn](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   从来没用过鸿蒙系统，能解BL锁刷安卓吗？

   [回复](#comment-2796)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=initials&r=pg&initials=ob)

      [2026年4月17日 4:11 下午](https://zhongxiaojie.cn/2026/04/990/#comment-2797)

      ![](https://badgen.h4ck.org.cn/badge/友链/集美们/blue?icon=chrome) ![公主](https://badgen.h4ck.org.cn/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.h4ck.org.cn/badge/角色/女王/red?icon=matrix) ![Queen](https://badgen.h4ck.org.cn/badge/精神状态/恬静/pink?icon=codebeat)

      ![Google Chrome 146.0.0.0](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 146.0.0.0") Google Chrome 146.0.0.0 ![Mac OS X  10.15.7](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X  10.15.7") Mac OS X 10.15.7 ![cn](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      nope，旧的都不行

      [回复](#comment-2797)
2. ![](https://gg.lang.bi/avatar/274c47dce1129c047f40c2782e85bb49e1fdb1521122d29de5d7806618c7ef5a?s=64&d=initials&r=pg&initials=%E6%B0%B4%E6%8B%8D)

   [2026年4月17日 4:11 下午](https://zhongxiaojie.cn/2026/04/990/#comment-2798)

   ![Level 2](https://badgen.h4ck.org.cn/badge/亲密度/Level 2/cyan?icon=codebeat)

   ![Google Chrome 146.0.0.0](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 146.0.0.0") Google Chrome 146.0.0.0 ![Windows 11 x64 Edition](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11 x64 Edition") Windows 11 x64 Edition ![cn](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   达人！

   [回复](#comment-2798)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=initials&r=pg&initials=ob)

      [2026年4月17日 4:13 下午](https://zhongxiaojie.cn/2026/04/990/#comment-2799)

      ![](https://badgen.h4ck.org.cn/badge/友链/集美们/blue?icon=chrome) ![公主](https://badgen.h4ck.org.cn/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.h4ck.org.cn/badge/角色/女王/red?icon=matrix) ![Queen](https://badgen.h4ck.org.cn/badge/精神状态/恬静/pink?icon=codebeat)

      ![Google Chrome 146.0.0.0](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 146.0.0.0") Google Chrome 146.0.0.0 ![Mac OS X  10.15.7](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X  10.15.7") Mac OS X 10.15.7 ![cn](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      主要是这个浏览器用的最多，所有的数据都在上面。换别的实在是代价有点大。

      [回复](#comment-2799)

      1. ![](https://gg.lang.bi/avatar/8a012e16bd9362f5813bc8e7dea51352a5f457dbc97c15599931ba3598920472?s=64&d=initials&r=pg&initials=%E6%A2%A6%E4%B8%8D)

         [2026年4月17日 10:41 下午](https://zhongxiaojie.cn/2026/04/990/#comment-2836)

         ![Level 2](https://badgen.h4ck.org.cn/badge/亲密度/Level 2/cyan?icon=codebeat)

         ![IBrowse r](htt...