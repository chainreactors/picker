---
title: Matano - The Open-Source Security Lake Platform For AWS
url: https://buaq.net/go-130905.html
source: unSafe.sh - 不安全
date: 2022-10-15
fetch_date: 2025-10-03T19:55:03.070222
---

# Matano - The Open-Source Security Lake Platform For AWS

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

![](https://8aqnet.cdn.bcebos.com/bcaae618e84e4c63ad43d2684c1982e4.jpg)

Matano - The Open-Source Security Lake Platform For AWS

Matano is an open source security lake platform for AWS. It lets you ingest petabytes of sec
*2022-10-14 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-130905.htm)
阅读量:37
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqX3w4a55hJEMy-NZgBEQXV6orLxnR9zMqLFoAwGaVr2rIvB9-Fk2tDQKvTsmigZkR0cxrKFvEKOWTKbfH9P8EldUNDj69w-GCkfqORU6Nt05MAlNxvdGMblhjtmMXpG7cTjDVnORQgVLR73y53lG5JPoiEO8clQY4CuBzqtCyd7WT2zpH1qClkuX6Rw/w640-h260/matano.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqX3w4a55hJEMy-NZgBEQXV6orLxnR9zMqLFoAwGaVr2rIvB9-Fk2tDQKvTsmigZkR0cxrKFvEKOWTKbfH9P8EldUNDj69w-GCkfqORU6Nt05MAlNxvdGMblhjtmMXpG7cTjDVnORQgVLR73y53lG5JPoiEO8clQY4CuBzqtCyd7WT2zpH1qClkuX6Rw/s741/matano.png)

