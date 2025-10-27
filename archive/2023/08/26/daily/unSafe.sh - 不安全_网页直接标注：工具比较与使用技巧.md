---
title: 网页直接标注：工具比较与使用技巧
url: https://buaq.net/go-175420.html
source: unSafe.sh - 不安全
date: 2023-08-26
fetch_date: 2025-10-04T11:59:29.443002
---

# 网页直接标注：工具比较与使用技巧

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

![](https://8aqnet.cdn.bcebos.com/e1d7f42333eddc5ca9ff9c2452e0af9b.jpg)

网页直接标注：工具比较与使用技巧

与先抓取再标注的常见功能相比，「在原始网页上直接标注」效率更高、适用面更广，在不少场合是更有意义的选择。本文分析和比较了 Hypothesis、Raindrop 和 Readwise Reader 三
*2023-8-25 21:31:9
Author: [sspai.com(查看原文)](/jump-175420.htm)
阅读量:32
收藏*

---

与先抓取再标注的常见功能相比，「在原始网页上直接标注」效率更高、适用面更广，在不少场合是更有意义的选择。本文分析和比较了 Hypothesis、Raindrop 和 Readwise Reader 三款具有直接标注功能的产品。

如果你用过任何「稍后读」类工具，一定不会对「标注」（annotation）功能陌生。但凡以「全功能」为志向的此类产品，都会不同程度地支持高亮、评论等标注功能。不过，大多稍后读工具所支持的，都是在经过抓取和解析的「清洁版」上标注。

这当然有其好处，例如利于专注、不受原网页断链影响等，但相应的缺点就是不够方便和通用。比如，有时只是想快速标记个别片段，如果搬出稍后读工具先抓取、跳转再标注，就显得过于繁琐。又比如，有的网页的设计使其很难被抓取，或者其内容本来就不属于文章范畴，先保存再标注的方法也就不灵了。

在这些场合，「在原始网页上直接标注」就是更有意义的选择。与先抓取再标注相比，直接标注效率更高、适用面更广；摩擦力小了，人就更有动力多做标注，避免出现那种明知有用却就是懒得动手摘录的情况。

![](https://cdn.sspai.com/2023/08/25/a46e78444794e32f94f8202f2e94c185.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

实际上，直接标注功能也算是互联网早期倡导者的一项未竟之志。在他们看来，互联网作为一张知识之网，本就应比实体文档更便于标注和交叉检索。「互联网之父」Tim Berners-Lee 在九十年代的一篇[提案](https://www.w3.org/History/1989/proposal.html)中就主张，超文本系统应当支持用户为批注和「节点」（一个信息单元，例如文件或文章）添加个人标注。早期浏览器 [Mosaic](https://en.wikipedia.org/wiki/Mosaic_%28web_browser%29) 曾以直接标注为重点功能之一，Marc Andreessen 本人也[大力推广](https://genius.com/Marc-andreessen-why-andreessen-horowitz-is-investing-in-rap-genius-annotated)（其投资的 Genius 是为数不多自带标注功能的网站之一）。

不仅如此，万维网联盟（W3C）还曾经成立过专门的工作组，开展网页标注的标准制定工作，并在 2017 年就形成了一套[正式推荐标准](https://www.w3.org/zh-hans/news/2017/three-recommendations-to-enable-annotations-on-the-web/)。根据这套标准，一条规范意义上的「标注」包含标注内容（body）、标注对象（target），以及对两者之间关系的说明。W3C 还研究了如何通过一系列「[选择器](https://www.w3.org/TR/2017/NOTE-selectors-states-20170223/#selectors)」（selector）定位标注对象，如何通过一系列「状态」（state）信息识别不同版本和格式的标注对象等问题。

遗憾的是，或许因为技术难度大、商业前景小等[综合因素](https://www.slideshare.net/dwhly/hypothesis-quick-overview-20110710)，网页直接标注始终没能流行起来——维基百科上列举着大量[已经扑街](https://en.wikipedia.org/wiki/Web_annotation#Discontinued_web_annotation_systems)的产品。

![](https://cdn.sspai.com/2023/08/25/ed994e2b09fa03c0e68112e19cd78d01.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

历史上（失败）的网页标注产品（来源：Hypothesis）

两年多前，我通过一款叫做 Hypothesis 的工具接触了网页标注，并写过[一篇文章](https://type.cyhsu.xyz/2020/10/hypothesis-tutorial/)介绍心得。在那之后，我一直持续使用和关注这类工具。尽管属于一个受关注较少的需求，近两年确实也能看到陆续有新的工具支持了网页直接标注。

根据尝试和比较，我认为其中相对优秀、发展前景较好的是 Raindrop 和 Readwise Reader。与 Hypothesis 相比，它们也各有侧重和优劣，值得研究和比较一番。如果你也有兴趣尝试直接标注网页的方法，希望本文能对你的选择有所帮助。

下表是从各个关键维度对三款工具的简要比较，后文则会做细化评论，并提供一些自己发现的使用技巧。

| **服务** | Hypothesis | Read w | Raindrop |
| --- | --- | --- | --- |
| **标注稳固性** | 最好（据原文内容、文本位置和 XPath 定位） | 较好（据原文内容、文本位置和变种 CSS Selector Path 定位） | 一般（仅据原文内容定位） |
| **网页兼容性** | 一般 | 较好 | 较好 |
| **摘录富文本格式** | 不支持 | 支持 | 不支持 |
| **评论富文本格式** | 支持 | 支持 | 不支持 |
| **桌面端支持** | 一般（JavaScript bookmarklet） | 最好（浏览器插件或 web app） | 较好（浏览器插件或 web app） |
| **移动端支持** | 较差（JavaScript bookmarklet） | 一般（iOS 或 Android app） | 尚可（iOS app、iOS Safari 插件或 Android app） |
| **数据导出** | 仅 API | 应用内复制（markdown）或 API | 应用内复制（纯文本或 markdown）或 API |
| **API 保存** | 支持 | 暂不支持 | 支持 |
| **保存原始内容** | 不支持 | 支持（正文部分） | 支持（原页面） |
| **价格** | 免费（开源） | $96/年（有提价计划） | 高亮标注等基本功能免费  文本标注等高级功能 $28/年 |

## Hypothesis：严谨但难用的「学术派」

对于一款标注工具来说，最关键的技术要素一定是「如何记录标注信息」，这将在很大程度上决定着它的使用体验。而在网页上直接标注的一大技术难点，就是第三方的网页内容不受用户控制，随时可能发生改版和修订，导致难以找回原先的标注位置。

Hypothesis 主要面向教育市场客户，而它的标注技术也可谓「教科书级」，基本就是照着 W3C 的标准来实现的。尽管在本文对比的三款工具中出现最早，它的标注定位能力至今仍然是未被超越的。

我在之前的文章中已经详细介绍过 [Hypothesis 的技术原理](https://type.cyhsu.xyz/2020/10/hypothesis-tutorial/#%E4%BA%8Chypothesis-%E7%9A%84%E6%9D%80%E6%89%8B%E9%94%8F%E6%A8%A1%E7%B3%8A%E9%94%9A%E5%AE%9A)，有兴趣可以翻看，这里只做一快速回顾。简单来说，Hypothesis 实现了一套称为「模糊锚定」的方案，**同时使用三种方法**存储标注文本在页面上的位置：

* 范围选择器 `RangeSelector`：记录标注文本所属 HTML 元素在网页中的位置，以 [XPath](https://www.w3.org/TR/xpath/) 表示；
* 文本位置选择器 `TextPositionSelector`：记录标注文本的起始和结尾在全部文本内容中的位置，以字符数偏移量表示；
* 文本引用选择器 `TextQuoteSelector`，记录标注文本的原始内容以及其前后相邻各 32 个字符，以字符串表示。

![](https://cdn.sspai.com/2023/08/25/65eb5c80ed077034cd66b644790ec585.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

当用户重新打开一个之前标注过的网页时，Hypothesis 会依次使用上述选择器，按照从精确到模糊的原则，尝试找回标注部分的位置。由于记录信息的冗余量足够多，Hypothesis 表现出极好的容错能力，即使原网页的结构、版式甚至内容顺序发生相当显著的变化，仍然能有很大概率成功定位。

可惜的是，正如很多开源工具一样，Hypothesis 的美好之处主要停留在技术底层，上层的用户体验则仅仅以「勉强能用」为追求。如今，这个工具的易用性跟我当年前发现它时相比，几乎没有任何改进：

* **使用繁琐。**每次必须要手动点击一个[专用的小书签](https://web.hypothes.is/start/)才能显示工具栏和标注历史（仅 Chrome 有插件，但仅仅是给相同代码打了个包，并无太多额外便利）。兼容性也比较一般，在一些版式复杂网页上运行时，经常无法正常选择和标注，或者干扰网页原有功能和布局。
* **无移动端。**虽然小书签理论上也可以在移动端浏览器上运行，但因为并未针对触摸操作优化过，真正能用的几率大概只有五成。

![](https://cdn.sspai.com/2023/08/25/a2c00150d6f50963d4a82dbae09a1f40.JPEG?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

* **管理不便。**官方版的网页管理界面只能简单搜索和查阅，不能批量管理和导出，必须依赖另一个由主要维护者个人提供的网页前端 [Facet](https://jonudell.info/h/facet/)。
* **不能存档。**Hypothesis 只专注于网页标注这一个功能，意味着如果网页本身发生删改或断链（在如今越发屡见不鲜），就无法找回当时的上下文，空留零星摘录。

好在，Hypothesis 完善的 [API 接口](https://h.readthedocs.io/en/latest/api-reference/)为 DIY 一个更好的体验提供了可能。

我在先前文章中已经[举例说明](https://type.cyhsu.xyz/2020/10/hypothesis-tutorial/#%E4%B8%89api-%E7%9A%84%E8%BF%9B%E9%98%B6%E4%BD%BF%E7%94%A8%E4%BB%A5%E5%B0%86%E6%9C%80%E8%BF%91%E6%89%B9%E6%B3%A8%E5%AF%BC%E5%87%BA%E4%B8%BA-markdown-%E4%B8%BA%E4%BE%8B)如何使用 API 将特定网页的标注导出为 markdown 格式。基于相同的原理，针对 [Obsidian](https://github.com/weichenw/obsidian-hypothesis-plugin)、[Logseq](https://github.com/c6p/logseq-hypothesis) 等笔记工具，都有人开发了相应的导出插件；包括后文会提到的 Readwise 在内，很多第三方服务也支持从 Hypothesis 同步标注内容。

另一种我后来发现的 API 用途是在移动端添加标注，比用小书签要顺畅得多。这里的难点在于 Hypothesis 创建标注的 API 语法 [[文档](https://h.readthedocs.io/en/latest/api-reference/#tag/annotations/paths/~1annotations/post)] 非常繁琐（拜它的数据结构所赐），以下是经过反复试错发现的最简调用方法：

```
{
  "group": "__world__",
  "document": {
    "title": "Example Title",
    "link": [
      {
        "href": "https://example.org/test"
      }
    ]
  },
  "uri": "https://example.org/test",
  "target": [
    {
      "selector": [
        {
          "type": "TextQuoteSelector",
          "exact": "Lorem ipsum dolor..."
        }
      ]
    }
  ]
}
```

这里：

* 简便起见，我们只使用 `TextQuoteSelector` 保存标注部分原文（记录在 `.target[0].selector[0].exact` 中）。
* `"group": "__world__"` 表示保存到默认的「公开」（Public）分组；如果想保存到私人（Private）或其他[自创分组](https://web.hypothes.is/help/annotating-with-groups/)，可以向 `https://api.hypothes.is/api/groups` 端点发送 GET 请求查询其对应 `id`。

得益于晚近版本的 Safari 分享菜单可以一次性输出当前浏览的网页标题、链接和选中部分文本，用一个 iOS 版快捷指令 [[下载](https://www.icloud.com/shortcuts/fcc098445ada4e5397d54294f9800011)] 就能按上述格式调用 API。导入这个快捷指令后，在开头填写 API token [[查询入口](https://hypothes.is/account/developer)] 和分组 id 即可。之后，在 Safari 中选中任意文本，通过分享菜单传递给该快捷指令，即可保存相应标注到 Hypothesis。

## Raindrop：朴实堪用的「经济适用款」

Raindrop 上线于 2013 年末，定位原本是云端书签管理器，随着功能发展逐渐融入了稍后读和标注等附加功能。这也成了它相比 Hypothesis 的一个显著优势：无需另寻方法保存网页内容，在一个工具里就能一站解决。再加上免费起步、年付 28 美元的低廉价格，堪称当下泛知识管理类服务中的性价比之选。（可能因为[开发者](https://help.raindrop.io/about/#who-made-raindropio)人在哈萨克斯坦？）

![](https://cdn.sspai.com/2023/08/25/da904cd13012bf7e8b5a079f575af8af.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

（来源：Raindrop）

但或许同样是受限于书签管理的核心定位，Raindrop 中的标注更像是一个「充话费送的」、锦上添花的功能，从设计到交互都有很多棱角粗糙之处。

**首先，从数据结构上看，Raindrop 的标注数据非常简陋。**它仅仅只记录标注部分的纯文本内容，也不包含任何文本位置信息。

如果标注的内容都是完整句子，这倒也没有太大问题。但如果标注部分比较简短、又恰好在文中多次出现（常见于高亮小标题、关键词时），只基于文本内容就完全无法准确定位。这时，Raindrop 只会傻愣愣地找到相同内容在文中第一次出现的地方，罔顾事实地认定这就是标注位置，令人捂脸不止。

这种数据结构也严重影响了 Raindrop 的性能。由于每条标注都要通过搜索匹配的方式来确定位置，重新打开有标注历史的页面时，至少要等待好几秒才能看到高亮内容浮现，并且等待时间随着高亮数量的增多而延长。如果网络不好，等个十几二十秒是很常见的。

**同时，Raindrop 的标注交互设计也有问题：**在新创建一条标注时，按照减少用户等待的原则，本应立即将标注部分高亮，异步地向服务器写入数据；但它实际上做的却恰好相反，先传输数据等待远程反馈，再刷新高亮位置并显示。这种奇葩设计导致从标注到显示高亮之间……也有几秒到十几秒的等待。作为 Raindrop 多年用户，我只能说确实感到自己的耐心随着使用年限而同步增长。

看到这里，你可能认为本文不会推荐用 Raindrop 做标注。但实际上，自从 Raindrop 支持标注以来，我已经将很多日常标注改用它来完成，只有认为值得细读的文章才会保存到稍后读工具里另行处理。

究其原因，对于在快速浏览间隙，零散标注二三要点的用例，追求的无非是留个记号、方便事后找回，上述那些设计问题其实影响有限。相比之下，Raindrop 的更多优点让它成为这种快速标注场景下的首选：

文章来源: https://sspai.com/prime/story/web-annotators-compared
 如有侵权请联系:admin#...