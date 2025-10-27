---
title: Deep Dive into SeaTunnel Databend Sink Connector CDC Implementation
url: https://cloudsjhan.github.io/2025/08/18/Deep-Dive-into-SeaTunnel-Databend-Sink-Connector-CDC-Implementation/
source: cloud world
date: 2025-08-19
fetch_date: 2025-10-07T00:15:35.957266
---

# Deep Dive into SeaTunnel Databend Sink Connector CDC Implementation

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## Deep Dive into SeaTunnel Databend Sink Connector CDC Implementation

posted

2025-08-18

|

in

[Databend](/categories/Databend/)

|

visitors:

|

|

wordcount:

1,197
|

min2read ≈

7

![](https://)

# Deep Dive into SeaTunnel Databend Sink Connector CDC Implementation

## Background

[Databend](https://github.com/databendlabs/databend) is an AI-native data warehouse optimized for analytical workloads with a columnar storage architecture, serving as an open-source alternative to Snowflake. When handling CDC (Change Data Capture) scenarios, executing individual UPDATE and DELETE operations severely impacts performance and fails to leverage Databend’s batch processing advantages.

Before [PR #9661](https://github.com/apache/seatunnel/pull/9661), SeaTunnel’s Databend sink connector only supported batch INSERT operations, lacking efficient handling of UPDATE and DELETE operations in CDC scenarios. This limitation restricted its application in real-time data synchronization scenarios.

## Core Challenges

CDC scenarios present the following main challenges:

1. **Performance Bottleneck**: Executing individual UPDATE/DELETE operations generates excessive network round-trips and transaction overhead
2. **Resource Consumption**: Frequent single operations cannot utilize Databend’s columnar storage advantages
3. **Data Consistency**: Ensuring the order and completeness of change operations
4. **Throughput Limitation**: Traditional approaches struggle with high-concurrency, large-volume CDC event streams

## Solution Architecture

### Overall Design Approach

The new CDC mode achieves high-performance data synchronization through the following innovative design:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` graph LR     A[CDC Data Source] --> B[SeaTunnel]     B --> C[Raw Table]     C --> D[Databend Stream]     D --> E[MERGE INTO Operation]     E --> F[Target Table] ``` |

### Core Components

#### 1. CDC Mode Activation Mechanism

When users specify the `conflict_key` parameter in configuration, the connector automatically switches to CDC mode:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` | ``` sink {   Databend {     url = "jdbc:databend://databend:8000/default?ssl=false"     user = "root"     password = ""     database = "default"     table = "sink_table"          # Enable CDC mode     batch_size = 100     conflict_key = "id"     allow_delete = true   } } ``` |

#### 2. Raw Table Design

The system automatically creates a temporary raw table to store CDC events:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` CREATE TABLE IF NOT EXISTS raw_cdc_table_${target_table} (     id VARCHAR,                    -- Primary key identifier     table_name VARCHAR,            -- Target table name     raw_data JSON,                 -- Complete row data (JSON format)     add_time TIMESTAMP,            -- Event timestamp     action VARCHAR                 -- Operation type: INSERT/UPDATE/DELETE ) ``` |

#### 3. Stream Mechanism

Leveraging [Databend Stream](https://docs.databend.com/sql/sql-commands/ddl/stream/) functionality to monitor raw table changes:

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` CREATE STREAM IF NOT EXISTS stream_${target_table}  ON TABLE raw_cdc_table_${target_table} ``` |

Stream advantages:

* **Incremental Processing**: Only processes new change records
* **Transaction Guarantee**: Ensures no data loss
* **Efficient Querying**: Avoids full table scans

#### 4. Two-Phase Processing Model

**Phase 1: Data Writing**

* SeaTunnel writes all CDC events (INSERT/UPDATE/DELETE) to the raw table in JSON format
* Supports batch writing for improved throughput

**Phase 2: Merge Processing**

* Periodically executes [MERGE INTO](https://docs.databend.com/sql/sql-commands/dml/dml-merge) operations based on SeaTunnel AggregatedCommitter
* Merges data from raw table to target table

### MERGE INTO Core Logic

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` | ``` MERGE INTO target_table AS t USING (     SELECT          raw_data:column1::VARCHAR AS column1,         raw_data:column2::INT AS column2,         raw_data:column3::TIMESTAMP AS column3,         action,         id     FROM stream_${target_table}     QUALIFY ROW_NUMBER() OVER(         PARTITION BY _id          ORDER BY _add_time DESC     ) = 1  ) AS s ON t.id = s.id WHEN MATCHED AND s._action = 'UPDATE' THEN      UPDATE SET * WHEN MATCHED AND s._action = 'DELETE' THEN      DELETE WHEN NOT MATCHED AND s._action != 'DELETE' THEN      INSERT * ``` |

## Implementation Details

### Key Code Implementation

Based on [PR #9661](https://github.com/apache/seatunnel/pull/9661) implementation, the main core classes involved are:

#### DatabendSinkWriter Enhancement

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``` | ``` public class DatabendSinkWriter extends AbstractSinkWriter<SeaTunnelRow, DatabendWriteState> {          private boolean cdcMode;     private String rawTableName;     private String streamName;     private ScheduledExecutorService mergeExecutor;          @Override     public void write(SeaTunnelRow element) throws IOException {         if (cdcMode) {             // CDC mode: write to raw table             writeToRawTable(element);         } else {             // Normal mode: write directly to target table             writeToTargetTable(element);         }     }        private void performMerge(List<DatabendSinkAggregatedCommitInfo> aggregatedCommitInfos) {         // Merge all data from raw table to target table         String mergeSql = generateMergeSql();         log.info("[Instance {}] Executing MERGE INTO statement: {}", instanceId, mergeSql);          try (Statement stmt = connection.createStatement()) {             stmt.execute(mergeSql);             log.info("[Instance {}] Merge operation completed successfully", instanceId);         } catch (SQLException e) {             log.error(                     "[Instance {}] Failed to execute merge operation: {}",                     instanceId,                     e.getMessage(),                     e);             throw new DatabendConnectorException(                     DatabendConnectorErrorCode.SQL_OPERATION_FAILED,                     "Failed to execute merge operation: " + e.getMessage(),                     e);         }     } } ``` |

#### Configuration Options Extension

New CDC-related configurations in `DatabendSinkOptions`:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` public class DatabendSinkOptions {     public static final Option<String> CONFLICT_KEY =             Options.key("conflict_key")                     .stringType()                     .noDefaultValue()                     .withDescription("Conflict key for CDC merge operations");      public static final Option<Boolean> ALLOW_DELETE =             Options.key("allow_delete")                     .booleanType()                     .defaultValue(false)                     .withDescription("Whether to allow delete operations in CDC mode"); } ``` |

### Batch Processing Optimization Strategy

The system employs a dual-trigger mechanism for executing MERGE operations:

1. **Quantity-based**: Triggers when accumulated CDC events reach `batch_size`
2. **Time-based**: Triggers when SeaTunnel’s checkpoint.interval is reached

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` if (isCdcMode && shouldPerformMerge()) {     performMerge(aggregatedCommitInfos); } ``` |

## Performance Advantages

### 1. Batch Processing Optimization

* **Traditional Approach**: 1000 updates = 1000 network round-trips
* **CDC Mode**: 1000 updates = 1 batch write + 1 MERGE operation

### 2. Columnar Storage Utilization

* MERGE INTO operations fully leverage Databend’s columnar st...