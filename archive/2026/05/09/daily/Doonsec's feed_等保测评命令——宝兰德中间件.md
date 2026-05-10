---
title: 等保测评命令——宝兰德中间件
url: https://mp.weixin.qq.com/s/Z5hY9rWE55Wp6MX3ea8voQ
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:32:49.996715
---

# 等保测评命令——宝兰德中间件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JJfExzHZwzG7icvOxPmxCJnRJHXswwudwFiaWHc76bK1af8xJwUum17NMnNUw4V8iaLjqoaiapAL9pZIlYGnyGiahw2aYTSOOqHrUVIxqpgZucu4/0?wx_fmt=jpeg)

# 等保测评命令——宝兰德中间件

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

各位大佬，想看那种网络设备/操作系统/数据库/中间件的**测评命令清单，可在留言区留言！**

依据 **GB/T 22239-2019《信息安全技术 网络安全等级保护基本要求》第三级"安全计算环境"** 条款，结合宝兰德官方安全指南及现场测评实践。

**适用产品**：BES Application Server V9.x / V10.x、BES MQ、BES DataExchange、BES Container

---

## 一、BES应用服务器（BES AS）

### 1.1 身份鉴别

| 控制项 | 测评命令/配置 | 达标判据 |
| --- | --- | --- |
| 管理员口令 | `cat $BES_HOME/conf/admin.conf` | 强口令策略 |
| 默认账户 | `cat $BES_HOME/conf/users.properties` | 修改默认admin口令 |
| 密码复杂度 | 控制台 → 系统管理 → 安全策略 | 长度≥8，复杂度≥3种 |
| 登录失败锁定 | 控制台 → 安全管理 → 登录控制 | 失败5次锁定30分钟 |
| 会话超时 | 控制台 → 系统管理 → 会话管理 | ≤30分钟 |
| 双因子认证 | 控制台 → 安全管理 → 认证方式 | 关键用户启用 |

**BES特有配置：**

```
# 查看BES安装路径
echo$BES_HOME
ls-la${BES_HOME:-/opt/bes}/

# 查看版本信息
cat${BES_HOME}/version.txt
cat${BES_HOME}/release 2>/dev/null

# 查看管理员配置文件
cat${BES_HOME}/conf/admin.conf
cat${BES_HOME}/conf/users.properties

# 查看角色权限配置
cat${BES_HOME}/conf/roles.xml
cat${BES_HOME}/conf/groups.properties

# 查看安全域配置
cat${BES_HOME}/conf/security-domain.xml

# 查看登录失败锁定配置
cat${BES_HOME}/conf/login-config.xml
cat${BES_HOME}/conf/lockout-policy.xml 2>/dev/null

# 查看密码策略配置
cat${BES_HOME}/conf/password-policy.xml
# 关键配置项：
# bes.password.minLength=8
# bes.password.complexity=3
# bes.password.history=12
# bes.password.maxAge=90
# bes.password.expiryWarning=7

# 查看会话超时配置
cat${BES_HOME}/conf/session-config.xml
# bes.session.timeout=30
# bes.session.invalidateOnShutdown=true

# 查看双因子认证配置（BES V10+）
cat${BES_HOME}/conf/mfa-config.xml 2>/dev/null
cat${BES_HOME}/conf/otp-config.xml 2>/dev/null

# 查看证书认证配置
cat${BES_HOME}/conf/certificate-config.xml
ls-la${BES_HOME}/conf/*.jks ${BES_HOME}/conf/*.p12

# 查看密钥库内容
keytool -list-v-keystore${BES_HOME}/conf/bes.keystore -storepass changeit 2>/dev/null |head-20
```

### 1.2 访问控制

```
# 查看控制台访问控制
cat${BES_HOME}/conf/admin-access.xml
cat${BES_HOME}/conf/management.xml |grep-E'allow|deny|bind|address'

# 查看管理接口绑定地址
cat${BES_HOME}/conf/management.xml |grep'management-bind-address'
cat${BES_HOME}/conf/management.xml |grep'management-port'

# 查看JMX访问控制
cat${BES_HOME}/conf/jmxremote.access
cat${BES_HOME}/conf/jmxremote.password

# 查看JMX SSL配置
cat${BES_HOME}/conf/jmx-ssl-config.xml 2>/dev/null

# 查看应用部署权限
ls-la${BES_HOME}/autodeploy/
ls-la${BES_HOME}/applications/

# 查看数据源配置（核查明文密码）
cat${BES_HOME}/conf/datasource.xml |grep-E'password|url|user'|head-10

# 查看是否启用密码加密
cat${BES_HOME}/conf/datasource.xml |grep-E'encrypted|encryption'
cat${BES_HOME}/conf/security.xml |grep-E'password-encryption'

# 查看EJB安全配置
cat${BES_HOME}/conf/ejb-jar.xml |grep-E'security-role|method-permission'

# 查看Web应用安全约束
cat${BES_HOME}/conf/web.xml |grep-E'security-constraint|auth-constraint|security-role'

# 查看Servlet过滤器（安全过滤）
cat${BES_HOME}/conf/web.xml |grep-A5'filter-name.*[Ss]ecurity'

# 查看资源引用安全
cat${BES_HOME}/conf/resource-ref.xml |grep-E'res-auth|res-sharing-scope'
```

