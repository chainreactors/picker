---
title: BinaryAI更新布告｜漏洞存在性分析功能上线
url: https://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247511952&idx=1&sn=fb6c167d7e11e70f7c74b2dc72ab2a2f&chksm=fbfe9395cc891a838b2137f982fe26ffd6086b203b3b72f93f249399022f284a94e58a0cf9e2&scene=58&subscene=0#rd
source: 腾讯科恩实验室
date: 2024-10-31
fetch_date: 2025-10-06T18:55:01.286036
---

# BinaryAI更新布告｜漏洞存在性分析功能上线

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zZKnUibvoer8OsyHGcq2sYfjqjibibicfgeOmx39ibjic6hdBeRjic1iabMpZ04Bz7LOVhTibvQxmyeYWWGORj0lFTMFyLw/0?wx_fmt=jpeg)

# BinaryAI更新布告｜漏洞存在性分析功能上线

原创

腾讯科恩实验室

腾讯科恩实验室

**BinaryAI（https://www.binaryai.cn）**

腾讯安全科恩实验室二进制安全智能分析平台—BinaryAI，可精准高效识别二进制文件的第三方组件及其版本号，旨在推动SCA（软件成分分析）技术在**DevSecOps**、**威胁****情报**、**安全研究**等应用场景发展。

漏洞存在性分析功能上线

更

BinaryAI最新上线漏洞存在性分析功能，基于函数语义相似性匹配技术检测目标二进制文件是否包含修复已知漏洞的补丁代码，即判断文件是否已经对漏洞进行打补丁操作，旨在降低漏洞误报以及增强交互式验证分析能力。

BinaryAI目前仅支持用户体验示例文件的漏洞存在性分析效果。**如需功能试用或业务合作，请联系：binaryai@tencent.com。**

功能介绍

传统的软件成分分析工具分析输出第三方组件清单后，关联得到这些组件涉及的已知漏洞列表。然而，由于这些工具未能验证漏洞是否真实存在，导致大量误报的产生，意味着需要投入更多时间和人力确认这些漏洞存在与否。

为了缓解漏洞误报过高带来的人工验证漏洞存在性难度大、成本高的问题，BinaryAI提出了一种二进制文件漏洞存在性分析技术，将漏洞存在性分析问题转化为判断目标文件函数与漏洞修复补丁前后源码的语义相似性，利用BinaryAI在函数相似性检索的算法优势大大降低漏洞人工验证成本。

示例文件

以BinaryAI首页示例文件“libpng\_1.2.50-2+deb8u3”为例：

https://www.binaryai.cn/analysis/2c5572c1f6879c67f1392216ea51af707f58e5f28597d17bec207643248f1d67

分析结果页的“漏洞存在性分析”结果展示了文件可能存在的漏洞列表，表格中还展示了每个漏洞相应的CVSS分数以及风险等级，并根据该文件中的函数和漏洞、补丁源码函数相似性分析结果，给出漏洞存在性的判定结果。

![](https://mmbiz.qpic.cn/mmbiz_png/zZKnUibvoer8OsyHGcq2sYfjqjibibicfgeOcgria1UcgPqY7P3SMcWds1jf2vEibicU4APSa42PHCIdQiaPSkPQYx1eZA/640?wx_fmt=png&from=appmsg)

如图所示，BinaryAI识别到该文件中存在与部分漏洞源码高度相似的函数，同时也检测到部分函数与补丁源码相匹配。点击“查看相关函数”，可以进一步查看与漏洞相关的函数位置。

![](https://mmbiz.qpic.cn/mmbiz_png/zZKnUibvoer8OsyHGcq2sYfjqjibibicfgeOtaMrWMiaXcQ5iagib9qZj2mCzWPbqVGRNFk6tYJ4cK3k3DEeyP6n5JGsg/640?wx_fmt=png&from=appmsg)

点击函数地址，可以在交互式分析页面查看补丁前后的源码。可以看到文件中漏洞相关函数和补丁后的源码函数具有更高的语义相似性。

![](https://mmbiz.qpic.cn/mmbiz_png/zZKnUibvoer8OsyHGcq2sYfjqjibibicfgeOYoKVCVeXpuuOXdMXibkCrRFnuzTicOLKWKJtiavEh0MOPnAJtDlpadYoA/640?wx_fmt=png&from=appmsg)

还可以通过点击筛选图标，在交互式分析页面直接筛选特定漏洞/补丁源码匹配结果的函数。

![](https://mmbiz.qpic.cn/mmbiz_png/zZKnUibvoer8OsyHGcq2sYfjqjibibicfgeOF2YV38FiaajqYicNViafXj4aic4fRjXQZXDhsu58Jl0mmXn5fOITSxYUjQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zZKnUibvoer8OsyHGcq2sYfjqjibibicfgeOjhgR0kIFENmJ25JibOYial4tyJDdlaTpLycqXqSZ9E0Xzib5NROceic49g/640?wx_fmt=png&from=appmsg)

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