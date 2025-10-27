---
title: 【安全圈】新型 PIXHELL 声音攻击能从 LCD 屏幕噪音中泄露信息
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064335&idx=4&sn=e114f651f6c93675075a02c7f12819db&chksm=f36e660fc419ef19c2aa90c1661626aac9f229e4269061a9853c3b6dde00b3265a9f0afe385c&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-12
fetch_date: 2025-10-06T18:29:18.751175
---

# 【安全圈】新型 PIXHELL 声音攻击能从 LCD 屏幕噪音中泄露信息

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgRicbQ6VzsjWRPfpanbuyeSichtfanqujEoVenoJ8P4vBprxIN5F7H20DelVfEG5QGz9Fm84nKEPjg/0?wx_fmt=jpeg)

# 【安全圈】新型 PIXHELL 声音攻击能从 LCD 屏幕噪音中泄露信息

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

数据泄露

以色列内盖夫本古里安大学（Ben Gurion University of the Negev）的研究人员发现，一种被称为 “PIXHELL”的新型侧信道攻击可通过突破“音频间隙”攻击气隙系统（Air-gapped ）中的计算机，并利用屏幕上像素产生的噪声来窃取敏感信息。

所谓气隙系统是一种将电脑进行完全隔离（不与互联网以及任何其他联网设备连接）以保护数据安全的系统，通常是通过断开网线、禁用无线接口和 USB 连接来实现， 被认为是最难以渗透的、最安全的计算机。

## 攻击原理

该大学软件和信息系统工程系进攻性网络研究实验室（Offensive Cyber Research Lab）负责人Mordechai Guri （莫迪凯·古里）博士在新发表的论文中称，气隙和音频气隙计算机中的恶意软件会生成精心制作的像素图案，产生频率范围在0-22千赫的噪声，恶意代码利用线圈和电容器产生的声音来控制从屏幕发出的频率，声音信号可以编码和传输敏感信息。

值得注意的是，这种攻击不需要任何专门的音频硬件、扬声器或被攻击计算机的内部扬声器，而是依靠LCD屏幕产生声音信号。

古里博士表示，气隙系统御措施可能被恶意内部人员或其他社会工程学技术渗透，如恶意U盘的插入、点击恶意链接或下载受感染的文件，攻击者还可能利用软件供应链攻击，瞄准软件应用程序依赖关系或第三方库。通过破坏这些依赖关系引入在开发和测试过程中可能被忽视的漏洞或恶意代码。

因此，PIXHELL攻击利用部署在被入侵主机上的恶意软件创建一个声音通道，从音频屏蔽系统中泄露信息。这是因为LCD屏幕的内部组件和电源中包含电感器和电容器，当电流通过线圈时，这些电感器和电容器会以可听到的频率振动，产生高音噪音，这种现象被称为电感啸叫。具体而言，耗电量的变化会引起电容器的机械振动或压电效应，从而产生可听到的噪音。影响耗电模式的一个关键因素是点亮的像素数量及其在屏幕上的分布，因为白色像素比深色像素需要更多的电量来显示。

此外，当交流电（AC）通过屏幕电容器时会以特定频率振动， 声波由液晶屏的内部电气部分产生。其特性受屏幕上投射的实际位图、图案和像素强度影响。

通过仔细控制屏幕上显示的像素图案，就可以从LCD屏幕上产生特定频率的声波，而攻击者可以利用这种技术，以声波信号的形式渗出数据，然后将这些信号调制并传输到附近的 Windows 或 Android 设备，然后解调数据包并提取信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgRicbQ6VzsjWRPfpanbuyeSfTTWNoxwNr0sEb5G14xbdJmpDrYpC9ia62211d29RNlLGs5icYKr1qhA/640?wx_fmt=jpeg&from=appmsg)攻击场景：被入侵计算机（A）上的恶意软件会对信息进行编码，并使用精心制作的像素模式通过发射的声波信号将信息外泄。附近的笔记本电脑接收信号、解码并将其发送给攻击者

## 限制条件

