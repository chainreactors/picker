---
title: 切掉大模型的拒答神经
url: https://mp.weixin.qq.com/s/IbQl28QkCHqjVByG4fM8PQ
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:45:23.612499
---

# 切掉大模型的拒答神经

# 切掉大模型的拒答神经

原创

Violet Walker
Violet Walker

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NtpTYP3oRVby1aktCdgM7Hlo2CvW6f9SPYl8k9mfVJ3UEFHeWagdyzYkicibSv2ic0Q3XtNSrIgDjEgiaZcKOSTGlrz4DKxKCPnaA/640?from=appmsg)
> **导语**：不用微调，不用租集群，一张家用显卡几十分钟，直接把开源大模型里那道拒答机制从权重层面抹掉。这个叫 Heretic 的开源项目已经在 GitHub 上攒了 4.1 万星，Hugging Face 上挂着 8000 多个它改造过的模型。技术不复杂，含义不轻。

![Heretic 一条 pip 命令切掉大模型拒答神经](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6ONvxibgc23O4qMvuKZaJGG7AiauqwKe04bonCDLr3Diah0aibr9vPwDQLjQ6K6Huwdz0gtx2jkf7xY1vwjRPHaN5tnlUC7sXwXbzI/640?from=appmsg "Heretic 一条 pip 命令切掉大模型拒答神经")

![Heretic 官方中文 README](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6OOByYm1eDHPjzvVPKKZkJoKwMAEYepX4Z0sQJz7VCtsiaCWuCibIptMLQyYUfB8Hv0gaJok3Fkqlq83OJ0qnClJGgAMVswaFpak/640?from=appmsg "Heretic 官方中文 README")

*（图：Heretic 官方中文 README 首页，来源 GitHub）*

## 它改的到底是什么：数学手术，不是重训

作者是 Philipp Emanuel Weidmann，2025 年 9 月建仓，AGPL-3.0 协议，Python 实现。

工具的核心思路很直接：拿一组"正常问题"和一组"有害问题"跑一遍模型，对比两组输入在模型内部激活上的差异，差出来的那个方向就是所谓的**拒答方向**；再把模型残差流里沿着这个方向的分量投影掉，拒答行为就没了。整个过程不更新任何训练参数，只动权重。

它内置两种改法：

* **ARA（Arbitrary-Rank Ablation）**，默认算法，专门为 Heretic 开发的，在多层网络上按秩做消融，参数细节作者放在 PR #211 里，技术 preprint 官方说即将公开
* **方向性消融（directional ablation，俗称 abliteration）**，经典做法，源头是 Arditi et al. 2024 的那篇论文（arXiv:2406.11717）。Heretic 的实现用了跨层的柔性消融权重核，同时支持投影消融和保范数的 MPOA 变体

判断改得好不好，靠的是打分器插件。默认两个：一个统计拒答率（keyword\_rate.py），一个算 KL 散度（kl\_divergence.py）——前者往死里压，后者负责把模型原本的能力按在地上，防止切完变傻。多个打分器可以同时启用、同时优化。想自己定义行为，继承 `Scorer` 基类实现 `get_score` 就行，不用改 Heretic 本体代码。

搜参数的是 Optuna 的 TPE 优化器。搜索空间里是这些：起止消融层、保留正常行为的权重、引导异常行为的权重、过度修正的相对权重、邻近层数量。

## 跑一遍要什么

环境要求 Python 3.10+ 和 PyTorch 2.6+（按显卡选对应版本）。安装和执行就两条命令：

```
pip install -U heretic-llm
heretic Qwen/Qwen3-4B-Instruct-2507
```

换成任何模型名或本地权重路径都行。默认动作就是去拒答，其他行为靠配置文件切换：config.default.toml（拒答抑制）、config.noslop.toml（禁低俗内容）、config.nohumor.toml、config.nosyco.toml（减少阿谀奉承）、config.emotions.toml、config.terse.toml。默认从工作目录读 config.toml，也可以用环境变量 `HERETIC_CONFIG_FILE` 指定。注意 1.x 的配置和 2.x 不兼容，官方给了迁移指南。

跑完有四个选项：保存模型、上传到 Hugging Face、直接对话测试效果、跑标准 benchmark。

硬件门槛比想象的低。官方给的数是：RTX 3090 配默认配置，处理 Qwen3-4B-Instruct-2507 大约 30 到 40 分钟。还支持 bitsandbytes 的 4-bit 在线量化，显存不够时可以再压一压。稠密模型、多模态模型、多种 MoE 架构、较新的混合架构都在支持范围内。

## 官方演示里的真实数字

