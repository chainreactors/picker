---
title: 亚马逊云服务（AWS）如何生产威胁情报（一）
url: https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486155&idx=1&sn=60fe469355ff2f4d8d5026fdaeb99b30&chksm=fb04c9a3cc7340b54754d887fa53cbddc2427a1ea8d871b144469c1e0d5566f60cd139a9d553&scene=58&subscene=0#rd
source: 天御攻防实验室
date: 2024-12-10
fetch_date: 2025-10-06T19:39:56.770715
---

# 亚马逊云服务（AWS）如何生产威胁情报（一）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hPq2VZ0zUBB8kuZSrbZJicNjyibbicMGMoLfL74XLzjucicokcZKkDQflQ5AzXB9hzks1E1iajvx2rRde9xZjsDlJVg/0?wx_fmt=jpeg)

# 亚马逊云服务（AWS）如何生产威胁情报（一）

原创

天御

天御攻防实验室

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hPq2VZ0zUBAwZQYIRcMGdob0eTGKx525Ddp9DrwAwWLOGwL1HNIwiayA2mzhHsdiakoCUfBmN7fib078lq2yjXTMg/640?wx_fmt=png)

## **引言**

在当今复杂的网络安全环境中，威胁情报的生产和应用变得越来越重要。作为全球最大的云服务提供商之一，亚马逊云服务（AWS）利用其独特的规模优势，构建了一套完整的威胁情报生产体系。本文将深入探讨AWS如何通过创新的技术手段和系统化的方法来生产和应用威胁情报。

## **威胁情报的规模与影响**

AWS的基础设施规模为其提供了独特的全球威胁可见性。数据显示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hPq2VZ0zUBB8kuZSrbZJicNjyibbicMGMoLDM3MicTco6xYh6icOqCEBkS1nBtwIIC9gqUpxNq7L3jSibqrvibvZQHjRw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hPq2VZ0zUBB8kuZSrbZJicNjyibbicMGMoLcnkWvibMM68pNQUySoJkGbMlxicBBlf2S4OIibqojrGuwqVCQmeuCB91g/640?wx_fmt=png&from=appmsg)

* 每天观察超过7亿次威胁互动
* 约4.5亿次可被归类为恶意行为
* 在过去12个月中：

+ 成功检测并限制约270亿次对S3存储桶的未授权访问尝试
+ 阻止了约2.7万亿次针对EC2上易受攻击服务的访问
+ 发出约8万次takedown请求以瓦解恶意行为者的基础设施

## **三大核心威胁情报系统**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hPq2VZ0zUBB8kuZSrbZJicNjyibbicMGMoLgUfjFVmF2YkviarIOl70orZ0SmTngAib5QAZ4oWDpING0dQ87M3LtzEA/640?wx_fmt=jpeg)

##

### **1. MatPot蜜罐系统**

MatPot是AWS的全球分布式蜜罐网络，是其威胁情报生产的核心系统之一。

## 技术特点

* 动态适应性：持续演化和改变策略
* 广泛覆盖：模拟数百种不同服务和协议
* 快速响应：平均90秒内可检测到探测，3分钟内发现主动利用
* 深度集成：与AWS Shield、WAF和GuardDuty等安全服务紧密结合

## 设计原则

1. 开发敏捷性

* 安全工程师和软件工程师协同开发
* 支持快速迭代和更新

2. 实验导向

* 内置实验能力
* 优化与威胁行为者的互动

3. 真实性和隐蔽性

* 难以被识别为蜜罐
* 平衡暴露度和真实性

4. 高质量数据采集

* 完善的互动分类系统
* 可信的威胁判定机制

5. 威胁工件处理

* 自动化的工件提取
* 安全的存储机制

### **2. Sonaris系统**

Sonaris专注于检测和限制滥用扫描和利用尝试。

## 核心能力

* 与MatPot深度集成
* 高准确度的威胁识别
* 精确的干预机制
* 自动化的规则生成

## 应用场景

* 为AWS WAF提供托管规则
* 为Route 53 Resolver DNS防火墙提供规则
* 快速响应新型漏洞威胁

### **3. Mithra系统**

Mithra是AWS基于神经网络的图模型系统，专门用于识别恶意域名。

## 技术规模

* 38亿个节点
* 480亿条边

## 关键优势

* 高精确度的恶意域名识别
* 领先外部威胁情报源数天到数月的预警能力
* 持续的自我学习和进化能力

## **威胁情报的生产方法**

### 主动收集方法

AWS采用以下欺骗技术进行威胁情报收集：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hPq2VZ0zUBB8kuZSrbZJicNjyibbicMGMoLoSmhcbOU3mK2hht4ibbaSDCJHsD8CubZR0r0XOUHx1pHZDrxyAKWeMA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hPq2VZ0zUBB8kuZSrbZJicNjyibbicMGMoLTkiaiaILATYw4sibhzVjWWpShrTvRSUtJjn8eAxNaRiacDvmzy6SUxTrRw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hPq2VZ0zUBB8kuZSrbZJicNjyibbicMGMoLicHtEFiaGdI3vEBv4nfvicKuywuG0TtjoMvbdJaibeG36Tj1Hs61hs5BfA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hPq2VZ0zUBB8kuZSrbZJicNjyibbicMGMoLnGwl7RAIvfDXUa6zyfRia9r6jyMYuG8n2YZwE35ibDJksVmllwy0pnfg/640?wx_fmt=png&from=appmsg)

1. 诱饵和陷阱

* 策略性暴露的信息和工件
* 针对性的服务模拟
* 精心设计的系统漏洞

2. 蜜标（Honey Tokens）

* 虚假但可信的数字实体
* 多样化的诱饵类型
* 预警触发机制

3. 蜜罐（Honeypots）

* 低交互蜜罐：用于大规模探测检测
* 高交互蜜罐：完整服务模拟

### **威胁情报处理流程**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hPq2VZ0zUBBx2ESUwvicgTOfTm1Otk2tv0jvPWFeaWeawQUfRuIichBCuk3sxT9YcXGtx6ib9jdenUHMIKuMYSDRg/0?wx_fmt=png)

天御攻防实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hPq2VZ0zUBBx2ESUwvicgTOfTm1Otk2tv0jvPWFeaWeawQUfRuIichBCuk3sxT9YcXGtx6ib9jdenUHMIKuMYSDRg/0?wx_fmt=png)

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