---
title: 电子取证初探——六种常见图片隐写
url: https://mp.weixin.qq.com/s/Om6pVYOMXYsgfdKQVZUsBg
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:52:10.420291
---

# 电子取证初探——六种常见图片隐写

# 电子取证初探——六种常见图片隐写

原创

是羊羊羊呀
是羊羊羊呀

羊羊羊的forensic

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwVJwdhUCRpoIQo9fGbybkK60s9IiahiaS7ZnGaKZP2zScl8CXm9UiaHT3XcxLnvgMsibHW1SccOA06SZ9O80g6AQh9TLhBF5Wev4Bs/640?wx_fmt=png&from=appmsg)

**引入**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwUibgeLatNuMdWKQhIxicswSdMibrI3pyrKYVqYxWrV4CSibwOMPqN2xeYDsd13PUKTwrcf1TuArma3JTQFoE8pup9rOFSO6QjRiacw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwXX5DbWhdwgEsKb5q1MZMiaGoLTw6vRNFcpuF2l0taN7RbCEe9g1M6xmbskVjACVM8ZiafFEiav5TAoR6LbBQdlLgLRBHFPHcpPOM/640?wx_fmt=png&from=appmsg)

一张照片里，除了你看到的画面，还能放进别的东西吗？

可以。一段文字、一个压缩包，甚至另一幅黑白图，都可能藏在其中。图片照常打开，并不意味着里面只有画面。

所以，今天本文用下面同“一”张图片，介绍六种常见的图片隐写～

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZXQtRibNoDwXfxVMvhz6VUkjUdwhuibeUXJt8GrqRJ24UecDdcba0Z0KSUxaFQm3XGTRCpVmk1Oia4AAE6qaQbpyrqlAmB0maLHutQxeib2nhXo/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwXb6jBek6mTx3u0nOZRYkUdhHKfnWT305LRachFRYRZYtUibc49Qn1vlsuPAaA87SBwh9u5MY9iaHibRlPFABR5oueXR0KckuezAE/640?wx_fmt=png&from=appmsg)

**开始前，先介绍一下图片的基本参数**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwUTciakQsfHpu4CSXjZbqHTQ2libWjaTVQnzIEpGZicBibV6x1w9tUibgQkrcf3LibdibGvo2rJmLvhj2gJ1r8OxVeKMp50zjLRRz48hk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwUKVLQUUNxEbe1uJAOeO1FHmJwIkzmCesIPdKbMl4bibMRsUQrYPk8UTrIOyWIQfuPeQLrDs5I0fzibnHxxa6ib6DKIH5BNZ64qYc/640?wx_fmt=png&from=appmsg)

人看的是图片，电脑看的是文件。

把一张图片放大到一定程度，画面就像许多小色块拼成的马赛克。这些小色块叫像素。

电脑保存图片时，并不是直接保存“这是一只玩偶”这句话，而是按照一定的格式，把数据写进文件。看图软件读取并解码这些数据，才把画面显示出来。

所以，同一张图片可以从两个角度观察：

**1、看文件结构：** 文件里有哪些标记、备注和数据？图像结束以后，还有没有其他字节？

**2、看解码后的图像：** 每个像素的颜色是多少？有没有透明度？某些细小变化能否组成信息？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwU2dibT5xGpgx34iccPTye88lMDnsV1VwMpeiby3CPjh1ncyT0m27MiaHxq6YicgynqbicINGIgYBHPaBFgFLYMC4ibUSVINpHTpedEZU/640?wx_fmt=png&from=appmsg)

例如，PNG 文件中的图像数据经过压缩，不能直接把文件里的“第一个字节”当成“第一个像素的红色值”。

工具需要先读懂格式、解压数据，才能分析像素。

本次实操的前两题主要看**文件结构**；第三至第五题**观察像素、透明度和调色板**；第六题进入 **JPEG 压缩使用的系数**。

每到一种方法，我们再解释这个对应的一些概念。（其实是我不想整理在一起）

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwWrtnNLic2BeZvibzb1icickiaXwhCcNmFgDnwzA8XntuqoQbwyicFAic7aEKiaCYtgKbYkVpvFDzj9OxYwYg9aeNFjsCjyFp3HODGYNTQ/640?wx_fmt=png&from=appmsg)

**一种常见的编码——Base64**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwWXnCT6STKgEzpcuDtzbF854FlDR2ibpcNfotpTGXyic1s3eL4zDhr2cia7jH639sgo4C0cslQHyZEqick45nuZx28lWLROr2WCAv0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwVkeSf0aO6R7gcUIB68RV8sC6buAU0Uu9ibSk7HLafBiaqXbjYafpayfMmMAj8icrzCTDXb5nIP4uf7CCoY45wMXQO69BhiaibUW7eo/640?wx_fmt=png&from=appmsg)

