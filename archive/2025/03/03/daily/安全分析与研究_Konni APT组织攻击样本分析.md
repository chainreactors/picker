---
title: Konni APT组织攻击样本分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490877&idx=1&sn=016e64533eef12e61a91ec8b47c646a5&chksm=902fb215a7583b0384988b5a4325fbf0e77fb6465c39b9b2a497fac1bef9f872cf19f1d387b9&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-03-03
fetch_date: 2025-10-06T21:56:29.916805
---

# Konni APT组织攻击样本分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXibLFt7zBZ99Iqcf6tS2gX7RlRcWRfBbdg0GZovo6bHtgTbNba4AP7ZROl2icsLa5ktPI4O9OSJW2g/0?wx_fmt=jpeg)

# Konni APT组织攻击样本分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

APT是全球企业面临的最大的安全威胁之一，需要安全厂商密切关注，未来APT组织还会持续不断的发起网络攻击活动，同时也会持续更新自己的攻击武器，开发新的恶意软件变种，研究各种新的攻击技术，使用新的攻击手法，进行更复杂的攻击活动，这将会不断增加安全威胁分析和情报人员分析溯源与应急响应的难度，安全研究人员需要不断提升自己的安全分析能力，更好的应对未来各种威胁挑战，安全对抗会持续升级，这是一个长期的过程。

Konni APT组织是朝鲜半岛地区最具代表性的APT组织之一，自2014年以来一直持续活动，据悉其背后由朝鲜政府提供支持，该组织经常使用鱼叉式网络钓鱼的攻击手法，经常使用与朝鲜相关的内容或当前社会热点事件来进行攻击活动，该组织的主要目标为韩国政治组织，以及日本、越南、俄罗斯、中国等地区。

针对Konni APT组织攻击样本进行相关分析，样本相关信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXibLFt7zBZ99Iqcf6tS2gX7My0tq7ibNMT73CUtkcFnOaUPsrEyXcagmCozy1pPx8vq9yGxFkrTBIQ/640?wx_fmt=png)

样本分析

1.初始样本为一个LNK文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXibLFt7zBZ99Iqcf6tS2gX7kT42leXQn1Hadicuiaz0b18G03SOdo6kicessFjicxxTnuWfzSVbt0wLicw/640?wx_fmt=png)

2.解析LNK文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXibLFt7zBZ99Iqcf6tS2gX742ZiaofTz05icPEG2FBLBOe0XZmRkXiczyQnOz8UFicyzFrdsCFcyI2icew/640?wx_fmt=png)

3.样本运行之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXibLFt7zBZ99Iqcf6tS2gX7RSgwlM3Nd5griaC3icxV0xyPffrRM65FooVrJLguq6pn4IAkT3a4myVQ/640?wx_fmt=png)

4.在指定的目录下生成的恶意文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXibLFt7zBZ99Iqcf6tS2gX7rHsIborUMeaib4LVHznSebfWHphps4zmV3cfeS9lHDMQMUtvleWH5dw/640?wx_fmt=png)

通过上面的动态行为以及生成的恶意文件，我大概就能判断该攻击样本是Konni APT组织的攻击样本了，这里会有人说，不要装逼了，你咱判断的？我只能用下面的图片来回复一下。

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXibLFt7zBZ99Iqcf6tS2gX7bicGNXU0femZiblasbFvbPf8hNMUoMoNxicqkoVBU9libtXE7aXuYialbdA/640?wx_fmt=png)

此前我在跟踪分析全球勒索病毒家族的时候，针对一些主流的勒索病毒家族，我只需要看一下文件大小，就能大概判断是属于哪个勒索病毒家族的。

5.start.vbs恶意脚本内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXibLFt7zBZ99Iqcf6tS2gX7dpjJSO5pg6fa92RqnrHXtiabsNsKFcQz6f44ibfeljFyPa8djMB7icM7g/640?wx_fmt=png)

6.93152588.bat恶意脚本内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXibLFt7zBZ99Iqcf6tS2gX7N59y1cwhLuBMkTrrbeQmcjjP7VENHvRYJsgSOWAkU8dg5f0mm03YIw/640?wx_fmt=png)

7.32791673.bat恶意脚本内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXibLFt7zBZ99Iqcf6tS2gX7qhs0gnBMpaHAXOj5ibID3YEXHenJwqrP7vkRCaaDFP6xlTxgmdUY2Jg/640?wx_fmt=png)

8.96001702.bat恶意脚本内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXibLFt7zBZ99Iqcf6tS2gX7SoiaksaRDDPaqic017H0fMLavXahpiazVNIjiaQussOXTqdMrtC7aHnI4w/640?wx_fmt=png)

9.45150722.bat恶意脚本内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXibLFt7zBZ99Iqcf6tS2gX7eGJwGSqzAKhXHZ4434Wwfnia3a14ibKnEZTdGdXrpab9HHMQE5Jq6ia9Q/640?wx_fmt=png)

10.92754154.bat恶意脚本内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXibLFt7zBZ99Iqcf6tS2gX7yL4ibFbezTzOvLXqbiasMX7PaYdDk7PdQ6tjfOQ2VWsc5kPKeZiaia7qZw/640?wx_fmt=png)

11.从远程服务器下载CAB，解压缩之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXibLFt7zBZ99Iqcf6tS2gX7IaCNjH7M7sghntzeSJRRLicQATw2GWbTXepsAMRJa1WJxmpeUaOFoXw/640?wx_fmt=png)

其他分析过程省略，对该样本感兴趣的可以自行研究。

总结结尾

黑客组织利用各种恶意软件进行的各种攻击活动已经无处不在，防不胜防，很多系统可能已经被感染了各种恶意软件，全球各地每天都在发生各种恶意软件攻击活动，黑客组织一直在持续更新自己的攻击样本以及攻击技术，不断有企业被攻击，这些黑客组织从来没有停止过攻击活动，非常活跃，新的恶意软件层出不穷，旧的恶意软件又不断更新，需要时刻警惕，可能一不小心就被安装了某个恶意软件。

对恶意软件分析与研究感兴趣的，但没有基础的读者，可以学习笔者的《恶意软件分析基础课程》，可以零基础入门恶意软件分析。

[恶意软件分析基础教程](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzA4ODEyODA3MQ==&action=getalbum&album_id=3823208984147918849&from_itemidx=1&from_msgid=2247490541#wechat_redirect)

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmW8qYF2seSKglWFKoJdassltn5V5IPUn3OGXsdD4v2nRPg8ZzFAicpXlmlwVmd9KTm4XPkRcXtBEKw/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

安全分析与研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

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