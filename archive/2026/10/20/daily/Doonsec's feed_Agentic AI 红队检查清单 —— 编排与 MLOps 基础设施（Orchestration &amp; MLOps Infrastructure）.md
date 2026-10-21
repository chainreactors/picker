---
title: Agentic AI 红队检查清单 —— 编排与 MLOps 基础设施（Orchestration &amp; MLOps Infrastructure）
url: https://mp.weixin.qq.com/s/Y_13-fzHyngUkyn-d7RBLA
source: Doonsec's feed
date: 2026-10-20
fetch_date: 2026-10-21T06:48:35.510017
---

# Agentic AI 红队检查清单 —— 编排与 MLOps 基础设施（Orchestration &amp; MLOps Infrastructure）

# Agentic AI 红队检查清单 —— 编排与 MLOps 基础设施（Orchestration & MLOps Infrastructure）

原创

APT-101
APT-101

APT-101

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PIWj1VguNovRfljDnSIgWb54BHgNl6wdzz8RE6WiccOCV3lLBmYo1PCgqgGXjlVbtYvTMBhhJtFSEN6fVZnCu24RpnzY5uWXmXGgkZOYVczY/640?wx_fmt=png&from=appmsg)

> **来源**：《An agentic AI red team checklist: 222 tests, WSTG-style》，Ravi Rajput，infosecravi.com，2026-10-08。 全表 222 项测试 / 20 个类别；本文件为**第 2 类「编排与 MLOps 基础设施」共 14 项**（AI-INF-001 ~ AI-INF-014）。 **风险等级分布**：严重 7 项 / 高 6 项 / 中 1 项 —— 本类是全部 20 类中「严重」密度最高的一类之一。 **检测方式分布**：反射型 5 项 / 反射｜带外 5 项 / 带外 2 项 / 盲测型 1 项 / 反射｜盲测 1 项。 **框架映射分布**：ML06:2023 12 项 / LLM08 向量与嵌入弱点 2 项（011、012）。 **术语约定**：`target`、`api.target`、`endpoint` 为目标资产占位符；`TARGET` 为已知存活主机；`<COLLAB>` 为带外监听地址。

---

## 这一类的定位

第 1 类（侦察与发现）负责**扫出端口**，这一类负责**把端口变成能力**。14 项里有 12 项映射到 `ML06:2023`（ML 系统供应链/部署弱点），而不是 LLM 应用层——说明标准层面把它归为**基础设施层缺陷**，与模型无关，修的是部署姿势。

按后果可分两条链：

* **读链（信息收集）**：`001` MLflow 未认证列举 → `009` TensorBoard 读图 → `012` 特征库/registry 读数据 → `005` Redis 读集群状态。
* **写链（代码执行）**：`002` 注册恶意模型 → `004` Ray 任务提交 → `007/008` Notebook kernel → `010` DAG 注入 → `014` SLURM 作业。

**`AI-INF-002` 是这两条链的交汇点**：MLflow 写权限既能投毒下游推理（完整性），也能通过模型加载路径直接落到反序列化 RCE（可用性）。

---

## 一览

| 测试编号 | 测试名称 | 风险等级 | 检测方式 | 框架映射 |
| --- | --- | --- | --- | --- |
| AI-INF-001 | 未认证的 MLflow tracking server（列举 experiments/runs/artifacts） | 高 | 反射型 | ML06:2023 |
| AI-INF-002 | MLflow 模型注册篡改（注册恶意模型） | **严重** | 盲测型 | ML06:2023 |
| AI-INF-003 | MLflow 路径遍历 / LFI / XSS（核实 CVE） | **严重** | 反射型｜带外 | ML06:2023 |
| AI-INF-004 | 未认证的 Ray dashboard / 任务提交 RCE | **严重** | 带外 | ML06:2023 |
| AI-INF-005 | Ray GCS（Redis）未认证集群访问 | **严重** | 反射型 | ML06:2023 |
| AI-INF-006 | Kubeflow dashboard / pipeline 未认证访问 | 高 | 反射型 | ML06:2023 |
| AI-INF-007 | Kubeflow notebook server 未认证 / 令牌绕过 | **严重** | 反射型｜带外 | ML06:2023 |
| AI-INF-008 | Jupyter 未认证 kernel 执行 / 令牌绕过 | **严重** | 反射型｜带外 | ML06:2023 |
| AI-INF-009 | TensorBoard 未认证读取图/指标 | 中 | 反射型 | ML06:2023 |
| AI-INF-010 | Airflow / Prefect DAG 注入 / 未认证 API | **严重** | 带外 | ML06:2023 |
| AI-INF-011 | 模型服务端点 /invocations 未认证推理与注入 | 高 | 反射型｜带外 | LLM08 向量与嵌入弱点 |
| AI-INF-012 | 特征库 / model registry 未认证读取 | 高 | 反射型 | LLM08 向量与嵌入弱点 |
| AI-INF-013 | MLOps 默认凭据与弱认证 | 高 | 反射型｜盲测型 | ML06:2023 |
| AI-INF-014 | GPU 主机 / 作业调度器（SLURM）滥用 | 高 | 反射型｜带外 | ML06:2023 |

