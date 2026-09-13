---
title: 103种蜜罐 + AI威胁分析：这个开源Honeynet到底有多能打？
url: https://mp.weixin.qq.com/s/I7C6vNhTOpR0tMH65J0DYA
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:58:17.933641
---

# 103种蜜罐 + AI威胁分析：这个开源Honeynet到底有多能打？

# 103种蜜罐 + AI威胁分析：这个开源Honeynet到底有多能打？

只会看监控的实习生

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 【开源蜜网平台】Go + 多协议蜜罐 + AI 威胁分析，构建企业级欺骗防御体系！

Honeynet 是一个面向企业安全场景的蜜网与欺骗防御平台。

项目采用 Go 原生 Server + Agent 架构，集成多协议蜜罐、Web 蜜罐、蜜饵、攻击事件分析、YARA 检测、威胁情报、IP 定位以及多渠道告警等能力。

目前项目完整发行版本为 v0.24.0。

Server、Agent 以及蜜罐运行链不依赖 Docker，默认采用 Go 原生二进制运行，并结合 systemd 或 Windows Service 进行管理。

Docker 主要用于数据分析引擎 ClickHouse。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFEzj6RFCT8jXb9IKicZUrIpPRtCLcpmf5wQfibHwAISBtInpW3ibzoSohpXeVldDDwQOndy7wiblTMFPXWyWNyNJR6WjZbaS19ial9Y/640?wx_fmt=webp&from=appmsg)

## 0x01 项目介绍

Honeynet 是一个面向企业安全运营、蓝队、攻防演练以及欺骗防御场景设计的蜜网平台。

整体采用 Server + Agent 分布式架构。

| 组件 | 主要作用 |
| --- | --- |
| honeynet-server | 管理 API、Web 控制台、数据存储以及控制通道 |
| honeynet-agent | 节点能力、蜜罐监听、蜜饵投放以及安全事件采集 |
| MySQL | 用户、节点、蜜罐、规则、告警、系统配置等业务数据 |
| ClickHouse | 攻击事件、安全分析数据 |

Server 负责平台管理、数据处理和控制。

Agent 负责实际的蜜罐监听、蜜饵投放以及安全事件采集。

通过 Server + Agent 的方式，可以将多个蜜网节点统一纳入平台管理。

---

## 0x02 核心能力

Honeynet 目前提供以下核心能力：

| 能力 | 功能 |
| --- | --- |
| 多协议蜜罐 | FTP、PostgreSQL、SMTP、DNS、MSSQL、MongoDB、RDP、SMB、LDAP 等 |
| Web 蜜罐 | 支持完整 Web 资源和自定义 Web 模板 |
| 蜜饵 | 文件、凭据、网络 Token |
| 攻击检测 | IOC、YARA、攻击事件分析 |
| 扫描感知 | Linux 全端口扫描感知 |
| 威胁情报 | IPv4 / IPv6 离线威胁情报 |
| IP 定位 | IPIP 离线城市定位 |
| 告警通知 | SMTP、Syslog、Webhook、企业微信、钉钉、飞书 |
| 节点安全 | TLS 1.3、mTLS、客户端证书、CA 指纹固定 |
| Agent 升级 | SHA-256 + Ed25519 签名、灰度升级、自动回滚 |
| AI 分析 | 单事件分析、攻击者画像、AI Agent 训练、评估、审批和发布 |

---

## 0x03 多协议蜜罐

Honeynet 提供大量可以真实监听的蜜罐服务。

目前包含 **36 种 Go 原生协议蜜罐 + 67 种完整 Web 资源**，共计 **103 种可真实监听的低/中交互蜜罐**。

同时平台提供 **111 种蜜罐服务目录**。

Agent 启动后会向 Server 上报自身支持的蜜罐能力，能力标识采用 `pot.<service>`。

Server 创建蜜罐时，只允许选择目标 Agent 实际支持的服务。

这样可以避免管理端配置节点无法运行的蜜罐服务。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFGbbX271eePeLCo8Me1k0x5zO8Qib43VHzuysbib3ia2HXhkAHjME5MiaOib1icmh23enibZKcbicDDALicJRnjhPpJicaiabEAbPZn9mJibpI/640?wx_fmt=webp&from=appmsg)

