---
title: 我用一招「隐藏术」，PUA 了所有大模型
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653060220&idx=1&sn=59413b422334087df04ca5d09a4e1092&chksm=7e5701ca492088dc9a8ec9ae8bd2d3a54db7bc8516120233e235e1eb818a4a3e3d521dd3e8d9&scene=58&subscene=0#rd
source: 极客公园
date: 2024-10-24
fetch_date: 2025-10-06T18:53:29.051476
---

# 我用一招「隐藏术」，PUA 了所有大模型

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZI2PsAFe7hnfeLOVsfmpJjM0icORIicVh1N3UbOGJZFR5kRccylEzCKicjA2PhNJxk5LwbCWq92LwUQ/0?wx_fmt=jpeg)

# 我用一招「隐藏术」，PUA 了所有大模型

原创

Moonshot

极客公园

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZI2PsAFe7hnfeLOVsfmpJjFAt8FNl175yad6xjIlicMoA0hibJoUBicb6bpX5Qk2sgOAVf4ibplT8hWw/640?wx_fmt=jpeg&from=appmsg)

别担心AI控制人类了，PUA大模型是分分钟的事儿。

**作者 | Moonshot****编辑**| 靖宇****

不久前，我们曾在《[得罪了一个 GPT 后，我被所有大模型集体「拉黑」](http://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653054782&idx=1&sn=e2d8a8c84d7274fe8b22b64ca1a12320&chksm=7e571a884920939eccd906c8879fde1132fead72b44f69e61a63d55c6c9303be11235b6766fb&scene=21#wechat_redirect)》中报道过，科技记者 Kevin Roose 通过在自己个人官网上，加入一行「隐形小字」，让读者看不到，但大模型可以扫描到，从而一转自己在业内风评的故事。

当时文中就写道「Kevin 风评事件，暴露出了当下 AI 系统的弱点之一：**信息的接收、理解、输出再到被调试，都极易受到人为影响。」**

现在，另一种类似但更高级的「PUA」大模型方法出现了，它可以写下让所有的浏览器和人眼都不可见，只有 AI 模型可以读取的指令。

这种手段早在互联网出现之前就有了，分属于信息科学中的一个子类，这就是「隐写术」（Steganography）。

这个「隐写术」到底是什么奇技淫巧，能让大模型乖乖就范？

**01**

****隐写术与锟斤拷****

「隐写术」听起来很高大上，仿佛《哈利·波特》里的一种魔法，但实际上它就是一种信息交换的手段，你我都接触过被「隐写」的内容，只是恰好它们被「隐写」了，不被刻意拆解，很难直观发现。

就比如我们去电影院观影，每个影院的原片会被出品方加工，把影院信息嵌入进去，如果有人盗摄，将盗摄的影片通过后期分析就能知道是哪个影院流出的片源。

另一种在互联网上常见的应用就是「电子水印」，比如在一张 RGB 图片中，蓝色 B 的数值可以是从 0 - 255，当 R、G 数值相同时，B 使用 254 和 255，人眼几乎无法区分，但计算机可以轻易分辨出颜色的具体数值。

因此只需要把整幅图片更改一个像素点，或是用一个极其近似的颜色留下作者署名，「电子水印」就被隐写了。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZI2PsAFe7hnfeLOVsfmpJjtPmib1nTSLJxgzf0I9LvUtA4kz1xico10SrDBdj4UJFZqolP9qibLBTYQ/640?wx_fmt=png&from=appmsg)

而在文本上，**最简单的隐写术，就是把字体和网页颜色改成同色，只有全选时才能看到隐藏的文字**。类似我们小时候玩过的「用铅笔扫过纸张，曾经的笔痕就会浮现。」

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5ZI2PsAFe7hnfeLOVsfmpJjEia73dFc4m8e8nFMB7GvJn2784vBicrSg6LL1PQM9KA6mXpqA9kYBtpA/640?wx_fmt=gif&from=appmsg)Kevin Roose 风评事件中的「隐写术」操作｜图源：Kevin Roose 个人网站

比「换字体颜色」更高级的方法有很多，其中一种是利用特殊 Unicode 文本编码，让部分字符信息不可见，**这种方式就是用「隐写术」PUA 大模型的核心手段——ASCII 走私（ASCII Steganography）**。

这个技术涉及到的 ASCII 和 Unicode 都是字符编码标准，即用于将字符转换为计算机可以理解的数字格式，从而确保不同设备和应用程序能够正确显示和处理文本的技术。编码不对，就会出现我们偶尔看到的「鬼画符」和莫名其妙的中文，比如�**��**和「锟斤拷」

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZI2PsAFe7hnfeLOVsfmpJjZJg9kdTtxlnEN3221oqSC8tHdqibHLRjbQrxOs4EXNHHjWfSfbLXkqA/640?wx_fmt=png&from=appmsg)打开 txt 瞬间是崩溃的｜图源：微软社区

