---
title: 让Claude Code写了个运维健康检查的Skill还挺好用的
url: https://mp.weixin.qq.com/s/VMmuxM4DDiSuEYWR8QG94w
source: Doonsec's feed
date: 2026-01-21
fetch_date: 2026-01-22T03:34:12.246867
---

# 让Claude Code写了个运维健康检查的Skill还挺好用的

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6cNzMD9ovmP9MISB2eiaUMKK8yk3Zy39FLibJekiaiatuS06GibponLvPXPfeXobuhy1BljAC8U7KgMxMIX3edkic2XQ/0?wx_fmt=jpeg)

# 让Claude Code写了个运维健康检查的Skill还挺好用的

原创

xiejava
xiejava

fullbug

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6cNzMD9ovmP9MISB2eiaUMKK8yk3Zy39FBvrlbiaTJwVpXpHzJpbHfQlWHNbKce2b6wLkIVokue1fibRxH9Co3XZQ/640?wx_fmt=jpeg)

手头上有几台服务器，经常要对服务器进行健康检查、安全检查等。这几天让ClaudeCode自己写了个Skill这样就一句话活就让AI给干了。本文详细介绍了如何使用Claude Code AI辅助开发工具，从零开始构建一个生产级运维健康检查的Skill。重点阐述了整体架构设计、核心功能实现细节以及实际应用效果。该系统采用模块化设计，提供三大检查模块（基础健康检查、深度安全审计、Docker容器监控），支持双格式输出（Markdown人工可读 + JSON机器可处理），具有良好的可扩展性和兼容性。

## 一、背景与设计目标

### 1.1 实际需求

在日常运维工作中，我们需要对多台服务器进行健康检查，涵盖系统资源、Docker容器状态、安全指标等多个维度。虽然市面上有很多成熟的监控方案（如Prometheus、Grafana、Zabbix等），但在以下场景中，我们需要一个轻量级、快速部署的检查工具：

* **日常巡检：每天对服务器进行快速健康扫描**
* **安全审计：定期检查异常进程、可疑网络连接、文件系统安全**
* **容器监控：检查Docker容器运行状态、资源使用情况**
* **问题排查：当系统出现问题时，快速获取当前状态信息**

### 1.2 设计目标

基于上述需求，我设定了以下设计目标交给了Claude Code：

**核心特性**：

* ✅ **轻量级部署**：基于Bash脚本，无需额外依赖，远程执行无需安装
* ✅ **双格式输出**：同时生成Markdown（人工阅读）和JSON（机器处理）格式
* ✅ **模块化架构**：三大检查模块独立运行，可按需组合
* ✅ **状态可视化**：使用emoji（✅正常/⚠️警告/❌严重）直观展示
* ✅ **广泛兼容性**：支持bash 3.2+（macOS默认版本），适配主流Linux发行版

## 二、整体架构设计

### 2.1 系统架构

Claude Code自动帮我设计了整体架构
运维健康检查系统采用模块化设计，包含三个独立的检查模块：

| 模块名称 | 脚本文件 | 功能定位 | 核心检查项 |
| --- | --- | --- | --- |
| **基础健康检查** | health-check.sh | 日常巡检、快速评估 | 系统资源、内存、磁盘、网络、服务状态、基础安全 |
| **深度安全检查** | security-check.sh | 安全审计、威胁检测 | 异常进程、可疑连接、文件安全、账户安全、系统完整性 |
| **Docker容器监控** | docker-check.sh | 容器环境管理 | 容器状态、资源使用、镜像管理、存储空间 |

**设计原则**：

* **独立性：每个脚本可单独运行，互不依赖**
* **一致性：统一的输出格式和状态指示**
* **可扩展性：易于添加新的检查项或模块**
* **远程友好：支持SSH管道执行，无需远程安装**

### 2.2 文件结构

|  |
| --- |
| ``` host-manage/ ├── skills/ops-health-check/ │   ├── SKILL.md                    # Skill定义和使用文档 │   └── scripts/ │       ├── health-check.sh         # 基础健康检查脚本 │       ├── security-check.sh       # 深度安全检查脚本 │       ├── docker-check.sh         # Docker监控脚本 │       └── lib/ │           └── output.sh           # 输出格式化库（核心） ├── docs/plans/ │   ├── 2025-01-17-ops-health-check-design.md     # 整体设计文档 │   └── 2025-01-18-json-output-design.md          # JSON输出设计 └── health-reports/                 # 检查报告输出目录     ├── health-check-*.md           # Markdown格式报告     ├── health-check-*.json         # JSON格式数据     ├── security-check-*.md     ├── security-check-*.json     ├── docker-check-*.md     └── docker-check-*.json ``` |

