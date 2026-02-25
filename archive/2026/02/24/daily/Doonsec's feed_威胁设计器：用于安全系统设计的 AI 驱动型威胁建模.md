---
title: 威胁设计器：用于安全系统设计的 AI 驱动型威胁建模
url: https://mp.weixin.qq.com/s/NQGVvImhTdBwFyjwU17xSg
source: Doonsec's feed
date: 2026-02-24
fetch_date: 2026-02-25T04:13:00.278856
---

# 威胁设计器：用于安全系统设计的 AI 驱动型威胁建模

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/T0ibbhsCmribQ7bldn1rtgibmaetomcibbzrrraswFcM7cZy9R31Lt2xWOUZqSibNwrKGvBcic3LhWex5FuRBkcLnHbemDnNtZl6QiaDw6rec5K6JU/0?wx_fmt=jpeg)

# 威胁设计器：用于安全系统设计的 AI 驱动型威胁建模

原创

网络安全民工
网络安全民工

网络安全民工

![]()

在小说阅读器中沉浸阅读

# 威胁设计器：用于安全系统设计的 AI 驱动型威胁建模

**Threat Designer**是一款人工智能驱动的代理程序，可自动执行并简化安全系统设计中的威胁建模流程。它利用大型语言模型 (LLM) 的强大功能，分析系统架构，识别潜在的安全威胁，并生成详细的威胁模型，从而使开发人员和安全专业人员能够在开发的最初阶段就融入安全性。

---

## 快速链接

* 📖阅读 AWS 博客文章
* ⭐请给这个仓库加星标以支持该项目
* 📚入门指南

---

## 特征

* **架构分析**- 提交架构图并分析其威胁
* **交互式编辑**- 通过用户界面更新威胁建模结果
* **迭代改进**- 根据您的编辑和补充输入重新构建威胁模型
* **多种导出格式**- 可将结果导出为 PDF、DOCX 或 JSON 格式
* **AI助手（哨兵）** ——与内置助手交互，深入了解威胁模型
* **威胁目录**- 浏览和管理过往威胁模型

---

## 建筑学

### 解决方案架构

**使用的AWS服务：**

* AWS Amplify
* Amazon API Gateway
* 亚马逊 Cognito
* AWS Lambda
* Amazon Bedrock AgentCore 运行时
* Amazon DynamoDB
* 亚马逊 S3

### 代理逻辑流程

---

## 入门

### 先决条件

**所需工具：**

您的本地计算机上必须安装以下工具：

* Node.js（版本 18 或更高版本）和 npm
* 卷曲
* jq
* Python（3.12 或更高版本）和 pip
* Terraform CLI
* Docker运行
* AWS CLI已配置相应的凭证

**AI模型提供商：**

Threat Designer 支持两家 AI 提供商。请根据您的偏好选择其中一家：

#### 选项 1：亚马逊基岩版（默认）

您必须在 AWS 区域中启用对以下模型的访问权限：

* **Claude 4.6 Opus**
* **Claude 4.5 Sonnet**
* **Claude 4.5 Haiku**

要启用 Claude 模型，请按照此处的说明操作。请确保您已订阅这些模型，否则`AccessDeniedException`在使用应用程序时会收到异常。

> **注意：**如果部署在非美国地区，请验证您所在地区的推理配置文件 ID。请参阅“支持的区域和推理配置文件模型”。

#### 选项 2：OpenAI

你需要：

* 有效的 OpenAI API 密钥
* 可访问 GPT-5.2 或 GPT-5 Mini 模型

部署过程中，系统会提示您输入 API 密钥。

### 安装与部署

1. **克隆仓库**

```
git clone https://github.com/awslabs/threat-designer.gitcd threat-designer
```

2. **使部署脚本可执行：**

```
chmod +x deployment.sh
```

3. **导出 AWS 凭证**

```
# Option I: Export AWS temporary credentialsexport AWS_ACCESS_KEY_ID="your_temp_access_key"export AWS_SECRET_ACCESS_KEY="your_temp_secret_key"export AWS_SESSION_TOKEN="your_temp_session_token"export AWS_DEFAULT_REGION="your_region"# Option II: Export AWS Profileexport AWS_PROFILE="your_profile_name"
```

