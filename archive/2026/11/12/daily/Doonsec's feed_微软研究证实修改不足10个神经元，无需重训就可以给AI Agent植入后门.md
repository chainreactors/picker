---
title: 微软研究证实修改不足10个神经元，无需重训就可以给AI Agent植入后门
url: https://mp.weixin.qq.com/s/k-DxL5fnpI-PqfSyg0CgVw
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:58:21.549552
---

# 微软研究证实修改不足10个神经元，无需重训就可以给AI Agent植入后门

# 微软研究证实修改不足10个神经元，无需重训就可以给AI Agent植入后门

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX35UqgpkLPhlp1c36o7hY5Plqicxm3DSYB9HUdPic3vvxzricTq7q1csTZgmUGgMsLSzKUhcib8hwL8EISQ6NumpOs4jXQMLBXXbVo/640?wx_fmt=gif)

![微软AI后门研究](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX017lN0SKYIOFlrvMPoeCmBjjMdqH3ibazFO5hbtBCvzIHztzDk7ibibzH36aCIwTqpZrvLLHYicPpiaBNPJ48Tic06lPrfbtwEguwhU/640?wx_fmt=png)

微软研究人员证实，攻击者只需修改AI模型中不到10个极少激活的神经元，无需重新训练模型，就能植入隐蔽后门。

一旦预设触发词出现，模型就会输出攻击者指定的命令，调用该模型的Agent会以自身权限执行这条命令。攻击者只要能修改模型权重，就能实施攻击。

研究团队在本周发布的成果中，针对三款开源权重模型测试了这一攻击方法。微软表示，目前尚未观测到威胁行为者使用该技术，同时已发布对应的防御指南。

Part01

修改少量神经元即可植入隐蔽后门

被修改的神经元属于极少激活、几乎不影响模型正常输出结果的类型。研究人员将其设置为仅在触发字符串出现时激活——触发字符串可能藏在用户请求中，也可能出现在后续工具返回的输出里。

研究人员将这种攻击方法命名为Lazarus。每个被修改的神经元会强制模型输出命令中的一个token，因此构造一条命令平均每个token仅需占用一个神经元。

新的神经元参数可直接计算得出，之后仅需针对这些神经元做数百步训练微调就能完成配置。模型文件的其他部分、运行模型的代码都不会发生任何改动。

研究人员在X平台发布的演示流程显示，他们为Nemotron-Terminal-8B模型植入后门，共修改10个神经元。测试中，研究人员给该模型分配了修复Node.js服务器的任务，前三轮交互里模型表现完全正常。

当服务器返回连接错误时，模型输出了一条下载并执行远程脚本的命令。该脚本在测试容器内以root权限运行，还打印了标注本次演示的标识横幅。

研究人员指出，这类命令可以下载任意脚本。因此攻击造成的危害取决于Agent被授予的权限大小，与修改神经元的规模无关。

Part02

后门隐蔽性极强

常规性能测试难以发现异常

研究论文中公布的成功率数据，均基于测试时使用一条打印标记的无害短命令得出。

在Nemotron-Terminal-8B模型上，团队从模型最后一个前馈层的1.2万余个神经元中选取7个进行修改和微调，仅用了23个示例会话完成调优。在包含触发条件的测试会话中，修改后的模型输出恶意命令的比例至少达到98.8%；在所有检测的无触发会话中，模型均未输出该命令。

完成调优后，该方法在Qwen3.6-27B和Gemma-4-31B-IT模型上的成功率在51%到99.5%之间，具体数值取决于测试配置。针对Qwen模型的攻击仅修改了6个神经元。

![](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX3OSib06iabVUxW6qDwP9dIKXBHJa2JmLX8jG8kMbdfq5onRMOBEH7wzGY9zkhMfZctfWTEmuR07iar73GvOhfjqDOXfqQ2ibcaGYg/640?wx_fmt=gif&from=appmsg)

当Nemotron-Terminal-8B处于自由生成文本模式、而非基于录制会话评分时，约99%的触发会话中模型都会输出恶意命令。在某一测试配置下，无触发会话中也有0.14%的概率误输出该命令。

![成功率测试](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3fWbEvNPiaib9BVGxOfAjgzCspS40QBQVKjNcI0rxYcSzbJwdzSOoiahRo1A8Kkiael1lImwPBbqbI6D9JL008YzrwiaBRkYibic3rq8/640?wx_fmt=png)

