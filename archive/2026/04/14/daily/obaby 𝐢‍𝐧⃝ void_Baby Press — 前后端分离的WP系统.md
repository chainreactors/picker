---
title: Baby Press — 前后端分离的WP系统
url: https://zhongxiaojie.cn/2026/04/933/
source: obaby 𝐢‍𝐧⃝ void
date: 2026-04-14
fetch_date: 2026-04-15T04:39:04.678050
---

# Baby Press — 前后端分离的WP系统

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

# Baby Press — 前后端分离的WP系统

2026年4月14日 09:53
[57 条评论](https://zhongxiaojie.cn/2026/04/933/#comments)

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/330A0342-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/330A0342.jpg)

WP的系统怎么说呢，有时候真的感觉一言难尽，庞杂的功能，丰富的插件、主题。几乎能满足所有人的需求，当然，也能满足我的需求。

之所以要做这么个东西，最主要的是前几天在杜老师的聊天室收到一条消息：

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Jietu20260413-153059@2x.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Jietu20260413-153059%402x.jpg)

跟随这条消息我也去了解了一下这个东西，按照官方的说法，其实是这么个东西：

> Cloudflare 将这款项目命名为 **[EmDash](https://zhida.zhihu.com/search?content_id=272537863&content_type=Article&match_order=1&q=EmDash&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzYyMzg0MzQsInEiOiJFbURhc2giLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNzI1Mzc4NjMsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.hbNLrLtb-W2woQtKCaeh8T7iKQUwMCCBhwPN3gNKYjo&zhida_source=entity)**，将其定位为 **WordPress 的精神继承者**，这并不是对 WordPress 简单的复刻，而是**用现代化技术栈，重新实现一套面向未来的 CMS**，并且重点解决了 WordPress 24 年发展中积累的的架构臃肿、安全隐患与性能瓶颈问题。

说是高性能的wp，但是实际上跟wp没有任何的关系，除了所谓的精神继承。刚开始我还以为是基于wp的优化，现在看来其实是完全做了另外一套系统，这**精神继承**，可以说是非常抽象了。

再加上 『爱看』在我没有~~丢失以前的网站数据~~的时候，就一直建议可以自己写个系统。重新搭建之后，他又提过几次：

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/UserslingPictures截图Jietu20260413-151422@2x-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/UserslingPictures%E6%88%AA%E5%9B%BEJietu20260413-151422%402x.jpg)

既然 cf可以这么干，那么自己当然也可以这么干。只是，这次自己既不想重写，又不想使用php，于是，我换了最熟悉的django+vue3来实现这个新的系统，至于数据库当然还是用wp原来的。既然设计好这一切，那么声息的就是让ai开始动工了。

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Jietu20260413-162804@2x-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/Jietu20260413-162804%402x.jpg)

当然在开发过程中，不可避免的要面临一些问题，例如wp的shortcode，主题插件的一些功能：相册、代码高亮等等。不过这些东西都可以重新通过python进行处理和渲染。还有一些php的原生小组件渲染就有些困难了，这些只能通过其他方法进行实现。例如归属地、ua，访客信息等等。暂时尚未完成，为了处理ip归属地查询，目前将插件的归属地查询已经独立成了python服务，开源地址：<https://cnb.cool/oba.by/baby-ip-location>

测试地址：<https://ip.zhongxiaojie.cn>

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/2026-04-13-16.35.48-ip.zhongxiaojie.cn-bd6eded2e665-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/2026-04-13-16.35.48-ip.zhongxiaojie.cn-bd6eded2e665.jpg)

当前测试页面效果：

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/04/2026-04-14-09.51.23-i.zhongxiaojie.cn-7455ee5b34d3.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/04/2026-04-14-09.51.23-i.zhongxiaojie.cn-7455ee5b34d3.jpg)

访问地址：

<https://i.zhongxiaojie.cn>

代码暂未开源，还在继续完善。

---