有些题目提取出来的内容并不是可以直接阅读的答案，而是一串类似下面的字符：

**ZmxhZ3tkZW1vfQ==**

这是 flag{demo} 的 Base64 编码。

编码可以理解为“按照公开规则换一种写法”（有点类似于战争的密码本？）。

Base64 经常使用大小写字母、数字、+、/，末尾有时会出现用于补齐的 =。

并不是所有 Base64 都以 = 结尾，也不能仅凭外观就确定编码类型。（但是可以去试试）

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwXZhPcHX3jw5z6MWicHLlbq7Wtjw5sMy7r6HiaKuWu4ZX89TuAkKeLXS6FylT2yWaSY0szeyyYRcUxvibxMyFjQ7ZGRia5pwl0TibGY/640?wx_fmt=png&from=appmsg)

**介绍一种工具——CyberChef**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwVpts8L6ibfdnE8iaqqr8YQibHicQsr661ic6dkbkleibcYde66PibiaTk1QnL4dR2lKjAJPy1ZjjXIYQaubJaM0oSJP53l93FSKwmmY2g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwXlyWQfI3Btvk95nh5uia3RWic1Pw5yomhdpEpP1gCeQfRdfSLuAXgodlXzgHevO2mcpNv0LrBIU40263f7HnVIlF3DT9ciaiaGIbA/640?wx_fmt=png&from=appmsg)

打开网页，https://gchq.github.io/CyberChef/
不难看出来有4个区域。

**左侧找操作，中间排步骤，右侧上方放输入，右侧下方看输出。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwXg4tXZTaBlxaKFJa5XODOB3hrqoYRaiax5LZfqaicb94pwFxbViboX6oZ7h3u9WwtnGom1gOrUbczfUCml5tmcrxHaZtJENIOsZo/640?wx_fmt=png&from=appmsg)

下面，请你动动小手，跟着操作一下。

1. 在 Input（输入） 区粘贴上面的 ZmxhZ3tkZW1vfQ==，不要带上引号或代码框。
2. 在 Operations（操作） 的搜索框里输入 From Base64。
3. 把 From Base64 拖到 Recipe（配方） 区，也可以双击操作名称。确认 Recipe 里只有这一个操作。
4. 保持 Auto Bake（自动执行） 勾选，Output（输出） 应出现 flag{demo}。没有自动执行时，点击 Bake!。

这就是“解码”。后面的题目会重复使用它。换**任务时要清空旧配方。**

比如刚刚读取过 EXIF，接下来解码一段文字，应先把那段编码复制到新的输入，再只保留 From Base64。不要把整份元数据报告直接接到 Base64 后面，否则字段名、说明文字也会参与解码，很容易得到乱码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwWtQEkA9QqgJ3O1vDXk3ZKdyg17P997AtpkvaYn9icewiav5wdgOFLxgUPfd0vHiciaUibrjcqyUyeKA2sM0tSYaic07S3avpueVUCWU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwUEFXmhETgsZl9uIwwel9he81n46aAWZ998Rl3pjCNASywY96KXia6YsdqOOghwKFpsbRudtFiaPLoYUwibjvBXWaOrjRBEYFHqas/640?wx_fmt=png&from=appmsg)

**题型一——EXIF**

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwVLnmicdEicde0dRPno4KYZJyXPRf6OPwq1XuqZTFicFEhTfJ7akg7ooW5NWE6I6j9zia1xica2WRlLib3s2wKoNt0CQWDexs2ichDClU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwXZQ1Ars7rTuYa3jOFZedAaiaAiaa3ciaCV6kRLhkKYtzb8KeIq6YEAIqGZ3dxj8xhXNOscC3jTicapHG0Mg4g36icKdn2JlafVLxZ4/640?wx_fmt=png&from=appmsg)

手机照片可以记录拍摄参数、软件名称、图片描述等信息。这些关于文件的信息叫元数据。其中一种常见组织形式叫 EXIF。

你可以把它理解为照片附带的一张资料卡。看图时通常只显示照片，资料卡上的内容需要另外读取。如果有人往“图片描述”字段写了一条消息，它就不会直接出现在画面上。

图片里的文本也不只存在于 EXIF：JPEG 可以有 COM 注释段，PNG 可以有文本数据块。本题先练习 EXIF 中的 ImageDescription，意思是“图片描述”。

下面进入实操

目标：找到描述字段里的留言，再还原 flag。

