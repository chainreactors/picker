---
title: [智能体攻防实战] 一.大模型赋能网络入侵检测实战探索（CodeBuddy和d.run实现）
url: https://mp.weixin.qq.com/s/iatnItf7YOAYAQyVA69AJg
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:25:37.500782
---

# [智能体攻防实战] 一.大模型赋能网络入侵检测实战探索（CodeBuddy和d.run实现）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZaibroIiatwe2PiaGTibAK7s7GFibTyMSfGxqzxwhFhqCPERtIicD4DLLic68MmoSdMXaZ5BJkIYqV8Ycj3JtiaNx5S5rFf2HHb2SsEOpt5x8aA1Fmc/0?wx_fmt=jpeg)

# [智能体攻防实战] 一.大模型赋能网络入侵检测实战探索（CodeBuddy和d.run实现）

原创

Eastmount
Eastmount

娜璋AI安全之家

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**为了更好地分享AI Agent在网络安全领域的实践方法与应用经验，作者正式开启“智能体攻防实战”专栏。本专栏将围绕“大模型如何赋能网络安全攻防实践”和“大模型及智能体内生安全”这两个主题展开，重点关注AI Agent、AI Coding、自动化分析、入侵检测、威胁情报、漏洞研判与安全运营等方向，尝试将大模型的语义理解、代码生成、工具调用和安全知识推理能力融入真实安全任务中。通过系列化案例，专栏希望降低网络安全实验、算法复现和工具开发的实践门槛，为安全研究人员、开发者和初学者提供更加直观、可操作的技术参考。基础文章，希望对您有帮助。感恩分享的第15年，fighting！**

本文作为“智能体攻防实战”专栏的第一篇，将以“大模型赋能网络入侵检测”为核心任务，探索如何借助CodeBuddy和d.run完成入侵检测实验的构建与运行。文章首先概述AI Agent在网络安全中的典型应用，然后基于CodeBuddy自动生成机器学习与深度学习入侵检测代码，进一步结合d.run在线环境完成实验运行、模型评估和结果分析。通过该案例，读者可以初步理解AI Agent如何贯穿数据预处理、特征提取、模型训练、性能评估和报告生成等环节，为后续开展智能化安全分析与攻防实验奠定基础。

代码开源地址：

* https://github.com/eastmountyxz/Agent-for-security

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe0Rg2dy1CnBFTlV3L8mjQspGudSVdaP6TiblbdN3ia5dcfWXAwJ1JUhJ3KuvFBJozwcPFdicsz0jJfMYeZOBqxUvFhFYRC7vMicRH4/640?wx_fmt=png&from=appmsg)

### 文章目录

* 一.AI Agent赋能网络安全概述
* 二.CodeBuddy自动构建机器学习IDS
* 三.CodeBuddy自动构建深度学习IDS
* 四.云端d.run运行深度学习入侵检测系统

+ 1.配置d.run平台
+ 2.运行深度学习代码

* 五.总结及新书推荐

**前文赏析：**

* [智能体攻防实战] 一.大模型赋能网络入侵检测实战探索（CodeBuddy和d.run实现）

**传统安全专栏：**
![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe25Ncu7unrOgpUVvom6438ibDhA0waHVibEeIwXYUtpTBEQDKcXgRKYGLGUyibDrOhhicqrED0Sdicxd3ItMdVibEPNbiaHNicQ3gwsaick/640?wx_fmt=png&from=appmsg)

---

# 一.AI Agent赋能网络安全概述

随着大模型、AI Coding与自动化生成技术的发展，AI Agent正在成为网络安全领域的重要智能化支撑。与传统安全工具主要依赖规则库、特征库和人工配置不同，AI Agent能够基于自然语言理解、安全知识推理和多源数据分析能力，对网络流量、系统日志、威胁情报、漏洞信息和告警事件进行综合研判。其核心作用并不是简单替代安全人员，而是将大模型的理解能力与安全工具链的执行能力结合起来，辅助完成从威胁发现、异常分析、攻击溯源到响应处置的全过程任务，从而提升网络安全工作的自动化、智能化和可解释化水平。

在实际应用中，AI Agent更适合作为网络安全任务中的“智能协同助手”。一方面，它可以帮助安全人员快速理解复杂数据和异常现象，例如对入侵检测结果进行解释、对日志告警进行归因、对漏洞风险进行分析；另一方面，它也可以调用代码运行、数据分析、可视化展示和报告生成等工具，辅助完成安全实验与工程实践。尤其在网络入侵检测场景中，AI Agent能够贯穿数据预处理、特征提取、模型构建、性能评估和结果分析等环节。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1buzq9S0c7ibbXlTkRk5Wyzf3eaXiacYGbepfYEib9IthehFEueicLibd8FWN6XYjKqeGtTVQTgibGJzISS1pYoSvNg1q9T3cmTZpaI/640?wx_fmt=png&from=appmsg)

AI Agent赋能网络安全的本质，是将大模型的语义理解、知识推理、代码生成与工具调用能力嵌入安全业务流程，使其能够辅助完成“感知—分析—决策—响应”的闭环任务。具体而言，其应用可体现在以下几个方面。

