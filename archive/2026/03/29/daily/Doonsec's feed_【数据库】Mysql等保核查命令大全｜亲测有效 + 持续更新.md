---
title: 【数据库】Mysql等保核查命令大全｜亲测有效 + 持续更新
url: https://mp.weixin.qq.com/s/kFcIUvG_MCcp9NAws48L6w
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:44:13.555473
---

# 【数据库】Mysql等保核查命令大全｜亲测有效 + 持续更新

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2r1REgdXKkrD9rvtwhXwK631CibrM9LyfwIYhiaMTpEeEGKuQEhictTXMJjiaicDlRnFotXia1rzrmb7scOwJQEppfgrtpA3M37P9b0UItOksBFmg/0?wx_fmt=jpeg)

# 【数据库】Mysql等保核查命令大全｜亲测有效 + 持续更新

Sec Online

![]()

在小说阅读器中沉浸阅读

以下文章来源于汤池杂货铺
，作者Fuyuanzi

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5J0Y2dAfZtVROkAVlm3W1h1cT95E1sJ3cFJ0nGNSmcJA/0)

**汤池杂货铺**
.

是一个什么都想学一点的小邋遢

---

解决以下3个痛点：

1️⃣能查到的大部分检查命令没有运行结果的截图，无法确定命令是否有效。

2️⃣不同版本的被侧目标可能使用不同的命令，过时或者较新的命令可能无法有效运行，明显降低检查效率**。**

3️⃣**网络公开的检查方法整体缺乏系统性与持续维护**

💽测试环境：虚拟机

💽测试镜像版本：CentOS-7-x86\_64-Minimal-1609-99.iso

💽数据库版本：Mysql 8.4.8

📚文末可提取本文的无水印PDF版本的百度网盘下载链接，方便各位在无网络环境下的使用。

👇如果有更加好的检测命令或者需要修改的地方，请在评论区留言。我会及时更新改正，并上传新的离线文件。

---

目录结构：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkqWr0CNejNqssAzMfJ5HKMrCZhPF0ywORvCribWZGYRAVP1vRz85iao1NZ1V0ukkM9oDoP2dTSickdgrP33ibAVlEPAMlNthODgj3o/640?wx_fmt=png&from=appmsg)

---

# 一、身份认证与密码策略

## 1.1 密码过期策略

```
SHOW VARIABLES LIKE 'default_password_lifetime';
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkroJrosib8ia5EZtyeoufn5a1m8nHRHw5z7F9I2gzSt6st3uk03LhicShOibJqibwDJWPzlYiabDTr4dgeFLkoLMauYGjag6D1tib6zjY/640?wx_fmt=png&from=appmsg)

## 1.2 密码复杂度验证

```
SHOW VARIABLES LIKE 'validate_password%';
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkoRT9OP93D6mnNj9DTKlIsBkmLlWF2L1a8lpdR5DuibKFEtibl3C4cAHBZjl4INvk3oQBLoNqwxiancrianknpO4cAzGtW8Cpcuy9s/640?wx_fmt=png&from=appmsg)

| 参数名 | 取值 | 含义 |
| --- | --- | --- |
| `validate_password.changed_characters_percentage` | 0 | 修改密码时，新密码与旧密码的字符差异百分比（0 = 无要求，100 = 完全不同） |
| `validate_password.check_user_name` | ON | 是否检查密码是否包含用户名（ON = 禁止密码包含用户名，OFF = 允许） |
| `validate_password.dictionary_file` | 空 | 密码字典文件路径（指定后，密码不能是字典中的值，空 = 不启用字典检查） |
| `validate_password.length` | 8 | 密码最小长度（默认 8 位，低于此长度的密码会被拒绝） |
| `validate_password.mixed_case_count` | 1 | 密码中至少包含的大小写字母数量（1 = 至少 1 个大写 + 1 个小写，0 = 无要求） |
| `validate_password.number_count` | 1 | 密码中至少包含的数字数量（1 = 至少 1 个数字） |
| `validate_password.policy` | MEDIUM | 密码策略等级： - LOW：仅检查长度 - MEDIUM：检查长度 + 数字 + 大小写 + 特殊字符 - STRONG：MEDIUM + 字典检查 + 字符差异 |
| `validate_password.special_char_count` | 1 | 密码中至少包含的特殊字符数量（!@#$%^&\* 等，1 = 至少 1 个） |

## 1.3 查询空密码

```
SELECT user, host FROM mysql.user WHERE authentication_string = '' OR authentication_string IS NULL;
```

数据库安全状态下，查询结果应为空

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkrpLtPFKujPkzFLXATW5DaEIUv9ICtBSRf74ex9cV6tIahiaLH3bugd0oISkcCzgzVGwhZd2btrHrkkFTKnSdJubNZeCia8EMZ3U/640?wx_fmt=png&from=appmsg)

## 1.4 匿名账户

