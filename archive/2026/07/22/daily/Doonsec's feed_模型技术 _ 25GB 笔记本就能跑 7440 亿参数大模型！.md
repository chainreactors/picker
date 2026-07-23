---
title: 模型技术 | 25GB 笔记本就能跑 7440 亿参数大模型！
url: https://mp.weixin.qq.com/s/WSAFdRWVbVP3fbXoTDuHtw
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:07:25.233335
---

# 模型技术 | 25GB 笔记本就能跑 7440 亿参数大模型！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KQ5kC5a54znYlLZvYJuuoTqfUE4MJkXdUA6LnTug4dqxEFvbcUJcjsKyj4BKbVO4GFJQ7OJFguCHiagP5L3WjiblFn0PRdExlly2iaVTiaIDJkM/0?wx_fmt=jpeg)

# 模型技术 | 25GB 笔记本就能跑 7440 亿参数大模型！

米斯特安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者荐语：

团队成员ZacharyZcR开发项目

以下文章来源于御之安
，作者御之安科技

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM73ymC94tcU0dibug9wSl4YkIia6ox0FS6ZanvF28JrxFQQ/0)

**御之安**
.

御之安科技扎根四川天府新区，秉持 “守护无声，保障万象” 理念，紧跟国家战略布局，聚焦AI+数据安全领域，自研四大核心产品、打造全栈安全产品矩阵，用硬核实力为政企客户构建全链路安全屏障，助力数字产业安全可信发展。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/G2uDgbh1kcQkFyptJuRBclflIDcoDgKCe7mA1xzd4pqxtPN45Nybl8hPb543HIgXzn929QDrqlwaqk0UHCVtmX1a42CrltOFLia57v3jia4dw/640?wx_fmt=gif&from=appmsg)

GLM-5.2拥有7440亿（744B）参数，原始权重文件体积高达756GB。单模型文件体量已远超绝大多数家用设备的存储总容量，传统部署方案必须依靠多台单价数十万的数据中心级GPU才能承载。而御之安科技自研技术colibrì打破了这一限制：仅一台12核CPU、25GB内存的普通笔记本，就能完整加载并运行该大模型，项目开源地址：https://github.com/JustVugg/colibri

整套方案的核心思路十分清晰：无需将完整模型全部载入内存，绝大多数权重常驻硬盘，仅在计算需要时实时读取加载。

