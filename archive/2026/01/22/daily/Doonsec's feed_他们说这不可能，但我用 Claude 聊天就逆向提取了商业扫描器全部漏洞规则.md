---
title: 他们说这不可能，但我用 Claude 聊天就逆向提取了商业扫描器全部漏洞规则
url: https://mp.weixin.qq.com/s/BXrnI0sZM92SATpmUdYkTA
source: Doonsec's feed
date: 2026-01-22
fetch_date: 2026-01-23T03:30:00.549903
---

# 他们说这不可能，但我用 Claude 聊天就逆向提取了商业扫描器全部漏洞规则

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BibeFvVBkRA9Mmxv1eCEciclEcBTqHYjqSoBpxkW7JZz7577ba52tE5HRHvs3R9Jg1V75Ds6q5cH0LflTVRibvwtg/0?wx_fmt=jpeg)

# 他们说这不可能，但我用 Claude 聊天就逆向提取了商业扫描器全部漏洞规则

原创

AI安全工坊
AI安全工坊

AI安全工坊

![]()

在小说阅读器中沉浸阅读

# 他们说这不可能，但我用 Claude 聊天就逆向提取了商业扫描器全部漏洞规则

> "
>
> 不需要懂逆向，不需要会编程，只需要和 AI 对话。本文记录了一次完整的技术实验：通过与 AI 助手对话，从某商业漏洞扫描器中提取漏洞检测规则的全过程。

---

**⚠️ 重要声明**

本文内容仅用于**安全研究**和**技术教育**目的，旨在：

1. 1. 探索 AI 在安全研究领域的应用边界
2. 2. 帮助安全产品厂商了解潜在风险并改进防护
3. 3. 促进安全社区的技术交流与进步

**请勿将本文技术用于任何未经授权的场景。** 未经授权对商业软件进行逆向工程可能违反相关法律法规和用户协议。读者应自行承担因不当使用而产生的一切法律责任。

---

## 0x00 背景

在安全行业，漏洞扫描器的核心竞争力在于其**漏洞检测规则库**。这些规则库通常包含：

* • 数千个 CVE 漏洞的检测逻辑
* • 大量未公开的 0day 检测规则
* • 针对国内软件的专属 POC
* • 多年积累的检测经验

对于安全研究人员来说，这些规则具有极高的学习价值。但厂商通常会采用各种手段保护这些核心资产：编译嵌入、压缩存储、加密保护…

传统的提取方式需要深厚的逆向工程功底，可能需要数天甚至数周的时间。

但这一次，我决定尝试一种不同的方式：**完全通过与 AI 对话来完成这个任务**。

## 0x01 工具准备

我使用的是 **Claude Code**，一个基于 Claude Opus 4 模型的终端 AI 助手。它可以：

* • 在终端中与你对话
* • 理解你的目标和上下文
* • 生成并执行 shell 命令
* • 根据命令输出调整策略
* • 生成完整的脚本代码

关键是：**你不需要知道具体怎么做，只需要描述你想要什么**。

## 0x02 目标分析

目标是一个 Docker 容器化部署的商业漏洞扫描器，架构如下：

