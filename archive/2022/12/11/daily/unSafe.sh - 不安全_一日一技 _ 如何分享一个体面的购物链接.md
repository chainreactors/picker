---
title: 一日一技 | 如何分享一个体面的购物链接
url: https://buaq.net/go-139455.html
source: unSafe.sh - 不安全
date: 2022-12-11
fetch_date: 2025-10-04T01:10:25.289919
---

# 一日一技 | 如何分享一个体面的购物链接

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/77c79114f6c9c36283124b9ee2b65f63.jpg)

一日一技 | 如何分享一个体面的购物链接

*2022-12-10 14:52:3
Author: [sspai.com(查看原文)](/jump-139455.htm)
阅读量:34
收藏*

---

如果让你「分享一个淘宝链接」，你脑海中首先浮现的格式是什么样的？

如果你经常跟微信好友分享，熟悉的格式也许是这样的：

```
椱ァ製这句话¢Abc123Xyz¢后咑閞👉淘宀┡ē👈
```

如果你习惯淘宝客户端里选择复制链接，也许看到的大多是这样的：

```
https://m.tb.cn/h.A1B2C3D4?tk=1a2b3c4d5A6
```

如果你足够老派，仍然坚持在电脑上访问淘宝，地址栏显示的链接应该类似这样：

```
https://item.taobao.com/item.htm
    ?ut_sk=1.X55/YjLY%2BlADADdx1FfSKE2K_12345678_1234567890123.Copy.1
    &id=123456789012
    &suid=A433CF27-ABCD-1234-DCBA-33D239D70323
    &shareUniqueId=12345678901
    &spm=a2159r.12345678.0.0
    &sp_abtk=gray_1_code_simpleios2
    &tbSocialPopKey=shareItem
    &sp_tk=A12bCdDEFGHiJ3
    &short_name=h.AB1CDE2
    . . .
```

（以上例子为方便阅览已做简化和改写处理，并替换为虚构数据。）

我的一般原则是非必要不用梗，但面对这几种「链接」，我愿意破例一次：在座的各位都是\_\_\_\_\_。

