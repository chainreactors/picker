---
title: ECU在OTA中的信息安全简介
url: https://mp.weixin.qq.com/s/o6ptBKu2QpmXTpRPFz_MrQ
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:26:56.724855
---

# ECU在OTA中的信息安全简介

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaCGcZHTJy7icxNdI6UBfHGVSE9lqEVfTKLrXMcSvDnqDCw1vdh4iaVmhOurpUT05RM7dEZda5DQqMa8YEic9QqGu4wtXFI5Ijl95g/0?wx_fmt=jpeg)

# ECU在OTA中的信息安全简介

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

**01**

**概述**

随着汽车智能化程度越来越高，OTA已经是职能汽车的基础功能和标志性功能。OTA通常分为SOTA 和FOTA，并且OTA过程中，通常涉及“云-管-端”三个环节。本文主要介绍一种在“端”上FOTA场景的信息安全部分，并涉及部分“云”和“管”上的信息安全内容。

**02**

**总体流程**

以“端”为核心的OTA信息安全简化流程如下：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBERAvglatuibicp2r8leiaibNziaBvHuAV9sXvqo7hiaS2q8pwhsAh8pcn5NyUnGx2ZzPKWOpykWW8s6HiamaiacQ2ibpuBIkfftZMeETc/640?wx_fmt=png&from=appmsg)

1. 主机厂在制作升级包的时候，需按照流程进行加密或验签等操作，确保升级包中包含了信息安全内容
2. ECU查询到存在可用的升级包
3. ECU需与车机交互，由用户授权进行下载和升级
4. ECU访问OTA服务器，获取升级信息，此步骤基于mTLS实现
5. ECU通过步骤3中的升级信息，通过单向TLS访问CDN，并进行升级包的下载
6. 升级包下载成功后，ECU对升级包进行解密并验签，通过后即可认为升级包合法，进入升级流程

**03**

**信息安全细节**

在上述流程中，涉及信息安全的主要是TLS、加解密、验签等环节。用途如下：

1. TLS：通过TLS协议解决双方的可信认证和传输安全。建立mTLS时，ECU和OTA Server分别会验证对方证书的合法性，通过此机制双方都是合法的，避免有攻击者冒充ECU或冒充OTA Server。后续传输信息基于TLS，也保证了信息的传输安全性
2. 加解密：通过对升级包进行加解密，保证升级包的机密性。因为CDN是单向认证（实际也可以配置mTLS，即便是mTLS，也可以考虑对升级包加密），可能导致攻击者获取到升级包的CDN地址，即可进行下载。通过对升级包进行加密，使得攻击者即便知道CDN地址，下载的软件包也是密文，从而保护升级包的机密性。对升级包加密可有效保证升级包的机密性，但同时也带来一个问题：升级用时变长，因为升级包通常比较大，会导致解密过程耗时较多，进而导致整个升级用时变长
3. 验签：验签主要保证升级包的完整性和真实性

**3.1 TLS**

TLS主要使用两种模式：双向认证mTLS、单向TLS。TLS原理都遵循RFC标准，以下做简单介绍

1、mTLS：在三次握手时，ECU会验证OTA Server的证书，OTA Server也会验证ECU的证书。验证过程包含：a.用证书链验证证书 b.使用OCSP验证证书。以上两步都通过，才可判定证书验证通过。

a. 因OTA Server会验证ECU证书，因此需确保ECU具有证书和私钥。通常此证书和私钥在OEM产线注入，格式可选择P12等，其中私钥在ECU中需进行安全存储。

b. 因使用到证书链，因此ECU需具有证书链。此证书链可通常可在开发阶段提前预置，并且ECU需要确保证书链的不可更改性。

2、单向TLS：当服务端无法配置mTLS时，可配置单向TLS。单向TLS仅实现ECU对OTA Server的认证，OTA ServER缺少对ECU的认证，其他和mTLS一致

**3.2 加解密**

