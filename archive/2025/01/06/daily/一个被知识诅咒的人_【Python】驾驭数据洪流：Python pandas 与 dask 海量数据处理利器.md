---
title: 【Python】驾驭数据洪流：Python pandas 与 dask 海量数据处理利器
url: https://blog.csdn.net/nokiaguy/article/details/144943566
source: 一个被知识诅咒的人
date: 2025-01-06
fetch_date: 2025-10-06T20:07:19.831186
---

# 【Python】驾驭数据洪流：Python pandas 与 dask 海量数据处理利器

# 【Python】驾驭数据洪流：Python pandas 与 dask 海量数据处理利器

原创
已于 2025-01-09 16:45:13 修改
·
1.2k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

10

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

27
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#pandas](https://so.csdn.net/so/search/s.do?q=pandas&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2025-01-05 12:30:46 首次发布

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Python杂谈
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12800257.html "Python杂谈")

390 篇文章

订阅专栏

随着数据爆炸式增长，传统数据处理工具在面对海量数据时常常捉襟见肘。本文深入探讨了 Python 中两个强大的数据处理库：`pandas` 和 `dask`，阐述了它们各自的优势和适用场景，并详细介绍了如何结合使用它们来高效处理和分析大数据集。`pandas` 提供了易于使用的数据结构和数据分析工具，适用于内存可容纳的中小型数据集。而 `dask` 则通过并行计算扩展了 `pandas` 的能力，使其能够处理超出内存限制的大型数据集。本文将通过丰富的代码示例和实际应用场景，演示如何使用这两个库进行数据加载、清洗、转换、分析和可视化，并提供优化数据处理性能的策略，帮助读者更好地驾驭数据洪流。

### 正文：

#### 1. 引言

大数据时代，数据量呈指数级增长，传统的数据处理方法面临严峻挑战。Python 作为一种功能强大的编程语言，拥有丰富的数据处理库，其中 `pandas` 和 `dask` 是处理大数据集的两把利器。`pandas` 提供了高效的数据结构和数据分析工具，适用于内存可容纳的中小型数据集。而 `dask` 则通过并行计算扩展了 `pandas` 的能力，使其能够处理超出内存限制的大型数据集。本文将深入探讨这两个库的特性和用法，并结合实际案例，演示如何使用它们高效处理海量数据。

#### 2. `pandas`：灵活高效的数据分析工具

`pandas` 是一个基于 NumPy 的开源数据分析库，提供了高性能、易于使用的数据结构和数据分析工具。其核心数据结构是 Series（一维数据）和 DataFrame（二维表格数据）。

##### 2.1 `pandas` 数据结构

* **Series：** 类似于一维数组，由一组数据和一组与之相关的索引组成。

```
import pandas as pd

# 创建一个 Series
s = pd.Series([1, 3, 5, 7, 9], index=['a', 'b', 'c', 'd', 'e'])
print(s)

# 访问 Series 中的元素
print(s['b'])  # 输出：3

# 切片操作
print(s['b':'d'])
```

* **DataFrame：** 类似于二维表格，由多个 Series 组成，共享相同的索引。

```
# 创建一个 DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
print(df)

# 访问 DataFrame 中的列
print(df['Name'])

# 访问 DataFrame 中的行
print(df.loc[0])

# 条件筛选
print(df[df['Age'] > 26])
```

##### 2.2 `pandas` 常用操作

* **数据读取：** `pandas` 支持多种数据格式的读取，如 CSV、Excel、SQL 数据库等。

```
# 读取 CSV 文件
df = pd.read_csv('data.csv')

# 读取 Excel 文件
df = pd.read_excel('data.xlsx')
```

* **数据清洗：** 包括处理缺失值、重复值、异常值等。

```
# 处理缺失值
df.fillna(0)  # 用 0 填充缺失值
df.dropna()   # 删除包含缺失值的行

# 处理重复值
df.drop_duplicates()
```

* **数据转换：** 包括数据类型转换、重塑、合并等。

```
# 数据类型转换
df['Age'] = df['Age'].astype(int)

# 数据重塑
df.pivot(index='Name', columns='City', values='Age')

# 数据合并
pd.merge(df1, df2, on='key')
```

