---
title: 2026聚合獬豸杯-服务器题解析
url: https://mp.weixin.qq.com/s/hB047TsN-rdXDMyEIXc-zQ
source: Doonsec's feed
date: 2026-06-16
fetch_date: 2026-06-17T07:00:03.066008
---

# 2026聚合獬豸杯-服务器题解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/A8DiammjC4XC135nJSRibMGbygL7ibvTA8Fich6fkx6VahLRAdBUOH8FRWv9jZUy5QhkosO88cvB1NR2KR2cWBZgRFfXcJ1bSZ2sGrZJiaffoIEg/0?wx_fmt=jpeg)

# 2026聚合獬豸杯-服务器题解析

怪叔叔
怪叔叔

取证与溯源

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 检材3 - 2026聚合獬豸杯-服务器题解析

* 作者：yagami
* 任务目录：/mnt/d/文档/hermes-work/jiancai3-server-q1-to-q20/
* 生成时间：2026-06-14
* 生成模式：完整 writeup
* 工具：Hermes Agent
* 模型：Qwen3.6-27B-Uncensored-HauhauCS-Aggressive-Q4\_K\_P.gguf
* 运行方式：本地

## 任务信息

* 题目范围：Q1-Q20（检材3 - 服务器取证）
* 服务器：192.168.100.119:22 root/123456 (CentOS 7)
* 状态文件：state.md, answers.md, findings.md, commands.md, errors.md, verification.md
* 验证策略：远程命令执行 + 源码分析 + 数据库查询 + 彩虹表字典爆破 + 后台登录实际验证

## 工具与模型

| 项目 | 内容 |
| --- | --- |
| 工具 | Hermes Agent |
| 模型 | Qwen3.6-27B-Uncensored-HauhauCS-Aggressive-Q4\_K\_P.gguf |
| 运行方式 | 本地 |

## 答案汇总

| 题号 | 答案 | 答案状态 | 验证等级 | 关键证据摘要 |
| --- | --- | --- | --- | --- |
| Q1 | 3.10.0 | 已验证 | L1 | uname -r 远程执行确认内核版本 |
| Q2 | ahao | 已验证 | L1 | getfacl /etc/shadow 显示 user:ahao:r-- ACL权限 |
| Q3 | nginx/1.20 | 已验证 | L1 | nginx -v 确认为 nginx/1.20.1 |
| Q4 | 5 | 已验证 | L1 | network-check.py 中 KICK\_DELAY="5 minutes" |
| Q5 | FF8180 | 已验证 | L1 | sha256sum faka\_backup.sql 后6位大写 |
| Q6 | Root@123456 | 已验证 | L2 | config.php源码 + MySQL登录测试双证据 |
| Q7 | 8081 | 已验证 | L2 | ss -tlnp + nginx.conf 双证据确认监听端口 |
| Q8 | 60M | 已验证 | L1 | php.ini upload\_max\_filesize = 60M |
| Q9 | 8.208.44.202 | 已验证 | L1 | autobackup.sh REMOTE\_SERVER="8.208.44.202" |
| Q10 | /fk/static/ | 已验证 | L2 | nginx日志33次访问 + login.php独立密码盐双证据 |
| Q11 | 192.168.203.135 | 已验证 | L1 | nginx日志该IP访问login.php共15次最多 |
| Q12 | abc123456 | 已验证 | L3 | 源码算法 + SQL备份哈希 + hashcat彩虹表爆破 + 后台登录验证四源交叉 |
| Q13 | 无忧支付 | 已验证 | L2 | faka\_backup.sql payapi=13 + set.php解码双证据 |
| Q14 | 2018/12/14 | 已验证 | L3 | 在线DB + SQL备份 + 源码页脚三源交叉验证 |
| Q15 | ZhangSan\_Sec | 已验证 | L3 | bash\_history追踪 + 隐藏备份文件 + 解码链三层验证 |
| Q16 | 24073 | 已验证 | L2 | faka/faka\_original双数据库交叉验证 + 源码确认status枚举 |
| Q17 | 5442 | 已验证 | L2 | faka/faka\_original双数据库按日统计交叉验证 |
| Q18 | 无畏契约自动扳机+透视+准星辅助 | 已验证 | L2 | faka/faka\_original双数据库JOIN统计交叉验证 |
| Q19 | guoqi | 已验证 | L2 | 数据库统计 + shua\_site用户名映射双证据 |
| Q20 | \_tmp\_z5m1w8 | 已验证 | L2 | mysql.user表 + SHOW GRANTS双查询交叉验证 |

## 解题过程

### Q1 服务器内核版本号

**题目**：请分析检材3：服务器的内核版本号是多少？【答案格式：4.25.0】

**答案**：3.10.0

**答案状态**：已验证

**验证等级**：L1

**解题思路**：SSH连接服务器后执行 uname -r 获取完整内核版本，按答案格式取主.次.修订三段。

**关键证据**：

