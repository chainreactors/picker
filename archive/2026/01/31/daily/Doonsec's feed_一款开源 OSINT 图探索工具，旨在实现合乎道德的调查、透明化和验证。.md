---
title: 一款开源 OSINT 图探索工具，旨在实现合乎道德的调查、透明化和验证。
url: https://mp.weixin.qq.com/s/ndTdN_qtHUIEY3iVdbZD6g
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:22:36.303356
---

# 一款开源 OSINT 图探索工具，旨在实现合乎道德的调查、透明化和验证。

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4Ln7j9YplYnKDJsKJvs3QVoIj1wTHX6ib7qJ9R7osOB9T8Lg0y2rRWX2baiaMlQBFOvxs3l46Vcswpic4WytTJh5A/0?wx_fmt=jpeg)

# 一款开源 OSINT 图探索工具，旨在实现合乎道德的调查、透明化和验证。

原创

网络安全民工
网络安全民工

网络安全民工

![]()

在小说阅读器中沉浸阅读

Flowsint 是一款开源 OSINT 图探索工具，旨在实现合乎道德的调查、透明化和验证。

![](https://mmbiz.qpic.cn/mmbiz_png/4Ln7j9YplYnKDJsKJvs3QVoIj1wTHX6ibYM68thWBHWqu2R1tf2l217XsF2icyakxbMpUhO8dlGYbtV2L3MibT0iaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/4Ln7j9YplYnKDJsKJvs3QVoIj1wTHX6ibNXHseIiaLbn47GsgfvgIAZFLoD5M6QW4HDPS46lteiaBJazY66WNoIXw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/4Ln7j9YplYnKDJsKJvs3QVoIj1wTHX6ibPbEWqWaOGGf5FXPuJuX8XtVDic2TticGcicY1tWyiadibj5ZMUckZtAza2A/640?wx_fmt=png&from=appmsg)

贡献

Flowsint 目前仍处于早期开发阶段，非常需要社区的帮助！欢迎提出问题、建议功能等等。

## 开始使用

不想看文字？明白了。以下是安装说明：

#### 1. 安装必备组件

* Docker
* 制作

#### 2. 运行安装命令

```
git clone https://github.com/reconurge/flowsint.gitcd flowsint make prod
```

然后访问http://localhost:5173/register并创建一个帐户。默认情况下没有凭据或帐户。

> ✅ 开源情报调查需要高度保密。所有信息都存储在您的计算机上。

## 那是什么？

Flowsint 是一款基于图的调查工具，专注于侦察和开源情报 (OSINT)。它允许您通过可视化的图形界面和自动增强器来探索实体之间的关系。

### 可用的增稠剂

**域增强器**

* 反向 DNS 解析 - 查找指向 IP 地址的域名
* DNS解析 - 将域名解析为IP地址
* 子域名发现 - 枚举子域名
* WHOIS 查询 - 获取域名注册信息
* 域名转网站 - 将域名转换为网站实体
* 域到根域 - 提取根域
* 域名到ASN - 查找与域名关联的ASN
* 域名历史记录 - 获取历史域名数据

**IP 增强器**

* IP 信息 - 获取地理位置和网络详情
* IP 地址到 ASN 的转换 - 根据 IP 地址查找 ASN

**ASN 增强器**

* ASN 转 CIDR - 获取 ASN 的 IP 地址范围

**CIDR 富集器**

* CIDR 到 IP 地址的转换 - 枚举一定范围内的 IP 地址

**社交媒体增强器**

* Maigret - 跨社交平台搜索用户名

**组织增强器**

* 组织到 ASN - 查找组织拥有的 ASN
* 组织信息 - 获取公司详情
* 组织到域名 - 查找组织拥有的域名

**加密货币增值器**

* 钱包到交易记录 - 获取交易历史记录
* 钱包到 NFT - 查找钱包拥有的 NFT

**网站增强器**

* 网站爬虫 - 抓取并绘制网站结构
* 网站链接提取 - 提取所有链接
* 网站域名提取 - 从 URL 中提取域名
* 网站到网络追踪器 - 识别追踪脚本
* 网站转文本 - 提取文本内容

**电子邮件增强器**

* 发送邮件至 Gravatar - 查找 Gravatar 个人资料
* 向泄露事件发送电子邮件 - 检查数据泄露数据库
* 向域名发送电子邮件 - 查找关联域名

**手机信息增强器**

* 电话泄露事件 - 检查泄露事件中的电话号码

**个人提升者**

* 个人与组织 - 查找组织关系
* 个人到域 - 查找与个人关联的域

**整合增强器**

* N8n 连接器 - 连接到 N8n 工作流程

## 项目结构

该项目由若干个独立模块组成：

### 核心模块

* **flowsint-core**：核心实用程序、编排器、Vault、Celery 任务和基类
* **flowsint-types**：Pydantic 模型和类型定义
* **flowsint-enrichers**：丰富器模块、扫描逻辑和工具
* **flowsint-api**：仅限 FastAPI 服务器、API 路由和模式
* **flowsint-app**：前端应用程序

### 模块依赖项

```
flowsint-app (frontend)
    ↓
flowsint-api (API server)
    ↓
flowsint-core (orchestrator, tasks, vault)
    ↓
flowsint-enrichers (enrichers & tools)
    ↓
flowsint-types (types)
```

## 开发设置

### 先决条件

* Docker

### 跑步

请确保您已安装**Make 工具**。

```
make dev
```

### 发展

该应用程序可通过http://localhost:5173访问。

## 模块详情

### flowsint-core

所有其他模块使用的核心实用程序和基类：

* 数据库连接（PostgreSQL、Neo4j）
* 身份验证和授权
* 日志记录和事件处理
* 配置管理
* 用于增强器和工具的基础类
* 实用函数

### 流类型

适用于所有数据类型的 Pydantic 模型：

* 域名、IP地址、ASN、CIDR
* 个人、组织、电子邮件、电话
* 网站、社交媒体账号、资质证书
* 加密钱包、交易、NFT
* 还有更多……

### 流量富集器

用于处理数据的增强模块：

* 域增强器（子域、WHOIS、解析）
* IP增强器（地理位置、ASN查找）
* 社交媒体强化器（梅格雷、夏洛克）
* 电子邮件增强器（泄露、Gravatar）
* 加密货币增值器（交易、NFT）
* 还有更多……

### flowsint-api

FastAPI 服务器提供：

* REST API 端点
* 身份验证和用户管理
* 图数据库集成
* 实时事件流

### flowsint-app

前端应用程序。

* 现代且用户界面友好的界面
* 专为高性能而设计（即使在数千个节点上也不会出现延迟）

## 开发工作流程

1. **添加新类型**：添加到`flowsint-types`模块
2. **添加新的增强器**：添加到`flowsint-enrichers`模块
3. **添加新的 API 端点**：添加到`flowsint-api`模块
4. **添加新实用程序**：添加到`flowsint-core`模块

## 测试

每个模块都有自己的（不完整的）测试套件：

```
# Test core modulecd flowsint-core poetry run pytest# Test types modulecd ../flowsint-types poetry run pytest# Test enrichers modulecd ../flowsint-enrichers poetry run pytest# Test API modulecd ../flowsint-api poetry run pytest
```

##

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/4Ln7j9YplYkgXg13os3mdJEN1k241aoU461aOjdLSrQvIscf5u8YrTFoPKmQZF8d26FIsE0wb5pS8Gdadytia6g/0?wx_fmt=png)

网络安全民工

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4Ln7j9YplYkgXg13os3mdJEN1k241aoU461aOjdLSrQvIscf5u8YrTFoPKmQZF8d26FIsE0wb5pS8Gdadytia6g/0?wx_fmt=png)

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