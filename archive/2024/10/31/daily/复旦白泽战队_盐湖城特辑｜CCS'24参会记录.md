---
title: 盐湖城特辑｜CCS'24参会记录
url: https://mp.weixin.qq.com/s?__biz=MzU4NzUxOTI0OQ==&mid=2247491218&idx=1&sn=f34b55eedb1ec6a12d5dc5f19b0ff57a&chksm=fdeb9aecca9c13fa3cfde3ae8c4ed8e8d5e8340b04e2f42a8e7a12c0d4cf4ad2a508366d4974&scene=58&subscene=0#rd
source: 复旦白泽战队
date: 2024-10-31
fetch_date: 2025-10-06T18:54:57.508873
---

# 盐湖城特辑｜CCS'24参会记录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RyyHWbbqW84TPfnZiaaKbTI0DKViaIBML5qFEguf5TAUxwgV3vLmpb9HsAiaqZ3BuVk8g9jeteXlL9JHfDOyQZ4XQ/0?wx_fmt=jpeg)

# 盐湖城特辑｜CCS'24参会记录

原创

K

复旦白泽战队

**白泽CCS'24参会小记**

2024年10月14日-18日，第31届计算机和通信安全大会（ACM Conference on Computer and Communications Security，CCS 2024）在美国盐湖城举行。

    本次CCS我们派出了来自白泽团队的博士生肖浩宇作为代表，为大家带来了关于隐私、AI安全、IoT安全方向的3场网络空间安全方向的论文报告，还与来自世界各地的优秀安全研究者线下面基，并游览了紧邻盐湖城被誉为“美国的死海”的的大盐湖。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW84TPfnZiaaKbTI0DKViaIBML5NcEEfmdgzKHDJhGvh1iaiaibnH4EGicJjUQdq2F7ERddUnAoLrJxRJxTnQ/640?wx_fmt=png&from=appmsg)

肖浩宇博士生（左一）

**NEWS**

**Part1 论文分享**

**Session – Usability and Measurement: Measuring and Understanding Privacy**

在这一session中，我们分享了关于移动应用运行时隐私通知 (RPN) 的最新研究成果：Are We Getting Well-informed? An In-depth Study of Runtime Privacy Notice Practice in Mobile Apps

    本篇工作首次系统研究了RPN在移动应用中的实践情况，致力于帮助理解现有RPN的生态、RPN实践与法律要求间的差距，以及造成此类差距的深层原因。为实现这一点，白泽成员们设计了一个自动化工作流程RENO，来高效且大规模地识别、提取和分析移动应用的RPN。在RENO的帮助下，我们分析了来自19个欧洲国家4,656个移动应用，并发现了许多有趣的结论。例如，77.10%的用户数据收集行为缺乏运行时隐私通知，且86.36%提供RPN的数据收集行为只呈现了3个通知元素，并不能满足GDPR要求的7个。通过调查，我们发现了造成这类隐私不合规问题的多个关键元素。例如应用商店不对RPN作强制要求，这导致开发者认为RPN是一个可选的隐私政策。这些研究成果都说明了RPN提供的用户数据收集迫切需要更高的透明度。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW84TPfnZiaaKbTI0DKViaIBML5o1paf7jK9J7CtzBMG8BRjiaVcGpOza482tIgHV5ZTia4uSh1jTlvHLcw/640?wx_fmt=png&from=appmsg)

**Session - ML and Security: Machine Learning Attacks**

在15号下午的ML and Security Session中，白泽博士生肖浩宇分享了来自白泽智能团队的另一项研究成果—— Neural Dehydration: Effective Erasure of Black-box Watermarks from DNNs with Limited Data。

    在这个数字时代，保护深度学习模型的知识产权变得愈发重要。黑盒水印技术作为一种保护手段，已经广泛应用于学术界和工业界，通过嵌入到深度神经网络（DNN）的预测行为中来标记模型的所有权。

    但是，黑盒水印技术并不是无懈可击的。白泽团队的研究揭示了现有主流黑盒水印技术在真实应用场景中的脆弱性。白泽成员们提出了Dehydra，一种新颖的通用水印移除攻击。白泽们的研究展示了如何利用受保护模型的内部机制来重建并移除水印信息。此外，白泽们还设计了目标类别检测和重建样本分割算法，以减少模型性能损失。

    在多个基准数据集和多种DNN架构上的全面评估显示，Dehydra成功破解了十款已有的主流黑盒模型水印技术，保留了至少90%的被盗模型的功能，同时对数据的依赖也极低，甚至能在完全零数据的场景下实现水印移除。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW84TPfnZiaaKbTI0DKViaIBML5rMnqYzpFiag93oRX7rkiaaPWOibsOkXqShgybNrnawGba82w97HI5ibDicg/640?wx_fmt=png&from=appmsg)

