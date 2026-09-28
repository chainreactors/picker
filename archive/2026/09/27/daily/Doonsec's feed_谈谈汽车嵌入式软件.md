---
title: 谈谈汽车嵌入式软件
url: https://mp.weixin.qq.com/s/YpHEviuymBkLbf5o0KsBTQ
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:53:45.590891
---

# 谈谈汽车嵌入式软件

# 谈谈汽车嵌入式软件

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**01**

**什么是嵌入式软件？**

嵌入式软件就是嵌入在硬件中的操作系统和开发工具软件，它在产业中的关联关系体现为：芯片设计制造→嵌入式系统软件→嵌入式电子设备开发、制造。

嵌入式软件最基本的理解是软件+硬件结合，来对产品做出定义，而非嵌入式软件又或是纯互联网行业则是单纯的对软件做出定义，其兼容性差，软件移植性差。

传统行业上对嵌入式的应用较为广阔，即便现在互联网行业如此发达，但是不得不承认，传统行业在社会发展中有不可替代的地位。传统行业与互联网的结和的嵌入式开发应用更是具有光明前景的。

嵌入式系统一般由嵌入式微处理器、外围硬件设备、嵌入式操作系统以及用户的应用程序4个部分组成，用于实现对其他设备的控制、监视或管理等功能。嵌入式软件就是基于嵌入式系统设计的软件，它也是计算机软件的一种，同样由程序及其文档组成，是嵌入式系统的重要组成部分。

嵌入式中硬件和软件也不再是截然分开的两个概念，而是紧密结合、相互影响的。因而出现了软硬件协同（codesign）设计方法，即使用统一的方法和工具对软硬件，协同设计软硬件体系结构，以最大限度地挖掘系统软硬件能力，避免由于独立设计软硬件体系结构而带来的种种弊病，得到高性能低代价的优化设计方案。

**嵌入式软件的特点：**

**1、独特的实用性**

嵌入式软件要求它与外部硬件和设备联系紧密，嵌入式系统以应用为中心，嵌入式软件是应用系统，根据应用需求定向开发，面向产业、需要特定的行业经验。每种嵌入式软件都有自己独特的应用环境和实用价值。。

**2、灵活的适用性**

嵌入式软件通常可以认为是一种模块化软件，它应该能非常方便灵活地运用到各种嵌入式系统中，而不能破坏或更改原有的系统特性和功能。嵌入式软件要使用灵活，应尽量优化配置，减小对系统的整体继承性，升级更换灵活方便。

**3、程序代码精简**

由于嵌入式系统本身的应用有小体积、小存储空间、低成本、低功耗等要求，嵌入式软件和大型机上的软件相比，具有代码精简、执行效率高等特点。

**4、可靠性、稳定性高**

嵌入式系统应用要求一般较为苛刻，特别是在涉及安全相关的领域，如汽车电子（下面会具体说明汽车软件嵌入式的相关内容）、还有工业控制、航空航天等，这些领域的嵌入式系统不仅要求硬件可靠，还对嵌入式软件提出了更高的要求。嵌入式软件需要运行可靠、稳定,具有错误处理及故障恢复等功能。

**嵌入式软件分类：**

按照通常的分类方法，**嵌入式软件可以分为系统软件、应用软件和支撑软件三大类：**

**1、系统软件**

系统软件控制和管理嵌入式系统资源，为嵌入式应用提供支持的各种软件，如设备驱动程序、嵌入式操作系统、嵌入式中间件等。

**2、应用软件**

应用软件是嵌入式系统中的上层软件，它定义了嵌入式设备的主要功能和用途，并负责与用户进行交互。应用软件是嵌入式系统功能的体现，如飞行控制软件、手机软件、MP3播放软件、电子地图软件等，一般面向特定的应用领域。

**3、支撑软件**

支撑软件是指辅助软件开发的工具软件，如在线仿真工具、交叉编译器源程序模拟器和配置管理工具等。

在嵌入式系统当中，系统软件和应用软件运行在目标平台上（即嵌入式设备上），而对于各种软件开发工具来说，它们大部分都运行在开发平台（PC机）上，运行Windows或 Linux操作系统。

**02**

**嵌入式软件和非嵌入式软件的区别**

嵌入式：在已有的硬件上移植（需要修改操作系统源码，安装不需要）操作系统解决软硬件耦合导致的问题。

