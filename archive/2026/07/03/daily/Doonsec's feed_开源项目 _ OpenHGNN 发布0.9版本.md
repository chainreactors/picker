---
title: 开源项目 | OpenHGNN 发布0.9版本
url: https://mp.weixin.qq.com/s/TepQtZHR_YOgpoNiU08oJg
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:46:30.591261
---

# 开源项目 | OpenHGNN 发布0.9版本

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6gtnxe1uggEwazaRbdTz8gia19Yor6Xr5lNONFBMia8pLm8dzFEfJkCmDoRd45J4gywujrjq4E8TicPAPxJnnkJ4wqIALM6ZASuV3p1sSVSIwM/0?wx_fmt=jpeg)

# 开源项目 | OpenHGNN 发布0.9版本

原创

曹文轩
曹文轩

北邮 GAMMA Lab

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图1：OpenHGNN v0.9 release overview](https://mmbiz.qpic.cn/sz_mmbiz_png/6gtnxe1uggGNVs859ltYibhRUy0h2nQfyjtHGYiclZps5IxSPsaicia4NQTnfFOfcqzwTKHz1GIWngFHBNpEKocXbaUqWOX6dkqkbrmZbVmftfM/640?wx_fmt=png&from=appmsg)

图1：OpenHGNN v0.9 release overview

OpenHGNN 现已推出最新的 0.9 版本，欢迎大家从启智社区、GitHub 或通过 pip 下载使用。OpenHGNN 是一个基于 DGL 的开源异质图神经网络工具包，面向异质图模型研究、算法复现和下游应用实验，集成了异质图神经网络领域的前沿模型、训练流程、任务接口和数据处理能力。

相比此前版本，OpenHGNN 0.9 不只关注模型数量增长，也更加重视文档完整性、模型接入规范和 DGL 原生实现。新版本新增 10 个模型贡献，对应 11 个注册模型名；新增 `node_regression` 任务，支持连续值节点标签预测；同时系统更新模型文档、复现指南和任务说明，让用户更容易发现、运行和复现模型，也让贡献者更清楚如何把新算法集成到 OpenHGNN 中。

## 一、新增异质图神经网络模型

OpenHGNN 0.9 版本新增 10 个模型，覆盖异质图表示学习、自监督学习、异质时序图、图级表示、推荐和关系数据建模等方向。这些模型来自 NeurIPS、IJCAI、SIGIR、ICML、KDD、ICLR 等会议或近期预印本工作。

![图2：OpenHGNN v0.9 model contributions](https://mmbiz.qpic.cn/mmbiz_png/6gtnxe1uggGEtdcq5bt6K9d8rDTdLv4waLZSibuEBO9MpoenMjZc5ABZtYrALJFGbAtJpPbJx5GiccrEMPAy5uwnkl2Qr9M3D6OQzoUNyP6pA/640?wx_fmt=png&from=appmsg)

图2：OpenHGNN v0.9 model contributions

| 模型贡献 | 注册模型名 | 会议/来源 | 主要任务 |
| --- | --- | --- | --- |
| HGDL | `HGDL` | NeurIPS 2024 | 节点分类/标签分布学习 |
| HGEN | `HGEN` | IJCAI 2025 | 节点分类 |
| HGSketch | `HGSketch` | SIGIR 2025 | 图级表示 |
| HGOT | `HGOT` | ICML 2025 | 节点分类 |
| RMR | `RMR` | KDD 2024 | 节点分类 |
| HERO | `HERO` , `HERO_homo` | ICLR 2024 | 节点分类 |
| SEHTGNN | `SEHTGNN` | NeurIPS 2025 | 节点分类、链路预测、节点回归 |
| HTGformer | `HTGformer` | SIGIR 2025 | 链路预测、节点分类、节点回归 |
| HCMGNN | `HCMGNN` | IJCAI 2024 | 推荐 |
| RelGT | `RelGT` | arXiv 2025 | 关系数据预测 |

这些新增模型让 OpenHGNN 进一步覆盖近期异质图学习的重要方向。更重要的是，v0.9 将模型贡献与文档、复现命令、任务说明和注册表检查结合起来，使模型不仅“进入仓库”，也能被用户通过统一入口发现、运行和验证。

## 二、文档体系更新与复现路径优化

随着 OpenHGNN 模型数量不断增加，用户最常遇到的问题不再只是“库里有没有这个模型”，而是“这个模型怎么安装、怎么运行、用什么数据、指标是多少、失败时该查哪里”。OpenHGNN 0.9 围绕这一问题重新整理了文档入口。

新版本补充了快速开始、模型总览、任务总览、模型复现指南和 0.9 release note。每个 v0.9 新模型的文档都尽量统一到固定字段：论文来源、注册模型名、支持任务、trainerflow、数据来源、预处理方式、运行命令、评估指标、预期结果、硬件/耗时说明和随机种子。用户可以从 README 直接进入模型复现页，也可以从 Sphinx 文档中按任务或模型查找运行方式。

这意味着用户不需要在 README、源码、PR 讨论和输出目录之间来回查找信息。对贡献者来说，新增模型需要补齐哪些材料也更加明确：模型代码、数据接入、配置、README/文档和复现实验说明都有了更统一的参考格式。

## 三、新增 node regression 任务

OpenHGNN 0.9 新增 `node_regression` 任务，用于处理节点标签为连续值的异质图学习问题。相比节点分类任务，节点回归更关注数值预测能力，适用于属性估计、时序数值预测、风险分数预测和回归型下游评估等场景。

在新任务中，模型可以通过统一的 `task`、`dataset` 和 `trainerflow` 接入节点回归流程，数据集侧提供连续值标签，评估侧使用 MAE、RMSE 等回归指标。这样，支持连续值预测的模型不需要在各自 trainer 中重复实现一套回归逻辑，而是可以复用 OpenHGNN 的统一任务入口。

例如，SEHTGNN 可以通过如下命令运行节点回归任务：

```
python main.py -m SEHTGNN -d sehtgnn_covid -t node_regression -g 0 --use_best_config
```

`node_regression` 的加入扩展了 OpenHGNN 的任务覆盖范围，使其在节点分类、链路预测、推荐等常见任务之外，也能覆盖更多真实场景中的连续值预测需求。

## 四、基于 DGL 的统一模型体验与辅助 skill

OpenHGNN 围绕 DGL 构建异质图学习能力。v0.9 继续强化这一特点，让新增模型能够更好地复用 DGL 的异构图表示、采样流程、消息传递机制和图神经网络算子。

为了让用户和贡献者更快上手，本版本还在仓库中新增了 `openhgnn-algorithm-developer` skill。它沉淀了 OpenHGNN 常用的模型运行、结果复现、任务选择、`Experiment` 故障排查和新算法接入流程。用户可以用它快速定位模型、数据集和运行命令；贡献者也可以参考它检查模型、trainerflow、dataset、task、配置和文档是否与 OpenHGNN 的 DGL 体系保持一致。

安装方式也很简单。克隆 OpenHGNN 后，可以将仓库中的 skill 复制到本地 Codex skills 目录：

```
mkdir -p ~/.codex/skills
cp -r skills/openhgnn-algorithm-developer ~/.codex/skills/
```

之后重新开启 Codex 会话，即可通过 `$openhgnn-algorithm-developer` 调用该 skill，辅助模型复现、问题定位和新算法接入。

通过更统一的 DGL 模型体验和辅助 skill，OpenHGNN 0.9 希望让前沿异质图模型更容易被发现、运行、比较、复现和继续扩展。

## 五、推荐环境与安装方式

OpenHGNN 0.9 推荐使用 Python 3.11、PyTorch 2.4.0、DGL 2.4.0+cu121 和 CUDA 12.1。仓库中新增了 `constraints.txt`、`environment.yml` 和 Dockerfile，用于帮助用户构建更稳定的复现环境。

```
conda create -n openhgnn python=3.11
conda activate openhgnn
pip install -c constraints.txt -r requirements.txt
pip install -e .
```

用户也可以继续从 GitHub、启智社区或 pip 获取 OpenHGNN，并根据文档选择 CPU/GPU 环境和具体模型依赖。

## 结语

OpenHGNN 0.9 的发布目标不是简单堆叠更多模型，而是把模型库从“有代码”推进到“有文档、可运行、可复现、可维护”。我们希望通过更完整的模型文档、更规范的模型接入和基于 DGL 的统一模型体验，让 OpenHGNN 成为更可靠、更易用的异质图神经网络开源工具包。

欢迎大家继续将自己的异质图算法集成到 OpenHGNN 中。感谢大家一直以来对 OpenHGNN 算法库的支持，我们将持续围绕异质图模型、训练流程、数据集、文档和工程质量进行改进。

* GitHub 地址：https://github.com/BUPT-GAMMA/OpenHGNN
* 启智社区地址：https://openi.pcl.ac.cn/GAMMALab/OpenHGNN
* Email: wenxuanc@bupt.edu.cn

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AYxz3cIHvyoiayibng0FojESWtukKaO5zH1D94qCSeOjkzZpNfKoYddl1n8FJ7j610Wa5W4BSTtwBa4Y0QsC8d7Q/0?wx_fmt=png)

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