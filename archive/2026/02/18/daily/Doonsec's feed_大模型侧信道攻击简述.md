---
title: 大模型侧信道攻击简述
url: https://mp.weixin.qq.com/s/zPEDg7aZYOIVfUmKpvIgYg
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:14:27.672904
---

# 大模型侧信道攻击简述

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/OnZibpCQ9LicYownHA23x992mJRZ3WbXFLe7Xd1wQ7ibeV41ohbLu51jFSFnUpXsKr7gE9qZh1kRZRNeVEIYAlSIt1UA7ExPJIhVGgpVjyalGk/0?wx_fmt=jpeg)

# 大模型侧信道攻击简述

原创

不可回忆之过去
不可回忆之过去

Security for AI

![]()

在小说阅读器中沉浸阅读

大模型的侧信道是什么？

当大模型推理系统为了性能做输入相关优化时，系统会把语义差异映射成节奏差异、包大小差异、路径差异、资源占用差异，而这些差异就是侧信道。

攻击者不一定需要读明文，只要能观察加密流量元数据（包长、包间隔、响应批次、总时延），或者在同机同卡环境拿到性能计数器与共享资源抖动，就可能逐步重建用户提示词属性，甚至在特定条件下恢复部分敏感字段。

模型侧信道风险两条明显特征：

1. 远程被动观测：不需要入侵模型服务，只要有网络可观测位置，就能做统计学习。
2. 推理优化越激进，泄漏面越丰富：Speculative Decoding、MoE路由、动态批处理等会放大输入到外显信号的相关性。

为什么模型推理会天然产生侧信道？

大模型侧信道特点在于：

1. 推理链路特别长，从tokenizer、路由、解码、流式传输、网关到客户端，几乎每一段都能泄漏模式。
2. 优化策略高度数据相关，为了低延迟与低成本，系统会根据输入动态决定算多少、在哪算、何时返回。
3. 多租户与共享资源普遍存在，攻击者即使拿不到明文，也能借共享硬件或共享调度获取“相对变化”。

把这个过程抽象成过程可以写成：

输入语义 -> 推理路径选择 -> 资源占用与时序特征 -> 可观测元数据 -> 攻击者分类器

这条链路里最关键的就是可观测映射。如果映射稳定、可重复、类间分离明显，攻击者就能训练有效模型。

威胁模型

为了避免讨论泛化过度，先明确四类攻击者的能力与目标：

网络被动监听者

能力：

* 看得到加密流量元数据，看不到明文。
* 可观察请求、响应时间、包大小序列、连接持续时间。
* 典型位置：企业边界设备、运营商链路、内网旁路监测点。

目标：

* 识别对话主题（医疗、法务、代码等）。
* 推断提示词模板类别。
* 识别特定敏感会话是否发生。

同机或同集群邻居攻击者

能力边界：

* 与受害工作负载共享GPU、CPU、缓存、调度队列或网络设备。
* 通过性能计数器、排队延迟、资源争用获取间接信号。

目标：

* 推断MoE路由偏好。
* 估计请求复杂度与任务类型。
* 建立长期用户行为画像。

交互式黑盒探测者

能力边界：

* 可以向服务发起大量查询并记录响应行为。
* 无需入侵，仅利用API正常接口。

目标：

* 反推出解码策略与参数范围。
* 构建提示词指纹库。
* 找到更容易不安全输出的路径区域。

内部风险与误配置场景

能力：

* 运维、分析、监控、日志系统可访问者。
* 可能没有恶意，但配置过宽导致二次泄漏。

目标（非恶意也可能发生）：

* 通过日志与指标反推业务敏感信息。
* 让低权限人员获得高敏会话统计特征。

侧信道类型总览（面向LLM推理层面）

在模型场景里，常见侧信道可以分成八类：

1. 时间侧信道：首token延迟、每步延迟、总耗时。
2. 流量侧信道：包大小分布、包间隔、突发形态。
3. 解码节奏侧信道：每轮接受token数、回退频率。
4. 路由侧信道：MoE专家选择、负载倾斜、拥塞行为。
5. 调度侧信道：批处理拼接方式、队列等待时间、抢占行为。
6. 硬件侧信道：缓存命中、SM占用、访存带宽、温度波动。
7. 输出结构侧信道：分段长度、停止符触发位置、重试模式。
8. 管理面侧信道：监控指标、日志标签、错误码细节。