### 1.3 安全审计

```
# 查看审计日志配置
cat${BES_HOME}/conf/audit.xml
cat${BES_HOME}/conf/audit-log.properties

# 查看日志目录
ls-la${BES_HOME}/logs/
ls-la${BES_HOME}/logs/audit/

# 查看访问日志
cat${BES_HOME}/logs/access.log 2>/dev/null |tail-20
cat${BES_HOME}/logs/localhost_access_log.* 2>/dev/null |tail-20

# 查看审计日志（管理操作）
cat${BES_HOME}/logs/audit.log 2>/dev/null |tail-20
cat${BES_HOME}/logs/admin-audit.log 2>/dev/null |tail-20

# 查看安全日志
cat${BES_HOME}/logs/security.log 2>/dev/null |tail-20

# 查看登录日志
cat${BES_HOME}/logs/login.log 2>/dev/null |tail-20
grep-i"login\|logout\|fail"${BES_HOME}/logs/server.log |tail-20

# 查看日志保留策略
cat${BES_HOME}/conf/logging.properties |grep-E'rotation|size|count|days'
cat${BES_HOME}/conf/log4j.properties |grep-E'MaxFileSize|MaxBackupIndex'

# 查看日志权限
ls-la${BES_HOME}/logs/*.log |head-5
stat-c'%a %U:%G'${BES_HOME}/logs/*.log 2>/dev/null |head-5

# 查看集中审计配置（BES V10+）
cat${BES_HOME}/conf/central-audit.xml 2>/dev/null
cat${BES_HOME}/conf/syslog-appender.xml 2>/dev/null
```

### 1.4 传输与存储安全

```
# 查看HTTPS/SSL配置
cat${BES_HOME}/conf/server.xml |grep-A10'SSL|TLS|https|keystore|truststore'

# 查看SSL协议版本（应禁用TLSv1.0/1.1）
cat${BES_HOME}/conf/ssl-config.xml |grep-E'sslProtocol|sslEnabledProtocols'

# 查看密码套件配置
cat${BES_HOME}/conf/ssl-config.xml |grep-E'ciphers|cipherSuite'

# 查看证书配置
cat${BES_HOME}/conf/server.xml |grep-E'certificateKeystoreFile|certificateKeyFile'
ls-la${BES_HOME}/conf/*.jks ${BES_HOME}/conf/*.p12 ${BES_HOME}/conf/*.pem 2>/dev/null

# 查看国密SSL配置（BES V10+国密版）
cat${BES_HOME}/conf/gmssl-config.xml 2>/dev/null
cat${BES_HOME}/conf/sm2-config.xml 2>/dev/null

# 查看证书有效期
keytool -list-v-keystore${BES_HOME}/conf/bes.keystore 2>/dev/null |grep-E'Valid from|until'

# 查看静态资源缓存控制（安全头）
cat${BES_HOME}/conf/web.xml |grep-E'Cache-Control|Pragma|Expires'

# 查看会话Cookie安全配置
cat${BES_HOME}/conf/context.xml |grep-E'httpOnly|secure|sameSite'
cat${BES_HOME}/conf/session-config.xml |grep-E'cookie-http-only|cookie-secure'

# 查看错误页面配置（防止信息泄露）
cat${BES_HOME}/conf/web.xml |grep-A5'error-page'
ls-la${BES_HOME}/webapps/ROOT/WEB-INF/classes/ |grep-i error

# 查看目录浏览配置
cat${BES_HOME}/conf/web.xml |grep-i'listings'
cat${BES_HOME}/conf/default-web.xml |grep-i'listings'
```

---

## 二、BES消息中间件（BES MQ）

### 2.1 身份鉴别

| 控制项 | 测评命令/配置 | 达标判据 |
| --- | --- | --- |
| 队列管理器认证 | `cat $BES_MQ/qmgrs/QM1/qm.ini` | 启用通道认证 |
| 通道认证 | `dspmqaut` | 限制通道访问 |
| 用户口令 | `cat $BES_MQ/sas/connection.conf` | 强口令策略 |
| 证书认证 | `dspmqcsv` | 启用TLS通道 |
| 连接认证 | `cat $BES_MQ/qmgrs/QM1/config.ini` | 启用连接认证 |