4. **运行部署：**

```
./deployment.sh
```

部署过程中，系统会提示您执行以下操作：

* 选择您的AI模型提供商（Amazon Bedrock或OpenAI）
* 请输入您的 OpenAI API 密钥（如果您使用 OpenAI）
* 请提供有效的电子邮件地址以用于用户凭据
* 选择是否启用哨兵AI助手

> **注意：**将在 Amazon Cognito 用户池中创建一个用户，并将临时凭证发送到配置的电子邮件地址。

### 访问应用程序

部署成功后，您可以在输出结果中找到登录 URL：

```
Application Login page: https://dev.xxxxxxxxxxxxxxxx.amplifyapp.com
```

---

## 配置选项

### 人工智能模型提供商选择

Threat Designer 支持两个可在部署期间选择的 AI 提供商：

```
Select AI model provider:
1) Amazon Bedrock (Claude) (default)
2) OpenAI (GPT-5.2)
```

#### Amazon Bedrock 配置（默认模型）

**Used Models：**

* **Claude 4.X 系列车型**

**主要特点：**

* **推理**：混合模型
* **推理等级**：无、低、中、高、最高（对应不同的推理代币预算或自适应努力程度）

> **注意：** Terraform 变量中列出的模型`adaptive_thinking_models`（例如 Claude Opus 4.6）使用基于工作量级别的自适应思维（例如`low`，` 1`、 `medium``2`、` `high`3`、`4` `max`），而不是基于令牌预算。对于这些模型，`reasoning_budget`配置将被忽略——用户界面中的推理级别将直接映射到工作量字符串。标准模型继续像以前一样使用基于令牌预算的推理。
>
> **注意：** Claude Opus 4.6 最大支持 128K 个代币的输出，而其他 Claude 4.x 系列型号最大支持 64K 个代币的输出。如果在不同型号之间切换，请务必`max_tokens`相应地更新配置，以避免 API 错误。

#### OpenAI 配置

**Used Models：**

* **GPT-5 Mini**（默认）——速度更快，成本效益更高
* **GPT-5.2** - 最高推理能力

**主要特点：**

* **理由**：始终启用（内置功能，无法禁用）
* **推理等级**：低、中、高（对应于 OpenAI 的推理难度）

**使用 OpenAI：**

1. `2`部署过程中，当系统提示选择模型提供商时，请选择相应的选项。
2. 出现提示时，请输入您的 OpenAI API 密钥。
3. 该系统将配置 Threat Designer 和 Sentry 以使用 OpenAI

#### 在不同服务提供商之间切换

在 Amazon Bedrock 和 OpenAI 之间切换：

1. 使用以下方式重新部署解决方案`./deployment.sh`
2. 出现提示时，请选择其他服务提供商。

> **重要提示：**无法在切换服务提供商后继续之前已建立的会话。您需要重新开始威胁建模会话。

### 网络搜索集成（可选功能）

Sentry 可以使用Tavily进行实时网络搜索，以查找 CVE、漏洞和安全主题。此功能为**可选**功能，需要 Tavily API 密钥。

#### 启用网络搜索

部署过程中，系统会提示您：

```
Enter your Tavily API key (optional, press Enter to skip):
(Enables web search and content extraction in Sentry assistant)
```

* **通过 API 密钥**：Sentry 可访问实时安全研究所需的`tavily_search`工具`tavily_extract`
* **如果没有 API 密钥**：Sentry 可以正常工作，但无法执行网络搜索。

#### 获取 Tavily API 密钥

1. 请访问tavily.com注册
2. 请前往您的控制面板获取您的 API 密钥
3. 密钥以`tvly-`前缀开头

#### 网络搜索功能

启用后，哨兵功能可以：

* 搜索 CVE 和漏洞信息
* 研究威胁情报和攻击技术
* 查阅技术安全文档
* 从安全公告和研究论文中提取内容

网络搜索专注于安全相关主题，不会搜索一般信息、人物或组织。

---

### 哨兵AI助手（可选功能）

Sentry 是一款人工智能助手，可通过对话式交互帮助您分析和探索威胁模型。此功能为**可选功能**，可在部署期间启用或禁用。

#### 部署期间启用/禁用哨兵系统

