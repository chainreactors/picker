---
title: G.O.S.S.I.P 安全预警 2024-07-09 这是谁的学院？
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498394&idx=1&sn=bfac1007730b4230ace881c546700011&chksm=c063d443f7145d5536d98d7b9ca887fb0d9e65404a99f141620e1a87d13cb5b4f6ce9bf40910&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-07-10
fetch_date: 2025-10-06T17:45:33.382661
---

# G.O.S.S.I.P 安全预警 2024-07-09 这是谁的学院？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GECUWHkLuxLYRgqyW7icZqhDoqWkeicOxhHwOQSaWkFibffI3liaunzWjz5WS0dRamw6sO4icFmWZcnQg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 安全预警 2024-07-09 这是谁的学院？

原创

L0tus@iKun

安全研究GoSSIP

> 计算机安全的所有问题，都只是CVE吗？

在一个风平浪静（但是全球变暖）的夜晚，G.O.S.S.I.P 成员在阅读一篇古老的技术文章时，对作者的学校（Helsinki University of Technology）产生了好奇，于是随手Google了一下，结果不搜不知道，一搜吓一跳：在打开Google根据地理位置推送的其他信息标签时，看到了如下的令人瞳孔地震诧异的信息（你在下图中看到了什么熟悉的名字？）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GECUWHkLuxLYRgqyW7icZqhuCuBjKfztcBpLV5PXFWa6C4CcicGPw2ToZRXNzAFOjYgPBlUcdPMIKw/640?wx_fmt=png&from=appmsg)

What the hack? Kunkun?

在反复确认了不是我们因为爱坤而导致Google缓存了相关信息，也不是因为我们老眼昏花看错之后，一瞬间很多可能性飘过了我们的脑细胞。消息源污染？供应链攻击？学校官网被黑了？智能推荐的模型被投毒或输出了什么奇怪的训练数据？莫非，难道，坤坤真冠名了一所学院？？

天马行空的猜测结束后，我们去Google Map上进行了“实地”调查，发现在地图上，确实有这么一所**阿尔托大学蔡徐坤艺术学院**！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GECUWHkLuxLYRgqyW7icZqhcwBHlqYcw6c2O4UcZ6zYZ2jiaSToXlvYpgqmx3YXIMQOl1f5YfOMHbw/640?wx_fmt=png&from=appmsg)

因为阿尔托大学蔡徐坤艺术学院和赫尔辛基理工大学是两所地理位置比较接近的大学，所以在搜索的过程中，被Google连带推荐给了用户，所以前面我们搜索Helsinki University of Technology的时候就顺路发现了这所堪比霍格沃茨的学校。

可是，如果我们把Google Map切换为默认语言（英文）时（但是我们勉强考过了大学英语四级），居然发现一切信息都回归了正常？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GECUWHkLuxLYRgqyW7icZqhH0evtm8yMdLsrpowIjWlcZHciaz7PJykPHt4m5URzP1wibwpjRFmEdRg/640?wx_fmt=png&from=appmsg)

这究竟是为什么呢？iKun已经买了中文版Google Map的热搜？

把Google Map定位到东京，进行搜索，我们发现了一堆类似的“错误”地名，一些跟坤坤风马牛不相及的地点，在中文显示的时候，就莫名其妙地被冠以奇怪的中文别名：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GECUWHkLuxLYRgqyW7icZqhL998SThty7lLJU7aoZG1JlXfXCeUy7kvjRauhQibqR00XoJOO5QNL4Q/640?wx_fmt=png&from=appmsg)

你以为这只是一个玩笑？不是的！是一群善良的人在警告我们！

---

为了研究了这个问题的根源，我们进行了深入的分析，最后猜测，这种现象的发生，因由于Google Map允许使用者进行协作，为特定的地点补充相关的信息修改建议（特别是非本国语种，如下图所示）。实际上，每个用户都可以对觉得奇怪的地点提出修改建议，不过到底是谁来审核并通过，是不是审核者对于非母语的不熟悉，可能看到的中文字符都觉得是对的，就任其通过了？又或是每个修改建议都被交给AI去检查了呢？我们不得而知。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GECUWHkLuxLYRgqyW7icZqhzXLmx5SLfaDLiaib0JsI4WMFAXn7szJt5ptPRcJicA9RdLLRXxUIRnnicQ/640?wx_fmt=png&from=appmsg)

不过，作为安全研究人员，我们对于这种现象的存在格外的敏感，大家可能看了以后，除了感受到恶趣味然后一笑而过，不会深入考虑太多。但是，想象一下这几年大家报复式地出国旅游，在国外总不可能用国内这些高x地图百x地图吧，然后很多人查询的时候也许又不熟悉当地的文字（你去希腊试试），这背后会不会有很大的安全隐患呢？

试想一下，一个去东南亚某国旅行的人，想要寻找男士会所吃饭的地方，于是就在Google Map上打开中文界面，浏览附近的男士会所餐厅。在异国他乡，显然是跟随地图最靠谱，可是如果想去的地方真的是想去的地方吗？既然阿尔托大学都能被坤坤收购，你怎么知道你想要去的地方不是被一些别有用心的人进行了恶意修改呢？这种真实世界的钓鱼攻击，比网络世界的钓鱼攻击钓到的鱼大多了，上钩的鱼不光可以做烤鱼，还可以取腰子呢！

看完了我们这篇文章，你是不是要感谢坤坤！如果没有他，我们就不可能从这种玩笑般的存在中发现潜在的风险，毕竟除了本地人，谁也不会从一个正常的地名上看出来什么蹊跷。所以我们不仅要注意辨别，在国外搜索地点的时候一定要多留心多确认，同时，如果你去过一个地方，再看到Google Map上这种怪异的地名时，可以积极提交修改（举报），拯救更多人的腰子防止错误信息的传播。

最后，我们要特别致谢iKun，用这么一种隐秘而伟大的方式提醒了大家，谢谢你们！！！

预览时标签不可点

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