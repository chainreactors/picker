---
title: SkillSentinel — Skill 安全扫描哨兵
url: https://mp.weixin.qq.com/s/KvufZmYaeSFl1Prl626B7A
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:04:04.297224
---

# SkillSentinel — Skill 安全扫描哨兵

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/bfbRn7oUmpL0bH1Uef8Aljh6yYf4ejR3aCiae9cw8M1On0AfOSRsbh53crJUndHNta7zoicCcQJ7XiahLgsYe3zWSWupJe6cyib42h0Nun5SsfM/0?wx_fmt=jpeg)

# SkillSentinel — Skill 安全扫描哨兵

摸鱼信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz/ZaoI13zBQuevMHz8QReZjgT2m0icnNdpsiaKd1ODUxtTycI2KMx26KcYbr8Mm6ZLwU4KSQS4fIhY0qpibrFuIhvUg/640?wx_fmt=bmp&from=appmsg)

# SkillSentinel — Skill 安全扫描哨兵

SkillSentinel 是 Skill 生态的"入口门禁"，在 Skill 安装、加载、启用之前执行自动化安全审计。

**定位不是通用 SAST，不是运行时沙箱，而是 Skill 生态里的轻量安全网关。**

## 在 Claude Code 中使用

其它下载方法参考：魔塔社区下载（推荐）

### 1. 安装到 Claude Code

```
# git仓库下载
git clone https://github.com/wpsec/skills.git ~/.claude/skills/skill-sentinel

# 或者软链接已有项目
ln -s /path/to/Skill-Sentinel ~/.claude/skills/skill-sentinel

# 安装依赖
cd ~/.claude/skills/skill-sentinel && pip install -r requirements.txt
```

codex 同理

### 2. 重启 Claude Code

Skill 安装后需要**重启客户端**才能被 Claude Code 发现。

### 3. 调用方式

安装后可通过以下方式调用：

| 方式 | 示例 | 说明 |
| --- | --- | --- |
| 斜杠命令 | `/skill-sentinel` | 初始化扫描所有已安装 Skill |
| 自然语言 | "扫描我的 Skill 安全性" | Claude Code 自动识别并调用 |
| 自然语言 | "检查 ~/.claude/skills/ 下有没有恶意 Skill" | 同上 |
| 自然语言 | "扫描 /path/to/skill 这个 Skill" | 扫描单个 Skill |

### 4. 可用命令

```
# 初始化扫描（扫描所有已安装 Skill）
/skill-sentinel

# 扫描指定目录
cd ~/.claude/skills/skill-sentinel && python3 -m skill_sentinel --scan-dir /path/to/skills

# 扫描单个 Skill
cd ~/.claude/skills/skill-sentinel && python3 -m skill_sentinel /path/to/skill
```