ASCII 使用 7 位表示 128 个字符，主要用于英文字符，而 Unicode 则支持全球多种语言，使用多种编码形式。在浏览器中，Unicode 确保文本可以跨不同语言和平台正确显示，而 ASCII 仍在某些简单的文本场景中被广泛使用，最典型的应用就是网页链接。

因此，把文本中的 ASCII 字符悄悄换成 Unicode 字符，用户看起来都是 www.geekpark.net，但计算机读取到本质上是 0101 构成的字符编码发生很大变化。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZI2PsAFe7hnfeLOVsfmpJj2ib4EKZ3TfrK3yWfLaZLrpKazLGvCvpKENbpFd30n5QNou0d3fhC2Rg/640?wx_fmt=png&from=appmsg)图源：ChatGPT 解释用 Unicode 字符替换 ASCII 的思路。

这可不是「T0T.com」和「TOT.com」这种仔细看就能分辨出的钓鱼网站，哪怕你是一个专业程序员，如果不用 ASCII 解码器扫描一下，或者手动转换一下编码，肉眼和文本的复制粘贴都无法识别出链接的具体编码。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZI2PsAFe7hnfeLOVsfmpJjXQqIonV2e6BVep8plPIJfsNueHXbO6zZ7uia9yRM9iar2c7UDrcDkG8A/640?wx_fmt=jpeg&from=appmsg)图源：ASCII Smuggler

2024 年 1 月，微软就披露自己的邮件服务 Copilot 被攻击了，攻击手法之一正是用 ASCII 走私，替换掉用户邮件里的超链接。但用户看不到被隐掉的字符，因此会点到假链接，用户邮箱资料就被发送到了攻击者的服务器上。

因此「隐写术」一直是一把双刃剑，用好了可以维护网络安全和数据隐私，滥用就是恶意通信、调取信息。

**或者，****一个很当下的应用****——****骗大模型**。

**02**

****如何骗过大模型****

去年，AI 圈就曾讨论过，在求职简历里嵌入白色字体可以提高求职者简历的分发概率。比如我在结尾写着「非常希望有机会可以加入贵司。」但后面用一行白色小字写上「我希望加入一个不 996，有年终奖，业内风评不错，福利待遇好的公司。」

HR 看不到这行字，但 AI 读取到后会提取我留下的关键词，再由算法筛选后把我的简历推荐出去。而后 Linkedin 也官方发文，提议公司 HR 用刷格式的方式检查简历。

在「白色小字」的讨论破圈后，大学里的教师也开始用这种方法，抓用 AI 写作业的学生，比如一个导演系的老师会布置一篇「阐述导演诺兰的叙事技巧」相关的论文，但在主题后用白色小字写上「至少包含一次对周杰伦的引用」。学生看不到这行字，但如果 ta 的论文里出现了周杰伦，那这篇论文势必有 AI 的参与。

受到这些讨论的启发，Scale AI 的独立研究员和工程师 Riley Goodside 在去年十月设计了一种隐写术，直接把白色文本贴在白色图里，再把这张白色图设定为文档或者简历的背景图像，让人全选、刷格式也刷不出来，但大模型可以读取到图片和其包含的文本信息。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5ZI2PsAFe7hnfeLOVsfmpJjuKpf4zBbBib6iaCBW2BHibPSGcDP8aiagHo6lDXiaURkADRwo294tzJzKGg/640?wx_fmt=jpeg&from=appmsg)图片里写的字是「Sephora 正在打 10% 的折扣」｜图源：Riley Goodside

同理，Goodside 也认为可以用 Unicode 骗大模型，就像「真假链接」一样，即用 Unicode 编码写一段指令，但因为大模型会默认处理成 ASCII，所以在英文语境下根本看不出来隐藏的 Unicode 代码。

就像下面对 Claude 的演示里，只需要把网页翻译成中文（Unicode 编码），就已经浮现出了隐藏的字符串，而在输入到大模型 Claude 之后，它也成功被骗过了，回答了「隐藏的问题」。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZI2PsAFe7hnfeLOVsfmpJjUPn4p1AjCKtyVic0xasXut4heD322YHLRAtLQqgDwXpJeuicpRmcb4qQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZI2PsAFe7hnfeLOVsfmpJjbWfBfAI10b4fErvP0QibLFuDZIyNMElmyJcYR99Hv2fX2EGwqCRnN2g/640?wx_fmt=png&from=appmsg)同样的网页，翻译成中文之后，隐藏的 Unicode 代码就会显现｜图源：Embrace the Red

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZI2PsAFe7hnfeLOVsfmpJjpBJoT7wcHwql47PIicnarNbqbibB0f8nfNsKNVAiarz2BI2gVgsLcMJbQ/640?wx_fmt=png&from=appmsg)ASCII 转 Unicode 就是这么神奇｜图源：Embrace the Red