```
SELECT user, host FROM mysql.user WHERE user = '';
```

用来查询 MySQL 中**用户名为空字符串**的匿名用户，如果返回空结果，说明你的数据库中没有匿名用户；如果返回结果，说明存在安全风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkqZw1qmic5epGicuEWK4er8nlsbIKkmEumqOnvYOicfDoYZONs4to9bpIhZl6sicsSDXFfPu3M5Dxic28XjhRv0XJENvfkClial5GD0c/640?wx_fmt=png&from=appmsg)

# 二、权限管理

主要希望数据库遵循最小权限原则

## 2.1 超级管理员账户

```
SELECT user, host FROM mysql.user WHERE super_priv = 'Y';
```

仅限必要的管理账号，禁止 '%' 主机授权的 super 用户

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkqI0IMu0aebTEQrd0KkqObPNGBru4Ds4wC89RWlthp1pJAbkfjQyIHPEsv8weRy9ibswUKupyew8ByabWcIkEIbmjRF587UAn4Q/640?wx_fmt=png&from=appmsg)

## 2.2 检查文件权限

```
SELECT user, host FROM mysql.user WHERE file_priv = 'Y';
```

拥有此权限可读取服务器任意文件，应严格限制。

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkqpJr4fMy0ZDUGIOUn60pZuxXDGPTwQLXaAUkPpJQcibLicMMmep31BUGuBoF0tYLrVOluH6ZlnkPVa0r1BLiaqE54AsS8KA1kiaMo/640?wx_fmt=png&from=appmsg)

## 2.3 核心权限查询

```
SELECT user, host, grant_priv, shutdown_priv, process_priv FROM mysql.user;
```

查询 MySQL 用户的**核心权限**（授权权限、关闭服务权限、查看进程权限），应避免 `%` 用户具备此权限。

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkpy7AkmtCfibJpeeqcRgaUib8MxtMgME8rbXNZibYByMOv10GbrbUSpKJgdW0ibQxVBQ8F2YPXGTmuZ4aiaK91ZntT164Yhnicfiapglg/640?wx_fmt=png&from=appmsg)

## 2.4 test 数据库权限

```
SHOW GRANTS FOR 'public'@'%';
```

* • 如果有 public 用户，请删除；
* • 移除对 test 库的公共访问权限，或直接删除 test 库；

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkoqsjZZAYyH6JdPfdUJSkj95MUMGELsbhia0NRFtW1fk453dWuXS6VVkK99hgakiafNmtH9VIKDxrj7CN9j3icpAjP6qhxPudWJV4/640?wx_fmt=png&from=appmsg)

# 三、网络与连接安全

## 3.1 绑定地址

```
cat /etc/my.cnf
```

不应绑定在 `0.0.0.0` (除非有防火墙严格限制)，最好绑定内网 IP 或 `127.0.0.1`。

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkqLia6jEicRTp8lS4DAdCNLl0feCCTuAQBsvwkdDqibw8kwQI7utiagibDAL9IHgB2Rdy9VxMZUR9picb3UsnUYghK4ZEonbNgqx5MPM/640?wx_fmt=png&from=appmsg)

## 3.2 本地加载数据

```
SHOW GLOBAL VARIABLES LIKE 'local_infile';
```

`local_infile = ON` 存在以下安全隐患，生产环境建议保持 `OFF`：

1. 1. **文件读取漏洞**：攻击者可利用该功能，诱骗 MySQL 客户端读取服务器本地的敏感文件（如 `/etc/passwd`、`/var/lib/mysql/mysql.user`）；
2. 2. **注入风险**：结合 SQL 注入，可通过 `LOAD DATA LOCAL INFILE` 写入恶意数据或读取系统文件；

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkr9Gm9zhpPVsAwAu1hXvgPRIc9CNpg14ZWicupc9UxJnJHRB87jiaHuF1Xy7vNf93ucNHP5U2nic4ibcwMVU7obm33iarlh7ynEZNs8/640?wx_fmt=png&from=appmsg)

## 3.3 最大连接数与超时

```
SHOW VARIABLES LIKE 'max_connections';
SHOW VARIABLES LIKE 'wait_timeout';
SHOW VARIABLES LIKE 'interactive_timeout';
```

请根据实际业务情况设定合理值，避免 DoS 攻击；超时时间不宜过长。

**max\_connection**:

* • 小型应用（日均访问 < 10 万）：500 - 1000；
* • 中型应用（日均访问 10 万 - 100 万）：1000 - 2000；
* • 大型应用：结合实际硬件配置和访问量综合判断；

**wait\_timeout / interactive\_timeout**:

* • 非交互式连接（wait\_timeout）：300 秒（5 分钟）- 900 秒（15 分钟）；
* • 交互式连接（interactive\_timeout）：3600 秒（1 小时）（兼顾运维操作便利性）；

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKko5vQBrn0hZiarnQN6TgwTOFk39cflibAEATAEico9BibvF8zGAb76RwVNz4GICf7u0201JD4r9ibdfpNSkh88icKXjxPXzFEWZv075w/640?wx_fmt=png&from=appmsg)