## 三、核心功能实现

Claude Code自动帮我实现了所有的功能

### 3.1 基础健康检查模块（health-check.sh）

这是日常运维使用最频繁的模块，专注于快速评估系统整体健康状况。

#### 3.1.1 系统运行时间和负载检查

**检查目的**：了解系统运行时长和当前负载压力

**实现逻辑**：

|  |
| --- |
| ``` # 获取系统运行时间 uptime_output=$(uptime) uptime_clean=$(echo"$uptime_output" | sed 's/^ *//g')  # 兼容不同系统的uptime输出格式 uptime_str=$(uptime -p 2>/dev/null || \ echo"$uptime_clean" | awk -F'up ''{print $2}' | awk -F',''{print $1}')  # 提取负载平均值（1分钟、5分钟、15分钟） load_str=$(echo"$uptime_clean" | awk -F'load average:''{print $2}' | sed 's/^ *//g') load_1min=$(echo$load_str | awk '{print $1}' | sed 's/,//') load_5min=$(echo$load_str | awk '{print $2}' | sed 's/,//') load_15min=$(echo$load_str | awk '{print $3}')  # 判断负载状态 load_status=$(check_load_status "$load_1min""$CPU_WARNING""$CPU_CRITICAL") ``` |

**状态判断函数**：

|  |
| --- |
| ``` check_load_status() { local load=$1 local warning=$2 local critical=$3  # 使用bc进行浮点数比较 if (( $(echo"$load >= $critical" | bc -l) )); then echo"critical" elif (( $(echo"$load >= $warning" | bc -l) )); then echo"warning" else echo"ok" fi } ``` |

**关键点**：

* 使用`bc -l`进行浮点数比较，兼容不同系统
* 兼容`uptime -p`命令（human-readable格式）不可用的情况
* 同时收集三个时间维度的负载数据，用于趋势分析

#### 3.1.2 内存使用检查

**检查目的**：监控内存和swap使用情况，防止内存耗尽

**实现逻辑**：

|  |
| --- |
| ``` # 获取内存信息（单位：MB） memory_info=$(free -m | grep Mem) mem_total=$(echo$memory_info | awk '{print $2}') mem_used=$(echo$memory_info | awk '{print $3}') mem_avail=$(echo$memory_info | awk '{print $7}')  # available列更准确 mem_percent=$(awk "BEGIN {printf \"%.1f\", $mem_used * 100 / $mem_total}")  # Swap检查 swap_info=$(free -m | grep Swap) swap_total=$(echo$swap_info | awk '{print $2}') swap_used=$(echo$swap_info | awk '{print $3}')  if [ "$swap_total" -gt 0 ]; then     swap_percent=$(awk "BEGIN {printf \"%.1f\", $swap_used * 100 / $swap_total}") else     swap_percent=0 fi  # 状态判断 if (( $(echo"$mem_percent >= $MEMORY_CRITICAL" | bc -l) )); then     mem_status="critical" elif (( $(echo"$mem_percent >= $MEMORY_WARNING" | bc -l) )); then     mem_status="warning" else     mem_status="ok" fi ``` |

**输出示例**：

|  |
| --- |
| ``` ### 内存使用 - **总内存**: 16384MB - **已使用**: 12500MB (76.3%) - **可用**: 3884MB - **Swap**: 256MB / 2048MB (12.5%) - **状态**: ⚠️ 警告 ``` |

**关键点**：

* 使用`free`命令的`available`列而非`free`列，更准确反映可用内存
* 同时检查swap使用率，高swap使用率通常意味着内存压力
* 支持自定义阈值配置（通过环境变量`MEMORY_WARNING`、`MEMORY_CRITICAL`）

#### 3.1.3 磁盘空间检查

**检查目的**：监控所有挂载点的磁盘使用情况，防止磁盘空间不足

**实现逻辑**：

