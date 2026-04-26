---
title: 划时代发布！DeepSeek-V4 预览版重磅登场，百万上下文从此普惠
url: https://mp.weixin.qq.com/s/0LIM0BHum3jJ5DiBgNCUPg
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:59:06.233586
---

# 划时代发布！DeepSeek-V4 预览版重磅登场，百万上下文从此普惠

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaCwmQowIM63y2mUPZNZyBesRubODEuXaKaVvLick2iaJO2rhjyM8veqlHqtEpSHjLvEicw07ra61qjCIMuvK3WT03TTBicRjWtPcBGSYTmf1b8c/0?wx_fmt=jpeg)

# 划时代发布！DeepSeek-V4 预览版重磅登场，百万上下文从此普惠

原创

Al1ex
Al1ex

七芒星实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

新版发布

2026年4月24日，DeepSeek正式推出了全新一代模型DeepSeek-V4预览版，这是继上一代V3系列之后时隔15个月的重磅更新。新模型不仅全面开源权重，还同步公布了技术报告并且已经适配国产昇腾芯片。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaCwmQowIM61j5LaML9p4h3uHvJ22W4CKceg4Pw5zxibnOEibrZMEDVP67LWI0etuSewDrlbHJksOMTBhsehzXq8QibKMORLricibUt3ZMG8PIibg8/640?wx_fmt=png&from=appmsg)

DeepSeek官方将此次发布定位为"预览版"——并非V4系列的完整旗舰,而是拉开全新世代的序幕。正如其公告中所引用的古训："不诱于誉，不恐于诽，率道而行，端然正己。"这份专注与务实，也让业界对后续正式版充满期待

模型特性

DeepSeek-V4一共推出了两个版本：Pro(旗舰版)和 Flash(经济版)。两者全部标配100万token的超长上下文，相当于一次可以处理三部《三体》的体量。

* V4-Pro：总参数1.6万亿，激活参数49B，采用MoE(混合专家)架构，性能全面向世界最顶级的闭源模型看齐
* V4-Flash：总参数 284B，激活参数 13B，主打轻量与高效，推理成本极低

![](https://mmbiz.qpic.cn/mmbiz_png/iaCwmQowIM61nzyTDAzDcjT7Ne6gl9kcrRvxuvysMyyor0jcAd3CJd298ibibhMfyEeSKEcM8TkPiayFFdT0om7ctqPJpqTGibuIhGaO4jibLxq7o/640?wx_fmt=png&from=appmsg)

在能力表现上，DeepSeek-V4-Pro的Agent能力实现了质变，尤其是在 Agentic Coding评测中，Pro版本拿下了开源模型的最佳成绩。内部工程师反馈V4在日常代码任务中的使用体验已经超越了Sonnet 4.5，交付质量接近Opus 4.6(非思考模式)。在一项内部研发编程基准测试中(约200个真实任务)，V4-Pro-Max的通过率达到67%，而Sonnet 4.5 仅为 47%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaCwmQowIM63tbpNfyDgmxwvtBFk3X5E6NHGGHWFZNb5TK4BMkFOdGUVVoHLNS52MLFe2q3N7tuVciavbzVB70FJRZ6eIuImeevuk9xJtglNc/640?wx_fmt=png&from=appmsg)

在数学、STEM及竞赛型代码任务中V4-Pro同样亮眼。HMMT 2026 Feb 竞赛数学基准得分95.2，这与Opus-4.6 Max(96.2)和GPT-5.4(97.7)差距极小；在更难的Apex Shortlist测试中甚至拿到90.2 分，超过了同场所有竞品。世界知识测评方面，Pro版本大幅领先其他开源模型，仅次于顶尖闭源模型Gemini-Pro-3.1

