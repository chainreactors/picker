---
title: 黄仁勋GTC大会梳理
url: https://mp.weixin.qq.com/s/9D2HsoG3FUKtgTia5u1TaA
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:16:49.551731
---

# 黄仁勋GTC大会梳理

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/316EM2ouicpxJT662ibza1tjbEzx4abg5HIBs1kwvL6oF3mtuBEvibwU0dPFP7CVnT3077rGzjUnbX2oCiaTVicpdprhOEFaaOb4IYYF8k7iad5ic4/0?wx_fmt=jpeg)

# 黄仁勋GTC大会梳理

AI与代码安全

![]()

在小说阅读器中沉浸阅读

黄仁勋在最近的GTC大会上的演讲，核心可以概括为一句话：**AI 正在进入“工业化大生产时代”，而 NVIDIA 要做的是这场工业革命的“基础设施提供者”**。

![](https://mmbiz.qpic.cn/mmbiz_jpg/316EM2ouicpyYX1zt28GEiaRthic4RODjOVktPeDoq0h6s6eCJ5IAwYicYiaue085PycaDk1Z9r8Iia3ob492ztw0AgkzxeHiafGXky8RYAbMvHXA8/640?wx_fmt=jpeg&from=appmsg)

# **一、最核心主线：AI进入“工厂时代”**

黄仁勋提出一个非常关键的概念：

## **1.1****AI Factory（AI工厂）**

1）AI不再只是模型训练

2）而是像电厂一样持续“生产智能（tokens）”

3）输入：数据+ 算力

4）输出：token（文本/图像/决策）

本质变化：

1）从“训练一次 → 用很久”

2）变成“持续推理 → 持续产出价值”

他强调：未来企业的核心资产不是软件，而是“生成智能的能力”。

# **二、重磅硬件发布（算力全面升级）**

## **2.1****Blackwell架构（重头戏）**

这是本次最重要发布：

### **2.1.1****关键特点：**

专为**生成式AI & 推理优化**

比上一代Hopper架构性能大幅提升

重点提升：推理效率（LLM运行更便宜）、能耗比（降低AI成本）。

### **2.1.2****核心芯片：**

**B200 GPU**

**GB200（CPU+GPU超级芯片）**

意义：

1）AI成本下降 → 应用爆发

2）推理成为主战场（不是训练）

## **2.2****NVL72机架级系统（AI超级节点）**

一个机架=72块Blackwell GPU

专门为超大模型推理设计

特点：

1）可以运行万亿参数模型

2）低延迟高吞吐

本质：AI算力从“服务器”升级为“数据中心级机器”。

## **2.3****AI超级计算机生态**

推出多个“整机方案”：

1）DGX SuperPOD（企业级AI数据中心）

2）与云厂商深度整合

涉及公司：Amazon、Google、Microsoft

NVIDIA定位：不只是卖GPU，而是卖“AI基础设施”

# **三、软件战略：从CUDA到“AI操作系统”**

## **3.1****CUDA仍是护城河**

CUDA依然是核心：

1）开发者生态极强

2）绑定全球AI软件栈

## **3.2****推出一整套AI软件平台**

包括：

1）TensorRT（推理加速）

2）NIM（模型服务框架）

3）NeMo（大模型开发）

目标：把AI开发变成“标准化工业流程”

## **3.3****AI微服务（NIM）**

一个非常关键的新方向：

1）模型→ API化

2）企业可以像调用云服务一样调用AI

类似：AWS API、SaaS服务

意义：AI门槛大幅降低、企业无需训练模型也能用AI

# **四、AI应用爆发的几个方向**

## **4.1****数字人（Digital Human）**

更真实的虚拟人

实时语音+表情+理解

应用：客服、游戏NPC、虚拟主播

## **4.2****机器人（Physical AI）**

强调一个新概念：

### **4.2.1****Physical AI（物理AI）**

AI进入现实世界（机器人/自动驾驶）

涉及平台：

1）Isaac（机器人平台）

2）Omniverse（仿真平台）

本质：AI不仅理解世界，还能“行动”

## **4.3****自动驾驶**

继续推进：DRIVE平台、与车企合作深化

## **4.4****科学计算& 医疗**

AI用于：药物发现、分子模拟、气候预测

AI成为“科研工具”

# **五****、企业AI：下一波最大市场**

黄仁勋反复强调：“每家公司都会有自己的AI工厂”

企业将：部署私有AI模型、运行在本地或云上

### **5.1****企业AI特点：**

1）数据私有

2）定制模型

3）持续推理

类似：ERP → AI系统

# **六、生态战略：绑定全球科技巨头**

合作范围极广，如下：

### **6.1****云厂商：**

Amazon、Google、Microsoft

### **6.2****AI公司：**

OpenAI、Meta、xAI

NVIDIA角色：AI时代的“水电煤”

# **七、最重要的趋势判断**

## **7.1****AI从训练 → 推理时代**

过去：训练大模型

现在：让模型跑起来赚钱

## **7.2****Token成为新“单位”**

类似电力单位（kWh），AI公司卖的是token产出能力。

## **7.3****算力=生产力**

GPU ≈ 工厂机器；数据中心≈ 工厂。

## **7.4****AI成本正在快速下降**

Blackwell降低推理成本，推动应用爆发。

## **7.5****软件正在被“AI重写”**

未来软件：不再是固定逻辑，而是生成式系统。

# **八、总结**

黄仁勋这次GTC传递的核心信息是：

**AI已经从“科研项目”，变成“工业基础设施”，而NVIDIA要成为这个时代的电力公司。**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/gbFHCWYSgF4dWsMlOVnEDAzyugosHQFicRvViccFWcTR87YWA0ZVg0p2tXglgnXEQElwnIhhmpEwulCbzCbzKb1A/0?wx_fmt=png)

AI与代码安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/gbFHCWYSgF4dWsMlOVnEDAzyugosHQFicRvViccFWcTR87YWA0ZVg0p2tXglgnXEQElwnIhhmpEwulCbzCbzKb1A/0?wx_fmt=png)

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