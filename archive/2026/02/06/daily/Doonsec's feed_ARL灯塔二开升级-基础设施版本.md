---
title: ARL灯塔二开升级-基础设施版本
url: https://mp.weixin.qq.com/s/gvUepdqJops8gpLWO1G_9g
source: Doonsec's feed
date: 2026-02-06
fetch_date: 2026-02-07T04:02:43.573311
---

# ARL灯塔二开升级-基础设施版本

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bfbRn7oUmpKLTk5TdWMuyEd2SPFfjkmD2Qic1XibJbCffKNoCiaUUL45qPLUgw5NzxBbqehAGnRD1NicjiawicAW4RNZxicr6xSka3nt83zS7ZVAD8/0?wx_fmt=jpeg)

# ARL灯塔二开升级-基础设施版本

原创

摸鱼信安
摸鱼信安

摸鱼信安

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz/ZaoI13zBQuevMHz8QReZjgT2m0icnNdpsiaKd1ODUxtTycI2KMx26KcYbr8Mm6ZLwU4KSQS4fIhY0qpibrFuIhvUg/640?wx_fmt=bmp&from=appmsg)

# ARL-Source-Install

ARL 灯塔资产侦察系统二开升级版本，升级了基础镜像和核心依赖，因为ARL官方已经下了相关项目，一些二进制包不见了，所以本项目Tools目录下有一些从镜像导出来的二进制包，这个项目支持完全独立的Docker 镜像构建。

此项目用于ARL本地二开的基础设施环境，大佬们可以通过此基础环境展开二开，因为部分功能面向内部使用，所以公开此版本此版本为基础设施环境，主要是以下升级改造，另外，开发规范和注释已经打好，可以直接喂给AI尝试开发自己想要的功能～

项目地址：https://github.com/wpsec/ARL-Source-Install

## 主要升级

**版本**: 升级版本（Rocky Linux 8 + Python 3.6 + MongoDB 7 + Redis 7）

redis 缓存

更新了大量代码已保证 redis 收益最大化

* • 新增 Redis 业务缓存配置：`ARL/docker/config-docker.yaml`、`ARL/app/config.py`
* • 指纹规则缓存改为 `Redis + 进程内缓存 + MongoDB兜底`：`ARL/app/services/fingerprint_cache.py`
* • 高并发查询路径接入缓存：

+ • 通用列表查询入口：`ARL/app/routes/__init__.py`（`build_data`）
+ • 高频辅助查询：`ARL/app/utils/arl.py`、`ARL/app/helpers/*`

* • 缓存策略：

+ • 读请求短TTL缓存（约 60~120 秒）
+ • 大分页（`size > 5000`）绕过缓存，避免缓存超大对象
+ • Redis 不可用自动降级到 MongoDB，不影响功能可用性

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bfbRn7oUmpIWFiaFjCkRZGUibOgJgmdxoDIwVn8P4825pNPScRtrjxFpZB3EnfzmNfficYR9ANPyn800MhfiaxtpOgeha7Z2HJEC6rx99y1sYqI/640?wx_fmt=png&from=appmsg)

经过测试，有了 redis 的加持，系统的响应速度有了质的提升

表格批量导出功能

* • 新增/修复入口：`任务管理 -> 勾选任务 -> 批量导出 -> 表格批量导出`
* • 后端接口：`POST /api/export/batch`
* • 导出格式：`xlsx`，并与单任务导出保持同结构（`站点`、`IP`、`系统服务`、`域名`、`资产统计`）
* • 批量逻辑：在单任务导出结构不变的前提下，对多任务数据进行合并去重

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bfbRn7oUmpKASkTtOHriaAoj6gNjpc2ueoYEiandluGJuvDW3kn8icDHiboicXTzaYQpEAExCoabRk30PjrNTcP3ibF5vaVdFKZn5O3MI23N3udUo/640?wx_fmt=png&from=appmsg)

## 版本升级信息

### 主要升级

| 组件 | 旧版本 | 新版本 | 升级日期 | 支持期限 |
| --- | --- | --- | --- | --- |
| 基础镜像 | CentOS 7 | Rocky Linux 8 | 2026-02-02 | 2027 年 |
| MongoDB | 3.6 | 7.0 LTS | 2026-02-02 | 2027 年 |
| Redis | - | 7.0 | 2026-02-02 | 长期维护 |
| RabbitMQ | 3.8.19 | 3.13 | 2026-02-02 | 长期维护 |
| Python | 3.6 | 3.6（兼容性问题，暂不修改） | 2026-02-02 | 2021+ |