|  |
| --- |
| ``` echo"### 磁盘空间" echo"| 挂载点 | 设备 | 容量 | 已用 | 可用 | 使用率 | 状态 |" echo"|--------|------|------|------|------|--------|------|"  # 遍历所有挂载点（排除临时文件系统） df -h | grep -vE '^Filesystem|tmpfs|overlay|none' | whileread -r line; do     device=$(echo$line | awk '{print $1}')     size=$(echo$line | awk '{print $2}')     used=$(echo$line | awk '{print $3}')     avail=$(echo$line | awk '{print $4}')     use_percent=$(echo$line | awk '{print $5}' | sed 's/%//')     mount=$(echo$line | awk '{print $6}')  # 判断状态 if [ "$use_percent" -ge "$DISK_CRITICAL" ]; then         status="critical"         emoji="❌" elif [ "$use_percent" -ge "$DISK_WARNING" ]; then         status="warning"         emoji="⚠️" else         status="ok"         emoji="✅" fi  # 输出Markdown表格行 echo"| $mount | $device | $size | $used | $avail | ${use_percent}% | $emoji |"  # 收集JSON数据     add_disk_data "$mount""device""$device"     add_disk_data "$mount""total_gb""$size"     add_disk_data "$mount""used_gb""$used"     add_disk_data "$mount""available_gb""$avail"     add_disk_data "$mount""used_percent""$use_percent"     add_disk_data "$mount""status""$status" done ``` |

**输出示例**：

|  |
| --- |
| ``` ### 磁盘空间 | 挂载点 | 设备 | 容量 | 已用 | 可用 | 使用率 | 状态 | |--------|------|------|------|------|--------|------| | / | /dev/sda1 | 100G | 45G | 55G | 45.0% | ✅ 正常 | | /data | /dev/sdb1 | 500G | 425G | 75G | 85.0% | ⚠️ 警告 | | /boot | /dev/sda2 | 1G | 250M | 750M | 25.0% | ✅ 正常 | ``` |

**关键点**：

* 自动过滤`tmpfs`、`overlay`等临时文件系统
* 支持多个挂载点，每个挂载点独立判断状态
* 使用整数比较（已去除百分号），提高性能
* 同时生成Markdown表格和JSON数组数据

#### 3.1.4 网络连接统计

**检查目的**：了解当前网络连接数量，快速发现异常连接

**实现逻辑**：

|  |
| --- |
| ``` # 使用ss命令替代netstat（更现代） ifcommand -v ss >/dev/null 2>&1; then # 总连接数     total_connections=$(ss -tn | wc -l)  # 外部连接数（排除本地回环）     external_connections=$(ss -tn | awk '{print $5}' | \         grep -v '127.0.0.1' | \         grep -v '::1' | \         cut -d':' -f1 | \         sort -u | \         wc -l)  # 监听端口数     listening_ports=$(ss -tln | wc -l) else # 降级到netstat     total_connections=$(netstat -tn 2>/dev/null | wc -l)     external_connections=$(netstat -tn 2>/dev/null | awk '{print $5}' | \         grep -v '127.0.0.1' | \         grep -v '::1' | \         cut -d':' -f1 | \         sort -u | \         wc -l)     listening_ports=$(netstat -tln 2>/dev/null | wc -l) fi  add_system_data "network_total_connections""$total_connections" add_system_data "network_external_connections""$external_connections" add_system_data "network_listening_ports""$listening_ports" ``` |

**关键点**：

* 优先使用`ss`命令（现代Linux推荐），降级到`netstat`
* 统计外部独立IP连接数，而非连接总数（更准确反映异常）
* 包含监听端口数量，便于发现未授权监听

#### 3.1.5 systemd服务状态检查

**检查目的**：检查系统服务运行状态，发现失败服务

**实现逻辑**：

|  |
| --- |
| ``` # 检查systemd是否可用 ifcommand -v systemctl >/dev/null 2>&1; then # 统计服务状态     running_services=$(systemctl list-units --type=service --state=running 2>/dev/null | \         grep 'loaded loaded' | wc -l)      failed_services=$(systemctl list-units --type=service --state=failed 2>/dev/null | \         grep 'loaded loaded' | wc -l)      enabled_services=$(systemctl list-unit-files --type=service --state=enabled 2>/dev/null | \         grep 'enabled' | wc -l)  # 获取失败服务列表 if [ "$failed_services" -g...