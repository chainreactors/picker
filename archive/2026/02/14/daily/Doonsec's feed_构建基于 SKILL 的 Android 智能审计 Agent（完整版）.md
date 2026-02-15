---
title: 构建基于 SKILL 的 Android 智能审计 Agent（完整版）
url: https://mp.weixin.qq.com/s/x20A5LwLXraO7EinTLXN5g
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:19:28.147173
---

# 构建基于 SKILL 的 Android 智能审计 Agent（完整版）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/unnlWdxxboPjUp22Cwc5ia5ub2d87MvD3bbxzuv8Cq1fOg8s869cpjD2kM5YGajjarTnKVUSice7icpl2YMUy74FuaNz9H1DtVqa0jetWhnK28/0?wx_fmt=jpeg)

# 构建基于 SKILL 的 Android 智能审计 Agent（完整版）

原创

牧之
牧之

从黑客到保安

![]()

在小说阅读器中沉浸阅读

# **一、简言**

在移动安全领域，完全依赖正则表达式的扫描容易产生海量误报，而完全依赖 AI 阅读代码又受限于上下文窗口和对复杂数据流的计算能力。

本文提出一种**基于 Skill 编排**的审计架构。该架构将传统的静态分析工具（Soot/FlowDroid）封装为 Agent 的“工具箱”，由 Claude Code 等大模型作为“大脑”进行调度与最终决策。

# **二、核心架构思路**

我们可以设计一个 **“漏斗式”** 的分析流水线：

1. **第一层：java代码和资源文件获取 (基础设施层)**

* Jadx反编译，获取伪码和AndroidManifest.xml

2. **第二层：基于模式匹配的快速筛选 (特征层)\***\*\*\*

* 先用 **Semgrep** 或 **Regex** 快速扫描反编译后的 Java 源码。
* 寻找特征：硬编码密钥、弱加密算法（ECB模式）、SQL 拼接字符串、Log 打印敏感信息。
* 分析AndroidManifest.xml中的暴露组件。

3. **第三层：Soot/FlowDroid 路径验证 (数据流层)**

* 针对第二层发现的“可疑点”，将其作为 Sink（污点汇聚点），进行定向的污点分析。确认用户输入（Source）是否真的能到达这里。

4. **第四层：AI 代码审计 (语义层)**

* 提取关键代码片段，喂给 LLM。
* 让 AI 判断：是否存在过滤逻辑？是否是误报？并生成修复建议。

具体架构图示如下：