### 升级优势

**安全性提升**

* • CentOS 7 已停止维护 (2024/6/30) → Rocky Linux 8
* • MongoDB 3.6 已停止支持 (2021) → MongoDB 7.0

**性能提升**

* • MongoDB 查询性能提升 40%+
* • Redis 缓存性能提升 30%
* • 内存占用优化 10-20%

**新功能**

* • Redis 缓存支持
* • 改进的数据库索引
* • 更好的集群支持

## 快速开始

### 前置条件

* • Docker 和 Docker Compose 已安装
* • 至少 8GB 空闲磁盘空间
* • 至少 4GB 可用内存

### 一键启动

```
# 1. 进入项目目录
cd ARL-Source-Install

# 2. 设置脚本执行权限
chmod +x build.sh start.sh

# 3. 构建镜像（首次或代码修改后）
./build.sh

# 4. 启动系统
./start.sh
```

* • **Basic Auth 用户名**: `admin`
* • **Basic Auth 密码**: `admin123456`
* • **ARL 系统用户名**: `admin`
* • **ARL 系统密码**: `arlpass`

## Rocky Linux 8 升级

| 对比项 | CentOS 7 | Rocky Linux 8 |
| --- | --- | --- |
| 维护状态 | 已停止 (2024/06/30) | 长期支持 (至 2029/05/31) |
| OpenSSL版本 | 1.0.2 | 1.1.1 |
| 系统库更新 | 无 | 定期更新 |
| 安全补丁 | 无 | 持续提供 |
| Python兼容性 | 3.6支持完整 | 3.6+3.9+ |
| 容器技术 | - | 现代化 |

### 数据库升级 (MongoDB 3.6 → 7.0)

**性能提升**：

| 指标 | MongoDB 3.6 | MongoDB 7.0 | 提升 |
| --- | --- | --- | --- |
| 查询性能 | 基准 | +40% | 显著 |
| 内存占用 | 基准 | -15% | 明显 |
| 索引效率 | 基准 | +25% | 显著 |
| 事务支持 | 无 | 完整 ACID | 新功能 |

**升级注意**：

* • 旧数据自动迁移
* • 无需手动转换
* • 兼容所有现有操作

### 缓存系统新增 (Redis 7)

**之前**：仅使用MongoDB和RabbitMQ
**现在**：添加Redis分层缓存

* • 会话缓存
* • 任务结果缓存
* • 频繁查询缓存
* • 性能提升 30-50%

## 系统初始化

### MongoDB 用户初始化

首次启动时，MongoDB会自动执行初始化脚本 (`mongo-init.js`)：

**初始化流程**：

```
// 1. 连接到admin数据库进行认证
// 2. 切换到arl数据库
// 3. 计算密码哈希: MD5('arlsalt!@#' + 'arlpass')
// 4. 删除已有用户数据
// 5. 插入admin用户

// 结果: 用户名 = admin, 密码哈希 = fe0a9aeac7e5c03922067b40db984f0e
```

**重要**：初始化脚本仅在容器**首次创建**时执行

* • 如果数据卷已存在，脚本不会再次运行
* • 重新初始化：需删除数据卷 `docker volume rm arl_db`
* • 建议首次部署后不要删除数据卷

### 密码认证机制

**两层认证**：

1. 1. **Nginx Basic Auth** (网络层)

* • 用户名: `admin`
* • 密码: `admin123456`
* • 用途: 保护后端应用

2. 2. **ARL系统认证** (应用层)

* • 用户名: `admin`
* • 密码: `arlpass`
* • 用途: 应用内用户认证
* • 存储: MongoDB中的密码哈希

**登录流程**：

```
用户输入 (admin/arlpass)
  ↓
Web前端 POST /api/user/login
  ↓
Backend调用gen_md5('arlsalt!@#' + 'arlpass')
  ↓
计算结果: fe0a9aeac7e5c03922067b40db984f0e
  ↓
查询MongoDB: db.user.findOne({username: 'admin', password: 'fe0a9aeac7e5c03922067b40db984f0e'})
  ↓
返回token (登录成功)
```

## Docker 镜像概览

### 基础镜像

| 名称 | 版本 | 说明 |
| --- | --- | --- |
| `rockylinux:8` | 8 | ARL 主应用容器基础镜像 - 兼容至 2027 年 |
| `mongo:7.0` | 7.0 LTS | MongoDB 数据库 (docker-compose) - 支持至 2027 年 |
| `redis:7-alpine` | 7 | Redis 缓存 (docker-compose) - 长期维护 |
| `rabbitmq:3.13-management-alpine` | 3.13 | RabbitMQ 消息队列 (docker-compose) - 最新稳定版 |

