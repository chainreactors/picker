---
title: 【实战教学】超融合：把兩台配备vLLM的Nvidia DGX工作站，以607.8 tok/s的速度处理GLM-5.3
url: https://mp.weixin.qq.com/s/V2e4oz9Myeu2SZxQ8RVqIg
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:42:10.781730
---

# 【实战教学】超融合：把兩台配备vLLM的Nvidia DGX工作站，以607.8 tok/s的速度处理GLM-5.3

# 【实战教学】超融合：把兩台配备vLLM的Nvidia DGX工作站，以607.8 tok/s的速度处理GLM-5.3

原创

CyberSecGuy
CyberSecGuy

像梦又似花

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

#

当大模型规模冲到千亿级别，单卡显存再大也会触碰到天花板。最近英伟达官方放出了一套完整的落地方案：用两台 DGX Station GB300，通过 ConnectX-8 RDMA 高速互联，基于 vLLM 张量并行跑起了 7530 亿参数的 GLM-5.3 NVFP4 量化模型，对外提供统一的 OpenAI 兼容接口。

![](https://mmbiz.qpic.cn/mmbiz_png/01RLQI6qOeBjqHzd6N8Dx9IkficemZqnkbnHXOCU44ic87akEzYXQhdWichJMEqmJMuLCHEeD2VBUiacD4BzYPBNpORrlDgDqTcJNNiaOws65zHA/640?wx_fmt=png&from=appmsg)

今天我们把这套官方方案拆解清楚，从架构原理、部署步骤到实测性能一次讲透。---实战内容放在后面

---

## 一、为什么必须跨机部署？

这次部署的主角是GLM-5.3 NVFP4，一款经过量化的混合专家（MoE）大模型：

* 总参数量：7530 亿
* 每 Token 激活参数：400 亿
* 模型权重体积：约 464 GB

虽然稀疏激活大幅降低了计算量，但所有权重必须常驻显存才能保证路由效率。而单块 GB300 GPU 仅配备 252 GB HBM3e 显存，哪怕是量化版本也无法完整容纳。

解决方案是张量并行（Tensor Parallelism, TP=2）：把模型的权重张量按维度切分，均匀分布到两张 GPU 上；每一步推理时，两张 GPU 各自计算部分结果，通过高速互联交换中间数据，最终合并输出。

---

## 二、整体架构：两台机器，一个统一接口

整套方案的硬件和软件栈非常清晰，对外只暴露一个 API 端点，上层业务完全感知不到底层是两台机器。

### 硬件底座

* 两台 NVIDIA DGX Station GB300
* ConnectX-8 网卡 RDMA 直连，400Gbps 带宽，支持 GPU Direct RDMA
* 数据直接在 GPU 显存间传输，不经过 CPU 和系统内存，延迟极低

### 软件与角色分工

* 推理引擎：vLLM，原生支持分布式张量并行
* Station A（Rank 0）：主节点，对外提供 OpenAI 兼容 API，负责请求接入与结果返回
* Station B（Rank 1）：纯计算工作节点，不对外暴露接口，只参与模型计算
* 每台机器各承担约一半的权重存储与计算量

![](https://mmbiz.qpic.cn/sz_mmbiz_png/01RLQI6qOeAAprfwBAOGASWWbkDrbvrbyPUzcnjzDdWktg1mT4NsTcHgteAibvibw0fOGE714RicGZ8za2TeQLg9Ks1bFWCmrbremJqT9HVwhE/640?wx_fmt=png&from=appmsg)

图1. 两个节点服务于同一个模型：每个GPU负责在选定的RDMA连接上存储和计算模型的一部分数据。它们的内存仍然是独立的。

### 三项核心性能优化

为了在跨机场景下仍保持高吞吐，方案中启用了 vLLM 的多项关键优化：

1. 多 Token 预测（MTP）：一种推测解码技术，每步先生成 4 个候选 Token 再校验，有效提升生成吞吐量
2. FP8 KV 缓存：相比传统 FP16 缓存，显存占用减半，可容纳更长上下文与更多并发请求
3. 前缀缓存：重复的提示词前缀无需重复计算，多轮对话、同类请求场景下收益显著

---

##

## 三、部署全流程：五步跑通分布式推理

官方给出了完整的可复现步骤，我们提炼成 5 个核心阶段，适合技术团队参考落地。

### 第一步：环境与组网校验

两台机器分别完成基础环境检查：

* 确认 Docker 与 NVIDIA Container Toolkit 正常可用
* 验证 RDMA 链路状态、网卡名称、IP 地址
* 测试巨帧 ping 连通性、时间同步、GPU 状态
* 配置主节点到从节点的 SSH 免密登录，用于后续模型同步

### 第二步：模型下载与同步

1. 在主节点通过 Hugging Face 下载 GLM-5.3 NVFP4 权重（约 464 GB）
2. 通过 rsync 将模型完整同步到从节点，确保两边文件完全一致
3. 校验文件清单、结构与配置字段，确认模型完整性

> 张量并行要求两边运行完全相同的软件版本与权重文件，一致性校验是避免诡异报错的关键。

### 第三步：编写启动配置

两台机器分别写入环境配置文件，定义：

* 节点角色（Rank 0 / Rank 1）
* 主从节点 IP、RDMA 网卡与设备名
* 模型路径、容器镜像、端口等通用参数

### 第四步：启动分布式服务

启动顺序有讲究：先启从节点，再启主节点。

* 从节点以无头模式启动，等待主节点连接
* 主节点启动后，vLLM 自动通过 NCCL 建立分布式通信组
* 两边分别加载一半权重，预热内核、捕获 CUDA 图
* 主节点日志输出 `Application startup complete` 即代表服务就绪

### 第五步：健康检查与验证

1. 调用健康检查接口，确认主节点 API 正常响应
2. 检查 NCCL 日志，确认走的是 GPU Direct RDMA 而非 TCP 回退
3. 发送测试对话请求，验证输出正常、结束标志正确
4. 查看 nvidia-smi，确认两边各有约 231 GB 显存用于权重，验证模型切分正确

---

##

##

## 四、实测性能：并发16时吞吐峰值607.8 token/s

官方使用 AIPerf 工具，基于 SPEED-Bench Coding 数据集（80 段编程对话）做了完整压测，全程开启前缀缓存、MTP 推测解码与 FP8 KV 缓存。(下表怎么来的往下看就知道了![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Watermelon.png))

| 配置并发数 | 总吞吐量 (token/s) | 平均请求延迟 (s) | 首 Token 延迟 (ms) | 单 Token 间隔 (ms) |
| --- | --- | --- | --- | --- |
| 1 | 107.4 | 49.84 | 479.75 | 8.78 |
| 8 | 386.0 | 114.17 | 433.79 | 19.01 |
| 16 | 607.8 | 136.46 | 482.90 | 23.77 |
| 32 | 385.0 | 453.54 | 899.36 | 77.90 |

### 关键结论

* 吞吐量峰值出现在并发 16 的位置，达到 607.8 token/s
* 并发提升到 32 时，吞吐量不升反降，KV 缓存与调度开销成为瓶颈，请求延迟大幅上升
* 单请求场景首 Token 延迟不到 500ms，生成速度约 110 token/s，体验流畅
* 前缀缓存对真实业务场景的吞吐提升贡献显著

---

## 五、适用场景与落地建议

这套方案最适合以下场景：

* 需要本地部署超大参数模型，数据敏感不能上云
* 单卡 / 单机显存无法容纳模型规模
* 对推理延迟、吞吐量有较高要求的企业级内部服务

### 几个落地避坑提示

1. 网络是跨机并行的生命线：必须用 RDMA 高速互联，普通 TCP 网络会让通信延迟成为主要瓶颈，性能大幅下降
2. 并发不是越高越好：根据显存与业务延迟要求，找到最优并发点，盲目堆并发反而会降低吞吐
3. 张量并行适合小规模扩展：2~8 卡规模优先用张量并行；更大规模建议结合流水线并行、专家并行做分层拆分

上面的概念看完了，该动手进入实战环节![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Yellowdog.png)

实战环节(Nvidia官方)

##

##

## 步骤 1：准备两个站点

##

本教程使用一台独立的计算机（例如笔记本电脑）来管理这两个站点。首先，从该计算机分别打开与每个站点的 SSH 连接。或者，也可以在每个站点上使用本地终端进行操作。在这一步中，需要在两个站点上执行所有的命令，除非这些命令以“On A.”开头。

这两个站点运行着相同的容器和检查点，但职责不同：站点 A（等级为 0）负责托管 API，而站点 B（等级为 1）仅作为工作节点运行，没有独立的 API 服务器。

---

##

## 首先，检查 Docker 访问权限，并收集之后会使用的网络信息：

```
docker versionibdev2netdevip -br addr
```

注意：如果 `docker version` 的输出中没有 `Server` 部分，那么客户端就无法与 Docker 守护进程进行通信。如果出现 `permission denied` 错误，请按照 Docker 安装后的操作进行修复：使用 `sudo usermod -aG docker "$USER"` 命令将用户添加到 `docker` 组中，然后运行 `exit` 命令。之后重新连接设备并再次运行 `docker version` 命令。 `docker` 组拥有 root 级别的权限。

在 `ibdev2netdev` 中，列出了两个直接使用的路径： `cx8r0` 和 `cx8r1` 。可以选择其中一个来处理流量，比如 `cx8r1` 。同时，需要在每个站点上为它记录两件事：

* **Its RDMA device**

  在 `ibdev2netdev` 行中，这是一个 RDMA 设备，该行的末尾是轨道的名称。而在 `mlx5_1 port 1 ==> cx8r1 (Up)` 行中，这个设备的名称是 `mlx5_1` 。
* **Its IPv4 address**

  它的 IPv4 地址位于以铁路名称开头的 `ip -br addr` 行中。而在 `cx8r1 UP 192.168.101.1/24` 行中，地址则被标记为 `192.168.101.1` 。

这两个站点使用的铁路名称和设备都是相同的；唯一的区别是在 IPv4 地址上有所不同。

接下来，在每个站点上创建 `~/glm53.env` 。这个文件存储了后续命令所使用的数值。

```
nano ~/glm53.env
```

请粘贴以下文本，并将每个 `<...>` 的占位符替换为你记下的数值，注意保持引号的保留。

```
RANK="<NODE_RANK>"                    # RANK="0" on Station A, RANK="1" on Station B HEAD_IP="<STATION_A_IPV4_ADDRESS>"    # IPv4 address you noted on Station A; same in both filesWORKER_IP="<STATION_B_IPV4_ADDRESS>"  # IPv4 address you noted on Station B; same in both filesRAIL_IFACE="<RAIL_NAME>"              # Rail you picked, for example cx8r1; same in both filesRAIL_HCA="<RDMA_DEVICE>"              # RDMA device you noted, for example mlx5_1; same in both files
IMG=vllm/vllm-openai:v0.30.0-aarch64IMG+=@sha256:4864d46625cbc3307623e29ac742030655e27249feba7b97ec925ce4cc4dfb56MODEL_REPO=nvidia/GLM-5.3-NVFP4MODEL_REV=e3b8f9f2fad29727dfa95e766c5cac18ea1414bfMODEL_HOST="$HOME/models/GLM-5.3-NVFP4"CONTAINER=glm53-fullPORT=8000
if [ "$RANK" = 0 ]; then  NODE_IP=$HEAD_IP; PEER_IP=$WORKER_IPelse  NODE_IP=$WORKER_IP; PEER_IP=$HEAD_IPfi
GPU_UUID=$(nvidia-smi --query-gpu=uuid,name --format=csv,noheader |  awk -F, '$2 ~ /GB300/ {gsub(/ /,"",$1); print $1; exit}')
```

例如，使用默认的地址 `cx8r1` 时，站点 A 的文件结构是这样的。站点 B 的文件结构也相同，只是 `RANK="1"` 的位置有所不同。

```
RANK="0"HEAD_IP="192.168.101.1"WORKER_IP="192.168.101.2"RAIL_IFACE="cx8r1"RAIL_HCA="mlx5_1"
```

## `MODEL_HOST` 是从你的主目录构建的，而步骤 2 则通过 SSH 将检查点复制到 B 站的同一路径中。

## 注意：后续的操作都从 `source ~/glm53.env` 开始，这些数值需要被加载到程序中。每次打开新的 SSH 会话时，都请再次执行此命令。

##

## 在两个站点上，都请填入相关数值，并检查存储情况、连接状况以及基础内存使用情况：

```
source ~/glm53.envmkdir -p "$MODEL_HOST" && df -h "$MODEL_HOST"ethtool "$RAIL_IFACE"ip link show dev "$RAIL_IFACE"ping -I "$RAIL_IFACE" -M do -s 8972 -c 3 "$PEER_IP"timedatectl show -p NTPSynchronized --valuenvidia-smi
```

## 这些检查能够在布线设置和地址分配出现错误之前将其捕捉到，从而避免出现 NCCL 超时问题。预计会看到 `400000Mb/s` 这样的链接，MTU 为 9000，成功发送了巨型帧 ping，时间同步也正常。 `nvidia-smi` 在 GB300 上应该不会出现计算进程。在配备了显示 GPU 的站台上，Xorg 可能会同时出现在两个 GPU 上，占用一些内存空间。

## 提示：请注意 `nvidia-smi` 所显示的 GPU 内存使用情况；第四步会将实际内存使用情况与模型加载后的内存使用情况进行比较。

##

##

## 2. 通过 SSH 将检查点从 A 复制到 B。因此，A 需要无密码访问 B。在 A 上，创建一个没有密码短语的密钥（详情请参阅关于 SSH 密钥的部分）。在确认了 B 的主机指纹后，将它的公共密钥复制到 B 上，然后确认登录成功：

```
ssh-keygen -t ed25519ssh-copy-id "$WORKER_IP"ssh -o BatchMode=yes "$WORKER_IP" hostname
```

##

## 步骤 2：下载并复制该模型

##

## 张量并行性要求两个处理节点能够使用相同的软件来处理相同的权重数据。首先，在两个节点上同时加载固定的图像：

##

```
docker pull "$IMG" &&docker image inspect "$IMG" --format '{{.Architecture}} {{.RepoDigests}}'
```

## 这个过程可能需要几分钟的时间。通过匹配 arm64 摘要，可以确保两个等级运行相同的软件。

## 在 A 点上，下载固定的检查点文件。该文件的大小约为 464GB，下载时间大约为 1 小时，当下载速度为 1GB/s 时；或者大约 6 分钟，当下载速度为 10GB/s 时。

```
mkdir -p "$MODEL_HOST"docker run --rm --network host -v "$MODEL_HOST:/model" \  --entrypoint bash "$IMG" -lc \  "exec hf download '$MODEL_REPO' --revision '$MODEL_REV' --local-dir /model"
```

## 当 `hf download` 打印出 `Downloaded` 时，请将文件复制到 B 盘上。在 A 盘上：

```
ssh "$WORKER_IP" "mkdir -p '$MODEL_HOST'" &&rsync -aH --info=progress2 --exclude '.cache/' \  "$MODEL_HOST/" "$WORKER_IP:$MODEL_HOST/"
```

## 每个磁盘都保存了完整的检查点数据；在加载数据时，vLLM 会将权重分布到各个 GPU 上，而无需进行进一步的量化处理。

##

## 在 A 阶段，比较这两份副本（通过 SSH 方式对 B 的文件列表进行比对）。然后验证这个检查点是否准确无误：

```
(  set -euo pipefail  L=$(find "$MODEL_HOST" -path '*/.cache' -prune -o \    -type f -printf '%P %s\n' | LC_ALL=C sort | sha256sum)  R=$(ssh "$WORKER_IP" "set -o pipefail; find '$MODEL_HOST' \    -path '*/.cache' -prune -o -type f -printf '%P %s\\n' | \    LC_ALL=C sort | sha256sum")  test "$L" = "$R"  test "$(find "$MODEL_HOST" -maxdepth 1 \    -name 'model-*-of-00050.safetensors' | wc -l)" = 50  python3 -c "import j...