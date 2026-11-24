---
title: 自部署 Ollama 流式响应包长侧信道攻击实测与缓解方案评估
url: https://xz.aliyun.com/news/93435
source: 先知安全技术社区
date: 2026-11-23
fetch_date: 2026-11-24T11:47:34.476513
---

# 自部署 Ollama 流式响应包长侧信道攻击实测与缓解方案评估

[先知社区](/)[文章](/news)[视频](/course)[众测](/vuln)[赛事](/ctf)[技能](/skills)[墨白](/mobai)[活动](/events)[名人堂](/hof)[积分商城](/points-mall)

[写文章](/write)

有用收藏打赏分享

# 自部署 Ollama 流式响应包长侧信道攻击实测与缓解方案评估

[![](/images/default-avatar.png)xhu](/users/180460)·2026-11-23 09:48·15 分钟·52·江西·AI专栏

本文针对自部署 Ollama 服务的 TLS 加密流量，利用随机森林分类器对 SSE 流式响应的包长特征进行建模，实现不解密推断用户对话主题。实验对比了关闭流式、反代缓冲、随机填充、定长填充与时序抖动五种缓解措施的效果，证实网关层随机填充是唯一能将准确率压至随机线且不影响流式体验的方案。

> 导读：TLS加密只保护内容，藏不住流量的形状。本文把公开研究针对商业API的包长侧信道攻击搬到自部署Ollama场景：10类中文主题、真实抓包与随机森林分类实测主题推断准确率，再对关流式、反代缓冲、随机填充、定长填充、时序抖动五类缓解逐项实测准确率衰减与延迟代价，并给出可落地的部署层结论。

## **1 加密救不了隐私：问题从哪来**

### **1.1 两年半研究脉络，一条没有合上的口子**

这条攻击线不是新故事，但它一直在进化：

2024年3月，Ben-Gurion大学的Weiss等人在USENIX Security '24论文《What Was Your Prompt? A Remote Keylogging Attack on AI Assistants》（arXiv:2403.09751）里把流式响应的token长度侧信道做成了远程键盘记录攻击——从加密流量逐token恢复对话文本。该问题经微软安全响应中心（MSRC）流转至各厂商，Cloudflare于同月公开了自己的缓解方案：对token响应做填充与聚合。此后主流厂商陆续把token合并引入为默认缓解。同期，Carlini等人在arXiv:2403.06565（Stealing Part of a Production Language Model）里证明了推理服务的时序信号还能反推模型内部属性。

2025年11月，微软Defender安全研究团队发布Whisper Leak（arXiv:2511.03675，11月7日安全博客同步）：不解密任何流量，仅凭包长与时序训练分类器，就能推断用户与LLM对话的主题，实验覆盖多家主流厂商，并事先向约30家厂商做了责任披露。

2026年，USENIX Security '26收录的PromptEcho（From Length to Content: Token-Length Side-Channel Attacks on LLM API Merged Outputs，Sijia Li等）给出结论：token合并没有关上这扇门——合并后的传输仍存在可利用的长度侧信道。

也就是说，两年半过去，厂商侧的缓解（合并、padding）一直在被证明不够。

### **1.2 本文要补的三个空白**

第一是部署形态。公开研究有一个共同前提：目标是商业API。商业服务前置了CDN、API网关和厂商侧缓解层，攻击者与模型之间隔着整条优化过的链路。但另一类部署形态被系统性忽略了：把Ollama直接架在公网VPS上，Nginx一层反代加自签证书就对外提供服务。这条路径上没有任何厂商侧缓解，TLS记录的形状原样暴露。本文实测的就是这个场景：自部署小模型服务，攻击者能看到什么。

第二是语言。公开实验以英文提示词为主，中文的分词密度、UTF-8字节宽度都不同，泄露特征是否同样成立需要数据说话。

