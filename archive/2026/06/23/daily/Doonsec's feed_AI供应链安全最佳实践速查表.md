---
title: AI供应链安全最佳实践速查表
url: https://mp.weixin.qq.com/s/UYYsGvtK20IbGMbLzIOEMw
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:02:15.178301
---

# AI供应链安全最佳实践速查表

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jcrjcnYMMMPoxsuZ608iase3RKxT7lueqoggH5EicmPeytiaI4XAIMVPAOutzqx3tPaXcgFhfxxgV6ladDMNpYZDcAj8U7jHtCEo7bsFOC7RTk/0?wx_fmt=jpeg)

# AI供应链安全最佳实践速查表

原创

无相AI
无相AI

青藤云安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

传统软件供应链安全侧重于保护源代码、依赖项、工具及流程等组件，防范供应链攻击。该安全模型以软件工厂为核心构建：开发人员主机、源代码管理系统、CI/CD流水线、构建基础设施、制品仓库和部署平台。这些部分共同组成可信链路，制品只要经过合规工具、运行器和工作流校验，就默认安全。但人工智能彻底改变了该格局。

#

***PART 0****1***

**AI带来的变化**

**AI系统不会取代传统软件工厂，但极大拓展了其边界。**工厂原有组件仍不可或缺，但不再是定义软件构建与运行的全部资产。因此，AI催生了大量全新供应链攻击路径。

本文汇总供应链安全基础知识，剖析软件供应链安全在AI时代的演变，并提供落地实操建议以防护业务系统。

***PART 02***

**什么是供应链攻击？**

供应链攻击指攻击者入侵上游可信组件，进而入侵下游目标的安全事件。美国CISA定义典型供应链攻击：被入侵的开源依赖包、投毒更新包、盗用密钥篡改代码签名。

传统供应链安全规范包括SAST静态扫描、SCA成分分析、加固CI/CD环境、精细化访问管控。

**但AI工作流新增核心产物与流程，衍生传统防护手段无法拦截的新型攻击：**训练数据集与嵌入向量投毒、植入后门/被篡改的模型权重、恶意提示模板、遭入侵的代理工具、不安全的模型序列化格式，以及依托AI集成开发环境、编排框架发起的入侵。

***PART 03***

**AI供应链攻击面**

**AI落地后，训练数据集、预训练/微调模型、提示词、嵌入向量、实验环境、推理流水线，与源代码等传统组件共同构成供应链。**

开发团队接入LangChain、LlamaIndex、CrewAI等LLM框架、各类AI工具与IDE插件后，供应链进一步延伸，新增代理编排器、提示模板、内存存储、运行时决策层。

**综上，AI供应链安全必须覆盖：**

1. 训练数据集与数据增强服务

2. 模型、权重、配置文件与模型仓库

3. IDE开发环境、笔记本文档、模型实验环境

4. 元数据与全链路推理业务

5. 公共模型平台与各类第三方AI组件

#

***PART 04***

**AI供应链常见威胁**

下面梳理AI供应链主要风险与攻击者利用方式

## **1. 训练与运行环境威胁**

**GPU驱动、Docker/containerd容器运行时、机器学习框架存在漏洞时，会催生新型供应链攻击。**攻击者拿到高权限账号或利用配置漏洞后，可窃取自研训练逻辑、占用硬件资源，例如私自占用大量CPU、GPU算力运行非法任务。

## **2. 开源AI库风险**

**AI新增分词器、嵌入工具、Agent开发SDK等全新依赖。**一旦软件包含漏洞或被植入恶意代码，会静默渗透训练、推理全链路，单个库缺陷就能造成多环境大范围信任失效。

## **3. 模型制品漏洞**

PyTorch.pt这类不安全序列化格式，调用`torch.load()`载入模型时可触发远程代码执行（RCE）。**攻击者篡改权重、配置、模型断点文件后，能暗中降低模型性能、诱导异常输出，且异常无明显特征。**

## **4. 第三方集成风险**

AI大多通过API对接外部服务商获取大模型、向量数据库、分词服务，每一处对接都是攻击面；第三方平台沦陷或鉴权薄弱时，企业提示词与内部业务数据极易泄露。

## **5. 代理框架工具链式滥用**

