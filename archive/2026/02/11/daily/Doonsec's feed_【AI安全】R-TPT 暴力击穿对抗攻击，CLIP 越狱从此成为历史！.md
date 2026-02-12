---
title: 【AI安全】R-TPT 暴力击穿对抗攻击，CLIP 越狱从此成为历史！
url: https://mp.weixin.qq.com/s/hoZutFpokckGSTz5ObRjgQ
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:18:15.593236
---

# 【AI安全】R-TPT 暴力击穿对抗攻击，CLIP 越狱从此成为历史！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Y05UtykogHRu9geR0E06uZjPZY1rxMY9UPLz9S8wvLle3t32ByrVfBFTMmfdoF9Xlib4GuJjjlLc0kx1GXrZVE71Jr6RvMgcKxoHhQvAB1JA/0?wx_fmt=jpeg)

# 【AI安全】R-TPT 暴力击穿对抗攻击，CLIP 越狱从此成为历史！

原创

Oxo Security
Oxo Security

Oxo Security

![]()

在小说阅读器中沉浸阅读

# 一、 你以为坚不可摧的 CLIP，其实在“像素炸弹”面前脆如薄纸？ 😱

##### AI 时代！人人都在深耕 AI 安全，你缺的就是这关键一步！🚀

`安全圈已经“卷”向 AI 了！错过这个关键点，可能正在被时代边缘化。`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c9uzmFRqtCIwuQZzWHXcLVTmoTfLpES3uxw9DESYkLhm5xOCiaXLNAr5BoudicDsXRdhGCd8T6Sib5VQ/640?wx_fmt=png&from=appmsg)

咱们现在天天用的多模态大模型（VLMs），比如大名鼎鼎的 **CLIP**，竟然藏着一个足以让所有开发者彻夜难眠的“致命后门”！这就是让 AI 圈闻风丧胆的—— **对抗攻击（Adversarial Attack）**！💥

想象一下，你有一张极其清晰的“金毛犬”照片，但在攻击者手里，只要往这张图里加入一些你肉眼根本不成出来的“微小噪音”（就像给照片加了一层隐形滤镜），CLIP 就会瞬间变“智障”，言之凿凿地告诉你这是一台“割草机”！这就是所谓的 **“像素炸弹”**，它能直接绕过模型的视觉逻辑，精准实施“降智打击”。 🤯

