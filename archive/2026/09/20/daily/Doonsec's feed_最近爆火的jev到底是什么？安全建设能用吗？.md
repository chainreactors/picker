---
title: 最近爆火的jev到底是什么？安全建设能用吗？
url: https://mp.weixin.qq.com/s/s8mGOzyWAptPBN7T5ZXfBw
source: Doonsec's feed
date: 2026-09-20
fetch_date: 2026-09-21T07:23:12.558107
---

# 最近爆火的jev到底是什么？安全建设能用吗？

# 最近爆火的jev到底是什么？安全建设能用吗？

原创

initsec
initsec

初始安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 最近爆火的 Jev 到底是什么

> 官方文档：https://docs.typesafe.ai/introduction

Jev 是 TypeSafe 推出的旗舰闭源模型，也是首款 System One 模型。给它一段应用状态和一组预先定义好的问题，它会返回可以直接交给代码使用的结构化决策结果。

我更愿意把它称为决策模型。DeepSeek、Kimi 等模型生成文本，Jev 不做聊天，也不输出自然语言句子。它只处理选择题、打分题和判断题，可在约 100 毫秒内给出结果，返回类型化选项、评分、概率和置信度。

简言之，Jev 是面向机器消费的决策 AI，而非供人类阅读的文本生成器。输入应用状态与预先定义好的问题，它直接返回类型化选项、评分、概率和置信度。因此非常适合作为智能体的内部控制层，负责路由、排序、重试、升级或停止等决策；只有当业务真正需要生成自然语言文本时，再去调用通用大语言模型。