对升级包进行加密主要目的是保护升级包的机密性，但缺点是需解密操作，比较耗时（尤其在软件包较大时），因此是否对软件进行加解密应综合考虑。加解密通常使用对称算法AES（非对称速度更慢），可使用AES-CBC或AES-GCM等算法实现（具体实现可参考mbedtls移植之AES算法）。使用对称算法需要解决一个重要问题：对称密钥的机密性保护。通常此对称密钥不建议预置，因为采用预置的方式，密钥泄漏后难以更新已量产车的密钥。推荐在OTA时实时下发，简单点就通过mTLS在“请求OTA基础信息”时OTA Server下发到ECU。若想安全性更高，可以考虑采用数字信封方案。

**3.3 验签**

验签主要目的是验证升级包的完整性和真实性，验签在OTA过程中必须具有，否则攻击者可伪造升级包或篡改升级包后进行OTA，导致非法或非预期软件运行在ECU中。验签通常使用SHA256+RSA2048或SHA256+ECDSA算法（具体算法实现可参考mbedtls移植之RSA签名验签算法和mbedtls移植之ECDSA签名验签算法），验签过程简化图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBAGBaS8sKSR6oskYKT708FNrwJ4ZWmOaqPNibmIP8vYG2A30qF5tYkZ2OXCQqKlLkM3adyXj7iaQJQFFBiaGWx8228nU3aGzgxTU/640?wx_fmt=png&from=appmsg)

通常非对称的公私钥 对由OEM生成和管理，私钥需严格保护，避免泄漏。公钥或证书可在OEM产线注入到ECU中，也可提前给供应商预置，ECU中的公钥或证书需具有不可更改性。若攻击者可篡改此公钥/证书，则会导致验签流程不可信。

**04**

**思考**

1. OTA过程中需要信息安全的目的核心是保障升级包的完整性和真实性，因此最基础的需求是升级包需具有签名且ECU需对升级包进行签名验签。在此基础上，可扩展出更多信息安全需求，例如传输的安全性、升级包是否有必要保护机密性、相关证书/密钥等如何安全的传输和存储等。
2. 应结合实际场景进行方案设计，例如有些ECU仅支持OBD刷写，那理论上ECU只要做签名眼前即可，其他环节的安全性不需要ECU参与。有些ECU支持OTA，但属于被刷件，那相关措施就需要在OTA Master上实施。
3. 应建立PKI系统以便规范化的管理相关密钥、证书等。

来源：CSDN博主「辛勤搬砖的门卫」

https://blog.csdn.net/anjiyufei/article/details/149578210

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAgXyLqfnkPJhyibCoBSOMGSsdQ03SEf01kcUbPAEzhf5nb6vyvYWINevstJCARUgy8qNpTa2lKVo7g7RPFm8IicY9aYtviaowaTE/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

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

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJVW2JR9ib5icMR4wIs58nO6ia3OicH5l6vONnmuhfLqMKqj8T2AnD7W1vqQ/640?wx_fmt=png&from=appmsg)

**公司类型占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJU6yKtYSJu4oPaJABYuCSyTpLXjRNbVv7OUTUUCxmB1OuPhtcM4j1kw/640?wx_fmt=png&from=appmsg)

**文章**

# [不要错过哦，这可能是汽车网络安全产业最大的专属社区！](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&chksm=e9270eacde5087bacb4d9c888f3a21ceae227156c89aba0be7d9ebc8b02a68b4f11e7595255a&scene=21#wechat_redirect)

[关于涉嫌仿冒AutoSec会议品牌的律师声明](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247531034&idx=2&sn=e466ca3e7c2927a91dd9a81be705afe1&chksm=e9273ec1de50b7d7f540ae2e4c255bfb42f842228a87f7dbc65297027a878544a9e796e09cf6&scene=21#wechat_redirect)

[一文带你了解智能汽车车载网络通信安全架构](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247517280&idx=2&sn=8bfafb17871598c9cc0041bc9ee5f65d&chksm=e927c0bbde5049ad8cdb3647f6cdfce00c2db7a7b484941027bb7edf3128e4eaa74d6727dd46&scene=21#wechat_redirect)

[网络安全：TARA方法、工具与案例](http://mp.weixin.qq.com/s?__b...