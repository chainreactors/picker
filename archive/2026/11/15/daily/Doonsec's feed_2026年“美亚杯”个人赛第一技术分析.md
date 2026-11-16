---
title: 2026年“美亚杯”个人赛第一技术分析
url: https://mp.weixin.qq.com/s/AtAvGrMbECvjlCIyJTOtIw
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:45:09.372610
---

# 2026年“美亚杯”个人赛第一技术分析

# 2026年“美亚杯”个人赛第一技术分析

原创

石子铭
石子铭

星宇Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 大模型在电子数据取证中的本地部署

![](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQo7PXbwB9UyeIzibF28SBqjlw9fdPtp4FXGT2ibN2c2ZW0R7g5PDWSciab3yeic7fwXMMSndnsLUNset089z7oQeQSx8IjhMg2o2e0/640?wx_fmt=png&from=appmsg)

PPT完整内容在文末。

## 一、部署动机

取证作业的数据是检材，完整性、保密性和可追溯性都是硬约束。把涉案数据发往云端推理，数据处理的主体就超出了办案环境，这条链路在证据规则上很难解释清楚。可行的做法只有本地推理：模型、算力、数据都在同一台受控设备上。

本轮备赛因此把重点从刷题转向三件事：本地模型部署、微调可行性验证、硬件选型。

## 二、环境构成

| 层级 | 选型 | 承担的工作 |
| --- | --- | --- |
| 算力 | NVIDIA DGX Spark | 本地推理与微调实验 |
| 模型 | Qwen3.6-35B-A3B-FP8 | 代码阅读、文本理解、线索归纳 |
| 智能体 | 美亚Qiko 3.0 | 调用取证工具，接入分析流程 |

三者是依次约束的关系：硬件决定可运行的模型规模与上下文长度，模型决定单次分析的质量上限，智能体决定模型能否真正接触到检材和工具。

## 三、参数含义

模型名称中的三组字段经常被误读，需要分开理解。

**35B是总参数量。**约350亿参数，混合专家架构（MoE）。这一项决定权重大小和知识容量。

**A3B是每token的激活参数量。**约30亿参数参与前向计算，是MoE带来的计算收益，直接体现为解码延迟下降。

这里有一个选型时容易出错的地方：激活参数不等于存储需求。全部专家权重都要驻留内存，按FP8每参数1字节估算，权重部分在35GB量级，另需叠加KV cache、上下文和运行时开销。如果按30亿参数估硬件配置，部署阶段一定会失败。

**FP8指权重量化精度。**8位浮点使权重占用和访存带宽约降为FP16的一半。DGX Spark这类统一内存架构上，解码阶段受带宽限制，带宽下降直接换算成生成速度提升。

量化的精度损失不是零，实际精度和生成速度都需要在目标硬件上实测。取证场景读取的是配置项、变量名、时间字段这类低容错的字符串，量化噪声可能恰好落在关键token上，表现为个别字段读错而非整体质量下降。

## 四、实测结论

**便携性。**整机体积可随身携带，现场部署不需要机房条件。

**生成速度。**上下文压缩与token生成速度较快，等待时间不影响分析节奏。

**成本。**MoE加FP8在能力与部署成本之间取得折中，不必按满配硬件规划。

## 五、两个必须分开验证的环节

推理部署和微调是两条独立的技术路线。推理侧验证的是模型在给定硬件上能否稳定、及时输出；微调侧验证的是领域数据能否提升目标能力。前者跑通不代表后者可行，后者有效也不代表能部署。两者需要各自建立基线并记录指标。

模型输出必须人工核验。模型可以做快速定位、批量阅读和线索串联，但不承担结论责任。写入报告的内容需要能回溯到具体的源文件、记录或字节偏移。

## 六、Qiko 3.0的使用方式

最初的方案是自行组装：从GitHub获取取证MCP与Skills，配WorkBuddy、Codex搭建工作流。这条路可行，但搭建成本高，更换检材类型时还要重新适配。

Qiko 3.0把取证能力做成了集成层，内置多类MCP与Skills，可直接调用取证大师。省去的是环境搭建与工具串联的重复工作。

实际流程分三步：人工定位并导出源文件；把文件与题目交给模型，由模型读取代码、定位变量；人工回看调用链与配置覆盖关系，确认答案有源文件依据。

例如钓站后台账号那道题，人工定位到`/home/johnnymoney1/Desktop/TronicData/`后，模型负责在代码中找账号变量和认证逻辑，最终需要人工核对配置优先级和启动方式，才能确定实际生效的值。

模型在流程中的定位是读取与归纳，方向设定和结论核验由人完成。本地算力有限时，上下文长度、并发数和模型规模互相挤占，需要在具体任务上取舍。算力受限条件下，能稳定运行的中等规模模型比跑不动的更大模型更有实际价值。

## 七、小结

把大模型用进取证流程，需要同时满足三个条件：数据不出本地；输出可回溯到源文件；人的判断在流程内。参数选型解决第一条，工具集成提高效率，后两条依赖流程设计和取证基本功。

