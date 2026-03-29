---
title: 用 fail2ban 防御暴力破解的落地实践
url: https://mp.weixin.qq.com/s/cswNCsalhvILUxF-91OZ4w
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:34:18.194987
---

# 用 fail2ban 防御暴力破解的落地实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2I159AwKj54Jathl9cWUKLzkOsUomBjZz5GH9xdibE6sHdL1U9LUQfmH1HDSEpsThaibfNddWicVTxBd56x42fKJUSYicIgB7X6oNqfC1I8xr8g/0?wx_fmt=jpeg)

# 用 fail2ban 防御暴力破解的落地实践

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器中沉浸阅读

# 一、概述

### 1.1 背景介绍

暴力破解（Brute Force Attack）是最原始也是最有效的攻击手段之一。攻击者通过自动化工具对 SSH、Web 登录、数据库等服务进行大量密码尝试，直到命中正确的凭据。根据公网蜜罐数据统计，一台新上线的 Linux 服务器暴露 SSH 端口后，平均 5 分钟内就会收到第一次暴力破解尝试，每天被扫描数千次是常态。

暴力破解攻击的危害不仅在于密码被破解本身：

| 危害类型 | 具体说明 |
| --- | --- |
| 凭据泄露 | 弱密码被破解后攻击者获取系统权限 |
| 资源消耗 | 大量认证请求消耗 CPU 和内存 |
| 日志膨胀 | auth.log/secure 日志文件快速增长 |
| 影响正常访问 | 连接数被恶意请求占满 |
| 合规风险 | 未防护暴力破解不符合等保要求 |

#### fail2ban 的工作原理

fail2ban 是一个入侵防御框架，核心机制是日志监控 + 自动封禁：

```
日志文件               fail2ban                    防火墙
(auth.log)              引擎
                          |
  新日志行 ------>  Filter（正则匹配）
                          |
                    匹配失败特征？
                      |       |
                     是      否（忽略）
                      |
                  计数器 +1
                      |
                  超过阈值？
                    |      |
                   是     否（继续计数）
                    |
              Action（执行封禁）  ------>  iptables/nftables
                    |                      添加 DROP 规则
              记录封禁日志
                    |
              启动解封定时器  ------>  到期自动解封
```

核心概念：

* **Filter**：定义匹配规则的正则表达式，从日志中识别失败的认证尝试
* **Jail**：一个监控单元，包含 filter + action + 参数（阈值/时间窗/封禁时间）
* **Action**：匹配后执行的操作，通常是防火墙封禁
* **Ban/Unban**：封禁和解封操作

### 1.2 与其他防御手段对比

| 工具 | 原理 | 优势 | 劣势 |
| --- | --- | --- | --- |
| fail2ban | 日志正则匹配 | 通用性强，支持任意日志格式的服务 | 依赖日志实时写入 |
| DenyHosts | 解析 /etc/hosts.deny | 简单轻量 | 仅支持 SSH，项目已不活跃 |
| SSHGuard | 日志解析 | 多协议支持，低资源占用 | 自定义规则不如 fail2ban 灵活 |
| CrowdSec | 日志分析 + 社区威胁情报 | 共享封禁列表，现代架构 | 部署复杂，需要联网同步 |
| 防火墙限速 | 连接频率限制 | 不依赖日志 | 无法区分正常和恶意请求 |

fail2ban 在单机防护场景下是最成熟的选择：配置灵活、文档丰富、社区活跃、资源消耗低。对于大规模集群，可以考虑 CrowdSec 或 fail2ban + 集中式日志的组合方案。

### 1.3 适用场景

* SSH 服务暴力破解防护
* Nginx/Apache 的 HTTP Basic Auth 暴力破解防护
* Web 应用登录接口的暴力破解防护
* 恶意扫描（路径遍历、漏洞探测）过滤
* MySQL/PostgreSQL 远程登录保护
* 邮件服务（Postfix/Dovecot）暴力破解防护
* 自定义应用日志的异常行为检测

### 1.4 环境要求

| 组件 | 版本要求 | 说明 |
| --- | --- | --- |
| 操作系统 | Ubuntu 24.04 LTS / Rocky Linux 9.5 | 内核 6.12+ |
| fail2ban | 1.1.x | 当前稳定版 |
| Python | 3.12+ | fail2ban 运行依赖 |
| iptables/nftables | 系统自带 | 封禁后端 |
| firewalld | 2.x（可选） | Rocky Linux 默认 |
| rsyslog/systemd-journald | 系统自带 | 日志来源 |

