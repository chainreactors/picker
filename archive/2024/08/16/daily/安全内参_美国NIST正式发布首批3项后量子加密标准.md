---
title: 美国NIST正式发布首批3项后量子加密标准
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512404&idx=2&sn=5b1e0cf87892ec405693b086d209db97&chksm=ebfaf674dc8d7f62e0790970cc44fb107a0af6a426758b2e2330431264dac6338c90413eefbd&scene=58&subscene=0#rd
source: 安全内参
date: 2024-08-16
fetch_date: 2025-10-06T18:04:00.060723
---

# 美国NIST正式发布首批3项后量子加密标准

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7voBJ5yvszW9ciaZqxZMEXVOklNuMUTrVy2gvoBhmLQwzwu5yuJibGyf1McH8sWpjkj70ia6OUkJM9uA/0?wx_fmt=jpeg)

# 美国NIST正式发布首批3项后量子加密标准

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvbN6HVkEzyuTVx30vmw4PI2HbRdRmVpPwicubcaulGYSBaxWialQfX9xUZYzhwRhpQNUB8uUB4m9F1Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

经过多年的评审与筛选，美国国家标准与技术研究院（NIST）本周正式敲定了三项用于应对量子计算威胁的加密算法，这标志着全球首批后量子（post-quantum）安全加密标准的诞生。

早在2016年，随着量子计算技术逐渐从理论走向现实，NIST便呼吁全球密码学家开发新的加密标准，以应对量子计算可能带来的威胁。传统的加密算法如RSA，因其基于大数分解等问题，在量子计算机面前不堪一击。

**首批三项标准胜出**

经过数年评审，NIST从69个提交的算法中筛选出了三项新标准，分别是ML-KEM、ML-DSA和SLH-DSA，有望将成为NIST量子安全战略的基石。

以下是首批通过的三项后量子加密标准：

* ML-KEM是基于模块格的密钥封装机制，速度很快，适用于快速加密操作，如安全访问网站。
* ML-DSA则是用于数字签名的标准，能够确保文件或软件在传输过程中的完整性和真实性。
* SLH-DSA同样是一种数字签名标准，但其安全性更强，代价是需要更大的签名或更长的签名生成时间。

值得注意的是，另一个名为Falcon的算法也通过了初审，但尚未被选为首批标准之一。NIST表示，将继续评估其他算法，并计划在未来几个月内宣布约15个进入下一轮测试和分析的算法。

**新标准的基石：格密码学**

成为首批标准的三个算法均基于格密码学（Lattice-based cryptography），是一种与传统密码学大相径庭的数学机制。这三种新算法都是为非对称加密而设计的，即用于对消息进行编码的密钥与用于对消息进行解码的密钥不同。

格密码学利用“背包问题”等复杂数学问题，不仅对传统计算机具有极大的挑战性，量子计算机同样难以破解。

IBM密码学研究员Gregor Seiler表示，所谓的“背包问题”是指：从一组非常大的数字中取出一些数字并将它们相加。总数是另一个大数。数字相加很容易。但要弄清楚哪些数字被用来加到这个总数是非常困难的。基于格的密码学采用了这个想法，并增加了难度。背包里不再装满数字，而是装满了向量。

**向量子安全迁移**

**除了数学加密算法之外，NIST还公布了相关的实现细节。**

NIST量子加密标准化项目负责人、数学家达斯汀·穆迪（Dustin Moody）表示，尽管未来还会有更多标准出台，但企业应立即开始使用首批三个后量子加密标准，以应对潜在的量子计算攻击风险。他指出，这三项算法将成为主要的量子安全标准，其他标准则作为备选方案，以应对未来可能出现的安全挑战。

“我们不必等待未来的标准，”穆迪在公告中表示：“请立即开始使用这三项标准。我们需要做好准备，以防现有标准遭到攻破，我们也将继续制定后备计划以确保数据安全。但对于大多数应用来说，这些新标准将是主角。”

企业需要注意的是，量子安全加密比以前的加密演变更加复杂，因为算法与传统加密有很大不同，因为有多种不同的算法可用于不同的用例，并且软件供应链比以往任何时候都更加复杂。

总之，随着算法的更新迭代，企业需要保持灵活性，才能迅速适应新的、更有效的量子加密安全标准。

参考链接：

https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

文章来源：GoUpSec

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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