尽管如此，这种攻击方式存在一些限制条件，包括发射的声音信号功率和质量需要取决于具体的屏幕结构、内部电源、线圈和电容器的位置等因素。另一个更加限制的条件在于，PIXHELL 攻击默认情况下需要将显示屏幕调整为由黑白交替行组成的位图模式，因此了保持隐蔽性，攻击者可能会采用在目标用户不在时进行攻击，比如在非工作时间行所谓的'通宵攻击'，降低被揭露和暴露的风险。

但古里博士也指出了一种可在平时工作时间转变为隐蔽攻击的方法，即在传输之前将像素颜色降低到非常低的值，比如使用 (1,1,1)、(3,3,3)、(7,7,7) 和 (15,15,15) 的 RGB数值，从而给用户造成屏幕是完全黑色的假象。但同样，这一方法的副作用是大幅降低了声音的制作水平。此外，如果用户仔细观察屏幕，仍然可以发现异常之处。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgRicbQ6VzsjWRPfpanbuyeSf4L1xAw58Xc4M5C5ucEibpUSI7jgt80Lv6oIpFKBtc37nuRPKeoUIGw/640?wx_fmt=jpeg&from=appmsg)四种近似黑色的RGB数值显示效果

该研究这并不是第一次在实验装置中突破音频间隙限制。古里博士在之前进行的研究中还采用了计算机风扇（Fansmitter）、硬盘驱动器（Diskfiltration）、CD/DVD 驱动器（CD-LEAK）、电源装置（POWER-SUPPLaY）和喷墨打印机（Inkfiltration）产生的声音。

作为应对措施，建议使用声音干扰器来中和传输，监控音频频谱是否有异常或不常见的信号，限制授权人员的物理访问，禁止使用智能手机，并使用外部摄像头来检测异常的屏幕调制模式。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgkUguUn2Zr2jE7dxoVOPckLPdj78V4glicW8B5l0wYOEZDiaUNPm6kFmfU1qSpspg793icvkdGzG1bw/640?wx_fmt=jpeg)[【安全圈】全国首例！三名程序员在虚拟币钱包中植入“后门”，窃取上万条用户密码](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064313&idx=1&sn=f0e564b32de7f9a8451a7838cd09ce68&chksm=f36e6679c419ef6f89e6896804adff9e1368a071fdeda74e84abab8a9f3a1fbff730d6cd9350&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljUASPgGc31ibGFF8QlWO2bDVRTmG60tLcehoiaraLcyb9sHGOuavM5GxCJMTSegsHe0rNJzoDG9Cww/640?wx_fmt=jpeg&from=appmsg)[【安全圈】美国一 AI 公司因非法收集面部数据被罚超 3000 万欧元](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064313&idx=2&sn=1a2768fa4fc1c00cdb0d5257c8f13ab0&chksm=f36e6679c419ef6f6aabf549f51379c2bdefb5b3097e8d633c0b1971d029fc37b4b0f41e6637&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgkUguUn2Zr2jE7dxoVOPckwO49EEhAmZlicZuPyaMTV5V0Ot6L28ujkfcMaic2GwicQtMLqtcgJhymw/640?wx_fmt=jpeg)[【安全圈】McAfee 识别出 280 多个虚假安卓应用，可能会窃取加密货币钱包](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064313&idx=3&sn=779efcc08939bdd90510ded9e796ed50&chksm=f36e6679c419ef6f32af6ed70d1c1bc2cf9c6ec712a4762d0fbf5fab5a13b9ec9c822a19b1d6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgkUguUn2Zr2jE7dxoVOPckGjKj87HLbicfdk2VICtNmbsstdWXUibE5L8tO1tM7K4x5iavP9AVefLUg/640?wx_fmt=jpeg)[【安全圈】黑客背刺同行，向对方发送信息窃取软件](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064313&idx=4&sn=0aa1c34198f22da1fad88f018223ddf9&chksm=f36e6679c419ef6f6509c94daed8b8325067c714e4eb88049e1be19548527e03aa43c500eb0a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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