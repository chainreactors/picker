---
title: 12GB 显卡也能跑Qwen3.8-Flash-Next(125B)? 消费级硬件迎来本地AI革命！
url: https://mp.weixin.qq.com/s/g-LDGO06WIW4MBbqJ4xkvw
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:21:53.897838
---

# 12GB 显卡也能跑Qwen3.8-Flash-Next(125B)? 消费级硬件迎来本地AI革命！

# 12GB 显卡也能跑Qwen3.8-Flash-Next(125B)? 消费级硬件迎来本地AI革命！

原创

骨哥说事
骨哥说事

骨哥说事

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

#

#

# **防走失：****https://gugesay.com/**

**不想错过任何消息？设置星标****↓ ↓ ↓**

#

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg)

*还记得前段时间，要运行一个千亿级AI模型需要租用昂贵的云端服务器吗？现在，这个门槛正在被一个开源项目彻底打破。*

## 一、消费级硬件的AI大模型时代来临

最近在GitHub上发布的**Strata项目（目前已高达11.3k Star）**，让普通玩家的游戏PC变成了强大的AI工作站。这个开源项目让用户能够在NVIDIA或AMD显卡（12GB VRAM以上）+ 32GB以上RAM的配置下，本地运行Qwen3.8-Flash-Next这个庞大的1250亿参数MoE模型。

**什么是MoE模型？** MoE（Mixture of Experts，混合专家模型）是一种高效的模型架构，它通过"分而治之"的思想，每次推理只激活部分"专家"网络。Qwen3.8-Flash-Next采用了超稀疏MoE架构，具有24,576个专家，但每个token只激活约6B参数。这种设计让巨大的模型能够在有限的硬件资源下运行。

## 二、超越想象的本地推理速度

让我们看看官方给出的实际测试效果：

* **RTX 5070 (12GB)** + Ryzen 5 7600 + 64GB RAM配置下，

+ Q2\_0量化版本：**94 tokens/s的生成速度**
+ 读取32K token长文档：**2,650 tokens/s**

* 即使是上一代的RTX 3090 (24GB)，预计也能达到**100-140 tokens/s**的生成速度

对于大多数应用来说，这基本可以满足实时交互的需求。

## 三、Strata的智能内存管理策略

Strata项目的核心创新在于其**智能的内存和计算资源分配策略**。简单来说，它巧妙地将模型的不同部分分配到PC的不同硬件资源中：

1. **显卡承担重任**：保留最常用的几千个"专家"模块（约12GB）
2. **RAM作为缓冲区**：存储所有24,576个专家（约40-55GB）
3. **CPU辅助计算**：处理RAM中的专家计算
4. **SSD作为后备**：存储巨大的查找表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZjlPs9JSkpWiaTpEUJiaSiaaSevPM5LECkMwR73u5khjp045B1gruFjYngS9MRG997P5ZHB2fmwLLGFVOk28IM6hr0Zs5jiaZlhq58/640?wx_fmt=png&from=appmsg)

这种"分层计算"的概念好比一个智能厨房：

* 常用的调料放在灶台上（显存）
* 偶尔用的食材放在冰箱里（内存）
* 大包装的原料放在储藏室（SSD）

## 四、三步开启本地AI之旅

**系统要求**：

* 显卡：NVIDIA RTX 20/30/40/50系列或AMD RX 7900/7800等12GB以上VRAM
* 内存：32GB以上（64GB体验最佳）
* 硬盘：至少80GB可用空间
* 系统：Windows 10/11或Linux

**安装步骤**：

1. 下载Strata项目或直接运行`START-HERE.bat`（Windows）/ `./setup.sh`（Linux）
2. 选择适合内存的模型版本（推荐根据RAM大小选择）
3. 等待自动下载并启动，打开浏览器访问 `http://127.0.0.1:8080`

**模型选择建议**：

* 32GB RAM → **Coder版**（专门优化的代码模型）
* 48GB RAM → **IQ2\_XS**（性价比最高的平衡版）
* 64GB RAM → **IQ2\_XS**或**IQ3\_S**（追求最高性能）
* 96GB+ → **IQ3\_S**或**UD-IQ4\_XS**（极限性能版）

## 总结

Strata项目的出现不仅仅是又一个GitHub repo，它代表着AI技术走向普及的重要一步。12GB显卡运行125B参数的MoE模型，这曾经只存在于研究论文中的设想，现在已经变成了触手可及的现实。

对于IT和科技爱好者来说，现在是尝试本地AI部署的最佳时机。无论你是想打造一个私密的AI编程助手，还是想深入研究大模型推理技术，抑或是单纯享受将服务器级别的AI能力带到桌面的乐趣，Strata都为你提供了一个绝佳的入口。

技术的边界正在不断被打破，而这一次，打破边界的工具掌握在了每一个拥有消费级硬件的用户手中。AI民主化不再是空洞的口号，而是正在发生的现实。

项目地址：https://github.com/Niko1221/Strata

- END -

**感谢阅读，如果觉得还不错的话，动动手指给个三连吧～**

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZj0vZ4HI9JCibQwzj9ZHia88e3thicG9MD8BG7hfmbSq8EeqG0WROTia6wbHU9BYw0kZjo37eohmhibDUgJKMPXXgRe4COyEQoYjwWA/0?wx_fmt=png)

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