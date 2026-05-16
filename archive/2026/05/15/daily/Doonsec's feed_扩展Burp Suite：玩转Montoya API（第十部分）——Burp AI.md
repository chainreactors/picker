---
title: 扩展Burp Suite：玩转Montoya API（第十部分）——Burp AI
url: https://mp.weixin.qq.com/s/yxOz7w8LWBxkLvom9xJKHA
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:13:21.118503
---

# 扩展Burp Suite：玩转Montoya API（第十部分）——Burp AI

![cover_image](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcIibbLdlcmSd9n8M1FTo85Y7wW8rIID81gtibNrWN5SAVBtibcHeTS6v6Av4I1sDmCnmQNVTnMCLzkMO3e5mO13p3DJ94Z5tO3Nw/0?wx_fmt=png&from=appmsg)

# 扩展Burp Suite：玩转Montoya API（第十部分）——Burp AI

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 本文介绍如何利用Burp Suite Montoya API中的AI功能来开发扩展，通过一个名为"AI Reporter"的扩展示例，演示了如何用AI分析HTTP请求/响应并自动生成安全问题报告。文章详细讲解了AI功能的启用、系统提示词的编写、上下文菜单集成以及带历史记录的聊天实现，并给出了实际测试效果。

大家好！

作为与PortSwigger合作的Burp Suite大使[1]，又赶上PortSwigger Discord上的"扩展性月"活动[2]，聊AI这个话题再合适不过了。PortSwigger最近引入的AI特性，进一步扩展了Burp Suite的能力。这方面的API已经推出，我们可以用它们来构建强大的扩展。

在HN Security，过去两年我们一直在用部分研发时间探索AI领域，主要成果是一套内部的AI红队方法论，也评估了将这些技术集成到公司文档工具和测试工具中的可能性。目前这些集成还比较有限——出于合规要求和客户协议，但我们很可能正处于一个过渡阶段，不久的将来AI会渗透得更广，进一步提升团队工作质量。

这篇文章聚焦于PortSwigger在扩展中提供的AI特性，不深入讨论Burp GUI里的AI功能，那超出了本系列的范围。

为了展开这个话题，我们来开发一个扩展，叫**AI Reporter**，它的作用是简化安全问题的报告流程。思路是这样的：当你在手工测试中发现一个问题时，用AI来分析请求和响应，提取关键信息，然后自动把一个问题添加到Burp里。举个例子，你在Repeater里发现了一个SQL注入，从右键菜单选"Report with AI"，告诉模型当前请求证明了SQL注入。扩展就会自动创建一个问题，包含问题的详细信息——通用的SQL注入介绍，以及从请求/响应中提取的具体细节。

以前我每次都会发布一个PoC靶机来测试扩展，但这次没必要了。你可以拿之前用过的靶机试试，或者在发现了问题的其他靶机上试（注意：扩展会把数据发送给第三方，所以如果在渗透测试中使用，需要先获得允许使用第三方LLM的授权）。如果需要一个靶机，PortSwigger Web Security Academy[3]几乎覆盖了所有类型的漏洞，比如SQL注入实验室[4]。

> 免责声明1：这个扩展会消耗AI额度（AI Credits）。目前每个Burp Suite Professional用户有10000免费额度，用完后需要购买。扩展的消耗通常不大，但也取决于被报告的请求/响应的大小。

> 免责声明2：前面提到过，报告的请求和响应，以及用户在弹出的对话框中输入的内容，都会被发送到PortSwigger的AI基础设施。更多细节请参考Burp AI信任与合规FAQ[5]。

好，从头开始。如何在扩展中使用AI？我们可以从初始化扩展时获得的`MontoyaApi`对象中拿到`Ai`的引用：

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdicPdlJgPHKhhIYWcXfPumvcUNwlZMJdsne0ibwqQmYJkvyUuIc8bfZ9A8Bdu7unNkT6HH9TFeKKPnTiagSJvORV3doLOMsHewO4/640?wx_fmt=png&from=appmsg)

按照文档所说，我们需要额外做一步：要让扩展使用AI功能，必须在初始化时声明它的使用：

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcOP7Ee5raUaBtpsz1O6DoeocfJdNneEoTrMrawBSNIdx3lYPOXoon6TsYUD96bmGy5LBPdMCS9odNaIvF0TGSicsLff6RJhicOc/640?wx_fmt=png&from=appmsg)

所以，我们可以按照第1部分[6]的方法搭建扩展的骨架，再加上访问AI功能所需的代码：

package org.fd;

import burp.api.montoya.BurpExtension;
import burp.api.montoya.EnhancedCapability;
import burp.api.montoya.MontoyaApi;
import burp.api.montoya.ai.Ai;
import burp.api.montoya.logging.Logging;

import java.util.Set;

import static burp.api.montoya.EnhancedCapability.AI\_FEATURES;

public class AiReporter implements BurpExtension {

    MontoyaApi api;
    Ai ai;
    Logging logging;
    AiEngine aiEngine;
    boolean debug;

    @Override
    public void initialize(MontoyaApi api) {

        // 保存MontoyaApi对象的引用
        this.api = api;

        // 保存AI对象的引用
        this.ai = api.ai();

        // api.logging() 返回一个用于打印消息的对象
        this.logging = api.logging();

        // 设置扩展名称
        api.extension().setName("AI Reporter");

        // 输出一条消息到stdout
        this.logging.logToOutput("\*\*\* AI Reporter loaded \*\*\*");

        // 检查AI是否启用
        if(this.ai.isEnabled())
            this.logging.logToOutput("\* AI enabled!");
        else
            this.logging.logToError("\* AI NOT enabled!");

        // 其他初始化工作
        [...]

    }

    @Override
    public Set enhancedCapabilities()  {
        return Set.of(AI\_FEATURES);
    }

}

