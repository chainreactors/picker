---
title: Part 1: A Comparison Between the Pricing Models of Modern Data Warehouses
url: https://buaq.net/go-264638.html
source: unSafe.sh - 不安全
date: 2024-09-29
fetch_date: 2025-10-06T18:21:38.234104
---

# Part 1: A Comparison Between the Pricing Models of Modern Data Warehouses

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/83c4fc3c66e6ebff284abbfcfa0f1fa9.jpg)

Part 1: A Comparison Between the Pricing Models of Modern Data Warehouses

I had a chance to learn more about the up-to-date comparison of data warehouses lately working on my
*2024-9-28 23:45:16
Author: [hackernoon.com(查看原文)](/jump-264638.htm)
阅读量:8
收藏*

---

I had a chance to learn more about the up-to-date comparison of data warehouses lately working on my side projects. It's hard to do benchmarks for databases, but it's harder to do comparisons on their pricing. There are 3 major things you need to consider:

## Considerations

### Storage Cost

Often providers such as Redshift and Snowflake use their proprietary database formats. While the pricing is based on the data volume, it's hard to estimate how much data space you will need before actually using them. However; looking at the storage pricing for [Snowflake](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf?ref=hackernoon.com), [S3](https://aws.amazon.com/s3/pricing/?ref=hackernoon.com), and [BigQuery](https://cloud.google.com/bigquery/pricing?ref=hackernoon.com#storage) the margin is pretty small for the storage.

