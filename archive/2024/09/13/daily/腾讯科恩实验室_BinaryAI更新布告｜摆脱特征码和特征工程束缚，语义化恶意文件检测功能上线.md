---
title: BinaryAI更新布告｜摆脱特征码和特征工程束缚，语义化恶意文件检测功能上线
url: https://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247511896&idx=1&sn=17f4962ddd9b42727e3a499ea79b39f6&chksm=fbfe935dcc891a4b121131b3bf5a237932dff91f79544de3d6d4747f0ddb62b34cd989f0b37d&scene=58&subscene=0#rd
source: 腾讯科恩实验室
date: 2024-09-13
fetch_date: 2025-10-06T18:28:00.048235
---

# BinaryAI更新布告｜摆脱特征码和特征工程束缚，语义化恶意文件检测功能上线

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zZKnUibvoericJztibUiaQp09DIynWQl3kAgThImHg3QnYJkAWUknkg0fJpS3dfB8icF32nf0UnURp1YPia5eWCEX7fQ/0?wx_fmt=jpeg)

# BinaryAI更新布告｜摆脱特征码和特征工程束缚，语义化恶意文件检测功能上线

原创

腾讯科恩实验室

腾讯科恩实验室

**BinaryAI（https://www.binaryai.cn）**

腾讯安全科恩实验室二进制安全智能分析平台—BinaryAI，可精准高效识别二进制文件的第三方组件及其版本号，旨在推动SCA（软件成分分析）技术在**DevSecOps**、**威胁****情报**、**安全研究**等应用场景发展。

恶意文件检测功能上线

更

本次发布，BinaryAI上线了恶意文件检测功能Beta版，支持对可执行文件进行函数级语义识别汇总，展示判定结果（恶意、安全）和恶意概率。