第三是缓解的实测对照。论文给出的缓解方案（如TokenPadding）偏学术，而自部署运维真正会动的层是Nginx反代和自写网关。关流式、反代缓冲、SSE填充、时序抖动这四类"运维可操作"的手段，各自能换来多少准确率下降、付出多少延迟代价，公开资料里没有对照数据。本文逐项实测。

## **2 威胁模型与泄露原理**

### **2.1 流式响应为什么逐chunk下发**

OpenAI兼容API在请求体里带 `"stream": true` 时，服务端以SSE（Server-Sent Events）返回：每个生成步产生一个 `data: {...}\n\n` 事件，JSON里包着增量token。Ollama的 `/v1/chat/completions` 兼容此行为。逐chunk下发是流式体验的来源，也是泄露的来源：SSE事件的字节数等于固定的JSON包装加上该token的UTF-8字节宽度——包装恒定不变，波动部分只来自token本身。

### **2.2 TLS不隐藏长度**

TLS（1.2与1.3均如此）对记录载荷加密，但记录头中的length字段是明文的。tshark里 `tls.record.length` 直接可读。TCP层的到达时间同样明晃晃地暴露。加密链路上，攻击者拿不到内容，但拿到一个完整的"形状序列"：每次响应的TLS记录长度序列与到达时间序列。

### **2.3 主题如何从形状里浮出来**

以qwen2.5的分词器为例，一个汉字通常对应1个token（UTF-8占3字节），英文单词、标点、代码符号各有自己的字节宽度。10类主题（菜谱、代码、诗歌、运维……）的用词分布差异，会体现在"每个SSE事件的字节数"这个序列的统计分布上。分类器要做的，就是把形状序列映射回主题。注意这里必须排除一个混淆变量：答案的长短。如果某类主题的回答天然更长，分类器学到的可能只是长度而非主题。实验协议里用固定 `max_tokens=64` 控制了这一点。

威胁模型：被动监听者（同WiFi、企业出口、ISP链路上的任意位置），只读包元数据，不解密、不注入、不干扰。任务是10类闭集主题判定。

