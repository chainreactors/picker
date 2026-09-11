---
title: AI供应链安全工程
url: https://mp.weixin.qq.com/s/6qJlcARd3Y_-yrBaUn9MxQ
source: Doonsec's feed
date: 2026-09-10
fetch_date: 2026-09-11T06:47:53.180677
---

# AI供应链安全工程

# AI供应链安全工程

原创

pandazhengzheng
pandazhengzheng

安全分析与研究

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 一、AI-BOM实现

AI系统的物料清单比传统软件复杂：不仅包含代码依赖，还包含模型权重、训练数据、超参数、评估基准。

### 1.1 AI-BOM格式设计

```
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class ModelComponent:
    name: str
    version: str
    source: str                    # 来源仓库/URL
    source_hash: str               # 来源内容哈希
    weights_hash: str              # 权重哈希
    license: str
    dependencies: list = field(default_factory=list)  # 依赖的模型/库
    training_data: Optional[str] = None              # 训练数据引用
    training_code_hash: Optional[str] = None         # 训练代码哈希
    evaluation_results: Optional[dict] = None        # 评估结果

@dataclass
class DataComponent:
    name: str
    version: str
    source: str
    source_hash: str
    license: str
    preprocessing: list = field(default_factory=list)  # 预处理管线
    statistics: Optional[dict] = None                   # 统计摘要

@dataclass
class AIBOM:
    project: str
    version: str
    created: datetime
    models: list = field(default_factory=list)
    datasets: list = field(default_factory=list)
    code_dependencies: list = field(default_factory=list)
    inference_dependencies: list = field(default_factory=list)
    signature: str = ""
```

### 1.2 自动生成工具

```
class AIBOMGenerator:
    def __init__(self, project_root):
        self.root = project_root

    def generate(self):
        bom = AIBOM(
            project=self._project_name(),
            version=self._project_version(),
            created=datetime.now(),
        )
        # 1. 扫描模型依赖
        bom.models = self._scan_models()
        # 2. 扫描数据依赖
        bom.datasets = self._scan_datasets()
        # 3. 扫描代码依赖（pip/poetry/requirements）
        bom.code_dependencies = self._scan_code_deps()
        # 4. 扫描推理依赖（ONNX/TensorRT版本等）
        bom.inference_dependencies = self._scan_inference_deps()
        # 5. 签名
        bom.signature = self._sign(bom)
        return bom

    def _scan_models(self):
        models = []
        for model_file in self._find_model_files():
            comp = ModelComponent(
                name=model_file.name,
                version=model_file.version,
                source=model_file.source_url,
                source_hash=model_file.repo_hash,
                weights_hash=hash_file(model_file.path),
                license=model_file.license,
            )
            models.append(comp)
        return models
```

### 1.3 全链路追踪

```
class ProvenanceTracker:
    """从训练到部署的全链路追踪"""
    def __init__(self, storage):
        self.storage = storage

    def record_training(self, model_id, data_id, code_hash, hyperparams):
        record = {
            "event": "training",
            "model_id": model_id,
            "data_id": data_id,
            "code_hash": code_hash,
            "hyperparams": hyperparams,
            "timestamp": datetime.now().isoformat(),
        }
        self.storage.append(record)

    def record_evaluation(self, model_id, benchmark, results):
        record = {
            "event": "evaluation",
            "model_id": model_id,
            "benchmark": benchmark,
            "results": results,
            "timestamp": datetime.now().isoformat(),
        }
        self.storage.append(record)

    def record_deployment(self, model_id, env, config):
        record = {
            "event": "deployment",
            "model_id": model_id,
            "env": env,
            "config": config,
            "timestamp": datetime.now().isoformat(),
        }
        self.storage.append(record)

    def trace(self, model_id):
        """返回某模型从训练到部署的完整链路"""
        return [r for r in self.storage if r.get("model_id") == model_id]
```

---

## 二、模型完整性验证

### 2.1 权重签名