![](https://mmbiz.qpic.cn/mmbiz_png/zZKnUibvoericJztibUiaQp09DIynWQl3kAgQA8cn5dq7FBAphqODudw1zhpJBE3xRUOr5gJkvGqZUgicKmN2BXe6zg/640?wx_fmt=png&from=appmsg)

BinaryAI此前已上线[“基于KHash的恶意软件家族基因分析”](http://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247511774&idx=1&sn=a25dd6e19d6036651b71272ea7768fea&chksm=fbfe92dbcc891bcd178534e45a7cd5e5757be05dee31572b0a17663f8735099f4b0940057cd8&scene=21#wechat_redirect)功能，可通过计算用户上传的二进制文件与已知恶意软件之间的相似度，识别目标文件所属的恶意软件家族及其变体。

功能优势

传统反病毒引擎以规则引擎为主，基于特征码技术实现对已知恶意文件的查杀。这种方法在时间性能和准确率方面表现出色，但其时效性大打折扣，尤其是在面对不断演变的恶意软件时，问题尤为突出。尽管目前基于机器学习技术的反病毒引擎已逐渐投入应用，但由于这些机器学习模型的输入依赖于特征工程（例如EMBER：https: //github.com/elastic/ember），在攻防对抗中，往往被恶意文件开发者轻松绕过，导致基于机器学习技术的反病毒引擎起不到应有的效果。同时，缺乏语义化信息也使得这类引擎的可解释性较差。

作为传统反病毒引擎的能力补充，BinaryAI的恶意文件检测引擎创新性地探索了一套基于语义化的查杀引擎技术，通过大模型相关技术实现端到端文件检测。**这一技术的核心优势在于其无需依赖任何特征码或特征工程，已在威胁情报海量文件数据上进行了全面的训练，确保其具备准确性。**BinaryAI的恶意文件检测引擎可以灵活应对新型恶意软件的威胁，将会大幅提升恶意软件检测的时效性和可解释性。

目前威胁情报业务中已打通文件检测流程，旨在通过BinaryAI恶意文件检测引擎发现其他引擎未检出的恶意文件，相关实践成果会陆续对外发布。

本期其他更新

BinaryAI此次发布还通过量化加速技术，在准确率等指标不变的情况下，向量检索速度提升为原先的4倍，同时存储成本下降为原来的1/8。

更多业务体验

BinaryAI的算法引擎核心能力已同步落地应用于腾讯安全多款产品，包括：

* **腾讯威胁情报TIX与攻击面管理ASM**（https://tix.qq.com）
* **腾讯云二进制软件成分分析BSCA**（https://cloud.tencent.com/product/bsca）
* **腾讯主机安全云镜**（[腾讯主机安全（云镜）兵器库：斩杀挖矿木马的利剑-BinaryAI引擎](https://mp.weixin.qq.com/s?__biz=MzI5ODk3OTM1Ng==&mid=2247499680&idx=1&sn=a5771e0990df8ea6259ff4b6d22df5de&scene=21#wechat_redirect)）

此外，科恩实验室始终以积极的姿态探索软件安全领域和前沿AI结合的科研落地，推动成果转化以解决产业痛点问题。

![](https://mmbiz.qpic.cn/mmbiz_png/zZKnUibvoer9vEmy17rhTRezEHgviap0gbKnYg7ZHCLQbK1Nzo8U9noB32RhuN4q7CLyskL3icZBibIicaib74AS2icrQ/640?wx_fmt=png)

欢迎访问 **https://www.binaryai.cn**或 **阅读原文**前往体验！

**★**

**往期相关**

**★**

[•](http://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247496102&idx=1&sn=7835a7682a921a324d1a1e65a23a9c2d&chksm=fbfecda3cc8944b5a620e57ab9b32272f629bd31c3ecdf56ecbdc66e52ae39eb537dd49182c1&scene=21#wechat_redirect)[携手共研｜BinaryAI合作计划启动，面向广大学者开放底座能力](http://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247507888&idx=1&sn=68f73819d0ea05164d6c3ede197ed40b&chksm=fbfee3b5cc896aa357fa5cf4b8894f29797544d7ad9746fd4015ae6e358d179aa15ac2375fa5&scene=21#wechat_redirect)

[•](http://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247496102&idx=1&sn=7835a7682a921a324d1a1e65a23a9c2d&chksm=fbfecda3cc8944b5a620e57ab9b32272f629bd31c3ecdf56ecbdc66e52ae39eb537dd49182c1&scene=21#wechat_redirect)[BinaryAI更新布告｜二进制函数匹配模型BAI-3.0上线](http://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247507971&idx=1&sn=f7f7f4e07b6f2edd1b96cdd612228b02&chksm=fbfe9c06cc89151020abe41745e5571068352ef4a15c8596f314bf2e9cc84a1eba4060216182&scene=21#wechat_redirect)

[•](http://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247496102&idx=1&sn=7835a7682a921a324d1a1e65a23a9c2d&chksm=fbfecda3cc8944b5a620e57ab9b32272f629bd31c3ecdf56ecbdc66e52ae39eb537dd49182c1&scene=21#wechat_redirect) [科恩自研二进制相似性哈希算法“KHash”上线BinaryAI，助力更全面的文件安全分析场景](http://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247511576&idx=1&sn=89804c914e39b525355957dc73b9f460&chksm=fbfe921dcc891b0b1af24d25f3894408899225c37f41d31a29c8ef9b3bfea4c2d5ca6446437c&scene=21#wechat_redirect)

[•](http://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247496102&idx=1&sn=7835a7682a921a324d1a1e65a23a9c2d&chksm=fbfecda3cc8944b5a620e57ab9b32272f629bd31c3ecdf56ecbdc66e52ae39eb537dd49182c1&scene=21#wechat_redirect) [科恩BinaryAI@ICSE2024论文解读｜基于大模型的二进制软件成分分析](http://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247511406&idx=1&sn=95c3abbd7c897be62c1593b8b5b7d33b&chksm=fbfe916bcc89187dfb618e217aee4b12621e747cada871df9945dd520e03cd88785fe49097a5&scene=21#wechat_redirect)

[•](http://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247496102&idx=1&sn=7835a7682a921a324d1a1e65a23a9c2d&chksm=fbfecda3cc8944b5a620e57ab9b32272f629bd31c3ecdf56ecbdc66e52ae39eb537dd49182c1&scene=21#wechat_redirect) [BinaryAI更新布告｜恶意软件家族基因分析功能上线](http://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247511774&idx=1&sn=a25dd6e19d6036651b71272ea7768fea&chksm=fbfe92dbcc891bcd178534e45a7cd5e5757be05dee31572b0a17663f8735099f4b0940057cd8&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/zZKnUibvoericeibR9Via8lKsXBGe86PNOO29563lc14hN34D4ibbIeAjn8H388NjENBlYQibdA9GCW708MbsgxwqnWA/0?wx_fmt=png)

腾讯科恩实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/zZKnUibvoericeibR9Via8lKsXBGe86PNOO29563lc14hN34D4ibbIeAjn8H388NjENBlYQibdA9GCW708MbsgxwqnWA/0?wx_fmt=png)

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