## 3.4 SSL/TLS 启用

```
SHOW STATUS LIKE 'Ssl_version';
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkpuMl1NEyBfA0WUAIZJbDMPq5eyAvLefh7Ef6ZI9ftPicJaZYRjmUtfhe3lxaUyAxyIpau1iabEicBmDluqZictVXw3VCrsWzPptnc/640?wx_fmt=png&from=appmsg)

| 输出 Value | 含义 |
| --- | --- |
| `TLSv1.2` /`TLSv1.3` | MySQL 已启用 SSL/TLS，当前使用的加密协议版本（TLSv1.3 是最安全的版本） |
| `TLSv1` /`TLSv1.1` | 启用了 SSL/TLS，但协议版本过旧（存在安全漏洞，如 POODLE 攻击） |
| 空值（无结果） | MySQL 未启用 SSL/TLS，所有连接均为明文传输（极高安全风险） |
| 其他ssl相关信息的检查如下👇： |  |

```
SHOW VARIABLES LIKE '%ssl%';
```

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkpwDyuUPQ5981JnRCVeTyibgBXKNGPqba93nBZFSG02cGlNzysXpGMXW6o9nia5evQ2cxnAPpq0Y0B1RcG469XhFmtt0LLYae79I/640?wx_fmt=png&from=appmsg)

## 3.5 数据库版本

```
SELECT VERSION();
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkpvCb1HkcB5nHFLkpwXTaDNptWeCTmj72LtkBs2kria0ejo33WNXFOWyV0y3ojyNyaibOJpl0UKmf5OThaNoRzkdTOLpDC5TVPYQ/640?wx_fmt=png&from=appmsg)

**直接访问安全公告库**：

链接：https://www.oracle.com/security-alerts/（MySQL 属于 Oracle 旗下产品，安全公告统一发布在此）

* 操作步骤：

1. 页面搜索框输入 `MySQL 8.4.8` 或 `CVE MySQL 8.4`；
2. 筛选「MySQL Server」「8.4.x」版本，即可看到 8.4.8 修复的安全漏洞（包括 CVE 编号、漏洞等级、影响范围、修复方式）。

**8.4 系列安全汇总页**：

链接：https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-8.html

（8.4.8 版本专属更新日志，包含「Security Fixes」章节）

# 四、日志与审计

## 4.1 检查通用日志

```
SHOW VARIABLES LIKE 'general_log';
```

生产环境通常关闭以减少性能损耗，但在排查问题或高安环境下需开启并定期归档。

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkreubRJwLm71dHvmpG5DGR72Y5iagxPGCAUlf3PpUcRrZC8MVRl1MyAfuhnU63X9u3F5JWZcoJrGFa1SXUic2VkUrzqdJVy9pcls/640?wx_fmt=png&from=appmsg)

## 4.2 检查错误日志

```
cat /etc/my.cnf
```

![](https://mmbiz.qpic.cn/mmbiz_png/2r1REgdXKkr8VmBQhSWh2zVMk8IiaMAj2H2lSXqZxK8LHXOOLGEsPZ9pHYZ6l07ANo2l7LTm9EgvPKoLzARPRlFQKXEKOGQm7rfE4pV2icLOk/640?wx_fmt=png&from=appmsg)

## 4.3 检查审计

```
SHOW VARIABLES LIKE '%audit%';
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkr3ODmI6nTmoBSm5cCqMia9M4wwicUKAm2vBibvQanYFgMnQV555jHwHONn5FzlPtq68icIX8YZqqqrmENlQC909X38ic0ibY4sFmcsE/640?wx_fmt=png&from=appmsg)

# 五、配置文件的物理检查

## 5.1 文件权限查看

```
ls -l /etc/my.cnf
```

属主为 root:mysql，权限为 644 或 600，严禁其他用户可写。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkr7lQGobMTjTzJlJfPXLOUhAQiagxzCnDgKdNybhPFQEEcibvz5Lj9Wib8ztIOXqSic3L3HG8hDK5sl3UMW0MGPaTKicXlI6WKtBxics/640?wx_fmt=png&from=appmsg)

## 5.2 关键参数核查

```
cat /etc/my.cnf
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2r1REgdXKkr8DeHQZ4Fm8AzzPWB97m8xCx4OhUM3f305kEBTFlicNgj1L186CUfbovOKKm4kD5NKkLL3R3eib7LMPpRntutF5JtRcGaI8Poeg/640?wx_fmt=png&from=appmsg)

1. 1. skip-symbolic-links（禁用符号链接）

* • **作用**：禁止 MySQL 使用符号链接（软链接）访问数据文件，防止攻击者通过目...