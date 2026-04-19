---
title: 漏洞利用技术的“起源”
url: https://mp.weixin.qq.com/s/xKxghgmtRL8YTi613_5HyQ
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:47:54.677178
---

# 漏洞利用技术的“起源”

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/StcNgRRgTbdhOsogFGEYtIvahYHtQ9pqslbeY1bUUDyfjWKDN89K9a0dBqfKia7mQCiaqr2fcd2now9S6GzV4eIZOumk2mNibZ47cf7o7D6bHE/0?wx_fmt=jpeg)

# 漏洞利用技术的“起源”

原创

天御
天御

天御攻防实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hPq2VZ0zUBAwZQYIRcMGdob0eTGKx525Ddp9DrwAwWLOGwL1HNIwiayA2mzhHsdiakoCUfBmN7fib078lq2yjXTMg/640?wx_fmt=other)

本文摘选自Halvar Flake的一篇文章，书评：《这就是他们告诉我世界将如何终结》。

Halvar Flake于2021年2月写了一篇妮可所著《这就是他们告诉我世界将如何终结》一书的书评。该书试图揭示“零日漏洞市场”及其运作机制，以及美国政府在这一市场中的参与方式，同时还探讨了国家间“网络战”的多个方面。

文章中谈到了漏洞利用技术的“起源”的故事。

Halvar Flake自1990年代后期起便从事信息安全工作；曾属于一个充满玩趣精神的青年文化群体，该群体率先开发了如今被各大军事强国广泛采用的大部分软件漏洞利用技术。HF曾经营一家同时向防御方和进攻方销售技术的公司。HF撰写过大量漏洞利用程序，并发表过一篇论文，阐明了理解这些技术的理论基础。HF曾为多国政府和公民社会成员提供培训，内容涵盖漏洞利用程序的构建与分析，以及后门和植入程序的分析。HF曾花费数月时间阅读Stuxnet、Duqu以及俄罗斯Uroburos木马的反汇编代码。HF在谷歌工作了五年，主要负责协助谷歌防御政府级攻击者；随后又在Project Zero项目中工作数年，致力于推动软件行业采用更好的安全实践。

妮可似乎无法想象漏洞利用技术和漏洞利用本身并非美国的发明。书中似乎暗示，漏洞利用技术和“技艺”（是由美国国家安全局发明的，随后通过举办培训课程的政府承包商“扩散”到可能侵犯人权的“外国出生”行为体手中。

这种说法在多个层面上都是错误的、荒谬的，且带有侮辱性。

首先，它侮辱了所有非美国的安全研究者，他们一生中投入大量时间，率先开发了漏洞利用技术。

现实情况是，从美国国家安全局流出的软件漏洞利用专业知识净流量为负：过去几十年中，半代非美国漏洞利用开发者移民到美国，并最终获得美国护照。美国的漏洞利用供应链一直高度依赖“外国出生”人士。美国国家安全局会积极采用外部技术；而在过去25年中，我尚未听说有任何漏洞利用技术是从美国国家安全局“泄露”出去的，而非在外部被发明。

本书序言在讨论NotPetya时，似乎暗示俄罗斯需要借助Shadow Brokers泄露的“美国武器”才能造成严重破坏。任何对堆溢出利用历史以及漏洞开发社区有现实了解的人都知道，这种说法完全错误。

另外，