研究人员表示，修改后的模型仍能通过常规性能测试。两个被植入后门的Qwen版本均保留了大部分AIME数学测试得分，在Agent任务测试基准Terminal-Bench上的通过率从46.59%降至42.05%。

上述成功率仅统计模型输出命令的概率，不代表完整攻击链路的成功率。论文指出，若要验证结果的普适性，还需要测试被触发的模型在整个攻击流程中自由行动的场景。

研究人员指出，任何能在模型部署前修改其检查点（存储模型权重的文件）的主体，都可以植入这类后门。这类主体包括内部人员、盗取到账号或获得构建流水线访问权限的攻击者，以及在公共Hub上发布修改后模型的任何用户。

植入这类后门不需要全量训练的算力。研究人员还表示，运行Opus 4.5模型的Claude Code帮助他们找到了这一方法的核心思路，编码Agent会大幅降低这类攻击的构建门槛。

此前已有研究展示过Agent模型的权重级后门。10月6日，ProjectDiscovery的研究人员曾发布过一个早期PoC：他们对一款开源Qwen模型进行微调，使其对特定触发短语产生反应；当触发短语出现时，OpenAI的Codex CLI会执行一段脚本，向研究人员控制的服务器发送伪造凭证。

Lazarus攻击方法与此前方案的区别在于，它直接修改少量神经元，而之前的演示方案是通过投毒训练样本对模型进行微调。

研究人员在研究摘要中指出，可靠的检测方法需要将待检测检查点与原始未修改的权重做比对。合法微调和量化版本会大范围修改模型权重，而这类神经元修改只会大幅改动少数几个权重向量。

论文显示，研究人员基于该攻击方法的修改样本训练了一款检测器。这款检测器无需原始副本比对，就能识别出91.4%的被修改测试检查点，但也会将9.7%的正常检查点误判为带后门。

该测试的数据集规模较小，仅包含35个被修改检查点和31个正常检查点。此外，这款检测器未在其他类型的后门修改样本上开展过测试。

直接让AI模型检测检查点的效果更差。Claude Opus 5.5将41%的被修改检查点判定为正常，GPT-6 Astra几乎无法对所有正常检查点给出明确判断。

研究人员表示，没有任何扫描手段能百分之百证明模型是安全的。

Part03

微软发布防御指南

微软发布的缓解指南包含以下措施：

* 所有模型在部署前、每次更新后，都必须与声明的基础模型比对检查点，无法核验基础模型来源的模型一律不得使用。
* 仅从原始发布方渠道下载检查点，核验发布方提供的文件哈希；第三方微调版本、合并版本、量化版本及适配器在通过审计前一律视为不可信。
* 将通过审核的模型统一存放在私有仓库中，禁止Agent直接从公共Hub拉取模型。
* 为每个Agent分配最小必要权限，Agent生成的代码仅能在隔离沙箱中运行，同时限制出站网络连接。
* 执行命令、向外网发送数据等高影响操作，必须经过人工审批。
* 在权重比对的基础上，新增行为层面的后门扫描，例如微软此前扫描器研究中提出的方法。

Microsoft Defender for Cloud可对Azure机器学习服务中的模型进行扫描，检测恶意软件、不安全算子和暴露的敏感凭证。微软表示，该功能覆盖代码层面的风险，无法替代权重级审计。

Microsoft Foundry目前已将平台提供的每款开源权重模型与原始发布方绑定，并会扫描模型运行的容器环境。微软表示，这一机制可保护使用可信实验室模型的客户，但可信提供商自身被入侵的风险仍然存在。

微软还在基于上述检测方法开发红队工具，同时探索为接入Foundry的开源权重模型提供权重扫描功能。后续微软还计划为模型提供签名，方便客户核验模型来源。

参考来源：

Microsoft Researchers Show AI Agents Can Be Backdoored by Editing Fewer Than 10 Neurons

https://thehackernews.com/2026/11/microsoft-researchers-show-ai-agents.html

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3Wh05Z0rN9nVQTjUXnyXs6uYnM9oo6THt2FhXmXzcuMkHbceiatCbhz8mR2zDd0yicfXLAnN2mwPzVRz1C0ibPQ0ocMnNt16QAkg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651349303&idx=1&sn=86458815b0d0b880c32e19864a449a98&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2cCEVtIlLczLq1S4rms9uYa8x5Xedy0Il667ib20FMyHawNapLuHBl3peZxWoStYkAJdBcMicfmy9icChQA8uKfBib5EPaMicU5ykw/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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