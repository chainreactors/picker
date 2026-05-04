---
title: DNS隧道检测的新方法：我们靠什么做到了99.9%的精准率？
url: https://mp.weixin.qq.com/s/-0Pk_idwHLAi4hqYR79GBA
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:29:19.932017
---

# DNS隧道检测的新方法：我们靠什么做到了99.9%的精准率？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibeia1PgnviaqesvHm0sib6FboF8hib6icjTSibkHq4XLfG7PHM6uMhAxL4KHt7zsqopUnhMgRdK6y20s2Fbic9lGEpapfxjX4o8TQrvkU/0?wx_fmt=jpeg)

# DNS隧道检测的新方法：我们靠什么做到了99.9%的精准率？

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> DNS隧道攻击是把数据藏在合法的DNS查询里偷运出去。我们构建了一个机器学习检测系统，通过引入卷积自编码器提取的重建损失和基于分词分析的新特征，将检测精度推到99.9%，误报率极低。这套系统现在每天能实时处理数十亿次查询。

## 被滥用的“电话簿”

DNS，可以理解为互联网的电话簿，把“google.com”翻译成“8.8.8.8”这样的IP地址。问题在于，防火墙通常对DNS流量放行且很少仔细检查，这成了攻击者眼中的“高速公路”。

他们把命令、偷来的数据，编码塞进一长串看似混乱的子域名里，比如“po3asvtjvfkebjuke4qsvf3ja6agsznrt.tunnel.com”，就能建立一条隐蔽的通信隧道。从Decoy Dog、Saitama到DNS Anchor，越来越多的恶意软件在用这招绕过防御。

检测这事儿一直很难。合法的DNS查询也可能很长很怪，你需要一套法子，能分辨什么是正常的“怪”，什么是在偷东西。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfkLbvCe050Z5V5l3JYw5h59oKicHLZGUgVMQmTtW0xC79MWeCLewOZe9Z8NfkGV3IHHaTO1TZMbz3uZbHq6mxTm08O02jwPQC4/640?wx_fmt=jpeg&from=appmsg)

## 数据：先分清“容易题”和“难题”

我们的数据来自各家公司的DNS日志。要训练模型，首先得准备好“好”的和“坏”的样本。

所谓“好”的样本，是从真实网络流量里精心挑选的。但我们做了两件重要的事来提升训练质量：第一，过滤掉查询量最大的前500个有效二级域名（SLD），比如google.com这类。它们占了总流量的一半以上，但识别它们太容易，对提升模型判断力没帮助。把它们去掉，能逼着模型去啃更难啃的骨头。

第二，我们还得把那些合法的“隧道”应用剔除，比如一些杀毒软件、垃圾邮件过滤器自带的DNS查询功能。在实际部署中，我们有单独的流程来放行这些已知的良性应用。

至于“坏”的样本，我们收集了成千上万个DNS隧道查询，涵盖了几乎所有主流工具，比如Pupy、DNSCat2、Sliver、Iodine，还有Cobalt Strike，甚至包括一些安全研究员自己写的定制工具。这样能确保模型见过的“坏”足够多，也足够狡猾。

### 一个训练样本切片

| 流量类型 | 时间戳 | 源IP | 查询域名 (QNAME) | 查询类型 | 响应码 | 资源记录 |
| --- | --- | --- | --- | --- | --- | --- |
| 良性 | 2024-05-01 00:01:59 | 192.168.4.2 | google.com | 1 | 0 | [8.8.8.8, 500] |
| 隧道 | 2024-05-01 00:01:59 | 192.168.4.12 | po3asvtjvfkebjuke4qsvf3ja6agsznrt.12237.2b.dd.tunnel.com | 1 | 0 | [35.18.9.23, 0] |

## 特征工程：两个杀手锏

特征，就是我们从原始DNS数据里提炼出来的、能区分好坏的关键指标。我们提取了近20种特征，但其中两个是我们的独门武器。

### 1. 自编码器重建损失：让模型感受“正常”的脉搏

第一个新法子，是用一个轻量级的一维卷积神经网络（CNN）自编码器。这个自编码器是个无监督模型，我们用400万个正常域名前缀（就是“www.”之后，“.com”之前的那部分）来训练它。

它的任务是学习“压缩”和“解压”一个域名前缀。训练之后，它会对正常域名的模式（比如常见的单词、缩写）了如指掌。当一个新的域名前缀输入时，自编码器会尝试重建它。

如果是正常域名，重建起来很容易，损失值很低。但如果是一个充满随机字符的隧道前缀，比如“2po3asvtjvfkebjuke4qsvf3ja6agsznrt”，模型就会懵，重建得一塌糊涂，损失值很高。这个“重建损失值”，就成了一个非常强有力的特征。