* **网络入侵检测辅助**
  AI Agent可参与网络流量数据分析、异常行为识别与入侵检测模型构建，辅助安全人员发现潜在攻击行为。相较于传统规则检测方法，Agent能够结合上下文语义、历史告警和模型输出结果，对异常流量进行更具解释性的分析。
* **安全日志智能分析**
  在主机日志、系统日志、防火墙日志和Web访问日志分析中，AI Agent能够自动提取关键字段、识别异常模式并归纳事件线索。其优势在于能够将分散的日志信息转化为结构化安全事件，降低人工筛查成本。
* **威胁情报理解与关联**
  AI Agent可以对安全报告、漏洞公告、APT分析文章和开源威胁情报进行语义解析，提取攻击组织、攻击工具、漏洞编号、攻击手法等关键信息。通过与ATT&CK框架、历史事件和内部告警进行关联，Agent能够辅助判断威胁来源与攻击阶段。
* **漏洞分析与风险研判**
  面对漏洞描述、CVE公告和代码片段，AI Agent可辅助分析漏洞成因、影响范围和潜在利用方式。它还可以结合资产信息与暴露面情况，对漏洞风险进行优先级排序，帮助安全团队确定修复顺序。
* **恶意代码辅助分析**
  在恶意脚本、可疑样本或混淆代码分析中，AI Agent能够辅助解释代码逻辑、识别可疑函数调用和潜在恶意行为。对于安全初学者或分析人员而言，Agent可将复杂代码行为转化为可理解的自然语言说明。
* **攻击链溯源分析**
  AI Agent能够将告警、日志、流量和威胁情报进行关联，辅助还原攻击者从初始访问到横向移动、权限提升和数据外传的完整路径。通过攻击链视角分析，安全人员可以更清晰地理解攻击过程和关键风险节点。
* **检测规则生成与优化**
  AI Agent可根据攻击样本、日志特征或威胁情报内容，辅助生成YARA规则、Sigma规则、Snort规则或IDS检测逻辑。与此同时，它还可以根据误报情况和样本变化，对规则条件进行优化，提高检测规则的适用性。
* **安全自动化响应**
  在安全运营场景中，AI Agent可根据告警等级和处置策略，辅助生成封禁IP、隔离主机、停用账号或通知管理员等响应建议。与自动化工具结合后，Agent能够推动部分低风险、标准化任务的半自动化执行。
* **安全报告自动生成**
  AI Agent能够根据检测结果、日志分析过程和模型评估指标，自动生成安全分析报告、入侵检测实验报告或事件复盘材料。该能力有助于提升安全实验记录、攻防演练总结和日常运维汇报的规范化水平。
* **安全代码辅助开发**
  在网络安全实验与工具开发中，AI Agent能够辅助完成数据读取、特征提取、模型训练、接口调用和可视化代码编写。结合CodeBuddy等AI编程工具，开发者可以更高效地构建入侵检测原型系统，降低安全算法实践门槛。
* **攻防演练辅助决策**
  在红蓝对抗和攻防演练中，AI Agent可以辅助分析攻击路径、生成防守建议并总结演练过程中的薄弱环节。它并非替代安全专家，而是作为智能辅助工具提升攻防研判效率和复盘质量。
* **安全知识问答与培训**
  AI Agent可基于安全知识库、漏洞案例和攻击技术框架，为学习者提供网络安全概念解释、实验步骤指导和问题排查建议。对于教学和培训场景而言，其能够降低网络安全学习门槛，并提升实践教学的交互性。

---

# 二.CodeBuddy自动构建机器学习IDS

下面介绍CodeBuddy调用大模型或智能体构建入侵检测模型代码的具体过程。整个流程如下图所示：

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe2DPMkenLjsG6sg2eLtVYT7kVckrPIC9rr1K0sWZRwHdDDw3XgTFpRD70mf4CWdicYiaoj9Lwkq99M58QO2RjBicWBBZHyWxCqCrU/640?wx_fmt=png&from=appmsg)

本文构建的数据集如下图所示，关键字段包括：

* **payload\_id**

  恶意请求payload编号
* **attack\_type**

  网络攻击类型，包括八种常见类型 XSS、SQLi、SSI、LDAPi等
* **obfuscated\_url**

  混淆恶意请求Payload
* **url\_n\_gram**

  使用N-gram提取特征

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1aH5CayCOvjQTRnFOabmibC6hJSibXsJw74nh0ypUPvmLQJgh8ATiax8qia4IWD9dGaicI8JSu57BIGsanWGkqiczMeOXvsw4YqbYGg/640?wx_fmt=png&from=appmsg)

**第一步，在本地构建IDS目录（工程），打开CodeBuddy IDE。** 其主界面如下图所示，打开该工程文件夹。在IDS工程中包含data文件夹，包含训练集、测试集和验证集3个CSV文件。

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe0RAcXd4Cv4VFRkvmP3p8gFaYsSh8I1r4s66CPjpicaag5GRHg6SpgO2yISusL4aT2us17jxMKdfw9bj9wxJWJUXAWRVIOuaDVE/640?wx_fmt=png&from=appmsg)