```
class ModelSignatureManager:
    def __init__(self, private_key, public_key):
        self.private = private_key
        self.public = public_key

    def sign_model(self, model_path):
        weights_hash = hash_file(model_path)
        signature = sign(weights_hash, self.private)
        return {
            "model_path": model_path,
            "weights_hash": weights_hash,
            "signature": signature,
            "signer": "model_registry",
            "timestamp": datetime.now().isoformat(),
        }

    def verify_model(self, model_path, manifest_entry):
        actual_hash = hash_file(model_path)
        if actual_hash != manifest_entry["weights_hash"]:
            return False, "hash_mismatch"
        if not verify(
            manifest_entry["weights_hash"],
            manifest_entry["signature"],
            self.public
        ):
            return False, "signature_invalid"
        return True, "verified"
```

### 2.2 safetensors安全加载

`safetensors`格式避免`pickle`反序列化漏洞，是加载不可信模型的首选：

```
from safetensors import safe_open

class SafeModelLoader:
    def __init__(self, allowed_keys=None, max_size_gb=10):
        self.allowed_keys = allowed_keys
        self.max_size = max_size_gb

    def load(self, path):
        # 1. 文件大小检查
        if file_size(path) > self.max_size * 1e9:
            raise SecurityError("model_too_large")
        # 2. 用safetensors加载（无代码执行）
        with safe_open(path, framework="pt") as f:
            keys = f.keys()
            if self.allowed_keys and not set(keys).issubset(self.allowed_keys):
                raise SecurityError(f"unexpected_keys: {set(keys) - self.allowed_keys}")
            weights = {k: f.get_tensor(k) for k in keys}
        # 3. 权重统计检查
        self._check_weight_stats(weights)
        return weights

    def _check_weight_stats(self, weights):
        for name, w in weights.items():
            if torch.isnan(w).any() or torch.isinf(w).any():
                raise SecurityError(f"invalid_weights: {name}")
            if w.abs().max() > 1e6:
                raise SecurityError(f"suspicious_weights: {name}")
```

### 2.3 来源验证

```
class SourceVerifier:
    def __init__(self, trusted_registries):
        self.trusted = trusted_registries

    def verify(self, model_source):
        # 1. URL域名白名单
        if not self._trusted_domain(model_source.url):
            return False, "untrusted_domain"
        # 2. 仓库签名验证
        if not model_source.repo_signature_valid:
            return False, "repo_signature_invalid"
        # 3. 发布者身份验证
        if model_source.publisher not in self.trusted_publishers:
            return False, "untrusted_publisher"
        # 4. 模型卡完整性
        if not self._verify_model_card(model_source):
            return False, "model_card_incomplete"
        return True, "verified"
```

---

## 三、依赖审计自动化

### 3.1 依赖树扫描

```
class DependencyAuditor:
    def __init__(self, cve_db, poison_db):
        self.cve_db = cve_db
        self.poison_db = poison_db

    def audit(self, project):
        # 1. 解析依赖树
        deps = self._parse_dependencies(project)
        findings = []
        # 2. CVE关联
        for dep in deps:
            cves = self.cve_db.query(dep.name, dep.version)
            for cve in cves:
                findings.append({
                    "type": "cve",
                    "dep": dep.name,
                    "version": dep.version,
                    "cve": cve.id,
                    "severity": cve.severity,
                })
        # 3. 投毒包检测
        for dep in deps:
            if self.poison_db.is_known_poisoned(dep.name, dep.version):
                findings.append({
                    "type": "poisoned_package",
                    "dep": dep.name,
                    "version": dep.version,
                })
        # 4. typosquatting检测
        for dep in deps:
            if self._is_typosquatting(dep.name):
                findings.append({
                    "type": "typosquatting",
                    "dep": dep.name,
                })
        return findings

    def _is_typosquatting(self, name):
        for trusted in self.trusted_packages:
            if self._edit_distance(name, trusted) <= 2 and name != tru...