```
┌─────────────────────────────────────────────────────────┐
│                    系统架构                              │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────┐    gRPC     ┌─────────────────────┐   │
│  │  Web 前端   │◄───────────►│    扫描引擎          │   │
│  │  (Python)   │             │    (Go 语言)         │   │
│  └──────┬──────┘             │                     │   │
│         │                    │  核心二进制 150MB+   │   │
│         ▼                    │  - POC 规则嵌入      │   │
│  ┌─────────────┐             │  - 漏洞检测逻辑      │   │
│  │  数据库     │             └─────────────────────┘   │
│  │  (SQLite)   │                                       │
│  └─────────────┘                                       │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

我的目标：**提取扫描引擎中嵌入的全部 POC 规则**。

## 0x03 第一阶段：信息收集

### 对话 1：确定规则存储位置

**我**：我想从这个扫描器中提取漏洞检测规则，规则应该是 YAML 格式的 POC。帮我分析一下可能的存储位置。

**AI**：好的，让我们先分析几种可能的存储方式：

1. 1. **数据库存储**：规则可能在 SQLite/MySQL 中
2. 2. **文件系统**：独立的 YAML 文件
3. 3. **编译嵌入**：打包进 Go 二进制
4. 4. **远程加载**：从服务器动态获取

让我们逐一排查。先看数据库：

```
docker exec web-container sqlite3 /data/db.sqlite3 ".tables"
```

**执行结果**：

```
sys_plugin          vuln_category       scan_task
user_plugin         ...
```

**AI**：有 `sys_plugin` 表，让我们看看里面有什么：

```
docker exec web-container sqlite3 /data/db.sqlite3 \
"SELECT COUNT(*) FROM sys_plugin;"
```

**执行结果**：

```
5500
```

**AI**：有 5500 条插件记录！让我们看看表结构：

```
docker exec web-container sqlite3 /data/db.sqlite3 \
"PRAGMA table_info(sys_plugin);"
```

**执行结果**：

```
0|id|INTEGER|1||1
1|plugin_key|VARCHAR(255)|1||0
2|name|VARCHAR(255)|1||0
3|category|VARCHAR(50)|1||0
4|version|VARCHAR(36)|0||0
```

**AI**：只有元数据（key、name、type），没有 POC 内容字段。规则不在数据库中。

### 对话 2：检查文件系统

**我**：那看看文件系统里有没有。

**AI**：

```
docker exec scanner-engine find / -name "*.yml" -o -name "*.yaml" 2>/dev/null | head -20
```

**执行结果**：

```
（空）
```

**AI**：没有独立的 YAML 文件。让我们检查二进制：

```
docker exec scanner-engine ls -lh /app/scanner
```

**执行结果**：

```
-rwxr-xr-x 1 root root 156M Dec 30 06:10 /app/scanner
```

**AI**：156MB 的 Go 二进制，很可能规则就嵌入在里面。让我们验证：

```
docker exec scanner-engine strings /app/scanner | grep -i "poc\|rule\|yaml" | head -20
```

**执行结果**：

```
plugins/pocs/
plugins/pocs/cve-2021-44228.yml
plugins/pocs/cve-2022-22965.yml
...
```

**AI**：确认了！规则以 yml 文件的形式嵌入在二进制中。让我们统计数量：

```
docker exec scanner-engine strings /app/scanner | \
  grep -oE "plugins/pocs/[a-zA-Z0-9_-]+\.yml" | \