```
# Ubuntu 24.04 安装
sudo apt update
sudo apt install -y fail2ban

# Rocky Linux 9.5 安装（需要 EPEL 源）
sudo dnf install -y epel-release
sudo dnf install -y fail2ban fail2ban-firewalld

# 检查版本
fail2ban-client version
# Fail2Ban v1.1.0

# 检查服务状态
sudo systemctl status fail2ban
```

---

## 二、详细步骤

### 2.1 配置文件结构

fail2ban 的配置文件层级：

```
/etc/fail2ban/
├── fail2ban.conf          # 全局配置（日志级别、socket 路径等）
├── fail2ban.local         # 全局配置覆盖（自定义项写在这里）
├── jail.conf              # 默认 jail 定义（不要直接修改）
├── jail.local             # jail 自定义配置（所有自定义都写在这里）
├── jail.d/                # jail 片段配置目录
│   └── defaults-debian.conf
├── filter.d/              # filter 正则定义
│   ├── sshd.conf
│   ├── nginx-http-auth.conf
│   └── ...
├── action.d/              # action 动作定义
│   ├── iptables-multiport.conf
│   ├── nftables-multiport.conf
│   ├── firewallcmd-rich-rules.conf
│   └── ...
└── paths-*.conf           # 不同发行版的路径定义
```

**核心原则**：永远不要修改 `.conf` 文件，所有自定义配置写在 `.local` 文件中。fail2ban 会先读取 `.conf`，再用 `.local` 覆盖。

### 2.2 基础配置

#### 创建 jail.local

```
sudo cat > /etc/fail2ban/jail.local << 'EOF'
[DEFAULT]
# 封禁时间（秒），默认 10 分钟
bantime = 3600

# 检测时间窗口（秒），在这个时间窗口内达到阈值就封禁
findtime = 600

# 失败次数阈值
maxretry = 5

# 封禁动作（Ubuntu 用 iptables，Rocky 用 firewallcmd）
# Ubuntu 24.04:
banaction = iptables-multiport
banaction_allports = iptables-allports

# Rocky Linux 9.5（取消上面两行注释，使用下面的）:
# banaction = firewallcmd-rich-rules
# banaction_allports = firewallcmd-rich-rules

# 忽略的 IP（不会被封禁）
ignoreip = 127.0.0.1/8 ::1 10.0.0.0/8 172.16.0.0/12 192.168.0.0/16

# 封禁时间递增（重复违规者封禁时间翻倍）
bantime.increment = true
bantime.factor = 2
bantime.maxtime = 604800

# 通知邮箱（可选）
# destemail = admin@example.com
# sender = fail2ban@example.com
# mta = sendmail
# action = %(action_mwl)s

# 后端（自动检测，推荐 systemd）
backend = systemd

[sshd]
enabled = true
port = ssh
filter = sshd
maxretry = 3
findtime = 300
bantime = 3600
EOF
```

#### 启动服务

```
# 检查配置语法
sudo fail2ban-client -t
# OK: configuration test is successful

# 启动并设置开机自启
sudo systemctl enable --now fail2ban

# 查看运行状态
sudo fail2ban-client status
# Status
# |- Number of jail:      1
# `- Jail list:   sshd
```

### 2.3 SSH 防护配置

SSH 暴力破解是最常见的攻击类型。fail2ban 内置的 sshd filter 覆盖了大部分场景。

```
# 查看 sshd filter 内置的匹配规则
cat /etc/fail2ban/filter.d/sshd.conf
```

sshd filter 能匹配的日志模式包括：

| 日志模式 | 含义 |
| --- | --- |
| `Failed password for <user> from <host>` | 密码认证失败 |
| `Failed publickey for <user> from <host>` | 公钥认证失败 |
| `Invalid user <user> from <host>` | 不存在的用户名 |
| `Connection closed by authenticating user` | 认证过程中断开 |
| `maximum authentication attempts exceeded` | 超过最大认证次数 |

#### 增强的 SSH 防护配置

```
# /etc/fail2ban/jail.local 中的 [sshd] 部分
[sshd]
enabled = true
port = ssh
filter = sshd[mode=aggressive]
# aggressive 模式包含更多匹配规则，会匹配 "Invalid user" 等

