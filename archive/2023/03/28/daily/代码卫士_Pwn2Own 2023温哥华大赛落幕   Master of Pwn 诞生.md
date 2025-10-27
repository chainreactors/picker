---
title: Pwn2Own 2023温哥华大赛落幕   Master of Pwn 诞生
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516047&idx=2&sn=a225997cb03f9f055833105eda14fa4c&chksm=ea948ee5dde307f330a1543027a79928971a225c3b8568cdaabcda54ce90828671c0cdca112d&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-28
fetch_date: 2025-10-04T10:53:31.671054
---

# Pwn2Own 2023温哥华大赛落幕   Master of Pwn 诞生

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTshNd2iamlSye8z4iap7MWpribTMhWlgsLiaHtNWicEMnlStZiakoP3SnLw8eDcAZFzQcZj6Lyr9R39VQg/0?wx_fmt=jpeg)

# Pwn2Own 2023温哥华大赛落幕 Master of Pwn 诞生

ZDI

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**为期三天的2023 Pwn2Own 温哥华大赛落下帷幕。来自十个国家的参赛选手共发现27个唯一漏洞，获得超百万美元 (1035000) 的赏金和一辆特斯拉。本届大赛的Master of Pwn 是Synacktiv 团队，他们以53个积分点、53万美元、一辆特斯拉 Model 3夺得Master of Pwn的称号，并获得2.5万美元的奖金。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTshNd2iamlSye8z4iap7MWprwkicMhpjfxSvGAKXP84E5RFLBZwfjfdeLUQB3OERkvH5SO3XlW1eo6A/640?wx_fmt=png)

*图1：排行榜*

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTshNd2iamlSye8z4iap7MWprJEdC2icYJIrXx0zFbnWrSSWwVgVPcr7eQygD9bVjP91GEndd51CO0kg/640?wx_fmt=jpeg)

*图2：冠军团队*

****我们将以时间顺序回顾这一精彩赛事的比赛情况。首先回顾下比赛类别，包括虚拟机、web浏览器、企业应用、服务器、本地提权、企业通信以及汽车七大类。****

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTshNd2iamlSye8z4iap7MWprKtUCD1o6hEWdYha9fceo4ib5OicmOxrADU9YCpeRqr8ibxphPZ10Iq3cA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTshNd2iamlSye8z4iap7MWprKtUCD1o6hEWdYha9fceo4ib5OicmOxrADU9YCpeRqr8ibxphPZ10Iq3cA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTshNd2iamlSye8z4iap7MWprTHd0JQTJ9olAg7se9yV6g0EibTLvj0QmlCAXficsPrSZCGDJ1u9uAOyw/640?wx_fmt=png)

**第一天比赛情况**

|  |  |  |
| --- | --- | --- |
| **结果** | **战队** | **经过** |
| 成功 | Haboob SA | AbduAziz Hariri 通过由6个漏洞组成的逻辑链，利用可导致逃逸杀向和绕过被禁API列表的失败补丁，对Adobe Reader 成功发动攻击，他由此获得5万美元的赏金和5个积分点。 |
| 失败 | Last\_minute\_pwnie | 未能在规定时间内使Ubuntu exploit起作用。 |
| 成功 | STAR Labs | 成功利用由2个漏洞组成的利用链攻击微软SharePoint，由此获得10万美元奖励和10个积分点。 |
| 成功 | Qrious Security | Bien Pham 通过一个界外读和基于栈的缓冲区溢出漏洞利用Oracle VirtualBox，由此获得4万美元奖励和4个积分点。 |
| 成功 | Synaktiv | （1）   成功对特斯拉网关执行TOCTOU攻击，获得10万美元奖励和10个积分点，以及一辆特斯拉Model 3。  （2）   使用一个TOCTOU漏洞在苹果macOS 上提权，获得4万美元赏金和4个积分点。 |
| 撞洞 | STAR Labs | 成功攻击Ubuntu Desktop，但所用exploit   是此前已知的，不过仍然获得1.5万美元的赏金和1.5个积分点。 |
| 成功 | Marcin Wiązowski | 成功通过一个输入验证不当漏洞提升Windows 11的权限，为此获得3万美元的赏金和3个积分点。 |
| **总结：**共为12个唯一0day颁发37.5万美元的赏金和一辆特斯拉Model 3。 | | |

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTshNd2iamlSye8z4iap7MWprKtUCD1o6hEWdYha9fceo4ib5OicmOxrADU9YCpeRqr8ibxphPZ10Iq3cA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTshNd2iamlSye8z4iap7MWprTHd0JQTJ9olAg7se9yV6g0EibTLvj0QmlCAXficsPrSZCGDJ1u9uAOyw/640?wx_fmt=png)