* **数据分析：** 包括统计分析、分组聚合等。

```
# 统计描述
df.describe()

# 分组聚合
df.groupby('City')['Age'].mean()
```

#### 3. `dask`：扩展 `pandas` 的并行计算能力

`dask` 是一个灵活的并行计算库，可以将 `pandas`、NumPy 等库扩展到大规模数据集的处理。`dask` 提供了两种核心数据结构：`dask.array` 和 `dask.dataframe`。

##### 3.1 `dask.dataframe`

`dask.dataframe` 是一个基于 `pandas` DataFrame 的分布式数据结构，可以将大型数据集分成多个小的 `pandas` DataFrame，并在多个 CPU 或集群上并行处理。

```
import dask.dataframe as dd

# 读取大型 CSV 文件
ddf = dd.read_csv('large_data.csv')

# 执行与 pandas 类似的操作
print(ddf.head())
print(ddf['column_name'].mean().compute()) # 使用.compute()触发计算
```

##### 3.2 `dask` 的核心概念

* **延迟计算：** `dask` 采用延迟计算的方式，只有在调用 `compute()` 方法时才会真正执行计算，这使得 `dask` 可以高效地处理大型数据集。
* **任务调度：** `dask` 可以将计算任务分解成小的任务，并在多个 CPU 或集群上并行执行。

##### 3.3 `dask` 与 `pandas` 的结合使用

`dask` 可以很好地与 `pandas` 结合使用，例如可以使用 `dask` 读取大型数据集，然后使用 `pandas` 进行局部处理。

```
import pandas as pd
import dask.dataframe as dd

# 读取大型 CSV 文件
ddf = dd.read_csv('large_data.csv')

# 对每个分区应用 pandas 函数
def process_partition(df):
    # 在这里使用 pandas 进行数据处理
    return df.groupby('category')['value'].sum()

result = ddf.map_partitions(process_partition).compute()
print(result)
```

#### 4. 海量数据处理策略

* **数据分块：** 将大型数据集分成多个小的块，分别加载和处理。
* **使用合适的数据类型：** 选择合适的数据类型可以减少内存占用。例如，可以使用 `int8` 代替 `int64`，如果数值范围允许的话。
* **避免不必要的数据复制：** 尽量使用原地操作，避免创建大量中间变量。
* **使用 `dask` 进行并行计算：** 对于超出内存限制的数据集，使用 `dask` 进行并行计算可以显著提高处理效率。
* **优化 I/O 操作：** 使用高效的文件格式（如 Parquet、HDF5）和压缩算法可以减少 I/O 时间。
* **内存管理：** 监控内存使用情况，避免内存溢出。可以使用 Python 的 `gc` 模块进行垃圾回收。

#### 5. 案例分析：处理大型日志文件

假设我们有一个大型的 Web 服务器日志文件，需要分析用户的访问行为。日志文件包含以下字段：

* `timestamp`：访问时间戳
* `user_id`：用户 ID
* `url`：访问 URL
* `status_code`：HTTP 状态码
* `bytes_sent`：发送的字节数

日志文件大小为 10GB，无法一次性加载到内存中。我们可以使用 `dask` 和 `pandas` 来处理这个日志文件。