我们还改进了损失函数，以消除域名长度不一带来的干扰，让这个特征更稳定。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibcj3eFGRwrLW1uTgc77AJDZTxwgn37ZpvHHYELDFzPmoHuZVTz9iaGTDEBTd8mIvnR3XKS1DmELqvHIcfGjYoskJOicQgjSRiaF1Y/640?wx_fmt=jpeg&from=appmsg)

### 2. 分词比率：数数有几个“词”

第二个法子，想法很直接：大部分正常域名用的是自然语言词汇，而隧道域名用的是编码（如十六进制、base32），看起来像乱码。

我们用一个基于成本的分词算法，尝试把域名前缀拆解成字典里存在的单词。比如“facebooksecurity”可以完美拆成[“face”, “book”, “security”]，一共3个片段。

但“youjf34gwid86fih”这种编码字符串，只能被拆成[“you”, “j”, “f”, “34”, “g”, “w”, “id”, “86”, “f”, “i”, “h”]这样11个零碎的片段，因为没有哪个字典认得“jf34”这种东西。

于是我们得到一个关键特征：片段数与域名长度的比值（分词比率）。良性域名这个比值通常很低（如0.19），而隧道域名则非常高（如0.69）。

### 特征示例表

| 类型 | 前缀 | 分词结果 | 片段数 | 前缀长度 | 分词比率 |
| --- | --- | --- | --- | --- | --- |
| 良性 | facebooksecurity | [“face”, “book”, “security”] | 3 | 16 | 0.19 |
| 隧道 | youjf34gwid86fih | [“you”, “j”, “f”, “34”, “g”, “w”, “id”, “86”, “f”, “i”, “h”] | 11 | 16 | 0.69 |

## 结果与权衡：为什么是随机森林？

我们用多种算法试了，最终随机森林（Random Forest）完胜。下面是关键数据对比：

| 指标 | 随机森林分类器 (%) | 逻辑回归分类器 (%) |
| --- | --- | --- |
| **查询级F1分数** | **99.71** | 90.32 |
| **SLD级F1分数** | **96.79** | 50.96 |
| **SLD级查准率** | **94.97** | 34.76 |
| **SLD级查全率** | **98.69** | 95.42 |

这里得重点说说SLD级（域名级）指标，因为它直接关系到实际运维。查全率（Recall）接近99%，意味着几乎所有的隧道域名都能被逮住，漏网之鱼极少。查准率（Precision）95%，意味着被我们标记为“可疑”的域名里，有95%确实有问题，只有5%是误报。

这5%的误报重要吗？非常重要。我们最终要阻断的是整个域名，而不是单次查询。如果一个正常域名被误阻断，可能会影响客户业务。逻辑回归模型在域名级查准率只有34.76%，意味着它每标记3个“坏”域名，就有2个是误报——这对安全团队来说简直是灾难。

我们选择了高查全率略优先的策略。宁可多抓一些可疑的（保证不放过坏人），然后通过后续的“二次验证”流程（比如核查信誉、检查基础设施）把误报过滤掉，也不愿因为一开始就卡得太死而漏掉真正的攻击。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibdaaiaNc7Hr5mpXzD8Yaf2ickRVpof2WWo1ia5zmS1IQdGHrPanbZtQNzb9ibGdcX2gQxI7cialkz3XvcuYfMBMQGIXicAeZ4CWC4Qps/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibeGOKMY1B268Mib2XzlNXkgOY18Kyz19aZUI7jxYibCLnCBw0WdmFfzmQ869zG2uPWiaibs3NqGlGQrOhqkc3Svuw83oAhf6MqCoSY/640?wx_fmt=jpeg&from=appmsg)

## 新特征到底有多重要？

拿掉我们创新的自编码器损失和分词比率这两个特征会怎样？我们做了“消融实验”。

结果是：SLD级查准率从95%暴跌到86%，F1分数从97%降到92%。这意味着每天在数十亿次查询的规模下，误报数量会激增，给二次验证带来巨大压力。

所以结论很清楚，这两个新特征不是锦上添花，而是我们实现高精度、低误报的核心。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibcqZaxgkV8sUEvJ1g0Qj1vB0t0wSkDsicBiaZ13fNsecvOUqsfOR7VMNlgXTBX897AGibXnJMVLgZnWFcsGXspGjOdseKTg1wt8Hg/640?wx_fmt=jpeg&from=appmsg)

## 在生产中运转

这套系统已经在我们的平台实时运行。它能近乎实时地处理数十亿DNS查询，秒级发现潜在隧道。检出可疑域名后，会进入前面提到的二次验证环节，比如核对已知良性应用名单、分析域名关联的基础设施信息，结合威胁情报再次研判。

最终，确认无误的恶意隧道会被自动阻断并告警，而那些“虚惊一场”的合法流量则被放行。说实话，这种规模和精度的结合，才是让它真正能用的关键。毕竟，一个只能在论文里跑出高分的模型，对现实世界的攻击是没用的。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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