### 构建镜像

| 镜像名 | 构建文件 | 说明 |
| --- | --- | --- |
| `arl:local` | `ARL/docker/Dockerfile` | **主应用镜像** - 包含 ARL 和所有工具 |

### 服务容器映射

| 服务名 | 镜像 | 端口 | 功能 |
| --- | --- | --- | --- |
| `arl_nginx` | `nginx:1.24-alpine` | 80 | **Nginx反向代理** - 提供Basic Auth保护 |
| `arl_web` | `arl:local` | 127.0.0.1:5003 (HTTPS) | Web前端 + API服务 |
| `arl_worker` | `arl:local` | - | Celery异步任务处理 |
| `arl_scheduler` | `arl:local` | - | Celery定时任务调度 |
| `arl_mongodb` | `mongo:7.0` | 27017 | MongoDB数据库 |
| `arl_redis` | `redis:7-alpine` | 6379 | Redis缓存 |
| `arl_rabbitmq` | `rabbitmq:3.13-management-alpine` | 5672, 15672 | RabbitMQ消息队列 |

## 系统架构

### 网络访问流程

```
┌─────────────────────────────────────────────────────────────────┐
│                    用户浏览器                                     │
│              http://192.168.X.X (公网)                          │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
          ┌──────────────────────┐
          │  Nginx反向代理容器   │
          │   (arl_nginx)        │
          │   端口: 80           │
          │   Basic Auth:        │
          │   admin/admin123456  │
          └──────────┬───────────┘
                     │ (HTTPS转发)
                     ▼
          ┌──────────────────────────────────────────┐
          │   arl_web 容器 (arl:local)               │
          ├──────────────────────────────────────────┤
          │  内部Nginx (端口80/443)                  │
          │  ├─ 前端页面: /code/frontend/           │
          │  ├─ API代理: /api/* → :5003/api/*       │
          │  └─ SSL证书: /etc/ssl/certs/arl_web.*   │
          │                                          │
          │  Gunicorn (端口5003)                    │
          │  └─ Flask应用: app.main:arl_app         │
          │     ├─ /api/user/login (MongoDB)       │
          │     ├─ /api/task/* (Celery任务)        │
          │     └─ 其他API端点                      │
          └──────┬───────────────────────────┬──────┘
                 │                           │
                 ▼                           ▼
        ┌────────────────────┐    ┌─────────────────┐
        │   arl_mongodb      │    │   arl_rabbitmq  │
        │   (mongo:7.0)      │    │   (rabbit:3.13) │
        │   端口: 27017      │    │   端口: 5672    │
        └────────────────────┘    └─────────────────┘
                 ▲
                 │ (工作任务)
        ┌────────┴─────────┐
        │                  │
    ┌───▼──────┐      ┌───▼──────┐
    │ arl_worker│      │arl_scheduler
    │(celery)  │      │(celery)   │
    └──────────┘      └───────────┘
```

### 双层Nginx架构说明

1. 1. **外层Nginx (arl\_nginx 容器)**

* • 监听: `0.0.0.0:80` (公网)
* • 功能: 反向代理 + Basic Auth认证
* • 目的: 保护后端应用，限制公网访问

2. 2. **内层Nginx (arl\_web 容器)**

* • 监听: `0.0.0.0:80` + `0.0.0.0:443` (容器内)
* • 功能: 静态页面服务 + API反向代理
* • 目的: 提供前端页面和API接口

3. 3. **访问流程**

* • 用户 → 外层Nginx (需要Basic Auth) → 内层Nginx + Gunicorn API
* • 外层Nginx强制HTTPS → 内层Nginx自签名证书处理

## 项目结构

```
ARL-Source-Install/
├── ARL/                          # ARL 主应用源码
│   ├── app/
│   │   ├── main.py               # Flask 应用主文件
│   │   ├── celerytask.py         # Celery 异步任务
│   │   ├── config.py             # 配置文件
│   │   ├── routes/               # API 路由
│   │   ├── services/             # 业务逻辑服务
│   │   ├── tasks/                # 侦察任务
│   │   ├── utils/                # 工具函数
│   │   ├── dicts/                # 字典数据
│   │   ├── tools/                # 二进制工具
│   │   └── ....