运行程序时`./deployment.sh`，系统会提示：

```
Enable Sentry AI Assistant? (y/n, default: y)
```

* **启用 (y)**：部署完整的 Sentry 基础架构，包括 Amazon Bedrock AgentCore Runtime、DynamoDB 会话表和 ECR 存储库。用户界面中将显示“助手”抽屉。
* **禁用 (n)**：跳过 Sentry 基础架构部署。助手抽屉将从用户界面中隐藏，核心威胁建模功能将继续正常运行。

#### 在现有部署中切换哨兵

**要禁用哨兵：**

1. 更新`.deployment.config`项目根目录中的文件：

```
ENABLE_SENTRY=false
```

2. 重新部署解决方案

**启用哨兵模式：**

1. 更新`.deployment.config`项目根目录中的文件：

```
ENABLE_SENTRY=true
```

2. 重新部署解决方案

---

## 清理

1. 按照此处的说明**清空架构桶。**
2. **使销毁脚本可执行：**

```
chmod +x destroy.sh
```

3. **导出 AWS 凭证**

```
# Option I: Export AWS temporary credentialsexport AWS_ACCESS_KEY_ID="your_temp_access_key"export AWS_SECRET_ACCESS_KEY="your_temp_secret_key"export AWS_SESSION_TOKEN="your_temp_session_token"export AWS_DEFAULT_REGION="your_region"# Option II: Export AWS Profileexport AWS_PROFILE="your_profile_name"
```

4. **执行脚本：**

```
./destroy.sh
```

本文探讨了生成式人工智能如何通过自动化漏洞识别、生成全面的攻击场景以及提供情境化的缓解策略，革新威胁建模实践。与以往难以应对威胁分析中创造性和情境化挑战的自动化方法不同，生成式人工智能凭借其理解复杂系统关系、推理新型攻击途径以及适应独特架构模式的能力，克服了这些局限。传统的自动化工具依赖于僵化的规则集和预定义的模板，而人工智能模型现在能够解读细致入微的系统设计，推断组件间的安全隐患，并生成人类分析师可能忽略的威胁场景，从而使高效的自动化威胁建模成为现实。

## 威胁建模及其重要性

威胁建模是一种结构化的方法，用于识别、量化和应对与应用程序或系统相关的安全风险。它从攻击者的角度分析系统架构，以发现潜在漏洞、确定其影响并实施相应的缓解措施。有效的威胁建模会检查数据流、信任边界和潜在攻击途径，从而制定针对特定系统的全面安全策略。

在安全左移策略中，威胁建模是一项至关重要的早期干预措施。通过在设计阶段（即编写任何一行代码之前）实施威胁建模，组织可以从源头上识别并解决潜在漏洞。下图展示了这一工作流程。

![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribRmy9eDo3F0mB0ZpqskicTqdXWjWx8u3TXC5OSiaLTwZHIaOGXXqcxKV1FkrqvZ9aXu8ME5FVibJbpaKV6075vJTbicYGmyd41xan8/640?wx_fmt=png&from=appmsg)

这种积极主动的策略能够显著减少安全债务的累积，并将安全从瓶颈转变为创新的推动力。从一开始就将安全考量融入其中，团队便可在整个开发生命周期中实施适当的控制措施，从而从一开始就构建出更具弹性的系统。

尽管威胁建模具有诸多显而易见的优势，但在软件开发行业中，其应用仍然不足。这种应用受限源于传统威胁建模方法固有的几个重大挑战：

* **时间****要求**——整个过程需要1-8天才能完成，并且需要多次迭代才能全面覆盖。这与现代软件开发环境中紧迫的开发周期相冲突。
* **评估****不一致**——威胁建模存在主观性问题。安全专家在威胁识别和风险等级评估方面往往存在差异，导致不同项目和团队之间评估结果不一致。
* **扩展性****限制**——手动威胁建模无法有效应对现代系统的复杂性。微服务、云部署和系统依赖关系的增长速度超过了安全团队识别漏洞的能力。

## 生成式人工智能如何提供帮助

