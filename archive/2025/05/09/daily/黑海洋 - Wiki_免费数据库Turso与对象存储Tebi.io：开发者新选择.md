---
title: 免费数据库Turso与对象存储Tebi.io：开发者新选择
url: https://blog.upx8.com/4793
source: 黑海洋 - Wiki
date: 2025-05-09
fetch_date: 2025-10-06T22:28:54.334093
---

# 免费数据库Turso与对象存储Tebi.io：开发者新选择

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 免费数据库Turso与对象存储Tebi.io：开发者新选择

发布时间:
2025-05-08

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
37959

## 一、Turso：高性能免费SQLite数据库

![](https://img.7761.cf/img/20250508/1967131577.png)

**核心优势**

* **完全免费**：无需绑卡，无隐藏费用
* **强大性能**：支持每月10亿次读取/2500万次写入
* **大容量**：最高支持9GB存储空间
* **技术架构**：基于SQLite构建，兼容Cloudflare D1但性能更优

**适用场景**
前端开发、中小型应用、需要轻量级但高性能数据库的项目

**官网直达**
👉 [turso.tech](https://blog.upx8.com/go/aHR0cHM6Ly90dXJzby50ZWNoLw)

## 二、Tebi.io：大容量免费对象存储

![](https://img.7761.cf/img/20250508/646552063.jpg)

### 基础信息

* **成立时间**：2020年
* **免费额度**：
  + **存储空间**：25GB（需绑卡）
  + **月流量**：250GB
  + **额外功能**：支持域名绑定、静态网站托管

### 多区域存储策略

| 选择区域数 | 实际可用空间 | 节点分布 |
| --- | --- | --- |
| 2个节点 | 25GB | 德国×3、新加坡×1、美东×2、美西×2 |
| 3个节点 | 16GB | 共8个全球节点 |
| 4个节点 | 12.5GB | 数据自动冗余 |

**对比Backblaze B2**

* 优势：免费空间更大（B2仅10GB）、支持更多CDN节点
* 注意：需绑定信用卡（B2无需绑卡）

**适用场景**

**官网直达**
👉 [tebi.io](https://blog.upx8.com/go/aHR0cHM6Ly90ZWJpLmlvLw)

# Tebi.io自定义域名绑定教程（以`s3.upx8.com`为例）

## 前期准备

1. **域名要求**

   * 拥有域名管理权限（可修改DNS解析）
   * 建议使用子域名（如`s3.upx8.com`）
2. **Tebi账户**

   * 已完成信用卡绑定（免费额度需验证）

## 绑定步骤

### 1. 创建同名存储桶

* 登录[Tebi控制台](https://blog.upx8.com/go/aHR0cHM6Ly90ZWJpLmlvLw)
* 创建存储桶 → 命名必须为 **`s3.upx8.com`** （严格匹配域名）
* 选择至少2个存储区域（建议德国+新加坡）

### 2. 配置DNS解析

| 记录类型 | 主机记录 | 记录值 |
| --- | --- | --- |
| CNAME | s3 | s3.tebi.io. |
| 👉 注意结尾的`.`（部分DNS服务商自动补全） |  |  |

### 3. 开启托管功能

1. 进入存储桶 → **Hosting**标签页
2. 点击 **Enable** → 勾选 **SSL自动续签**
3. 等待状态变为绿色 **Active**（约5分钟）

## 验证绑定

1. 访问 `https://s3.upx8.com`
2. **预期结果**：
   * 出现 `404 Not Found` → 表示域名已成功绑定但未上传文件
   * 若见Tebi默认页 → 需检查DNS缓存（尝试`curl -v`查看响应头）

## 常见问题排查

| 问题现象 | 解决方案 |
| --- | --- |
| DNS解析失败 | 检查CNAME记录是否带末尾`.` |
| SSL证书未签发 | 等待最长1小时或手动重新启用Hosting |
| 访问显示403/Forbidden | 确认存储桶权限设为`Public` |
| 部分地区无法访问 | 更换存储区域组合（如美东+新加坡） |

## 后续操作建议

1. **上传索引文件**

   * 上传`index.html`到存储桶根目录
   * 访问`https://s3.upx8.com`即可显示内容
2. **性能优化**

   ```
   # 测试全球访问延迟
   curl -o /dev/null -s -w "%{time_connect}\n" https://s3.upx8.com
   ```
3. **流量监控**
   在Tebi控制台查看实时流量（免费额度250GB/月）

**注意事项**
❗ 绑定域名后不可修改存储桶名称
❗ 删除存储桶需先关闭Hosting功能
❗ 建议开启存储桶版本控制防止误删

**注意事项**

* Tebio的免费额度需绑卡验证
* 超出免费额度后Turso仍保持可用（限速），Tebi则按量计费

## 三、组合使用建议

1. **数据架构**：Turso管理结构化数据 + Tebi存储静态资源
2. **成本优化**：完全免费方案可支持中小型项目早期阶段
3. **全球部署**：利用Tebi的多区域特性提升海外用户访问速度

[取消回复](https://blog.upx8.com/4793#respond-post-4793)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")