[![闺蜜圈APP](/support/guimiquan-ads2.jpg)](https://guimiquan.cn "闺蜜圈APP")

**博客：** [obaby 𝐢‍𝐧⃝ void](https://zhongxiaojie.cn/)

**地址：** <https://zhongxiaojie.cn/>

**文章：** [《Baby Press — 前后端分离的WP系统》](https://zhongxiaojie.cn/2026/04/933/)

[AI](https://zhongxiaojie.cn/tag/ai/)[WordPress](https://zhongxiaojie.cn/tag/wordpress/)[WP](https://zhongxiaojie.cn/tag/wp/)[重构](https://zhongxiaojie.cn/tag/%E9%87%8D%E6%9E%84/)

[Next Post](https://zhongxiaojie.cn/2026/04/915/)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=initials&r=pg&initials=ob)

#### obaby

独立 APP 开发者
偶尔写点东西
希望与过往一刀两断

#### You may also like

2026年4月2日 16:46

#### [下载微信公众号的视频](https://zhongxiaojie.cn/2026/04/778/)

2026年1月22日 09:27

#### [卡巴斯基引发的网络异常](https://zhongxiaojie.cn/2026/01/208/)

2026年3月24日 08:58

#### [野心家](https://zhongxiaojie.cn/2026/03/667/)

### 57 comments

1. ![](https://gg.lang.bi/avatar/0fe0fdba49c108bc6f6ace52de075553d7768f4eb7d694adf8e495a0c6192531?s=64&d=initials&r=pg&initials=J.) **[J.sky](https://suiyan.cc/)**说道：

   [2026年4月14日 10:31 上午](https://zhongxiaojie.cn/2026/04/933/#comment-2620)

   ![](https://badgen.h4ck.org.cn/badge/友链/集美们/blue?icon=chrome) ![Level 4](https://badgen.h4ck.org.cn/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Google Chrome 147.0.0.0](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 147.0.0.0") Google Chrome 147.0.0.0 ![GNU/Linux x64](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/os/linux.png "GNU/Linux x64") GNU/Linux x64 ![cn](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   沙发，然后再看。

   [回复](#comment-2620)
2. ![](https://gg.lang.bi/avatar/0fe0fdba49c108bc6f6ace52de075553d7768f4eb7d694adf8e495a0c6192531?s=64&d=initials&r=pg&initials=J.)

   [2026年4月14日 10:37 上午](https://zhongxiaojie.cn/2026/04/933/#comment-2621)

   ![](https://badgen.h4ck.org.cn/badge/友链/集美们/blue?icon=chrome) ![Level 4](https://badgen.h4ck.org.cn/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Google Chrome 147.0.0.0](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 147.0.0.0") Google Chrome 147.0.0.0 ![GNU/Linux x64](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/os/linux.png "GNU/Linux x64") GNU/Linux x64 ![cn](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   现在博客系统遍地开花，可选的太多了，既然今天换了这套系统，明天还会喜欢上另一个，用不了多久，所有的程序都有两种可能，要么被Rust重构，要么被智能体取代。

   [回复](#comment-2621)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=initials&r=pg&initials=ob)

      [2026年4月14日 1:39 下午](https://zhongxiaojie.cn/2026/04/933/#comment-2636)

      ![](https://badgen.h4ck.org.cn/badge/友链/集美们/blue?icon=chrome) ![公主](https://badgen.h4ck.org.cn/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.h4ck.org.cn/badge/角色/女王/red?icon=matrix) ![Queen](https://badgen.h4ck.org.cn/badge/精神状态/恬静/pink?icon=codebeat)

      ![Google Chrome 146.0.0.0](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 146.0.0.0") Google Chrome 146.0.0.0 ![Mac OS X  10.15.7](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X  10.15.7") Mac OS X 10.15.7 ![cn](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      智能体替代不了博客，毕竟不是一样的东西。
      活人味的东西，会越来越少的。但是不会消失。

      [回复](#comment-2636)
3. ![](https://gg.lang.bi/avatar/0b3b8cb95165c8e438337c47068ca52924eb8c720204352f7173082960b42c74?s=64&d=initials&r=pg&initials=%E8%8A%B1%E9%9D%9E)

   [2026年4月14日 10:58 上午](https://zhongxiaojie.cn/2026/04/933/#comment-2622)

   ![Level 4](https://badgen.h4ck.org.cn/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Google Chrome 147.0.0.0](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 147.0.0.0") Google Chrome 147.0.0.0 ![Windows 11 x64 Edition](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11 x64 Edition") Windows 11 x64 Edition ![cn](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   其他不知道，访问速度还是挺快的

   [回复](#comment-2622)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=initials&r=pg&initials=ob)

      [2026年4月14日 1:39 下午](https://zhongxiaojie.cn/2026/04/933/#comment-2637)

      ![](https://badgen.h4ck.org.cn/badge/友链/集美们/blue?icon=chrome) ![公主](https://badgen.h4ck.org.cn/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.h4ck.org.cn/badge/角色/女王/red?icon=ma...