![](https://mmbiz.qpic.cn/mmbiz_png/Y05UtykogHQUy7VicMa4fUppzVgep4Ep3TEOVo1DKNHkGqxamIKibYYLbJ8ArdogNMFpZ4FJWohbiaIQ0yj2MzIibsc7Af7ialWNpP4pjD5ZQmYg/640?wx_fmt=png&from=appmsg)

更要命的是，现在的视觉大模型大多是开源的，大家都用那一两个经典的权重。攻击者只需要在家里偷偷练好“攻击脚本”，就能像拿到了万能钥匙一样，横扫所有基于 CLIP 开发的应用。这哪是模型啊，这简直就是给黑客留的“入户大门”！ 🚪🔓

过去，科学家们想出的办法是 **“对抗训练”**。简单来说，就是把这些有毒的图片喂给模型吃，让它产生免疫力。但这里有个巨坑：

1. 1. **太烧钱了！** 💸 训练一次 CLIP 级别的模型，那算力开销普通公司根本玩不起。
2. 2. **太笨重了！** 🐢 你得提前准备好带标签的数据。如果换个新任务，对不起，重练吧！
3. 3. **灵活性极差！** 只要模型部署了，它的防御力就固定了，面对新型攻击只能“坐以待毙”。

难道我们就只能看着大模型被这些“像素炸弹”炸得体无完肤吗？**并不是！** 来自中科大和中科院自动化所的大神们出手了！他们带来了一套名为 **R-TPT（Robust Test-Time Prompt Tuning）** 的神级操作，直接在“推理阶段”给模型穿上了防弹衣！不用重新训练，不用标注数据，就在你点下“识别”按钮的那一秒钟，防御就完成了！简直是 AI 界的“临阵磨枪，不快也光”！ 🛡️✨

---

# 二、 降维打击！拒绝“马后炮”，R-TPT 开启“推理即防御”的新纪元 🚀

传统的防御方法像是在造房子的时候就把钢筋加粗（对抗训练），而 **R-TPT** 就像是给房子配了一个“瞬时扫描仪”和“动态装甲”。无论攻击者怎么变幻套路，R-TPT 都能在模型开口说话之前，把那些阴招给化解掉。

这里我们要引入一个高级词汇：**测试时提示微调（Test-Time Prompt Tuning, TPT）**。大家坐稳了，我们要开始拆解 R-TPT 的核心逻辑了！ 🧠

![](https://mmbiz.qpic.cn/mmbiz_png/Y05UtykogHR2lGmcC4sf3SU5oEIKIHIhbJnodmd48WfBCZdA5uOyp0Hjf1FPAw6Ss4M1d579g9iaeb8iaoK7IBxaBGUBlOlGhocJ4zB4srBps/640?wx_fmt=png&from=appmsg)

### 1. 什么是 TPT？（原本的“老路子”）

传统的 TPT 想法很美好：既然一张图可能被干扰，那我就把这张图旋转、缩放、裁剪，搞出 N 个“分身”。然后让模型去读这些分身，只要大多数分身都说这是“狗”，那模型就觉得自己的信心增加了，从而优化一下它说话的“提示词”（Prompt）。

### 2. 为什么 TPT 在攻击面前会“反向白给”？ ❌

大神们在研究中发现了一个惊人的事实：传统的 TPT 在面对对抗攻击时，不仅不能防御，反而会\*\*“助纣为虐”\*\*！

* • **对抗样本的迷惑性：** 攻击者生成的噪音是非常精准的。即使你对图片做了旋转、裁剪，模型依然可能给出错误但“极度自信”的预测。
* • **逻辑冲突：** 传统的优化目标（边缘熵最小化）会强迫所有“分身”去向那个错误的“自信预测”靠拢。这就像是一个谎言被重复了一千遍，模型最后自己都信了，直接掉进坑里死活不出来。

### 3. R-TPT 的逆天改命方案 🛠️

R-TPT 的核心逻辑非常硬核且直白，它直接对底层的优化公式动了“大手术”！它提出了两个必杀技：

| 必杀技名称 | 核心逻辑 | 作用 |
| --- | --- | --- |
| **点熵最小化 (PEM)** | 丢弃导致冲突的 KL 散度项，只保留个体信心提升 | 防止模型被错误的“群体共识”带偏 |
| **可靠性加权集成 (RWE)** | 给每个“分身”打分，谁靠谱谁说话，坏分子闭嘴 | 自动识别并过滤掉那些被污染的干扰视图 |

这种设计巧妙地避开了对抗攻击最擅长的“群体误导”，让模型在极短的时间内找回理智。下面我们将进入最硬核的部分，看看 R-TPT 到底是怎么手撕对抗攻击的！ 👇

---

# 三、 逻辑重构！切除“恶性肿瘤”，点熵最小化让 AI 不再“随大流” 🔪🧠

🎯 **【AI 安全攻防 · 算法加固】**

**为什么原本用于增强一致性的 KL 散度，在对抗攻击下反而成了摧毁 AI 逻辑的“帮凶”？R-TPT 又是如何通过“暴力切除”数学项，让模型在推理性命悬一线时找回真理的？**

欲了解本章节关于点熵最小化（PEM）的底层数学逻辑、详细对比实验以及对抗环境下的策略演变，欢迎加入 **Oxo AI Security 知识星球** 获取完整深度解析。星球内部不仅涵盖此类顶会论文的实战化解读，更有丰富…

---

* • 📚 **AI 文献解读**：最前沿的 LLM 安全论文深度剖析。
* • 🐛 **AI 漏洞情报**：第一时间掌握主流大模型的 0-day 漏洞与越狱方式。
* • 🛡 **AI 安全体系**：从红队攻击到蓝队防御的全方位知识图谱。
* • 🛠 **AI 攻防工具**：红队专属的自动化测试与扫描工具箱。

🚀 立即加入 **Oxo AI Security 知识星球**，掌握AI安全攻防核心能力！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c86l9BKV2TcgrjKw8B41ge3ibibq5qqLoNW0aJYvEfAAibSfRgU74vleMaXJ2chff1d7sk5B7xHcI6iaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RBozUQPW9c86l9BKV2TcgrjKw8B41ge30c1ib8vQunnAo8BIkojRnd5y8VoLeTxpl6czmSXAI91OxicJEaAibrGgA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c98C8Gg5hFYTHHv2QrMvZ8foNQRgkoOLR2p0ulacK7KCmZxeoT0k1fQ99pTvK43Q3cMgPzabRkqiaQ/0?wx_fmt=png)

Oxo Security

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c98C8Gg5hFYTHHv2QrMvZ8foNQRgkoOLR2p0ulacK7KCmZxeoT0k1fQ99pTvK43Q3cMgPzabRkqiaQ/0?wx_fmt=png)

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