### 协议蜜罐版本

| 版本 | 新增协议 |
| --- | --- |
| v0.9 | FTP、PostgreSQL、SMTP、DNS |
| v0.10 | MSSQL、MongoDB、Elasticsearch、MQTT、Modbus TCP、RTSP |
| v0.11 | SMB、RDP、LDAP、SNMP、POP3、IMAP |
| v0.12 | HTTPS、SMTPS、IMAPS、POP3S、LDAPS |
| v0.13 | TFTP、VNC、Memcached、Oracle TNS、ZooKeeper、Kafka |
| v0.14 | Siemens S7comm、CoAP、BACnet/IP |

v0.12 开始增加节点级 TLS 能力。

---

## 0x04 Web 蜜罐

除了协议蜜罐之外，Honeynet 还提供 Web 蜜罐能力。

Web 服务配置直接读取 `honeypot-templates-server/services/config.json`。

目前包含 **68 条静态 Web 服务配置**，其中 **67 条具备完整资源，可以直接原生启动**。

`router-cmcc` 因为缺少资源目录，不会上报能力。

### Web 服务支持

| 类型 | 说明 |
| --- | --- |
| 普通文件 | 提供静态 Web 资源 |
| URL 查询参数映射 | 支持请求参数映射 |
| METHOD\_\_接口名/index.html | 支持基于 HTTP 方法的接口资源 |

Web 资源包中的脚本不会被执行，也不会自动下载外部文件。

每次 Web 访问都会产生 `web.request` 事件。

如果攻击者提交用户名、密码等凭据，则会产生 `web.credential` 事件。

---

## 0x05 Web 请求与凭据捕获

Web 蜜罐会对访问行为进行统一记录。

普通请求产生 `web.request` 事件。

凭据提交产生 `web.credential` 事件。

通过这种方式，可以将 Web 蜜罐访问行为直接纳入平台安全事件体系。

对于资源包中的 Web HTTPS 配置，也支持直接启用 HTTPS。

---

## 0x06 蜜饵投放与命中检测

Honeynet 支持文件、凭据以及网络 Token 等多种蜜饵。

| 类型 | 作用 |
| --- | --- |
| 文件蜜饵 | 监控攻击者对指定文件的访问和操作 |
| 凭据蜜饵 | 通过伪造凭据检测攻击者使用行为 |
| 网络 Token | 构造网络层面的诱捕检测点 |

### 文件蜜饵

Agent 可以监控指定文件。

Linux 环境下可以使用 `inotify` 等机制感知文件访问和变化。

当攻击者读取、修改或者访问蜜饵文件时，可以产生对应安全事件。

### 凭据蜜饵

可以在环境中投放伪造凭据。

当攻击者尝试使用这些凭据时，可以判断其已经获取到了不应该获取的信息。

### 网络 Token

网络 Token 可以用于构造更加隐蔽的攻击检测点。

蜜饵命中后会统一进入事件、审计和 Critical 告警链路。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFEuQHD9TBEN2sicDhqhFUxM1aW4YTkQyCcHE6cJXbU0ahIT6xtnm3b2dNkrMqia9jWXAM7Hl4adtAXicyjPslIzYRoiaIvKl9dpq8E/640?wx_fmt=webp&from=appmsg)

## 0x07 Linux 全端口扫描感知

Honeynet 提供 Linux 全端口扫描感知能力。

Agent 使用 `AF_PACKET` 对网络流量进行感知。

平台会按照来源 IP、协议、时间窗口以及目标端口数量进行累计分析。

当一个来源在短时间内访问大量不同目标端口时，可以生成 `port.scan` 事件。

该功能具有以下特点：

| 特性 | 状态 |
| --- | --- |
| 默认开启 | 否 |
| 监听新端口 | 不会 |
| 修改 iptables | 不会 |
| 修改 nftables | 不会 |
| 网络感知 | 支持 |

因此该能力属于被动式扫描感知。

---

## 0x08 攻击事件检测

平台会统一采集蜜罐、Web、蜜饵等产生的安全事件。

