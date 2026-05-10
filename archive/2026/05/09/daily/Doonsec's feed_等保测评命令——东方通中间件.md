---
title: 等保测评命令——东方通中间件
url: https://mp.weixin.qq.com/s/xY7ym6LSA_OQWYEpQsPKfg
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:32:46.130852
---

# 等保测评命令——东方通中间件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JJfExzHZwzGxcNnBvSPq9uUW7el6j2T3iaSMdJ4fo99M5xEZrLojlBLC6frLFOYLeXShgvtgr37AFs7GoHDgwsGcxYKQSsnWlnILkhl6obBk/0?wx_fmt=jpeg)

# 等保测评命令——东方通中间件

Sec Online

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于汪汪虚拟空间
，作者初恋是小马

![](http://wx.qlogo.cn/mmhead/ibkKkoaQFco6tfIIq0gLqqv5a4nPiawT7sTia17cAoV5PMialOoAaWjZmUkGGYaR1EibW0qAX5StwTXU/0)

**汪汪虚拟空间**
.

汪汪·虚拟空间｜专注学习分享这里有计算机、数学、英语等干货笔记愿你在这里，找到需要的知识，遇见更好的自己

各位大佬，想看那种网络设备/操作系统/数据库/中间件的**测评命令清单，可在留言区留言，我会以最快速度给你们总结，然后发出来！**

依据 **GB/T 22239-2019《信息安全技术 网络安全等级保护基本要求》第三级"安全计算环境"** 条款，结合东方通各产品官方安全指南及现场测评实践。

**适用产品**：TongWeb V7.0 / TongLINK V9.0 / TongEASY V6.0 / TongDXP V3.0 / TongWeb Embedded V1.0

---

## 一、TongWeb 应用服务器

### 1.1 身份鉴别

| 控制项 | 测评命令/配置 | 达标判据 |
| --- | --- | --- |
| 控制台口令 | `cat ${TW_HOME}/conf/twns.xml | grep -A5 "security-domain"` | 强口令策略 |
| 默认账户 | `cat ${TW_HOME}/conf/twusers.properties` | 修改默认admin口令 |
| 密码复杂度 | 控制台 → 系统配置 → 密码策略 | 长度≥8，复杂度≥3种 |
| 登录失败锁定 | 控制台 → 安全管理 → 登录控制 | 失败5次锁定30分钟 |
| 会话超时 | 控制台 → 系统配置 → 会话超时 | ≤30分钟 |

**TongWeb特有配置：**

```
# 查看TongWeb安装路径
echo$TW_HOME
ls-la${TW_HOME:-/opt/TongWeb}/

# 查看控制台配置
cat${TW_HOME}/conf/twns.xml |grep-E'management|console|security'

# 查看用户配置文件
cat${TW_HOME}/conf/twusers.properties
cat${TW_HOME}/conf/twgroups.properties

# 查看角色权限配置
cat${TW_HOME}/conf/tw-roles.xml

# 查看server.xml中的安全域配置
cat${TW_HOME}/conf/server.xml |grep-A10'security-domain'

# 查看登录失败锁定配置（通过JMX或配置文件）
cat${TW_HOME}/conf/twsecurity.xml 2>/dev/null |grep-E'lock|fail'

# 查看HTTPS配置
cat${TW_HOME}/conf/server.xml |grep-E'SSL|TLS|https|keystore|truststore'

# 查看密钥库文件
ls-la${TW_HOME}/conf/*.jks ${TW_HOME}/conf/*.p12 2>/dev/null
keytool -list-v-keystore${TW_HOME}/conf/twserver.jks 2>/dev/null |head-20
```

### 1.2 访问控制

```
# 查看控制台访问控制
cat${TW_HOME}/conf/twns.xml |grep-E'allow|deny|remote|localhost'

# 查看管理接口绑定地址
cat${TW_HOME}/conf/twns.xml |grep'management-bind-address'

# 查看JMX访问控制
cat${TW_HOME}/conf/jmxremote.access 2>/dev/null
cat${TW_HOME}/conf/jmxremote.password 2>/dev/null

# 查看应用部署权限
ls-la${TW_HOME}/autodeploy/
ls-la${TW_HOME}/applications/

# 查看数据源配置（核查明文密码）
cat${TW_HOME}/conf/twns.xml |grep-A10'datasource'|grep-E'password|url|user'

# 查看是否启用密码加密
cat${TW_HOME}/conf/twns.xml |grep-E'password-encryption|encrypted'
```

### 1.3 安全审计

```
# 查看日志配置
cat${TW_HOME}/conf/logging.properties

# 查看访问日志
ls-la${TW_HOME}/logs/access.*
cat${TW_HOME}/logs/access.log 2>/dev/null |tail-10

# 查看审计日志（管理操作）
ls-la${TW_HOME}/logs/admin.*
cat${TW_HOME}/logs/admin.log 2>/dev/null |tail-10

# 查看安全日志
ls-la${TW_HOME}/logs/security.*
cat${TW_HOME}/logs/security.log 2>/dev/null |tail-10

# 查看日志保留策略
cat${TW_HOME}/conf/logging.properties |grep-E'rotation|size|count|days'

# 查看日志权限
ls-la${TW_HOME}/logs/
stat-c'%a %U:%G'${TW_HOME}/logs/*.log 2>/dev/null |head-5
```

### 1.4 入侵防范

```
# 查看版本信息
cat${TW_HOME}/version.txt
cat${TW_HOME}/release 2>/dev/null

# 查看补丁信息
ls-la${TW_HOME}/patches/ 2>/dev/null

# 查看不安全的HTTP方法
cat${TW_HOME}/conf/web.xml |grep-E'http-method|security-constraint'

# 查看错误页面配置（防止信息泄露）
cat${TW_HOME}/conf/web.xml |grep-A5'error-page'

# 查看目录浏览配置
cat${TW_HOME}/conf/web.xml |grep-i'listings'

# 查看会话Cookie安全配置
cat${TW_HOME}/conf/context.xml |grep-E'httpOnly|secure|sameSite'

# 查看类加载器安全配置（防止反序列化漏洞）
cat${TW_HOME}/conf/catalina.properties |grep-E'classloader|filter|serial'

# 查看是否禁用不安全的协议
cat${TW_HOME}/conf/server.xml |grep-E'SSLProtocol|sslProtocol|enabledProtocols'
```

---

## 二、TongLINK 消息中间件

### 2.1 身份鉴别

| 控制项 | 测评命令/配置 | 达标判据 |  |  |
| --- | --- | --- | --- | --- |
| 节点认证 | `cat ${TLQ\_HOME}/etc/tlq.conf | grep -E 'auth | password | ssl'` | 启用节点间认证 |
| 用户口令 | `cat ${TLQ_HOME}/etc/users.conf` | 强口令策略 |  |  |
| 管理控制台 | `cat ${TLQ_HOME}/etc/monitor.conf` | HTTPS访问+强口令 |  |  |
| 密钥管理 | `ls -la ${TLQ_HOME}/etc/*.key` | 密钥文件权限600 |  |  |

**TongLINK特有配置：**

```
# 查看TongLINK安装路径
echo$TLQ_HOME
ls-la${TLQ_HOME:-/opt/TongLINK}/

# 查看主配置文件
cat${TLQ_HOME}/etc/tlq.conf |grep-E'security|auth|ssl|encrypt|password'

# 查看用户配置
cat${TLQ_HOME}/etc/users.conf
cat${TLQ_HOME}/etc/groups.conf 2>/dev/null

# 查看节点配置（集群环境）
cat${TLQ_HOME}/etc/nodes.conf 2>/dev/null |grep-E'node|auth|ssl'

# 查看SSL/TLS配置
cat${TLQ_HOME}/etc/ssl.conf 2>/dev/null
ls-la${TLQ_HOME}/etc/*.pem ${TLQ_HOME}/etc/*.crt ${TLQ_HOME}/etc/*.key 2>/dev/null

# 查看队列访问控制
cat${TLQ_HOME}/etc/acl.conf 2>/dev/null
cat${TLQ_HOME}/etc/queues.conf |grep-E'acl|permission|auth'

# 查看主题访问控制
cat${TLQ_HOME}/etc/topics.conf 2>/dev/null |grep-E'acl|permission'
```

### 2.2 安全审计

```
# 查看日志目录
ls-la${TLQ_HOME}/logs/

# 查看消息日志
cat${TLQ_HOME}/logs/tlq.log 2>/dev/null |tail-20

# 查看安全审计日志
cat${TLQ_HOME}/logs/security.log 2>/dev/null |tail-20
cat${TLQ_HOME}/logs/audit.log 2>/dev/null |tail-20

# 查看连接日志
cat${TLQ_HOME}/logs/connections.log 2>/dev/null |tail-10

# 查看日志轮转配置
cat${TLQ_HOME}/etc/log.conf |grep-E'rotation|size|days|backup'

# 查看日志级别
cat${TLQ_HOME}/etc/log.conf |grep-E'level|debug|info|warn|error'

# 查看日志保留期限
find${TLQ_HOME}/logs/ -name"*.log*"-mtime +180 -ls2>/dev/null |wc-l# 应无超过6个月的日志
```

### 2.3 入侵防范

```
# 查看版本和补丁
cat${TLQ_HOME}/version.txt 2>/dev/null
cat${TLQ_HOME}/VERSION 2>/dev/null
ls-la${TLQ_HOME}/patches/ 2>/dev/null

# 查看监听端口
ss -tulnp|grep-E'$(cat ${TLQ_HOME}/etc/tlq.conf | grep port | head -1)'
cat${TLQ_HOME}/etc/tlq.conf |grep-E'port|bind'

# 查看网络绑定地址
cat${TLQ_HOME}/etc/tlq.conf |grep-E'bind.address|listen|interface'

# 查看连接数限制
cat${TLQ_HOME}/etc/tlq.conf |grep-E'max.connection|max.session|limit'

# 查看消息大小限制（防止DoS）
cat${TLQ_HOME}/etc/tlq.conf |grep-E'max.message|max.size|limit'

# 查看心跳和超时配置
cat${TLQ_HOME}/etc/tlq.conf |grep-E'heartbeat|timeout|keepalive'

# 查看持久化配置（防消息丢失）
cat${TLQ_HOME}/etc/tlq.conf |grep-E'persistent|store|journal'
ls-la${TLQ_HOME}/store/ 2>/dev/null
```

---

## 三、TongEASY 交易中间件

### 3.1 身份鉴别

| 控制项 | 测评命令/配置 | 达标判据 |  |  |
| --- | --- | --- | --- | --- |
| 交易节点认证 | `cat ${TE\_HOME}/etc/telink.conf | grep -E 'auth | key | cipher'` | 启用双向认证 |
| 管理口令 | `cat ${TE_HOME}/etc/admin.conf` | 修改默认口令 |  |  |
| 加密算法 | `cat ${TE_HOME}/etc/security.conf` | 国密SM2/SM3/SM4或AES256 |  |  |

**TongEASY特有配置：**

```
# 查看TongEASY安装路径
echo$TE_HOME
ls-la${TE_HOME:-/opt/TongEASY}/

# 查看核心配置文件
cat${TE_HOME}/etc/telink.conf |grep-E'security|auth|encrypt|ssl|cipher'

# 查看安全域配置
cat${TE_HOME}/etc/security.conf
cat${TE_HOME}/etc/domain.conf 2>/dev/null

# 查看密钥配置
ls-la${TE_HOME}/etc/security/
cat${TE_HOME}/etc/security/keys.conf 2>/dev/null

# 查看国密配置（V6.0+支持国密）
cat${TE_HOME}/etc/gmtlse.conf 2>/dev/null |grep-E'SM2|SM3|SM4|GM'

# 查看证书配置
ls-la${TE_HOME}/etc/certs/
openssl x509 -in${TE_HOME}/etc/certs/server.crt -text-noout2>/dev/null |head-20

# 查看交易路由安全配置
cat${TE_HOME}/etc/route.conf |grep-E'auth|secure|ssl'

# 查看监控配置
cat${TE_HOME}/etc/monitor.conf |grep-E'password|auth|bind|ssl'
```

### 3.2 安全审计

```
# 查看日志目录
ls-la${TE_HOME}/logs/

# 查看交易日志
cat${TE_HOME}/logs/telink.log 2>/dev/null |tail-20

# 查看交易追踪日志（用于审计）
cat${TE_HOME}/logs/trace.log 2>/dev/null |tail-20

# 查看错误日志
cat${TE_HOME}/logs/error.log 2>/dev/null |tail-10

# 查看统计日志（用于分析）
cat${TE_HOME}/logs/stat.log 2>/dev/null |tail-10

# 查看日志配置
cat${TE_HOME}/etc/log.conf |grep-E'level|file|size|rotation'

# 查看交易流水号生成规则（用于追踪）
cat${TE_HOME}/etc/telink.conf |grep-E'serial|trace|xid|guid'
```

### 3.3 高可用与数据完整性

```
# 查看集群配置
cat${TE_HOME}/etc/cluster.conf 2>/dev/null

# 查看主备切换配置
cat${TE_HOME}/etc/ha.conf 2>/dev/null |grep-E'failover|switch|backup|primary'

# 查看事务日志（确保交易完整性）
ls-la${TE_HOME}/journal/
ls-la${TE_HOME}/txlog/

# 查看检查点配置
cat${TE_HOME}/etc/telink.conf |grep-E'checkpoint|sync|flush'

# 查看数据备份配置
cat${TE_HOME}/etc/backup.conf 2>/dev/null
ls-la${TE_HOME}/backup/ 2>/dev/null
```

---

## 四、TongDXP 数据交换平台

### 4.1 身份鉴别

| 控制项 | 测评命令/配置 | 达标判据 |
| --- | --- | --- |
| 平台管理员 | `cat ${TDXP_HOME}/config/users.xml` | 强口令+定期更换 |
| 交换节点认证 | `cat ${TDXP_HOME}/config/nodes.xml` | 证书认证 |
| 传输加密 | `cat ${TDXP_HOME}/config/transport.xml` | SSL/TLS或国密 |

**TongDXP特有配置：**

```
# 查看TongDXP安装路径
echo$TDXP_HOME
ls-la${TDXP_HOME:-/opt/TongDXP}/

# 查看用户配置
cat${TDXP_HOME}/config/users.xml
cat...