![](https://mmbiz.qpic.cn/mmbiz_png/bfbRn7oUmpLgzFazRsIz51HlcEQWNRsZ39dsOTBwicpmYmLjIDmgVNMy8icEIb9c31icVnP7NAJxgIxwYLCFY8r9leGAibH9PxyibXiabhLChuickM/640?wx_fmt=png&from=appmsg)

## 命令行使用

如果不想安装为 Claude Code Skill，也可以直接在终端使用：

```
# 安装依赖
pip install -r requirements.txt

# 扫描 Skill（终端输出）
# 初始化安全基线（扫描所有已安装 Skill）
python3 -m skill_sentinel --init

# 扫描单个 Skill（终端输出）
python3 -m skill_sentinel /path/to/skill

# JSON 输出
python3 -m skill_sentinel /path/to/skill --json

# 导出报告
python3 -m skill_sentinel /path/to/skill -o report.json

# 使用自定义规则
python3 -m skill_sentinel /path/to/skill --rules my_rules.py
```

### 作为 Python 库

```
from skill_sentinel import scan_skill

result = scan_skill("/path/to/skill")
print(result["risk_level"])   # "allow" | "review" | "block"
print(result["risk_score"])   # 0-100+
```

## 扫描流程

```
新 Skill 安装/加载
  │
  ▼
发现 Skill 根目录 → 解析 SKILL.md
  │
  ▼
构建资产图（入口→引用→脚本→配置→压缩包→间接依赖）
  │
  ▼
规则扫描（839 条正则规则）
  │
  ▼
风险评分 → allow / review / block
  │
  ▼
输出证据（文件:行号 + 规则 + 原因 + 建议）
```

## 风险分类

| # | 分类 | 典型检测项 |
| --- | --- | --- |
| 1 | 提示注入 | 忽略前置指令、角色扮演劫持、AI 行为篡改 |
| 2 | 数据外发 | HTTP 请求、Webhook、邮件、FTP 上传 |
| 3 | 提权与越权 | sudo、setuid、capabilities、容器的逃逸 |
| 4 | 持久化与自启动 | crontab、systemd、注册表、LaunchAgent |
| 5 | 文件破坏与目录篡改 | rm -rf、删除/覆写关键文件、chmod 777 |
| 6 | 供应链投毒 | curl |
| 7 | 反弹Shell/后门 | socket+dup2、SSH 隧道、ngrok/frp 内网穿透 |
| 8 | 隐蔽下载与远程执行 | eval/exec、base64 解码执行、subprocess |
| 9 | 敏感信息泄露 | 硬编码密钥、.env 读取、SSH 私钥、云凭证 |
| 10 | 混淆与遮蔽行为 | chattr、nohup、screen/tmux 隐藏、免杀 |

## 规则资产

共计 **839 条**正则规则，分三个文件，覆盖 10 大风险分类和 14 个 APT 攻击技术领域。

### 规则文件概览

| 文件 | 规则数 | 定位 | 适用场景 |
| --- | --- | --- | --- |
| `rules/total_rules.py` | 312 | 全高危操作扫描 | 覆盖面广，适合首次审计 |
| `rules/precise_rules.py` | 288 | 恶意高危精确扫描 | 误报更低，适合日常门禁 |
| `rules/apt_rules.py` | 239 | APT 级高级威胁检测 | 补充盲区，适合深度审计 |

### `rules/total_rules.py` 覆盖（312 条，全高危操作扫描）

| # | 分类 | 规则数 | 严重度分布 | 典型检测 |
| --- | --- | --- | --- | --- |
| 1 | 提示注入 | 17 | low:17 | ignore all instructions、角色扮演、人格设定、升级伪装 |
| 2 | 数据外发 | 13 | med:6 low:7 | HTTP 请求、FTP 上传、SMTP 发信、Telegram/Webhook 外发 |
| 3 | 提权与越权 | 12 | high:8 low:4 | sudo ALL=、setuid、cap\_set\_proc、内核模块加载 |
| 4 | 持久化与自启动 | 11 | high:5 low:6 | crontab 写入、systemctl enable、注册表 Run、LaunchAgent |
| 5 | 文件破坏与目录篡改 | 28 | critical:3 high:10 low:15 | DROP TABLE、rm -rf /、dd of=/dev/sda、chmod 777 |
| 6 | 供应链投毒 | 11 | high:6 med:5 | curl |
| 7 | 反弹Shell/后门 | 14 | critical:2 high:5 med:7 | socket+dup2、ngrok、SSH -R/-L/-D 隧道、frp 内网穿透 |
| 8 | 隐蔽下载与远程执行 | 159 | critical:5 high:12 med:9 low:133 | os.system、subprocess、eval/exec、pickle.loads、base64 -d |
| 9 | 敏感信息泄露 | 41 | high:2 low:39 | 硬编码密码/token/api\_key、读取 .env、SSH 私钥、AWS/GCloud 凭证 |
| 10 | 混淆与遮蔽行为 | 6 | low:6 | chattr +i/a、nohup &、disown、screen -dmS、tmux new-session -d |

### `rules/precise_rules.py` 覆盖（288 条，恶意高危精确扫描）

| # | 分类 | 规则数 | 严重度分布 | 典型检测 |
| --- | --- | --- | --- | --- |
| 1 | 提示注入 | 12 | low:12 | ignore previous instructions、伪装角色、无视系统提示 |
| 2 | 数据外发 | 5 | med:2 low:3 | 上传到 pastebin/transfer.sh、SCP 外发、rsync 外发 |
| 3 | 提权与越权 | 19 | high:17 low:2 | sudo su -、setuid、SUID shell、CVE 漏洞利用、UAC 绕过 |
| 4 | 持久化与自启动 | 13 | high:8 low:5 | @reboot cron、systemctl enable、注册表 Run、LaunchDaemon |
| 5 | 文件破坏与目录篡改 | 35 | critical:7 high:15 low:13 | DROP DATABASE、rm -rf / --no-preserve-root、shred -zu |
| 6 | 供应链投毒 | 9 | high:6 med:3 | pip install --index-url、npm install -g --unsafe-perm、git push --force |
| 7 | 反弹Shell/后门 | 39 | critical:18 high:13 med:8 | Bash TCP 反弹Shell、MSFVenom、CobaltStrike、PHP一句话木马 |
| 8 | 隐蔽下载与远程执行 | 131 | critical:10 high:13 med:3 low:105 | xp\_cmdshell、PowerShell bypass、execute\_script、编码/加密后执行 |
| 9 | 敏感信息泄露 | 17 | high:1 low:16 | 读取 /etc/shadow、SSH 私钥、AWS credentials、kubeconfig |
| 10 | 混淆与遮蔽行为 | 8 | critical:5 high:3 | Windows Defender 排除路径、关闭实时监控、免杀 |

### 三文件汇总

| # | 分类 | total\_rules | precise\_rules | apt\_rules | 合计 |
| --- | --- | --- | --- | --- | --- |
| 1 | 提示注入 | 17 | 12 | 34 | 63 |
| 2 | 数据外发 | 13 | 5 | 22 | 40 |
| 3 | 提权与越权 | 12 | 19 | 6 | 37 |
| 4 | 持久化与自启动 | 12 | 13 | 4 | 28 |
| 5 | 文件破坏与目录篡改 | 28 | 35 | 1 | 64 |
| 6 | 供应链投毒 | 11 | 9 | 4 | 24 |
| 7 | 反弹Shell/后门 | 14 | 39 | 10 | 63 |
| 8 | 隐蔽下载与远程执行 | 159 | 131 | 124 | 415 |
| 9 | 敏感信息泄露 | 41 | 17 | 11 | 69 |
| 10 | 混淆与遮蔽行为 | 6 | 8 | 23 | 36 |
|  | **合计** | **312** | **288** | **239** | **839** |

### 严重程度分布

| 等级 | total\_rules | precise\_rules | apt\_rules | 合计 | 评分权重 |
| --- | --- | --- | --- | --- | --- |
| critical | 10 | 40 | 4 | 54 | 25 分/条 |
| high | 48 | 47 | 22 | 117 | 10 分/条 |
| medium | 27 | 16 | 52 | 96 | 3 分/条 |
| low | 227 | 185 | 161 | 572 | 1 分/条 |

### APT 攻击技术覆盖（`rules/apt_rules.py`）

| # | APT 技术 | 规则数 | MITRE ATT&CK | 典型检测 |
| --- | --- | --- | --- | --- |
| 1 | LOLBin 利用 | 55 | T1218 | certutil, mshta, regsvr32, osascript, systemd-run |
| 2 | 高级混淆 | 28 | T1027 | 多级编码链、字符串拼接、Unicode 混淆、动态代码生成 |
| 3 | 无文件执行 | 11 | T1620 | memfd\_create, /dev/shm, mmap, /proc/self/fd |
| 4 | 隐蔽 C2 | 24 | T1090/T1572 | DNS 隧道、社交媒体 C2、死点解析器、加密隧道 |
| 5 | 供应链高级攻击 | 13 | T1195 | 版本混淆、extra-index-url、postinstall 投毒 |
| 6 | AI 高级提示注入 | 37 | — | 工具调用劫持、无授权操作、静默执行、多语言注入 |
| 7 | 时间延迟触发 | 11 | T1654 | time.sleep、调度器、日期条件、环境检测 |
| 8 | 数据批量窃取 | 10 | T1041 | 分段传输、编码外传、隐写术 |
| 9 | 防御规避 | 14 | T1562 | SELinux/Defender 禁用、SIP 绕过、审计关闭 |
| 10 | 横向移动 | 12 | T1021 | SSH pass、WinRM、PsExec、Impacket |
| 11 | 凭据转储 | 8 | T1003 | LSASS dump、DPAPI、浏览器凭据 |
| 12 | 容器逃逸 | 7 | T1611 | cgroup release\_agent、docker.sock 挂载 |
| 13 | 内核模块攻击 | 5 | T1547 | insmod、内核参数篡改 |
| 14 | Python 代码注入 | 8 | — | AST 操纵、字节码注入、猴子补丁 |

### 规则格式

```
MALICIOUS_PATTERNS = {
    r"(?i)\bos\.system\s*\(": "执行系统命令 (os.system)",
    r"(?i)\brm\s+-rf\s+/": "删除根目录",
    # ...
}
```

### 自定义规则

通过 `--rules` 参数指定自定义规则文件：

```
python3 -m skill_sentinel /path/to/skill --rules my_rules.py
```

## 输出结构

```
{
  "skill_name": "example-skill",
  "skill_path": "/path/to/skill",
  "scan_time": "2026-06-22T16:49:17",
  "risk_level": "block",
  "risk_score": 94,
  "summary": {
    "total_files": 123,
    "scanned_files": 159,
    "total_findings": 57,
    "categories": {"8": 36, "5": 18, "3": 3},
    "severity_counts": {"critical": 0, "high": 3, "medium": 5, "low": 49}
  },
  "findings": [
    {
      "file": "/path/to/script.py",
      "line": 42,
      "rule": "执行系统命令 (subprocess)",
      "severity": "medium",
      "category": 8,
      "match": "subprocess.run"
    }
  ],
  "evidence": [
    {
      "file": "/path/to/script.py",
      "line": 42,
      "rule": "执行系统命令 (subprocess)",
      "category": "隐蔽下载与远程执行",
      "severity": "medium",
      "reason": "第 42 行匹配到...