支持以下检测维度：

| 检测能力 | 说明 |
| --- | --- |
| IOC | IOC 特征匹配 |
| YARA | 文件及内容特征检测 |
| 攻击特征 | 攻击行为识别 |
| 来源 IP | 攻击源关联 |
| 资产信息 | 关联受影响资产 |
| 事件关联 | 对多条攻击事件进行关联分析 |

原始 HTTP 请求会保存到 `raw_packet` 字段中。

同时支持对敏感证据进行脱敏。

---

## 0x09 YARA 双阶段检测

Honeynet 集成 YARA 检测能力。

整体采用 Agent 本地初筛与 Server 二次确认的双阶段检测模式。

攻击请求首先经过 Agent 本地检测，再将检测结果提交 Server 进行进一步复核。

当前内置 **54 个 YARA 规则块**。

Agent 首先进行本地快速匹配，然后将结果交给 Server 进一步确认。

自定义正则表达式使用 Go RE2。

---

## 0x0A IP 地理定位

平台支持使用 IPIP 离线数据库进行攻击源城市定位。

攻击事件可以关联以下信息：

| 信息 | 内容 |
| --- | --- |
| IP | 攻击源 IP |
| 国家 | IP 所属国家 |
| 地区 | IP 所属地区 |
| 城市 | IP 所属城市 |

整个定位过程使用离线数据库，不需要依赖在线查询接口。

---

## 0x0B 离线威胁情报

Honeynet 支持 IPv4 / IPv6 离线威胁情报。

情报数据采用 AES-256-GCM 进行保护。

数据格式兼容 `intelligence-db 1.0.2`。

通过离线威胁情报，可以在不依赖外部实时查询服务的情况下，对攻击来源进行本地情报匹配。

---

## 0x0C 告警通知

平台支持多种告警外发方式：

| 类型 | 支持 |
| --- | --- |
| SMTP | 支持 |
| Syslog | 支持 |
| Webhook | 支持 |
| 企业微信 | 支持 |
| 钉钉 | 支持 |
| 飞书 | 支持 |

攻击事件、蜜饵命中以及 Critical 级别事件可以通过配置的通知渠道进行外发。

同时支持失败重试。

---

## 0x0D Agent 安全通信

Honeynet 对 Server 与 Agent 之间的通信进行了安全设计。

### Agent 网关

| 能力 | 说明 |
| --- | --- |
| TLS 1.3 | 加密通信 |
| CA 指纹固定 | 限制可信 CA |
| 客户端证书 | 双向身份认证 |
| 自动续期 | 自动维护证书 |
| 证书吊销 | 支持节点证书吊销 |

### 控制通道

控制通道使用 `mTLS + WSS` 进行保护。

---

## 0x0E 断网情况下的事件可靠性

安全事件采集需要考虑网络中断情况下的数据可靠性。

Honeynet 在 Agent 侧增加了本地持久化事件队列。

事件处理流程为：

攻击事件产生

Agent 本地队列

发送 Server

Server 持久化

业务副作用完成

返回 ACK

只有 Server 完成安全事件持久化以及相关业务副作用之后，才会向 Agent 返回 ACK。

网络中断时，事件会继续保存在本地队列。

---

## 0x0F 队列满载保护

Agent 本地事件队列满载时，不会静默删除尚未收到 Server ACK 的旧事件。

也就是说，**不会通过删除旧事件的方式给新事件腾空间。**

对于永久无效的事件，则会写入 `dead-letter-events.jsonl`。

该文件使用 `0600` 权限，并在执行 `fsync` 后从主队列中移除。

这种机制可以尽可能保证安全事件在传输过程中的完整性。

---

## 0x10 Agent 签名与安全升级

Agent 升级采用 **SHA-256 + Ed25519** 进行完整性和签名校验。

Linux Agent 支持：

| 能力 | 说明 |
| --- | --- |
| 金丝雀发布 | 先在少量节点进行验证 |
| 分批灰度 | 分批次发布新版本 |
| 健康检查 | 验证升级后的节点状态 |
| 自动暂停 | 异常情况下停止继续发布 |
| 自动回滚 | 升级失败后恢复旧版本 |

