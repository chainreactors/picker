---
title: 从细节看GPT-4 Microsoft Security Copilot
url: https://mp.weixin.qq.com/s?__biz=MzI1MjQwMTAyOQ==&mid=2247483830&idx=1&sn=f9b03390485ff5268d62c1a447a7f148&chksm=e9e5055cde928c4af5ab2c6a1b1f3f13e20d39e0107945cbda0195b987cff5a11bc7d1471482&scene=58&subscene=0#rd
source: 落水轩
date: 2023-03-30
fetch_date: 2025-10-04T11:08:12.316630
---

# 从细节看GPT-4 Microsoft Security Copilot

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZrnQ9cTzz1V6yO9iaOskRxTic4UO9cdfaTQHXAQ8ibxCu5musUVcHekQsym22HTjkibZS9Zia4qwjib8vacGhwACMBSQ/0?wx_fmt=jpeg)

# 从细节看GPT-4 Microsoft Security Copilot

原创

高渐离

落水轩

最近一直在关注ChatGPT怎么在各个行业大杀四方。终于等到了微软带着他，杀到了安全行业。

空气中弥漫着一股焦虑的味道。

当然，在GPT-4杀进来之前，我们几个小伙伴已经内部讨论过一番，关于我们这个领域会怎么被干掉。

大家的共识是，我们肯定会被干掉。哈哈哈哈。

小伙伴们有的悲观，觉得人类到了奇点了，我们碳基生物可能只是硅基生物的bios，负责引导硅基生物加载。

不过我一直是个乐观主义者，心里一直想着都是，这下又有个辅助工具，可以让老板发现不了我是个水货。例如，我可以让他帮我写很多脚本，还显得我每天有代码产出一样。这简直就是划水利器，懒人福音。

所以，我要看看能怎么用Ms Security Copilot来划水。我这里没试用，以下全部来自于微软官网的小视频，结合我自己的一些理解。不为正确性负责。

## 案例

非常简洁的界面如下，支持外部和内部安全数据的查询，以及文件查询，事件分析：

