---
title: GoAttack——网络安全扫描分析平台
url: https://mp.weixin.qq.com/s/Z393AgudDtloFDhY5F-B7A
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:41:07.672836
---

# GoAttack——网络安全扫描分析平台

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qqiaD4wiajgFzQLTlpWiaWQ6KjdkxicKricnu5zBibfum38O17E3nTl5R9tFrPGUbThJfnZVUiaGibHmAU40KJSoSzcx8iafj5mxInHIc8HjRe2UibYibM/0?wx_fmt=jpeg)

# GoAttack——网络安全扫描分析平台

一个人挺好
一个人挺好

一个人挺好 wa

![]()

在小说阅读器中沉浸阅读

## 项目地址

https://github.com/dragonkeep/GoAttack

## 项目概述

GoAttack 是一款运用 **Go 语言**作为后端和 **Vue 3** 作为前端开发的现代化网络安全扫描分析平台。它被设计用于对标商业级漏洞扫描器，提供主机探测、端点梳理、资产测绘、漏扫 POC 验证和自动报告等多位一体的安全分析能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFymBFpYNVicaNibo3p386cOal324JYlntTJnMVylYpuqNrG0zbMfbFann1rkHGNVo7GRDNZqTyfiaLgmgKDCzGGms3KBVZSY1Yyto/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFy8KyVhnXrgUcTt75fT4O57w4LBRTLiamL9p6libExUVuTkstsiat4TQXtL0U0HfT33u7YB4659U4tZLiaafQWKsicBekcvlMwLITYE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFyX6YibCFGwRADsWJLSFFRuNpmCricc4prZGQ0sHp7w8Ufru9w6IibI6YszysY6gcCpSnbx1HxzwfQb04Ww72lGkLic6gb7nrLBTM8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFzcAdI3kRq6pwGE0wzU0DC7ZVNAzPf9lWqu9iaBxc82yJQYpEr1YDRmrpnsSJU21PaN61ic9Apm3vcZ3ic4ugh3O3VrurKhww7Fs8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFzZKdG7pwtMYYeloml6ia8vz9nt1jeVLkh4vBUng1PFbG5CJGdDz61iaC0ooDklzUblEz3sSMpxmM2VbchUAZiaZ93O8qV2eibMnMA/640?wx_fmt=png&from=appmsg)

**目标用户群体：**

* 安全工程师
* 红蓝渗透测试人员
* 安全运维管理团队

**默认登录凭证：**

* 账号：`admin`
* 密码：`Qaz@123#`

---

## 系统架构

### 技术栈架构

表格

| 层级 | 技术选型 | 说明 |
| --- | --- | --- |
| **前端层** | Vue 3 + TypeScript | 现代化响应式框架，类型安全 |
| **UI 组件库** | Arco Design | 字节跳动开源的企业级设计系统 |
| **可视化** | Echarts | 数据图表展示与漏洞趋势分析 |
| **后端层** | Go (Gin 框架) | 高性能 HTTP Web 框架 |
| **数据库** | MySQL 8.0+ | 关系型数据持久化存储 |
| **缓存层** | Redis | 会话管理、进度同步、热点数据缓存 |
| **自动化** | Docker + Docker Compose | 容器化一键部署 |

### 核心依赖组件

**后端关键库：**

* `Gin`：HTTP Web 框架
* `Go-Redis`：Redis 客户端连接池
* `Go-MySQL-Driver`：MySQL 数据库驱动
* `Chromedp`：无头浏览器自动化（用于 Web 指纹识别）

**集成工具：**

* **Nuclei**：POC 漏洞验证引擎模板体系
* **Fscan**：弱口令爆破扩展生态
* **Gobuster**：目录枚举插件
* **Nmap-service-probes**：服务指纹识别数据库
* **Wappalyzer**：Web 技术栈识别引擎

---

## 3. 核心功能模块

### 3.1 资产测绘引擎

**主机探测 (Alive Scan)**

* 利用 ICMP 协议快速扫描目标存活状态
* 支持批量 IP 段探测

**端口扫描 (Port Scan)**

* **TCP 扫描**：支持 TOP1000 端口及全端口高并发扫描
* **UDP 扫描**：支持 TOP100 常规协议探测与解析
* 扫描策略优化，适应不同网络环境

**服务指纹识别**

* 结合自研引擎及 `nmap-service-probes` 数据库
* 精准识别服务名称（Service）、产品（Product）和版本号（Version）

**Web 技术栈识别**

* 内置深度重写的高能 Web 探针
* 集成 Wappalyzer 引擎机制
* 识别 HTTP/HTTPS 协议下的建站程序、开发框架
* 支持路由重定向链追踪分析

**目录与子域名爆破**

* 内联搭载 `gobuster` 插件化组件
* 高度配置化的目录枚举策略
* 扫描结果无缝链接至资产指纹模块展示

### 3.2 漏洞检测引擎

**POC 漏洞验证引擎**