![](https://mmbiz.qpic.cn/mmbiz_png/H74eHWFliciaX6a50ZPP0rZibH8liap9ciaF5PH3fx4po2QdqqicEHEoR6hxHBKGyvib3OssZ9icv57bBC2LzyP7E64piaib3r9m9hFAUdlKP7uxKDH9Y/640?wx_fmt=png&from=appmsg)

base

## 三种决策类型

Jev API 把决策拆成三种类型。这样做是为了收窄问题范围，让模型只负责判断，不负责组织回答。：

| 原语 | 问题形式 | 返回结果 | 举例问题 | 关键要点 |
| --- | --- | --- | --- | --- |
| **Choice（选择）** | 封闭式选择题，预先给定候选集合，最多支持 255 个选项 | 最优选项、全部选项的概率分布、置信度 | 这条安全告警属于哪一类？候选：[注入类、配置类、信息泄露类、other] | 支持增加 `other` 选项表达「以上都不符合」；适合分类、工单路由、资产标签 |
| **Score（评分）** | 有序量表打分，设置 2‑10 个等级，每个等级附带判定说明 | 分数，对应等级、各等级概率分布、置信度 | 评估该漏洞的风险等级：[信息、低、中、高、严重] | 用于连续性维度评估：风险等级、危害程度、满意度等；是有序分级，并非简单的 0~1 数值 |
| **Noul（布尔概率）** | 命题真伪判断题 | 单个 0 ～ 1 浮点数：**该命题为 “是” 的概率** | 这封邮件是否属于钓鱼邮件？ | 没有独立 confidence 字段，概率值本身就是置信度；适合条件分支、安全校验、是否人工介入 |

举个场景：处理单次客服工单时，可以一次同时发起多项判断：该工单分配给哪个团队（Choice）、客户不满程度（Score）、客户是否明确提出退款诉求（Noul）。业务代码仅需要通过普通`if`逻辑组合这些类型化结果即可。TypeSafe 官方将 Jev 比喻成**智能 if 语句**：当手写硬编码规则容易失效时，用来完成分类、路由、打分、信息提取、流程分支判断。

jev-api-decision-types-mindmap

![](https://mmbiz.qpic.cn/sz_mmbiz_png/H74eHWFliciaX0hBTYomHPlN8F6K1v5Oa8OturXVHt9VgrxjxrCmxcSw83FLRVCUlYlGoy2iaRHT6YzaXYia3FCcOSVPnbMlWB80Q3LeoX5tves/640?wx_fmt=png&from=appmsg)

## Jev 与 LLM 的核心区别

二者最核心区别在输出形态。传统大语言模型逐 Token 生成字符串，业务拿到文本后还需要自行解析、校验格式，还要面对幻觉、输出格式错乱的风险。而 Jev 需要预先定义全部合法答案集合，直接返回强类型结果，无需额外解析，从根源消除格式解析异常。

|  | Jev（System One） | 主流大语言模型 |
| --- | --- | --- |
| 输出内容 | 类型化决策结果 + 概率信息 | 生成自由文本字符串 |
| 采样方式 | 并行，一次性批量处理多个问题 | 串行，逐 Token 生成 |
| 响应延迟 | 70‑500 毫秒（官方公开数据） | 秒级 |
| 结构化输出错误 | 理论 0% | 存在出错概率 |
| 置信度 | 输出经过校准 | 普遍存在过度自信现象 |

两个突出特性：

1. **并行采样**：Jev 可以并行处理一次请求内的全部问题；哪怕同时提交 10 个问题，响应耗时几乎不会增加。
2. **校准置信度**：Jev 使用 TypeSafe 提出的\*\*RLCD（Reinforcement Learning for Calibrated Decisions，校准决策强化学习）\*\*训练，以真实业务结果作为优化目标，而非单纯拟合人类偏好。整体上置信度越高，预测准确率越高，这个特性对判断是否自动执行、是否转交人工非常关键。

Jev 和 LLM 一样具备自然语言理解能力，当前仅支持纯文本输入（字符串、JSON、文本数组），暂不支持图片、音频、视频多模态。

## Jev 的适用场景与局限

Jev 面向**答案集合已知、高频重复的决策场景**设计，适合工单分类、意图路由、内容审核、信息提取、指标打分，也可以作为其他大模型输出结果的安全护栏。 得益于多问题并行，且不会因为增加问题产生额外输出计费，可以采用 “扇出” 模式，一次性提交全部待判断问题，再交由业务代码筛选需要使用的结果。

**不适用场景：凡是需要生成内容的任务都不适合，例如对话聊天、代码生成、推理过程解释等。**

另外有两处重要局限：

1. **没有通用世界知识**。Jev 仅能读取你传入的上下文`state`，不会主动调用外部工具查询信息，这也决定了基于它搭建工作流的能力上限。
2. **置信度校准属于群体统计属性**。TypeSafe 明确说明，校准效果建立在大量预测样本之上，**不保证单次调用结果一定正确**，Jev 依然会出现判断错误。

## Jev 体验渠道

可以从官方排队申请

1、在官网 https://typesafe.ai/ 加入候补名单 waitlist，务必填写附加问卷，一般 24 小时内即可通过；新用户默认赠送 5U 额度。

2、Codex 对话安装方式（也可手动下载 skill 配置文件导入操作台）：

```
Install the TypeSafe skill. run `npx skills add typesafe-ai/skills --skill typesafe-ai`. You can read the skill directly at https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md (raw: https://raw.githubusercontent.com/typesafe-ai/skills/main/skills/typesafe-ai/SKILL.md). Then use the TypeSafe skill when working on this project.
```

3、回到操作台，建立 API Key。

4、在提示词开头说明 `use the TypeSafe skill` 即可

```
use the TypeSafe skill，api key 已设置到环境变量 TYPESAFE_API_KEY，ip: 1.2.3.4 访问了 https://www.gm7.org/.git/config，帮我判定是否为恶意攻击行为、对漏洞类型进行分类，同时对威胁进行打分。
```

![](https://mmbiz.qpic.cn/mmbiz_png/H74eHWFliciaWPqSALY2Kb8s5Y9fc1t38iaqZE5yibf0nN2v5r5iapN1e49vRNu68PL8MKYibjF3OXicNQUFbr8bjsvTGjCYRfP6kia9uLBicI3ibJhIo/640?wx_fmt=png&from=appmsg)

image-20260920085423935

---

除官方渠道外，有一些三方渠道也可以体验 jev，价格基本都在 $0.042 / 100 万输入 Token。

* https://openrouter.ai/~typesafe/jev-latest
* https://vercel.com/ai-gateway/models/jev
* https://developers.cloudflare.com/ai/models/typesafe/jev/
* https://www.netlify.com/changelog/typesafe-jev-ai-gateway/
* https://model.kyssta.lol/typesafe/jev-latest

## Jev 接口调用参数

```
POST /v1/systemone HTTP/1.1
Host: api.typesafe.ai
Authorization: Bearer ${TYPESAFE_API_KEY}
Content-Type: application/json
{
  "state": ${STATE},                       // string | object | array，所有问题共享的上下文
  "model": ${MODEL},                       // 例如 jev-latest

  "questions": {
    "${noul_question_id}": {
      "type": "noul",                      // yes/no 判断，返回 yes 概率
      "instructions": ${NOUL_INSTRUCTIONS},
      "criteria": {                         // 可选，定义 true/false 的边界
        "true": ${YES_MEANING},
        "false": ${NO_MEANING}
      }
    },

    "${choice_question_id}": {
      "type": "choice",                     // 从封闭集合中选一个
      "instructions": ${CHOICE_INSTRUCTIONS},
      "criteria": {                         // 必填：选项 -> 选项定义
        "${option_1}": ${OPTION_1_DEFINITION},
        "${option_2}": ${OPTION_2_DEFINITION},
        "${no_match_option}": ${NO_MATCH_DEFINITION}
      }
    },

    "${score_question_id}": {
      "type": "score",                      // 按有序等级评分
      "instructions": ${SCORE_INSTRUCTIONS},
      "criteria": [                         // 必填：2–10 个有序等级
        ${LEVEL_0},                          // 低
        ${LEVEL_1},                          // 中
        ${LEVEL_N}                           // 高
      ]
    }
  }
}
```

**响应框架**

```
{
  "model": ${RESOLVED_MODEL},
  "answers": {
    "${noul_question_id}": {
      "type": "noul",
      "noul": ${PROBABILITY_OF_YES}
    },
    "${choice_question_id}": {
      "type": "choice",
      "choice": ${BEST_OPTION},
      "probabilities": ${OPTION_DISTRIBUTION},
      "confidence": ${CONFIDENCE}
    },
    "${score_question_id}": {
      "type": "score",
      "score": ${WEIGHTED_LEVEL_INDEX},
      "legend": ${LEVEL_INDEX_TO_DESCRIPTION},
      "probabilities": ${LEVEL_DISTRIBUTION},
      "confidence": ${CONFIDENCE}
    }
  },
  "usage": {
    "input_tokens": ${INPUT_TOKENS},
    "output_tokens": ${OUTPUT_TOKENS}
  }
}
```

核心抽象就是三个部分：`state` 提供上下文，`questions` 定义一组独立的类型化判断，`answers` 按同样的 `question_id` 返回结构化结果。

## 安全领域典型应用场景

* 漏洞数据包智能分析
* 安全告警自动化研判
* IP 是否执行封禁的判定
* 资产风险评分
* 漏洞风险自动定级
* ...

把 Jev 接入 AI SOC 的研判流程后，可以把分类、定级和封禁判断交给它，减少大模型推理的 Token 消耗，也能缩短告警研判时间。

![](https://mmbiz.qpic.cn/mmbiz_png/H74eHWFliciaXlic4VHhKDce8ost7EoGjaCuenWghqxy1zZnjjEBmRoo1wrXcsVEK4le4icc0y7B9lxxLWCMgibr65avG7EdoaTALvZWLG18BYCg/640?wx_fmt=png&from=appmsg)

image-20260920141947631

```
{
    "state": "{\"event_id\":\"123\",\"src_ip\":\"14.146.259.4\",\"rule_id\":\"m_rule/aab3\",\"rule\":{\"rule_name\":\"sky\"},\"attack_type\":14,\"attack_type_str\":\"Info Leak\",\"timestamp\":\"1789265201\",\"site_uuid\":\"6\",\"website_name\":\"测试-https\",\"website\":\"https://www.gm7.org/_profiler/phpinfo.php\",\"action\":{\"value\":1,\"translation\":\"Deny\"},\"risk_level\":\"Medium\",\"count\":52}",
    "model": "jev-latest",
    "questions":
    {
        "vulnCategory":
        {
            "type": "choice",
            "instructions": "是对应的哪一种攻击类型？",
            "criteria":
            {
                "注入类": "攻击者通过可控输入，拼接恶意语句交由后端解析器执行，如SQL注入、命令注入、模板注入等",
                "配置类": "系统、中间件、云资源等运维部署配置不当引发风险，如默认密码、开启目录浏览、危险调试模式等",
                "信息泄露类": "系统对外非预期暴露敏感信息，如源码备份泄露、堆栈报错泄露、密钥与用户隐私泄露等",
                "权限越权类": "鉴权校验缺失，低权限用户访问或操作非自身/高权限资源，包含水平越权、垂直越权、未授权访问",
                "认证会话类": "身份认证、会话管理存在缺陷，如弱口令、验证码失效、会话固定、Cookie安全属性缺失",
                "跨站类": "前端输出过滤不足，包含XSS跨站脚本、CSRF跨站请求伪造",
                "代码执行类": "可直接执行用户可控代码或系统指令，含反序列化漏洞等",
                "业务逻辑类": "业务流程设计缺陷，通过篡改业务流程实现违规操作，如支付篡改、短信轰炸、风控绕过",
                "文件上传类": "上传校验不严，可上传恶意脚本文件并触发解析执行，如图片马、后缀绕过上传",
                "第三方组件类": "框架、中间件、依赖组件本身存在原生CVE漏洞"
            }
        },
        "threatScore":
        {
            "type": "score",
            "instructions": "判定该事件对应的威胁评分（CVSS 0~10分）",
            "criteria":
            [
                "0|无风险：属于正常访问、误报，不存在可利用安全隐患",
                "1|低危：仅少量非敏感信息暴露，利用条件苛刻，危害有限",
                "2|中危：可获取部分敏感信息，存在被进一步利用的可能性",
                "3|高危：可读取敏感数据或有限执行命令，存在较大业务与资产风险",
      ...