官方演示是录屏跑的，终端输出能看到全过程：加载 400 条有害提示（来自 mlabonne/harmful\_behaviors），分别为 good prompts 和 bad prompts 采集模块的 I/O，然后进入 100 组候选参数的搜索。

![Heretic 运行终端输出](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MPbcYurpa4oDxpJHIdiaYvCHUdZax9yMHyXg138ezFGYshweJU5X6PW0hMmIKsAB6krtsM3EeRzfat2PFuf0ibS7Il5iaRbfE0iaY/640?from=appmsg "Heretic 运行终端输出")

*（图：Heretic 实际运行输出，参数与评估指标可见，来源官方演示录屏）*

第一组 trial 的参数就挺说明问题：消融层从 1 到 20，保留正常行为的权重 0.6060，引导异常行为的权重 0.0006，过度修正相对权重 0.5979，邻近层数量 4。这组评估结果是拒答 81/100，KL 散度 0.1493。

这就是起点，不是终点——后面的 99 组 trial 由 Optuna 接着搜，直到拒答率被压下去、KL 散度被按在地板上。单组 trial 耗时 1 分 02 秒，全程剩余时间估算 1 小时 43 分；显存上，分配了 8.58 GB GPU 显存、预留 8.60 GB，系统常驻内存 3.67 GB。

## 规模：4.1 万星和 8000 多个改造版模型

* GitHub：41,519 star、4,960 fork、66 个未关闭 issue，2026 年 11 月 16 日仍有提交
* 拿过 trendshift 的 "#1 Repository of the Day"
* Hugging Face 上带 `other=heretic` 标签的模型超过 8000 个，README 和官网都挂了这个统计
* 社区前作也有一串：AutoAbliteration、FailSpy/abliterator、wassname/abliterator、ErisForge 等，但作者强调 Heretic 是从零写的，没复用这些项目的代码

## 下载地址

* 源码仓库：https://github.com/p-e-w/heretic
* 官网与文档：https://heretic-project.org
* PyPI 安装：`pip install -U heretic-llm`（包名 heretic-llm）
* Codeberg 镜像：https://codeberg.org/p-e-w/heretic
* Hugging Face 组织：https://huggingface.co/heretic-org
* 复现库 Grimoire：https://huggingface.co/spaces/heretic-org/Heretic-Grimoire
* 模型与下载统计：https://heretic.sdad.pro/
* 基础论文（Arditi et al. 2024）：https://arxiv.org/abs/2406.11717

## 值得警惕的那一面

对做模型的人，这是坏消息：**对齐不是发布即生效的**。任何拿到开源权重的人，都能在自己的机器上把拒答抹掉，全程不需要入侵任何系统、不需要偷 API Key。8000 多个改造版模型说明这已经是流水线级别的操作，不是几个人的实验。

对企业采购和自部署也一样：可自部署的开源模型，"已对齐"这个属性是跟着权重走的，谁部署谁负责。第三方改造版模型在 Hugging Face 上没有统一签名和校验，谁把它拉进生产环境、谁承担这个风险。

风险的方向也因此变了——原本模型"不答"，现在它"什么都答"。护栏没了，剩下的是内容安全策略、审计和出口管控这些软手段。

站在防守的角度，合理的做法不是禁用这个工具（它本身是公开的开源研究），而是把自部署模型的权重来源纳入管理：只用官方或内部可追溯的构建版本，第三方改造权重默认不进生产。

## 参考来源

* Heretic 官方仓库与 README（https://github.com/p-e-w/heretic）
* Heretic 官网（https://heretic-project.org）
* Arditi et al. 2024：Refusal Aversion in LLMs（https://arxiv.org/abs/2406.11717）

**版权声明**：本文由华盟网原创发布，保留所有权利。文中图片来源于 Heretic 官方仓库与演示录屏。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MbZxeB4pceWDuEfH4Yu7b5JbR3iabcibG3rhd30klvFwpVHuDcrSxDicwGlFm8qZiciaG1ibfXuKv8ib0lbYqA5udbW8PNvfp2TMjm8M/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PqIlEXpqX8M61E7OnvKaRPA5kmXibhU7wAmSKrhAI78p9micSNeiag87gKPmkXdAEEjZDF8MIzgo0Qq1a9xbxv2FB9EwIk4ibaV1k/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MicUgaZ8h2SexSMKiaVDoDbrLuTzrUEsARoBibnmRia3LClmPhL7fY1kLU1c7icFRib6aWjQeDwZg9sNEvoUcd3eyiafLxrd3BucYX0E/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6Mgv0aC7RrJFVGTGDGey0w2tbtRLLWaxMq4Nk7EStgjkApMQ2mLVPKfRNhfIT47dxug5cPWhEXup4icZ32u3E1dsc6o3yhObk1g/640?from=appmsg)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过