![图片](https://mmbiz.qpic.cn/mmbiz_png/unnlWdxxboN70Lrqgjn274LiasQS2bpNdWcoiaQ77K2VRB5xZOrKJiaPUibibiagDZv07SwlZBCsPnBJTkTmW2FmicW1OrXMe6S2Y62heoWYK9VJ14/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

目录结构如下：

```
app-security-automation/├── CLAUDE.md          <-- 核心：Claude Code 的“大脑”配置├── SKILL.md           <-- 核心：详细的审计技能文档├── scripts/           <-- 脚本 (quick_scan.sh, analyze_candidates.py)├── tools/             <-- 工具 (flowdroid, android.jar)├── targetapks/        <-- 待测 APK└── files/             <-- 输出结果
```

# **三、详细工作流设计**

## **第一步：源码还原**

Agent 调用 `scripts/decompile.sh`。

将 APK 转换为 Java 伪代码。Agent 会特别关注 `--show-bad-code` 参数，确保即使反编译不完美也能获取尽可能多的逻辑信息。

## **第二步：快速锚定**

面对海量文件，AI 不可能逐行阅读。我们需要先找到“靶点”。

**Agent 调用 scripts/quick\_scan.sh**。基于特征库（如 `rawQuery`, `loadUrl`, `Runtime.exec`）进行快速扫描。产出一份包含文件路径和行号的 **“潜在风险列表”**。

## **第三步：污点分析与路径验证**

这是本架构的核心差异点。 正则只能看到“有点像漏洞”，Soot 才能证明“数据确实流过去了”。Agent 针对第二步发现的可疑点，调用 `scripts/analyze_candidates.py`。利用工具 Soot + FlowDroid 将第二步发现的 Sink 点（如 SQL 执行处）作为目标，追踪 Source 点（如 `getIntent`, `EditText`），计算是否存在一条从 Source 到 Sink 的通路。最后产出结构化的数据流报告。例如：“在 `LoginActivity.java` 中，变量 `username` 从 `Intent` 输入，未经净化直接流入 `rawQuery`。”

## **第四步：AI 智能裁决**

这是传统工具无法替代的环节。工具不懂业务逻辑（比如这个 SQL 拼接是否只是在查本地配置表？），但 AI 懂。

Agent 读取源码 + FlowDroid 报告，结合数据流证据和业务逻辑，判定是误报还是漏洞风险。

# 四、各个脚本的功能详解

## decompile.sh

代码内容如下：

```
#!/bin/bash
# 用法: ./scripts/decompile.sh <path_to_apk> <output_dir>
APK_PATH=$1OUTPUT_DIR=${2:-"../wsource_dump"} # 默认为 source_dump 目录# 建议：将 JADX_JAR 路径改为配置变量或相对路径，确保通用性JADX_JAR="../tools/jadx-1.5.3-all.jar"
if [ -z "$APK_PATH" ]; then    echo "Usage: $0 <apk_file> [output_dir]"    exit 1fi
if [ ! -f "$JADX_JAR" ]; then    echo "Error: JADX jar not found at $JADX_JAR"    exit 1fi
echo "[*] Starting Decompilation for $APK_PATH..."
# 清理旧目录，防止混淆if [ -d "$OUTPUT_DIR" ]; then    echo "[-] Cleaning old output directory..."    rm -rf "$OUTPUT_DIR"fi
# 执行 Jadx (针对 AI 优化的参数 + 强制 CLI 模式)# -cp "$JADX_JAR" jadx.cli.JadxCLI : 强制调用 CLI 主类，避免启动 GUIjava -Xmx4g -cp "$JADX_JAR" jadx.cli.JadxCLI \    -d "$OUTPUT_DIR" \    --show-bad-code \    --deobf \    --threads-count 4 \    --no-imports \    --comments-level none \    "$APK_PATH"
# 检查返回值if [ $? -eq 0 ]; then    echo "[+] Decompilation Successful! Output: $OUTPUT_DIR"
    # 验证目录结构，方便后续脚本定位 source_root    if [ -d "$OUTPUT_DIR/sources" ]; then        echo "[+] Source Root located at: $OUTPUT_DIR/sources"    else        # 某些旧版 jadx 可能会直接输出在根目录，做个兼容提示        echo "[!] Warning: 'sources' subdirectory not found. Check structure."    fielse    echo "[!] Decompilation With Errors."    exit 1fi
```

这个脚本 `decompile.sh` 是自动化安全审计流程中的**第一步**，其核心作用是**将 APK 文件还原为可读的 Java 源代码**。

以下是它的主要功能描述：

**1. 强制命令行模式 (Headless Automation)**

* **功能**: 通过 `-cp "$JADX_JAR" jadx.cli.JadxCLI` 显式调用 Jadx 的命令行接口类。
* **目的**: 防止在服务器、Docker 或没有图形界面的环境中误启动 Jadx 的 GUI 窗口，确保脚本能静默运行。

**2. 环境清理与初始化 (Clean Setup)**

* **功能**: 运行前检查输入参数，并执行 `rm -rf "$OUTPUT_DIR"`。
* **目的**: 确保每次反编译都是“干净”的，防止旧的扫描结果（残留文件）干扰本次分析，避免误报。

**3. 针对“机器阅读”优化的反编译配置**

脚本使用了一组特定的参数，生成的代码是给 **Grep** 或 **AI** 看的，而不是给人看的：

* `--show-bad-code`: **保留反编译失败的代码**。对于安全审计来说，即使代码反编译不完整（比如只有字节码结构），也可能包含关键的字符串或逻辑，不能直接丢弃。
* `--deobf`: **自动反混淆**。尝试给混淆过的变量（如 `a.b.c`）重命名为有意义的名字，便于后续分析。
* `--no-imports`: **移除 import 语句**。对于正则扫描和 AI 分析，`import` 语句通常是噪音，去掉可以减少文件体积和上下文干扰。
* `--comments-level none`: **移除注释**。去掉了 Jadx 生成的自动注释（如“// from class: ...”），让代码更纯净，减少 Token 消耗。

**4. 性能保障**

* `java -Xmx4g`: 分配 **4GB 内存**，防止反编译大型 APK（如 100MB+ 的应用）时发生 OOM（内存溢出）崩溃。
* `--threads-count 4`: 启用 **4 线程**并行处理，加快反编译速度。

**5. 输出结构验证**

* **功能**: 反编译结束后，自动检查 `$OUTPUT_DIR/sources` 目录是否存在。
* **目的**: 为下一步（Python 脚本分析）做检查。如果目录结构不对，提前报错，避免后续脚本因为找不到路径而瞎跑。

## quick\_scan.sh

代码内容如下：

```
#!/bin/bash
SOURCE_DIR=$1OUTPUT_CSV="../files/scan_candidates.csv" # 中间文件TEMP_DIR=$(mktemp -d)
if [ -z "$SOURCE_DIR" ]; then    echo "Usage: $0 <source_dir>"    exit 1fi
# 初始化 CSV 头echo "type,filepath,linenum,content" > "$OUTPUT_CSV"
echo "=== Android Security Quick Scan (Parallel Mode) ==="echo "Target: $SOURCE_DIR"
# 定义辅助函数：提取信息并写入 CSV# 参数: $1=漏洞类型, $2=输入文件process_results() {    local v_type=$1    local input_file=$2
    # 逐行读取 grep 结果 (格式: file:line:content)    # 使用 awk 处理冒号分隔，注意文件路径可能包含冒号的情况需要小心处理，    # 这里假设 standard grep output format: path:line:content    while read -r line; do        # 提取文件路径 (第一个冒号前)        filepath=$(echo "$line" | cut -d: -f1)        # 提取行号 (第二个冒号前)        linenum=$(echo "$line" | cut -d: -f2)        # 提取内容 (剩余部分)，移除可能的逗号以防破坏 CSV        content=$(echo "$line" | cut -d: -f3- | tr -d ',')
        echo "$v_type,$filepath,$linenum,$content" >> "$OUTPUT_CSV"    done < "$input_file"}
scan_sql() {    # 增加过滤条件，减少误报    grep -rnE "rawQuery|execSQL" "$SOURCE_DIR" | grep "+" | head -n 20 > "$TEMP_DIR/sql.raw"    process_results "SQL_INJECTION" "$TEMP_DIR/sql.raw"}
scan_secrets() {    # 排除 BuildConfig 和 R.java    grep -rnEi "api_key|access_token|secret_key|password =" "$SOURCE_DIR" | grep -vE "BuildConfig.java|R.java" | head -n 20 > "$TEMP_DIR/secrets.raw"    process_results "HARDCODED_SECRET" "$TEMP_DIR/secrets.raw"}
scan_webview() {    grep -rn "setJavaScriptEnabled" "$SOURCE_DIR" | head -n 20 > "$TEMP_DIR/webview.raw"    process_results "WEBVIEW_RISK" "$TEMP_DIR/webview.raw"}
scan_cmd_injection() {    # 扫描 Runtime.exec 或 ProcessBuilder    grep -rnE "Runtime\.getRuntime\(\)\.exec|ProcessBuilder" "$SOURCE_DIR" | head -n 20 > "$TEMP_DIR/cmd.raw"    process_results "CMD_INJECTION" "$TEMP_DIR/cmd.raw"}
scan_path_traversal() {    # 简单的文件操作扫描 (注意：这可能会有很多误报，需要 FlowDroid 过滤)    grep -rnE "new File\(|FileInputStream" "$SOURCE_DIR" | grep "+" | head -n 20 > "$TEMP_DIR/file.raw"    process_results "PATH_TRAVERSAL" "$TEMP_DIR/file.raw"}
# 并发执行scan_sql & PID1=$!scan_secrets & PID2=$!scan_webview & PID3=$!scan_cmd_injection & PID5=$!scan_path_traversal & PID6=$!
wait $PID1 $PID2 $PID3
echo "=== Scan Finished ==="echo "candidates saved to: $OUTPUT_CSV"# 同时也打印给人看cat "$OUTPUT_CSV" | column -t -s,
rm -rf "$TEMP_DIR"
```

这个脚本 是自动化安全审计流程中的**第二步**，接在反编译之后执行。

它的核心作用是**利用正则表达式（Regex）进行快速、粗粒度的“海选”**，从海量的源代码中定位出所有“疑似”漏洞的代码行，并生成结构化的 CSV 清单，供后续的深度分析工具 FlowDroid 使用。

以下是它的主要功能描述：

**1. 并行化正则扫描 (Parallel Grep Scanning)**

* **功能**: 同时启动多个后台进程 (`&`) 分别扫描不同类型的漏洞（SQL注入、硬编码密钥、WebView 风险等）。
* **目的**: 充分利用多核 CPU，极大缩短扫描时间。相比于串行执行 `grep`，这种方式在处理大型项目时效率倍增。

**2. 多维度漏洞模式匹配 (Pattern Matching)**

脚本内置了针对 Android 常见高危漏洞的检测规则：

* **SQL 注入 (`SQL_INJECTION`)**: 查找 `rawQuery` 或 `execSQL`，并尝试通过 `grep "+"` 筛选存在**字符串拼接**的代码行（拼接才是注入的根源）。
* **硬编码密钥 (`HARDCODED_SECRET`)**: 查找 `api_key`, `access_token` 等敏感关键词，同时**智能排除**`BuildConfig.java` 和 `R.java` 等自动生成的干扰文件。
* **命令注入 (`CMD_INJECTION`)**: 监测 `Runtime.exec` 和 `ProcessBuilder`，这是执行系统命令的高危入口。
* **WebView 风险 (`WEBVIEW_RISK`)**: 检查 `setJavaScriptEnabled`，这是开启 XSS 攻击面的常见配置。
* **路径遍历 (`PATH_TRAVERSAL`)**: 寻找 `new File` 或 `FileInputStream` 并伴随字符串拼接的操作。

**3. 数据清洗与结构化输出 (ETL)**

* 功能:

  定义了 `process_results`函数，将 `grep` 原始的输出（文件:行号:内容）解析并转换为标准的 CSV 格式：

+ `type`: 漏洞类别（如 SQL\_INJECTION）
+ `filepath`: 文件路径
+ `linenum`: 代码行号
+ `content`: 代码片段（并移除了可能破坏 CSV 结构的逗号）

* **目的**: 将非结构化的文本日志转换为机器可读的 **CSV...