**在智能代理框架内，一条提示注入、脏输入即可触发恶意链路。**例：攻击者操控代理读取内部数据库、汇总数据并外传至指定接口；该行为看似合规，传统SAST/SCA无法识别风险。

## **6. 暴露接口风险**

即便后端防护严密，对外开放的模型接口仍会泄露密钥。攻击者借助侧信道攻击、模型反演提示，可窃取训练隐私数据、个人身份信息（PII）和核心商业数据。

***PART 05***

**AI威胁难以检测的原因**

AI新增海量组件大幅扩大攻击面，除此之外，安全盲区是另一难题。

**AI系统内部逻辑不透明、结构复杂，带来隐性风险：AI输出是概率化而非确定性结果，回复波动属于正常现象。这种天然可变性让恶意行为隐藏；攻击发生后，难以复现、溯源定位。**

以上因素大幅提升风险评估难度，受篡改的模型和AI流程极易向下游多租户、云平台扩散安全事故。

***PART 06***

**AI供应链安全十大最佳实践**

##

## **1. 梳理AI物料清单（AI-BOM）**

准则：无法溯源全生命周期的制品，禁止接入任意AI业务。

**AI-BOM登记系统内全部AI资产：**模型、数据集、流水线、接口、全量依赖（代理定义、模型元数据、训练数据集、实验笔记），搭建全生命周期可信链路。依托准入资产清单，阻止不可信工具动态加载运行。

## **2. 加固AI开发流水线**

核心：环境隔离 + 全链路可视

（1）将第三方模型权重视作不可信二进制文件，在低权限隔离沙箱加载，规避RCE漏洞；

（2）SCA扫描范围扩容，除AI依赖库外，纳入GPU驱动、机器学习专用容器运行环境；

（3）定期轮换密钥，落地强约束RBAC权限，避免单份凭证泄露就全盘失守。

## **3. 第三方风险管控**

接入前完成严格厂商安全尽调，梳理间接依赖，深挖嵌套SDK中潜藏的上游恶意组件。

**通过令牌配额、API调用频次上限、费用封顶规则，防范资源耗尽攻击与大模型滥用。**

## **4. AI落地零信任架构**

**对接第三方AI服务商不可默认信任。**基于最小权限、持续鉴权、全组件分级授权搭建零信任架构；将所有模型、服务商、向量库、智能代理全部视作潜在攻击入口。

## **5. 模型制品加密签名**

遵循OpenSSF开源安全基金会OMS模型签名规范，对模型权重、配置、分词组件、预处理资源整体签名固化。

CI/CD部署环节强制签名校验，哈希与签名不符直接拦截上线，仅可信流水线产出制品可投产。

## **6. 像源代码一样扫描代理工作流配置**

CrewAI的agents.yaml、tasks.yaml等配置文件定义代理行为逻辑，等同于可执行代码。

（1） 纳入代码扫描范围，排查权限超限、非法Shell调用、可被篡改的任务目标；

（2）通过代码化安全策略划定边界，约束代理在既定安全范围运行。

## **7. 加固RAG语义检索链路**

RAG是AI主流落地方案，加固检索层：

（1）原始知识库采用WORM（一次写入、多次读取）存储，防止文档被暗中篡改；

（2）检索内容送入大模型前，通过次级LLM或确定性过滤，拦截内嵌恶意指令与篡改内容。

## **8. 防护RAG配套内存存储**

向量库、持久化内存库是AI核心基建，脏数据会慢慢造成模型行为漂移。

（1）在向量库部署异常检测，标记异常数据集群；

（2）按数据来源做可信度打分，设置数据过期策略，按租户/代理隔离存储空间。

## **9. 持续全域风险可视化**

依托专业供应链工具实现：

（1）全量记录API请求，捕捉模型反演、数据窃取行为；

（2）统一视图梳理AI资产、账号、暴露面，追踪风险传播路径；

（3）自动化资产盘点，发现私自部署的影子AI；

（4）持续监控第三方对接链路，消除管控盲区。

## **10. AI红队安全测试**

AI红队测试不止验证模型幻觉，还要模拟黑客利用内部可信AI工具实施入侵，测试场景：

（1） 针对开发机、CI流水线、训练环境中的AI插件、智能助手、代理开展渗透测试；

（2）构造对抗提示，测试模型是否泄露密钥、环境变量、敏感数据；