From Snowflake, we know that the storage cost is usually < 10% of the total cost of data warehouses. Also, the compaction for the files doesn't make a huge difference (~30%) in the storage according to [Clickbench](https://benchmark.clickhouse.com/?ref=hackernoon.com#eyJzeXN0ZW0iOnsiQWxsb3lEQiI6dHJ1ZSwiQWxsb3lEQiAodHVuZWQpIjp0cnVlLCJBdGhlbmEgKHBhcnRpdGlvbmVkKSI6dHJ1ZSwiQXRoZW5hIChzaW5nbGUpIjp0cnVlLCJBdXJvcmEgZm9yIE15U1FMIjp0cnVlLCJBdXJvcmEgZm9yIFBvc3RncmVTUUwiOnRydWUsIkJ5Q29uaXR5Ijp0cnVlLCJCeXRlSG91c2UiOnRydWUsImNoREIgKERhdGFGcmFtZSkiOnRydWUsImNoREIgKFBhcnF1ZXQsIHBhcnRpdGlvbmVkKSI6dHJ1ZSwiY2hEQiI6dHJ1ZSwiQ2l0dXMiOnRydWUsIkNsaWNrSG91c2UgQ2xvdWQgKGF3cykiOnRydWUsIkNsaWNrSG91c2UgQ2xvdWQgKGF3cykgUGFyYWxsZWwgUmVwbGljYXMgT04iOnRydWUsIkNsaWNrSG91c2UgQ2xvdWQgKEF6dXJlKSI6dHJ1ZSwiQ2xpY2tIb3VzZSBDbG91ZCAoQXp1cmUpIFBhcmFsbGVsIFJlcGxpY2EgT04iOnRydWUsIkNsaWNrSG91c2UgQ2xvdWQgKEF6dXJlKSBQYXJhbGxlbCBSZXBsaWNhcyBPTiI6dHJ1ZSwiQ2xpY2tIb3VzZSBDbG91ZCAoZ2NwKSI6dHJ1ZSwiQ2xpY2tIb3VzZSBDbG91ZCAoZ2NwKSBQYXJhbGxlbCBSZXBsaWNhcyBPTiI6dHJ1ZSwiQ2xpY2tIb3VzZSAoZGF0YSBsYWtlLCBwYXJ0aXRpb25lZCkiOnRydWUsIkNsaWNrSG91c2UgKGRhdGEgbGFrZSwgc2luZ2xlKSI6dHJ1ZSwiQ2xpY2tIb3VzZSAoUGFycXVldCwgcGFydGl0aW9uZWQpIjp0cnVlLCJDbGlja0hvdXNlIChQYXJxdWV0LCBzaW5nbGUpIjp0cnVlLCJDbGlja0hvdXNlICh3ZWIpIjp0cnVlLCJDbGlja0hvdXNlIjp0cnVlLCJDbGlja0hvdXNlICh0dW5lZCkiOnRydWUsIkNsaWNrSG91c2UgKHR1bmVkLCBtZW1vcnkpIjp0cnVlLCJDbG91ZGJlcnJ5Ijp0cnVlLCJDcmF0ZURCIjp0cnVlLCJDcnVuY2h5IEJyaWRnZSBmb3IgQW5hbHl0aWNzIChQYXJxdWV0KSI6dHJ1ZSwiRGF0YWJlbmQiOnRydWUsIkRhdGFGdXNpb24gKFBhcnF1ZXQsIHBhcnRpdGlvbmVkKSI6dHJ1ZSwiRGF0YUZ1c2lvbiAoUGFycXVldCwgc2luZ2xlKSI6dHJ1ZSwiQXBhY2hlIERvcmlzIjp0cnVlLCJEcnVpZCI6dHJ1ZSwiRHVja0RCIChEYXRhRnJhbWUpIjp0cnVlLCJEdWNrREIgKFBhcnF1ZXQsIHBhcnRpdGlvbmVkKSI6dHJ1ZSwiRHVja0RCIjp0cnVlLCJFbGFzdGljc2VhcmNoIjp0cnVlLCJFbGFzdGljc2VhcmNoICh0dW5lZCkiOmZhbHNlLCJHbGFyZURCIjp0cnVlLCJHcmVlbnBsdW0iOnRydWUsIkhlYXZ5QUkiOnRydWUsIkh5ZHJhIjp0cnVlLCJJbmZvYnJpZ2h0Ijp0cnVlLCJLaW5ldGljYSI6dHJ1ZSwiTWFyaWFEQiBDb2x1bW5TdG9yZSI6dHJ1ZSwiTWFyaWFEQiI6ZmFsc2UsIk1vbmV0REIiOnRydWUsIk1vbmdvREIiOnRydWUsIk1vdGhlcmR1Y2siOnRydWUsIk15U1FMIChNeUlTQU0pIjp0cnVlLCJNeVNRTCI6dHJ1ZSwiT3hsYSI6dHJ1ZSwiUGFuZGFzIChEYXRhRnJhbWUpIjp0cnVlLCJQYXJhZGVEQiAoUGFycXVldCwgcGFydGl0aW9uZWQpIjp0cnVlLCJQYXJhZGVEQiAoUGFycXVldCwgc2luZ2xlKSI6dHJ1ZSwiUGlub3QiOnRydWUsIlBvbGFycyAoRGF0YUZyYW1lKSI6dHJ1ZSwiUG9zdGdyZVNRTCAodHVuZWQpIjpmYWxzZSwiUG9zdGdyZVNRTCI6dHJ1ZSwiUXVlc3REQiAocGFydGl0aW9uZWQpIjp0cnVlLCJRdWVzdERCIjp0cnVlLCJSZWRzaGlmdCI6dHJ1ZSwiU2luZ2xlU3RvcmUiOnRydWUsIlNub3dmbGFrZSI6dHJ1ZSwiU1FMaXRlIjp0cnVlLCJTdGFyUm9ja3MiOnRydWUsIlRhYmxlc3BhY2UiOnRydWUsIlRlbWJvIE9MQVAgKGNvbHVtbmFyKSI6dHJ1ZSwiVGltZXNjYWxlREIgKGNvbXByZXNzaW9uKSI6dHJ1ZSwiVGltZXNjYWxlREIiOnRydWUsIlVtYnJhIjp0cnVlfSwidHlwZSI6eyJDIjp0cnVlLCJjb2x1bW4tb3JpZW50ZWQiOnRydWUsIlBvc3RncmVTUUwgY29tcGF0aWJsZSI6dHJ1ZSwibWFuYWdlZCI6dHJ1ZSwiZ2NwIjp0cnVlLCJzdGF0ZWxlc3MiOnRydWUsIkphdmEiOnRydWUsIkMrKyI6dHJ1ZSwiTXlTUUwgY29tcGF0aWJsZSI6dHJ1ZSwicm93LW9yaWVudGVkIjp0cnVlLCJDbGlja0hvdXNlIGRlcml2YXRpdmUiOnRydWUsImVtYmVkZGVkIjp0cnVlLCJzZXJ2ZXJsZXNzIjp0cnVlLCJkYXRhZnJhbWUiOnRydWUsImF3cyI6dHJ1ZSwicGFyYWxsZWwgcmVwbGljYXMiOnRydWUsIkF6dXJlIjp0cnVlLCJhbmFseXRpY2FsIjp0cnVlLCJSdXN0Ijp0cnVlLCJzZWFyY2giOnRydWUsImRvY3VtZW50Ijp0cnVlLCJzb21ld2hhdCBQb3N0Z3JlU1FMIGNvbXBhdGlibGUiOnRydWUsInRpbWUtc2VyaWVzIjp0cnVlfSwibWFjaGluZSI6eyIxNiB2Q1BVIDEyOEdCIjp0cnVlLCI4IHZDUFUgNjRHQiI6dHJ1ZSwic2VydmVybGVzcyI6dHJ1ZSwiMTZhY3UiOnRydWUsImM2YS40eGxhcmdlLCA1MDBnYiBncDIiOnRydWUsIkwiOnRydWUsIk0iOnRydWUsIlMiOnRydWUsIlhTIjp0cnVlLCJjNmEubWV0YWwsIDUwMGdiIGdwMiI6dHJ1ZSwiMTkyR0IiOnRydWUsIjI0R0IiOnRydWUsIjM2MEdCIjp0cnVlLCI0OEdCIjp0cnVlLCI3MjBHQiI6dHJ1ZSwiOTZHQiI6dHJ1ZSwiMTQzMEdCIjp0cnVlLCJkZXYiOnRydWUsIjcwOEdCIjp0cnVlLCJjNW4uNHhsYXJnZSwgNTAwZ2IgZ3AyIjp0cnVlLCJBbmFseXRpY3MtMjU2R0IgKDY0IHZDb3JlcywgMjU2IEdCKSI6dHJ1ZSwiYzUuNHhsYXJnZSwgNTAwZ2IgZ3AyIjp0cnVlLCJjNmEuNHhsYXJnZSwgMTUwMGdiIGdwMiI6dHJ1ZSwiY2xvdWQiOnRydWUsImRjMi44eGxhcmdlIjp0cnVlLCJyYTMuMTZ4bGFyZ2UiOnRydWUsInJhMy40eGxhcmdlIjp0cnVlLCJyYTMueGxwbHVzIjp0cnVlLCJTMiI6dHJ1ZSwiUzI0Ijp0cnVlLCIyWEwiOnRydWUsIjNYTCI6dHJ1ZSwiNFhMIjp0cnVlLCJYTCI6dHJ1ZSwiTDEgLSAxNkNQVSAzMkdCIjp0cnVlLCJjNmEuNHhsYXJnZSwgNTAwZ2IgZ3AzIjp0cnVlfSwiY2x1c3Rlcl9zaXplIjp7IjEiOnRydWUsIjIiOnRydWUsIjQiOnRydWUsIjgiOnRydWUsIjE2Ijp0cnVlLCIzMiI6dHJ1ZSwiNjQiOnRydWUsIjEyOCI6dHJ1ZSwic2VydmVybGVzcyI6dHJ1ZSwiZGVkaWNhdGVkIjp0cnVlfSwibWV0cmljIjoic2l6ZSIsInF1ZXJpZXMiOlt0cnVlLHRydWUsdHJ1ZSx0cnVlLHRydWUsdHJ1ZSx0cnVlLHRydWUsdHJ1ZSx0cnVlLHRydWUsdHJ1ZSx0cnVlLHRydWUsdHJ1ZSx0cnVlLHRydWUsdHJ1ZSx0cnVlLHRydWUsdHJ1ZSx0cnVlLHRydWUsdHJ1ZSx0cnVlLHRydWUsdHJ1ZSx0cnVlLHRydWUsdHJ1ZSx0cnVlLHRydWUsdHJ1ZSx0cnVlLHRydWUsdHJ1ZSx0cnVlLHRydWUsdHJ1ZSx0cnVlLHRydWUsdHJ1ZSx0cnVlXX0=).

