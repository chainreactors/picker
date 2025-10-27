---
title: iPhone 屏幕好在哪？OLED 次像素渲染深度解析
url: https://buaq.net/go-135312.html
source: unSafe.sh - 不安全
date: 2022-11-13
fetch_date: 2025-10-03T22:36:17.996625
---

# iPhone 屏幕好在哪？OLED 次像素渲染深度解析

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

![](https://8aqnet.cdn.bcebos.com/d5361c035370471c7a1564d88bc2481a.jpg)

iPhone 屏幕好在哪？OLED 次像素渲染深度解析

视频：iPhone 屏幕好在哪？OLED 次像素渲染深度解析 Hello 大家好，欢迎收看这一期的 Apple 护城河视频，我是初号。我们频道之前用了好几期视频，给大家分享了几个 Apple
*2022-11-12 11:5:18
Author: [sspai.com(查看原文)](/jump-135312.htm)
阅读量:37
收藏*

---

![](https://cdn-static.sspai.com/ui/img-placeholder.png)

视频：iPhone 屏幕好在哪？OLED 次像素渲染深度解析

Hello 大家好，欢迎收看这一期的 Apple 护城河视频，我是初号。

我们频道之前用了好几期视频，给大家分享了几个 Apple 产品在显示效果上做的比较好的地方，像是色彩管理，可以根据图片或者视频的配置文件，在正确的色彩空间下进行渲染，再比如 local HDR，可以利用 OLED 或者 miniLED 高亮度的特性，让图片或者视频能够尽可能还原出当时场景的亮度。没看过的朋友强烈建议看看之前这几期视频。

![](https://cdn.sspai.com/2022/11/11/dbc9fa90dc3f89862d8f0407063bc593.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)![](https://cdn.sspai.com/2022/11/11/8ed36e80ba7f598a14d216ab68f68336.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

但其实不知道大家有没有注意到一个问题，那就是这俩功能本质上是在干一件事，就是创造一个亮度和色彩都足够大的容器，把可以把所有内容统一转进来，再转换成屏幕接受的数据格式，因为对于屏幕的像素来说，他只接受一种数据格式，那就是 RGB 信号和当前的亮度，这部分是在系统中完成，不需要硬件的参与，我愿称其为操作像素的艺术。

但我们今天要分享的主题，则要比这个更加底层，因为我们都知道，内容当中的每一个像素，到屏幕上实际需要 RGB 几个像素来混合显示，这就是屏幕的次像素或者说子像素。

那次像素是如何被驱动进行显示的？OLED 和 LCD 之间的区别在哪？ Apple 在这又有什么积累？那接下来我就来好好讲讲。

![](https://cdn.sspai.com/2022/11/11/ecce9a15c62b578d5cc2b8ffe2c0d6b5.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

## 次像素渲染

先给大家做一点简单的科普，OLED 的像素并不是 RGB 1:1:1 的，像主流的钻石排列，红蓝就各少了一半的像素，这时候如果显示一个白点，只点亮 RGB 三个像素可能就不够，还需要从旁边借像素，来确保颜色和形状尽可能的还原，这就是**次像素渲染算法**。

做得好可以让你感觉不到 OLED 缺少红蓝像素这个先天的劣势，做的不好那就会出现模糊或者锯齿，看起来不够清晰。所以这个功能算是那种，做的越好，你反而越没有感知的一个功能。

![](https://cdn.sspai.com/2022/11/11/175092050dd6c5f0779ac0b17f2a5076.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

但大家可能不知道的是，尽管 LCD 是标准的 RGB 排列，他也需要借助类似的手段来平滑曲线或者圆角，像 Windows 有 ClearType 和整数缩放，Mac 这边有 HIDPI，都是在解决类似的问题，这些功能可以由软件来自定义，适配不同的显示屏，但是移动端由于功耗限制更加严格，所以类似的算法必须固化在硬件中，这个硬件就是显示芯片，又叫 DDIC，他不太起眼，藏在显示屏的背后，但是一般看楼斌老板的拆解视频，都能找到他的身影。

![](https://cdn.sspai.com/2022/11/11/41e076a2670cfd3195870f5b872fb803.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

视频在 B 站被热心网友指正，这个框里圈出来貌似不是 DDIC，DDIC 在图中左边的封装内（待确认）

这也是软件端能控制的最末尾，软件系统是不能通过命令单独点亮一个「次像素」的，只有 DDIC 才有这个功能。所以不管聊显示的什么内容什么算法，最后可能都绕不开这颗芯片，今天先简单介绍下，未来我们的视频可能还会提及他。科普完毕我们进入正题。

![](https://cdn.sspai.com/2022/11/11/919fdde645beb4e4c44c588bb2d43acb.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

DDIC 功能

为了这次给大家演示次像素渲染的效果，我还把放弃多年的 html 开发捡了起来，手写了个测试次像素渲染的网页，在这里也感谢 Navis 老师提供的创意，之所以用网页而不是图片，是因为每个设备的屏幕分辨率不一样，有 1080P 的、有 2K 的、还有 Apple 这种非标准分辨率的，要保证各个设备显示测试图案的大小接近，使用一样的字体，且不受图片压缩带来的影响，用代码画出来是最靠谱的，这个图虽然看着比较简陋，但是效果已经达到了。

![](https://cdn.sspai.com/2022/11/11/de0d0cea7c26b51880a19504018283e9.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

[测试页面在这](https://temp.sspai.com/spr-test/index.html)[里](https://pan.baidu.com/s/138c4KzwMRWR0afRdTqCLcA?pwd=hc9d)，实现得很粗糙还望各位开发大佬轻喷，大家可以试试在自己手机上显示的效果。那这里再提醒一下，次像素渲染的算法实际上是 DDIC 芯片厂和屏厂一起来完成的，所以这里本质上是三星屏和国产屏、LCD 和 OLED，以及不同分辨率之间的区别。

所以请大家不要纠结我是在用什么型号的手机，这个跟本次测试其实没有关系。那我们先来看看 1080P LCD 屏幕的表现。

我们先看测试图案的上半部分，乍一看显示效果非常好，文字清晰不发虚，这些间隔 2 个单位的直线斜线，也都能分辨出轮廓，毕竟是 LCD 嘛，基础效果肯定是没问题的，但是往下看图标的显示效果，比如说新建便签的图标，左右和上下就出现了宽度不一致的问题，再看看耳机图标头梁的部分，也有明显的锯齿。

![](https://cdn.sspai.com/2022/11/11/cc5b41afc4fc630676c664ad6ea03334.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

我们用显微镜放大看看次像素渲染实际的情况，那些半亮不亮的像素，就是为了显示平滑而从旁边借的像素，但 LCD 借的都是完整的 RGB 像素，不能借单个次像素。在便签这个图标中，其实不用借像素，也能把图标显示完整，借了之后反倒多余让四边不等宽，而耳机的图标这边，你能看到处理的又不够激进，尤其是头梁的上边缘，并没有借用，导致曲线看起来就不够平滑。

![](https://cdn.sspai.com/2022/11/11/ffd3efcf36c89b8b18da63135a9afd0b.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)![](https://cdn.sspai.com/2022/11/11/54406d464381b56ac01f329490356431.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

然后我们就着这两个图标，再来对比一下 1080P OLED 的表现，并且把国产屏和三星屏放一起看看区别，首先便签图标好像有着一样的上下左右不等宽的问题，这里国产 OLED 的表现似乎还好一些，但是耳机图标的曲线，三星 OLED 看起来会更加平滑，并且比 LCD 表现更好。

![](https://cdn.sspai.com/2022/11/11/804c2c78cd4cda6af455ddde84731dd3.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

我们对比显微镜下的表现，国产屏在借用次像素时，上边缘的曲线向下多借用了几组像素，并且红色像素很亮很显眼，侵占黑区太多就中断了曲线的连续性。

![](https://cdn.sspai.com/2022/11/11/eadbe84a56a4f7ae5c8e6030f6b014b3.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

并且如果回到测试图，看下排的大图标，三星屏仍然有优势，但是国产屏在显示文字的时候扳回一城，看起来会更加锐利，借用像素导致的边缘彩边现象更少，算是有益有弊吧。

![](https://cdn.sspai.com/2022/11/11/614ac38b0abdfbc97b4f30d1d81aea81.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)![](https://cdn.sspai.com/2022/11/11/32bd0a928c0bc42e407b63bbf0d132d2.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

并且从这也能看得出来，**只要次像素渲染算法做的好，OLED 跟 LCD 差别已经并不明显，甚至有些场景，因为可以更精细的控制次像素对边缘进行填充，OLED 在平滑度上还要好于 LCD**，OLED 已经不是当年的 OLED，这就好像 CMOS 当年各项素质也是不如 CCD，但最终还是把 CCD 淘汰了，确实是时代变了呀。

![](https://cdn.sspai.com/2022/11/11/e9d96e19f6de6ead32ff0ffb9be76363.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

然后我们再看看两个 1.5K 和 2K 级别屏幕的对比，这里姑且按照红米的说法把 iPhone 也算成 1.5K，首先这一轮三块屏在清晰度上，相比 1080P 的屏幕都要好上不少，尤其是直线的辨识度上，因为像素密度更高的关系，次像素渲染算法有了更多发挥的空间，甚至显示一个单位的点，都要比 1080P 的更清晰。

![](https://cdn.sspai.com/2022/11/11/ace9ef0b88354a50426c31c28232b6d2.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)![](https://cdn.sspai.com/2022/11/11/a88e7c00b702a82e60a27b90a81fb3f8.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

在显微镜下观察，这是 1080P 屏幕的点，这是 1.5K 国产屏的点，这是 iPhone 的点，而这是 2K 三星屏幕下的点，从这可以发现，1.5K 确实是一个分水岭，显示出的点更接近一个正方形，我们再看看 1 个单位间隔的绿线，他们中间的分界线，也都比 1080P 的屏更加明确。

![](https://cdn.sspai.com/2022/11/11/ec3345acee76b18224212e1a2b026d75.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)![](https://cdn.sspai.com/2022/11/11/4a075c3291b2a9c434a6c790205f331d.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

如果说到这三块屏难分秋色的话，那再往下看图标的效果，iPhone 的优势就非常大了，便签图标四边等宽，耳机图标极其平滑，这个甚至超过了分辨率更高的 2K 屏。

![](https://cdn.sspai.com/2022/11/11/b7b905eb96839442af36151f15e0486a.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

放大看细节，iPhone 在黑色区域调用了更多的次像素进行填充，不发光的区域最小，但是跟国产 1080P 屏不一样的是，填充的次像素亮度很低，平衡的更好，所以最终肉眼看上去，曲线会更加平滑。

![](https://cdn.sspai.com/2022/11/11/e4668fec1663ad73cc62047ee845fd48.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

其实看到这我们可以做一个小结了，1080P 下 LCD 屏幕跟三星的 OLED 各有优劣，但都略好于国产的 OLED 屏幕，主要体现在 LCD 字体更加清晰，但三星的 OLED 曲线处理更加平滑，而到了 1.5K 这个级别，国产 1.5K、iPhone 和三星的 2K 表现大体接近，但是在图标显示的平滑度上，iPhone 展现出了相对明显的优势。

当然啊，我这里的测试图属于非常极端的条件，是专门为了找问题而制作的，实际大家在使用手机的过程中，内容本身的清晰度差异可能远远大于算法的优劣。但还是得说，这两年国产屏的飞速发展，显示效果已经非常出色，**早些年三星钻排屏幕清晰，显示效果好的优势再一点点被抹平**，尤其是我在 K50U 的视频中说，1.5K 屏在中端产品上代替 1080P 屏幕一定是大势所趋了，今天的测试结果也侧面证明了这一点。再就是分辨率高并不一定清晰，次像素渲染算法能把清晰度的优势给抹平，甚至反超。

![](https://cdn.sspai.com/2022/11/11/d703ceb4eb57ebaac09e4520d268e8af.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

这里又要类比相机了，好的 CMOS 只能决定下限，配合上好的算法和调试效果，才能拉高整体的上限。我估计有朋友可能会说，这都太极端了，我觉得 1.5K 都挺好了，反正实际用也看不出啥区别。我相信大多数人应该都是这么想的。

确实作为一期护城河的视频，如果只挖到这一层，Apple  的优势似乎还不够明显，但你说，Apple  每年找屏厂独家定制的屏幕花那么多钱，他到底厉害在哪呢？是不是还有什么细节我们没有发现呢？

## 能力展现

这时候大家再仔细看看 Apple 的屏幕，不管是对比 1.5K 的国产屏，还是三星的 2K 屏，你们有没有发现 Apple 的像素好像更大一些，像素看起来更密集、间隔更小？其实不管对比哪个 OLED 都是一样的，iPhone 的屏幕，像素就是最大的，**这个东西的学名叫做像素的「开口率」**。

开口率做大有很多的好处，比如说同样的电压，开口率大的像素亮度会更高，反过来说达到同样的亮度也会更加省电，对屏幕的寿命也有一定的提升。

![](https://cdn.sspai.com/2022/11/11/bc7bb49e345b28b7570093a327a18c74.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

不知道这时候会不会有朋友问，**为什么开口率做大有这么多优势，连三星自己的 2K 屏幕都没有跟进，只有 Apple 是独一份呢？**

说实话答案其实很简单，那就是良率和成本。OLED 屏幕的生产是通过蒸镀的方式固定像素位置的，RGB 三种像素对应要做三次蒸镀，每次蒸镀会用到一种掩膜，像素透过掩膜落在基材上就算固定成功，所以为了保证良率减少坏点，掩膜的开口要比像素稍大一点。

![](https://cdn.sspai.com/2022/11/11/878bdb7442339324e44169517d7587a0.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

**但是如果像素开口率很大，像素又很密，掩膜开口大小就很矛盾，弄小了像素固定不到基材上，就变成了坏点，弄大了落到了旁边像素上，颜色就错了。**总之这是个行业难题，我不知道 Apple 到底花了多少时间和成本解决了这个问题，但最后的结果是，Apple  的屏幕在三星有完全独立的生产线，并且 iPhone 屏幕的亮度成为了行业标杆，功耗还做的很好。这可能就是钞能力把。

![](https://cdn.sspai.com/2022/11/11/845b95cd0f825bda71b5d03c0762e559.jpg?imageView2/2/w/1120/q...