---
title: 一波三折 Carplay 播放视频「未完结」
url: https://h4ck.org.cn/2025/06/20984
source: obaby@mars
date: 2025-06-19
fetch_date: 2025-10-06T22:51:58.721616
---

# 一波三折 Carplay 播放视频「未完结」

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

[苹果『iOS』](https://h4ck.org.cn/cats/xtxg/%E8%8B%B9%E6%9E%9C%E3%80%8Eios%E3%80%8F)

# 一波三折 Carplay 播放视频「未完结」

2025年6月18日
[48 条评论](https://h4ck.org.cn/2025/06/20984#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/WechatIMG1605.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/06/WechatIMG1605.jpg)

上一篇写 caryplay 自定义壁纸分析的时候，[段先森](https://www.duanxiansen.com/) 提了个问题，说什么时候能播放视频。

当时自以为是的以为既然能把 vlc 播放器添加到 carplay，那么自然就能播放视频了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/Jietu20250618-101926.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/06/Jietu20250618-101926.jpg)

直到后来自己试了一下才发现，这个虽然能添加到 carplay 但是在车机上只能播放音频文件，并没有播放视频的功能。看来还是自己想得简单了，你以为的并不是你以为的。

不过，这半途而废，毕竟不是我的风格，于是开始搜索这种视频播放方案。

最后还是找到了https://onejailbreak.com/blog/tds-carplay/ ，

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/tds-carplay.766x0.webp)](https://h4ck.org.cn/wp-content/uploads/2025/06/tds-carplay.766x0.webp)

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/tds-carplay-2.854x0-is.webp)](https://h4ck.org.cn/wp-content/uploads/2025/06/tds-carplay-2.854x0-is.webp) [![](https://h4ck.org.cn/wp-content/uploads/2025/06/tds-carplay-3.854x0-is.webp)](https://h4ck.org.cn/wp-content/uploads/2025/06/tds-carplay-3.854x0-is.webp)

这个东西，原理并不是简单的通过投屏实现的，具体的原理可以看源代码：

https://github.com/thomasdye12/TDS-Carplay?tab=readme-ov-file

按照简介，要使用也很简单：

Here’s how to install TDS CarPlay via TestFlight Link:

**Step 1**. Install TestFlight App from the App Store.

**Step 2**. [Download TDS CarPlay](https://onejailbreak.com/blog/tds-carplay/download) and select the TestFlight Link from the available options.

**Step 3**. When the TestFlight app opens, approve the installation of the TDS CarPlay app.

**Step 4**. Restart your iPhone after installation is completed.

**Step 5**. Open the TDS CarPlay app from your home screen.

然而，上面的 testflight 方法的问题在于，所有的体验名额已经满了，也就无法安装。那么剩下一条路就是下载 ipa 签名，下载 ipa 签名之后，会面临另外一个问题，权限问题：

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/Jietu20250618-102928.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/06/Jietu20250618-102928.jpg)

签名的 mobileprovision 文件需要有上面的两个 carplay 权限，然而，普通的应用商店账号是没这个权限的，也就是即使签名安装了也无法添加到 carplay 上，以为这个问题来回折腾了无数次，直到最后才发现是权限问题。而这个全是是需要单独申请的，通过下面的页面申请：

https://developer.apple.com/contact/request/carplay/

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/Jietu20250618-103214.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/06/Jietu20250618-103214.jpg)

申请的时候选择 communication，申请的时候开始选了个 drive task，结果拿到的权限依然不够。这个权限对应的默认可用属性，参考这个：

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/Jietu20250618-103736.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/06/Jietu20250618-103736.jpg)

申请的时候没仔细研究各个属性的却别，随便申请了一个，结果就导致再次申请权限的时候 apple 直接回了个已经有对应的权限了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/AE8349DF07A24CEBB087B69E596CEAD2.png)](https://h4ck.org.cn/wp-content/uploads/2025/06/AE8349DF07A24CEBB087B69E596CEAD2.png)

看到这个回复，人直接麻了，这尼玛，该怎么搞。后面给苹果回了封邮件说明了下情况，看苹果的答复吧，暂时就卡在这里了。

苹果 carplay 开发文档：https://developer.apple.com/download/files/CarPlay-Developer-Guide.pdf

「待续……」

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《一波三折 Carplay 播放视频「未完结」》](https://h4ck.org.cn/2025/06/20984)
\* 本文链接：<https://h4ck.org.cn/2025/06/20984>
\* 短链接：<https://oba.by/?p=20984>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[carplay](https://h4ck.org.cn/tags/carplay)

[Previous Post](https://h4ck.org.cn/2025/06/20996)
[Next Post](https://h4ck.org.cn/2025/06/20978)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2013年8月20日

#### [使用gdb和cycript越过iOS应用的越狱检测](https://h4ck.org.cn/2013/08/5317)

2021年9月3日

#### [百度语音识别 ASR 收费导致的bug](https://h4ck.org.cn/2021/09/8970)

2017年11月25日

#### [百度语音识别 语音唤醒失败](https://h4ck.org.cn/2017/11/6005)

### 48 comments

1. ![](https://gg.lang.bi/avatar/ffc1ac2ecde17b2eb1caff3e94c119fdaea4dc1a947a08a3092b388bf9b454d0?s=64&d=identicon&r=r) **[ACEVS](https://acevs.com/)**说道：

   [2025年6月18日 11:29](https://h4ck.org.cn/2025/06/20984#comment-127135)

   ![Level 5](https://badgen.net/badge/亲密度/Level 5/orange?icon=codebeat)

   ![Google Chrome 137](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 137") Google Chrome 137 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   没有车 先mark

   [回复](#comment-127135)
2. ![](https://gg.lang.bi/avatar/c74d85e5f513e4b79c20bfe8e48002c93982ddbc4848e29de52e3c54ac7fcce3?s=64&d=identicon&r=r)

   [2025年6月18日 11:55](https://h4ck.org.cn/2025/06/20984#comment-127136)

   ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![Google Chrome 137](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 137") Google Chrome 137 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   Carplay 可以播放视频？我的好像一直不行，车机也不让放，说出于安全考虑 不可以行驶中看视频

   [回复](#comment-127136)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年6月18日 13:09](https://h4ck.org.cn/2025/06/20984#comment-127140)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 134](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 134") Google Chrome 134 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      正常是不行的

      [回复](#comment-127140)
3. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r)

   [2025年6月18日 12:59](https://h4ck.org.cn/2025/06/20984#comment-127138)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Google Chrome 137](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 137") Google Chrome 137 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   知道了你有Carplay

   [回复](#comment-127138)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年6月18日 13:10](https://h4ck.org.cn/2025/06/20984#comment-127142)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Goo...