1. 新开一个 CyberChef 页面。在 Input 栏点击 Open file as input，选择练习包里的 01\_照片的备注.jpg。也可以把文件拖进 Input。
2. 搜索 Extract EXIF，将它加入 Recipe。此时先不要添加 Base64 操作。
3. 等待文件载入完成，在 Output 找到 ImageDescription。本题的字段值以 memo=base64: 开头。
4. 只复制 base64: 后面的那一串字符。新开一个空白 CyberChef 页面，把它粘贴到 Input，再按前面的步骤使用 From Base64。

如果恢复出了完整的 flag{...}，说明两步都做对了：先从元数据中找到内容，再按照编码规则还原文字。

Strings 操作也能帮助寻找文件里的可打印文字。不过，搜到字符后，还应确认它来自哪个字段。“在哪里找到的”是这道题的一部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwX9mFxETlCqmZaxGorlFbeiaRzib2m7QNFemQAsXKwTMBVNNdnkveiapK5lEHVqypxrCmxLvUMmVvwoXboAtjfDUnYW5KhBJvzoWc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwUxWHaW4yC68BwSxIUMvsyYaZVbdCOarpzxxNS1cXVAWlKcBu8fFFdlCmN3tR1xeMC1ofo85Nt46vlOGZDEq03ZSmG84SgyGiag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwV6QiagXpICqUU0ibuPYNYktiacESPIg56CJNqBc6lIWqicE9YfVia3nYBjrUVunYRn7EsvTVXtyibiaLhUXcGcRc5yLJVuIHKYdpJHoI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwUn5qWlRv2gINoKRA9rtTRRmxHTMd7EtAGzwLyl9iaIpdDLX3wqknJKLGGJ3IGDGI8VDY4xSaBgoIQJR3fTM9Qjwibiaa888mn5Y8/640?wx_fmt=png&from=appmsg)

**第二种题型——十六进制后接文件**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwX2HPNpvf5syaZaKibZTXqtkxvZc3ibYRrs6r2MY5ZzK1OJKc9Hf0iadXD7CAdEddDT9VWBGsFTibAco31az9DicPnDj58hibSWIVbKo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwWSGzKOHy3rNib26Pyl4vvKeeDBC7dKvbuhViaJAtvqztJib79fxyRTAicpZO3bTe7GhLYAOc0sG8qWG52pYYSLKEOZwnafy3SdeK4/640?wx_fmt=png&from=appmsg)

之前有推文讲过，jump

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwXPlls89zGOOeW34WhcVVlCvdT98iccCUSPOicAhOL4CmuTo5L0ktJLu7RwkNPg71GnkwH93ePyQC7SMca8ibvKVxH0gGlJk3JciaU/640?wx_fmt=png&from=appmsg)

**第三种题型——LSB**

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwVGRamT9D2jNd3BDiaFKgGcTrRW94g3spFeUQwczM8ZricKtu5icVKUiaGvMBcicKd1Bu7leQl0dkLyyWHh9V3FVYBZ8lwbUXIzJQck/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwW30lRp9zDGEhqbGWX0E9AUQibFYib2AePXKhP4AsHaNVHsvyLrBG7iaSh9sbAa0o0rbLPe5EElTYqTOxKvnNYx1Sh1ftjB3vNluA/640?wx_fmt=png&from=appmsg)

常见的真彩色图片用三个通道描述颜色：R 是红色，G 是绿色，B 是蓝色。在本题采用的 8 位通道中，每个值都在 0 到 255 之间。

假设一个像素的 R 值是 154，只把它改成 155，变化很小，肉眼通常不容易发现。用二进制写出来，两者只差最后一位：

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwVkPKvRSsPlZN6sNQ5Hq47IEEO5SrLic2XURRWTTSkm0V0ic0A8sOJXM2IwT96W9up8TyqpjmtOo3xN5rRRSlSsjbl1uELHR58fk/640?wx_fmt=png&from=appmsg)

最后一位叫最低有效位，英文缩写是 LSB。它对这个数值的影响最小：改变它，数值只会相差 1。

于是我们可以约定：这一位为 0，就记录一个 0；这一位为 1，就记录一个 1。连续读取 8 个像素中选定的位，可以拼成一个字节；很多字节又能组成文字或文件。

这只是最容易理解的顺序嵌入方式。有些 LSB 算法还会改变嵌入位置或通道选择。

实操

目标：从红色通道取出位流，再对其中的编码文本解码。

打开

https://georgeom.net/StegOnline/upload

，点 UPLOAD IMAGE，选择题目 PNG，然后进入 Extract Files/Data。

页面会出现 R、G、B 三列和编号 7 至 0 的多行。按下面设置：

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwUiasXZic9AIj5hbBiasFO0ADRSSibrsVDvdlLftZgLdveW2BEcSdyUMPKibKJtgw1iaP0XJ799dia7AmoibA1vIDRMRzOb39RjghTbw4k/640?wx_fmt=png&from=appmsg...