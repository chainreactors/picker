---
title: Patchwork APT最新攻击样本与威胁情报分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490678&idx=1&sn=d87ceda739b6e5b3458cce1cbf83d960&chksm=902fb35ea7583a48cf85b7c6660fa634e94e1536b5bd6916996441e31131cee9424fd97e7c41&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-25
fetch_date: 2025-10-06T20:37:45.392872
---

# Patchwork APT最新攻击样本与威胁情报分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXhp6r6pWLiaq0A9ok3HlXUAFxDweibWiabKibRNsExPUHDrfzpZMqBK0sxA/0?wx_fmt=jpeg)

# Patchwork APT最新攻击样本与威胁情报分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/news/16843

先知社区 作者：熊猫正正

Patchwork(白象) APT组织是一支疑似南亚某政府背景的黑客组织，最早于2009年左右被发现，主要攻击中国、巴基斯坦、孟加拉国等国家军工、外交、教育，科研机构等，窃密重要数据，该组织主要使用鱼叉式钓鱼攻击手法，附带伪造为PDF文件的LNK恶意文件，通过PS脚本从黑客远程C2服务器下载恶意软件，攻击中使用了多种不同的恶意软件家族，包含：BADNEWS木马、Spyder后门、Remcos RAT、Havoc C2、NorthStarC2、GRAT等。

笔者近期在威胁情报平台追踪到Patchwork APT组织的最新的攻击样本和威胁情报，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXUd2XSY1jGcVxX2vjEiaPyqrQRkicx2p7Vq3Vh8ibbC5JFMBcn3KgsHzNA/640?wx_fmt=png)

对该APT组织最新的攻击样本和威胁情报进行了详细分析，分享出来供大家参考学习一下。

样本分析

1.通过威胁情报平台，关联到相关的样本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXrdCJ7oxaPrNFkwHibz0aMNiaiaHs7zXuVwJzwT5lic1RXbJkib3icaTvy4NA/640?wx_fmt=png)

2.解析LNK恶意软件样本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXibO5nn9fBAGjqXL6NK80xkELnEM7cTNTXRRRDLrxnQeMGFHeCHgnbGA/640?wx_fmt=png)

3.从远程服务器上下载恶意软件，下载的恶意软件编译时间为2025年1月20日，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyX2icMhaI2fMEFPiaDL5bLyUOCsxiczOfylq93oySpbSdVJerbqYE8UYgOw/640?wx_fmt=png)

4.解密数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXbVNRBb4FEst4sg0giaPfbCAhFIFQnJJBjb3yHSs8xEbGZQnXWicdE7Lw/640?wx_fmt=png)

5.将解密的数据注入进程，然后通过APC启动执行ShellCode，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXySWk0ia8IH2YvDjiaWmVnMh65o0ZUjWOjMXT2icAfCvW9GlTAXYQdeK5g/640?wx_fmt=png)

6.ShellCode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXvFONMYtgs8jNxy2Xx1n6ibb4RnEgUPVOibumLONY8MXjXsZ49f7xzqYQ/640?wx_fmt=png)

7.执行ShellCode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXjsxSh3qUViar6Z3uvB8JjDJ9tww748ttML4WJnfoLbuaialwkfQd2L3g/640?wx_fmt=png)

8.解密ShellCode中的加密数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXicflGRYeF6W6Gca2zznnibpLEq8wdGutomjccof0Fa6C1t5kCmqrGicYQ/640?wx_fmt=png)

9.解密之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXTVmnN99hiaKcibeYlMY3L04vnHaiaMYIEheQd2fjpegIujUyQMzI37jBQ/640?wx_fmt=png)

10.从内存中加载执行解密数据中的PayLoad，PayLoad代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXayQM0XQrovjwS93BykTxMradn6aI84SjdAWiciaDC1NYHianC3VNbf4WQ/640?wx_fmt=png)

与此前分析过的Pathwork APT变种样本代码结构基本一致，可以判定为Patchwork APT组织的攻击样本。

11.PayLoad上传受害者信息和数据到远程服务器hongbaow.info，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXcpBeyh1mdFvhm8Bx4z4Gxq0Bl5wOdrv1l94TDpeyVLzZT7saibsmLuw/640?wx_fmt=png)

12.将上面下载恶意软件的远程服务器C2域名在威胁情报平台上进行查询，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXTVGa0Nz04YhY5zz0N6rmDZqSXm4crK0FJXc9oykjIxjicGFwS2F3Ybg/640?wx_fmt=png)

到此Pathwork APT最新的攻击样本和威胁情报就分析完了，有兴趣的可以自己下载相关的样本进行分析与研究。

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWx7TwtxEUnyUFibicYuAATyXV02PeZcVYgp88Vcwl6VWtR6TsYiaJWcRsibARG5DRFrpyTe01Lu30XEg/640?wx_fmt=png)

总结结尾

APT是全球企业面临的最大的安全威胁之一，需要安全厂商密切关注，未来APT组织还会持续不断的发起网络攻击活动，同时也会持续更新自己的攻击武器，开发新的恶意软件变种，研究各种新的攻击技术，使用新的攻击手法，进行更复杂的攻击活动，这将会不断增加安全威胁分析和情报人员分析溯源与应急响应的难度，安全研究人员需要不断提升自己的安全分析能力，更好的应对未来各种威胁挑战，安全对抗会持续升级，这是一个长期的过程。

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmW8qYF2seSKglWFKoJdassltn5V5IPUn3OGXsdD4v2nRPg8ZzFAicpXlmlwVmd9KTm4XPkRcXtBEKw/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

预览时标签不可点

阅读原文

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