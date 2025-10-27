---
title: 中国科学院信工所 | Snowflake代理请求的隐蔽性分析
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491417&idx=1&sn=948790356cdbfb890e36824bd672ac2d&chksm=fe2ee0d2c95969c44d6ad51182b3d405b6604dd6152396d64656389ad1e770e5707123f01e61&scene=58&subscene=0#rd
source: 安全学术圈
date: 2024-12-07
fetch_date: 2025-10-06T19:39:55.869446
---

# 中国科学院信工所 | Snowflake代理请求的隐蔽性分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WE6PLW6MbW2d7eicTeJ6Q8klKNiaDWrY2a1jjJ8MhxZFMe5XC38y5ygnt3R53wibV8J8Jb1gHsQhStMw/0?wx_fmt=jpeg)

# 中国科学院信工所 | Snowflake代理请求的隐蔽性分析

原创

宋坤书

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WE6PLW6MbW2d7eicTeJ6Q8klKVW5rYoJEBEnxclB0lTeqQE9BaqWMmA1wIeV5kKgLUdVPjFus5sRuw/640?wx_fmt=png&from=appmsg)
> *原文标题：Covertness Analysis of Snowflake Proxy Request*
> *原文作者：Yibo Xie, Gaopeng Gou, Gang Xiong, Zhen Li, Mingxin Cui*
> *原文链接：https://ieeexplore.ieee.org/document/10152736*
> *发表会议：Computer Supported Cooperative Work in Design(CSCW-D)*
> *笔记作者：宋坤书@安全学术圈*
> *主编：黄诚@安全学术圈*

### 1、研究背景

在网络封锁中，IP黑名单是一种简单且有效的技术，利用了互联网中许多网站和应用程序使用固定IP地址的特性。例如，一些国家通过将Tor网络中三跳路径的IP地址列入黑名单，成功阻止了对Tor匿名通信网络的访问。

为了规避IP黑名单的限制，Snowflake代理系统应运而生。Snowflake代理通过动态IP地址和志愿者参与的短期代理服务（包括浏览器扩展、网页代理和独立桌面代理），生成大量短期的代理IP，使得完全封禁变得几乎不可能。目前，研究主要从代理本身入手，例如利用WebRTC协议中的证书模式或流量特征检测Snowflake代理。然而，这些方法易受代理位置和版本变化的影响，效果有限。

针对这一问题，本文提出了一种新方法，重点检测Snowflake代理的代理请求而非代理本身。由于Snowflake代理需要频繁从代理数据库获取最新的代理IP，其请求模式具有独特性。通过对代理请求的分析，发现其在数据包大小、方向、时间及网络速度等方面表现出与普通网络请求的差异。基于这些特征，本文采用机器学习模型对Snowflake代理请求进行精准检测。在跨版本实验中，该方法表现出高效性，并且对正常流量的误报率较低。这是首个通过检测代理请求来阻断Snowflake代理的研究。

### 2、检测方法

#### 2.1 本文提出的方法

现有的雪花代理阻断方法主要集中在直接阻止代理本身，但由于代理的IP地址短暂且流量模式不稳定，这些方法已经被成功规避。本文提出了一种不同的思路，即通过检测和阻断雪花代理的请求来阻止其使用。

雪花代理使用的是一个名为Broker的数据库来维护可用的代理信息。用户在使用雪花代理之前，必须先从Broker请求代理。通过观察，代理请求和代理使用之间存在强依赖关系。由于雪花代理的IP地址是短暂的，用户需要频繁地从Broker请求最新的代理，以应对IP的快速变化。

如果阻断代理请求，用户将无法在每次启动雪花软件时获取可用代理，也无法在使用过程中及时刷新代理。基于这一观察，本文提出通过检测代理请求而非代理本身来彻底阻断雪花代理的方法。该方法在Snowflake阻塞中的原理如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WE6PLW6MbW2d7eicTeJ6Q8klicCRHcnBaK040mXnk3USHicxNQZNBkOESACyh1rYGnVaiaT4Cep1MibCwA/640?wx_fmt=png&from=appmsg)

#### 2.2 可行性分析

Snowflake代理请求通过模仿CDN上的普通web请求，实现了一定程度的隐蔽性，但其伪装在以下几个方面存在明显漏洞：

1. 数据包大小：Snowflake代理请求相较于普通的web请求，需要额外传递会话描述和用户信息（如代理版本），导致数据包大小分布复杂，包含更多短数据包和非典型包。这使其在数据包大小特征上显著区别于普通web请求。
2. 数据包方向：普通web请求遵循“请求-响应”的通信模式，服务端生成的数据包通常多于客户端。然而，Snowflake代理请求由于上传会话描述和用户信息，导致客户端发送的数据包数量显著多于普通web请求。本文统计了Snowflake代理请求和Chrome网络请求中前40个包的包大小分布及方向，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WE6PLW6MbW2d7eicTeJ6Q8klNNOGHKJXENQaicy0MA5JLpjmnma63d6GuULfWL6UYc1iaSQNqyrIBTAA/640?wx_fmt=png&from=appmsg)