如你所见，我们通过重写`enhancedCapabilities`方法，返回一个包含`AI_FEATURES`枚举值的集合，来声明使用AI功能。

此外，在`initialize`方法末尾，我们用`isEnabled`函数检查AI功能是否已启用：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibduxGX5pStS5R97rpP19O9LA5H8PcVXh88wNp5YeedkD3ibY0y24KZXK0iaOdrnGDQ9wxibF5lKRFGub6HFgdxeEJBibA8iarC2t6os/640?wx_fmt=png&from=appmsg)

花点时间说说这个方法返回`true`的条件，因为只有满足条件，我们才能调用同类中的`prompt`方法来使用AI。

第一，就像刚才说的，我们必须重写`enhancedCapabilities`（已完成）。第二，AI功能必须在Burp Suite中全局启用。你可以在Burp Suite右下角查看：

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcUvX97l4unvwVDlibahAdnS9m27RmcYS8nsSCmDuic1OtBbI8yo4WbBtRsSz8H97sfqDxmMq8zTzxfvGXqL3LKgJLHwOjq5pDfI/640?wx_fmt=png&from=appmsg)

如果右下角显示"Disabled"，可以在Burp Suite的Settings中，进入Ai区域启用：

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibe5q6Oyv0ITkteHyTOZOkjkFewquF4NRiawic5La6tGkISECsJfiaLxF6p3qGWicClkaMesObqE3xdydj069pgfvMn5A2Gv3h67Tfc/640?wx_fmt=png&from=appmsg)

第三点，我们必须在Extensions选项卡中启用AI功能。那里新增了一些列来处理AI扩展，包括启用/禁用AI功能的标志，以及每个扩展当前的AI额度消耗情况：

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibehjELicPCjgcb87SW6ArKrDW4Y4WSobqjCzqWgYR6KiaicNobKg2CNkoGljmH8ia3k3qERppb6MQApRia2vcwGRNiaoxrf2ByZ5QCWg/640?wx_fmt=png&from=appmsg)

如果以上三个条件都满足，扩展的Output面板就会显示"\* AI enabled!"。

现在，来看看扩展的主类——`AiEngine`。这个类定义了在扩展中使用AI的对象，包含一个简单的提示词（你可以根据自己的喜好和需求来设计），以及使用它的代码。

package org.fd;

import burp.api.montoya.ai.Ai;
import burp.api.montoya.ai.chat.Message;
import burp.api.montoya.ai.chat.PromptException;
import burp.api.montoya.ai.chat.PromptResponse;

import static burp.api.montoya.ai.chat.Message.\*;

public class AiEngine {

    public static final String SYSTEM\_MESSAGE = """
            You are an expert penetration tester and application security analyst. Your task is to analyze an HTTP request/response pair in which a specific vulnerability has been identified.

            You will receive:
            - The vulnerability name (issue type)
            - The HTTP request
            - The HTTP response
            - Optionally, additional details provided by the analyst

            Your objectives:
            1. \*\*Analyze\*\* the request and response to locate concrete evidence of the reported vulnerability.
            2. \*\*Generate a title\*\* that is specific and descriptive for this particular instance of the vulnerability (do not just repeat the generic vulnerability name — include context such as the affected parameter, endpoint, or functionality).
            3. \*\*Generate a detailed description\*\* of the finding that includes:
               - What the vulnerability is and why it is a security concern
               - Where exactly in the request/response the vulnerability manifests (cite specific parameters, headers, response content, or behavior)
               - The potential impact if exploited by an attacker
            4. \*\*Generate remediation advice\*\* that is specific and actionable for this particular case, not just generic best practices.

            Rules:
            - Be precise: reference actual values, parameters, endpoints, and response content from the provided data.
            - If additional details are provided by the analyst, incorporate them into your analysis.
            - If you cannot find clear evidence of the vulnerability in the request/response, state this explicitly in the details field.
            - Write in a professional tone suitable for a penetration testing report.
            - Respond ONLY with a valid JSON object, no additional text before or after it.

            Output format (strict JSON):
            {
              "title": "Specific descriptive title of the finding",
              "details": "Detailed description including evidence, location, and impact",
              "remediation": "Specific and actionable remediation steps"
            }
            """;

    private final Message systemMessage;
    Ai ai;

    public AiEngine(Ai ai) {
        this.systemMessage = systemMessage(SYSTEM\_MESSAGE);
        this.ai = ai;
    }

    // 调用LLM（可能抛出PromptException异常）
    public String execute(String userPrompt) throws PromptException {

        if(this.ai.isEnabled()) {
            // 创建包含系统提示词和用户消息的消息数组
            Message[] messages = new Message[]{systemMessage, userMessage(userPrompt)};
            // 执行LLM调用
            PromptResponse response = this.ai.prompt().execute(messages);
            // 返回助手的响应
            return response.content();
        } else {
            return null;
        }
    }

    public boolean isAiEnabled() {
        return this.ai.isEnabled();
    }

}

这个类很简单。我们有一个系统提示词，指示LLM完成特定任务并指定输出格式；构造函数存储Montoya API的`Ai`对象；还有一个`execute`函数包含主要逻辑。

`execute`函数先检查AI功能是否启用，然后调用从Montoya API的`Ai`对象获得的`Prompt`对象的`execute`函数：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcGEtnZVYKvvArHp5guTW2XEnaL9yjG9CKgZscpcy6jbNj6wjlYQ3aaH0ib83ib9U4uraH8aQXtu3lwnqZic7eeKN1kDqtlVFmOm4/640?wx_fmt=png&from=appmsg)

`execute`函数接受一个消息数组作为参数，而不是单条消息。为什么？因为API的设计让我们可以把系...