maxretry = 3
findtime = 300
bantime = 3600

# 如果 SSH 使用非标准端口
# port = 2222
```

#### 验证 SSH 防护是否生效

```
# 查看 sshd jail 状态
sudo fail2ban-client status sshd
# Status for the jail: sshd
# |- Filter
# |  |- Currently failed: 2
# |  |- Total failed:     47
# |  `- Journal matches:  _SYSTEMD_UNIT=sshd.service + _COMM=sshd
# `- Actions
#    |- Currently banned: 3
#    |- Total banned:     15
#    `- Banned IP list:   103.xx.xx.92 45.xx.xx.201 185.xx.xx.33

# 查看 iptables 中的封禁规则
sudo iptables -L f2b-sshd -n -v
# Chain f2b-sshd (1 references)
#  pkts bytes target  prot opt in   out  source          destination
#   234 14040 REJECT  all  --  *    *    103.xx.xx.92    0.0.0.0/0
#   156  9360 REJECT  all  --  *    *    45.xx.xx.201    0.0.0.0/0
```

### 2.4 Nginx 防护配置

#### HTTP Basic Auth 暴力破解防护

```
# /etc/fail2ban/jail.local 追加

[nginx-http-auth]
enabled = true
port = http,https
filter = nginx-http-auth
logpath = /var/log/nginx/error.log
maxretry = 5
findtime = 300
bantime = 3600
```

#### Nginx 恶意扫描防护

fail2ban 默认不包含通用的 Nginx 恶意扫描 filter，需要自定义：

```
# 创建自定义 filter
sudo cat > /etc/fail2ban/filter.d/nginx-badbots.conf << 'EOF'
[Definition]
# 匹配常见恶意扫描特征
failregex = ^<HOST> .* "(GET|POST|HEAD) .*(\.php|\.asp|\.aspx|\.jsp|\.cgi|\.env|wp-login|wp-admin|phpmyadmin|\.git|\.svn|config\.|\.bak|\.sql|shell|eval|base64).*" (400|403|404|444)
            ^<HOST> .* "(GET|POST) /" [0-9]+ [0-9]+ "-" ".*(?:masscan|zgrab|python-requests|Go-http-client|Scrapy|curl/|wget/).*"

ignoreregex =
EOF
```

```
# /etc/fail2ban/jail.local 追加

[nginx-badbots]
enabled = true
port = http,https
filter = nginx-badbots
logpath = /var/log/nginx/access.log
maxretry = 3
findtime = 60
bantime = 86400
```

#### Nginx CC 攻击防护

```
# 创建 CC 攻击检测 filter
sudo cat > /etc/fail2ban/filter.d/nginx-cc.conf << 'EOF'
[Definition]
# 匹配短时间内同一 IP 的高频请求（需要在 Nginx 中配置 limit_req 返回 429 或 503）
failregex = ^<HOST> .* "(GET|POST|PUT|DELETE) .*" (429|503) .*$
            limiting requests, excess: .* by zone .*, client: <HOST>

ignoreregex =
EOF
```

```
# /etc/fail2ban/jail.local 追加

[nginx-cc]
enabled = true
port = http,https
filter = nginx-cc
logpath = /var/log/nginx/error.log
          /var/log/nginx/access.log
maxretry = 30
findtime = 60
bantime = 600
```

### 2.5 自定义 filter 正则编写

编写自定义 filter 是 fail2ban 最核心的技能。

#### 正则编写规则

```
# fail2ban filter 正则语法
# <HOST> - 特殊标记，匹配 IP 地址并作为封禁目标
# ^      - 行首（fail2ban 自动处理时间戳前缀）
# .*     - 任意字符
# 其他   - 标准 Python 正则语法
```

#### 测试 filter 是否生效

```
# 测试 filter 规则是否匹配日志
sudo fail2ban-regex /var/log/auth.log /etc/fail2ban/filter.d/sshd.conf

# 测试自定义 filter
sudo fail2ban-regex /var/log/nginx/access.log /etc/fail2ban/filter.d/nginx-badbots.conf

# 测试单行日志
echo '103.1.2.3 - - [13/Mar/2026:10:00:00 +0800] "GET /wp-login.php HTTP/1.1" 404 0' | \
  sudo fail2ban-regex - /etc/fail2ban/filter.d/nginx-badbots.conf

# 输出示例
# Results
# ===...