![](https://xzfile.aliyuncs.com/2026/11/23/0933/e0d72ad9-c6e.png)

图1 实验拓扑

## **3 服务端搭建**

### **3.1 目标环境与模型**

实验目标机是一台阿里云ECS：2vCPU、2GB内存、1Mbps公网带宽，Alibaba Cloud Linux 3（内核5.10.134）。这个配置是个人开发者自部署LLM的典型下限档，也正因为带宽只有1Mbps，后续延迟代价的测量才会被放大到值得讨论的程度。

内存约束下选qwen2.5-0.5b-instruct（GGUF q4\_k\_m，491MB）。Ollama已预装，模型权重从ModelScope拉取后经Modelfile导入。这里有个国内VPS的现实困难值得记录：直连Ollama Registry与hf-mirror的下载吞吐都只有几十KB/s，最终走ModelScope源并用 `curl -C -` 断点续传才稳定拉完（491,400,032字节分三次续传）——1Mbps带宽的机器拉491MB模型本身就是一次运维体验：

```
# ModelScope 源 + 断点续传（实际分多次完成）
curl -sL -C - -o /home/admin/models/qwen25-ms.gguf \
  "https://modelscope.cn/models/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/master/qwen2.5-0.5b-instruct-q4_k_m.gguf"
​
cat > /tmp/Modelfile <<EOF
FROM /home/admin/models/qwen25-ms.gguf
EOF
ollama create qwen25-05b -f /tmp/Modelfile
```

模型导入结果与运行态进程见图2。

![](https://xzfile.aliyuncs.com/2026/11/23/0934/6969f362-2ae.png)

图2 模型导入与运行态进程

### **3.2 Nginx TLS反代：一行配置决定泄露强度**

用openssl自签证书（生产环境换成ACME证书不影响本文结论，TLS层对包长的处理一致）：

```
openssl req -x509 -newkey rsa:2048 -keyout side.key -out side.pem \
  -days 30 -nodes -subj "/CN=llm-side-lab"
```

反代配置里有一行值得单独说：

```
server {
    listen 8443 ssl;
    ssl_certificate     /etc/nginx/ssl/side.pem;
    ssl_certificate_key /etc/nginx/ssl/side.key;
    ssl_protocols       TLSv1.2 TLSv1.3;
    gzip off;                          # 压缩会改写包长特征，SSE 也不应压缩
​
    location / {
        proxy_pass http://127.0.0.1:11434;
        proxy_http_version 1.1;
        proxy_set_header Connection "";
        proxy_buffering off;           # 关键行：SSE 逐 chunk 即时转发
        proxy_read_timeout 300s;
    }
}
```

`proxy_buffering off` 是所有流式部署教程都会教的一行：不关它，Nginx会把上游chunk攒进8KB缓冲区，用户就看不到"逐字吐出"的效果。但换个视角——这行配置同时是把每个SSE事件即时推到网络上的开关。缓冲关闭时，TLS记录与token一一对应，泄露信号最强；缓冲开启时，响应被攒成整块下发。它是本文最重要的缓解实验变量（第6.2节）。

自签证书首次访问会触发浏览器告警（图4），这不影响侧信道（攻击者只看元数据），只影响用户体验。8443反代的实际配置与 `nginx -t` 校验结果见图3。

![](https://xzfile.aliyuncs.com/2026/11/23/0938/7edee696-a5d.png)

图3 8443反代配置与nginx -t校验结果

![](https://xzfile.aliyuncs.com/2026/11/23/0934/f2d824f5-a31.png)

图4 浏览器对自签证书的告警页

### **3.3 服务端行为验证**

用 `curl -N`（禁用缓冲）走8443发一个流式请求，确认SSE逐chunk到达。图5是真实回显：每个 `data:` 事件的 `content` 字段就是一个增量token，粒度1~2个汉字不等。

![](https://xzfile.aliyuncs.com/2026/11/23/0935/cb82c2d8-3eb.png)

图5 SSE流式响应逐chunk到达

## **4 攻击端实现**

### **4.1 抓包与流量切分**

攻击端在Kali上。抓包用dumpcap（免root，capabilities已配）：

```
dumpcap -i eth0 -w cap_base.pcap -f "host 118.31.227.72 and port 8443"
```

图6是基线配置下tcpdump的实时输出：服务端8443发往客户端的每一行 `Flags [P.]` 就是一个token包，`length` 字段逐包变化，肉眼即可分辨。

![](https://xzfile.aliyuncs.com/2026/11/23/0935/9c01a047-7c2.png)

图6 基线阶段tcpdump实时输出

一个关键设计：每次请求使用独立TCP连接（请求头带 `Connection: close`）。这样pcap里每条TCP流恰好对应一次请求-响应，不需要从长连接里切分响应边界。真实攻击里攻击者面对的多是keep-alive长连接，按SSE事件边界切分是额外工程；本文选择独立连接以简化归因，不改变泄露本质。

TLS记录提取用tshark，只取服务端到客户端方向的记录。这里有一个公开资料很少提到的坑：实验链路协商的是TLS 1.3，`tls.record.content_type`（解密后的内容类型）在没有密钥时为空，外层类型要改用 `tls.record.opaque_type`——TLS 1.3的所有记录外层统一为23：

```
tshark -r cap_base.pcap -Y "tcp.srcport == 8443 && tls.record.opaque_type == 23" \
  -T fields -e tcp.stream -e frame.time_epoch -e tls.record.length
```

这里还有第二个更隐蔽的坑：一个TCP段可能携带多条TLS记录（SSE事件小、服务端写入密时会被合并发送），此时tshark把同一帧内多条记录的长度用逗号拼进同一个字段输出。解析脚本若按整数直接转换，这类帧会被整帧丢弃——基线流量里它只占约4%，流式场景下仅造成轻微失真；但换到关流式或缓冲开启场景，响应被高度聚合，几乎所有帧都是多记录帧，逐帧丢弃会让特征矩阵直接蒸发成空集。稳健做法是按逗号拆分逐条展开，同帧记录共享帧时间戳。

本文第一版解析脚本恰好踩中此坑。事后核查被丢弃的602个帧，内容几乎全是 `122,1,38,817,281,69` 这样的响应开场簇与 `443,22,19` 这样的收尾簇——即响应头、TLS控制记录与[DONE]尾事件等常数结构。丢弃它们等价于一次无意的"去常数记录"预处理，基线准确率因此虚高了8个百分点（41.5%对修正后的33.0%）。本文所有阶段数据均以修正解析后的结果为准。

### **4.2 特征工程**

每条响应构造23维特征：

* 包长分桶直方图（11桶，边界0/64/128/192/256/320/384/512/768/1024/1536/+inf）；
* 记录数、总字节、均值、标准差、中位数、P90、首记录长、末记录长；
* 时序4项：平均到达间隔、间隔标准差、最大间隔、响应总时长。

时序4项可以整体关闭（消融实验用）。特征构造的核心实现如下（节选自分析脚本，与后文所有数字一一对应）：

```
SIZE_BINS = [0, 64, 128, 192, 256, 320, 384, 512, 768, 1024, 1536, 10**9]
​
def features(recs, use_time=True):
    # recs: [(到达时间, 记录长度), ...] 单次响应的全部记录
    ts = [t for t, l in recs]; ls = [l for t, l in recs]
    hist = [0] * (len(SIZE_BINS) - 1)
    for l in ls:
        for i in range(len(SIZE_BINS) - 1):
            if SIZE_BINS[i] <= l < SIZE_BINS[i + 1]:
                hist[i] += 1; break
    n = len(ls); arr = np.array(ls, dtype=float)
    f = hist + [n, arr.sum(), arr.mean(), arr.std(),
                np.median(arr), np.percentile(arr, 90), ls[0], ls[-1]]
    if use_time and n >= 2:
        d = np.diff(np.array(ts))
        f += [d.mean(), d.std(), d.max(), ts[-1] - ts[0]]
    else:
        f += [0.0, 0.0, 0.0, 0.0]   # 仅包长消融：时序 4 维置零
    return f
```

这样设计的动机：目标服务器上同时跑着一个第三方算力共享agent，周期性外连下载文件，构成真实生产环境里的背景噪声。时序信道对这类噪声最敏感，消融对照能回答"在真实噪声下，包长信道和时序信道各自贡献多少"。

### **4.3 实验协议**

* 10类主题（cooking/code/science/fitness/poem/game/business/ops/myth/movie），每类3条中文问法轮换，避免同一句提示重复造成的过拟合假象；
* 固定 `max_tokens=64`、`temperature=0.7`；
* 分类器与评测代码：

```
clf = RandomForestClassifier(n_estimators=300, random_state=42)
cv = StratifiedKFold(5, shuffle=True, random_state=42)
sc = cross_val_score(clf, X, y, cv=cv)            # 报告 mean±std
​
Xtr, Xte, ytr, yte = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=42)
clf.fit(Xtr, ytr)                                  # 留出集出混淆矩阵
```

* 每阶段独立抓包、独立训练评测。

![](https://xzfile.aliyuncs.com/2026/11/23/0935/962d8dba-3e7.png)

图7 特征提取流水线

### **4.4 缓解措施实现**

M3/M4/M5共用一个Python填充代理（127.0.0.1:9445，Nginx 8443切换上游到它）。填充利用了SSE规范允许的注释行：以冒号开头的行会被所有合规客户端解析器忽略，却能撑大事件体积——

```
def pad_event(ev):
    if PAD_MODE in ("random", "fixed"):
        target = random.randint(256, 1024) if PAD_M...