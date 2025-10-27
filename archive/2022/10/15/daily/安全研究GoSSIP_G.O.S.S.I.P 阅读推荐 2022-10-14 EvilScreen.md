---
title: G.O.S.S.I.P 阅读推荐 2022-10-14 EvilScreen
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247492914&idx=1&sn=52403a2177409a69c74574c49ccaee5a&chksm=c063cbebf71442fd8626d9aff415fbf4a9df2c06fba6d2d5498417d80c25058d99051b29c5b2&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2022-10-15
fetch_date: 2025-10-03T19:57:25.115748
---

# G.O.S.S.I.P 阅读推荐 2022-10-14 EvilScreen

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21GWZicGX3KVSQ7HIjav5ibEhOY3gFsUOic7PpO8iaPdQF4WfrXbZFibo1JBia9q9l6cN925W1QW1geoy3SA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2022-10-14 EvilScreen

原创

G.O.S.S.I.P

安全研究GoSSIP

经过了国庆七天的放纵和国庆之后七天上班的疲惫，今天还有多少人会居家隔离呢？在这个历史性的周末，我们要把一项由我们团队完成的研究工作推荐给大家。这项研究工作对智能电视进行了安全分析。利用现有智能电视常常使用三种遥控器、而这三种遥控器各有各的安全弱点的现状，我们发起了名为*EvilScreen*的特定安全攻击，能够连续绕过智能电视所在（无线）局域网的密码保护，欺骗智能电视和未授权的设备配对，最后利用远程屏幕控制协议对智能电视进行全面控制。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GWZicGX3KVSQ7HIjav5ibEhOZI74Wv4pPGK4pjtQMQO1jRgWtT6CNlCUIfcf6oyUWWicRS3xiaicj4Gzw/640?wx_fmt=png)

在智能家电的使用上，我们伟大的社会主义祖国遥遥领先于腐朽落后的资本主义世界，因此本文首先要为水深火热中的西方读者科普一下智能电视的控制方式。众所周知，西方世界都还处在古老的电视机+红外遥控器时代，从未见过智能电视。在2020年代，智能电视拥有三类不同的遥控方式，除了经典的红外遥控器，还可以使用蓝牙和Wi-Fi的方式无线远程操作。厂家除了给传统的遥控器进行升级，加装蓝牙（甚至包括一个语音传输）模块之外，也允许用户安装特定的companion app，在手机上通过Wi-Fi（手机和电视要提前接入到同一个无线局域网）来对电视进行控制。这种时尚的用法背后，存在一些基本的设计难题。首先，用户购买电视后，怎么样让电视识别这么多遥控设备（特别是手机），这背后涉及蛮复杂的配对问题；其次，电视在第一次安装（或者更换Wi-Fi）的时候怎么接入特定的无线局域网？最后，如果原配遥控器丢失了或者电视与遥控器的连接出了问题，用户如何重新配对？作为安全研究人员，考虑到这些因素，就会特别留意其中的安全威胁，进而想到不同的安全攻击！

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GWZicGX3KVSQ7HIjav5ibEhOqDcTAickElR3j1dJa7qib1L7Fic8KMYA4TZyESiawicC4lqbg9KsXhumDpQ/640?wx_fmt=png)

大家可能从下图中就能看到我们提出的EvilScreen攻击的基本思路：

