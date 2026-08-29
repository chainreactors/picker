---
title: 全球速卖通利用WebAudio API偷采指纹，蓝牙音频切换遭干扰
url: https://mp.weixin.qq.com/s/_PDw0o3Zqnc8HM3NM9d3pw
source: Doonsec's feed
date: 2026-08-28
fetch_date: 2026-08-29T08:29:31.408657
---

# 全球速卖通利用WebAudio API偷采指纹，蓝牙音频切换遭干扰

# 全球速卖通利用WebAudio API偷采指纹，蓝牙音频切换遭干扰

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX0xrgU9AofddFps5cQcpgFGTguv1WHntug0qfMbvP8RXmeTk5hszs0zaOTUlnIND5A9BIJib6xFs1eXaWf6bO05KiaK3DblVstXc/640?wx_fmt=gif)

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX219wxoLaWnYCaXM8gV9NCUZvKAKClVqvCLWBMvCR67tNUfaH3E2PiaichZyUVEqXOKELd4QbsaG1IzRxV4ntJkOdegicBPicP2iaE0/640?wx_fmt=png)

全球速卖通（AliExpress）的首页会在浏览器中悄然构建隐藏的WebAudio处理图，这一技术似乎支撑着一套激进的设备指纹识别系统，同时带来了一个意想不到的现实副作用：干扰已连接耳机上的蓝牙多点音频切换。

Part01

蓝牙耳机音频被意外切断

安全研究员Laserphile使用的是一副支持蓝牙多点连接的耳机，可同时与PC和手机保持配对。他发现，在Firefox或Chrome中打开全球速卖通首页后，手机端正在播放的音频会被突然切断。

将浏览器标签页静音、将整个浏览器静音，甚至将Windows系统音频静音，都无法恢复播放。只有关闭全球速卖通的标签页才能立即解决问题——尽管页面上看不到任何视频、音频播放器或媒体内容。

常规排查一无所获。页面上没有<audio>或<video>元素，没有对HTMLMediaElement.play()的调用，Media Session API也未报告任何活动的播放。这一行为仅在页面空闲数秒后出现，促使研究者使用插桩JavaScript直接监控Web Audio API进行深入调查。

Part02

AudioContext与零增益音频图

通过重写AudioContext构造函数和AudioNode.connect()方法，研究者找到了元凶：页面创建了两个独立的AudioContext实例，并使其处于运行状态，每个实例中的节点都连接到了系统音频输出端，却未发出任何可听见的声音。

堆栈跟踪将相关活动指向了两个脚本：collina.js和fireyejs.js，二者均托管在阿里巴巴资产服务器的AWSC路径下，与该公司反欺诈和机器人检测工具有关。

根据Laserphile的详细分析，全球速卖通网页利用WebAudio指纹识别使多点蓝牙耳机保持活跃状态。对高度混淆代码的反向工程揭示了一个WebAudio图模式：一个锯齿波振荡器馈入分析器节点和脚本处理器，然后通过一个设为零的增益节点，最终到达音频输出端。

由于该图即便在零音量下仍保持与音频输出的连接，浏览器会持续对其积极处理。这一状态与静音视频有本质区别，而Firefox和Windows显然将其视为合法的音频活动，从而使蓝牙连接持续锁定在PC上。

Part03

更广泛的追踪体系与缓解措施

音频指纹识别只是更庞大追踪套件中的一层。相同的脚本还会探测Canvas渲染、WebGL渲染器信息、屏幕与视口尺寸、硬件并发数、设备内存、已安装插件、WebRTC行为、鼠标与触摸事件、设备运动状态，以及常用于检测浏览器自动化的各类信号。

采集结果经序列化、加密后，通过fetch()和sendBeacon()传输至阿里巴巴的遥测端点。尽管此类指纹识别通常用于防范欺诈、虚假账号和爬虫，但研究者指出，该实现会在常规购物首页无条件运行——远早于登录或结账等任何敏感操作，且对用户没有任何可见提示。

此后，一份相关的Firefox缺陷报告以及一位Mozilla工程师的独立分析也佐证了这一行为的多个方面。

作为缓解措施，通过uBlock Origin自定义过滤器拦截上述两个脚本路径，可以阻止隐藏音频上下文的创建，恢复正常蓝牙切换。不过用户可能需要留意额外的验证码挑战，因为这些脚本很可能向全球速卖通的欺诈评分管道提供数据。

参考来源：

AliExpress Uses WebAudio API and Zero-Gain Audio Graphs for Silent Device Fingerprinting

https://cybersecuritynews.com/aliexpress-webaudio-device-fingerprinting/

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0grlwwcpsEQ5CIH725a7xAnwDLGFctXFohPibiaOVyzdqwaibKgD4x4enG6jhdgJQHziaqTMy1WR0Hibx4MceSVKd6C7HGGlA9zLibg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651344398&idx=1&sn=56c4e0d580e04a250d0e8c6cffd592b8&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3eRDUpH3UJicSe4tdw7nZYu9aa5PQ9KgkaP84oZz0bVYdBiaDt97VfDBLulDp3sWLgvzI4m0mc89MZ7feP2yfFAmcRWOlicWubZ4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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