Matano is an open source security lake platform for AWS. It lets you ingest petabytes of security and log data from various sources, store and query them in an open [Apache](https://www.kitploit.com/search/label/Apache "Apache") Iceberg data lake, and create Python detections as code for realtime alerting. Matano is *fully serverless* and designed specifically for AWS and focuses on enabling high scale, low cost, and zero-ops. Matano deploys fully into your AWS account.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEghH3oRgeqp6V4_fAgJpLhPQm2l9025YQD8EMo6nlCkJ8CVVPVb4zcpH34m9sMZzSi9Ib-d3PzbN0VkcUj4-aj3DscaFqqFajwB65YGe5gFnpRcQau2t171qCmKXwmGm8Zs-NOUbGuOAn3XQwKT03r3vDISVeVZmngXtJte3dX1MXzd3DJTuSUs_96V4A=w640-h324)](https://blogger.googleusercontent.com/img/a/AVvXsEghH3oRgeqp6V4_fAgJpLhPQm2l9025YQD8EMo6nlCkJ8CVVPVb4zcpH34m9sMZzSi9Ib-d3PzbN0VkcUj4-aj3DscaFqqFajwB65YGe5gFnpRcQau2t171qCmKXwmGm8Zs-NOUbGuOAn3XQwKT03r3vDISVeVZmngXtJte3dX1MXzd3DJTuSUs_96V4A)

## Features

#### Collect data from all your sources

Matano lets you collect log data from sources using [S3](https://github.com/matanolabs/matano "S3") or SQS based ingestion.

#### Ingest, transform, normalize log data

Matano normalizes and transforms your data using [Vector Remap Language (VRL)](https://vector.dev/docs/reference/vrl/ "Vector Remap Language (VRL)"). Matano works with the [Elastic Common Schema (ECS)](https://www.elastic.co/guide/en/ecs/current/index.html "Elastic Common Schema (ECS)") by default and you can define your own schema.

#### Store data in S3 object storage

Log data is always stored in S3 object storage, for cost effective, long term, durable storage.

#### Apache Iceberg Data lake

All data is ingested into an Apache Iceberg based data lake, allowing you to perform ACID transactions, time travel, and more on all your log data. Apache Iceberg is an open table format, so you always **own your own data**, with no vendor lock-in.

#### Serverless

Matano is a fully [serverless](https://www.kitploit.com/search/label/Serverless "serverless") platform, designed for zero-ops and unlimited [elastic](https://www.kitploit.com/search/label/Elastic "elastic") horizontal scaling.

#### Detections as code

Write Python detections to implement realtime [alerting](https://www.kitploit.com/search/label/Alerting "alerting") on your log data.

## Installing

[**View the complete installation instructions.**](https://www.matano.dev/docs/installation "The open-source security lake platform for AWS (20)")

You can install the matano CLI to deploy Matano into your AWS account, and manage your Matano deployment.

### Requirements

* Docker

### Installation

Matano provides [a nightly release](https://github.com/matanolabs/matano/releases/tag/nightly "a nightly release") with the latest prebuilt files to install the Matano CLI on GitHub. You can download and execute these files to install Matano.

For example, to install the Matano CLI for Linux, run:

```
curl -OL https://github.com/matanolabs/matano/releases/download/nightly/matano-linux-x64.sh
```

## Getting started

[**Read the complete docs on getting started**](https://www.matano.dev/docs/getting-started "The open-source security lake platform for AWS (22)").

### Deployment

To get started with Matano, run the `matano init` command. Make sure you have AWS [credentials](https://www.kitploit.com/search/label/Credentials "credentials") in your environment (or in an AWS CLI profile).

The interactive CLI wizard will walk you through getting started by generating an initial [Matano directory](https://www.matano.dev/docs/matano-directory "Matano directory") for you, initializing your AWS account, and deploying Matano into your AWS account.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdUK3Bqj7b8cajuoKx8yCaCWNPO9Kw4z1Viin9wfpjMEY9g69mywobrF4HMDwNQ4EXY6kqnq_6ev83VvRhhJxHENDz1FRUeHx5UkGRaG99-p1uAH8-Y4cAeS5v8yLNoKXrOFnrCsSUo-5X4uVzSbJUsyUy6wxumr-WbLnWRDSS3jbzb8dnQzXHVLVR0Q/w640-h360/matano_9_matano-init.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdUK3Bqj7b8cajuoKx8yCaCWNPO9Kw4z1Viin9wfpjMEY9g69mywobrF4HMDwNQ4EXY6kqnq_6ev83VvRhhJxHENDz1FRUeHx5UkGRaG99-p1uAH8-Y4cAeS5v8yLNoKXrOFnrCsSUo-5X4uVzSbJUsyUy6wxumr-WbLnWRDSS3jbzb8dnQzXHVLVR0Q/s1770/matano_9_matano-init.gif)

Initial deployment takes a few minutes.

## Documentation

[**View our complete documentation.**](https://www.matano.dev/docs "The open-source security lake platform for AWS (26)")

## License

* [Apache-2.0 License](https://github.com/matanolabs/matano/blob/main/LICENSE "Apache-2.0 License")

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj-DaZt9qjgneGKVtokDwUlMsD-thDPFseA82GXz6jz4y7alXG80CkSZhc8DPha4RfvcPdSBtt7gdWGJsp0eZX3yRCk7LPCNTHb1Lx_aALQVd4gnkN_E4YhJl-AtX2ZMNKnKjTyMUfrGgOlp1MUPVyR6STd11WMiYXGG3XZv7gyKlfmMY57brHm1OmFLg=s320)](https://blogger.googleusercontent.com/img/a/AVvXsEj-DaZt9qjgneGKVtokDwUlMsD-thDPFseA82GXz6jz4y7alXG80CkSZhc8DPha4RfvcPdSBtt7gdWGJsp0eZX3yRCk7LPCNTHb1Lx_aALQVd4gnkN_E4YhJl-AtX2ZMNKnKjTyMUfrGgOlp1MUPVyR6STd11WMiYXGG3XZv7gyKlfmMY57brHm1OmFLg)

Matano - The Open-Source Security Lake Platform For AWS
![Matano - The Open-Source Security Lake Platform For AWS](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqX3w4a55hJEMy-NZgBEQXV6orLxnR9zMqLFoAwGaVr2rIvB9-Fk2tDQKvTsmigZkR0cxrKFvEKOWTKbfH9P8EldUNDj69w-GCkfqORU6Nt05MAlNxvdGMblhjtmMXpG7cTjDVnORQgVLR73y53lG5JPoiEO8clQY4CuBzqtCyd7WT2zpH1qClkuX6Rw/s72-w640-c-h260/matano.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/10/matano-open-source-security-lake.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)