**第二天比赛情况**

|  |  |  |
| --- | --- | --- |
| **结果** | **战队** | **经过** |
| 成功/撞洞 | Synacktiv | （1）   通过由3个漏洞组成的利用链，以Host EoP 成功攻击 Oracle VirtualBox。虽然由于其中一个漏洞是此前已知的，但仍然获得8万美元赏金和8个积分点。  （2）   通过一个堆溢出和一个界外写成功利用特斯拉车载娱乐系统不受限root。他们获得第二级别的奖励，获得25万美元赏金和25个积分点。  （3）   使用一个不正确的指针扩展在Ubuntu Desktop 上实现提权，获得3万美元赏金和3个积分点。 |
| 成功 | Team Viettel | （1）   通过由2个漏洞组成的利用链成功攻击微软Teams，由此获得7.5万美元的赏金和8个积分点。  （2）   通过一个未初始化变量和一个释放后使用漏洞成功利用Oracle VirtualBox，获得4万美元赏金和4个积分点。 |
| **总结：**共为10个唯一0day 颁发47.5万美元的赏金。 | | |

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTshNd2iamlSye8z4iap7MWprKtUCD1o6hEWdYha9fceo4ib5OicmOxrADU9YCpeRqr8ibxphPZ10Iq3cA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTshNd2iamlSye8z4iap7MWprTHd0JQTJ9olAg7se9yV6g0EibTLvj0QmlCAXficsPrSZCGDJ1u9uAOyw/640?wx_fmt=png)

**第三天比赛情况**

|  |  |  |
| --- | --- | --- |
| **结果** | **战队** | **经过** |
| 成功 | ASU SEFCOM | 通过双重释放漏洞成功利用Ubuntu Desktop，获得3万美元赏金和3个积分点。 |
| 失败 | STAR Labs | 无法在规定时间内使微软Teams 利用运行。 |
| 成功 | Synacktiv | 通过一个释放后使用漏洞成功攻击Windows 11，获得3万美元赏金和3个积分点。 |
| 成功 | Theori | 通过一个释放后使用漏洞成功攻击Ubuntu Desktop，获得3万美元赏金和3个积分点。 |
| 成功 | STAR Labs | 使用一个未初始化变量和一个释放后使用漏洞成功攻击 VMWare Workstation，获得8万美元赏金和8个积分点。 |
| 撞洞 | Qrious Security | 成功攻击Ubuntu Desktop，但exploit为之前已知，但仍然获得1.5万美元的赏金和1.5个积分点。 |
| **总结：**Synacktiv 团队最终以53万美元的赏金、2.5万美元的奖金和1辆特斯拉Model   3问鼎Master of Pwn。 | | |

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[Pwn2Own 2023迈阿密大赛Master of Pwn诞生](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515624&idx=1&sn=0a54c1cb263d58d376e3709b3ad40342&chksm=ea948c82dde30594c7f3fc1ddff5214e65ddc1a2ce4de055eee00ece6135a67337fbcbd0d617&scene=21#wechat_redirect)

[2023 Pwn2Own 温哥华大赛公布目标和奖金](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515297&idx=1&sn=33f273731b9c3642e6bd57eadb2fa55c&chksm=ea948dcbdde304dd5bdce8ceb813d29a9a4882b4bd207bc2ee833661aaa1e3b8579b1175e134&scene=21#wechat_redirect)

[Pwn2Own 2022多伦多大赛Master of Pwn 诞生](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514975&idx=1&sn=092fe6b1273fbcc30a4f95941bbb65cf&chksm=ea948a35dde30323ac771eceed8d6b0cf4f156d112d38a5021da7664d261d78ae4626ec760a7&scene=21#wechat_redirect)

[Pwn2Own 2023迈阿密春季黑客大赛公布目标和奖金](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514911&idx=1&sn=edfb9902c59192447f4321dcba4b8d8d&chksm=ea948a75dde30363473d0e6eb0d684bc020aeaedc29885efc225876e18dd85ea482860ebc6b8&scene=21#wechat_redirect)

**原文链接**

https://www.zerodayinitiative.com/blog/2023/3/24/pwn2own-vancouver-2023-day

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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