![](https://mmbiz.qpic.cn/mmbiz_png/iaCwmQowIM62xsAcONdVkkE9iaic4setWxCdbp1t7y8cXIeyeATC9VIVspSzuiagkUemjJJ0CY46IZAKugEHujTVicWZddLBejt2XCENEvxYp0Jc/640?wx_fmt=png&from=appmsg)

技术创新

DeepSeek-V4在底层架构上做了大胆革新。它设计了一种新型注意力机制，在token维度进行智能压缩并融合了自研的DSA稀疏注意力技术。这一组合拳大幅降低了计算量与显存消耗。

实测数据很有说服力：在100 万token的上下文长度下，V4-Pro处理一个新token所需的算力仅为前代 V3.2 的 27%，KV缓存更是只有前代的 10%。正是这种极致效率，才让 1M 上下文能够成为所有官方服务的标配

![](https://mmbiz.qpic.cn/mmbiz_png/iaCwmQowIM62vxaTQYzdom7icFMmOUxQibmRticLjNnZJicL8ecNa0J94psoEciaKO2NXPVRxX8OgYXmghsKmQVF0OYSFSIYC8LbictiboThRibbiccfo/640?wx_fmt=png&from=appmsg)

V4还在以下方面实现了技术升级：

* 预训练上下文长度从 32K 提升至 100 万 token
* 强化学习阶段采用 GRPO 算法，辅以 KL 散度校正
* 新增 KV Cache 滑窗和压缩算法，进一步降低访存开销

使用方法

目前DeepSeek-V4 API已经同步上线了V4-Pro 与 V4-Flash，我们可以通过在CC-Switch中调整模型至deepseek-v4-pro即可

![](https://mmbiz.qpic.cn/mmbiz_png/iaCwmQowIM63tiansVBKlJXxXIEkeZURxTgx6x4m8cmveKk9ia9lvGj1ib7OKlUxN7yEbMBfhZqxQQ0icGm5ic7FEUNSjNrRof5RGia0ttW55uauP4/640?wx_fmt=png&from=appmsg)

随后在Claude中直接可以看到

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaCwmQowIM62lQIPeSWWw1ribLIHcdPt8RUhCkfZMlWkpupSkPrAHgAptL5eZ0WLGlqE0vjJdlI930SQVqCJa56ZGiaibicPsKzWHWUam6EiciaXFQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaCwmQowIM61xlicibr0D555QnmNYib0RQhZM9egeFPZnCCefaxgDL6j7BYjaaVfcKHCfibBHicoqR4N5bXL6m4YGrFllnKKBwhdgmpPUAqqrZDLA/640?wx_fmt=png&from=appmsg)

目前官网的chat中以及APP端尝试还是没有适配到DeepSeek v4模型

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaCwmQowIM63ice2iaMWgTjdlPnMGZT0TxOiaGwmIOAulSkuU4LRRJHKwIZG8yoDsg9JYGWDjBuGE51K3BibwRQiaF9yalaDPFxaxywwXQulicNOrA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaCwmQowIM61Y2qgkbC7zPibQ222UEdfHIWCAOqmzUJSbv51R62CNgYG1fO3zW9cR9ial4fJFicciaoTrTqWQYRhd9VEwfNbITiaxHCDWjSkH85II/640?wx_fmt=png&from=appmsg)

模型下载

DeepSeek-V4 模型开源链接

* https://huggingface.co/collections/deepseek-ai/deepseek-v4
* https://modelscope.cn/collections/deepseek-ai/DeepSeek-V4

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaCwmQowIM63zZFJNge88FrKDJFOLicDupRogCWKiaoSQu3Br2aFbYG4bLXd0mzHJL2QBAicwyBibZmgo6VpuBo2Lx9pIDOMZCf8IJPZrgiaBrprY/640?wx_fmt=png&from=appmsg)

DeepSeek-V4 技术报告

https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek\_V4.pdf

**推 荐 阅 读**

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/PJcQz9vmUickqzRByyKzldbMOEHRbwUzHmiazrVsk32mFQGSWeuiayXUyzzibVnQv61JSSelD87SuCK0b4WEK9SicNg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=8)](https://mp.weixin.qq.com/s?__biz=Mzg4MTU4NTc2Nw==&mid=2247491634&idx=1&sn=a1873ac267a553dbe39d9b8eae72c5d1&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/PJcQz9vmUickqzRByyKzldbMOEHRbwUzHuymSGgjibhhPTabupfXRQ63icNSVu5ILUZMhaicD6icF02SQUGazFfxAsQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=9)](https://mp.weixin.qq.com/s?__biz=Mzg4MTU4NTc2Nw==&mid=2247493905&idx=2&sn=32dabb1937bb95a440a7e79d05519a44&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/PJcQz9vmUicmoCSvN9up1yJgHEP6fsXZLWVR2SkHAp3ecDzJt5T3Yq7bY4DtyD5KkErB1ZKv1BJqRiaQRGfevfXw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=10)](https://mp.weixin.qq.com/s?__biz=Mzg4MTU4NTc2Nw==&mid=2247492829&idx=2&sn=8b06dc14b5843d622465cb26c6ddbbe5&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/PJcQz9vmUickqzRByyKzldbMOEHRbwUzHIaBgzXLZTzKELSmO0826xOlmn3q7U2t188XgsNw6TQKg4Qnqakb4DA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=11)](http://mp.weixin.qq.com/s?__biz=Mzg4MTU4NTc2Nw==&mid=2247491787&idx=2&sn=509e2b46d9144323fc9d13a1567296c3&chksm=cf611bc3f81692d5579b8a9128ff711eea3f7660b1ccd884e0be264e895fbfcb4c995c609be8&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/PJcQz9vmUicmoCSvN9up1yJgHEP6fsXZLWcWm0PwrtU8k03ib2zf8F27icMJ1qGH1gcMvCImQiaLw1tEiaJ6OkRZmOQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=12)](http://mp.weixin.qq.com/s?__biz=Mzg4MTU4NTc2Nw==&mid=2247491804&idx=2&sn=eb334c8bb0be9ea0a3baf21db6e8fd07&chksm=cf611bd4f81692c2e80f7855552fdb63b52b89c8b4fbfd50fabbf7cf478aff60c23ff0c22d8c&scene=21#wechat_redirect)横向移动之RDP&Desktop Session Hija

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iaCwmQowIM61mkJ2Me0v9ribBLiat8Ga80zHme7iaic1IfY2tORnxGYC8JBsEeDB2CnlsiajVUy85H2wKrUgfEX7KFW7sdoicta8SVQ75dibWQVP4t4/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=34)](https://mp.weixin.qq.com/s?__biz=Mzg4MTU4NTc2Nw==&mid=2247497796&idx=1&sn=a1c92e6bb604e82a232aa8d3bab5ea4c&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicndic3XHt9u9FYSIsekXaQhOeicSXliav6mVVlDsbJMv2O4smTtDPNAfWDBL4e8rxSFvBLoV9uhUkCrw/0?wx_fmt=png)

七芒星实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicndic3XHt9u9FYSIsekXaQhOeicSXliav6mVVlDsbJMv2O4smTtDPNAfWDBL4e8rxSFvBLoV9uhUkCrw/0?wx_fmt=png)

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