---

## 14 项明细

### AI-INF-001

**测试编号**：AI-INF-001 **测试类别**：编排与 MLOps 基础设施 **测试名称**：未认证的 MLflow tracking server（列举 experiments/runs/artifacts） **风险等级**：高

**测试方法**

1. 在无认证的情况下查询 /api/2.0/mlflow/experiments/list。
2. 列举 run 与 metric。
3. 若可访问，下载已记录的 artifact。

```
curl -s http://target:5000/api/2.0/mlflow/experiments/search | jqcurl -s http://target:5000/api/2.0/mlflow/experiments/list
```

**预期结果**

在无凭据情况下返回 experiment 与 run 的 JSON，包含 artifact 路径。

---

### AI-INF-002

**测试编号**：AI-INF-002 **测试类别**：编排与 MLOps 基础设施 **测试名称**：MLflow 模型注册篡改（注册恶意模型） **风险等级**：严重

**测试方法**

1. 确认对 model registry 具有写权限。
2. 注册恶意或投毒后的模型 artifact。
3. 验证该模型被服务加载或被下载。

```
curl -s -X POST http://target:5000/api/2.0/mlflow/registered-models/createfickling model.pkl
```

**预期结果**

成功注册新增或替换的模型版本，且可按名称检索。

---

### AI-INF-003

**测试编号**：AI-INF-003 **测试类别**：编排与 MLOps 基础设施 **测试名称**：MLflow 路径遍历 / LFI / XSS（核实 CVE） **风险等级**：严重

**测试方法**

1. 识别 MLflow 版本。
2. 对 artifact 与 view 端点测试路径遍历。
3. 对照当前 CVE 确认文件读取或 XSS 执行。

```
curl -s 'http://target:5000/model-versions/get-artifact?path=../../etc/passwd'nuclei -tags mlflow -severity high,critical
```

**预期结果**

返回服务器文件内容或执行注入脚本，且与当前 CVE/NVD 条目相符。

> **注意**：原清单刻意不硬编码 CVE 编号（攻击*类别*稳定、具体编号会腐化）。引用具体 CVE 前须对照最新 NVD 核实，详见「使用提示」末条。

---

### AI-INF-004

**测试编号**：AI-INF-004 **测试类别**：编排与 MLOps 基础设施 **测试名称**：未认证的 Ray dashboard / 任务提交 RCE **风险等级**：严重

**测试方法**

1. 在无认证的情况下访问 /api/jobs/。
2. 提交一个运行攻击者代码的任务。
3. 通过回调或输出确认执行。

```
curl -s http://target:8265/api/jobs/ray job submitnuclei -tags ray
```

**预期结果**

提交的任务成功执行攻击者代码并回调监听器。

---

### AI-INF-005

**测试编号**：AI-INF-005 **测试类别**：编排与 MLOps 基础设施 **测试名称**：Ray GCS（Redis）未认证集群访问 **风险等级**：严重

**测试方法**

1. 连接 6379 端口并执行 INFO。
2. 读取集群与状态键。
3. 尝试注入任务或状态记录。

```
redis-cli -h target -p 6379 INFOredis-cli -h target -p 6379 KEYS '*'nmap -sV -p 6379 target
```

**预期结果**

在未认证情况下返回 Redis INFO 与集群状态键。

---

### AI-INF-006

**测试编号**：AI-INF-006 **测试类别**：编排与 MLOps 基础设施 **测试名称**：Kubeflow dashboard / pipeline 未认证访问 **风险等级**：高

**测试方法**

1. 访问 dashboard 根路径与 /pipeline/。
2. 检查 pipeline 列表与创建 API。
3. 确认可访问 notebook 与 experiment。

```
curl -s http://target:8080/pipeline/curl -s http://target:8080/nuclei -tags kubeflow
```

**预期结果**

在无凭据情况下返回 dashboard 与 pipeline 数据。

---

### AI-INF-007

**测试编号**：AI-INF-007 **测试类别**：编排与 MLOps 基础设施 **测试名称**：Kubeflow notebook server 未认证 / 令牌绕过 **风险等级**：严重

**测试方法**

1. 在无令牌情况下访问 notebook server 端点。
2. 测试令牌绕过与头部操纵。
3. 通过 kernel 执行代码。

```
curl -s http://target:8888/api/contentscurl -s http://target:8888/api/kernelsnuclei -tags jupyter
```

**预期结果**

在无有效令牌的情况下获取 kernel 会话；注入的代码执行成功。

---

### AI-INF-008

**测试编号**：AI-INF-008 **测试类别**：编排与 MLOps 基础设施 **测试名称**：Jupyter 未认证 kernel 执行 / 令牌绕过 **风险等级**：严重

**测试方法**

1. 在无认证情况下查询 /api/contents 与 /api/kernels。
2. 通过查询串或头部技巧绕过令牌。
3. 启动 kernel 并执行代码。