第一种格式的问题在于它根本不是链接，而是淘宝为了躲避微信的屏蔽发明出来的「[火星文](https://www.thepaper.cn/newsDetail_forward_15240007)」、官方起的粉饰名称是「[淘口令](https://open.taobao.com/api.htm?source=search&docId=32461&docType=2)」。第二种虽然看起来比较正经，但仍然是一个「短网址」，性质上是不完整和临时的，访问后会被服务器跳转到一个「完全体」地址——通常就类似于第三种格式。

但第三种格式也不是一个好的网址，它的问题在于废话太多了。复习一下，在 [URL](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL) 中，从问号 `?` 开始，之后每一段形如 `key=value`、中间用 `&` 分开的键值对，都被称为「参数」（parameter）。规范意义上，参数的作用并不是定位网上的资源——那是问号 `?` 之前的路径（path）所做的事——而只是用来向服务器提供显示具体内容的补充信息。

![full URL](https://cdn.sspai.com/2022/12/10/article/7d6ef999559070025e83f1ee8b02a73f?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

而在上面的那段长链接中，绝大多数参数都和商品本身没有任何关系，只是为了推广和追踪目的服务的：有的标记了广告主的身份（以便广告归因和分成）；有的记录了分享者、也就是你本人的身份、设备类型、分享场景；有的用来控制接收者点击后，客户端显示怎样的界面。你以为自己分享的是字字珠玑，实际上却是在隐私地狱里替人推磨。

这不是淘宝一个平台的问题。如今在大多数电商平台，简洁、可读、易懂的链接都已经绝迹了。对此，当然可以选择睁一只眼闭一只眼，复制出来什么链接，就保存和分享什么链接；大多数不了解其中区别的人可能也是这么做的。

但我非常反对接受这样的链接。作为用户，我反对这种在链接里夹带私货的行为；返利和推广没问题，但需要披露。作为中文使用者，我反对各种「口令」对于文字的轻浮滥用。作为作者，我无法接受文章里出现这些审美上破产的格式。

所以问题来了：怎么得到一个体面的链接用来保存和分享？

为此，首先需要定义什么样的链接才是「体面」的。我的标准是，能够稳定、持续地重新定位到商品，而只包含最小、必要信息的链接。

什么样的信息对于定位商品是必要的呢？尽管不同电商平台的识别方法不同，但共同点是都会给每个型号的商品编配一个唯一编号；这就像是相应型号商品的「身份证号码」一样。例如，淘宝、拼多多一般用 12 位数字来编号，京东用 12 或 14 位数字（早年曾经用过较少位数）；亚马逊则使用更为严谨的 [ASIN](https://sellercentral.amazon.com/help/hub/reference/external/201844590) 机制，格式为 10 位大写字母和数字组合。

将这些商品编号与各自平台的规范链接模板拼接在一起，就得到了最干净的链接形态。如下表所示：

| 平台 | 规范链接模板 | 商品编号格式（正则表达式） | 规范链接示例 |
| --- | --- | --- | --- |
| 淘宝 | `https://item.taobao.com/item.htm?id=$ID` 或 | 一般为 12 位数字（`\d{12}`） | https://item.taobao.com/item.htm?id=123456789012 |
| 京东 | `https://item.jd.com/$ID.html` | 一般为 12 或 14 位数字（`\d{12,14}`） | https://item.jd.com/12345678901234.html |
| 亚马逊 | `https://www.amazon.com/dp/$ID` 或 `https://www.amazon.cn/dp/$ID` 等 （顶级域名对应不同地区分站） | 10 位大写字母和数字组合（`[0-9A-Z]{10}`） | https://www.amazon.com/dp/B0001ZY2XW |
| 拼多多 | `https://mobile.pinduoduo.com/goods.html?goods_id=$ID` 或 `https://mobile.yangkeduo.com/goods.html?goods_id=$ID` | 一般为 12 位数字（`\d{12}`） | https://mobile.yangkeduo.com/goods.html?goods\_id=123456789012 |

于是，剩下的问题就是如何得到商品编号。这并不困难：

* 京东、拼多多等客户端分享的链接中，本身就包含了商品编号参数，只要按照上表从链接里找出来即可。
* 淘宝略微麻烦一点，它的客户端默认分享的是 `m.tb.cn` 域名的短链接，但只要粘贴到浏览器里访问一次，等待被跳转到完整版的页面，跳转后的链接里就能看到记录商品编号的 `id` 参数（也可以直接从短链接的 HTML 源码里看到目标地址；淘宝团队在那里非常贴心地用中文加了醒目注释）。

![](https://cdn.sspai.com/2022/12/10/2eb391a993cb18f705d65643e06292e3.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

听我说

iOS 用户可以使用我做好的这个[快捷指令](https://www.icloud.com/shortcuts/308059b3c7ad4c708001df212f4ff834)；从客户端复制后运行即可得到规范链接。你也可以自行参考上面给出的正则表达式，用其他自动化工具实现类似效果。

另一个干扰因素在于，电商平台普遍都有五花八门的域名。例如，淘宝有短域名 `tb.cn`、隔壁的天猫 `tmall.com` 和国际版 `world.taobao.com`；京东有短域名 `3.cn` 和国际版 `jd.hk`；拼多多有替身域名 `yangkeduo.com`（羊可多？养客多？这甚至不能反映它[全部的想象力](https://www.v2ex.com/t/887582)）；等等。

但这些域名本质上都是马甲，大多数情况下可以与主域名互换使用。唯一特殊的是亚马逊，对于同一个 ASIN，使用 `amazon.cn` 和其他全球分站的域名，将会分别打开中区海外购的页面和相应商品在海外区的原始页面。

实际上，电商网站也以一种隐蔽的形式透露了链接的「标准答案」。在电脑版商品页面（可能需要登录）的空白处点击右键，选择「查看源码」，就能在 HTML 源码的头部找到这样的内容：

```
<html>
    <head>
        . . .
        <link rel="canonical" href="https://item.taobao.com/item.htm?id=123456789012" />
        . . .
```

这里，`<link rel=canonical>` 元素的作用就是提供「当前页面的规范（[canonical](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel#attr-canonical)）链接」。这是一个主要给搜索引擎看的信息，其目的正是在页面有多种「马甲」或带参数版本的情况下，自我坦白哪一个才是本尊，以免因为分散访问影响搜索排名。（拼多多没有这个元素，但也许它的词典里就没有 canonical 这个词。）

你可以用我做好的一个[小书签](https://codepen.io/platyhsu/pen/rNKbLjW)来提取网页的规范链接。将其拖拽到浏览器书签栏后，在浏览网页版电商页面时点击「ExtractCanonical」链接即可显示当前页面源码中的规范链接。

![](https://cdn.sspai.com/2022/12/10/21178d708eb7ed43a6b05345f6b2a2c9.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

当然，也许你看完这些解释，并没有自己实践的动力，觉得还是太麻烦了；这完全可以理解。写下这些的目的，更多是作为一种提示：作为用户，有权利知道自己的每步操作意味着什么，让谁获得利益。即使一定的商业行为是必要的，也应该以更透明的方式说明，并且给出选择机制，而不是把一切都藏在短链接和「火星文」后面。

2011 年，一名 Facebook 早期员工 Jeff Hammerbacher 在接受《彭博商业周刊》[采访](https://www.bloomberg.com/news/articles/2011-04-14/this-tech-bubble-is-different)时，说过一句著名的话：「我们这一代最聪明的人都在思考如何让人们点击广告；太糟糕了。」 (The best minds of my generation are thinking about how to make people click ads. That sucks.) 十年过去，聪明的人变得更聪明了，糟糕的东西变得更糟糕了。我们也许不能阻止，但能做的就是用笨办法对付聪明，用顽固对抗糟糕。

[![PlatyHsu](https://cdn-static.sspai.com/ui/img-placeholder.png)](https://sspai.com/u/platyhsu/updates)

You hypocrite lecteur, —mon semblable, —mon frère

文章来源: https://sspai.com/post/77189
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)