yuange表示，[NSFOCUS旧友记--yuange忆往事](https://mp.weixin.qq.com/s?__biz=MzUzMjQyMDE3Ng==&mid=2247487444&idx=1&sn=459a46cf2e38d115652bda155623b90e&scene=21#wechat_redirect)

DVE技术的文章原理是98年写的，当时还没有DEP等对抗措施。09年微软做出来DEP+ASLR等慢慢完善后，很多人都认为攻击走到了尽头比较难了，那时候我和很多人说难才更显价值。

思考怎么过这整套利用缓解措施，想到了十年前98年的文章，十年已经很久了，但是技术不会过时。很快做出来DVE漏洞利用技术，效果超级超级好。

14年公布了DVE技术，很多看不懂的喷子又把里面的一个小技巧(就这个小技巧也起码价值10万刀以上美金)当成了DVE，又在喷就这。

**推荐阅读**

**闲谈**

1. [中国网络安全行业出了什么问题？](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485457&idx=1&sn=d45cc35242cdc83e98b124531ea7c093&chksm=fb04cb79cc73426f21801f35912b626bf515dc2b9d85b3da578f8087d0a2960396ef1e6347bc&scene=21#wechat_redirect)
2. [国内威胁情报行业的五大“悲哀”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484999&idx=1&sn=485863f4e66a62f55aa69334c787e6f3&chksm=fb04c52fcc734c3919fc28c61a9b13488b89efe4c1ba5cb16f8f00f0c6e996c7f1df47984463&scene=21#wechat_redirect)
3. [对威胁情报行业现状的反思](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486063&idx=1&sn=11e005a726ced95e872e2ce7fb228ba2&chksm=fb04c907cc734011310b2cc58a4a6f1ac764ece04c7d7ca9f3e93f0849f92c5e891b32e4c58f&scene=21#wechat_redirect)
4. [安全产品的终局](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484846&idx=1&sn=35bab89f917f5043919e40893268d576&chksm=fb04c6c6cc734fd05c0423dc971a0578eb8b951ef1764be0a99e2bdd1c26b736d64cf61b6d77&scene=21#wechat_redirect)
5. [老板，安全不是成本部门！！！](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485908&idx=1&sn=b6cff013a1e9a9599bdde63ce56ecec0&chksm=fb04cabccc7343aac55b3c43020c855bade147461fece597f730bc0460e65c5610dd0f5d988b&scene=21#wechat_redirect)

**美国网络政策与战略专题**

1. [独家解读新版《美国网络战略》释放的危险信号](https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486777&idx=1&sn=1911cd25d5cd93c71bf17ed4d3a17d9a&scene=21#wechat_redirect)
2. [首发 | 特朗普政府对华网络政策评估](https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486086&idx=1&sn=15241eb0ec346072671268fe20014acb&scene=21#wechat_redirect)
3. [首发 | 美国国防部网络战略的演变](https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486174&idx=1&sn=7557d561e51c274a6fa2659698947c87&scene=21#wechat_redirect)
4. [美国政府网络政策观察（第一期） | 美国国防部将腾讯等中国公司列入"涉军企业清单"](https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486222&idx=1&sn=ad0d3c18ea016974fbdf59c21dcae00f&scene=21#wechat_redirect)
5. [特朗普上台，中美会发生网络战吗？](https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486232&idx=1&sn=5527e80a86875c017071d27f5b315e3e&scene=21#wechat_redirect)
6. [疯狂！美国安会网络官员扬言要对网络攻击者使用致命武力](https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486342&idx=1&sn=ecb3c631592968480ced965fc0d91462&scene=21#wechat_redirect)
7. [美军新增10亿美元预算用于对华进攻性网络战](https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486368&idx=1&sn=6fdb5ee85a16fcbaffbf69249ef3c393&scene=21#wechat_redirect)
8. [白宫闭门会议：授权美国私营部门进行网络攻击](https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486385&idx=1&sn=dda71bfbb1a0002fe724d68be1be8239&scene=21#wechat_redirect)
9. [特朗普政府正在推动授权私营部门进行网络攻击的法案！！](https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486501&idx=1&sn=bc11855873803a50679dc3a07071fcca&scene=21#wechat_redirect)
10. [美国公司是我们需要重视的下一个网络威胁](https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486554&idx=1&sn=67ec9a286966ec9b6492b491c2ba974c&scene=21#wechat_redirect)

**威胁情报**

1.[威胁情报 - 最危险的网络安全工作](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485331&idx=1&sn=0857185a1bc7ed04c2d1edc60cb93a34&chksm=fb04c4fbcc734dede0fd243984c30250ff7859f68a265b1a278ac72a5761ac0ccaf0038537ec&scene=21#wechat_redirect)
2.[威胁情报专栏 | 威胁情报这十年（前传）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484880&idx=1&sn=c2b5730f2a7011959096526ff775c8ac&chksm=fb04c6b8cc734fae9f6d2e0693cecd5fd594a01694d8e38bd95926cb88a0f627c3d5b2f36ea2&scene=21#wechat_redirect)
3.[网络威胁情报的未来](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485003&idx=1&sn=76253d23e51dde8dbf4d675b79ab43cf&chksm=fb04c523cc734c352490ca37f55f1c3a989d55807298cb308aa3c126e24816d6fda11a8766f1&scene=21#wechat_redirect)
4.[情报内生？| 利用威胁情报平台落地网空杀伤链的七种方法](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485042&idx=1&sn=afd1212b585f30bccdece8471fadd31d&chksm=fb04c51acc734c0c9fd0d1d388b7672defbe5ce17a10af58d3a5d336ba21fa21398b4ad860e2&scene=21#wechat_redirect)
5.[威胁情报专栏 | 特别策划 - 网空杀伤链](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484709&idx=1&sn=649a27516ca01baab49ce750e3502cc3&chksm=fb04c64dcc734f5becd252686228f6c3c2bd00bff52041e9dae6fde2008e1a43057989b9d16f&scene=21#wechat_redirect)
6.[以色列情报机构是如何远程引爆黎巴嫩传呼机的？](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486027&idx=1&sn=7d9215cbf71327fccda006c6c29938a3&chksm=fb04c923cc734035c661d4e3b93ad1e631fd55ee5a4ba7cd855c7e37bc513ca071860fdfb9b9&scene=21#wechat_redirect)
7.[对抗零日漏洞的十年（2014～2024）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486036&idx=1&sn=52131d932e8fe4f24db3d7bdf41625a0&chksm=fb04c93ccc73402a24144d8262153a73bc18c2098109a9885d2413dba9a33af83f8d664bc317&scene=21#wechat_redirect)
8.[零日漏洞市场现状（2024）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486041&idx=1&sn=1c9dc7508ba7d09c8f7c88f3018bae1d&chksm=fb04c931cc734027d17b83f774416085b6c492306ccf49f76cb99fa1fbf8b03c7ff6af23a781&scene=21#wechat_redirect)

**APT**

1. [XZ计划中的后门手法 - “NOBUS”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485524&idx=1&sn=aa2b7b0d57b250e5cc101e5dcbebbca6&chksm=fb04cb3ccc73422a9fe22937b801eceb205ceaf8bf3b76a92143d575d55e5fd2eef5adfacb36&scene=21#wechat_redirect)
2. [APT研究顶级会议](https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486477&idx=1&sn=4606b8430499a6e11ad9930aad758b1c&scene=21#wechat_redirect)
3. [十个常见的归因偏见（上）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484868&idx=1&sn=3d65e81115c967b165fa16021a211967&chksm=fb04c6accc734fba7c760fd14caaaf9a2d7991acc2557ee340e772ccbb805b30f1a46c793e8a&scene=21#wechat_redirect)
4. [抓APT的一点故事](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485237&idx=1&sn=9152fcb5f5b1f884e6da97ba9b04f69a&chksm=fb04c45dcc734d4bd8fbede2ae93dc52feeaaa11e215a3240bca32f3d43444a2c909e01a2814&scene=21#wechat_redirect)
5. [揭秘三角行动（Operation Triangulation）一](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485278&idx=1&sn=9def52d0d9063e86acb16533be2a52e8&chksm=fb04c436cc734d20b8c67348f7db21fa10921ad3826b37c713e847b73972f50de82b6c1f1e6b&scene=21#wechat_redirect)
6. [闲话APT报告生产与消费](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485325&idx=1&sn=d0219cfe811afe5e8fc8729c603de2bc&chksm=fb04c4e5cc734df3a8ad433a992172c1a9a0f236fd69550c72eb499e1202d23b81f32b379259&scene=21#wechat_redirect)
7. [一名TAO黑客的网络安全之旅](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485451&idx=1&sn=5f794deaaccf45e7d81958eba82cd556&chksm=fb04cb63cc73427538546f24b1be7cd78375a90174...