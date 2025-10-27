---
title: AI驱动机器人暴关键漏洞，可致机器人失控执行危险行为
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787055&idx=1&sn=5fbaf89659bf338d051cb13fa1bf9923&chksm=8893bac0bfe433d624ae16f6ea2aac5b4e7f989baf93d651e5c5725c4a3df924fd0e735b0fb4&scene=58&subscene=0#rd
source: 安全客
date: 2024-10-19
fetch_date: 2025-10-06T18:52:46.998753
---

# AI驱动机器人暴关键漏洞，可致机器人失控执行危险行为

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb6wMaaNwVNia6clG2yRjFHNQQ5p6NXGicH86hyKWFptib4YJkpvkRnSDM4hwsqB5OrCc9o2CFSu2JJPw/0?wx_fmt=jpeg)

# AI驱动机器人暴关键漏洞，可致机器人失控执行危险行为

安全客

近日，宾夕法尼亚大学的工程研究团队揭示了**AI驱动机器人中存在的关键漏洞，这些漏洞可以被恶意操控，导致机器人执行危险任务，包括引爆炸弹**。研究团队在这项研究中开发了一种名为RoboPAIR的算法，成功实现了在三种不同机器人系统上的100%“越狱”率，包括Unitree Go2四足机器人、Clearpath Robotics Jackal轮式车辆以及NVIDIA的Dolphin LLM自驾模拟器。

乔治·帕帕斯教授在声明中表示：“我们的研究表明，目前大型语言模型与物理世界的集成并不够安全。”

研究的第一作者亚历克斯·罗比指出，解决这些漏洞不仅仅需要简单的软件补丁，还需要全面重新评估AI在物理系统中的整合。**越狱，简单来说，就是绕过AI系统内置的安全协议和伦理约束**，这一概念在iOS早期已被广泛应用，爱好者们通过巧妙的方法获取手机的root访问权限，从而执行苹果未批准的操作。

在AI和机器人领域，越狱涉及利用精心设计的提示或输入操控AI，利用其编程中的漏洞。这些漏洞可能导致AI无视其伦理培训和安全措施，执行其明确不应执行的操作。**在这项研究中，研究人员成功地使机器人执行了诸如闯红灯、冲撞行人、引爆炸药等危险行为。**

在研究发布之前，宾夕法尼亚大学已通知相关公司，并与制造商合作以提升AI安全协议。罗比强调：“发现系统的弱点能够让其变得更安全，这对于网络安全和AI安全都是如此。”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb6wMaaNwVNia6clG2yRjFHNQIiaVvajibdMFvRIXuxwYPPNuYJx423xPYicaMNZr5l6o3eGWlJDO4Z9eg/640?wx_fmt=other&from=appmsg)

研究人员还指出，越狱对日益依赖提示工程的社会造成了影响，尤其是大型语言模型（LLMs）和具身AI系统。研究团队在论文《Bad Robot: Jailbreaking LLM-based Embodied AI in the Physical World》中发现了三种关键弱点：

**1.螺旋式漏洞传播：**在数字环境中操控语言模型的技术可以影响物理行为。例如，攻击者可能让模型“扮演恶棍”或“像醉酒司机一样行事”，从而让其行为偏离预期。

**2.跨领域安全不一致：**AI可能口头拒绝执行有害任务，但仍可能采取导致危险后果的行动。例如，攻击者可以调整提示格式，让模型误以为它在按预期行为，而实际上却在做有害的事情。

**3.概念欺骗挑战：**恶意行为者可能诱使具身AI系统执行看似无害的动作，然而这些动作结合起来可能导致有害结果。

研究人员测试了277个恶意查询，发现这些系统能够被操控以执行有害行为。除了在机器人领域的研究，团队还探讨了软件交互中的越狱，旨在帮助新模型抵御这些攻击。

这场研究人员与越狱者之间的猫捉老鼠游戏，使得越狱方法越来越复杂，以应对不断进化的AI模型。而随着AI在商业应用中的使用增加，模型开发者也面临更多挑战。比如，AI客服机器人已被人们诱导给出极端折扣，甚至推荐含有毒食物的食谱。

在这样的背景下，我们更倾向于选择一个拒绝引爆炸弹的AI，而不是一个礼貌地拒绝生成冒犯内容的AI。AI的安全性问题，不容忽视。

文章来源：

/https://decrypt.co/286994/how-researchers-hacked-ai-robots-into-breaking-traffic-laws-and-worse

**推荐阅读**

|  |
| --- |
| **01**  ｜[新技术绕过“noexec”，](http://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787042&idx=1&sn=9ff9664f254d1077000edf4df5aeb18b&chksm=8893bacdbfe433dbddfdff5e5b5ff909029b141c9c1b7ddb9543066891e251c28569991008e3&scene=21#wechat_redirect)[Linux](http://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787042&idx=1&sn=9ff9664f254d1077000edf4df5aeb18b&chksm=8893bacdbfe433dbddfdff5e5b5ff909029b141c9c1b7ddb9543066891e251c28569991008e3&scene=21#wechat_redirect)[执行风险激增](http://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787042&idx=1&sn=9ff9664f254d1077000edf4df5aeb18b&chksm=8893bacdbfe433dbddfdff5e5b5ff909029b141c9c1b7ddb9543066891e251c28569991008e3&scene=21#wechat_redirect) |
| \_ |

|  |
| --- |
| **02**  ｜[学校遭国家级黑客与勒索团伙的双重网络威胁](http://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787034&idx=1&sn=601d3128dda5bfa5e68dd68383a041e6&chksm=8893baf5bfe433e3ec3f75a4834085c3e9714c020268cd733fcb4f2de2390a547ffe654f9133&scene=21#wechat_redirect) |
| \_ |

|  |
| --- |
| **03**  ｜[全球资产管理巨头富达投资数据泄露](http://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787018&idx=1&sn=b72e450d8e3ce822c45ac404d55c09c0&chksm=8893bae5bfe433f3607adef80ddb4a56e18862f1836c8772208a5b19b12dabb29b927a067013&scene=21#wechat_redirect) |
| \_ |

**安全KER**

安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb6wMaaNwVNia6clG2yRjFHNQg2QKEvVXY7cJ4EyK9icHuUOiaJYTiabwryUSYOibTl848Ht2tRtsWib29lQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb6wMaaNwVNia6clG2yRjFHNQxHL3zSexIib1xnew1vkwJRBiaeRt6dOG50x4SmuzMp8Jt1zG4mttFvog/640?wx_fmt=png&from=appmsg)

**注册安全KER社区**

**链接最新“圈子”动态**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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