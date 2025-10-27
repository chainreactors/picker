---
title: G.O.S.S.I.P 阅读推荐 2022-12-28 SGX.Fail
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247493725&idx=1&sn=f5850e37965ce9eeceb38e8684ec5f5b&chksm=c063c684f7144f920997352a80e70e7df009e8aeba1a11adb5e2753d6343c0ec2ec164bca2a8&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2022-12-29
fetch_date: 2025-10-04T02:40:54.154126
---

# G.O.S.S.I.P 阅读推荐 2022-12-28 SGX.Fail

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21HUOB0l8auRWCxVS0BHtp06ibS13Tpg5fKGshVqP77aduGiaAwNKCsicXa4mjDZMVN2exlpYO8absPdA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2022-12-28 SGX.Fail

原创

G.O.S.S.I.P

安全研究GoSSIP

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HUOB0l8auRWCxVS0BHtp06GPlHYJcEhziaSqz5ibZMOdpbjIAPrK6kAYia6TVkvQMTsxayZ7bSU0Xicg/640?wx_fmt=png)

这几天估计很多地方都在拆拆拆，我们安全研究人员同样喜欢指出那些起不到应有防护作用的系统的问题，这几年来很多研究论文针对Intel的SGX这个毁誉参半的安全增强技术提出了多种攻击，今天推荐的论文*SoK: SGX.Fail: How Stuff Gets eXposed*对之前的工作进行了系统性总结：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HUOB0l8auRWCxVS0BHtp06eEn7NQC9BuhceJzJ1ZFKbQRFHN33MauibLMicXHialOqBxRtRnY7598FA/640?wx_fmt=png)

如果你不熟悉SGX技术，本文作者建议你阅读2016年在ePrint上放出的文章*Intel SGX explained*，我们就不再此处赘述。其中一个比较关键的机制——remote attestation是理解SGX的关键，建议读者花点功夫去搞清楚这个概念：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HUOB0l8auRWCxVS0BHtp06UY4qMEicoMO4Snor6wqH1somTuic5S8cRfV88T4RUopZ63WAZZmR9MEA/640?wx_fmt=png)

说说这篇论文的主要贡献，作者认为类似梅西有7座金球奖，本文亦有7大贡献：

1. 对已有SGX攻击技术的分类总结（论文第三章）；
2. 对SGX的升级机制的调研，以及其存在的缺陷的分析（论文第四章）；
3. 对一个基于SGX的区块链系统——`SECRET network`的安全分析和攻击（论文第五章）；
4. 对`PowerDVD`这个知名播放器中基于SGX的DRM保护方案的安全分析与攻击（论文第六章和附录C）；
5. 对论文中列举的攻击方法如何防护进行了讨论，为未来的TEE设计指明了方向（论文第七章）；
6. 实现了一个可以运行SGX enclave的模拟器（附录A）；
7. 提出了一种针对SGX revocation协议的拒绝服务攻击（附录C）

首先看看论文中对当前已有SGX攻击的总结，下表列举了近年来（可以说是层出不穷）的攻击技术，其中有一些是开发者的锅，但是很多问题Intel自己也有份（CPU预测执行导致的侧信道问题更是主要的祸根）

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HUOB0l8auRWCxVS0BHtp06RtcgGVAJ9Lw4gGxAibZM8A56giaOOHBiaetW0tgk8HsS9SI1K177VKUGQ/640?wx_fmt=png)

接下来是一个CPU采购指南，大家可以按照下表选择适合自己的退烧药避开受影响的CPU：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HUOB0l8auRWCxVS0BHtp06eGLWG6zYHOH7VXjiaxIHNZoicTwAAKnicqNTG9hboouK4SSmI14ibPLibCQ/640?wx_fmt=png)

接下来，作者对SGX的一个主要特点——能通过更新来修复核心安全性——这一机制进行了评估。相比起其它平台上（例如ARM TrustZone）上一旦出现安全问题导致根信任机密凭证丢失就无可救药相比，SGX可以一定程度上通过升级CPU微码（microcode）来挽救不利局面，毕竟Intel是一家设计制造一把抓的大厂（嗯，最后还是做不过台积电和AMDYES！）

不过，升级CPU微码往往需要主板厂商配合，通过BIOS升级流程来完成，而这项技术在1998年的时候可能比较流行（如果能理解这个CIH梗的读者，你一定见证过1999年地球保卫战），现在的新用户大部分可能被厂商弄得连手机换电池都不知道了，所以论文作者很严肃地调研了Intel释放出安全更新到主流厂商和用户能够进行升级的时间周期。调查结果表明，这些升级通常需要数月甚至超过一年的时间才能完成，这期间，攻击者可以做的事情就非常多了~

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HUOB0l8auRWCxVS0BHtp06P3heSribvSlQhaXiaBAjrQAOkhEhlevvrJX9LsONfiaEKOUOAZbJCAKPw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HUOB0l8auRWCxVS0BHtp06vq7lbhw7blRzdvaH6aUmATrIX69ZfKDKQlj44x6xFdvrFSQ2MkHwTw/640?wx_fmt=png)

在论文的第五章，作者对一个基于SGX的区块链区块链系统——`SECRET network`进行了安全分析，并通过 xAPIC 漏洞 (https://www.intel.com/content/www/us/en/developer/articles/technical/software-security-guidance/advisory-guidance/stale-data-read-from-xapic.html) 来攻破了`SECRET`的防护：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HUOB0l8auRWCxVS0BHtp06671cta3fCxmo3ppFBluTQrdFXibSPMnqX3H9gaic9QiaxMRGvtDLSRnnQ/640?wx_fmt=png)

论文第六章中，作者再接再厉，对`PowerDVD`播放器中基于SGX的DRM保护方案使用的AACS2算法进行了逆向还原，并最终利用一个虚假的SGX环境（即作者实现的模拟执行环境EGX）来运行`PowerDVD`的enclave代码，提取了DRM的核心密钥，这部分逆向工作非常精彩，限于篇幅在正文中甚至无法体现，读者可以去附录C-E看看更多细节（不是教你搞蓝光盗版！）同时，如果大家对EGX这个模拟执行环境感兴趣，可以去看看附录A里面的实现细节。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HUOB0l8auRWCxVS0BHtp06Ha6rAIFEFgZCESfibojDb9K0AaMmLrBwtzrj0cw8ZqTQ1IdI58UeGgg/640?wx_fmt=png)

最后我们想说，这篇论文真是太充实了，总共28页双栏，正文14页，附加部分（包括139篇参考文章和5个附录）和正文一样长。作者还开发了网站 (https://sgx.fail/) 供大家访问，啊啊啊现在安全圈怎么可以这么卷！！！

---

论文：https://sgx.fail/files/sgx.fail.pdf

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