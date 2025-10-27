---
title: 你的地盘听你的？
url: https://h4ck.org.cn/2025/06/20996
source: obaby@mars
date: 2025-06-21
fetch_date: 2025-10-06T22:53:21.003746
---

# 你的地盘听你的？

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

# 你的地盘听你的？

2025年6月20日
[52 条评论](https://h4ck.org.cn/2025/06/20996#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/WechatIMG1610.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/06/WechatIMG1610.jpg)

大雨如期而至，伴着狂风，打在玻璃上发出噼里啪啦的声音。屋里的空气变得潮湿而又烦闷，于是去找空调的遥控器，由于坏了一个，三个空调只有两个好用的遥控机，好在两个挂机型号是一样的可以通用。

这第一次开空调想着把空气滤网清洗一下，柜机的周末已经洗过，剩下卧室的两个挂机，拆下来洗干净，装回去，主卧的空调一切顺利。

次卧空调打开，过了没多久就显示了故障码 F3。

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/WechatIMG1611-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/06/WechatIMG1611.jpg)

搜了一下，发现可能是外机通讯故障。打开智驾 app，准备报修。

然而，在打开 app 的时候，提示发现新的设备可以接入，一个热水器。这就挺奇怪的，之前装的小厨宝几百块钱的东西，感觉应该不支持联网功能。看到这个提示，还是链接配置了一下，配置过程倒是很顺利，轻易就连上了家里的 wifi，远控控制了一下关机，发现没动静。

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/16081750397675_.pic_-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/06/16081750397675_.pic_.jpg)

（设备已经删除了）

现在基本可以肯定这个东西不是我的了，应该是刚装修的隔壁邻居，已经装上了热水器。

并且这个热水器没有配置过，所以出于配网模式。只是这种模式现在看来，问题不少。只要开启了蓝牙和 wifi 功能，一旦扫描到设备就提示配网，这个设计的确省去了要开启配网模式的繁琐手续，但是安全性的问题也自然暴露了出来。

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/16091750397676_.pic_-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/06/16091750397676_.pic_.jpg)

这种配网扫描的模式，同样会搜索周围的可配网设备，那么在设备使用期间。如果没配置过网络，那么自然这个机会就留给了别人。并且，这种模式下是设备的控制权完全到了别人手里，例如热水器温度设置，启用时间，功率设置等等。

如果是洗衣机，微波炉，电磁炉等设备，被远程启动也可能会出问题。

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/16071750397523_.pic_-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/06/16071750397523_.pic_.jpg)

所以，这种支持快速配网的设备，到手之后就先配网吧，最起码连到自己的手机上，不要让别人轻易的获取了控制权。

只是现在支持联网的设备越来越多了，几乎成了标配了。那么要想恶心人其实也简单，带着手机，扫描可配网设备，都连到自己的手机上，然后就可以为所欲为了。

你说你想连的设备不在你家附近，没网？

如果有 wifi，弄个装了 kali 的系统去破解 wifi 密码吧，先搞定 wifi，然后搞定设备。甚至如果设备已经连接到这个 wifi 了，自己把电脑链接进去也可以做点别的事情。

什么连网络都没有？如果真的想搞，带个无线网卡吧，扫到设备连到你的无线网卡上一样能控制设备。反正，就是想搞点破坏或者恶作剧而已不是吗？

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/16121750401345_.pic_-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/06/16121750401345_.pic_.jpg)

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/16131750401346_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/06/16131750401346_.pic_.jpg) [![](https://h4ck.org.cn/wp-content/uploads/2025/06/16141750401347_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/06/16141750401347_.pic_.jpg)

今天看微博，教主说，信息安全依然大有可为。这个东西的确不会过时，哪怕 ai 发展到一个很先进的成都，信息安全的问题可能依然需要人去解决。因为钻空子，或者找漏洞，不单需要技术积累，还需要一定的创造力、想象力。前几篇跟 carplay 相关的文章，真正的目的是为了开车看视频吗？其实并不是，就是想直到到底能不能行，能不能突破这个限制而已，哪怕真的能看，自己也不会开车看视频，毕竟之前小六子的车机能直接播放视频，但是却基本没看过。

等哪天到了机械公敌时代，懂点信息安全，可能活的时间也能比别人更长一些。

你的地盘听你的？

不，我可以让你的地盘听我的。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《你的地盘听你的？》](https://h4ck.org.cn/2025/06/20996)
\* 本文链接：<https://h4ck.org.cn/2025/06/20996>
\* 短链接：<https://oba.by/?p=20996>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[信息安全](https://h4ck.org.cn/tags/%E4%BF%A1%E6%81%AF%E5%AE%89%E5%85%A8)[家电](https://h4ck.org.cn/tags/%E5%AE%B6%E7%94%B5)

[Previous Post](https://h4ck.org.cn/2025/06/21011)
[Next Post](https://h4ck.org.cn/2025/06/20984)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2025年2月5日

#### [白月光 II](https://h4ck.org.cn/2025/02/19103)

2024年4月23日

#### [流量没了ಥ\_ಥ](https://h4ck.org.cn/2024/04/16700)

2025年3月10日

#### [品味江南（二）–夜半钟声到客船](https://h4ck.org.cn/2025/03/19668)

### 52 comments

1. ![](https://gg.lang.bi/avatar/c8b1c4e066955840427abd9f454b9fb9569d4480ec1b84bb78c8b210d91893d8?s=64&d=identicon&r=r) **爱看**说道：

   [2025年6月20日 15:18](https://h4ck.org.cn/2025/06/20996#comment-127208)

   ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Google Chrome 109](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 109") Google Chrome 109 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   只听灵妹妹的

   [回复](#comment-127208)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年6月21日 15:47](https://h4ck.org.cn/2025/06/20996#comment-127224)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 134](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 134") Google Chrome 134 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      😉

      [回复](#comment-127224)

      1. ![](https://gg.lang.bi/avatar/c8b1c4e066955840427abd9f454b9fb9569d4480ec1b84bb78c8b210d91893d8?s=64&d=identicon&r=r)

         [2025年6月22日 20:53](https://h4ck.org.cn/2025/06/20996#comment-127249)

         ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

         ![Google Chrome 109](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 109") Google Chrome 109 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

         毕竟又白又大

         [回复](#comment-127249)
2. ![](https://gg.lang.bi/avatar/ffc1ac2ecde17b2eb1caff3e94c119fdaea4dc1a947a08a3092b388bf9b454d0?s=64&d=identicon&r=r)

   [2025年6月20日 15:30](https://h4ck.org.cn/2025/06/20996#comment-127209)

   ![Level 5](https://badgen.net/badge/亲密度/Level 5/orange?icon=codebeat)

   ![Google Chrome 137](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 137") Google Chrome 137 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   确实安全第一，目前没啥联网的设备。之前买烤箱还是选了个机械控制的。感觉寿命长点似乎。

   [回复](#comment-127209)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年6月21日 15:47](https://h4ck.org.cn/2025/06/20996#comment-127225)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 134](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 134") Google Chrome 134 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      越简单越可靠

      [回复](#comment-127225)
3. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r)

   [2025年6月20日 16:28](https://h4ck.org.cn/2025/06/...