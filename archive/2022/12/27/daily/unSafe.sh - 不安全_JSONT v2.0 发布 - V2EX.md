---
title: JSONT v2.0 发布 - V2EX
url: https://buaq.net/go-141466.html
source: unSafe.sh - 不安全
date: 2022-12-27
fetch_date: 2025-10-04T02:31:59.901615
---

# JSONT v2.0 发布 - V2EX

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

![](https://8aqnet.cdn.bcebos.com/a2e7cd4ca10e7d24ae70617844a31e14.jpg)

JSONT v2.0 发布 - V2EX

大约一年前我在 v 站发布了 JSONT的第一个版本，后续收到了很多热心用户的反馈，工具也一直在迭代升级，直到最近，我感觉是时候做一个彻底的重构升级了，于是开启了“快速”的重构之旅，大约耗时 2 周。
*2022-12-26 21:9:12
Author: [v2ex.com(查看原文)](/jump-141466.htm)
阅读量:61
收藏*

---

大约一年前我在 v 站[发布了 JSONT](https://v2ex.com/t/830936)的第一个版本，后续收到了很多热心用户的反馈，工具也一直在迭代升级，直到最近，我感觉是时候做一个彻底的重构升级了，于是开启了“快速”的重构之旅，大约耗时 2 周。

1 、技术栈方面当然是选择了最新的 vue3+vite ，UI 选择了 Tailwind+Vuetify3 。个人很喜欢 Tailwind ，但是他本身是一个 CSS 框架，没有太好的交互组件库，于是搭配了 vuetify ，这也是个人认为做的最好（设计思想）的 vue 组件库了。

2 、网站布局从之前的左文本右树形结构改成了分开独立的视图，出发点是大多数场景下都是粘贴 JSON 到文本框中后就没有再动过文本了，所以完全可以在格式化后“去掉文本框” 目前的交互就是，用户进入网站，将 JSON 粘贴到为空的文本框中，就会自动触发格式化操作，或者手动输入完成按 Tab 键也可以触发。文本视图下也改成了 Vscode 同款在线编辑器，可以很方便地从头开始编写 JSON 。其次未来也会考虑加入类似 JSON Hero 这样更多的 JSON 视图模式。

3 、基本功能都保留且做了优化，部分功能（比如 MOCK 和函数）正在加入中

4 、由于看到之前某位仁兄的画图本域名的遭遇，而 JSONT 本身也有未登录的一键分享功能，不想牺牲这样一个方便的功能，于是决定把网站整体迁到境外，域名目前已经撤销备案正在转移中，前端和后端都部署在了境外服务中，有了 PWA 的加持目前国内速度还可以接受，除了首次可能会慢点，后续基本会比较快。

5 、如果之前访问过网站，由于 PWA 的原因，要想快速看到新版可能需要手动更新一下 worker ，具体方式就是 F12 -> Application ->Service workers -> Unresiter 然后刷新网站即可。

6 、目前和以后 JSONT 都不会放广告影响用户体验，当然这也是我个人对于一个工具型应用的原则，但是考虑到服务器成本，将来可能会加入一些额外的高级付费服务功能（类似保存服务端，但是不会影响之前已保存的文件）。

7 、由于 JSONT 的后端服务并不繁杂，之前还用了 Nest ，趁着本次重构之际加之不能再解析到阿里云 ECS ，索性将后端都放到了轻量级的 worker 中，目前来看效果还可以。

总之，很感谢有着类似需求和喜好的人使用 JSONT ，其实也是我自己经常会用的，我个人是做前端开发的，说一个我经常使用的场景，测试在线上发现了 BUG ，当然是因为数据问题，但是我们又不能连线上接口或者很麻烦，于是需要测试把线上接口的数据发给我，这个时候测试直接使用分享功能将数据以链接的形式发给我，我这边打开之后直接使用“生成接口”的功能将其变成一个可以跨域访问的接口，然后将代码里面的地址临时换成 mock 接口地址，于是便能快速复现问题了。

所以 JSONT 的很多功能都是我个人在实际开发中发现的一些场景，当然也欢迎有着类似需求的同学多多建议让 JSONT 更强大更好用。( <https://jsont.run/>)

[![zx1gU0.png](https://s1.ax1x.com/2022/12/26/zx1gU0.png)](https://imgse.com/i/zx1gU0)

文章来源: https://v2ex.com/t/904694#reply6
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)