**第二步，在右下角提示框中选择合适的大模型，并输入详细的提示词。** 该提示词旨在读取数据集将特征转换为TF-IDF向量，并构建SVM机器学习算法进行分类，最终进行详细的入侵检测评估。

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe09ibCtD0dibOtT7oxfwyfLtSUoZ4Wunpa7QHroMJQtH125ia83rLouCsr5gqPEbsW1ib8hEonkgMLfQDBJerBCdNr1nHRLcLzgF8k/640?wx_fmt=png&from=appmsg)

```
请在IDS目录下创建Python代码，该代码需要：
（1）读取data目录下train_features.csv、test_features.csv、val_features.csv文件，提取[payload_id、attack_type、url_n_gram]。
（2）提取attack_type特征作为类别，url_n_gram作为特征。
（3）将特征转换为TF-IDF向量形式。
（4）构建SVM算法进行分类。
（5）输出test_features.csv的预测结果，使用评价指标进行评估，并且保留3位小数，绘制相关评价可视化图。
（6）输出预测结果和正确结果的类别CSV文件。
（7）请给出MD实验分析总结报告，详细描述实验结果，评价结果增加八个类别的平均结果。
```

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe1KcN40Px5uxtII2xWkgP9q7KyuMCI7W0wG3icHa11OVyVeHjIniaC5okiaKrXV6eFrM6JO6TgOf9CC3iahVaR9JNKkd2ibn9mmh7zU/640?wx_fmt=png&from=appmsg)

**第三步，CodeBuddy调用GLM-5.1大模型深度思考，并构建如下图所示的3个关键代码生成任务。**

* Create Python SVM classification script
* Run the script to generate results
* Generate MD experiment analysis report

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe0icvbSHLdia0QVOqDiaZiaYicfFwjlvIF0OKPcpzSEOBO5KNic1h0t9ibZU7O9gxfCdiaFpPnuRG8MianaxyxB4rTicQiceoMHiasiaI30iaMc4/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe2EK5AZ6pPiatX1RcmjhtXdhv3cL51ib8RoOaMOl8nraPdLSXKZ8NJU2dLSSVQQczw3e7XzaOrfrh2bJHXpc2Z7FrKH3GcBAhylA/640?wx_fmt=png&from=appmsg)

CodeBuddy会生成详细的SVM代码，如下所示，点击Keep可以接受生成的代码。

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe2bE2Mia83rnbibLkstRkzjkNPwY5KxOE0c41dyI0QIU4OEt2LAufCtYbJrFz70ickbzDcwmkzqsSFu13lmXodfVDEkgcSLFPGFks/640?wx_fmt=png&from=appmsg)

**第四步，CodeBuddy会自动运行代码并优化代码，下图展示了代码生成的结果。**

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe1GIn5Wwt9Ctj5icfDVamiaLWGOgSxb9Dh7rqVoSBzIXZXxdCwjCvjlbqibiaIc23KSzkiaSniaiaO2MJ7wxb6RoVE0FTNd2IY5G1icacY/640?wx_fmt=png&from=appmsg)

此外，生成MD文档详细总结了实验结果内容，方便大家进行更详细的入侵检测评估。

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe2XDQOU3chQMvLW3iatJ8XLO0ggcQHIy8PAhwExqz5CtfrUBPNW5hA0KI8JtibAqG8liaTbrCPMIE5RHZo9JgR4ibeuslJSWaajjUM/640?wx_fmt=png&from=appmsg)

SVM完整代码如下：

```
"""基于TF-IDF和SVM的Web攻击类型分类实验特征: url_n_gram类别: attack_type"""
import pandas as pdimport numpy as npimport matplotlibmatplotlib.use('Agg')import matplotlib.pyplot as pltimport seaborn as snsfrom sklearn.feature_extraction.text import TfidfVectorizerfrom sklearn.svm import SVCfrom sklearn.preprocessing import LabelEncoderfrom sklearn.metrics import (    accuracy_score, precision_score, recall_score, f1_score,    classification_report, confusion_matrix)import warningsimport osimport time
warnings.filterwarnings('ignore')
# 设置中文字体plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']plt.rcParams['axes.unicode_minus'] = False
# ============================================================# 1. 读取数据# ============================================================print("=" * 60)print("步骤1: 读取数据")print("=" * 60)
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
train_df = pd.read_csv(os.path.join(DATA_DIR, 'train_features.csv'))test_df = pd.read_csv(os.path.join(DATA_DIR, 'test_features.csv'))val_df = pd.read_csv(os.path.join(DATA_DIR, 'val_features.csv'))
print(f"训练集大小: {len(train_df)}")print(f"验证集大小: {len(val_df)}")print(f"测试集大小: {len(test_df)}")
# 提取指定列cols = ['payload_id', 'attack_type', 'url_n_gram']train_df = train_df...