![](https://mmbiz.qpic.cn/mmbiz_png/G2uDgbh1kcQU8FsY0oTFqVBKdIGCNgUcibGOkFOrInF7ZuAjcvm1oOv45ZibY9uCIlUVLalezWeocBkMhMic5RO5beGCcmgST5AuA0nhoggjeM/640?wx_fmt=png&from=appmsg)

## **MoE 混合专家架构：仅激活所需专家参与计算**

GLM-5.2采用MoE混合专家架构，可通俗理解为：模型内置近两万名专业专家，但每一次生成回答，只会调度匹配当前问题的8位专家参与运算，其余专家权重留存存储、待命待用。

核心参数明细：

* 模型共75层MoE结构，每层配备256个路由专家，叠加MTP预测头，全局总计19456个路由专家；
* 每生成1个token（可粗略理解为单个文字），每层仅激活8名专家参与计算。

![](https://mmbiz.qpic.cn/mmbiz_png/G2uDgbh1kcSAk4ibKUC9t6tCJapl9k82zP31GD7YHWIiaxP6U08jGOoT8Ewf5B9y3aDBVsf0mJ9n0Irqo91juQAtJlgmOfRq5uh6xs2g9QJ1U/640?wx_fmt=png&from=appmsg)

算力负载拆解：

* 单次token生成实际参与运算总参数约400亿（40B），仅占完整744B总参数的5.4%；
* 注意力模块、共享专家、词嵌入等全流程固定参与的稠密参数约170亿（17B）；
* 不同token间唯一发生变动的计算资源，仅为本轮激活的专家权重，数据体量约11GB。

![](https://mmbiz.qpic.cn/mmbiz_png/G2uDgbh1kcTbVQ4Cz5XUKhynnrrxerQhveLm0mINjwoAZtsJl0Pl0SAZHn7gE9s77GXE8vN8EzbWQicCyDcuJMHbPZjKmUcBYUFCnjz0hZVg/640?wx_fmt=png&from=appmsg)

## **colibrì三层****分级****存储****架构**

基于“任意时刻仅需少量权重参与计算”的特性，colibrì设计三层分级存储体系，分层存放模型权重，兼顾内存占用与读取效率：

|  |  |  |
| --- | --- | --- |
| **存储****层级** | **存储内容** | **数据体量** |
| 内存常驻层 | int4量化后的稠密固定参数 | 9.9GB |
| 硬盘按需加载层 | 全部19456个路由专家（int4量化，单专家约19MB） | 370GB |
| 可选显存加速层 | 高频调用热门专家常驻GPU显存 | 随硬件配置动态调整 |

系统搭配每层独立LRU缓存机制与热专家锁定策略，内存不足时仅会降低推理速度，不会修改模型量化精度、路由调度逻辑，保证输出效果不变。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G2uDgbh1kcTL9vMUlV8gvIPDicPpurkCeLmVC5eN6iaeP7zvicZRx7dkYYqRFjGg96xTHJhevSHy0h4EnzIAj6uRic4nxmiaRejDuoA5ia583Sc1c/640?wx_fmt=png&from=appmsg)

## **底层****引擎：****单****C文件****实现**

colibrì最初诞生于一台25GB内存、12核处理器的笔记本，整体采用极简开发路线：核心逻辑仅由c/glm.c单一主文件（约2400行代码）配合少量头文件构成，纯C语言开发，无第三方运行时依赖。

* 编译门槛低：仅需gcc+OpenMP即可完成编译；Python仅用于一次性模型格式转换，以及可选API网关部署；
* 全平台兼容：支持Linux、macOS（ARM NEON指令集）、Windows 11（MinGW编译，发布包附带免编译可执行程序）；
* 手写高性能SIMD计算内核：适配AVX2/AVX-512/VNNI/ARM NEON多套指令集，原生支持int4/int8/int2量化矩阵运算，兼容GLM-5.2原生DSA稀疏注意力机制；
* 输出正确性可验证：与Hugging Face Transformers官方参考实现逐token对齐校验，32组对比样本全部匹配无偏差。

## **工程****优化方案**

整套推理链路的核心瓶颈十分明确：冷启动生成单个token时，需从硬盘读取约11GB专家权重，磁盘I/O是全链路最慢环节。引擎围绕磁盘约束落地多重针对性优化：

1.**学习式缓存**

引擎自动记录每轮对话调用的专家信息并保存至.coli\_usage文件，程序重启后自动将高频使用专家锁定至空闲内存，对话复用次数越多，推理速度越快。

2.**路由前瞻预取（PILOT）**

利用第L层注意力输出提前推算第L+1层路由结果，可预先命中71.6%的真实top8专家；对比仅复用上一轮token专家的41.3%命中率提升显著。通过独立线程在当前层运算的同时，异步预读取下一层所需专家权重，消除磁盘等待阻塞。

3.**异步直写I/O**

已缓存专家直接参与计算，缺失专家由后台I/O线程池异步加载；开启DIRECT直读模式可绕过操作系统页缓存，NVMe固态环境下读取吞吐大幅提升。

* 安全说明：模型仅读取硬盘，无写入操作，对SSD寿命损耗极低；
* 潜在风险：内存分配过量触发系统swap分区写入，会加速SSD损耗；廉价固态长时间满速读取易出现散热降速。

4.MTP投机解码

模型提前预判后续多组token并快速计算，再完成结果校验，单次前向传播可同步产出2.2–2.8个token，推理速度提升且无损输出质量。

5.KV缓存压缩持久化

依托MLA注意力机制，将单token对话记忆从原始32768个浮点数压缩至576个，压缩比达57倍；缓存数据持久存储至.coli\_kv文件，关闭对话后重新打开可接续上下文，无需重复预处理填充。

## **多硬件****实测****性能****数据**

以下测试结果全部来自社区单机实测：

|  |  |  |
| --- | --- | --- |
| **机器** | **配置亮点** | **速度** |
| 25GB WSL2笔记本（项目起点） | 12 核，NVMe 虚拟盘 | 0.05–0.1 tok/s 冷启动 |
| Core Ultra 7 + 24GB WSL2 | --topp 0.7 调优后 | 0.07 → 0.11 tok/s |
| Ryzen 9950X + 123GB | 只换了SSD（1.5→8.8 GB/s） | 0.10 → 0.28 tok/s |
| Apple M5 Max + 128GB | ARM NEON，14.2 GB/s 盘速 | 1.06 tok/s |
| Ryzen AI Max+ 395（Strix Halo） | DIRECT + 学习钉存 47.6GB | 0.16 → 0.40 tok/s |
| Framework 13 笔记本 | int8 MTP 头 + 学习钉存 | 0.37 tok/s |
| 6×RTX 5090 + 192GB VRAM（作者主力机） | CUDA 后端，专家全常驻 | 6.8 tok/s 纯解码 |

![](https://mmbiz.qpic.cn/mmbiz_png/G2uDgbh1kcS9uNSLnE3fagJ2kfVHhHBeWmL3BBXs1YTTVGQIh4sUEzkpiaPzsFbSsDdEibxqgOBjg1rjnRu9kqzZYKz20xLPPRXoAbNeAf6yI/640?wx_fmt=png&from=appmsg)

实测总结三条规律：

* 硬盘带宽是第一约束：同一台机器只换SSD（1.5→8.8GB/s），速度0.10→0.28tok/s，耗时画像从"66%等硬盘"翻转为"57%做矩阵乘法"——瓶颈从I/O转移到计算。
* 小内存机器上，内存容量先卡住：24GB时每层只分到2个缓存槽，命中率3–4%，几乎次次要读盘。--topp 0.7（减少每层读取的专家数，有损，会打印警告）单开就提速1.6倍。
* GPU不一定有用：int4单行解码时，AVX2的int4核反而比f32慢（ARM NEON的SDOT则单token也受益）

瓶颈在哪取决于你的配置——硬盘饱和时加GPU同样白搭。建议先用coli plan看瓶颈

## **适用场景****与项目价值**

**1.适配场景**

* **单人使用、低并发需求：引擎原生为单请求流式解码设计，不支持高并发在线服务；**
* **本地模型研究、离线推理：无需采购昂贵数据中心GPU，普通 PC、笔记本均可部署；**
* **无GPU 设备可用：纯 CPU 推理是项目原生设计目标，GPU 仅作为可选加速模块。**

**2.项目局限性**

* **冷启动速度存在物理下限：硬盘读取速度决定最低0.05 token/s，仅能依靠缓存预热优化；**
* **量化精度完整测试待完善：内置coli bench基准测试框架，但受开发机磁盘性能限制，尚未完成全量精度校验。**

**3.项目内核价值**

colibrì 名称源自意大利语 “蜂鸟”—— 蜂鸟体型微小，依靠高频振翅实现空中悬停，恰好对应项目的技术取舍：仅依靠 25GB 内存、十余颗 CPU 核心，配合磁盘按需加载，即可驱动 7440 亿参数超大模型运行。

整套技术方案可概括为一句话：正视磁盘低速的物理硬件约束，通过学习缓存、路由预取、异步I/O 等优化手段，将磁盘等待移出推理关键路径。0.05 token/s 至 6.8 token/s 的速度差距，不存在底层原理区别，仅由专家缓存命中率、存储带宽差异决定。

对于想要在个人家用设备上开展大模型学习、验证、实验的开发者而言，该项目的核心意义不在于极致推理速度，而是将“家用设备完全无法运行 744B 超大模型” 变为 “可完整部署、可调试、可验证”，大幅降低超大参数模型本地研究的硬件门槛。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/G2uDgbh1kcQffGQeewv0OfQrpuV6thvQ32gpOuh2jqXsYobtSsAAtNW3DvZbBtT0f18yEc7icDxFV999ibkPpcxb4guq3ZjD51rYwSdFTOWib4/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/akMib3fibarLocC5XULzNaO2xO9mNc9QnicMjHvPfZfhKDOesE7D5DibcIPOSd9RlCdx9Sib7CawJjiads2vHWEichIsA/0?wx_fmt=png)

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