生成式人工智能彻底革新了威胁建模，它自动化了以往需要人类判断、推理和专业知识才能完成的复杂分析任务。生成式人工智能为威胁建模带来了强大的功能，它将自然语言处理与视觉分析相结合，能够同时评估系统架构、图表和文档。这些模型借鉴了MITRE ATT&CK和OWASP等广泛的安全数据库，可以快速识别复杂系统中的潜在漏洞。这种能够同时处理文本和图像并参考全面安全框架的双重能力，使得威胁评估比传统的人工方法更快、更彻底。

我们的解决方案Threat Designer利用Amazon Bedrock中提供的企业级基础模型 (FM)来革新威胁建模。借助Anthropic 的 Claude Sonnet 3.7高级多模态功能，我们能够大规模地创建全面的威胁评估。您还可以使用模型目录中的其他可用模型，或使用您自己精心调校的模型，从而最大限度地灵活运用预训练的专业知识或根据您的安全领域和组织需求量身定制的功能。这种适应性确保您的威胁建模解决方案能够提供与您独特的安全态势相符的精准洞察。

## 解决方案概述

Threat Designer 是一款用户友好的 Web 应用程序，它使开发和安全团队能够轻松进行高级威胁建模。Threat Designer 使用大型语言模型 (LLM) 来简化威胁建模流程，并以最少的人工干预识别漏洞。

主要特点包括：

* **架构图分析**——用户可以提交系统架构图，应用程序将利用多模态人工智能功能处理这些架构图，以理解系统组件及其关系。
* **交互式威胁目录**——该系统生成一个全面的潜在威胁目录，用户可以通过直观的界面浏览、筛选和细化这些威胁。
* **迭代改进**——借助回放功能，团队可以重新运行威胁建模流程，并进行设计改进或修改，从而了解这些更改如何影响系统的安全态势。
* **标准化导出**——结果可以导出为 PDF 或 DOCX 格式，便于与现有安全文档和合规流程集成。
* **无服务器架构**——该解决方案运行在基于云的无服务器基础架构上，无需专用服务器，并可根据需求自动扩展。

下图展示了威胁设计器的架构。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribT1tAxfu6koiaqNzYykfTEiaTSGZKuLXI5tfSNicS4LB6Cv8xHo0sxIJcmfxfJES6x0oPndlCkiaZOpbduKUCibIg9LvDFpPIRKST3w/640?wx_fmt=png&from=appmsg)

该解决方案基于无服务器架构构建，利用 AWS 托管服务实现自动扩展、高可用性和成本效益。该解决方案由以下核心组件构成：

* **前端**– AWS Amplify托管了一个使用Cloudscape设计系统构建的 ReactJS 应用程序，提供用户界面。
* **身份验证**– Amazon Cognito管理用户池，处理身份验证流程并确保对应用程序资源的访问安全。
* **API 层**——Amazon API Gateway作为通信枢纽，提供前端和后端服务之间的代理集成，并负责请求路由和授权。
* **数据存储**——我们使用以下服务进行数据存储：

+ 代理执行状态表维护处理状态
+ 威胁目录表存储已识别的威胁和漏洞

+ 两个Amazon DynamoDB表：
+ Amazon Simple Storage Service (Amazon S3) 架构存储桶用于存储系统图和工件。

* **生成式人工智能**——Amazon Bedrock 提供 FM 功能，用于威胁建模、分析架构图和识别潜在漏洞
* **后端服务**– AWS Lambda函数包含 REST 接口业务逻辑，使用Powertools for AWS Lambda (Python)构建。
* **代理服务**– 该代理服务托管在 Lambda 函数上，异步运行，用于管理威胁分析工作流、处理图表以及维护 DynamoDB 中的执行状态。

## 代理服务工作流程

该代理服务基于 LangChain 的LangGraph构建，我们可以通过基于图的结构来编排复杂的工作流程。这种方法融合了两种关键的设计模式：

* **关注点分离**——威胁建模过程被分解为离散的、专门化的步骤，这些步骤可以独立且迭代地执行。图中的每个节点代表一个特定的功能，例如图像处理、资产识别、数据流分析或威胁枚举。
* **结构化输出**——工作流程中的每个组件都会生成标准化的、定义明确的输出，这些输出可作为后续步骤的输入，从而提供一致性并促进下游集成，以实现一致的表示。

代理工作流程遵循有向图，处理从开始节点开始，并经过几个专门的阶段，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmri...