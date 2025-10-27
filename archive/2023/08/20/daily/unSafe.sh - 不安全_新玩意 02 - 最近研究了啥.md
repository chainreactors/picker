---
title: 新玩意 02 - 最近研究了啥
url: https://buaq.net/go-174817.html
source: unSafe.sh - 不安全
date: 2023-08-20
fetch_date: 2025-10-04T11:58:52.965582
---

# 新玩意 02 - 最近研究了啥

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

![]()

新玩意 02 - 最近研究了啥

最近研究的东西挺多的，包括 Raycast AI、Bear2、Inkdrop、Hookmark（一款将Mac上的软件进行双链的工具）、Keyboard Maestro 等，鉴于篇幅有限，今天重点就介绍
*2023-8-19 10:0:41
Author: [xzsj.vip(查看原文)](/jump-174817.htm)
阅读量:29
收藏*

---

最近研究的东西挺多的，包括 `Raycast AI`、`Bear2`、`Inkdrop`、`Hookmark`（一款将Mac上的软件进行双链的工具）、`Keyboard Maestro` 等，鉴于篇幅有限，今天重点就介绍 `Raycast AI` 和 `Obsidian 自定义样式 - Bear`。

[Raycast](https://www.raycast.com/) 不同于「聚焦」App 的地方在于它则「扩展了」这个搜索框的功能，通过 Raycast 可以快速启动程序或执行命令，例如设置窗口布局、调整声音大小、切歌等，是不是很熟悉？没错老牌效率类软件 [Alfred](https://www.alfredapp.com/) 可以做到同样的事，个人也是 Alfred 用户，切换到 Raycast 并**不完全是 Raycast 颜值或易用性**，最重要的原因在于 Raycast 的 Store 提供了功能丰富的扩展应用，这里随便列举几个常用的：

Raycast AI 是 Raycast 其推出的 Pro 功能（订阅用户才能使用），功能就是**集成了 ChatGPT 3.5 的 API**，让用户可以像使用 Raycast 那样（便捷的）使用 ChatGPT，最简单的使用方法就是通过「输入框」直接进行 AI 提问：

当然 Bob 也支持输入 openai key 使用翻译，但是 Raycast Pro 是包月的不限字数和次数，这样我就可以愉快的使用 AI 进行翻译，翻译效果比 Google 效果好一些（个人感觉），只不过速度不如 Google 翻译。

Raycast 是一款 macOS 上优秀的效率类软件，今天只是介绍了 Raycast AI 的部分功能，如果大家对 Raycast 感兴趣，可以自行搜索相关使用方法，虽然没有中文界面，但是页面设置简单，操作也符合 Mac 规范，几乎不影响使用，况且免费版的功能就完全够用（免费不包含 AI）。

实现这样的设置其实也不难，Obsidian 提供了一个插件 [Style Setting](https://github.com/mgmeyers/obsidian-style-settings) ，通过插件我们可以修改一些主题的样式，我就是在 [Blue Topaz 主题](https://github.com/whyt-byte/Blue-Topaz_Obsidian-css) 样式的基础上对照着 Bear 的「冰原」主题进行修改，最终改成这个样子的。
当我们分别安装了 `Style Setting` 插件和 `Blue Topaz` 主题后，打开 Obsidian 的设置就可以看到如下设置页面，其中提供了各种选项让我们设置：

```
{

"blue-topaz-theme@@color-scheme-options": "color-scheme-options-simplicity-topaz",

"blue-topaz-theme@@background-image-settings-switch": true,

"blue-topaz-theme@@background-image-settings-markdown-page-options": "background-image-settings-markdown-page-custom",

"blue-topaz-theme@@bg-markdown-page-opacity-cp": 1,

"blue-topaz-theme@@custom-markdown-page-background-color@@light": "#FEFDFD",

"blue-topaz-theme@@notebook-liked-markdown-page-options": "notebook-liked-markdown-page-stripe-notebook-2",

"blue-topaz-theme@@left-ribbon-style": "hide-left-ribbon",

"blue-topaz-theme@@layout-style-options": "layout-style-options-default",

"blue-topaz-theme@@scrollbar-style-option": "remove-scrollbars",

"blue-topaz-theme@@background-primary-bg-4-bt@@light": "#FEFDFD",

"blue-topaz-theme@@highlight-style": "bt-default-highlight",

"blue-topaz-theme@@accent-strong@@light": "#4D699E",

"blue-topaz-theme@@divider-color@@light": "#A1AFCB",

"blue-topaz-theme@@font-text-theme": "'LXGW WenKai'",

"blue-topaz-theme@@font-family-h1": "'LXGW WenKai'",

"blue-topaz-theme@@font-family-h2": "'LXGW WenKai',",

"blue-topaz-theme@@font-family-h3": "'LXGW WenKai'",

"blue-topaz-theme@@font-family-h4": "'LXGW WenKai'",

"blue-topaz-theme@@font-family-h5": "'LXGW WenKai'",

"blue-topaz-theme@@font-family-h6": "'LXGW WenKai'",

"blue-topaz-theme@@font-family-folder-file-title": "'LXGW WenKai'",

"blue-topaz-theme@@font-family-tag": "'LXGW WenKai'",

"blue-topaz-theme@@font-family-em": "'LXGW WenKai'",

"blue-topaz-theme@@h2-size": "1.5375em",

"blue-topaz-theme@@h3-size": "1.2125em",

"blue-topaz-theme@@print-h1-color@@light": "#4D699F",

"blue-topaz-theme@@h1-text-align-settings": "h1-text-align-start",

"blue-topaz-theme@@print-h2-color@@light": "#4D699F",

"blue-topaz-theme@@print-h3-color@@light": "#4D699F",

"blue-topaz-theme@@print-h4-color@@light": "#4D699F",

"blue-topaz-theme@@print-h5-color@@light": "#4D699F",

"blue-topaz-theme@@print-h6-color@@light": "#4D699F",

"blue-topaz-theme@@file-line-width": 48,

"blue-topaz-theme@@line-height-main": 2,

"blue-topaz-theme@@paragraph-spacing": 1.2,

"blue-topaz-theme@@letter-space-main": 1,

"blue-topaz-theme@@reduce-bottom-padding": true,

"blue-topaz-theme@@bottom-padding-value": "0em",

"blue-topaz-theme@@muted-activeline-bg": true,

"blue-topaz-theme@@fancy-hr": "default-hr",

"blue-topaz-theme@@hr-color-icon-1@@light": "#A1AFCB",

"blue-topaz-theme@@hr-color-icon-2@@light": "#A1AFCB",

"blue-topaz-theme@@hr-color-icon-3@@light": "#A1AFCB",

"blue-topaz-theme@@hr-color-icon-4@@light": "#A1AFCB",

"blue-topaz-theme@@fancy-hr-icon": "'😀'",

"blue-topaz-theme@@line-height-list": 1.4,

"blue-topaz-theme@@list-indent": 2,

"blue-topaz-theme@@unordered-list-style-options": "bt-default-unordered-list",

"blue-topaz-theme@@ordered-list-style-options": "default-ol-list-marker",

"blue-topaz-theme@@hide-embed-title": true,

"blue-topaz-theme@@link-underline-external": true,

"blue-topaz-theme@@link-underline-unresolved": true,

"blue-topaz-theme@@internal-link-color@@light": "#934743",

"blue-topaz-theme@@external-link-color@@light": "#934743",

"blue-topaz-theme@@unresolved-link@@light": "#934743",

"blue-topaz-theme@@link-click": true,

"blue-topaz-theme@@cursor-color@@light": "#C88280",

"blue-topaz-theme@@checkbox-size": "1rem",

"blue-topaz-theme@@img-grid": true,

"blue-topaz-theme@@loading-page-style-option": "default-loading-page",

"blue-topaz-theme@@setting-etc-pane-style": "setting-style-traditional",

"blue-topaz-theme@@titlebar-close-button": "default-titlebar",

"blue-topaz-theme@@hide-titlebar-close-btn": true,

"blue-topaz-theme@@outline-style": "default-outline-style",

"blue-topaz-theme@@stack-tabs-text-ori-options": "stack-tab-text-ori-mixed",

"blue-topaz-theme@@tab-head-style": "transparent-tab-style",

"blue-topaz-theme@@full-width-backlinks": true,

"blue-topaz-theme@@quiet-outline-optimize": true

}
```

还有一个更简单的方法，安装 [Better Command Palette](https://github.com/AlexBieg/obsidian-better-command-palette) 插件，然后如图设置「快捷指令」这样就可以更快地执行命令（每次按下 `CMD+SHIFT+P` 启动命令行）：

```
.link-icon > * {

display: none;

}

.internal-link::after {

content: "\00a0";

}

.cm-formatting-link-end~.data-link-text::after {

content: "";

}
```

Bear 2.0 版本的发布还是给我带来了一些新鲜感，包括表格、双向链接、新的样式和快捷操作体验等等，如果你想有一款颜值和功能都在线，也不用折腾得笔记软件，这里隆重推荐 [Bear](https://bear.app/)。

文章来源: https://xzsj.vip/2023/fresh-and-fun-02
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)