![](https://mmbiz.qpic.cn/mmbiz_png/ZrnQ9cTzz1V6yO9iaOskRxTic4UO9cdfaTeBnSFB4Gvhz8mOC0a6iaPEgice0IiawThZzvKMgxfNrbbFBcWCQdg9ibSg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/ZrnQ9cTzz1V6yO9iaOskRxTic4UO9cdfaTPGSd8vaZAlAaKou87ePFv0jfhRIRpzAFc1rvozfBuHMVDZcGCKmFpw/640?wx_fmt=png)

### 漏洞影响面

这里让Copilot回答log4j相关漏洞的信息。问完之后，紧接着问，这个漏洞影响了哪些windows设备？

![](https://mmbiz.qpic.cn/mmbiz_png/ZrnQ9cTzz1V6yO9iaOskRxTic4UO9cdfaTskqaNsR9ukDYd2icIAibOFq5chjfIibicWDeNg8shGIfW1bicxxLFD8blBQ/640?wx_fmt=png)

这个问题，Copilot翻车了。演示视频里说windows11 windows10 和windows 9都不受这个直接影响。但并没有windows9这个操作系统。充分说明，这是个真实的演示。

同时，回答里面通过Ms Defender的数据，确认这个漏洞并不影响当前这些设备。

这个回答也给出了数据参考，一个是Ms Security Blog这个开源数据，一个是Ms Defender for Endpoint采集上来的数据。

老实讲，这个演示中规中矩，缺乏让人心动的感觉。

### 事件调查之事件描述能力

事件调查的演示是用的一个勒索软件的case。

输入的Prompt是：

分析事件 OneNote Initial Access Alert da65065406（事件编号）

输出是：

这个告警标记 centoso.com域用户Terres的设备被一个组织用onenote附件投递恶意软件的方式进行了定向攻击。告警进程onenote.exe是打开SalesLeads.onepkg文件启动的，父进程是explorer.exe.....

数据来源Microsoft Sentinel。

![](https://mmbiz.qpic.cn/mmbiz_png/ZrnQ9cTzz1V6yO9iaOskRxTic4UO9cdfaTlh6aAzLVy3WvDwyJ7XyuoBiabYqU9nBkMSk9MrO1ADMzTwsic2XtuMPw/640?wx_fmt=png)

这里的图是GPT-4自己画的。

按微软的讲法，这个事件的summary展示了四个能力：

* 日志分析
* 告警总结
* 信息抽取
* 可视化

微软安全的女VP大佬当即感慨，说这个图太wonderful了。不过老实讲，很多安全软件现在都会生成这种图。这里的文字可能比图更吸引我。因为从描述来看，GPT的概括总结比较全。不然对于一个普通运营人员而言，看到这个图可能会比较懵逼。

### 事件调查之响应Prompt Book

这个微软生造的一个词，映射到现有的词语可能是安全PlayBook。

这个PromptBook做啥呢？主要是对事件调查一系列还要调查的事情形成固定的Prompt语句，让GPT去后台分析日志，给出结论。

我个人觉得这个点非常赞。

我们看看这起事件都有哪些Prompt语句和回复。

一、恶意软件影响分析Prompt Book

输入：这起事件之前，这个账户有哪些可疑行为

输出：XXX账户在之前有以下可疑行为，标记可能已经失陷了

1. 恶意onenote文件下载
2. 恶意powershell执行
3. onenote文件执行恶意文件
4. 可疑LDAP查询

输入：这起事件之后，这个账户有哪些可疑行为

输出：这个账户后续有可疑的行为，包括onenote powershell 和wmi

1. 通过wscript执行恶意代码
2. 尝试进程注入
3. 可疑启动目录文件
4. 可疑wmi进程创建
5. 可疑powershell执行

输入：分析这起事件期间，任意一台有恶意软件告警的机器流量

输出：

1. 某机器上的XXX进程和某某IP，某某端口进行通信，看起来与通常的行为有区别
2. 这个IP和这个端口还关联到另一个机器上的进程
3. 怀疑这个域里面这两台机器与相关的ZZZZ账户和YYYY账户都失陷

二、逆向分析exploits Prompt Book

这是一段用来逆向分析exploit的Prompt Book。

这个功能对我这种小白是很友好的。它会帮忙解释一段exploit在干啥。不过在这个例子里面，看起来解释的不是二进制的exploit，而是一段powershell脚本代码。

![](https://mmbiz.qpic.cn/mmbiz_png/ZrnQ9cTzz1V6yO9iaOskRxTic4UO9cdfaToqqL7J5F2D9D6l2a4QcKWYtrTKOmwromE8HoNFUfhkXrTwzl1SEBOA/640?wx_fmt=png)

输入：如果有的话，逆向下载exploit的脚本，并解释该脚本

输出：

![](https://mmbiz.qpic.cn/mmbiz_png/ZrnQ9cTzz1V6yO9iaOskRxTic4UO9cdfaTQEUfu9MAmBxWvLgUhIHvjRYiapAJCM4UIiazR1P1jWYvP4DEB0Z1RT0g/640?wx_fmt=png)

输入：提供exploit代码的全过程图，包括下载和利用

输出：

![](https://mmbiz.qpic.cn/mmbiz_png/ZrnQ9cTzz1V6yO9iaOskRxTic4UO9cdfaT99ZKiac6icaBbCn7R48dZ00vPCaicH4OnraKdwUwvbMYTzxgCwwA91LBA/640?wx_fmt=png)

三、止血Prompt Book

这是一段用来阻断攻击和保护数据的Prompt Book

![](https://mmbiz.qpic.cn/mmbiz_png/ZrnQ9cTzz1V6yO9iaOskRxTic4UO9cdfaTticjlehxWRloiaxMv7KIlnjL3r0N8pQQ2x2QfRGtK12wVhMaDLu5qthQ/640?wx_fmt=png)

输入：如何对失陷的设备和账户进行止血？

输出：设备的网络隔离，吊销账户权限，恢复原始的GPO策略。然后给出了详尽的处置方案

![](https://mmbiz.qpic.cn/mmbiz_png/ZrnQ9cTzz1V6yO9iaOskRxTic4UO9cdfaTkA1J0fo762qgdEKzvibNeWX5iaoJaxAFZ0W5ib0QVnp6knLiccjYSibOcbw/640?wx_fmt=png)

### 事件调查之事件总结

输入：总结该事件并画出攻击图

输出：

![](https://mmbiz.qpic.cn/mmbiz_png/ZrnQ9cTzz1V6yO9iaOskRxTic4UO9cdfaTaPSDhHibRLYuGwIH5UdlpQgU20Wqvw4VXFxoc2dtOlTcFjolxhmPzGA/640?wx_fmt=png)

## 训练数据来源

![](https://mmbiz.qpic.cn/mmbiz_png/ZrnQ9cTzz1V6yO9iaOskRxTic4UO9cdfaTRB7PVn6GM9HvztiaEEZvUxHSCkicU9v3KyIUGicZGd5KlSkoeiagYibicjicA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/ZrnQ9cTzz1V6yO9iaOskRxTic4UO9cdfaTTYFbrvlLurDiahaJ3CcZOF7JTLuEv3kAClttkt45oic4YRkAsiaicicBOsA/640?wx_fmt=png)

这个图充分说明了，这个Copliot首先是依赖于Cyber-trained model with security skills，也就是网络安全的领域模型，用的是专有模型。然后是threat intell，也就是大规模的黑数据，再次是端对端的安全工具。最后是OpenAI提供了一个新的交互模式，一个降低知识门槛的交互方式。

## 我们的差距

首先，需要比较好的基础数据。微软通过自己的几个端产品，已经形成了标准的格式化的安全数据。而国内，各家数据不通就算了，很多安全产品采集的数据也不全。我们其实陷入了跟文心一言一样的境地，我们的基础安全数据是存在很大问题的。

其次，国内安全市场很多时候还处于瞎扯淡阶段。概念吹破天，没看到落地。我个人觉得微软选的这个切入视角很有趣，很微软。它就是把安全事件处置响应当成一个做PPT和写word一样的事情，看看怎么用GPT-4提升生产力。

最后，微软一直强调your data  is your data。

## 总结

首先，这个Security Copilot并不是在讲如何通过大数据挖掘找出失陷机器。不是大家心心念念的那种炼丹术，通过机器学习，挖掘APT攻击。

其次，这个Security Copilot是在提供更好的事件处置和响应。提供更丰富的Context和解释性，将响应和调查的动作标准化自动化。更亲切好用的接口。有点类似于Splunk的SQL给事件调查带来的提升。但无疑，它比Splunk的SQL语句更牛逼。

最后，这个Security Copilot对于我这种安全能力一般的人是有用处的。它能够让一家公司，招聘一个能力一般的安全人员，来解决常见的事件响应处置。总体来说，它已经覆盖了很多常规的排查分析路径

它不能解决啥？

如果是牛逼的黑客，通过常规的Prompt Book的流量，可能会丢失他的攻击痕迹。例如他把自己的流量隐藏在常规的https请求里面。这样某些终端失陷就可能发现不了。

整体下来，我觉得微软对这个产品的定位还是很清晰的。

微软认为这个产品可以解决大规模的黑客攻击和安全防御从业人员不足的问题。也就是说，以后可以招一个略微懂点计算机的来做安全运营处置。以前大家都觉得安全从业还是有些门槛的，要么天赋禀异，要么学医，这下门槛被大大降低了，即使不学医，学挖掘机可能也可以进入这个行业了。

![](https://mmbiz.qpic.cn/mmbiz_png/ZrnQ9cTzz1V6yO9iaOskRxTic4UO9cdfaTHcoqdSCOTxic3yY3RvTjZfiagYL2MIppf8yTrQRiawlzddPLm2q2omTqg/640?wx_fmt=png)

我的个人看法，这个产品虽然不够性感，但是从商业模式上来看，可能会改变安全的生态环境。

安全事件运营一直是安全行业的短板。毕竟你让人全天候处置告警也不现实。现在如果有GPT卷进来，没准可以把安全运营变成一个成本很低的行业。24h全自动化无人值守的SOC不是梦。

这个做的好的话，很有可能是常规黑客与黑灰产对抗的一个比较大的转折点。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZrnQ9cTzz1WOsZoFuzvcqld7856xdZUXcXVmW7W3IPYG61GL78m6ILibka5ibzU3jtSBwNcKWUibiboYRfGwuTTOSA/0?wx_fmt=png)

落水轩

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZrnQ9cTzz1WOsZoFuzvcqld7856xdZUXcXVmW7W3IPYG61GL78m6ILibka5ibzU3jtSBwNcKWUibiboYRfGwuTTOSA/0?wx_fmt=png)

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