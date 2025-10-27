---
title: TiDB Lightning 源码阅读
url: https://jiajunhuang.com/articles/2025_09_02-lightning_source_code.md.html
source: Jiajun的技术笔记
date: 2025-09-03
fetch_date: 2025-10-02T19:32:30.135748
---

# TiDB Lightning 源码阅读

[Jiajun的技术笔记](/)

搜索

* [EN](https://blog.jiajunhuang.com)
* [归档](/archive)
* [分享](/sharing)
* [随想](/notes)
* [友链](/friends)
* 工具

  [面试题库](https://tiku.jiajunhuang.com)
  [幻灯片](https://jiajunhuang.com/page/index.md)
* [关于](/aboutme)

目录

* [TiDB Lightning 源码阅读](#TiDB%2bLightning%2b%25E6%25BA%2590%25E7%25A0%2581%25E9%2598%2585%25E8%25AF%25BB)
* [前言](#%25E5%2589%258D%25E8%25A8%2580)
* [一、项目整体架构](#%25E4%25B8%2580%25E3%2580%2581%25E9%25A1%25B9%25E7%259B%25AE%25E6%2595%25B4%25E4%25BD%2593%25E6%259E%25B6%25E6%259E%2584)
* [1.1 目录结构分析](#1.1%2b%25E7%259B%25AE%25E5%25BD%2595%25E7%25BB%2593%25E6%259E%2584%25E5%2588%2586%25E6%259E%2590)
* [二、核心导入流程深入分析](#%25E4%25BA%258C%25E3%2580%2581%25E6%25A0%25B8%25E5%25BF%2583%25E5%25AF%25BC%25E5%2585%25A5%25E6%25B5%2581%25E7%25A8%258B%25E6%25B7%25B1%25E5%2585%25A5%25E5%2588%2586%25E6%259E%2590)
* [2.1 主要导入步骤](#2.1%2b%25E4%25B8%25BB%25E8%25A6%2581%25E5%25AF%25BC%25E5%2585%25A5%25E6%25AD%25A5%25E9%25AA%25A4)
* [2.2 表结构恢复（restoreSchema）](#2.2%2b%25E8%25A1%25A8%25E7%25BB%2593%25E6%259E%2584%25E6%2581%25A2%25E5%25A4%258D%25EF%25BC%2588restoreSchema%25EF%25BC%2589)
* [2.3 数据导入（importTables）](#2.3%2b%25E6%2595%25B0%25E6%258D%25AE%25E5%25AF%25BC%25E5%2585%25A5%25EF%25BC%2588importTables%25EF%25BC%2589)
* [三、多后端架构设计](#%25E4%25B8%2589%25E3%2580%2581%25E5%25A4%259A%25E5%2590%258E%25E7%25AB%25AF%25E6%259E%25B6%25E6%259E%2584%25E8%25AE%25BE%25E8%25AE%25A1)
* [3.1 Backend 接口抽象](#3.1%2bBackend%2b%25E6%258E%25A5%25E5%258F%25A3%25E6%258A%25BD%25E8%25B1%25A1)
* [3.2 两种主要后端模式](#3.2%2b%25E4%25B8%25A4%25E7%25A7%258D%25E4%25B8%25BB%25E8%25A6%2581%25E5%2590%258E%25E7%25AB%25AF%25E6%25A8%25A1%25E5%25BC%258F)
* [3.3 引擎管理机制](#3.3%2b%25E5%25BC%2595%25E6%2593%258E%25E7%25AE%25A1%25E7%2590%2586%25E6%259C%25BA%25E5%2588%25B6)
* [四、检查点与容错机制](#%25E5%259B%259B%25E3%2580%2581%25E6%25A3%2580%25E6%259F%25A5%25E7%2582%25B9%25E4%25B8%258E%25E5%25AE%25B9%25E9%2594%2599%25E6%259C%25BA%25E5%2588%25B6)
* [4.1 检查点系统设计](#4.1%2b%25E6%25A3%2580%25E6%259F%25A5%25E7%2582%25B9%25E7%25B3%25BB%25E7%25BB%259F%25E8%25AE%25BE%25E8%25AE%25A1)
* [4.2 多层级状态追踪](#4.2%2b%25E5%25A4%259A%25E5%25B1%2582%25E7%25BA%25A7%25E7%258A%25B6%25E6%2580%2581%25E8%25BF%25BD%25E8%25B8%25AA)
* [4.3 断点续传实现](#4.3%2b%25E6%2596%25AD%25E7%2582%25B9%25E7%25BB%25AD%25E4%25BC%25A0%25E5%25AE%259E%25E7%258E%25B0)
* [五、错误处理与冲突解决](#%25E4%25BA%2594%25E3%2580%2581%25E9%2594%2599%25E8%25AF%25AF%25E5%25A4%2584%25E7%2590%2586%25E4%25B8%258E%25E5%2586%25B2%25E7%25AA%2581%25E8%25A7%25A3%25E5%2586%25B3)
* [5.1 ErrorManager 架构](#5.1%2bErrorManager%2b%25E6%259E%25B6%25E6%259E%2584)
* [5.2 冲突检测与处理](#5.2%2b%25E5%2586%25B2%25E7%25AA%2581%25E6%25A3%2580%25E6%25B5%258B%25E4%25B8%258E%25E5%25A4%2584%25E7%2590%2586)
* [5.3 错误恢复机制](#5.3%2b%25E9%2594%2599%25E8%25AF%25AF%25E6%2581%25A2%25E5%25A4%258D%25E6%259C%25BA%25E5%2588%25B6)
* [六、性能优化技术](#%25E5%2585%25AD%25E3%2580%2581%25E6%2580%25A7%25E8%2583%25BD%25E4%25BC%2598%25E5%258C%2596%25E6%258A%2580%25E6%259C%25AF)
* [6.1 并发控制策略](#6.1%2b%25E5%25B9%25B6%25E5%258F%2591%25E6%258E%25A7%25E5%2588%25B6%25E7%25AD%2596%25E7%2595%25A5)
* [6.2 内存管理优化](#6.2%2b%25E5%2586%2585%25E5%25AD%2598%25E7%25AE%25A1%25E7%2590%2586%25E4%25BC%2598%25E5%258C%2596)
* [6.3 磁盘IO优化](#6.3%2b%25E7%25A3%2581%25E7%259B%2598IO%25E4%25BC%2598%25E5%258C%2596)

# TiDB Lightning 源码阅读

## 前言

Lightning 是 TiDB 的高速数据导入工具，专门用于将 TB 级别的数据快速导入到 TiDB 集群中。作为 TiDB 生态系统的重要组件，Lightning 在大规模数据迁移场景中发挥着至关重要的作用。

## 一、项目整体架构

### 1.1 目录结构分析

Lightning 项目位于 TiDB 仓库的 `lightning/` 目录下，整体结构清晰且模块化：

```
lightning/
├── cmd/                    # 命令行工具入口
│   ├── tidb-lightning/    # 主程序入口
│   └── tidb-lightning-ctl/ # 控制工具
├── pkg/                   # 核心功能包
│   ├── importer/         # 导入控制器
│   ├── server/           # 服务器模式
│   └── web/              # Web界面
├── tests/                # 集成测试
└── web/                  # 前端界面源码
```

核心功能主要集中在 `pkg/lightning/` 包中：

* `backend/`: 后端存储抽象层，支持多种导入模式
* `checkpoints/`: 检查点机制，用于断点续传
* `config/`: 配置管理
* `errormanager/`: 错误处理和冲突解决
* `mydump/`: 数据解析和schema处理
* `common/`: 公共工具函数

## 二、核心导入流程深入分析

### 2.1 主要导入步骤

Lightning 的导入过程有7个步骤：

```
// 来自 import.go 中的 Run 方法
opts := []func(context.Context) error{
    rc.setGlobalVariables,    // 1. 设置全局变量
    rc.restoreSchema,         // 2. 恢复表结构
    rc.preCheckRequirements,  // 3. 预检查要求
    rc.initCheckpoint,        // 4. 初始化检查点
    rc.importTables,          // 5. 导入表数据
    rc.fullCompact,           // 6. 全量压缩
    rc.cleanCheckpoints,      // 7. 清理检查点
}
```

### 2.2 表结构恢复（restoreSchema）

`restoreSchema` 函数是导入流程的第二步，负责在目标数据库中创建所需的表结构：

**主要功能：**

1. **并发DDL执行**: 使用 `SchemaImporter` 并发创建数据库、表和视图
2. **智能重试机制**: 使用 `CREATE IF NOT EXISTS` 处理重复创建
3. **结构信息收集**: 获取创建后的表结构元信息
4. **后端适配**: 为不同后端模式准备必要的ID信息

   ```
   func (rc *Controller) restoreSchema(ctx context.Context) error {
   // 计算并发度，最小为4
   concurrency := max(2*rc.cfg.App.RegionConcurrency, 4)

   // 创建Schema导入器
   schemaImp := mydump.NewSchemaImporter(logger, rc.cfg.TiDB.SQLMode, rc.db, rc.store, concurrency)

   // 执行DDL导入
   err := schemaImp.Run(ctx, rc.dbMetas)

   // 获取表结构信息
   dbInfos, err := rc.preInfoGetter.GetAllTableStructures(ctx)

   // 为local backend设置数据库ID
   if isLocalBackend(rc.cfg) {
       // 获取远程数据库模型并设置ID映射
   }
   return nil
   }
   ```

### 2.3 数据导入（importTables）

![Lightning import process](./img/lightning-import-process.png)

数据导入是整个流程的核心，Lightning 采用了精巧的并发控制策略：

1. **表级并发**: 多个表可以并行导入
2. **引擎级并发**: 每个表的数据被分割为多个引擎并行处理
3. **Chunk级并发**: 每个引擎内的数据块并发写入

## 三、多后端架构设计

### 3.1 Backend 接口抽象

Lightning 通过定义统一的 `Backend` 接口，Lightning 支持多种不同的数据导入策略：

```
type Backend interface {
    Close()
    RetryImportDelay() time.Duration
    ShouldPostProcess() bool

    OpenEngine(ctx context.Context, config *EngineConfig, engineUUID uuid.UUID) error
    CloseEngine(ctx context.Context, config *EngineConfig, engineUUID uuid.UUID) error
    ImportEngine(ctx context.Context, engineUUID uuid.UUID, regionSplitSize, regionSplitKeys int64) error
    CleanupEngine(ctx context.Context, engineUUID uuid.UUID) error
    FlushEngine(ctx context.Context, engineUUID uuid.UUID) error
    FlushAllEngines(ctx context.Context) error
    LocalWriter(ctx context.Context, cfg *LocalWriterConfig, engineUUID uuid.UUID) (EngineWriter, error)
}
```

### 3.2 两种主要后端模式

```
// 第351-445行：Backend模式选择和初始化
switch cfg.TikvImporter.Backend {
case config.BackendTiDB:
    encodingBuilder = tidb.NewEncodingBuilder()
    backendObj = tidb.NewTiDBBackend(ctx, db, cfg, errorMgr)
case config.BackendLocal:
    // Local backend初始化逻辑
    backendObj, err = local.NewBackend(ctx, tls, backendConfig, pdCli.GetServiceDiscovery())
}
```

#### 3.2.1 Local Backend

* **适用场景**: 大规模数据导入，对性能要求极高
* **实现原理**: 直接生成SST文件并通过Ingestion方式导入TiKV
* **优势**: 导入速度最快，资源占用相对较低
* **劣势**: 对集群影响较大，导入期间需要独占使用

local 模式通过本地的 KV 数据库写入数据，生成SST之后，通过 Ingestion API 将数据导入到 TiKV 中，由于数据已经整理好，
绕过了TiDB的处理且是批量写入chunk的形式，因此导入速度较快。

#### 3.2.2 TiDB Backend

* **适用场景**: 小规模数据导入，需要与现有业务共存
* **实现原理**: 通过标准SQL INSERT语句导入数据
* **优势**: 对集群影响最小，支持事务语义
* **劣势**: 导入速度相对较慢

  ```
  // 构建INSERT语句
  func (be *tidbBackend) buildStmt(tableName string, columnNames []string) *strings.Builder {
  switch be.onDuplicate {
  case config.ReplaceOnDup:
      insertStmt.WriteString("REPLACE INTO ")
  case config.IgnoreOnDup:
      insertStmt.WriteString("INSERT IGNORE INTO ")
  case config.ErrorOnDup:
      insertStmt.WriteString("INSERT INTO ")
  }
  }
  ```

### 3.3 引擎管理机制

Lightning 引入了”引擎”(Engine)概念来管理数据导入的生命周期：

```
// 引擎状态转换: OpenedEngine -> ClosedEngine -> Import -> Cleanup
type OpenedEngine struct {
    engine
    tableName string
    config    *EngineConfig
}

type ClosedEngine struct {
    engine
}
```

每个引擎都有唯一的UUID，支持并发操作且状态独立管理。

## 四、检查点与容错机制

### 4.1 检查点系统设计

Lightning 的检查点系统是其可靠性的核心保障，支持任务级、表级、引擎级和Chunk级的细粒度状态管理：

```
type CheckpointStatus uint8

const (
    CheckpointStatusMissing         CheckpointStatus = 0
    CheckpointStatusLoaded          CheckpointStatus = 30
    CheckpointStatusAllWritten      CheckpointStatus = 60
    CheckpointStatusClosed          CheckpointStatus = 90
    CheckpointStatusImp...