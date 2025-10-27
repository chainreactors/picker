---
title: G.O.S.S.I.P 阅读推荐 2024-12-06 小心预训练语言模型变成隐私陷阱
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499320&idx=1&sn=84b5871a92d7f701a8b9764c4f51cfe1&chksm=c063d0e1f71459f7319d0f5a3901ffa3e248b6a23dee04308942f243a31098df6743500873b1&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-12-07
fetch_date: 2025-10-06T19:40:01.298558
---

# G.O.S.S.I.P 阅读推荐 2024-12-06 小心预训练语言模型变成隐私陷阱

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21FMmNgMATNDmfXByIqXJpOBwslFWmMrU19lNzcnjhJqnrdC7MzrqRoF7oE5AW5gZ1Q0z2GA8Y0QRA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-12-06 小心预训练语言模型变成隐私陷阱

原创

李安吉@SYSU

安全研究GoSSIP

千禧一代大概率是没有经历过给报社、杂志社投稿的这种过程吧？把你的文学作品抄写在一张张稿纸上，塞进信封让它变得胀鼓鼓的，贴上邮票（甚至可能因为超重还要加钱），小心翼翼把邮寄地址写好，投进那个永远不知道什么时候会开启的邮筒，然后就回到家去忐忑不安地等待回复。等到许多天之后，在学校的**收发室**（这个名词是不是也很神奇）收到了给自己的信，这时候心跳加速，拆开看看到底里面是录用通知还是“xxx同志，很抱歉地通知您……“。习惯被这个过程PUA之后，给什么CCS投稿早就不存在心理落差了~

说了半天，其实想要介绍的是我们最近收到的一批来自中山大学南雨宏老师的学生的投稿，他们在阅读了学术论文之后，也积极地写下了阅读笔记，并把这些成果投递给了我们，交给我们分享给大家。非常感谢老师和同学们对我们的信任，也希望大家都能把互联网早期那种无私分享的精神传递下去，当然，不管你的论文阅读笔记是不是关于你自己的论文，我们都会为你送上一份礼物哦。

今天要选发的论文笔记来自**李安吉**同学，论文 *CCSPreCurious: How Innocent Pre-Trained Language Models Turn into Privacy Traps*来自2024年的CCS，由于投稿格式是PDF，排版也比较漂亮，我们就不再转格式，直接贴上相关的截图，如果需要PDF原文的读者欢迎给我们留言。

论文PDF: https://arxiv.org/abs/2403.09562

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FMmNgMATNDmfXByIqXJpOBEZibiciaia8aJJHxe4qiaCKS5QlMCkQH6RsCDDrUTiaQQdtIicel907OqTsrQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FMmNgMATNDmfXByIqXJpOBFtcDVEbkicxicZMvOgTnk8tZ5z3RXbMqdRLcJ0qia3fRSBcZ7sLt9HVLA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FMmNgMATNDmfXByIqXJpOBBrlh5v7guxKjnP7jraWUZH01hJRsAoARRsFITTcvTEicqwOc5fmRjGQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FMmNgMATNDmfXByIqXJpOBVbrq39EwFt9tl5k7icbiaHxs0D8ic6hzc5JzMPkVYroR98X3y4ByxgtOg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FMmNgMATNDmfXByIqXJpOBic3uBoS0WZPf7G9Rs4iaWMpzJUO6DHib6kQ5xA4wibtvdfmt9Ul49JY8FQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FMmNgMATNDmfXByIqXJpOBaop88a0epQiauPZCpYYjz6GI7kBRiaViaV3pfO7hTYEaRDoGlriaqdAkicA/640?wx_fmt=png&from=appmsg)

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