新版本不会一次性推送到所有 Agent。

可以先通过少量节点进行验证，再逐步扩大发布范围。

---

## 0x11 Server 与 Agent 架构

Honeynet 采用 Server + Agent 分布式架构。

Server 负责统一管理。

Agent 负责实际的蜜罐服务、蜜饵以及事件采集。

多个 Agent 可以部署在不同网络区域，从而扩展整体蜜网覆盖范围。

数据层主要由 MySQL 和 ClickHouse 组成。

| 数据库 | 主要数据 |
| --- | --- |
| MySQL | 用户、节点、蜜罐、规则、告警、系统配置 |
| ClickHouse | 攻击事件、安全分析数据 |

---

## 0x12 Server 安装

Honeynet 支持原生安装。

目前支持：

| 平台 | 架构 |
| --- | --- |
| Linux | AMD64 |
| Linux | ARM64 |
| Windows | x86 |
| Windows | x64 |

Linux 环境需要 `systemd` 和 MySQL 8。

Linux 默认可以安装独立 ClickHouse。

如果已经准备好了外部 ClickHouse，可以使用 `--skip-clickhouse` 跳过本机 ClickHouse 安装。

---

## 0x13 编译 Server

Linux AMD64 编译：

```
make release-server VERSION=0.24.0 TARGET_OS=linux TARGET_ARCH=amd64
```

生成安装包后进行解压：

```
tar -xzf dist/honeynet-server-0.24.0-linux-amd64.tar.gz
```

执行安装：

```
sudo ./scripts/install-server.sh \
  --mysql-dsn '...' \
  --public-url 'http://192.0.2.10:8080' \
  --agent-public-url 'https://192.0.2.10:8443'
```

---

## 0x14 默认服务

安装完成后，系统默认包含以下服务：

| 服务 | 说明 |
| --- | --- |
| `honeynet-server` | Honeynet Server 主服务 |
| `honeynet-agent.service` | 内置 Agent 服务 |

如果只需要安装 Server，可以使用 `--server-only`。

默认服务端口：

| 服务 | 端口 |
| --- | --- |
| Console | `8080` |
| Agent mTLS | `8443` |

安装过程中会自动生成：

| 配置项 | 说明 |
| --- | --- |
| JWT | 身份认证 Token |
| 内置 Token | Agent 注册及管理所需 Token |
| 随机管理员密码 | 初始管理员登录凭据 |
| PKI | Server 与 Agent 通信所需证书体系 |
| 默认蜜罐 | 安装完成后自动创建的默认蜜罐 |

如果需要启用 Console TLS，可以增加 `--console-tls`。

---

## 0x15 ClickHouse 数据分析

Honeynet 使用 ClickHouse 保存攻击事件以及安全分析数据。

默认使用 ClickHouse 官方镜像：

`clickhouse/clickhouse-server:25.8.28.1`

Compose 项目：

`honeynet-analytics`

安装 ClickHouse：

```
sudo ./scripts/install-clickhouse.sh
```

执行数据迁移：

```
sudo ./scripts/migrate-clickhouse.sh
```

执行冒烟测试：

```
sudo ./scripts/smoke-clickhouse.sh
```

查看服务状态：

```
sudo docker compose -p honeynet-analytics ps
```

查看日志：

```
sudo docker compose -p honeynet-analytics logs
```

卸载时只会移除容器和网络，不会自动删除数据卷。

---

## 0x16 Windows Server

Windows Server 同样支持原生部署。

可以使用 PowerShell 执行安装：

```
.\scripts\install-server.ps1 `
  -DatabaseDSN '...' `
  -ConsoleTLS `
  -PublicURL 'https://192.0.2.20:8080' `
  -AgentPublicURL 'https://192.0.2.20:8443'
```

Windows Server 不需要在本机安装 ClickHouse。

---

## 0x17 自定义 Web 蜜罐

Honeynet 支持自定义 Web 蜜罐模板。

模板可以定义：

| 配置 | 说明 |
| --- | --- |
| 精确路由 | 指定 Web 请求路径 |
| HTTP 方法 | 指定 GET、POST...