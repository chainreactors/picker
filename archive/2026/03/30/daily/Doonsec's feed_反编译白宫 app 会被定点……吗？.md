---
title: 反编译白宫 app 会被定点……吗？
url: https://mp.weixin.qq.com/s/Nj-olbgjzSHXb6JLwbabEA
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:34:49.474206
---

# 反编译白宫 app 会被定点……吗？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NBEba9EhqpncibiaVvAonp5zibOiamUnnsGiboWPzfQJBwWicFw5zY0bhtzp5zs167rqggk4VZAgvnoE9GTj8N6auo9XFM6ZPxRe8jYR2YicYJr3Uc/0?wx_fmt=jpeg)

# 反编译白宫 app 会被定点……吗？

原创

营销号
营销号

非尝咸鱼贩

![]()

在小说阅读器中沉浸阅读

2026 年 3 月 27 日，“The White House”官方移动应用程序上线了。上线不久就有两位手痒的研究员发布了分析报告，分别针对 Android 和 iOS：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NBEba9EhqplBjswVA32AoAic10Z7kiaVBzl0C69JJuD1Yic6UYF9ibTau9DkUW3BYc7N2mhTDSsoZu5sQqOceRXjbNygKX11y9KiaODBVLkaQZn0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/NBEba9Ehqpk55OWll7x50icW9LyRTYic97DoVaib9UGuxLJDribj4O5cXdowhKbSCUsNBlOhB2cK22nk6MWKctDzfCR5A6ibChO3VMa6HefX5TXU/640?wx_fmt=png&from=appmsg)

外网链接咱就不贴了，很容易搜索到。由于这个 app 本质上是 expo（基于 React Native）框架开发，所以两篇文章大同小异。

在这里要提一嘴。React Native 有个坏处是，原本 iOS 下的 ipa 包都有fairplay 数字版权管理（DRM）保护，要反编译二进制代码，首先要做的事就是找个越狱设备进行“砸壳”。

然而 fairplay 只保护 Mach-O 可执行文件，React Native 的 hermes 字节码（jsbundle）是没有加密的。直接用 ipatool 工具从 iTunes 下载 ipa 回来直接 unzip 就好了。甚至是框架（.framework）里的本地代码，LC\_ENCRYPTION\_INFO\_64 的 cryptoff 会跳过文件头的相当一部分数据，即使不解密也能用 nm 工具打印出一堆符号来猜。相当于砸壳可有可无了。

所以 iOS 那篇分析的作者直接甩锅，没有用破解工具哦：

> We downloaded the app, unzipped it, and took a look at what’s inside. No hacking, no traffic interception, no DRM bypassing. Just standard macOS tools (strings, nm, plutil) pointed at a free app anyone can download from the App Store.
>
> Security Analysis of the Official White House iOS App

研究人员反编译发现，应用每隔数分钟采集一次 GPS 定位，数据同步至第三方服务器；在 WebView 注入 js 代码绕过网站付费墙（paywall）和隐私提示，违反欧盟 GDPR 法规；部分代码依赖的仓库是个人开发者，存在被篡改风险。

下面进入正题。

之前有发文章宣传过我写了个图形界面工具来方便 iOS 和 Android 两大主流平台的 app 分析。其中包括 React Native 运行时分析：

![](https://mmbiz.qpic.cn/mmbiz_png/NBEba9Ehqpk8Qu39vLWI8crylvWlkfpLOt8Ricib0trJQdKcZKyc7BZibIeT5P2MPSxUR1la2WOGCVbTpUX51CFhxkW6atusTF00p15o5nw9V8/640?wx_fmt=png&from=appmsg)

手欠的我当然是试了一把。理论上 React Native 的界面逻辑，通过注入 js 做原型链的钩子就能实现很多修改，暂时还没精力深入开发这块。

![](https://mmbiz.qpic.cn/mmbiz_png/NBEba9EhqpmHcvKR7nibxHxj3coia6sUZ4qG4YVacCjWMKxEcibP8HSCwibYsMTPxYcZWtyPib4Ug4SsgBBeEFZCZAblpWzJmEr5uwAPIiaOfbdXM/640?wx_fmt=png&from=appmsg)

但别人的分析都集中在 React Native 反编译上。我这时候意识到我的程序里面集成的 hermes 反编译还不够用，而正好前两天 push 了一下 radare2 开发者，给 r2hermes 工具加上了缺失的交叉引用功能。

在这里补充一下上下文。radare2 最近上了 hermes 字节码反编译的插件。radare2 虽然反编译效果算不上怎么样，但胜在免费开源集成方便。即使是 GPL，反正我不改代码不静态链接就好了。

于是今天搞了一下午，做了一个网页版的 radare2。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NBEba9Ehqpn2MLI0nhDOPrGiahhfZJE9NXx9iaoYiaMk8Y71ObQ4wibJXo30FSlkQuaCiblEQQy9dI6owlCp8QicCOMUDkicjcsL1OHPARcqnqm6eo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NBEba9Ehqpn07M4Uo0QqkwFwJ2n7CK6rkibTg6xTB0xcqjoVs5UtNnsyV1XXxpL4FI74nhWUwHIF5gCBAjO19OcEpkTfuTUgIlY0bQic47ZbE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NBEba9EhqpmvKfLlAn9VHasYvejOPUa3lnXWiaSThQiajDO2GQIWb8FH5CG7TbeOwA9SSSPU0r0xBsG0fc5h1zCA0fXoaTOxsmtZSkkyZaF3g/640?wx_fmt=png&from=appmsg)

配置 llm 之后简直就是开挂，反编译出来的东西跟源码似的。

基本找到了几位研究员提到的相关代码，在字符串里还多处硬编码了……不予置评。咱们是技术博主，不是观点输出博主。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NBEba9EhqpkPdvNJeHreQwgB8YPwjS6C3A73ia0ias4BjiaGNFxl8Nvg2uwgxu96ibrkA3AT61Xq6nNCeAicswaFVh3GRmBHukxhU82vkraC4Pz4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/NBEba9EhqpmJrIiaiasGm1thJ57PAjYLWicSXTXr3IR2CHwHqjWg6Ng58cYf9V5ibiaibB43CnmtKPxAyibjkMQWsF19RMLpKHuuqZPdNqzjicqLhFg/640?wx_fmt=png&from=appmsg)

工具已经发布了 v1.1.0 到 npm，node 一键安装：

```
npm i -g igf
```

也可以去 GitHub 页面直接下载 exe，基于 bun 打包的单文件。由于没（经费去）代码签名，下载安装的方式需要自行去除来自 Internet 标记，否则将无法运行。同样由于没有代码签名，没法验证文件是不是官方（我）构建的，所以还请风险自负。

问题来了，反编译白宫的 app 会被定点……吗？

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/6N4b2yN3FOJePjhDUn7xMMlhZWpLjDwu3WUia32nGS0LiaB64WpyniauGgN9ibRaG1okaRpxswTPwaEgqTlic3aRJrQ/0?wx_fmt=png)

非尝咸鱼贩

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/6N4b2yN3FOJePjhDUn7xMMlhZWpLjDwu3WUia32nGS0LiaB64WpyniauGgN9ibRaG1okaRpxswTPwaEgqTlic3aRJrQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过