* 强力集成 **Nuclei** 模板体系
* 自动执行精准匹配的 CVE/CNVD 级漏洞验证
* 支持 POC 批量导入（`nuclei-templates` 模板库）
* 自动提取漏洞证明（Proof of Concept）

**弱口令爆破攻击 (Brute-Force)**

* 高性能多协议服务口令探测模块
* 依托 Fscan 扩展生态，支持 20+ 核心企业基础服务：

表格

| 协议类别 | 支持服务 |
| --- | --- |
| 数据库 | MySQL, PostgreSQL, MSSQL, Redis, MongoDB, Oracle, Elasticsearch |
| 远程连接 | SSH, RDP, Telnet, VNC, WinRM |
| 文件传输 | FTP, SMB |
| 中间件 | Tomcat, Weblogic, JBoss, ActiveMQ, RabbitMQ, Jenkins |
| 目录服务 | LDAP |

* 智能触发机制：由资产服务版本指纹自动关联对应爆破策略

### 3.3 扫描编排模式

**三大主力扫描模式：**

1. **全量扫描**：全方位深度扫描

* 主机探测 + TCP/UDP 端口扫描 + 弱口令爆破 + 目录枚举 + Web 指纹 + POC 漏洞验证

2. **快速扫描**：精简实用流

* 主机探测 + TCP 端口扫描 + Web 指纹 + POC 验证 + 弱口令核心检测

3. **自定义扫描**：完全独立的子任务节点按需自勾选编排

* 灵活组合各功能模块
* 支持定时任务扫描执行
* IP / 域名资产及危险端口双向黑名单配置

### 3.4 数据可视化与报告

**仪表盘 (Dashboard)**

* 全盘监控安全数据变化、系统态势
* 漏洞严重度占比趋势分析（严重/高危/中危/低危）
* 实时扫描任务状态监控
* 资产总数、指纹识别数、漏洞发现数统计

**系统预警与消息**

* 内置红点及动态数值提醒系统
* 针对高危或致命级新漏洞资产进行实时下发提示

**报告中心模块**

* 一键归档与输出支持优质版式排列的 PDF 和 HTML 业务审计安全报告
* 适应甲乙方多重合规交付场景
* 支持报告模板自定义

---

## 4. 部署指南

### 4.1 Docker 快速部署（推荐）

**环境要求：**

* Docker 20.10+
* Docker Compose 2.0+

**部署步骤：**

```
# 1. 克隆项目
git clone https://github.com/dragonkeep/GoAttack.git
cd GoAttack/GoAttack-Docker

# 2. 一键启动服务（包含 MySQL、Redis、后端 API、前端服务）
docker-compose up -d--build
```

**服务端口映射：**

* 后端 API：3000 端口
* 前端界面：默认映射至 80/443 端口（具体查看 docker-compose.yml 配置）
* MySQL：3306 端口（内部通信）
* Redis：6379 端口（内部通信）

### 4.2 手动本地部署

**环境要求：**

* Go 1.20+
* Node.js 18+
* MySQL 8.0+
* Redis 6.0+

**步骤 1：数据库初始化**

```
# 确保 MySQL 服务运行，并创建数据库用户
# 项目启动时会自动检测并创建 `goattack` 数据库
# 自动执行 `GoAttack-Api/common/sql/init.sql` 完成表结构初始化
```

**步骤 2：后端服务部署**

```
cd GoAttack-Api/

# 安装依赖
go mod tidy

# 编译构建
go build -o go-attack .

# 以管理员/Root 身份运行（扫描需要执行端口扫描及集成嗅探等权限）
./go-attack

# 或开发模式热加载
go run main.go
```

**步骤 3：前端服务部署**

```
cd GoAttack-Admin/

# 安装依赖
npminstall

# 开发模式启动
npm run dev

# 生产构建
npm run build
```

---

## 项目目录结构

```
GoAttack/
├── GoAttack-Api/                 # 后端服务源码
│   ├── common/                   # 公共组件
│   │   ├── config/              # 配置文件（数据库、Redis 连接等）
│   │   └── sql/                 # 数据库初始化脚本
│   │       └── init.sql         # 表结构及基础数据
│   ├── core/                    # 核心扫描引擎
│   ├── plugins/                 # 插件管理（Nuclei、Gobuster 等集成）
│   ├── router/                  # Gin 路由定义
│   ├── service/                 # 业务逻辑层
│   └── main.go                  # 程序入口
│
├── GoAttack-Admin/              # 前端管理界面
│   ├── src/
│   │   ├── components/         # 公共组件
│   │   ├── views/              # 页面视图
│   │   │   ├── dashboard/     # 仪表盘
│   │   │   ├── task/          # 任务管理
│   │   │   ├── vulnerability/ # 漏洞管理
│   │   │   └── report/        # 报告中心
│   │   ├── api/               # API 接口定义
│   │   └── router/            # 前端路由
│   └── package.json
│
└── GoAttack-Docker/             # Docker 部署配置
    └── docker-compose.yml       # 容器编排配置
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

一个人挺好 wa

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

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