> If you use Iceberg Tables, you can use the same table in all the data warehouses.

### Compute Cost

Some charge based on the data your query processed, and some charge based on the compute units you use under the hood (warehouse, slot, etc.) The performance for specific operations such as ingestion, transformation, querying small tables vs big tables, and the use of specific SQL syntax such as WINDOW functions has a huge impact on the cost due to the way underlying engines implement them. Also, the performance/cost changes over time with the software updates.

Decoupling storage from computing is important because unless you have an anti-pattern use case, the most expensive pillar (> 90%) is the computing cost in all the data warehouses. While For compute, here is the terminology they use for compute:

|  |  | Data Processing / Price per TB |
| --- | --- | --- |
| [Snowflake](https://buremba.com/blog/part-1-compare-data-warehouse-pricing-model?ref=hackernoon.com#snowflake) | Warehouse ([$2 / hour](https://www.snowflake.com/en/data-cloud/pricing-options/?ref=hackernoon.com)) | - |
| [AWS Athena](https://buremba.com/blog/part-1-compare-data-warehouse-pricing-model?ref=hackernoon.com#aws-athena) | [DPU](https://aws.amazon.com/athena/pricing/?ref=hackernoon.com#SQL_queries_with_Provisioned_Capacity) ($3.6 / hour) | [Data scanned](https://aws.amazon.com/athena/pricing/?ref=hackernoon.com) ($5) |
| [AWS Redshift Serverless](https://buremba.com/blog/part-1-compare-data-warehouse-pricing-model?ref=hackernoon.com#aws-redshift-serverless) | [RPUs](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-capacity.html?ref=hackernoon.com)( $3.65 / hour) | - |
| [Google BigQuery](https://buremba.com/blog/part-1-compare-data-warehouse-pricing-model?ref=hackernoon.com#google-bigquery) | [Slots](https://cloud.google.com/bigquery/docs/slots?ref=ha...