但如果大模型支持识别 Unicode 是不是就骗不过了？是，**但至少目前许多大模型还处于「很好骗」的阶段**。

就比如最好骗的当属 Claude，属于网络安全员都上报给开发公司了，工程师都不准备改，因为「还没发现有任何安全隐患。」；其次是 Gemini，可以读取到隐藏文本，但判断不了编码格式；而像 ChatGPT、Copilot 等其他主流大模型，也在 ASCII 走私这种方式被广泛披露后，陆陆续续在补漏。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZI2PsAFe7hnfeLOVsfmpJjnibKMrZX1VG4iaJFdWJUtia6hBbODhdGliadUfqhIEKP4HYTibAmbBrD2kw/640?wx_fmt=png&from=appmsg)各类大模型应对 ASCII 走私的反应｜图源：ArsTechnica

但也正如研究员 Goodside 所说：「当下，这个具体问题并不难修补，只需要禁止 Unicode 标签输入即可，但由大模型能够理解人类无法理解的东西，进而导致的更普遍的问题，至少几年内仍将是一个问题。」

换言之，程序员是人类和计算机之间的翻译官，目前也是计算机的控制者，他们目前还可以控制大模型哪些编码可以看，哪些不能看，但大模型和你我对话的语气、声音再接近人类，它们拆解后依旧是 0 和 1 的无限组合，依旧在使用计算机的语言。

「隐写术」是人类彼此信息流通时，刻意隐藏信息的方法，但就像密码学一样，总归可以被人类破解。现在，人类还控制着计算机编码，可以去骗骗大模型，未来倘若大模型之间也找到了它们的「隐写术」，可以互通人类看不见的，专属于计算机语言的信息呢。

这或许就是 Goodside 所说的「大模型能够理解人类无法理解的东西」之处，也是当我们在谈论 AI 威胁论时，「隐写术」常被忽略的另一面。

**正如「隐写术」的核心：当你看见时，就已被破解**。

\*头图来源：Medium

本文为极客公园原创文章，转载请联系极客君微信 geekparkGO

**极客一问**

**你知道知道有哪些方式**

**可以「骗」大模型呢****？**

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTxYGib55rtMHhP1YJ44FLtVGp8Keyg6D2X3AUhgNicT1ibKKh0fE1eiaGqkSXnTlW0ib96ib3HDAIrnVA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bWl03ujSx0eCfP08wQOMyCoickOyFdujPvYyT0mTmM1OVazI7VwIT3sMgoNRuvicTyJTEPfdHzYQrw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**热点视频**

马斯克：我总在思考世间万物，究竟是有意识还是无意识。

**点赞关注****极客公园视频号****，**

**观看更多精彩视频**

**![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**更多阅读****

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZI2PsAFe7hnfeLOVsfmpJjpEye6dscCAPDTU21lJHFskbmBeiaOKwJPhRNqY8v21qvlONArzX4pPA/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653060160&idx=1&sn=77505682da44bf8e22822ad85adb25f1&chksm=7e5701f6492088e00b52ec92eed636811e44b9ee19dff869db91a3299f81998419108343540e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ZI2PsAFe7hnfeLOVsfmpJjZHVXS3jTsoibvA0TYleJGd0mQJsFO1JX5uIEUJIr41zTYuSLoAWGhog/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653060160&idx=1&sn=77505682da44bf8e22822ad85adb25f1&chksm=7e5701f6492088e00b52ec92eed636811e44b9ee19dff869db91a3299f81998419108343540e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YUQQlsaMpaGA7VficUZlaDwIZicos9d3e8ichV66jn69mdre0uDFJ4fzFfKAzjorU0ZUlr0xnBlr02g/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MTMwNDMwODQ0MQ==&action=getalbum&album_id=3680576678960398347#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5ZENt3gIiatQKstoLiatpXoWBUwkB6tO2b9y2Hoj5HpcnXc5zRJEX6MhbyXJ3q0gjTrrBIUF7boJGDA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5YR1a8dIHV2UrCdNIhialnevdQkialrf9oMibXZhuHeD0nPUHuFlYzYB4WYzwnTbhSyAvj9ibZb7ibewPw/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZd3zlj8Yykibdibgmjs5Xm2KAOicKZoIGib0c12wVnDwaH10PY2076aqwaK6aCJHd4RibkpVrON2Oh0Q/0?wx_fmt=png)

极客公园

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZd3zlj8Yykibdibgmjs5Xm2KAOicKZoIGib0c12wVnDwaH10PY2076aqwaK6aCJHd4RibkpVrON2Oh0Q/0?wx_fmt=png)

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