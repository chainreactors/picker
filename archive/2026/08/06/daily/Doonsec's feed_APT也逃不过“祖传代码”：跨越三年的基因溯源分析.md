---
title: APT也逃不过“祖传代码”：跨越三年的基因溯源分析
url: https://mp.weixin.qq.com/s/Bv5coxOIyNuIMsycud36uQ
source: Doonsec's feed
date: 2026-08-06
fetch_date: 2026-08-07T04:25:52.785430
---

# APT也逃不过“祖传代码”：跨越三年的基因溯源分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/m4YnfITRpGtkUpia5PZF4IOpBRibAD2ExNWNdFjhCwalO9oEFfbnkZPxmI0b6SzEdF6ucIkTxFSvMebPKUR6DxWwYAIv6NUM5rbFX0kDb2spo/0?wx_fmt=jpeg)

# APT也逃不过“祖传代码”：跨越三年的基因溯源分析

数默科技
数默科技

数默科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m4YnfITRpGujLcokQbKUI714jH7eZGdycZH2ytfEoZVR6fFicnHZqvjDUyVrPv9P4Ot6gvEaVWot25icQXCYs66iaqib1PvFbYNcSmS2YWUjqWg/640?wx_fmt=png&from=appmsg)

近期，安全分析团队捕获到一个下载器样本。该样本为近期重新编译的变体，IOC、YARA 规则、元数据关联均未命中有效情报——常规溯源路径基本走到了尽头。

团队转而从样本的“深层语义”特征入手，利用样本基因同源分析技术，最终发现与2023年和2025年的两个样本存在同源关系。综合代码特征、历史样本关联及内部掌握的其他攻击活动证据，分析人员以较高置信度判断：该样本与某APT组织既有工具链存在关联

**样本概况**

这个样本本身行为比较简单，主要流程如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m4YnfITRpGuc8ibAdd4kkK3atnVw6kdxvJ7Xv2O2pHyK7vjF7365Ssd4azcKQzhEUJ64A1mpKapJPEvko6AcJAnbM0YZoYJqnIGY9fFNQTcU/640?wx_fmt=png&from=appmsg)

样本是重新修改和编译的全新样本，编译时间戳与硬编码和混淆的C2特征均支持这一判断，这对IOC、YARA和其他基于传统“表层特征”的分析工作带来很大挑战。

**从“表层特征”到“基因溯源”**

“表层特征”会变，但代码的意图和结构很难变。我们将样本的特征拆成三个层次来看：

* **表层特征**

  IOC、Hash、二进制：AI时代变种的生产成本大幅降低，迭代速度快，让溯源工作难度激增。
* **中层实现特征**

  具体的算法逻辑、流程结构、数据结构：会随版本迭代变化，但变化范围小，变化速度慢。这和很多软件项目中的“祖传代码”一样，可能会修修补补，但大体流程和局部细节不会变。
* **深层语义特征**

  攻击逻辑链条本身：攻击意图的变化通常改动最小。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m4YnfITRpGv2qPiaHRhWsLs5dyQeavhevBl3VBehNIjK0l3FNk5qXcg7rY9e3XsPvPHpKNnlg4vq6fUohGz1msrhicyVFibApibn5xLmrD3rYow/640?wx_fmt=png&from=appmsg)

“中层实现特征”与“深层语义特征”构成了样本基因溯源的核心逻辑。中层与深层特征的提取，依赖AI对代码语义的自动化理解，而非人工规则，从而支撑起具有高鲁棒性的样本基因同源分析技术。

分析团队利用样本基因同源分析技术在历史样本库中检索，关联出具有某APT组织背景的两个不同样本。

![](https://mmbiz.qpic.cn/mmbiz_png/m4YnfITRpGtIBFHZFE5bMmkKydcocIRTzXJN8zwmxibxcqEYkdCX9STQSIh9wvevosv8YzKcZRaBZ2ibykibLbfsYibaPs3dGmicrpgWGL5GnbD0/640?wx_fmt=png&from=appmsg)

(样本检索结果视图，TOP 2具有较高同源置信度)

![](https://mmbiz.qpic.cn/mmbiz_png/m4YnfITRpGsttOGPAKuKVAiciaDjDMWq3p8JicwWduf5Lp5OKAEvS8X5ib0KtWRb7xgIHoSfK4Soj7bfJ4CHnDtb2UjHDsB4gk7GhLw7vicR1RM0/640?wx_fmt=png&from=appmsg)

（样本代码对比视图，深度相似度达到0.97）

本次样本（2026年）与历史样本A（2025年）和历史样本B（2023年）存在关联。通过分析发现这3个样本的行为意图、代码结构和局部代码习惯高度相关。将关键特征放在一起逐项比对，会看到高度同源的对应关系：

|  |  |  |  |
| --- | --- | --- | --- |
| **特征项** | **本次样本（2026）** | **样本A（2025）** | **样本B（2023）** |
| **隐窗+取用户名** | ✓ | ✓ | ✓ |
| **用户名缓冲区大小** | 0x100 | 0x100 | 0x100 |
| **硬编码URL混淆算法** | Base64+栈字符串混淆 | Base64 | XOR单字节 |
| **URLDownloadToFileA/W****下载文件** | W | W+A混用 | W |
| **伪装落地文件名** | W\*\*\*\*\*\*\*.exe | L\*\*\*\*.exe | I\*\*\*\*\*\*\*\*.exe |
| **拉起执行** | CreateProcessW cmd.exe /c   "..."×2 | CreateProcessA/W + cmd.exe | 线程后台执行 |
| **执行隐藏参数** | dwFlags=1, wShowWindow=0 | dwFlags=1, wShowWindow=0 | dwFlags=1, wShowWindow=0 |

三年间，攻击者极可能长期复用同一套 “祖传代码”，虽然样本的字符串混淆方式、释放路径、进程执行方式几经改写，但核心代码意图与结构特征始终一致。比如三个样本代码段开头均为：GetConsoleWindow + ShowWindow + GetUserNameW/A，并沿用了相同大小的缓冲区和相同的路径拼接逻辑。

需要指出的是，其中任何单一特征都不足以定论——隐藏窗口、下载文件、拉起执行，都是下载器家族的常见行为。但当函数调用序列、缓冲区大小、隐藏参数配置、路径拼接逻辑这一组指纹同时吻合时，若非同源传承，独立演化出如此吻合的特征组合，可能性微乎其微。这正是我们将三个样本判定为同源、并作出归因判断的核心依据。

**总结**

对攻击者而言，换一层混淆的成本以天计，重写一套经过实战检验的攻击逻辑，代价要高得多。基因溯源的意义，就在于把防御的主战场，从攻击者“最容易换”的那一层，转移到“最难换”的那一层。

而支撑这种回溯能力的，是持续沉淀的样本基因——检测指标的有效期以天计，样本基因的有效期以年计。这次跨越三年的关联，正是历史样本库价值的直接兑现。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/cSMPHO3DWPPXrhseMvecEsDhO73EPlhiaM0SJOJich7Ubv3btA88agKl6p7R1rpYorafMEhibF5ymg7TPNTFD8xQw/0?wx_fmt=png)

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