* uname -r 返回 `3.10.0-1160.119.1.el7.x86_64`
* 按格式提取前三段 = 3.10.0

**重点命令**：

```
ssh root@192.168.100.119 "uname -r"
```

**关键输出**：

```
3.10.0-1160.119.1.el7.x86_64
```

---

### Q2 读取 /etc/shadow 的普通用户

**题目**：请分析检材3：嫌疑人将某普通用户加入特殊用户组，赋予其读取 /etc/shadow 的权限，请问该普通用户的用户名是什么？【答案格式：admin】

**答案**：ahao

**答案状态**：已验证

**验证等级**：L1

**解题思路**：/etc/shadow 默认权限为 640（root:shadow），通过 getfacl 检查 ACL 发现普通用户 ahao 被额外授予读取权限。

**关键证据**：

* getfacl /etc/shadow 返回 `user:ahao:r--`，确认 ahao (uid=1000) 被额外授予读取权限

**重点命令**：

```
getfacl /etc/shadow
```

**关键输出**：

```
user::rw-
user:ahao:r--
group::r--
mask::r--
other::---
```

---

### Q3 Web 服务器名称及主版本号

**题目**：请分析检材3：分析嫌疑人所使用的 Web 服务器，其具体名称及主版本号是什么？【答案格式：apache/2.40】

**答案**：nginx/1.20

**答案状态**：已验证

**验证等级**：L1

**解题思路**：执行 nginx -v 确认 Web 服务器为 nginx/1.20.1，按格式取名称/主版本去掉修订号。

**重点命令**：

```
nginx -v2>&1
```

**关键输出**：

```
nginx version: nginx/1.20.1
```

---

### Q4 守卫脚本触发间隔

**题目**：请分析检材3：嫌疑人借助 AI 部署 "守卫" 脚本，非管理员 IP 登录时将触发定时强制登出，该服务每隔几分钟触发一次？【答案格式：10】

**答案**：5

**答案状态**：已验证

**验证等级**：L1

**解题思路**：找到守卫脚本 /usr/local/bin/network-check.py，其中 CHECK\_INTERVAL=30秒（检查间隔），KICK\_DELAY="5 minutes"（非管理员IP登录后5分钟强制登出）。

**重点命令**：

```
grep-E"CHECK_INTERVAL|KICK_DELAY" /usr/local/bin/network-check.py
```

**关键输出**：

```
CHECK_INTERVAL = 30
KICK_DELAY = "5 minutes"
```

---

### Q5 数据库备份文件 SHA256 后6位

**题目**：请分析检材3：计算服务器内数据库备份文件，计算其SHA256哈希值，取后6位，字母大写。【答案格式：6DEF3898】

**答案**：FF8180

**答案状态**：已验证

**验证等级**：L1

**解题思路**：服务器内 /tmp/db\_backup/ 下的备份文件几乎为空（20字节），真实备份是 faka\_backup.sql（27MB，来源：计算机检材内BitLocker解密获取）。对其计算 SHA256，取后6位大写。

**重点命令**：

```
sha256sum /tmp/faka_backup.sql
```

**关键输出**：

```
8dd79df101c67fd414100e1f0645e43b1cc5f5ddcf59305741c1a4318bff8180  /tmp/faka_backup.sql
```

后6位 = `ff8180` → 大写 = `FF8180`

**踩坑与修正**：

* 最初误用服务器内空备份文件 fk\_20260614\_103010.sql.gz（仅20字节），后确认真实备份为 faka\_backup.sql

---

### Q6 MySQL root 密码

**题目**：请分析检材3：MySQL 数据库 root 用户的登录密码是什么？【答案格式：根据实际值填写】

**答案**：Root@123456

**答案状态**：已验证

**验证等级**：L2

**解题思路**：从网站源码 config.php 中找到明文 MySQL 密码，并用 mysql 命令行登录测试确认。

**关键证据**：

* /usr/share/nginx/html/fk/config.php 中 `"pwd" => "Root@123456"`（数据库密码）
* MySQL登录测试 `mysql -u root -pRoot@123456 -e "SELECT 1"` 返回成功

**重点命令**：

```
grep "pwd" /usr/share/nginx/html/fk/config.php
mysql -u root -p'Root@123456' -e "SELECT 1 as mysql_test;"
```

**关键输出**：

```
"pwd" => "Root@123456", //数据库密码
mysql_test = 1 (登录成功)
```

---

### Q7 网站对外开放端口

**题目**：请分析检材3：外挂网站所对外开放的端口号是多少？【答案格式：1234】

**答案**：8081

**答案状态**：已验证

**验证等级**：L2

**解题思路**：通过 ss -tlnp 确认 nginx 监听 \*:8081，nginx.conf 中 listen 8081。原默认端口80被修改为8081。

**重点命令**：

```
ss -tlnp | grep nginx
grep "listen" /etc/nginx/nginx.conf
```

**关键输出**：

```
LISTEN *:8081 (nginx)
listen 8081; listen [::]:8081;
```

---

### Q8 最大上传限制