```
import dask.dataframe as dd
import pandas as pd

# 读取日志文件
ddf = dd.read_csv('web_server_log.csv',
                    parse_dates=['timestamp'], # 解析时间戳
                    dtype={'user_id': 'int32', 'status_code': 'int16', 'bytes_sent': 'int32'}, # 指定数据类型
                    blocksize="64MB") #指定每个分块的大小

# 统计每个用户的访问次数
user_access_count = ddf.groupby('user_id').size().compute()
print("每个用户的访问次数：\n",user_access_count.head())

# 统计不同状态码的出现次数
status_code_count = ddf['status_code'].value_counts().compute()
print("\n不同状态码的出现次数：\n",status_code_count)

# 统计每天的总流量
ddf['date'] = ddf['timestamp'].dt.date
daily_traffic = ddf.groupby('date')['bytes_sent'].sum().compute()
print("\n每天的总流量：\n",daily_traffic)

# 计算平均每次请求发送的字节数，并按状态码分组
def average_bytes(df):
    if len(df) == 0:  # 处理空分区的情况
        return pd.Series([], dtype='float64')
    return (df['bytes_sent'].sum() / len(df)).round(2)

average_bytes_by_status = ddf.groupby('status_code').apply(average_bytes, meta=('average_bytes', 'float64')).compute()
print("\n按状态码分组的平均字节数：\n",average_bytes_by_status)

# 找出访问量最多的前10个URL
top_10_urls = ddf['url'].value_counts().nlargest(10).compute()
print("\n访问量最多的前10个URL：\n",top_10_urls)

# 找出某个时间段内的访问记录，例如 2024年1月1日到2024年1月7日
start_date = pd.to_datetime('2024-01-01').date()
end_date = pd.to_datetime('2024-01-07').date()

date_range_access = ddf[(ddf['date'] >= start_date) & (ddf['date'] <= end_date)].compute()
print(f"\n{start_date} 到 {end_date} 之间的访问记录前5条：\n",date_range_access.head())

# 计算某个用户的平均访问间隔 (需要数据有序，这里假设数据已按时间戳排序)
def average_time_between_visits(df):
    if len(df) < 2:
        return pd.Timedelta(0)
    time_diffs = df['timestamp'].diff().dropna()
    return time_diffs.mean()

ddf = ddf.sort_values('timestamp') # 确保时间戳有序
average_interval_by_user = ddf.groupby('user_id').apply(average_time_between_visits, meta=('average_interval', 'timedelta64[ns]')).compute()
print("\n每个用户的平均访问间隔：\n", average_interval_by_user.head())
```

**代码解释和改进：**

1. **数据类型指定：** 在 `read_csv` 中使用 `dtype` 参数指定数据类型，可以显著减少内存占用。例如，将 `user_id` 指定为 `int32`，`status_code` 指定为 `int16`。
2. **`blocksize` 参数：** 使用 `blocksize` 参数可以控制 `dask` 读取文件的块大小，这对于性能优化非常重要。通常建议设置为 64MB 或 128MB。
3. **时间戳解析：** 使用 `parse_dates` 参数可以自动解析时间戳列，避免后续手动转换。
4. **`apply` 方法和 `meta` 参数：** 在 `groupby` 之后使用 `apply` 方法时，需要使用 `meta` 参数指定返回值的类型，这对于 `dask` 的正确执行至关重要。否则Dask无法推断输出的类型，会报错。
5. **空分区处理：** 在 `average_bytes` 函数中添加了对空分区的处理，避免出现除以零的错误。
6. **时间序列操作：** 增加了计算用户平均访问间隔的示例，并使用 `sort_values` 确保时间戳有序，这对于时间序列分析非常重要。
7. **数据过滤:** 增加了一个按日期范围过滤数据的例子，演示如何使用布尔索引进行数据筛选。
8. **输出结果的head()**: 为了防止结果输出过多，对于较大的结果，使用`.head()`方法只输出前几行。

通过以上改进，代码更加健壮、高效，并且能够处理更复杂的数据分析任务。

#### 6. 总结

本文详细介绍了如何使用 `pandas` 和 `dask` 处理海量数据。`pandas` 提供了易于使用的数据结构和数据分析工具，适用于内存可容纳的中小型数据集。`dask` 则通过并行计算扩展了 `pandas` 的能力，使其能够处理超出内存限制的大型数据集。通过结合使用这两个库，我们可以高效地处理和分析海量数据，从而更好地挖掘数据中的价值。在实际应用中，需要根据具体的数据集和分析任务选择合适的工具和策略，并不断优化代码以提高性能。

希望这篇文章能够帮助读者更好地理解和使用 `pandas` 和 `dask`，并在大数据处理的道路上更进一步。

关注博主即可阅读全文
![](https://csdnimg.cn/release/blogv2/dist/pc/img/arrowDownAttend.png)

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newWhite.png)

确定要放弃本次机会？

福利倒计时

*:*

*:*

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-roup.png)
立减 ¥

普通VIP年卡可用

[立即使用](https://mall.csdn.net/vip)

[![](https://profile-avatar.csdnimg.cn/2ccacbf1fc8347338ede60bde...