1. 为了能够进入智能电视所在的无线网络（智能电视的第一重防护），我们充分利用了传统的红外遥控器和一些电视配置的蓝牙（BLE）遥控器的弱点。在这些遥控器中，基本上没有安全认证（红外遥控）或者只有一些较弱的安全认证（BLE遥控），我们一则可以利用红外攻击在完全没有认证的情况下主动对电视发起遥控（歪果仁肯定也没见过支持红外功能的小米手机！），二则可以嗅探蓝牙信息，窃取数据。而这一步的关键，是基于用户在给智能电视进行配网（即选择Wi-Fi SSID并输入密码的过程）时，电视还没有接入Wi-Fi，因而只能用这些安全性更弱的遥控通信方式进行控制。
2. 现在的智能电视厂商很喜欢为自己的产品开发一个配套的companion app，让用户在手机上也能控制电视。但是从手机控制电视，肯定需要双方进行认证，否则很容易产生安全问题。这一步一般被称为配对（pairing）。只有经过配对的设备（从而共享了某些credential）之间才能互相通信，这也是智能电视的第二重安全防护。在假定我们已经突破了第一层防护之后，为了突破这层方法，我们假定攻击者已经处在无线局域网之中，可以观察流量，在电视和手机进行配对时，如果它们之间利用了一些（私有的）不安全配对协议，攻击者亦可解密流量，或者主动发起一些穷举攻击，甚至可以冒充合法设备来主动发起配对，欺骗用户确认。
3. 最后，在完成了对红外、蓝牙和Wi-Fi三类信道的控制权后，攻击者只需要攻破第三重防护：电视屏幕的远程控制调用。智能电视的操作系统一般从Android或Android TV OS衍生而来，于是也继承了触摸操作的特点。然而很少有人会去电视屏幕上戳戳戳吧？为了支持遥控器对屏幕的便捷操作，厂商一般会增加一些功能接口，包括远程投屏、远程安装应用等等，攻击者只需要去逆向分析一下厂商的companion app，往往会有很多惊喜哦！

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GWZicGX3KVSQ7HIjav5ibEhO8HS9ZSj0ic6BPIMNmibYxcaWE0OuUiaKyfzKvyLPGLx7IR4XackvxMwbQ/640?wx_fmt=png)

我们基于上述思路，对下列电视（是的，你没看过，还有乐视！）进行了分析（别问为什么不测试最新最贵的型号，买不起！！！）及其相关的TV OS还有智能遥控器进行了分析

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GWZicGX3KVSQ7HIjav5ibEhOgkMJclG2ficdjQ8uQsXTH8qMGFenQ09ibhaj8Wbiap64ZsKzQ8iayic6M1w/640?wx_fmt=png)

我们分析的关键，是对开展EvilScreen中至关重要的遥控器进行分析。特别关注的是智能电视和遥控器的配对，智能电视的配网，以及在这些遥控器驱动下智能电视的远程控制功能的分析：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GWZicGX3KVSQ7HIjav5ibEhOozNQTTTrryOibkJiby1vMAwbTtBC6OqMh6CNSia6cDibxqvTy5iag5WjHCA/640?wx_fmt=png)

总结一下，不管是国外的三星、索尼还是国内的TCL、康佳和小米，以及世界杯电视赞助商——海信，在EvilScreen攻击面前都存在安全问题。那这也是因为智能电视在实现上和传统电视、智能手机和IoT设备都有挺大不同的，我们用下表总结了区别，希望厂商能够更好地对各种攻击面进行防护：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GWZicGX3KVSQ7HIjav5ibEhOHGm1zRUGiboWsV0tauTXW21m2UtiaZxKKLDsQLOygNtJNsiclLKcQaRWw/640?wx_fmt=png)

实际上，本文的研究工作最初由G.O.S.S.I.P成员陈天成在2019年9月21日深圳的 “OGeek 即刻不凡” 大移动安全高峰论坛上以《劫持你的屏幕：打开智能电视认证的三重门》为题做过报告，此后又有来自电子科技大学和武汉大学的初畅和张宇飞两名实习生同学对研究工作进行了复核和补充，在此特别感谢！特别地，论文中包含了一个非常有趣的针对三星电视和APP配对协议的分析，有兴趣的读者可以特别关注哦：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GWZicGX3KVSQ7HIjav5ibEhOqS8ibkoWzcWYbQPvu3uJsqF9iag3TKH4sMxZBN1bcppNMYeqQFS1MNag/640?wx_fmt=png)

---

论文PDF：https://arxiv.org/pdf/2210.03014.pdf

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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