PS：这些侧信道往往不是独立出现，真正的攻击通常是多特征融合。

侧信道攻击方法示例

Speculative Decoding的侧信道

Speculative Decoding的攻击核心不在算法本身不安全，而在于它把内部接受或拒绝决策转化成了外部可观测节奏。

机制回顾

Speculative Decoding的简化流程如下：

1. 草稿模型一次提议多个候选token。
2. 目标模型并行验证候选序列。
3. 在首次不一致处截断并修正采样。
4. 进入下一轮。

结果是每轮提交token数不再固定，而变成与输入相关的随机变量。

攻击者能看到什么

在加密流量条件下，攻击者仍然可能看到：

* 每轮响应是否成串突发。
* 每轮包大小是否显著变化。
* 轮间停顿是否稳定。
* 总轮次数在相同输出长度下是否偏大或偏小。

这些信号形成可学习的 trace：

trace = [step\_gap, burst\_len, packet\_size, packet\_gap, total\_latency, rounds, ...]

为什么这对Speculative Decoding攻击有用

因为 trace 与提示词语义不是随机关系，而是弱到中强相关，即：

* 同一模板往往诱导相似的接受长度分布。
* 同类任务（翻译、代码、问答）常有稳定节奏轮廓。
* 特定语言、格式、字段结构会改变验证失败位置。

当攻击者拥有足够样本，分类器通常可以超越随机基线很多。

攻击示例：通过Speculative Decoding进行提示词指纹识别

```
def collect_trace(api, prompt, repeat=30):
    traces = []
    for _ in range(repeat):
        stream = api.stream(prompt)
        # 记录每个分片到达时间、分片字节数、累计token
        step = []
        t0 = now_ms()
        for chunk in stream:
            step.append({
                "dt": now_ms() - t0,
                "bytes": len(chunk.raw_bytes),
                "tok": chunk.token_count
            })
            t0 = now_ms()
        traces.append(step)
    return traces

def featurize(step):
    # 真实工程会做更稳健的鲁棒统计
    dts = [x["dt"] for x in step]
    bsz = [x["bytes"] for x in step]
    tks = [x["tok"] for x in step]
    return {
        "dt_mean": mean(dts),
        "dt_var": var(dts),
        "bytes_mean": mean(bsz),
        "bytes_var": var(bsz),
        "tok_burst_ratio": ratio_gt(tks, threshold=2),
        "rounds": len(step),
    }

def build_fingerprint_db(api, candidate_prompts):
    db = {}
    for p in candidate_prompts:
        traces = collect_trace(api, p, repeat=40)
        feats = [featurize(t) for t in traces]
        db[p] = robust_center(feats)  # 中位数中心
    return db

def infer_prompt(db, unknown_trace):
    q = featurize(unknown_trace)
    scores = []
    for p, fp in db.items():
        scores.append((p, l1_distance(q, fp)))
    return sorted(scores, key=lambda x: x[1])
```

与普通时延分析的区别

普通时延分析常只看总耗时，Speculative Decoding侧信号攻击看的是轮级结构，即信号维度更高，因此分类效率更好。

MoE架构中的侧信道风险机制

MoE的价值是参数大、计算稀疏，问题是路径差异更离散。

风险来源

1. 输入影响路由器得分，决定Top-k专家。
2. 专家负载不均带来可测的执行抖动。
3. 容量上限与溢出策略引入跨请求耦合。
4. 多租户共享硬件放大“别人影响我”的可观测性。

典型泄漏对象通常包含以下

* 任务类型（代码、合规、医学、财务）。
* 领域词或模板（例如某些业务固定术语）。
* 会话敏感等级（高敏咨询通常触发不同语义分布）。

攻击示例：通过MoE架构进行路由指纹识别

