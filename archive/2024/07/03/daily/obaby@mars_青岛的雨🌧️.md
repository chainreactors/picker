---
title: 青岛的雨🌧️
url: https://h4ck.org.cn/2024/07/17431
source: obaby@mars
date: 2024-07-03
fetch_date: 2025-10-06T17:41:37.143850
---

# 青岛的雨🌧️

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

# 青岛的雨🌧️

2024年7月2日
[67 条评论](https://h4ck.org.cn/2024/07/17431#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/07/9191719898963_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/9191719898963_.pic_.jpg)

虽然北方没有梅雨季节，这几天接连的阴雨似乎也昭示着雨季来临了。这里不是非洲的大草原，自然没有那广阔的草原和奔袭的野兽。只有那肆虐的狂风和冷冷的冰雨。

周六回县城的时候，路上就在淅淅沥沥的下着雨。时大时小，忽及忽慢。早上刚睁开眼，隔着窗户的三层玻璃，隐约能听到大雨打在玻璃上的声音。真的又开始下雨了。

青岛的雨从来都不会独来独往，每次必然都有强风作伴，这一对总是能制造不小的麻烦。

[![](https://h4ck.org.cn/wp-content/uploads/2024/07/9171719898929_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/9171719898929_.pic_.jpg)

早上到公司楼下的时候，路上的积水已经有五六公分了。强风裹挟着大雨点横着下，时不时的改变方向，不管雨伞朝着那个方向，总也躲不过大雨的偷袭，从下半身到上半身无一幸免。狂风吹着路上的积水竟然出现了层层的波浪，这下真的无路可逃了。

[<https://h4ck.org.cn/wp-content/uploads/2024/07/437_1719899080.mp4>](https://h4ck.org.cn/wp-content/uploads/2024/07/437_1719899080.mp4?_=1)

这几天精力又陷入了一个比较困顿的状态，到了晚上十一点左右就特别的困了。也没什么精力再熬一会儿。最近一直在想着将[闺蜜圈app](https://guimiquan.cn)从 vue2 迁移到 vue3 上来，上周的时候找了一晚上时间，尝试修改了一部分代码。主要是语法问题，以及系统架构变化导致的兼容性问题。css 的 deep，export import 等等。但是，上周折腾完之后虽然能跑起来了，但是页面一堆的问题，加载直接出错了。

昨天晚上又拿出来两个小时，重新进行了代码的优化。

[![](https://h4ck.org.cn/wp-content/uploads/2024/07/Jietu20240702-103529-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/Jietu20240702-103529.jpg)

经过这次折腾，终于页面重新跑起来了。然而，网络请求的兼容性还需要进一步处理。

之所以要进行项目升级，主要是针对所谓的鸿蒙 next 的兼容性。之前看 uni 官方的通告，vue2 版本很可能是不会进行鸿蒙 next 的兼容性适配的，也就是说要想打包鸿蒙 next 的应用至少需要 vue3。[早上又看了篇文章](https://mp.weixin.qq.com/s/oGR4FTvP0F_s9F7MBMPjcQ)，说了针对鸿蒙 next 的适配方案。

虽然提到了方案一：

>   方案一，是对存量uni-app项目的开发者非常友好的webview方案，这套架构是业内主流的Hybrid App架构，即逻辑层、视图层分离架构。老版uni-app在App平台使用的是这套架构，微信等各家小程序使用的也是这套架构。使用本方案，可以帮助开发者快速将之前基于uni-app开发的App、小程序、H5等，快速发布成鸿蒙App，快速入驻鸿蒙生态，抢先接收鸿蒙的流量红利。

这个可能也仅限于 vue3 的项目，未雨绸缪，所以提前尝试了一下，将 vue2 的项目升级到了 vue3。升级过程中各种语法以及框架变化还是蛮明显的，其中有一段 vue2 的代码，尝试让现在的各种 ai 升级成 vue3 版本。实际效果并不理想，尤其是所谓的那几个国产的。

**baidu comate,没有重新写代码，直接告诉我怎么写怎么引用：**

[![](https://h4ck.org.cn/wp-content/uploads/2024/07/Jietu20240702-104249.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/Jietu20240702-104249.jpg)

嗯，整体来说就是没啥用

**deepseek 直接将我的代码复制到了一份，然后啥也没说：**

[![](https://h4ck.org.cn/wp-content/uploads/2024/07/Jietu20240702-104349-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/Jietu20240702-104349.jpg)

**最靠谱的还是gpt，duckduckgo有免费的 gpt 3.5 turbo，这个还是蛮不错的：**

[![](https://h4ck.org.cn/wp-content/uploads/2024/07/Jietu20240702-104714-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/Jietu20240702-104714.jpg)

最起码他是真的给我转了，并且转的代码也没问题，完全可用。

窗外雨还在继续，不过现在感觉小了很多了。恼人之处在于，现在身上的衣服全部都是湿的，感觉非常不舒服，只能中午回去换衣服了。

[![](https://h4ck.org.cn/wp-content/uploads/2024/07/9181719898946_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/07/9181719898946_.pic_.jpg)

中午顶着瓢泼大雨回到家，家里也没什么能吃的东西。煮了一包泡面，把周日打包回来的剩菜热了一下。将就吃点东西，这些其实倒是也没那么关键。主要是能换身干净的衣服就行啦，吃完饭雨竟然停了，有的地方甚至有斑驳的阳光晒了下来。出门之后发现，早上宜人的温度已经荡然无存，偶尔从乌云后面的太阳偷偷摸摸的出来照射一下雨后的大地，瞬间空气的湿度就上来了。

肆虐的狂风也不见了踪迹，只剩下蒸笼一样的空气。如果说北方多数地区的夏天是烤箱，那么青岛的雨后就是个蒸笼。雾气氤氲，黏黏糊糊。汗水就顺着脸颊流了下来，在户外不多久衣服也就贴在了身上。嗯，当个大包子，感觉的确不怎么样。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《青岛的雨🌧️》](https://h4ck.org.cn/2024/07/17431)
\* 本文链接：<https://h4ck.org.cn/2024/07/17431>
\* 短链接：<https://oba.by/?p=17431>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[下雨](https://h4ck.org.cn/tags/%E4%B8%8B%E9%9B%A8)[落大雨](https://h4ck.org.cn/tags/%E8%90%BD%E5%A4%A7%E9%9B%A8)[雨天](https://h4ck.org.cn/tags/%E9%9B%A8%E5%A4%A9)

[Previous Post](https://h4ck.org.cn/2024/07/17447)
[Next Post](https://h4ck.org.cn/2024/07/17413)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2024年12月12日

#### [天生冤种？](https://h4ck.org.cn/2024/12/18769)

2025年5月11日

#### [FaceFusion 3.2.0 — 进阶体验（不要瑟瑟）](https://h4ck.org.cn/2025/05/20664)

2025年9月1日

#### [戛然而止](https://h4ck.org.cn/2025/09/21441)

### 67 comments

1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r) **[dujun](https://dujun.io)**说道：

   [2024年7月2日 13:57](https://h4ck.org.cn/2024/07/17431#comment-116837)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Safari 17](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/safari.png "Safari 17") Safari 17 ![iPhone iOS 17.4.1](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/iphone.png "iPhone iOS 17.4.1") iPhone iOS 17.4.1 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   vue3 和 vue2 是两个东西

   [回复](#comment-116837)

   1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r)

      [2024年7月2日 13:57](https://h4ck.org.cn/2024/07/17431#comment-116838)

      ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

      ![Safari 17](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/safari.png "Safari 17") Safari 17 ![iPhone iOS 17.4.1](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/iphone.png "iPhone iOS 17.4.1") iPhone iOS 17.4.1 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      仿佛

      [回复](#comment-116838)

      1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

         [2024年7月2日 13:59](https://h4ck.org.cn/2024/07/17431#comment-116839)

         ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

         ![Google Chrome 118](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 118") Google Chrome 118 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

         这俩字就多余，哈哈哈。就是两个东西。

         [回复](#comment-116839)

         1. ![](https://gg.lang.bi/avatar/ae3986ad90cef2c73e4d7f9dccdc5fab569b4912378cc60b6b43fdf8f32d1596?s=64&d=identicon&r=r)

            [2024年7月2日 14:05](https://h4ck.org.cn/2024/07/17431#comment-116840)

            ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

            ![Google Chrome 86](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 86") Google Chrome 86 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

            ![laugh](https://h4ck.org.cn/wp-content/plugins/kama-wp-smile/packs/qip/laugh.gif)

            [回复](#comment-116840)
2. ![](https://gg.lang.bi/avatar/44c40589887c2a6c75aab996bc0a381fa3e3f60b1...