（3）验证代理获取开发/流水线高权限后，访问内网工具、API、制品仓库的越权风险；

（4）测试供应链在遭遇篡改工具、投毒仓库、恶意模型后的故障表现。

#

***PART 07***

**总结**

#

综上，AI供应链安全是长期迭代工作，需要统一管控模型、数据、LLM开发工具、配置、代理框架与大模型服务商，青藤可提供对应安全能力支撑。

#

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jcrjcnYMMMMGjMmnicEUvqQciap5iauDdBGBAPWG2JbAN3nEmvsia3Ldgm7z6GASqJ4iaFotR3bFdSDWDPnh3yd84t280Eo5g10QkIibffF84Gc5U/640?wx_fmt=png&from=appmsg)

**往期回顾**

[未来安全在终端：AI和安全“双向原生”必争之地](https://mp.weixin.qq.com/s?__biz=MzAwNDE4Mzc1NA==&mid=2650851384&idx=1&sn=5eb2be02e792a45c384f108e63568572&scene=21#wechat_redirect)

[一张表看懂：AI for Security vs Security for AI](https://mp.weixin.qq.com/s?__biz=MzAwNDE4Mzc1NA==&mid=2650851338&idx=1&sn=e114a4cf804e7cba5dbbbd660b18fb22&scene=21#wechat_redirect)

[一张图：说清楚【AI对抗AI】落地实践](https://mp.weixin.qq.com/s?__biz=MzAwNDE4Mzc1NA==&mid=2650851276&idx=1&sn=2003983decb069236baf33f2a74139e9&scene=21#wechat_redirect)

[AI：攻击者的新“杠杆”](https://mp.weixin.qq.com/s?__biz=MzAwNDE4Mzc1NA==&mid=2650851351&idx=1&sn=35dfdd70b1df90c72c7e2bd8329fd243&scene=21#wechat_redirect)

[给CIO的Agentic AI落地路线图](https://mp.weixin.qq.com/s?__biz=MzAwNDE4Mzc1NA==&mid=2650851263&idx=1&sn=d3c83f7cde26d4762cc918dbafac2423&scene=21#wechat_redirect)

[终端是AI安全唯一的"战场"](https://mp.weixin.qq.com/s?__biz=MzAwNDE4Mzc1NA==&mid=2650851123&idx=1&sn=46e0b1069ed327c0fc98a40a7af5e921&scene=21#wechat_redirect)

在AI重构一切的2026年，供应链安全已不再是可选项，而是必选项。如果您觉得这篇文章帮您理清了思路，让你对AI for Security 或者是Security for AI有更深的见解，欢迎点击“关注”，我们将持续深挖AI安全盲区。

![](https://mmbiz.qpic.cn/mmbiz_png/jcrjcnYMMMOHNg2q7XSG07R8SGstOKWgn9OfxB84DxWia8YMgeSJCe0ZMAwp9RHVM12Jh1qPeAhkp7Jul2kY14J0J2icjwulDQmmXryoomibPI/640?wx_fmt=png&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jcrjcnYMMMNvTag1XXG7hDsuOnc2ibFZMNAzhRlIbhmfMicaHp4CrsM8JD3F3HA3ZxlefUlDZRuodHNk4pmQ6YI4B1SbgNicbvWBqpleCmHibus/640?wx_fmt=png&from=appmsg)

**点收藏**

![](https://mmbiz.qpic.cn/mmbiz_png/jcrjcnYMMMNkgFUpXvI7spJ1285E4kXM7gGEuNn4iatqjCPpjfADRERo8lmiaLkAkxs9ug6x4EzI7NVJjPfkRIco8rLAmrhuHUMTB38IXerjY/640?wx_fmt=png&from=appmsg)

**点在看**

![](https://mmbiz.qpic.cn/mmbiz_png/jcrjcnYMMMNTu1wuyeWfHzFq4MJgLbbicULLTS6AAaa3dDv9frubiaFp0H4ibv2008fria6I8rSJiabaumrrYq7Kj4OgGicwNvlxcCrET89n1djyk/640?wx_fmt=png&from=appmsg)

**点点赞**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7EpcyTBK4P1WPTQaAScoCKkianCbxMW6Ws340jzw69l94hzH56I696TJ4Z02pPVML9Tf2EVAvUGF99ll2PkO7rg/0?wx_fmt=png)

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