![](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQpibxl9c7rO0m44gNSxaGI2jFt2icdZudgGp6ESia3b64ria3rPOOgud1N00NTLSY2u20CLAluSPbMZYOTpytB9zcVCZppNs7hR0mM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQrrwTl7dgv574oIKiavnK5WLkyEJ9ELKYgyVkBSEudJ8ZvY1bRZhyXh1RX1WZmQvTfeLvbPR8CFQsw3sDvdvT9fnESH52zBMicibw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQrV8NrY3PjvFb4XKnuqmIhau5PMPbKrtW8l88OVCib7zdXP7oiaFzPeKxzpibUpoDErFMc2PpW8A9ia3DHyqpGO5xQ0j0jlanhHadw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQqO5UQad3UQrHDd33A4GYSP1gibqaib9OibSbk5G7jdichHr1EvT7tyxU46oVD0YSR757oEV5Gy3CibiatqcfzFjzsd334KQlzSLReibU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQrzz8YH6tvmVicr4AbUpK85h4RI5jq82Pvx7RdYWH7JnxEfxzSE2WO1qfvKoK8AhF6VNg14ulmib11QWUQreMdbOhupIwjmEyxac/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQoIrhkFhFXTZFe5N4dPxYIkuwnwBLgUmfY35icUoiaFVRzmZnw1icL0VmBsZQoKJkVKxA3MsoLVZVDpB8vsibVZascicww9hVRDwrj8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQribJWhMbpTon5Y2ibCKggicKwicmpe9nt2cRNjlUvjn37m3UiayVQVHtp3Y0ZCrhmcHSGlNUiazWzaFia94HhfmLfc0a9yAO6WGsVc3Y/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQrWUkBR6bIH8VZibm4Vr72KHGV8CEvVc9Vyt9ibjzjeCot4DF9TOKZ0vDGKZTsIfMdvPt6INia8FjiaEHxyFWDic2zPSKdt6pib5Geicc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQoEEwicgEMiasFbwMAxoCjuZ2qRUicRZbSegccGNBvG556gu5ADbQpsOGc0g1KoPknnav6qkSREHb0m2A6CeBEcicETJ1BIlzLrH4s/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQrR3kOYAuiayLZTFNo1y3x9pENtWkFJNc02uZcXVfNzvwHPLrLhXw5Opia7NDaTJr1whXC4eKWXhmicgaPbRibhWVSwG5A1riaAJWcY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQoibibyuxsM4Kg3hDz55vnew96uohsb63ABFGibb5NKyLP4UPWLXUCibjUDIVu73cRibR7ZzWQ38Mebgia5bx0hOaZcslSKQLaHMIVyA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQp3wsLwT8Jw9fV8QSHzZrN5nAyQu3hrtB6Z6Nrz9Ih0RCfFjicwQeUoQqnR1v3tibfJz0zUvMYXmwd3zxZUib6gUfmc1uQhdicNPOA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQoh5LYaxASJL5JuFib6vV4zA3yUqKfm69SicJicJQWHydVrkAamjt3c3xkTeHjKmw9HUeicuE9Rnm8jBG4eQAtQ10nlDj4pkBj5libc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQrzuTFcy7jeIiaZ75u44PMykyxZX31QzZhxhjxW5JYgV5n2jlJ2Os5W325KOYicVEKUVgvFJnuavX3C6Tz4Qz7cQtkkPf58zCjg8/640?wx_fmt=png&from=appmsg)

检材下载：

**下载链接1：**

https://pan.baidu.com/s/1oi0TXTBS5qeucPC\_pAda6w?pwd=tu25

提取码: tu25

**下载链接2：**

https://pan.baidu.com/s/1Q5nd4jKs3o6Sm-xmIihQrw?pwd=gh97

提取码: gh97

**下载链接3：**

https://pan.baidu.com/s/1xhIb3N3rc7-y7-OmhBoxYg?pwd=yeq

提取码: yeqv

**下载链接4：**

https://pan.baidu.com/s/11Q5XzZwsZfd4oThQKOhPdA?pwd=5945

提取码: 5945

**下载链接5：**

https://pan.baidu.com/s/1gJh1sSBW3b6JxzL6IiKXwQ?pwd=pico

提取码: pico

**SHA256**

**个人赛**

**Size (on windows)**：68GB

**SHA256 hash**：BD41B98BDB868D416FF136B75F1386BB6700B69F9C025E4EE76C430929272F65

**团体赛**

**Size (on windows)**：352GB

**SHA256 hash**：

9984A06FB8BC46B0A20AEF2AB507ABD73CC2F6DD954270BAB15575D9013C0047

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/O57ZTjAp9KOL0JJPSBRFM8Y3GwpOwWSpDSvWexu4uJ40TCnMzqRM9JQOxx8KibqwUWUXdicAXohNyARfdV9agCFw/0?wx_fmt=png)

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