**BES MQ特有配置：**

```
# 查看BES MQ安装路径
echo$BES_MQ
ls-la${BES_MQ:-/opt/bes-mq}/

# 查看队列管理器状态
dspmq
dspmq -o all

# 查看队列管理器配置
cat${BES_MQ}/qmgrs/QM1/qm.ini
cat${BES_MQ}/qmgrs/QM1/config.ini

# 查看通道认证配置
dspmqaut -m QM1 -t channel -n SYSTEM.DEF.SVRCONN
dspmqaut -m QM1 -t qmgr -p appuser

# 查看通道状态
echo"DISPLAY CHSTATUS(*)"| runmqsc QM1
echo"DISPLAY CHANNEL(*)"| runmqsc QM1 |grep-E'CHANNEL|SSL|MCAUSER'

# 查看监听器配置
echo"DISPLAY LISTENER(*)"| runmqsc QM1
echo"DISPLAY LSSTATUS(*)"| runmqsc QM1

# 查看连接认证
echo"DISPLAY QMGR CONNAUTH"| runmqsc QM1
echo"DISPLAY AUTHINFO(*)"| runmqsc QM1

# 查看SSL通道配置
echo"DISPLAY CHANNEL(*) SSLCIPH SSLCAUTH"| runmqsc QM1

# 查看证书存储
dspmqcsv -m QM1
ls-la${BES_MQ}/qmgrs/QM1/ssl/

# 查看密钥库
runmqakm -cert-list-db${BES_MQ}/qmgrs/QM1/ssl/key.kdb -pw password

# 查看连接数限制
echo"DISPLAY QMGR MAXCONN"| runmqsc QM1
echo"DISPLAY CHL(*) MAXINST MAXINSTC"| runmqsc QM1
```

### 2.2 访问控制

```
# 查看队列权限
dspmqaut -m QM1 -n QUEUE1 -t queue -p appuser
echo"DISPLAY QUEUE(*) CURDEPTH MAXDEPTH"| runmqsc QM1

# 查看主题权限
dspmqaut -m QM1 -n TOPIC1 -t topic -p appuser

# 查看进程权限
dspmqaut -m QM1 -n PROCESS1 -t process -p appuser

# 查看名称列表权限
dspmqaut -m QM1 -n NAMELIST1 -t namelist -p appuser

# 查看服务权限
dspmqaut -m QM1 -n SERVICE1 -tservice-p appuser

# 查看集群权限
echo"DISPLAY CLUSQMGR(*)"| runmqsc QM1
echo"DISPLAY CHANNEL(TO.*)"| runmqsc QM1

# 查看消息权限（BES MQ V9+）
echo"DISPLAY AUTHREC PROFILE('QUEUE1') OBJTYPE(QUEUE)"| runmqsc QM1

# 查看资源权限列表
echo"DISPLAY QMGR AUTHOREV"| runmqsc QM1
```

### 2.3 安全审计

```
# 查看审计配置
echo"DISPLAY QMGR AUDIT"| runmqsc QM1
echo"DISPLAY AUTHINFO(SYSTEM.DEFAULT.AUTHINFO.IDPWOS) AUTHTYPE(IDPWOS)"| runmqsc QM1

# 查看日志配置
cat${BES_MQ}/qmgrs/QM1/errors/AMQERR01.LOG |tail-50
cat${BES_MQ}/qmgrs/QM1/errors/AMQERR02.LOG |tail-20

# 查看FFST报告（故障诊断）
ls-la${BES_MQ}/errors/*.FDC 2>/dev/null |head-5

# 查看通道日志
cat${BES_MQ}/qmgrs/QM1/errors/AMQCHL.LOG 2>/dev/null |tail-20

# 查看审计日志（如启用）
cat${BES_MQ}/qmgrs/QM1/errors/AMQAUDIT.LOG 2>/dev/null |tail-20

# 查看消息日志
cat${BES_MQ}/qmgrs/QM1/errors/AMQMSG.LOG 2>/dev/null |tail-20

# 查看系统日志
dspmqlog -m QM1 -t100

# 查看死信队列
echo"DISPLAY QUEUE(SYSTEM.DEAD.LETTER.QUEUE)"| runmqsc QM1
echo"DISPLAY QSTATUS(SYSTEM.DEAD.LETTER.QUEUE)"| runmqsc QM1
```

### 2.4 数据加密

```
# 查看通道加密配置
echo"DISPLAY CHANNEL(SYSTEM.D...