嵌入式软件和非嵌入式软件的区别(即传统开发和嵌入式开发的优缺点）：

**传统开发的缺点：**

* 软硬件耦合度高导致软件移植性差

* 软件开发人员必须懂硬件

* 软件功能性差

**优点：简单，开发成本低**

**嵌入式开发的优点：**

* 解决传统开发软硬件耦合度导致的问题

* 多任务机制

* 提供了丰富的网络协议栈

* 提供了丰富的开源软件和工具

**缺点：硬件成本高**

**03**

**汽车嵌入式软件方向**

嵌入式软件部分分为软件架构、软件刷写、底层软件、应用层软件和故障诊断等几个部分。

**软件架构：**

* Boot-loader

* 软件平台层

* 策略应用层

Boot-loader作为一个单独的工程开发，生成一个独立的二进制文件。

下图为基于UDS协议的Boot-loader架构：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicxXQz0JRMTt5IwlSEqJGZ9NZCsPEu3yuMygXoibbMZwhibc9WytHicZEUrnoycMvNIQibZ7Pt9cmJaIQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

下图为软件架构：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicxXQz0JRMTt5IwlSEqJGZ98MFK8GgPLErHvuWM47DjibVa8dfw7B7Ojw1xLIWCB8eZQQBGicNiclh9Q/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

**软件刷写**：控制器复位后，将根据外部硬件配置选择boot-to-flash模式，跳转到Boot-loader，执行RAM自检。若自检成功并且检测到有效的应用软件，将跳转到应用软件，否则，进入boot-loader模式，等待刷新有效的应用软件。下图是Boot-loader软件逻辑。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicxXQz0JRMTt5IwlSEqJGZ96WicrKakQMYKWUSrY6dH9fhicAcqVU8LaU1YK7rF22iaOjwGNdw7PUS5Q/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=2)

**硬件依赖层（底层驱动）**：包括复杂驱动、看门狗、基础服务（系统调度所需定时器、中断管理和一些通用处理函数，如PLL驱动、Flash驱动、内存管理驱动、定时器驱动）、IO、CAN等其他驱动。

**硬件抽象层**：对IO口、PWM、CAN、SPI等功能模块进行抽象定义，使得应用程序实现不同底层平台的移植。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicxXQz0JRMTt5IwlSEqJGZ9XKlaQ60maX5zSibcDRTMkWF1cCfpaa4SXMPv9UJG2zyTHGDicXwjAhMA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=3)

**软件集成**：软件集成就是将应用层软件与底层软件集成为一个可刷写到硬件中的软件，软件集成的变量映射关系详见下图：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwicxXQz0JRMTt5IwlSEqJGZ9VU84C9b5f1nlSDFicFXg4qsSTjpTUSDAWV3AiaCsqyxBVZ08b9AtibFtQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=4)

底层会根据硬线或者CAN线输入，生成一系列的接口变量（函数），应用层直接调用底层上传的接口变量（函数）。硬件抽象层（HAL）将完成对底层信号到全局变量的映射。为实现硬件更改及平台移植，底层软件平台采用宏和脚本来完成全局变量和API（应用程序接口，例如函数）的自动生成。

**VCU整车控制策略：**

按功能模块划分有如下功能模块：输入信号处理、输出信号处理、转矩控制、上下电控制、档位模式、系统能力估算、故障诊断处理、附件管理等。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicxXQz0JRMTt5IwlSEqJGZ9HO3EYVcOQt78vKFVLc94KMngUQMLKibupFKZiaqEyV0zl9As10rr7uibg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=5)

从上图可以看出，整车控制器分为三个层次：最上层为应用层，也称为控制策略层；中间一层为底层，也成为基础平台软件层，它的作用类似电脑中的操作系统，最下面一层为硬件层，就是电脑中的电路板。

版权声明：本文为CSDN博主「819号宇航员」的原创文章

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA7BGa1vwHmHNlluBv83nX42cOwngUmsgRicQ6oyhxN3HmOsFIml2sUM8Yibk5GELQqiaFLt2dVzmf01r90xrW0vMWGpJX7zOsmkM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247575659&idx=3&sn=1b3acb3a33e0fc992b67b37bc4d04a0e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&sn=0ca6395502487515a921f32288b7e8df&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)

**部分入群专家来自：**

**新势力车企：**

特斯拉、理想、极氪、小米、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

**内资传统主流车企：**

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......

**全球领先一级供应商：**

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦尔、大疆、日立、哈曼、华为、百度、联想、联发科、普瑞均胜、德赛西威、蜂巢转向、均联智行、武汉光庭、星纪魅族、中车集团、潍柴集团、地平线、紫光同芯、字节跳动、......

**二级供应商(500+以上)：**

中科数测、ETAS、BlackDuck、NXP、上海软件中心、Deloitte、奇安信、为辰信安、云驰未来、信长城、泽鹿安全、纽创信安、复旦微电子、天融信、奇虎360、中汽中心、中国汽研、上海汽检、加特兰微电子、浙江大学......

**人员占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic...