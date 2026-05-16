---
title: UDS，进入Bootloader等同安全解锁，接受否？
url: https://mp.weixin.qq.com/s/uApB0bltb5Eeb8qm2-Qkow
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:11:45.933401
---

# UDS，进入Bootloader等同安全解锁，接受否？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaAg55d2oRUjrmCyMjC8ib5NgWR97dTrC6PE1IIaBbtPMLdUk5HTvwW0h5c2OOrMjs1RSlb7dOgnN7DDYfg2JfO1WK2huYc5p48E/0?wx_fmt=jpeg)

# UDS，进入Bootloader等同安全解锁，接受否？

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于开心果 Need Car
，作者开心果 Need Car

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7xmZWjMxkpzia4Ft2qUbKVib3waicn3vUKRjoL8iaKrC191A/0)

**开心果 Need Car**
.

号主：开心果 Need Car，主要从事汽车Autosar开发，公众号主要分享 通信、诊断、存储、网络管理、标定、Bootloader等工程开发问题。致力于将学到的知识，分享给更多的Autosar从业者，努力解答一线开发工程师的困顿！

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572731&idx=2&sn=c138b1b1bce7ef6c8f8d8b93df959bcd&scene=21#wechat_redirect)

控制器的主芯片中，往往不是单个程序的单打独斗，而是多个进程的相互配合，进而使得控制器发挥它应有的功能。一块主芯片会包含哪些程序呢？如果项目包含信息安全，一般来说，主芯片会包含：信息安全Bootloader程序，信息安全Application程序，用户Bootloader程序，用户Application程序等。示意如下：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8wLfPv1ydWVqnbiafn4rPcVehrul3PUKgVcaZmiaNEvafbcT4zfhNTnT1M3jWrL4OQ3S6D5pxtYtAQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

当芯片被供电那一刻，CPU就从第一条指令开始执行，第一条指令指向哪呢？就用户的第一条指令来说，往往是指Bootloader的指令。即：CPU最开始执行Bootloader程序。但是，一个控制器的主要功能在Application程序中，所以，如果要控制器“干活”，也就必须让程序进入Application，所以，这就有了Bootloader跳转（Jump）Application的讨论。

为了防止软件程序的非法访问和破环，对于软件的操作都需要格外的小心，所以，在UDS（Unified diagnostic services）的规范中有了0x27（Security Access service）和0x29（Authentication service）服务。

可是，有这样一种场景：如果芯片只有Bootloader程序或者Application程序失效，Bootloadert程序目前无法跳转Application程序。示意如下：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8wLfPv1ydWVqnbiafn4rPcVpnzico67bEBdkrQpcibmibde2Cpriaa1TzcfiawxIpsQqmiaXJxiaa3KqpqEA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

对于这样的工况，Bootloader程序是否还需要安全解锁？或者说，一旦程序进入了Bootloader程序，默认处于解锁状态，无需额外的0x27服务？是否可行呢？

个人观点：对于Bootloader来说，它最大的作用就是更新程序。所以，当程序进入Bootloader程序以后，就保持解锁状态是可以接受的。因为，程序进入不了Application或者没有Application，控制器是无法工作的，如果不能重新更新，控制器就等同于“砖”（brick）。

但是，有的小伙伴就问题：进入Bootloader和是否使用0x27/0x29服务不冲突呀。确实不冲突，但是，我们这里在讨论，不用0x27/0x29服务又怎样呢？难道就不升级？我们使用0x27/0x29服务的目的主要为了避免非法刷写的问题。就是说，需要确保更新程序得合法性。否则，程序就可能被恶意篡改，甚至使得产品被逆向和复制。

所以，如果不使用0x27/0x29服务，就得确保软件更新的合法性，即：下载到控制器内的Application或者其他组件是真实的，完整的。如何保证呢？软件下载以后，往往需要使用公钥（Public key）验证下载软件的合法性，所以，下载软件的真实性和完整性是可以得到保证的，示意如下：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8wLfPv1ydWVqnbiafn4rPcViauIRMIuqAW783NdL2Qb2ib9ljemvSc8OibWko1MFI1JEVVaRAkibciawAw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

延伸：如果0x27对应的安全级（Security Level）已经解锁，当前的安全级再次收到种子请求时，Server可以通过返回全0表示当前Security Level已经解锁，14229-1规范对应的解释如下：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8wLfPv1ydWVqnbiafn4rPcVSnCHa9gp1XTh6ytbux3ngLjpS22Fc9bkgVs3pk9Om8C3etrW9kcDlA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

**延伸拓展：**

在144229-1的规范中，已经给出了seed的请求处理方式。具体的细节描述在Table I.2，其中No.5的解释如下：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8wLfPv1ydWVqnbiafn4rPcVtIxIRnJqnEURQb5zkB13ibhUJTkILfGGg7MmKt2UBM6ZHHFCEoib9GZw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

关于Static\_Seed、Xx、Yy的描述如下所示：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8wLfPv1ydWVqnbiafn4rPcVf2oa4xFw54Fb9NtTuXKC26JZRyYxSDAU7ficgoicicqtF57XWdkpav8rg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

红框内容的具体解释：

（一）第一种情况

Condition：收到 SecurityAccess requestSeed 请求。且Static\_Seed == True。请求的securityAccessType已有一个活动的存储种子（seed）。

Action：保存子功能（SubFunction），即 xx = securityAccessType。

发送 SecurityAccess 正响应，并使用当前存储的种子作为请求的 securityAccessType 的种子。再次保存子功能。

解释：如果 ECU已经有对应类型的种子，就直接返回这个种子，不重新生成。

那么，Static\_Seed == True的前提下，存储的种子何时清除呢？规范要求如下：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8wLfPv1ydWVqnbiafn4rPcVuUibavVBAcn0ugQw9TZLlmp3q2IjqYMHzFUsw2d5w0xJpBEjgtwjicfw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

即：收到正确的key以后，如果Static\_Seed == True，清除生成的Seed。

（二）第二种情况

Condition：收到 SecurityAccess requestSeed 请求。Static\_Seed == True。请求的 securityAccessType 没有活动种子（与之前的类型不同）。

Action：为请求的 securityAccessType 生成并存储新的种子（如果当前 ECU运行周期内尚未生成）。保存子功能（SubFunction）。发送 SecurityAccess 正响应，并将新生成的种子作为活动种子返回。

解释：如果ECU没有对应类型的种子，就生成一个新的种子并返回。

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAgXyLqfnkPJhyibCoBSOMGSsdQ03SEf01kcUbPAEzhf5nb6vyvYWINevstJCARUgy8qNpTa2lKVo7g7RPFm8IicY9aYtviaowaTE/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaD9qjQXZdMwY876TkFlhIUib1kn4wc72e4cib9eharylSOXtAgAq234jTmZYKrXsGd0OALDotYN7MYS8h0mElMEuPddlDZic56KCg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572912&idx=3&sn=58184d21d6dabc713e8d93a0c1d80e40&scene=21#wechat_redirect)

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

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦尔、大疆、日立、哈曼、华为、百度、联想、联发科、普瑞均胜、德赛西威、...