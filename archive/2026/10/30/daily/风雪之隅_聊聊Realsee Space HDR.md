---
title: 聊聊Realsee Space HDR
url: https://www.laruence.com/2026/10/30/7736.html
source: 风雪之隅
date: 2026-10-30
fetch_date: 2026-10-31T07:46:52.764239
---

# 聊聊Realsee Space HDR

[Press "Enter" to skip to content](#main)

[风雪之隅](https://www.laruence.com)

左手代码右手诗

open menu

mobile menu toggle button

* [主页](http://www.laruence.com/)
* [PHP源码分析](http://www.laruence.com/php-internal)
* [PHP应用](http://www.laruence.com/php)
* [JS/CSS](http://www.laruence.com/jscss)
* [随笔](http://www.laruence.com/notes)
* [留言](https://www.laruence.com/guestbook)
* [博客地图](https://www.laruence.com/sitemap)

# 聊聊Realsee Space HDR中文EN

Published on [30 October 2026](https://www.laruence.com/2026/10) by [laruence](https://www.laruence.com/author/laruence)

* 本文地址: [https://www.laruence.com/2026/10/30/7736.html](https://www.laruence.com/2026/10/30/7736.html "Permanet Link to 聊聊Realsee Space HDR")
* 转载请注明出处

前俩天发了一篇PHP漏洞原理分析的公众号文章, 阅读刚过3万就被删了. 最气人的是，不告诉你具体为啥，还不给你任何申诉的途径。

今天不聊PHP了, 聊点别的, 过去半年我们(如视)做的一个工作, 我觉得挺好玩的: **Space HDR**.

## HDR

什么是HDR. HDR(High Dynamic Range, 高动态范围)这个词, 大家应该都不陌生了, 手机拍照界面上的那个HDR开关, 相册里的HDR标识, 这几年已经是基础设施了. 不过大家平时理解的HDR, 可能是不完全的. 拍照时候的HDR, 说的是一种技术手段: 相机对着同一个场景连拍几张不同曝光的照片, 欠曝的留住亮部细节, 过曝的留住暗部细节, 然后合成一张明暗都看得见的照片. 这个理解没错, 但它只是采集那一环.

一个真正的HDR, 是需要全链路支持的: 采集的时候要记录下足够宽的亮度范围, 存储和传输的时候要有能力承载这个范围的数据, 最后展示的时候, 屏幕要能把亮度真正放出来. 任何一环不支持, 到你眼睛里的就还是SDR.

所以大家经常看到一些照片, 明明号称是HDR照片, 但是在网页上看, 还是窗外亮成一片白, 暗处黑成一团. 因为Web分享的时候, 结果还是被"压成了"SDR.

要理解SDR和HDR的区别, 得先说"光"的亮度单位: nit(尼特)， 看一张图:

![](https://www.laruence.com/medias/2026/10/HDR亮度范围对比_v14.png)

图1: 亮度范围

为了更形象的理解：阴天的天空大概是200nit, 而太阳的表面, 是16亿nit..

在过去(SDR时代), 屏幕能展示的亮度范围, 一般在0.1到100nit之间. 也就是说, 我们拍照的时候, 需要把真实世界巨大的亮度范围, 压缩到这俩个数之间来展示. 过去SDR的时代, 从采集, 到存储, 到展示, 全部是以这个为标准.

而随着当代的屏幕能展示的亮度越来越高, 比如某品牌前段时间发布的手机, 号称屏幕瞬时亮度可以做到16000nit, 那就需要在采集的时候记录更多的亮度范围, 存储的时候需要更多的位宽来存更大的亮度范围, 展示的时候在支持HDR的屏幕上, 才能展示出真正的HDR.

链路上采集, 存储, 封装这些, 我们过去几年一直在做, 这次的工作, 主要是展示这一块: 把HDR真正送到浏览器里的屏幕上.

先从采集的设备说起.

## 0x1 伽罗华

如视的空间智能相机叫伽罗华, 最新一代是P4，它现在已经被广泛应用于贝壳的VR看房，美团的餐厅预订，以及各种展厅展馆，文物保护，甚至还有犯罪现场记录，比如香港警方的防爆科的阿sir们，就用的是我们的这个产品😊:

![伽罗华 P4](/medias/2026/10/galois-p4-new.png)
图2：伽罗华 P4

它是一台激光扫描仪, 机身里是905纳米的激光雷达加彩色镜头模组: 4/3英寸的CMOS, 4700万像素, 直出3亿像素的24K全景图, 激光测距的绝对误差在10毫米以内.

它在拍摄的时候，大概用16秒转一圈，一共拍5-6个角度，最后会通过我们的算法合成一张全景图。和拍照手机的HDR不一样, 伽罗华从第一代开始, 每一个角度的拍摄, 都是5张不同曝光的RAW数据. RAW就是传感器原始的输出, 没有经过机内的压缩和处理, 5张不同曝光下来, 亮度层次是全的. 也就是说, 在采集这一环, HDR的信息从一开始就是有的. 🙂

但是过去的问题在于: 采集到了, 展示不了. 产物是要放到公开的Web上给人方便分享，方便查看的, 而过去Web对于HDR的照片的展示，一直是远远落后于视频的支持的，所以过去这些数据到了输出这一层, 还是走SDR格式的JPEG, AVIF. RAW里的数据, 只是存了下来.

但技术发展到今天，有了一些新的变化. Chrome是2023年开始能正确显示HDR照片的(AVIF和Ultra HDR JPEG, Chrome 116起), Windows上的Edge随后跟进, Safari最晚, 到2025年的Safari 26才原生支持HDR图像, 顺带把WebGPU也带上了. 也就是说, 到去年, 单张照片在主流浏览器上算是都能亮起来了.

于是，时机已到, 我们花了半年, 用WebGPU把前端渲染引擎整个重写了一遍, 让它能一路走到屏幕.

## 0x2 存储: Ultra HDR的思路

先说"怎么存". 考虑到毕竟还是有很多设备不支持，我们也不得不采用了Ultra HDR: 底子还是一张兼容性最好的JPEG SDR底图, 增益图(gain map), 再加上解释增益的元数据. 普通解码器看到的, 就是那张SDR底图; 认得增益图的, 才恢复HDR. 就像给旧协议做协议升级时带一个可选的附加包, 老设备不认识就当没看见.

增益图描述的, 是每一个位置上SDR呈现和HDR呈现之间的关系. 恢复的时候, 底图先转换到线性光空间, 增益图再按自身的gamma, 增益范围与偏移规则去解释, 最后算出HDR的亮度.

我们沿用的是这个思路, 把全景空间的数据, 也做成底图加增益图的形式, 数百MB的完整光照数据, 压缩封装成浏览器和手机端能实时承载的轻量格式.

## 0x3 适配: 转动, 放大, 换视点

一张静态的照片, 底图和增益图摆在一起不动就完了, 但全景不行. 用户会转动视角, 会放大看细节, 每一次转动和放大, 都是对这俩张图的重新采样, 增益数据也需要对应的跟着变动.

先说转动. 底图和增益图必须始终保持方向与位置的对应, 这俩张图可以有不同的分辨率, 但格式规范要求, 缩放采样至少要采用双线性的方式, 否则俩张图就会错位, 增益加到不该加的地方.

再说放大. 放大的时候视野变窄, 系统会按当前的视野和显示尺寸, 选择合适的细节层级(LOD), 把局部纹理补充进来, 补充进来的这些纹理, 同样带着增益数据, 要同步更新.

这中间还有一个容易踩的坑: 颜色纹理需要解码到线性光, 但增益纹理不能这么处理, 它要保留原来的数据含义, 一旦被误当成颜色再做一次转换, 亮度关系就错了.

视角之内的问题是解决了, 还有视角之间的. 每个视点, 都有自己的一组信息: 底图, 增益图, 恢复参数. 用户在视点之间切换的时候, 过渡阶段要分别判断俩个视点的HDR可用性, 如果其中一个视点只有SDR底图, 那就按实际的内容处理, 不能硬套同一个增益.

## 0x4 展示: WebGPU

这些都解决了以后, 不管你怎么转, 怎么放大, 怎么换视点, 手里的亮度数据都是正确的了. 但还有最后一环: 怎么把它真正送到屏幕上, 而这一环, 过去在浏览器里是做不到的.

为什么做不到? 我们过去的渲染引擎是基于WebGL的, WebGL的画布, 输出的是8bit的sRGB颜色, 值的范围被钉死在0到1, 超过1的部分一律截掉. 也就是说, 不管你前面的增益算得多准, 到了最后输出这一步, "比白色更亮"的亮度还是放不出去, 屏幕上能看到的, 就还是SDR那个范围的世界.

而且这不是打补丁能解决的. 举个简化的例子, 线性标度下以SDR白为1, w是增益权重:

```

H = S × G^w

w = 0   =>  H = 0.5
w = 0.5 =>  H = 1.0
w = 1   =>  H = 2.0
```

取S = 0.5, G = 4, 偏移为0, 输出如上. 这个2.0代表超出参考白的范围, 如果中间哪一步把值截回1.0, 这个区别就丢了. WebGL的画布就是那个把值截回1.0的最后一环, 颜色输出管线在设计的时候, 就没有给扩展亮度留口子.

所以唯一的办法, 是换掉整个图形后端. 也就是WebGPU: 从Chrome 129起, WebGPU画布支持rgba16float的浮点格式与extended色调映射模式, HDR路径的浮点亮度, 才能一路不截断地落到屏幕上. 这就是这次花半年重写渲染引擎的原因.

最后是绘制的时机. 每次绘制前, 按用户设置, 显示能力和后端的选择确定HDR参数; 一旦检测到环境变化, 比如你中途开了系统的HDR开关, 就同步参数, 跳过当前绘制并更新中间纹理; 绘制完之后, 还要核对增益应用与画布配置. 任何一环没对上, 出来的就是错的颜色.

那怎么知道当前环境能不能走HDR? dynamic-range: high媒体查询提供信号. 用户关闭了HDR, 能力不匹配high, 或者实际跑的是WebGL 2, 就退回SDR底图, 所以旧设备上看到的效果, 和现行版本是一致的, 不出错. Web上没法像电视那样规定死整条链, 那就每一环都自己判断.

## 0x5 Demo

说了这么多, 先看结果, 大家可以先看看这个案例:

[打开新页查看 »](https://realsee.ai/GjVVLO3O?shareCode=vyKw3OyR&entry=share&utm_source=laruence_blog&utm_medium=article&utm_campaign=space_hdr)

注意看左边的内容, 左上角有"24K HDR"的标识. 这个空间开着「同步视角(Sync view)」功能, 你转动视角, 另一边会跟着你转到同一个位置, 一边是HDR的, 一边是SDR的, 同一个场景放在一起看, 更有助于你看出来差异.

看出来差异了么?

如果你看不到HDR标识, 或者感觉画面没有变化, 大概率是因为环境的某个环节不支持HDR, 可以点下面的这个测试按钮试试:

检测 HDR 支持

等待检测

如果三项都支持, 再去开上面的对比体验, 你应该能看出来差异了. 如果有不支持的, 可以开一下系统的HDR开关, 或者把浏览器升到最新(Chrome/Edge 113+, HDR输出需要129+), 再或者换一台带HDR屏幕的设备, 现在的主流手机基本都满足.

## 0x6 开源

我们开源了一个工具: [panorama-viewer](https://github.com/realsee-developer/panorama-viewer). 它是基于three.js WebGPU的全景查看器, 可以直接拖一张Ultra HDR JPEG进去, 从里面读取底图, 增益图和元数据, 在GPU上恢复影像, 还提供一个可以实时调节的显示增益滑块, 把增益从0拉到头, 你能直观地看到画面里多出来的是什么.

更多Space HDR的案例, 在 [Realsee Discover](https://discover.realsee.ai/), 可以按餐厅, 住宅, 酒店, 博物馆, 零售分类慢慢逛.

## 0x7 意义

人看照片, 画面里的光越接近人眼当时的感受, 就越觉得真实. VR要"身临其境", 亮度的范围补全了, 这四个字才会更有分量。

比如我们如视最大的客户，贝壳, 用户在手机上看房子, 采光的房间亮不亮, 朝北的房间暗不暗, 这些直接影响判断的信息, 是非常重要的.

再比如美团的餐厅预订, 订卡座之前先逛一遍, 落地窗边的位置, 射灯打着的氛围, 看完跟到过现场差不多. 需要考察空间的应用, 都是这个道理.

目前贝壳新房板块和美团已经大规模上线了Space HDR房源, 途家, 阿里这些平台也在接入中.

好了, 就介绍这么多, 感兴趣的，可以点开下面的几个案例查看：

* [武汉：天创·云和奕](https://open.realsee.com/lianjia/Lykj3NQLxolDrG06/wXmPbpLd4kef1h5hwTMPxOYfELM9ANlZ/)
* [东莞：佳兆业碧海云天](https://open.realsee.com/lianjia/7vO5MXNZ6ggD4XwG/B7yw51J9rXmHYhjhGTgX6evH6WeEqjNX/)
* [福州：龍庭路95號](https://open.realsee.com/lianjia/K8xbMym0ZBEMA62d/VmoA6eJgy4GsjhdhbTXgXNPHvL10OqrN/)

### Related Posts

* [关于PHP，关于Realsee](https://www.laruence.com/2022/04/12/6089.html)

Filed in [Realsee](https://www.laruence.com/category/realsee "View all posts in Realsee"), [随笔](https://www.laruence.com/category/notes "View all posts in 随笔")

* [Galois](https://www.laruence.com/tag/galois "View all posts tagged Galois")
* [HDR](https://www.laruence.com/tag/hdr "View all posts tagged HDR")
* [realsee](https://www.laruence.com/tag/realsee "View all posts tagged realsee")
* [Space HDR](https://www.laruence.com/tag/space-hdr "View all posts tagged Space HDR")
* [Ultra HDR](https://www.laruence.com/tag/ultra-hdr "View all posts tagged Ultra HDR")
* [WebGPU](https://www.laruence.com/tag/webgpu "View all posts tagged WebGPU")
* [伽罗华](https://www.laruence.com/tag/%E4%BC%BD%E7%BD%97%E5%8D%8E "View all posts tagged 伽罗华")
* [空间相机](https://www.laruence.com/tag/%E7%A9%BA%E9%97%B4%E7%9B%B8%E6%9C%BA "View all posts tagged 空间相机")

Previous Post
[Anatomy of This Nuclear-Grade PHP Vulnerability](https://www.laruence.com/en/2026/10/22/7686.html)

No Newer Posts
[Return to Blog](https://www.laruence.com)

## One Comment

1. ![石樱灯笼](https://cravatar.com/avatar/64f2aff021ad2833a7b98920f51df7da?s=48&r=g)

   [石樱灯笼](https://www.catscarlet.com)
   October 30, 2026

   我就说公众号那边不值得维护，平台抽风起来甚至无缘无故封号。

   HDR这路还是太长了，本质上需要显示设备上支持一个新的独立变量“亮度”，但是LCD最多支持到HDR400，相当于没有。但是LED屏幕目前的基础还是太差了。电视的情况还算好的，台式机液晶显示器也中规中矩，但是到笔记本屏幕和手机屏幕，就只能用瞎眼来形容了。

   [Reply](https://www.laruence.com/2026/10/30/7736.html?replytocom=562800#respond)

### Leave a Reply [Cancel reply](/2026/10/30/7736.html#respond)

Your email address will not be published. Required fields are marked \*

Comment

Name\*

Email\*

Website

[ ]  Save my name, email, and website in this browser for the next time I comment.

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Sidebar

![](/images/logo.jpg)

Laruence

[PHP](http://www.php.net/)核心开发者, [Zend](http://www.zend.com/)顾问, PHP7及PHP8 JIT核心作者. Yaf等开源项目作者.

Search

## 开源项目

[Yaf](http://pecl.php.net/package/yaf):  PHP Framework in PHP extension
[Yar](http://pecl.php.net/package/yar):  Light,...