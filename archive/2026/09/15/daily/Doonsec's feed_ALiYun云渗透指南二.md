---
title: ALiYun云渗透指南二
url: https://mp.weixin.qq.com/s/UPypd9ggkFtumcH1oTyMoA
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:02:21.885931
---

# ALiYun云渗透指南二

# ALiYun云渗透指南二

原创

YongYe安全
YongYe安全

YongYe 安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9ianUIMD6icKv8llB4oVbjLOibrS1xxiaaHGKE0rib3wm0yNPHNJj9JxgrFiauvfte5137DsMJBicXIfFJic07ticTNJe81BsofDlw2N8YxicGF5xSricU/640?wx_fmt=png&from=appmsg)

一、OSS

存储桶

```
# 列出所有OSS aliyun oss ls      # (ossutil 1.0)aliyun ossutil ls  # (ossutil 2.0)
# 查询桶描述信息aliyun ossutil stat oss://examplebucket
# 查询桶加密配置aliyun ossutil api get-bucket-encryption --bucket examplebucket
# 查询桶日志配置aliyun ossutil api get-bucket-logging --bucket examplebucket
# 上传文件（下载反过来）aliyun ossutil cp D:/examplefile.txt oss://examplebucket/desfolder/
# 上传多个指定类型文件aliyun ossutil cp -r D:/localfolder/ oss://examplebucket/desfolder/ --include "*.txt"
```

GUI浏览桶：

```
https://gosspublic.alicdn.com/oss-browser2-prod/2.1.1/oss-browser2-win-x64-2.1.1.exe?spm=a2c4g.11186623.0.0.6ac566d2EVPFQB&file=oss-browser2-win-x64-2.1.1.exe
```

Tips:

      垃圾浏览器，经常崩溃。

二、RDS

数据库

```
# 查询所有RDS实例aliyun rds DescribeDBInstances
# 查询RDS账号列表aliyun rds DescribeAccounts --DBInstanceId rm-xxx
# 查询RDS连接白名单aliyun rds DescribeDBInstanceIPArrayList --DBInstanceId rm-xxx
# 查询所有Redis实例aliyun r-kvstore DescribeInstances
# 查询所有MongoDB aliyun dds DescribeDBInstances
```

三、云万网

域名管理

```
# 列出注册域名aliyun domain query-domain-list --page-num 1 --page-size 100 --endpoint domain.aliyuncs.com
# 列出托管域名aliyun alidns describe-domains --page-num 1 --page-size 100 --endpoint alidns.aliyuncs.comaliyun alidns DescribeDomains
# 查询DNS 解析记录aliyun alidns DescribeDomainRecords --DomainName example.com
```

四、负载均衡

阿里云目前提供四种负载均衡产品

|  |  |  |  |
| --- | --- | --- | --- |
| 产品类型 | 产品全称 | CLI 产品名 | 适用场景 |
| CLB | 传统型负载均衡 | slb | 基础的四层（TCP/UDP）和七层（HTTP/HTTPS）负载均衡 |
| ALB | 应用型负载均衡 | alb | 专门面向七层（HTTP/HTTPS/QUIC）业务，支持复杂路由 |
| NLB | 网络型负载均衡 | nlb | 面向四层（TCP/UDP）业务，超高性能，海量并发 |
| GWLB | 网关型负载均衡 | gwlb | 适用于部署和扩展第三方网络虚拟设备 |

```
# 查看 CLB 实例列表aliyun slb describe-load-balancers aliyun slb DescribeLoadBalancers
# 查看 ALB 实例列表aliyun alb list-load-balancers
# 查看 NLB 实例列表aliyun nlb list-load-balancers
# 查看 GWLB 实例列表aliyun gwlb list-load-balancers
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hQV3W3SWhZAwUWpmzrCgaEq3yIVNGsdtiaCricBe5xUlkBw5m3TNEvfMRPllKCIZqmMKb4Yfr4b6QI1bCw8ZKXibw/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/hQV3W3SWhZCTC9c0yiaUnUquODcTh2sUwZp89npoZPB117ibnk7aibXo51yBMT5nyNjxNFP5GXvdJFhSrX1M14CcA/0?wx_fmt=png)

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