3. 数据包时间：普通web请求通常直接连接目标服务器，且通过托管在CDN上进一步提升性能。相比之下，Snowflake代理请求因CDN的中介作用，通信延迟明显增加。尤其在代理信息动态且无法缓存的情况下，用户需等待代理中介的响应，这种高延迟特性使其与普通web请求明显不同。文中统计了每个请求流的前40个数据包的发送和接收时间，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WE6PLW6MbW2d7eicTeJ6Q8kl4XN1wLyYrbaJrREId29ope0NtopPlt5Ja2U353iaYpbdtibeVKbtDlTA/640?wx_fmt=png&from=appmsg)

4. 网络速度：由于高延迟和较少的最大数据包数量，Snowflake代理请求的传输速度显著低于普通web请求。实验表明，Snowflake请求的网络速度仅为1.24KB/s，而普通web请求中最慢的也达到了77.42KB/s。

### 3、实验设置

#### 3.1 数据集设置

为了确保方法的实用性，本文采集了真实世界的流量数据用于训练机器学习模型。

1. 雪花代理请求流量：通过手动运行snowflake-client软件获取，避免对代理服务性能造成短时间影响，同时考虑到不同版本的Tor浏览器，确保数据的多样性和代表性。
2. 正常网络请求流量：使用Chrome、Firefox和Edge等主流浏览器访问Alexa前500的网站，并进一步采集视频、音频、图片和文件请求流量。此外，还包括了网络聊天、在线购物、在线会议、流媒体播放、远程桌面等多种类型的正常请求流量。

本文只捕获HTTPS流量（TCP端口443），并将其保存为pcap文件，每个文件对应一条流量记录。

#### 3.2 Snowflake流量和normal流量特征提取

从数据流量的数据包大小、方向、时间、网络速度四个方面提取统计特征：

1. 大小相关特征：包括上下行数据包大小的分布熵值、频率前五的包大小及其占比，共23维。
2. 方向相关特征：统计上下行数据包数量及占比，以及下行与上行的包数量比，共5维。
3. 时间相关特征：计算上下行方向上连续两包之间的时间间隔，并划分为29个不同比宽度的区间，每个区间的值为该区间的时间间隔占比，共58维。
4. 网络速度特征：计算上下行及整体流量的网络速度，共3维。

#### 3.3 模型（检测器）训练和评估指标

采用决策树（Decision Tree）算法进行分类。模型为二分类，只输出正类（代理请求）或负类（正常请求）。

评估指标包括准确率（Accuracy）、召回率（Recall，或真阳性率）和误报率（FPR），均为流量分类领域的标准指标。

### 4、实验结果

#### 4.1 流长度选择

雪花代理请求通常涉及30到50个数据包的流量。为确保检测的及时性，需尽早完成检测，以避免用户在检测完成前已获取代理信息。实验测试了不同流长度（5, 10, 15, 20, 25, 30,35）的检测准确率，发现流长度超过30个数据包后准确率趋于稳定，达到99.58%。为平衡准确率与效率，后续实验采用30个数据包的流长度。

#### 4.2 总体性能

实验显示检测器性能卓越：平均准确率为99.73%，召回率（Recall）为98.96%，误报率（FPR）约为0.25%。且检测结果在多次实验中波动较小，说明所提取特征能够有效区分代理请求与正常请求。

#### 4.3 多版本测试

从五个主要版本的Tor浏览器中分别采集了20条代理请求流量，测试结果显示在不同版本的雪花代理请求中表现出良好的泛化能力。最低召回率（Recall）为90%（Tor Browser版本11.5.7），其余版本均达100%。证明无需频繁针对新版本重新训练模型，方法具有实际可用性。

#### 4.4 误报测试

利用Stratosphere项目的15个数据集测试误报率（FPR），结果显示每个数据集的误报率（FPR）均小于20%，最高为12.91%，平均误报率为7.66%，其中两组数据集的误报率接近零。低误报率表明检测器对正常流量的干扰较少，具有较高的实际应用价值。Snowflake代理请求检测分类器在15个数据集中的误报率（FPR）如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WE6PLW6MbW2d7eicTeJ6Q8kl4OBfloxklGaXjUOkEmkjxmQ9ibtja6QGT7gDibZCRXpwwjrMXpgicPqWg/640?wx_fmt=png&from=appmsg)

### 5、本文贡献

本文研究通过检测代理请求来阻断雪花代理系统，并在实验中验证了其可行性与高效性。主要贡献如下：

1. 基于用户依赖代理请求获取Snowflake代理的特点，提出通过阻断代理请求来实现阻断代理本身的效果。
2. 分析发现Snowflake代理请求在伪装正常网络请求方面存在漏洞，其在数据包大小、方向、时间间隔、网络速度等方面易于被区分。
3. 利用决策树模型，通过流量中的前30个数据包提取特征进行检测。结果显示，检测器在不同版本中召回率（Recall）接近100%，对正常流量的平均误报率（FPR）为7.66%，表明方法具备高效性和实际应用价值。

本文的代码与数据集：*https://github.com/Xanole/SnowDT*

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

安全学术圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

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