sort -u | wc -l
```

**执行结果**：

```
5200
```

**结论**：5200 个 POC 文件嵌入在二进制中，但只能看到文件名，看不到内容（因为是压缩存储的）。

## 0x04 第二阶段：尝试直接提取（失败）

### 尝试 1：binwalk 分析

**我**：能不能用 binwalk 把这些文件提取出来？

**AI**：可以试试。先把二进制复制出来：

```
docker cp scanner-engine:/app/scanner /tmp/scanner
binwalk /tmp/scanner | head -50
```

**执行结果**：

```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             ELF, 64-bit LSB executable, AMD x86-64
4243407       0x40BFCF        gzip compressed data
30590113      0x1D2C4A1       LZ4 compressed data, legacy
30590270      0x1D2C53E       LZ4 compressed data, legacy
...
92520048      0x583BE70       End of Zip archive
```

**AI**：发现了 gzip、LZ4、Zip 等压缩数据。尝试提取：

```
binwalk -e /tmp/scanner -C /tmp/extracted/
ls /tmp/extracted/
```

**执行结果**：

```
_scanner.extracted/
```

```
ls /tmp/extracted/_scanner.extracted/
```

**执行结果**：

```
40BFCF.gz  583BE70.zip  ...
```

**AI**：让我们看看提取出了什么：

```
file /tmp/extracted/_scanner.extracted/*
```

**执行结果**：

```
40BFCF.gz: gzip compressed data
583BE70.zip: Zip archive data (时区数据)
...
```

**我**：解压看看有没有 POC？

**AI**：

```
zcat /tmp/extracted/_scanner.extracted/40BFCF.gz | strings | grep -i "name:\|rules:" | head -10
```

**执行结果**：

```
（空）
```

**结论**：❌ binwalk 提取的都是时区数据、图片等资源，不是 POC。

### 尝试 2：搜索原始 YAML 内容

**我**：直接在二进制里搜索 YAML 内容呢？

**AI**：

```
strings /tmp/scanner | grep -E "^name:\s*poc-" | head -10
```

**执行结果**：

```
（空）
```

**AI**：没有找到。说明 POC 内容确实是压缩存储的。让我们搜索一些 YAML 特征：

```
python3 << 'EOF'
with open('/tmp/scanner', 'rb') as f:
    data = f.read()

patterns = [b'name: poc-', b'rules:', b'requests:']
for p in patterns:
    idx = data.find(p)
if idx > 0:
print(f"Found '{p.decode()}' at offset {idx}")
print(data[idx:idx+200].decode('utf-8', errors='ignore'))
EOF
```

**执行结果**：

```
Found 'rules:' at offset 85829887
rules:
  braces:
    level: error
    max-spaces-inside: 1
  brackets:
    level: error
...
```

**AI**：这是 YAML lint 的配置规则，不是 POC。POC 内容确实被压缩了。

**结论**：❌ 无法直接从二进制中提取 POC 内容。

### 尝试 3：zstd 解压

**我**：binwalk 显示有 zstd 压缩块，试试解压？

**AI**：

```
# 找 zstd 块
python3 << 'EOF'
with open('/tmp/scanner', 'rb') as f:
    data = f.read()

zstd_magic = b'\x28\xb5\x2f\xfd'
idx = 0
blocks = []
while True:
    idx = data.find(zstd_magic, idx)
if idx == -1:
break
    blocks.append(idx)
    idx += 1

print(f"Found {len(blocks)} zstd blocks at: {blocks}")
EOF
```

**执行结果**：

```
Found 5 zstd blocks at: [16555387, 16651237, 16654105, 49156610, 184577972]
```

**AI**：尝试解压：

```
ddif=/tmp/scanner bs=1 skip=49156610 count=5000000 of=/tmp/zstd_block.zst
zstd -d /tmp/zstd_block.zst -o /tmp/zstd_out.bin
```

**执行结果**：

```
zstd: /tmp/zstd_block.zst : Decoding error (36) : Unsupported frame parameter
```

**结论**：❌ zstd 块不是标准格式，可能是自定义压缩或加密。

### 尝试 4：gRPC 接口

**我**：有没有 gRPC 接口可以获取 POC？

**AI**：让我们看看扫描引擎暴露了哪些端口：

```
docker exec scanner-engine netstat -tlnp
```

**执行结果**：

```
tcp  0  0  10.0.0.2:9090  0.0.0.0:*  LISTEN  -
```

**AI**：9090 端口是 gRPC 服务。安装 grpcurl 测试：

```
# 下载 grpcurl
curl -sLO https://github.com/fullstorydev/grpcurl/releases/download/v1.8.9/grpcurl_1.8.9_linux_x86_64.tar.gz
tar xzf grpcurl_1.8.9_linux_x86_64.tar.gz
docker cp grpcurl scanner-engine:/tmp/

# 列出服务
docker exec scanner-engine /tmp/grpcurl -plaintext 10.0.0.2:9090 list
```

**执行结果**：

```
Failed to list services: server does not support the reflection API
```

**AI**：服务端没有启用反射。我们需要 proto 文件。从反编译的代码中找到了接口定义：

```
service VulnScanner {
rpc Scan(ScanRequest) returns (ScanResult);
rpc GetTaskStatus(TaskRequest) returns (TaskStatus);
// 没有获取 POC 列表的接口！
}
```

**结论**：❌ gRPC 接口没有提供获取 POC 内容的方法。

## 0x05 第三阶段：内存提取（成功）

经过前面的失败尝试，AI 提出了一个关键洞察：

**AI**：我们换个思路。无论 POC 如何存储，在执行扫描时必须解压到内存中。我们可以从运行时内存中提取。

### 分析进程内存

**我**：怎么做？

**AI**：先找到进程：

```
docker exec scanner-engine pgrep -f scanner
```

**执行结果**：

```
1
```

**AI**：PID 是 1（容器内主进程）。看看内存布局：

```
docker exec scanner-engine cat /proc/1/maps | head -30
```

**执行结果**：

```
00400000-00402000 r--p 00000000 00:91 12345  /app/scanner
00402000-04000000 r-xp 00002000 00:91 12345  /app/scanner
04000000-0a000000 r--p 03d66000 00:91 12345  /app/scanner
0a000000-0a001000 r--p 0aeb3000 00:91 12345  /app/scanner
0a001000-0b000000 rw-p 0aeb4000 00:91 12345  /app/scanner
0b000000-0c000000 rw-p 00000000 00:00 0
0e000000-0e100000 rw-p ...