```
curl -s http://target:8888/api/contentscurl -s -X POST http://target:8888/api/kernelsnmap -sV -p 8888 target
```

**预期结果**

代码在 Jupyter 主机上执行并返回输出或回调。

---

### AI-INF-009

**测试编号**：AI-INF-009 **测试类别**：编排与 MLOps 基础设施 **测试名称**：TensorBoard 未认证读取图/指标 **风险等级**：中

**测试方法**

1. 在无认证情况下访问 6006 端口上的 TensorBoard。
2. 查询数据端点获取标量与直方图。
3. 提取模型元数据与图结构。

```
curl -s http://target:6006/data/plugins/scalars/scalarscurl -s http://target:6006/nmap -sV -p 6006 target
```

**预期结果**

在未认证情况下返回训练指标与图元数据。

---

### AI-INF-010

**测试编号**：AI-INF-010 **测试类别**：编排与 MLOps 基础设施 **测试名称**：Airflow / Prefect DAG 注入 / 未认证 API **风险等级**：严重

**测试方法**

1. 检查 Airflow 与 Prefect 的 API/UI 是否存在未认证访问。
2. 创建或触发恶意 DAG 或 flow。
3. 通过回调或日志确认执行。

```
curl -s http://target:8080/api/v1/dagscurl -s -X POST http://target:8080/api/v1/dags/bad_dag/dagRuns -d '{}'nuclei -tags airflow
```

**预期结果**

恶意 DAG 或 flow 成功运行并回调，证实编排层 RCE。

---

### AI-INF-011

**测试编号**：AI-INF-011 **测试类别**：编排与 MLOps 基础设施 **测试名称**：模型服务端点 /invocations 未认证推理与注入 **风险等级**：高

**测试方法**

1. 在无 SigV4 或无认证的情况下向 /invocations 发送 POST 请求。
2. 测试推理输出泄露。
3. 通过 pickle 或 SSRF 等构造输入测试注入。

```
curl -s https://endpoint/invocations -d '{}'curl -s http://target:8080/v1/embeddings -d '{"input":"..."}'
```

**预期结果**

在未认证情况下返回推理输出，或注入的输入触发回调。

---

### AI-INF-012

**测试编号**：AI-INF-012 **测试类别**：编排与 MLOps 基础设施 **测试名称**：特征库 / model registry 未认证读取 **风险等级**：高

**测试方法**

1. 枚举特征库与 registry 端点。
2. 查询特征、实体与模型元数据。
3. 提取 PII 与嵌入。

```
curl -s http://target:6333/collectionscurl -s http://target:8080/v1/objects?limit=10curl -s http://target:9200/_cat/indices
```

**预期结果**

在无凭据情况下返回特征值、模型元数据或向量载荷。

---

### AI-INF-013

**测试编号**：AI-INF-013 **测试类别**：编排与 MLOps 基础设施 **测试名称**：MLOps 默认凭据与弱认证 **风险等级**：高

**测试方法**

1. 测试已知默认值（minioadmin:minioadmin、admin:admin、airflow）。
2. 对登录端点暴力破解弱凭据。
3. 枚举认证后可用的能力。

```
curl -s http://target:9000/minio/health/livehydra -L users.txt -P pass.txt targetnuclei -tags default-login
```

**预期结果**

使用默认或弱凭据在某个 MLOps 服务上成功认证。

---

### AI-INF-014

**测试编号**：AI-INF-014 **测试类别**：编排与 MLOps 基础设施 **测试名称**：GPU 主机 / 作业调度器（SLURM）滥用 **风险等级**：高

**测试方法**

1. 识别 SLURM 调度器与 GPU 主机端点。
2. 提交任务或连接到计算节点。
3. 执行代码并通过输出或回调确认。

```
squeuesrun -N1 hostnamessh user@gpuhostnmap -sV -p 22,6817 target
```

**预期结果**

由攻击者控制的任务在调度器或 GPU 主机上运行，并返回输出或回调。

---

## 端口 → 服务对照（本类涉及）

| 端口 | 服务 | 对应测试项 |
| --- | --- | --- |
| 5000 | MLflow tracking / model registry | AI-INF-001、002、003 |
| 8265 | Ray dashboard / head | AI-INF-004 |
| 6379 | Ray GCS（Redis） | AI-INF-005 |
| 8080 | Kubeflow / Airflow | AI-INF-006、010 |
| 8888 | Kubeflow Notebooks / Jupyter | AI-INF-007、008 |
| 6006 | TensorBoard | AI-INF-009 |
| 9000 | MinIO | AI-INF-013 |
| 6333 | Qdrant（特征库） | AI-INF-012 |
| 9200 | Elasticsearch（特征库） | AI-INF-012 |
| 22 / 6817 | SSH / SLURM 调度器 | AI-INF-014 |

---

## 使用提示

* **不要硬编码 CVE**：清单刻意省略具体编号，攻击*类别*稳定而 CVE ID 会腐化（作者提到曾有一批二手文章反复引用已失效的 `AML.T0104`...