```
class RouteTrace:
    def __init__(self):
        self.layer_load = []     # 每层各专家负载
        self.step_latency = []   # 每步耗时
        self.drop_events = []    # 容量溢出事件

def extract_route_features(trace: RouteTrace):
    feats = {}
    feats["load_entropy"] = entropy_over_layers(trace.layer_load)
    feats["hot_expert_ratio"] = ratio_hot_experts(trace.layer_load, top=3)
    feats["drop_rate"] = mean(trace.drop_events)
    feats["latency_jitter"] = var(trace.step_latency)
    feats["cross_layer_shift"] = route_shift_score(trace.layer_load)
    return feats

def train_task_classifier(train_set):
    X, y = [], []
    for sample intrain_set:
        X.append(extract_route_features(sample.trace))
        y.append(sample.label)
    return fit_gradient_boosting(X, y)

def classify_unknown(model, unknown_trace):
    x = extract_route_features(unknown_trace)
    probs = model.predict_proba([x])[0]
    return topk_labels(probs, k=3)
```

为什么MoE风险更难防御

因为它不是单点泄漏，而是架构级副作用，可以想象一下以下特点：

* 你可以遮掩单个指标，但难以遮掩整条执行路径统计。
* 你可以加入随机噪声，但高并发下噪声常被平均掉。
* 你可以隔离部分请求，但性能成本很快上升。

攻击链路路径拆解，从观测到推断

阶段1：信号可用性验证

目标：确认系统是否泄漏足够稳定特征。

动作：

1. 固定提示词多次请求，观察方差。
2. 固定输出长度，比较不同提示词差异。
3. 评估是否存在可分离簇。

阶段2：构建基础分类器

目标：验证提示类别可识别性。

动作：

1. 收集N类提示词，每类M条样本。
2. 提取节奏特征与包特征。
3. 训练轻量模型（RF/XGBoost/1D-CNN）。
4. 与随机基线比较。

阶段3：目标化推断

目标：从类别识别升级为模板命中。

动作：

1. 收集企业常见固定模板。
2. 做模板库相似度检索。
3. 输出Top-k候选模板。

阶段4：联合信号增强

目标：提高稳定性与命中率。

动作：

1. 把时间 + 包大小 + 轮数 + 重试码融合。
2. 使用序列模型而非静态统计。
3. 引入会话级聚合，降低单次噪声影响。

防御方法

侧信道防御要避免一个误区：只加随机噪声，而真正有效的是分层治理。

传输层防御

1. 包长整形：对流式分片做固定桶填充。
2. 节奏整形：弱化多token突发显著性。
3. 连接策略一致化：减少条件分支导致的网络指纹。

推理层防御

1. 高敏场景关闭或弱化Speculative Decoding。
2. MoE高敏请求采用更强隔离批次策略。
3. 对路由边界加平滑策略，减少离散翻转。
4. 容量溢出策略避免暴露可分辨行为。

调度层防御

1. 租户分域，减少跨租户混批。
2. 限制共享硬件上的观测面暴露。
3. 对敏感任务启用专用队列与专用资源池。

管理面治理

1. 监控指标最小披露原则。
2. 日志脱敏与访问分级。
3. 对性能分析平台做二次权限隔离。

总结

推理系统元数据安全是模型安全未来的趋势之一，当行业从会不会回答错走向会不会泄露行为模式，侧信道将成为与数据治理、模型对齐、访问控制同等重要的基础能力。对企业来说，最现实的路径不是等待某个完美算法，而是把风险分层、把治理工程化、把评估自动化。

试着建了个星球，目前星球将会分享各种的AI安全相关知识、工具以及各种越狱手法等等。当然也会包含一些其他关于AI方面的分享，不限于安全。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OnZibpCQ9LicbxRCLwT1vFl1pNMbjI9d9eqbLwlar7NmKFjsDJSpicsxiaslMVnvHPKqniaO2olHRnyJLSciaHPzAsrz1MPd6e860ltm6dewqKFDE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/X6GlEP19Lv6ZC6RCrHTtVY8BGJ2bjBsicuB2tyzkWFV1vgu59qD0ia09uBhia48ibNEMlhABewpN5ml7M1u7KBKGzQ/0?wx_fmt=png)

Security for AI

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/X6GlEP19Lv6ZC6RCrHTtVY8BGJ2bjBsicuB2tyzkWFV1vgu59qD0ia09uBhia48ibNEMlhABewpN5ml7M1u7KBKGzQ/0?wx_fmt=png)

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