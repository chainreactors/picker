---
title: AI大语言模型再陷入危机———新型网络攻击LLMjacking深度剖析
url: https://www.freebuf.com/articles/network/401037.html
source: FreeBuf网络安全行业门户
date: 2024-05-16
fetch_date: 2025-10-06T17:16:07.457603
---

# AI大语言模型再陷入危机———新型网络攻击LLMjacking深度剖析

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

AI大语言模型再陷入危机———新型网络攻击LLMjacking深度剖析

* ![]()
* 关注

* [基础安全](https://www.freebuf.com/articles/network)

AI大语言模型再陷入危机———新型网络攻击LLMjacking深度剖析

2024-05-15 16:17:56

本文由ALESSANDRO BRUCATO于2024年5月6日发表于sysdig的官方博客，并在文中详细阐述了Sysdit威胁研究团队（TRT）近期发现的一种针对云端大语言模型服务的新型威胁。

![](https://image.3001.net/images/20240515/1715760803_66446ea3870afedf27fe8.jpg!small)

## 概述

Sysdig威胁研究团队（TRT）近期发现了一种新型的攻击活动，这种攻击活动能够利用窃取到的云端服务凭证来对托管在云端的大语言模型（LLM）服务执行恶意操作，研究人员将该活动命名为LLMjacking。该活动中窃取到的凭证来自于一个知名的目标，该目标系统运行了一个存在安全漏洞（CVE-2021-3129）的Laravel版本。该活动主要针对的目标是基于LLM的人工智能系统，更准确来说，主要针对的是Prompt提示滥用和训练数据篡改。在这种场景下，威胁行为者可以将LLM的访问权出售给其他网络犯罪团伙，而消耗的资源则由云端账号的拥有者买单。

一旦获取到了初始访问权限，他们就会提取云端凭证并访问云环境，然后尝试访问托管在云服务商的本地LLM模型。在我们观察到的活动中，被违规访问的是Anthropic的本地Claude(v2/v3) LLM模型。如果没被发现的话，这种类型的攻击将有可能导致目标账户每天产生超过$46,000美元的LLM消费。

除此之外，Sysdig的研究人员还发现威胁行为者则会利用LLM的反向代理来提供针对目标服务账号的访问权，这种操作要么是为了经济目的，要么就是为了提取LLM训练数据。

![](https://image.3001.net/images/20240515/1715760817_66446eb1c197762959885.png!small)

该活动主要针对的AI服务包括：

> AI21 Labs
>
> Anthropic
>
> AWS Bedrock
>
> Azure
>
> ElevenLabs
>
> MakerSuite
>
> Mistral
>
> OpenAI
>
> OpenRouter
>
> GCP Vertex AI

## 背景内容

### 云端托管的LLM模型

很多主流的云服务提供商，包括Azure Machine Learning、GCP的Vertex AI和AWS Bedrock，现在都提供了大型语言模型（LLM）服务。这些平台允许广大开发人员方便地访问人工智能（基于LLM）中的各种热门的模型。如下图所示，用户界面的设计非常简洁，使得开发人员能够快速开始构建自己的应用程序：

![](https://image.3001.net/images/20240515/1715760845_66446ecd6f679950e84e6.png!small)

但是，云服务提供商默认并不会启用这些模型，而是需要向云服务提供商提交一个请求之后才能使用和运行它们。针对某些模型，服务商使用的是自动审批机制，但对于其他模型（例如第三方模型），则需要提交使用申请表格，云服务商审批通过后即可马上使用和访问模型。但是，这种请求机制对于威胁行为者来说只是一种“减速带”，而不是有效的防御机制，因此它也不能被视作是一种安全保护措施。

云服务商提供了简单的CLI命令来简化开发人员与云托管LLM模型之间的交互过程，一旦配置好相关的配置和权限，我们就可以使用下面这样的命令轻松地与模型交互：

```
aws bedrock-runtime invoke-model –model-id anthropic.claude-v2 –body ‘{“prompt”: “\n\nHuman: story of two dogs\n\nAssistant:”, “max_tokens_to_sample” : 300}’  –cli-binary-format raw-in-base64-out  invoke-model-output.txt
```

### LLM反向代理

负责检查凭证是否能够使用目标LLM模型的核心检测代码还引用了另一个项目，即OAI Reverse Proxy。这个开源项目可以充当LLM服务的反向代理，这种工具将允许威胁行为者集中管理多个LLM账号的访问连接，同时不会暴露底层凭证，也就是威胁行为者窃取到的那些泄露凭证。在使用泄露凭证执行恶意操作的过程中，可以查看到与OAI反向代理匹配的用户代理试图使用LLM模型的行为：

![](https://image.3001.net/images/20240515/1715760863_66446edf63f6001828907.png!small)

上图显示的是研究人员在互联网上发现的OAI反向代理的一个例子。虽然没有直接证据表明该实例与此次攻击活动有任何关联，但它确实显示了它所收集和显示的信息类型。

下面的例子中显示了一个OAI反向代理实例，它被设置成可以使用多个类型的LLM模型，不过我们也没有发现该实例与此次恶意活动有关。

![](https://image.3001.net/images/20240515/1715760871_66446ee74babb818c7896.png!small)

如果威胁行为者收集到了大量有效的凭证，并想将可用LLM模型的访问权出售的话，反向代理会是一个很好的选择：

![](https://image.3001.net/images/20240515/1715760890_66446efa633f677f056b6.png!small)

## 技术分析

在技术分析部分，我们将讨论威胁行为者在入侵目标云环境时所采用的技术方法和细节。通过在云环境中使用看似合法的API请求，他们巧妙地测试了访问的边界，而不会立即触发警报。在接下来的示例中，演示了CloudTrail记录下的威胁行为者针对InvokeModel API调用策略。在示例中，威胁行为者发送了一个有效的请求，并故意将max\_tokens\_to\_sample参数设置为-1。这个很少使用的参数通常被认为会触发错误，但它却另有用途。它不仅证实了威胁行为者对LLM的访问真实存在，而且证实了这些服务是活动的，正如由此产生的ValidationException所表明的那样。如果出现不同的结果，例如AccessDenied错误，则会建议限制访问。这些细节信息也足以表明威胁行为者使用的是经过精心设计的方法，并揭示了泄露凭证能够在云账号内允许的操作行为。

### InvokeModel

CloudTrail记录下的InvokeModel API调用以及恶意事件样例如下代码所示：

```
{

    "eventVersion": "1.09",

    "userIdentity": {

        "type": "IAMUser",

        "principalId": "[REDACTED]",

        "arn": "[REDACTED]",

        "accountId": "[REDACTED]",

        "accessKeyId": "[REDACTED]",

        "userName": "[REDACTED]"

    },

    "eventTime": "[REDACTED]",

    "eventSource": "bedrock.amazonaws.com",

    "eventName": "InvokeModel",

    "awsRegion": "us-east-1",

    "sourceIPAddress": "83.7.139.184",

    "userAgent": "Boto3/1.29.7 md/Botocore#1.32.7 ua/2.0 os/windows#10 md/arch#amd64 lang/python#3.12.1 md/pyimpl#CPython cfg/retry-mode#legacy Botocore/1.32.7",

    "errorCode": "ValidationException",

    "errorMessage": "max_tokens_to_sample: range: 1..1,000,000",

    "requestParameters": {

        "modelId": "anthropic.claude-v2"

    },

    "responseElements": null,

    "requestID": "d4dced7e-25c8-4e8e-a893-38c61e888d91",

    "eventID": "419e15ca-2097-4190-a233-678415ed9a4f",

    "readOnly": true,

    "eventType": "AwsApiCall",

    "managementEvent": true,

    "recipientAccountId": "[REDACTED]",

    "eventCategory": "Management",

    "tlsDetails": {

        "tlsVersion": "TLSv1.3",

        "cipherSuite": "TLS_AES_128_GCM_SHA256",

        "clientProvidedHostHeader": "bedrock-runtime.us-east-1.amazonaws.com"

    }

}
```

他们发送了一个合法请求，但将max\_tokens\_to\_sample参数设置为了-1。这是一个无效错误，并会触发ValidationException错误，但对于威胁行为者来说，这是一个非常有价值的信息，因为它可以告诉威胁行为者目标凭证能够访问LLM，并启用了对应的服务。否则，他们会收到一个AccessDenied错误。

需要注意的是，AWS Bedrock并不是所有地区都支持，因此威胁行为者只会在支持的地区调用InvokeModel。现在，Bedrock仅支持下列地区：us-east-1、us-west-2、ap-southeast-1、ap-northeast-1、eu-central-1、eu-west-3和us-gov-west-1。除此之外，不同地区所支持的模型也不一样。

### GetModelInvocationLoggingConfiguration

有趣的是，威胁行为者还对服务的配置方式感兴趣。这部分数据可以通过调用GetModelInvocationLoggingConfiguration来获取，该API会返回S3和Cloudwatch日志配置。在我们配置的环境中，我们会使用S3和Cloudwatch收集尽可能多的攻击数据。配置信息如下所示：

```
{

    "loggingConfig": {

        "cloudWatchConfig": {

            "logGroupName": "[REDACTED]",

            "roleArn": "[REDACTED]",

            "largeDataDeliveryS3Config": {

                "bucketName": "[REDACTED]",

                "keyPrefix": "[REDACTED]"

            }

        },

        "s3Config": {

            "bucketName": "[REDACTED]",

            "keyPrefix": ""

        },

        "textDataDeliveryEnabled": true,

        "imageDataDeliveryEnabled": true,

        "embeddingDataDeliveryEnabled": true

    }

}
```

有关正在运行的Prompt及其结果的信息不会存储在Cloudtrail中，需要进行额外的配置才能将该信息发送到Cloudwatch和S3。进行此检查是为了隐藏他们活动的细节，使其不受任何安全审查的影响。OAI反向代理则出于隐私方面的考虑，不会使用任何启用了日志记录的AWS密钥。如果他们使用了AWS Bedrock，就无法去检查Prompt和响应了。

## 影响

在一次LLMjacking攻击活动中，会给目标账户带来大量的财务损失，因为LLM的使用并不便宜。考虑到最坏的情况，即威胁行为者滥用Anthropic Claude 2.x并在多个地区达到配额限制，目标账号每天的成本可能超过$46,000美元。

根据Claude 2的定价和初始配额限制：

> 1、1000个输入token价格为$0.008，1000个输出token价格为$0.024
>
> 2、根据AWS Bedrock的数据，每分钟最多可以处理500,000个输入和输出token，平均下来的话，1000个token的平均成本为$0.016；

计算下来，每天的总成本如下：

> (500K token/1000 \* $0.016) \* 60 分钟 \* 24 小时 \* 4 区域 = $46,080 / 天

通过最大限度地提高配额限制，威胁行为者甚至还可以阻止目标组织合法使用模型，从而中断业务运营。

## 检测

快速检测潜在威胁在保证服务安全方面至关重要，根据行业内的最佳实践，我们提供了下列针对此类威胁行为的关键策略：

> 1、云日志检测：Falco、Sysdig Secure和CloudWatch Alerts等工具都可以实现该功能，组织可以通过监控运行时活动和分析云日志，包括AWS Bedrock中使用的侦察策略，主动识别可疑行为；
>
> 2、详细数据记录：包括详细日志记录在内的全面日志记录可以为我们云环境的内部工作提供宝贵的数据，有关模型调用和其他关键活动的详细信息允许组织对其云环境中的活动有细致的了解；

下面给出的是一个可用的Falco检测规则：

```
- rule: Bedrock Model Recon Activity

  desc: Detect reconaissance attempts to check if Amazon Bedrock is enabled, based on the error code. Attackers can leverage this to discover the status of Bedrock, and then abuse it if enabled.

    condition: jevt.value[/eventSource]="bedrock.amazonaws.com" and jevt.value[/eventName]="InvokeModel" and jevt.value[/errorCode]="ValidationException"

    output: A reconaissance attempt on Amazon Bedrock has been made (requesting user=%aws.user, requesting IP=%aws.sourceIP, AWS region=%aws.region, arn=%jevt.value[/userIdentity/arn], userAgent=%jevt.value[/userAgent], modelId=%jevt.value[/requestParameters/modelId])

    priority: WARNING
```

下面给出的是包含了关于token处理在内的日志信息：

```
{

    "schemaType": "ModelInvocationLog",

    "schemaVersion": "1.0",

    "timestamp": "[REDACTED]",

    "accountId": "[REDACTED]",

    "identity": {

        "arn": "[REDACTED]"

    },

    "region...