**题目**：请分析检材3：嫌疑人为上传大型恶意插件修改文件上传限制，其最大上传限制是多少？【答案格式：100M】

**答案**：60M

**答案状态**：已验证

**验证等级**：L1

**解题思路**：从 php.ini 和 nginx.conf 确认上传限制。

**重点命令**：

```
grep "upload_max_filesize" /etc/php.ini
```

**关键输出**：

```
upload_max_filesize = 60M
```

---

### Q9 境外服务器IP

**题目**：请分析检材3：嫌疑人设置数据库定时自动备份并上传至境外，请问该境外服务器的IP地址是多少？【答案格式：8.8.8.8】

**答案**：8.208.44.202

**答案状态**：已验证

**验证等级**：L1

**解题思路**：从定时备份脚本 /etc/cron.daily/autobackup.sh 中找到境外服务器IP。

**重点命令**：

```
grep -n "REMOTE_SERVER" /etc/cron.daily/autobackup.sh
```

**关键输出**：

```
第7行: REMOTE_SERVER="8.208.44.202"
```

脚本通过 scp 将数据库备份上传至 root@8.208.44.202:/root/

---

### Q10 隐蔽后台路径

**题目**：请分析检材3：嫌疑人登录后台的目录路径是什么？【答案格式：/abc/abc】

**答案**：/fk/static/

**答案状态**：已验证

**验证等级**：L2

**解题思路**：服务器上有两个后台入口 /fk/admin/ 和 /fk/static/。通过 nginx 日志分析发现 /fk/static/login.php 被访问33次，远高于 /fk/admin/login.php 的7次。且 /fk/static/login.php 有独立密码盐 PWD='2025baofu!'，为嫌疑人实际使用的隐蔽后台。

**关键证据**：

* find 确认 /usr/share/nginx/html/fk/static/login.php 存在，有独立密码盐 `define('PWD', '2025baofu!')`
* nginx日志统计：/fk/static/login.php 被访问33次，/fk/admin/login.php 仅7次
* /fk/static/ 下大量后台管理页面被频繁访问：admin.php(36次)、dashboard.php(30次)、orderlist.php(28次)等

**重点命令**：

```
find /usr/share/nginx/html/fk/ -name "login.php"
zcat -f /var/log/nginx/access.log* | awk '$7 ~ /\/fk\/(static|admin)\/login/ {print $7}' | sort | uniq -c | sort -rn
```

**关键输出**：

```
/fk/static/login.php: 33次访问
/fk/admin/login.php: 7次访问
```

---

### Q11 后台登录页面最多访问IP

**题目**：请分析检材3：访问后台登录页面次数最多的 IP 地址是什么？【答案格式：192.168.1.1】

**答案**：192.168.203.135

**答案状态**：已验证

**验证等级**：L1

**解题思路**：从 nginx access.log 统计访问 /fk/(static|admin)/login.php 的IP地址，192.168.203.135 共15次最多。

**重点命令**：

```
zcat -f /var/log/nginx/access.log* | awk '$7 ~ /\/fk\/(static|admin)\/login\.php/ {cnt[$1]++} END {for (ip in cnt) print cnt[ip], ip}' | sort -rn | head -5
```

**关键输出**：

```
15 192.168.203.135
```

---

### Q12 后台管理员明文密码

**题目**：请分析检材3：网站后台管理员的明文密码为多少？【答案格式：根据实际值填写】

**答案**：abc123456

**答案状态**：已验证

**验证等级**：L3（四源交叉验证）

**解题思路**：从 faka\_backup.sql 解析 shua\_config 获取 admin\_pwd 缓存哈希值和 admin\_user=admin。从 /fk/static/login.php 确认登录算法为 sha256(明文密码 + "2025baofu!")。使用 Windows 本地 hashcat v6.2.6 对目标哈希进行彩虹表字典爆破，Cracked 得到 abc123456。最后用 curl 实际登录后台验证成功。

**关键证据**：

1. **从备份解析配置**：faka\_backup.sql 中 shua\_config 数据：

* admin\_user = admin
* admin\_pwd = 94bd34e3010a6468f312eafe359e9d926fc16bba62c0b6cf646d041a5c281bf2

2. **登录算法确认**：/fk/static/login.php 源码：

   ```
   define('PWD', '2025baofu!');
   $pass = hash('sha256', $pass .PWD);
   ```

   算法为 sha256(明文密码 + "2025baofu!")
3. **hashcat彩虹表字典爆破**：

* Windows本地 hashcat v6.2.6，-m 1410 (sha256($pass.$salt))，-a 0 字典模式
* 字典：彩虹表.txt（12,070条）
* 目标哈希：`94bd34e3010a6468f312eafe359e9d926fc16bba62c0b6cf646d041a5c281bf2:2025baofu!`
* 结果：Cracked 1/1 (100.00%)，Recovered: abc123456

4. **后台登录验证**：POST /fk/static/login.php 返回 HTTP 200，PHPSESSID ...