**Session - Security of Cyber-physical Systems**

随着IoT的普及，如何抵御IoT固件漏洞带来的安全风险也变得尤为重要。我们在这一session中为大家带来了固件漏洞检测的最新研究进展：Accurate and Efficient Recurring Vulnerability Detection for IoT Firmware。这个研究提出了一种新型的重现漏洞检测技术FirmRec。该技术克服了将重现漏洞检测应用到闭源二进制场景的多个关键挑战，包括如何在二进制场景表示漏洞语义，如何分析文本级漏洞报告获取代码级漏洞特征，如何准确和高效地利用已知漏洞签名检测重现漏洞。通过克服这些挑战FirmRec成功在320个固件上利用40个已知漏洞以远超现有工作检测到了642个漏洞，并获得了53个CVE，其中有35个漏洞评级为严重，11个为高危。相关工具已经开源在了Github，https://github.com/seclab-fudan/FirmRec/tree/main，欢迎大家follow我们的代码。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW84TPfnZiaaKbTI0DKViaIBML5hwbUc7XzPc2ZJmekeu4Y9AAEUazUUtJyIWk1NJiagUg4syPCskODZfg/640?wx_fmt=png&from=appmsg)

**NEWS**

**Part2 大会现场**

本次CCS也是盛况空前，会议现场人头攒动，汇集了来自五湖四海的安全研究人员，大家共聚一堂探讨网络空间安全的过去，现状和未来。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW84TPfnZiaaKbTI0DKViaIBML5qBmVdphXwbuXRNzvzIJjKTalH1Tjvx0aWIJkLy4ib9Uh87sRr0oXia1w/640?wx_fmt=png&from=appmsg)

本次会议一共收到了1964篇投稿，并接收了331篇研究论文。在这个过程中，要感谢各位审稿人的付出。因为你们的付出，我们才能领略到如此优质的安全研究成果。本次没有中稿的小伙伴们也不用灰心，金子总会发光的，我们尊重和敬佩为推进安全领域发展所做出的每一份努力！

![](https://mmbiz.qpic.cn/mmbiz_jpg/RyyHWbbqW84TPfnZiaaKbTI0DKViaIBML5icFGInG4Y7oD4mH79GOVOkgLeibzdobmYQe5EwqWm0ia93x3fzSZpLrdw/640?wx_fmt=jpeg&from=appmsg)

本次会议也从不同角度探讨了各个领域方向的安全问题，不仅有当下最热门的人工智能方向的安全问题、也包括了软件安全、网络安全等传统安全问题。与不同方向的研究者一起，从不同角度探讨安全问题，迸发出新的灵感火花，也是参会的一大乐趣。

![](https://mmbiz.qpic.cn/mmbiz_jpg/RyyHWbbqW84TPfnZiaaKbTI0DKViaIBML5sYKvPpCBPd5QUTw0BWfUicoPufbl60DmoRbU6mBXcEFiaELYWsLDFwgw/640?wx_fmt=jpeg&from=appmsg)

**NEWS**

**Part3 盐湖风光**

会议地点位于盐湖城位于美国犹他州，地处西部，地域辽阔，自然风光壮阔磅礴，紧靠着西半球最大的咸水湖大盐湖。趁着参会的机会，自然也要打卡一下标志性的大盐湖风光。虽然此次参会白泽er孤身一人远赴他乡，但是也很快就凑齐了一只四人复旦校友小队共赴盐湖。和志趣相同的优秀安全从业者共赏美景，从中获得的快乐也不虚此行了。也要提醒一下有意前往盐湖城的友友们，这里的深秋的气候比较干燥，寒冷（开会最后两天最低气温逼近零度），要注意水分补给和保暖呦。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW84TPfnZiaaKbTI0DKViaIBML5eVtC6UQJf3PrXj0IElOsiaJU93KHY4PG4GCzyb3rPiba6dGXuvApX2XA/640?wx_fmt=png&from=appmsg)

素材：肖浩宇

供稿、排版：肖浩宇、高思妍

责编：邬梦莹、林紫涵

审核：张琬琪、洪赓、林楚乔

复旦白泽战队

一个有情怀的安全团队

还没有关注复旦白泽战队？

公众号、知乎、微博搜索：复旦白泽战队也能找到我们哦~

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

复旦白泽战队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

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